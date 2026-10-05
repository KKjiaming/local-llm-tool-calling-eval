"""Launch only a verified local snapshot; no automatic remote downloads."""
import argparse
import json
import os
import pathlib
import socket
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="Qwen/Qwen3.5-9B")
    p.add_argument("--model-path", type=pathlib.Path)
    p.add_argument("--config", type=pathlib.Path, default=ROOT / "configs/full-single-turn-qwen.json")
    args = p.parse_args()
    config = json.loads(args.config.read_text())
    metadata = json.loads((ROOT / "records" / (args.model.replace("/", "--") + ".json")).read_text())
    path = ROOT / "models" / args.model.replace("/", "--") / metadata["revision"]
    if args.model_path:
        path = args.model_path.resolve()
    if not (path / "download_verified.json").exists():
        raise RuntimeError("Snapshot not fully downloaded and hash-verified")
    verified = json.loads((path / "download_verified.json").read_text())
    if verified["model"] != args.model or verified["revision"] != metadata["revision"]:
        raise RuntimeError("Verification report does not match the selected pinned model")
    for entry in verified["files"]:
        file_path = path / entry["name"]
        if pathlib.Path(entry["name"]).name != entry["name"] or file_path.stat().st_size != entry["size"]:
            raise RuntimeError("Verified runtime file is missing or changed")
    parsers = {"Qwen/Qwen3.5-9B": ("qwen3_coder", "qwen3"),
               "Qwen/Qwen3.8-27B": ("qwen3_coder", "qwen3"),
               "google/gemma-4-26B-A4B-it": ("gemma4", "gemma4")}
    if args.model not in parsers:
        raise RuntimeError("This model has no configured native parsers")
    tool_parser, reasoning_parser = parsers[args.model]
    server = config["server"]
    with socket.socket() as sock:
        # Allow reuse after our previous server shuts down; an active listener
        # still prevents binding (SO_REUSEPORT is deliberately not enabled).
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server["host"], server["port"]))
    # Check for compute jobs on selected cards without inspecting process args.
    inv = subprocess.run(["nvidia-smi", "--query-compute-apps=gpu_uuid,pid", "--format=csv,noheader"], capture_output=True, text=True, check=True)
    if inv.stdout.strip():
        raise RuntimeError("Compute jobs are present; inspect resource availability before launching")
    env = dict(os.environ)
    env.update({"CUDA_VISIBLE_DEVICES": ",".join(map(str, server["gpus"])),
        "HF_HOME": str(ROOT / ".cache/huggingface"), "HF_HUB_OFFLINE": "1",
        "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1", "TRANSFORMERS_OFFLINE": "1",
        "VLLM_NO_USAGE_STATS": "1", "VLLM_CACHE_ROOT": str(ROOT / ".cache/vllm"),
        "TRITON_CACHE_DIR": str(ROOT / ".cache/triton")})
    for key in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "OPENAI_API_KEY", "OPENAI_DEFAULT_HEADERS"):
        env.pop(key, None)
    environment = server.get("python_environment", ".venv")
    command = [str(ROOT / environment / "bin/vllm"), "serve", str(path),
        "--served-model-name", args.model, "--host", server["host"], "--port", str(server["port"]),
        "--tensor-parallel-size", str(server["tensor_parallel_size"]), "--dtype", server["dtype"],
        "--gpu-memory-utilization", str(server["gpu_memory_utilization"]),
        "--max-model-len", str(server["max_model_len"]), "--max-num-seqs", str(server["max_num_seqs"]),
        "--language-model-only", "--enable-auto-tool-choice", "--tool-call-parser", tool_parser,
        "--reasoning-parser", reasoning_parser, "--no-enable-prefix-caching", "--generation-config", "vllm"]
    command_record = {"command": command, "model_revision": metadata["revision"],
                      "config": config, "config_path": str(args.config.resolve())}
    (ROOT / "records" / (args.model.replace("/", "--") + "-server-command.json")).write_text(json.dumps(command_record, indent=2))
    (ROOT / "records/last-server-command.json").write_text(json.dumps(command_record, indent=2))
    print("Launching pinned local snapshot", flush=True)
    os.execve(command[0], command, env)

if __name__ == "__main__":
    main()
