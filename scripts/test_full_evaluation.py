"""Offline integrity checks; synthetic fixtures, never benchmark results."""
import contextlib
import copy
import io
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest import mock

import experiment_io
import run_subset


class ResumeIntegrity(unittest.TestCase):
    def test_interruption_keeps_failed_attempt_and_only_resumes_remaining_ids(self):
        posts = []
        health = {"ok": False}
        class Endpoint(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass
            def respond(self, value, status=200):
                data = json.dumps(value).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            def do_GET(self):
                if self.path == "/v1/models":
                    self.respond({"data": [{"id": "test/model"}]})
                else:
                    self.respond({}, 200 if health["ok"] else 503)
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                content = body["messages"][0]["content"]
                posts.append(content)
                if content == "case0" and not health["ok"]:
                    self.respond({"error": "synthetic interruption"}, 500)
                else:
                    self.respond({"choices": [{"message": {"content": "synthetic output", "tool_calls": []}, "finish_reason": "stop"}],
                                  "usage": {"prompt_tokens": 10, "completion_tokens": 1}})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "configs/splits").mkdir(parents=True)
            (root / "records").mkdir()
            rows = [{"category": "simple_python", "entry": {"id": f"simple_python_{i}", "question": [[{"role": "user", "content": f"case{i}"}]],
                      "function": [{"name": "echo", "description": "Synthetic fixture", "parameters": {"type": "dict", "properties": {}, "required": []}}]}} for i in range(2)]
            (root / "configs/splits/smoke.jsonl").write_text("".join(json.dumps(row)+"\n" for row in rows))
            (root / "records/test--model.json").write_text(json.dumps({"revision": "synthetic"}))
            server = ThreadingHTTPServer(("127.0.0.1", 0), Endpoint)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            config = {"status": "frozen_after_smoke_validation", "categories": ["simple_python"], "synthetic_validation": True,
                      "server": {"port": server.server_port, "gpus": [0, 1, 2, 3]}, "generation": {"temperature": 0, "seed": 1},
                      "warmup_requests": 1, "timeout_seconds": 5}
            path = root / "configs/config.json"
            path.write_text(json.dumps(config))
            argv = ["run_subset.py", "--model", "test/model", "--split", "smoke", "--run-name", "synthetic-check", "--config", str(path)]
            try:
                with mock.patch.object(run_subset, "ROOT", root), mock.patch.object(experiment_io, "ROOT", root), \
                     mock.patch.object(run_subset.subprocess, "run", return_value=SimpleNamespace(stdout="", returncode=0)), \
                     contextlib.redirect_stdout(io.StringIO()):
                    with mock.patch("sys.argv", argv), self.assertRaisesRegex(RuntimeError, "server is unavailable"):
                        run_subset.main()
                    output = root / "results/synthetic-check"
                    original = (output / "raw.jsonl").read_bytes()
                    self.assertEqual(json.loads((output / "run.json").read_text())["status"], "incomplete")
                    health["ok"] = True
                    with mock.patch("sys.argv", argv+["--resume"]):
                        run_subset.main()
                    raw = [json.loads(line) for line in (output / "raw.jsonl").read_text().splitlines()]
                    self.assertTrue((output / "raw.jsonl").read_bytes().startswith(original))
                    self.assertEqual([r["id"] for r in raw], ["simple_python_0", "simple_python_1"])
                    self.assertEqual(posts.count("case0"), 1)
                    self.assertEqual(posts.count("case1"), 1)
                    self.assertEqual(raw[0]["status"], "inference_error")
                    manifest = json.loads((output / "run.json").read_text())
                    self.assertEqual(manifest["status"], "completed_with_inference_errors")
                    self.assertEqual(manifest["inference_errors"], 1)
                    config["generation"]["seed"] = 2
                    path.write_text(json.dumps(config))
                    with mock.patch("sys.argv", argv+["--resume"]), self.assertRaisesRegex(ValueError, "configuration differs"):
                        run_subset.main()
            finally:
                server.shutdown()
                server.server_close()
                thread.join()


class OfficialForeignLanguageScoring(unittest.TestCase):
    def test_native_fc_java_and_javascript_accept_values_and_reject_wrong_values(self):
        from bfcl_adapter import LocalHandler, register
        from bfcl_eval.constants.enums import Language, ReturnFormat
        from bfcl_eval.eval_checker.eval_runner import _evaluate_single_ast_entry, _evaluate_single_relevance_entry
        registry = register("test/model")
        handler = LocalHandler("test/model", registry_name=registry)
        for category, language, return_format in [("simple_java", Language.JAVA, ReturnFormat.JAVA),
                                                  ("simple_javascript", Language.JAVASCRIPT, ReturnFormat.JAVASCRIPT)]:
            prompt = {"id": category+"_synthetic", "question": [[{"role":"user", "content":"Synthetic validation only"}]],
                      "function": [{"name":"sample.echo", "description":"Synthetic validation", "parameters":{"type":"dict",
                      "properties":{"label":{"type":"String"}}, "required":["label"]}}]}
            gold = [{"sample.echo":{"label":["example"]}}]
            for value, expected in [("example", True), ("wrong", False)]:
                verdict = _evaluate_single_ast_entry(handler, prompt["id"], [{"sample_echo": json.dumps({"label":value})}],
                         gold, copy.deepcopy(prompt), registry, category, language, return_format)
                self.assertEqual(verdict["valid"], expected)
        self.assertTrue(_evaluate_single_relevance_entry(handler, "synthetic", [], {}, registry, "live_irrelevance")["valid"])
        self.assertFalse(_evaluate_single_relevance_entry(handler, "synthetic", [], {}, registry, "live_relevance")["valid"])
        self.assertTrue(_evaluate_single_relevance_entry(handler, "synthetic", [{"echo":"{}"}], {}, registry, "live_relevance")["valid"])


if __name__ == "__main__":
    unittest.main()
