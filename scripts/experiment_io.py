"""Resolve and validate legacy splits and explicitly frozen full datasets."""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def input_path(run):
    path = ROOT / run["dataset_path"] if run.get("dataset_path") else ROOT / "configs/splits" / f"{run['split']}.jsonl"
    path = path.resolve()
    if not path.is_relative_to(ROOT / "configs"):
        raise ValueError("Dataset must be inside project configs")
    if hashlib.sha256(path.read_bytes()).hexdigest() != run["split_sha256"]:
        raise ValueError("Dataset content no longer matches the recorded run")
    return path
