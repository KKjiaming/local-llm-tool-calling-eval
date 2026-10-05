"""Freeze complete official single-turn categories without reading answers."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=["single_turn", "selected_six"], default="single_turn")
    parser.add_argument("--config", type=Path, default=ROOT / "configs/full-single-turn-qwen.json")
    args = parser.parse_args()
    from bfcl_eval.constants.category_mapping import SINGLE_TURN_CATEGORY, VERSION_PREFIX
    config = json.loads(args.config.read_text())
    commit = subprocess.check_output(["git", "-C", str(ROOT / "vendor/gorilla"), "rev-parse", "HEAD"], text=True).strip()
    if commit != config["bfcl_commit"]:
        raise RuntimeError("BFCL checkout differs from the pinned commit")
    subprocess.run(["git", "-C", str(ROOT / "vendor/gorilla"), "diff", "--exit-code", "HEAD", "--", "berkeley-function-call-leaderboard/bfcl_eval"], check=True, capture_output=True)
    categories = SINGLE_TURN_CATEGORY if args.scope == "single_turn" else config["categories"]
    source = ROOT / "vendor/gorilla/berkeley-function-call-leaderboard/bfcl_eval/data"
    rows, hashes = [], {}
    for category in categories:
        path = source / f"{VERSION_PREFIX}_{category}.json"
        hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        for line in path.read_text().splitlines():
            entry = json.loads(line)
            if len(entry["question"]) != 1:
                raise RuntimeError("Single-turn runner must not flatten multi-turn tasks")
            rows.append({"category": category, "entry": entry})
    ids = [row["entry"]["id"] for row in rows]
    assert len(ids) == len(set(ids))
    output = ROOT / "configs/datasets" / f"full_{args.scope}.jsonl"
    output.parent.mkdir(exist_ok=True)
    content = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    if output.exists() and output.read_text() != content:
        raise RuntimeError("Refusing to overwrite a different frozen dataset")
    output.write_text(content)
    manifest = {"bfcl_commit": commit, "bfcl_version": VERSION_PREFIX, "scope": args.scope,
                "n": len(rows), "categories": dict(collections.Counter(row["category"] for row in rows)),
                "dataset_path": str(output.relative_to(ROOT)),
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest(), "source_sha256": hashes,
                "selection": "Every source entry, original category and file order; no sampling or deduplication.",
                "excludes": "Multi-turn, memory, web-search and prompting-only format-sensitivity tasks.",
                "evaluation": "Per-entry official checks; case-weighted accuracy is not the BFCL v4 overall leaderboard score.",
                "holdout_note": "Includes existing smoke/dev/test IDs. Future adaptation must use development data only, never full-run failures to select rules or examples."}
    output.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
