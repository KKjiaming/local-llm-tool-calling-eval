"""Package only allowlisted code and complete single-turn results; no upload."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RUNS = [f"results/{model}-full-single-turn-20261005" for model in ("qwen9b", "qwen27b", "gemma4")]


def load_lines(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def validate_results():
    dataset = json.loads((ROOT / "configs/datasets/full_single_turn.manifest.json").read_text())
    reference_ids = None
    verified = []
    for directory in RUNS:
        folder = ROOT / directory
        run = json.loads((folder / "run.json").read_text())
        summary = json.loads((folder / "summary.json").read_text())
        raw = load_lines(folder / "raw.jsonl")
        scored = load_lines(folder / "scored.jsonl")
        ids = [row["id"] for row in raw]
        if run["status"] != "completed" or len(ids) != dataset["n"] or len(set(ids)) != len(ids):
            raise ValueError(f"Incomplete or duplicated run: {directory}")
        if run["split_sha256"] != dataset["sha256"] or summary["n"] != len(ids):
            raise ValueError(f"Dataset mismatch: {directory}")
        if [row["id"] for row in scored] != ids:
            raise ValueError(f"Scored ID coverage mismatch: {directory}")
        if reference_ids is not None and ids != reference_ids:
            raise ValueError("Models were not evaluated on identical ordered IDs")
        reference_ids = ids
        counts = collections.Counter(row["category"] for row in raw)
        if dict(counts) != dataset["categories"]:
            raise ValueError(f"Category coverage mismatch: {directory}")
        correct = sum(row["valid"] for row in scored)
        if correct != summary["correct"]:
            raise ValueError(f"Verdict/summary mismatch: {directory}")
        for category, count in counts.items():
            group = summary["categories"][category]
            if group["n"] != count or group["correct"] != sum(row["valid"] for row in scored if row["category"] == category):
                raise ValueError(f"Category score mismatch: {directory}/{category}")
        verified.append({"run": directory, "model": run["model"], "n": len(ids), "correct": correct})
    comparison = json.loads((ROOT / "reports/full-single-turn-20261005.json").read_text())
    if comparison["n"] != dataset["n"] or comparison["split_sha256"] != dataset["sha256"]:
        raise ValueError("Combined report dataset mismatch")
    if {m["model"]: m["correct"] for m in comparison["models"]} != {m["model"]: m["correct"] for m in verified}:
        raise ValueError("Combined report score mismatch")
    return verified


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "public-release/full-single-turn-public.zip")
    args = parser.parse_args()
    plan = json.loads((ROOT / "configs/public-release-files.json").read_text())
    paths = plan["files"]
    if len(paths) != len(set(paths)):
        raise ValueError("Duplicate public paths")
    verified = validate_results()
    entries = []
    for name in paths:
        supplied_path = ROOT / name
        path = supplied_path.resolve()
        if not path.is_relative_to(ROOT) or supplied_path.is_symlink() or not path.is_file():
            raise ValueError(f"Invalid public file: {name}")
        data = path.read_bytes()
        entries.append({"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    manifest = {"scope": plan["scope"], "completed_runs": verified, "files": entries,
                "original_files_modified": False, "uploaded": False}
    output = args.output.resolve()
    if output == ROOT or output.is_relative_to(ROOT / "results") or output.is_relative_to(ROOT / "records"):
        raise ValueError("Archive must not overwrite experiment records")
    if output.exists() or output in {(ROOT / name).resolve() for name in paths}:
        raise ValueError("Refusing to overwrite an existing file")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for entry in entries:
                data = (ROOT / entry["path"]).read_bytes()
                if hashlib.sha256(data).hexdigest() != entry["sha256"]:
                    raise ValueError(f"File changed during packaging: {entry['path']}")
                archive.writestr("open-model-tool-calling-study/" + entry["path"], data)
            archive.writestr("open-model-tool-calling-study/PUBLIC_MANIFEST.json", json.dumps(manifest, indent=2) + "\n")
        with zipfile.ZipFile(temporary) as archive:
            bad = archive.testzip()
            if bad:
                raise ValueError(f"Archive integrity error: {bad}")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({"archive": str(output.relative_to(ROOT)) if output.is_relative_to(ROOT) else str(output),
                      "files": len(entries), "uncompressed_bytes": sum(e["bytes"] for e in entries),
                      "archive_bytes": output.stat().st_size, "completed_runs": verified,
                      "uploaded": False}, indent=2))


if __name__ == "__main__":
    main()
