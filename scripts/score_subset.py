"""Call unmodified official BFCL per-entry checkers, then summarize local costs."""
import argparse
import collections
import hashlib
import json
import math
import os
import pathlib
import statistics
import subprocess
from experiment_io import input_path

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "vendor/gorilla/berkeley-function-call-leaderboard/bfcl_eval/data"

def wilson(success, n):
    if not n:
        return None
    z = 1.959963984540054
    mean = success / n
    center = (mean + z*z/(2*n))/(1+z*z/n)
    half = z*math.sqrt(mean*(1-mean)/n + z*z/(4*n*n))/(1+z*z/n)
    return [center-half, center+half]

def percentile(values, q):
    if not values:
        return None
    values = sorted(values)
    index = (len(values)-1)*q
    low = int(index)
    return values[low] + (values[min(low+1, len(values)-1)]-values[low])*(index-low)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("run_dir", type=pathlib.Path)
    args = p.parse_args()
    out = args.run_dir.resolve()
    os.environ["BFCL_PROJECT_ROOT"] = str(out)
    from bfcl_adapter import LocalHandler, register
    from bfcl_eval.constants.enums import Language, ReturnFormat
    from bfcl_eval.eval_checker.eval_runner import _evaluate_single_ast_entry, _evaluate_single_relevance_entry
    from bfcl_eval.utils import is_java, is_js, is_relevance_or_irrelevance
    meta = json.loads((out / "run.json").read_text())
    commit = subprocess.check_output(["git", "-C", str(ROOT / "vendor/gorilla"), "rev-parse", "HEAD"], text=True).strip()
    if commit != meta["config"]["bfcl_commit"]:
        raise RuntimeError("Scorer checkout differs from recorded BFCL commit")
    subprocess.run(["git", "-C", str(ROOT / "vendor/gorilla"), "diff", "--exit-code", "HEAD", "--", "berkeley-function-call-leaderboard/bfcl_eval"], capture_output=True, check=True)
    split_path = input_path(meta)
    rows = {r["entry"]["id"]: r for r in map(json.loads, split_path.read_text().splitlines())}
    raw = list(map(json.loads, (out / "raw.jsonl").read_text().splitlines()))
    if not meta["status"].startswith("completed"):
        raise RuntimeError("Incomplete experiment; refusing to publish a complete score")
    ids = [r["id"] for r in raw]
    assert len(ids) == len(set(ids)), "Duplicate attempts require a separate run"
    assert set(ids) == set(rows), "Incomplete run: refusing to summarize partial outputs as a complete subset"
    name = register(meta["model"])
    handler = LocalHandler(meta["model"], registry_name=name)
    answers = {}
    for cat in meta["config"]["categories"]:
        if is_relevance_or_irrelevance(cat):
            continue
        questions = list(map(json.loads, (DATA / f"BFCL_v4_{cat}.json").read_text().splitlines()))
        golden = list(map(json.loads, (DATA / "possible_answer" / f"BFCL_v4_{cat}.json").read_text().splitlines()))
        assert len(questions) == len(golden)
        # Match the official evaluator's positional alignment, including historical ID differences.
        answers.update({q["id"]: a["ground_truth"] for q, a in zip(questions, golden)})
    scored = []
    for r in raw:
        row = rows[r["id"]]
        result = {"id": r["id"], "category": r["category"], "latency_seconds": r["latency_seconds"],
                  "allocated_gpu_seconds": r["allocated_gpu_seconds"], "valid": False, "official_valid": None}
        if r["status"] != "completed":
            result.update({"error_group": "inference_error", "error": r.get("error")})
            scored.append(result)
            continue
        message = r["response"]["choices"][0]["message"]
        calls = message.get("tool_calls") or []
        # Match the official FC response parser: an empty tool_calls list stays
        # an empty list; only a missing/null tool_calls field falls back to text.
        model_output = ([{c["function"]["name"]: c["function"]["arguments"]} for c in calls]
                        if message.get("tool_calls") is not None else message.get("content"))
        if is_relevance_or_irrelevance(r["category"]):
            verdict = _evaluate_single_relevance_entry(handler, r["id"], model_output, row["entry"], name, r["category"])
        else:
            language, return_format = ((Language.JAVA, ReturnFormat.JAVA) if is_java(r["category"])
                else (Language.JAVASCRIPT, ReturnFormat.JAVASCRIPT) if is_js(r["category"])
                else (Language.PYTHON, ReturnFormat.PYTHON))
            verdict = _evaluate_single_ast_entry(handler, r["id"], model_output, answers[r["id"]], row["entry"],
                                                  name, r["category"], language, return_format)
        result.update({"valid": verdict["valid"], "official_valid": verdict["valid"], "official_verdict": verdict,
            "usage": r["response"].get("usage"), "finish_reason": r["response"]["choices"][0].get("finish_reason")})
        if result["valid"]:
            result["error_group"] = "correct"
        elif "irrelevance" in r["category"] and calls:
            result["error_group"] = "unnecessary_call"
        elif r["category"] == "live_relevance":
            result["error_group"] = "missing_or_invalid_call"
        elif "ast_decoder" in verdict.get("error_type", ""):
            result["error_group"] = "format_or_parse"
        else:
            expected = {key.replace(".", "_") for a in answers.get(r["id"], []) for key in a}
            got = {c["function"]["name"] for c in calls}
            result["error_group"] = "tool_selection" if got != expected else "arguments_or_call_count"
        scored.append(result)
    (out / "scored.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in scored))
    correct = sum(r["valid"] for r in scored)
    completed = [r for r in scored if r["official_valid"] is not None]
    latency = [r["latency_seconds"] for r in completed]
    tokens = [r["usage"]["completion_tokens"] for r in completed if r.get("usage")]
    category_scores = {}
    for cat in meta["config"]["categories"]:
        group = [r for r in scored if r["category"] == cat]
        category_scores[cat] = {"n": len(group), "correct": sum(r["valid"] for r in group),
                                "accuracy_attempted": sum(r["valid"] for r in group)/len(group)}
    summary = {"model": meta["model"], "revision": meta["model_revision"], "split": meta["split"],
        "n": len(scored), "correct": correct, "official_scored_n": len(completed),
        "official_accuracy_completed": correct/len(completed) if completed else None,
        "accuracy_attempted": correct/len(scored), "wilson_95_attempted": wilson(correct, len(scored)),
        "categories": category_scores, "errors": dict(collections.Counter(r["error_group"] for r in scored)),
        "latency_completed_seconds": {"mean": statistics.mean(latency) if latency else None,
            "median": statistics.median(latency) if latency else None, "p95": percentile(latency, 0.95)},
        "output_tokens": {"total": sum(tokens), "mean": statistics.mean(tokens) if tokens else None},
        "allocated_gpu_seconds_attempted": sum(r["allocated_gpu_seconds"] for r in scored),
        "truncated_outputs": sum(r.get("finish_reason") == "length" for r in scored),
        "aggregation": "Case-weighted accuracy across the recorded categories; not the BFCL v4 overall weighted leaderboard score.",
        "limitations": ["Only the recorded categories, not a BFCL v4 overall leaderboard score.",
            "Allocated GPU-seconds = request wall time multiplied by card count; not measured kernel compute time.",
            "GPU telemetry is sampled and includes serving allocations; not an exact memory peak.",
            "Wilson interval is descriptive only; dataset entries need not be independent or representative of real tasks.",
            "Automatic error labels are provisional; manually review representative failures."]}
    peaks = collections.defaultdict(float)
    for sample in map(json.loads, (out / "gpu_samples.jsonl").read_text().splitlines()):
        if sample["exit_code"] != 0:
            continue
        for line in sample["raw_csv"].splitlines():
            index, memory, *_ = line.split(",")
            peaks[index.strip()] = max(peaks[index.strip()], float(memory))
    summary["sampled_peak_vram_mib_per_gpu"] = dict(peaks)
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
