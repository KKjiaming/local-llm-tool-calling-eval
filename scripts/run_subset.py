"""Serial local FC requests, raw output and sampled GPU metrics. No remote API."""
import argparse
import copy
import datetime
import hashlib
import json
import os
import pathlib
import subprocess
import threading
import time
import urllib.error
import urllib.request
from experiment_io import input_path

ROOT = pathlib.Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--split", choices=["smoke", "dev", "test"])
    source.add_argument("--dataset", type=pathlib.Path)
    p.add_argument("--run-name", required=True)
    p.add_argument("--config", type=pathlib.Path, default=ROOT / "configs/full-single-turn-qwen.json")
    p.add_argument("--resume", action="store_true", help="Keep every recorded attempt; run only IDs not yet attempted")
    args = p.parse_args()
    config = json.loads(args.config.read_text())
    if (args.split == "test" or args.dataset) and config["status"] != "frozen_after_smoke_validation":
        raise RuntimeError("Formal test requires a validated and frozen configuration")
    if not args.run_name.replace("-", "").replace("_", "").isalnum():
        raise ValueError("run-name must contain only letters, numbers, underscore and dash")
    out = ROOT / "results" / args.run_name
    if args.resume and not out.exists():
        raise RuntimeError("Resume requires an existing run")
    out.mkdir(parents=True, exist_ok=args.resume)
    os.environ["BFCL_PROJECT_ROOT"] = str(out)
    from bfcl_eval.constants.enums import ModelStyle
    from bfcl_eval.constants.type_mappings import GORILLA_TO_OPENAPI
    from bfcl_eval.model_handler.utils import convert_to_tool
    split_path = args.dataset.resolve() if args.dataset else ROOT / "configs/splits" / f"{args.split}.jsonl"
    rows = [json.loads(line) for line in split_path.read_text().splitlines()]
    ids = [row["entry"]["id"] for row in rows]
    if len(ids) != len(set(ids)) or any(len(row["entry"]["question"]) != 1 for row in rows):
        raise ValueError("Expected unique single-turn cases")
    if set(row["category"] for row in rows) != set(config["categories"]):
        raise ValueError("Dataset categories must exactly match the recorded configuration")
    metadata = json.loads((ROOT / "records" / (args.model.replace("/", "--") + ".json")).read_text())
    manifest = {"model": args.model, "model_revision": metadata["revision"], "split": args.split or split_path.stem,
        "split_sha256": hashlib.sha256(split_path.read_bytes()).hexdigest(),
        "config": config, "start_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "running", "adaptation": None, "expected_n": len(rows)}
    if args.dataset:
        manifest["dataset_path"] = str(split_path.relative_to(ROOT))
    input_path(manifest)
    manifest["chat_template_kwargs"] = {}
    manifest["native_template_defaults"] = {"enable_thinking": not args.model.startswith("google/gemma-4-")}
    recorded = []
    if args.resume:
        previous = json.loads((out / "run.json").read_text())
        for key in ("model", "model_revision", "split", "split_sha256", "config", "adaptation"):
            if previous[key] != manifest[key]:
                raise ValueError(f"Resume configuration differs: {key}")
        raw_path = out / "raw.jsonl"
        recorded = [json.loads(line) for line in raw_path.read_text().splitlines()] if raw_path.exists() else []
        done_ids = [row["id"] for row in recorded]
        if len(done_ids) != len(set(done_ids)) or done_ids != ids[:len(done_ids)]:
            raise ValueError("Recorded attempts are not a unique prefix of the frozen dataset")
        if len(recorded) == len(rows):
            print("Every case already attempted; existing outputs retained", flush=True)
            return
        manifest = previous
        manifest["status"] = "running"
        manifest.setdefault("resume_events", []).append({"start_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                                        "already_attempted": len(recorded), "retry_existing_attempts": False})
    (out / "run.json").write_text(json.dumps(manifest, indent=2))
    stop = threading.Event()
    def monitor():
        with (out / "gpu_samples.jsonl").open("a" if args.resume else "w") as f:
            while not stop.is_set():
                tick = time.time()
                command = subprocess.run(["nvidia-smi", "--query-gpu=index,memory.used,utilization.gpu,power.draw", "--format=csv,noheader,nounits"], capture_output=True, text=True)
                sample = {"time_unix": tick, "raw_csv": command.stdout, "exit_code": command.returncode}
                f.write(json.dumps(sample) + "\n")
                f.flush()
                stop.wait(0.5)
    thread = threading.Thread(target=monitor, daemon=True)
    # Disable proxy for local inference. Never reads auth files or uses remote API keys.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    url = f"http://127.0.0.1:{config['server']['port']}/v1/chat/completions"
    def query(body):
        request = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
        with opener.open(request, timeout=config["timeout_seconds"]) as response:
            raw = response.read().decode()
            return raw, json.loads(raw)
    # Synthetic warmups are outside BFCL evaluation and timing summary.
    warm = {"model": args.model, "messages": [{"role": "user", "content": "Call ping with value 1."}],
        "tools": [{"type": "function", "function": {"name": "ping", "description": "Echo an integer.", "parameters": {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}}}],
        **config["generation"]}
    failed = sum(row["status"] != "completed" for row in recorded)
    attempts = len(recorded)
    complete = False
    monitor_started = False
    try:
        with opener.open(url.replace("/v1/chat/completions", "/v1/models"), timeout=10) as response:
            available = json.load(response)
        if args.model not in {item["id"] for item in available["data"]}:
            raise RuntimeError("Endpoint is not serving the requested model")
        with (out / "warmup.jsonl").open("a" if args.resume else "w") as f:
            for _ in range(config["warmup_requests"]):
                raw, _ = query(warm)
                f.write(raw + "\n")
        thread.start()
        monitor_started = True
        with (out / "raw.jsonl").open("a" if args.resume else "w") as f:
            for row in rows[len(recorded):]:
                entry = row["entry"]
                body = {"model": args.model, "messages": copy.deepcopy(entry["question"][0]),
                        "tools": convert_to_tool(entry["function"], GORILLA_TO_OPENAPI, ModelStyle.OPENAI_COMPLETIONS),
                        **config["generation"]}
                start_wall, start = time.time(), time.perf_counter()
                record = {"id": entry["id"], "category": row["category"], "request": body, "start_unix": start_wall, "attempt": 1}
                try:
                    raw, response = query(body)
                    record.update({"raw_response": raw, "response": response, "status": "completed"})
                except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
                    failed += 1
                    record.update({"status": "inference_error", "error": str(error)})
                    if isinstance(error, urllib.error.HTTPError):
                        record["http_status"] = error.code
                        record["http_error_body"] = error.read(8192).decode(errors="replace")
                record["latency_seconds"] = time.perf_counter() - start
                record["end_unix"] = time.time()
                record["allocated_gpu_seconds"] = len(config["server"]["gpus"]) * record["latency_seconds"]
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                f.flush()
                os.fsync(f.fileno())
                attempts += 1
                print(f"[{attempts}/{len(rows)}] {entry['id']}: {record['status']} {record['latency_seconds']:.2f}s", flush=True)
                if record["status"] != "completed":
                    # An unavailable server is an interrupted experiment, not
                    # thousands of scientific failures. Existing attempts stand.
                    try:
                        with opener.open(url.replace("/v1/chat/completions", "/health"), timeout=5) as health:
                            healthy = health.status == 200
                    except (urllib.error.URLError, TimeoutError):
                        healthy = False
                    if not healthy:
                        raise RuntimeError("Model server is unavailable; resume unattempted IDs after recovery")
        complete = True
    finally:
        stop.set()
        if monitor_started:
            thread.join(timeout=5)
        manifest["end_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        manifest["status"] = ("completed" if failed == 0 else "completed_with_inference_errors") if complete else "incomplete"
        manifest["attempted_n"] = attempts
        manifest["inference_errors"] = failed
        (out / "run.json").write_text(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
