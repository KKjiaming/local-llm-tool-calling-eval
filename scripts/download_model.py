"""Anonymous, resumable pinned model download with LFS SHA256 validation."""
import argparse
import concurrent.futures
import hashlib
import json
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="Qwen/Qwen3.5-9B")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--source", choices=["huggingface", "modelscope"], default="huggingface")
    p.add_argument("--source-manifest", type=pathlib.Path)
    args = p.parse_args()
    record = json.loads((ROOT / "records" / (args.model.replace("/", "--") + ".json")).read_text())
    model, revision = record["model"], record["revision"]
    mirror = {}
    if args.source == "modelscope":
        if not args.source_manifest:
            raise ValueError("ModelScope requires an inspected public file manifest")
        source_info = json.loads(args.source_manifest.read_text())
        assert source_info["Code"] == 200
        mirror = {s["Name"]: s for s in source_info["Data"]["Files"]}
        for weight in record["weights"]:
            matched = mirror[weight["name"]]
            assert matched["Size"] == weight["size_bytes"]
            assert matched["Sha256"] == weight["lfs_sha256"]
        print(f"Official ModelScope manifest: all {len(record['weights'])} weights match pinned HF SHA256", flush=True)
    # Only public metadata, explicitly anonymous curl. No auth headers or netrc.
    response = subprocess.run(["curl", "--fail", "--location", "--http1.1", "--retry", "3", "--max-time", "60", "--silent", "--show-error",
        f"https://huggingface.co/api/models/{model}/revision/{revision}?blobs=true"], capture_output=True, check=True)
    info = json.loads(response.stdout)
    assert info["sha"] == revision
    files = [s for s in info["siblings"] if s["rfilename"].endswith((".json", ".jinja", ".safetensors", ".model", ".txt"))
             and "/" not in s["rfilename"]]
    dest = ROOT / "models" / model.replace("/", "--") / revision
    dest.mkdir(parents=True, exist_ok=True)
    (ROOT / "records" / (model.replace("/", "--") + "-download-manifest.json")).write_text(json.dumps(info, indent=2))
    def download(s):
        name, expected = s["rfilename"], s.get("lfs", {}).get("sha256")
        target = dest / name
        size = s.get("size")
        url = f"https://huggingface.co/{model}/resolve/{revision}/{name}"
        if name.endswith(".safetensors") and args.source == "modelscope":
            url = f"https://modelscope.cn/models/{model}/resolve/master/{name}"
        if not target.exists() or (size and target.stat().st_size != size):
            print(f"Downloading {name} from {args.source if name.endswith('.safetensors') else 'pinned HF'}", flush=True)
            for attempt in range(8):
                process = subprocess.run(["curl", "--fail", "--location", "--http1.1", "--retry", "2", "--retry-delay", "2",
                    "--connect-timeout", "30", "--max-time", "900", "--continue-at", "-", "--silent", "--show-error",
                    url, "--output", str(target)])
                if process.returncode == 0:
                    break
                print(f"Transfer interrupted for {name}, attempt {attempt+1}/8; retaining partial file", flush=True)
                time.sleep(3)
            else:
                raise RuntimeError(f"Download failed after resumable attempts: {name}")
        if size and target.stat().st_size != size:
            raise RuntimeError(f"Wrong size for {name}")
        digest = hashlib.sha256()
        with target.open("rb") as f:
            for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
                digest.update(block)
        actual = digest.hexdigest()
        if expected and actual != expected:
            raise RuntimeError(f"SHA256 mismatch for {name}")
        if not expected and s.get("blobId"):
            data = target.read_bytes()
            blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
            if blob != s["blobId"]:
                raise RuntimeError(f"Git blob mismatch for pinned config/tokenizer file {name}")
        print(f"Verified {name} ({target.stat().st_size} bytes)", flush=True)
        return {"name": name, "size": target.stat().st_size, "sha256": actual, "expected_lfs_sha256": expected}
    verified = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(download, s): s for s in files}
        for future in concurrent.futures.as_completed(futures):
            verified.append(future.result())
    (dest / "download_verified.json").write_text(json.dumps({"model": model, "revision": revision, "weight_source": args.source,
        "files": sorted(verified, key=lambda s: s["name"])}, indent=2))
    print(dest, flush=True)

if __name__ == "__main__":
    main()
