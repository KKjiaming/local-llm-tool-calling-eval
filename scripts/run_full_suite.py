"""Sequential three-model full-category evaluation, with owned-server cleanup."""
import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MODELS = [
    ("Qwen/Qwen3.5-9B", "Qwen3.5-9B", "qwen9b", "configs/full-single-turn-qwen.json"),
    ("Qwen/Qwen3.8-27B", "Qwen3.8-27B", "qwen27b", "configs/full-single-turn-qwen.json"),
    ("google/gemma-4-26B-A4B-it", "Gemma4-26B-A4B-it", "gemma4", "configs/full-single-turn-gemma.json"),
]


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def stop_owned_server(server):
    if server.poll() is not None:
        return
    # start_new_session gives only this server and its children a private group.
    for sig, timeout in [(signal.SIGINT, 90), (signal.SIGTERM, 20), (signal.SIGKILL, 10)]:
        try:
            os.killpg(server.pid, sig)
            server.wait(timeout=timeout)
            return
        except ProcessLookupError:
            return
        except subprocess.TimeoutExpired:
            continue
    raise RuntimeError("Owned server did not shut down")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=Path, default=ROOT / "configs/datasets/full_single_turn.jsonl")
    parser.add_argument("--name", default="full-single-turn-20261005")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if not args.name.replace("-", "").replace("_", "").isalnum():
        raise ValueError("Invalid suite name")
    dataset = args.dataset.resolve()
    dataset_manifest = json.loads(dataset.with_suffix(".manifest.json").read_text())
    assert hashlib.sha256(dataset.read_bytes()).hexdigest() == dataset_manifest["sha256"]
    state_path = ROOT / "records" / (args.name + "-status.json")
    lock_handle = (ROOT / "records" / (args.name + ".lock")).open("a")
    try:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise RuntimeError("This suite already has a running controller") from None
    if state_path.exists() and not args.resume:
        raise RuntimeError("Suite exists; use --resume to retain existing attempts")
    state = {"name": args.name, "controller_pid": os.getpid(), "start_utc": utc(),
             "status": "running", "dataset": dataset_manifest, "models": {}}
    if args.resume and state_path.exists():
        previous = json.loads(state_path.read_text())
        assert previous["dataset"] == dataset_manifest
        state["models"] = previous["models"]
        state["previous_start_utc"] = previous["start_utc"]
    def save():
        temporary = state_path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(state, indent=2) + "\n")
        temporary.replace(state_path)
        # Update only the explicitly reserved block, preserving README prose.
        if dataset_manifest["scope"] == "single_turn":
            readme = ROOT / "README.md"
            text = readme.read_text()
            begin, end = "<!-- FULL_RUN_STATUS_START -->", "<!-- FULL_RUN_STATUS_END -->"
            if text.count(begin) == text.count(end) == 1:
                table = [f"Full suite `{args.name}`: **{state['status']}**. Latest recorded update: {utc()}.", "",
                         "| Model | Stage | Completed-run accuracy | Mean request latency |",
                         "|---|---|---:|---:|"]
                for model_id, _, _, _ in MODELS:
                    item = state["models"].get(model_id, {"status": "pending"})
                    summary = item.get("summary") if item["status"] == "completed" else None
                    accuracy = f"{summary['correct']}/{summary['n']} ({summary['accuracy_attempted']:.2%})" if summary else "—"
                    latency = f"{summary['latency_completed_seconds']['mean']:.3f} s" if summary else "—"
                    table.append(f"| {model_id} | {item['status']} | {accuracy} | {latency} |")
                table += ["", "Coverage: all 13 single-turn categories; not the complete BFCL v4 overall score.",
                          "Native thinking defaults and vLLM versions differ; latency is configuration-specific."]
                head, rest = text.split(begin)
                _, tail = rest.split(end)
                updated = head + begin + "\n" + "\n".join(table) + "\n" + end + tail
                temporary_readme = ROOT / "README.md.tmp"
                temporary_readme.write_text(updated)
                temporary_readme.replace(readme)
    def execute(command, log_path):
        with log_path.open("a") as log:
            subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    save()
    output_runs = []
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        for model, folder, short, config_name in MODELS:
            config = json.loads((ROOT / config_name).read_text())
            assert config["categories"] == list(dataset_manifest["categories"])
            run_name = f"{short}-{args.name}"
            output = ROOT / "results" / run_name
            output_runs.append(output)
            stage = state["models"].setdefault(model, {"run_dir": str(output.relative_to(ROOT))})
            stage.update({"status": "starting", "start_utc": utc()})
            save()
            run_is_complete = False
            if output.exists():
                previous_run = json.loads((output / "run.json").read_text())
                if previous_run["model"] != model or previous_run["config"] != config or previous_run["split_sha256"] != dataset_manifest["sha256"]:
                    raise ValueError("Existing model run differs from the frozen suite")
                run_is_complete = previous_run["status"].startswith("completed")
            if not run_is_complete:
                server = None
                server_log = ROOT / "records" / (run_name + "-server.log")
                try:
                    with server_log.open("a") as log:
                        server = subprocess.Popen([str(ROOT / config["server"]["python_environment"] / "bin/python"),
                            str(ROOT / "scripts/serve_model.py"), "--model", model,
                            "--model-path", str(ROOT / "incoming" / folder), "--config", str(ROOT / config_name)],
                            cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                    stage["owned_server_pid"] = server.pid
                    save()
                    deadline = time.monotonic() + 1200
                    while True:
                        if server.poll() is not None:
                            raise RuntimeError(f"Model server exited; see {server_log.name}")
                        try:
                            with opener.open(f"http://127.0.0.1:{config['server']['port']}/v1/models", timeout=3) as response:
                                ready = model in {m["id"] for m in json.load(response)["data"]}
                            if ready:
                                break
                        except (urllib.error.URLError, TimeoutError):
                            pass
                        if time.monotonic() >= deadline:
                            raise TimeoutError("Model server startup exceeded 20 minutes")
                        time.sleep(2)
                    stage["status"] = "generating"
                    save()
                    command = [str(ROOT / ".venv-eval/bin/python"), str(ROOT / "scripts/run_subset.py"),
                        "--model", model, "--dataset", str(dataset), "--run-name", run_name,
                        "--config", str(ROOT / config_name)]
                    if output.exists():
                        command.append("--resume")
                    execute(command, ROOT / "records" / (run_name + "-generation.log"))
                finally:
                    if server is not None:
                        stop_owned_server(server)
                    stage["server_stopped_utc"] = utc()
                    save()
            stage["status"] = "scoring"
            save()
            for script in ["score_subset.py", "export_result_table.py"]:
                execute([str(ROOT / ".venv-eval/bin/python"), str(ROOT / "scripts" / script), str(output)],
                        ROOT / "records" / (run_name + "-scoring.log"))
            stage.update({"status": "completed", "end_utc": utc(),
                          "summary": json.loads((output / "summary.json").read_text())})
            save()
            print(f"{model}: {stage['summary']['correct']}/{stage['summary']['n']} completed", flush=True)
        for script in ["compare_runs.py", "plot_results.py"]:
            execute([str(ROOT / ".venv-eval/bin/python"), str(ROOT / "scripts" / script),
                     *map(str, output_runs), "--output", str(ROOT / "reports" / args.name)],
                    ROOT / "records" / (args.name + "-report.log"))
        state["status"] = "completed"
    except BaseException as error:
        state.update({"status": "incomplete", "error": type(error).__name__ + ": " + str(error)})
        raise
    finally:
        state["end_utc"] = utc()
        save()


if __name__ == "__main__":
    main()
