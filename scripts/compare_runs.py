"""Build paired answer tables from completed, scored runs on identical cases."""
import argparse
import collections
import csv
import html
import json
from pathlib import Path

from export_result_table import CATEGORIES


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    loaded = []
    for path in args.runs:
        summary = json.loads((path / "summary.json").read_text())
        run = json.loads((path / "run.json").read_text())
        records = [json.loads(line) for line in (path / "raw.jsonl").read_text().splitlines()]
        scores = [json.loads(line) for line in (path / "scored.jsonl").read_text().splitlines()]
        with (path / "answers.csv").open(encoding="utf-8-sig", newline="") as f:
            answers = list(csv.DictReader(f))
        assert len(records) == len(scores) == len(answers) == summary["n"]
        assert [r["id"] for r in records] == [r["id"] for r in scores] == [r["题目ID"] for r in answers]
        assert sum(s["valid"] for s in scores) == summary["correct"]
        loaded.append({"path": path, "summary": summary, "run": run, "records": records, "scores": scores, "answers": answers})
    base = loaded[0]
    for other in loaded[1:]:
        assert other["run"]["split_sha256"] == base["run"]["split_sha256"]
        assert other["run"]["config"]["bfcl_commit"] == base["run"]["config"]["bfcl_commit"]
        assert [r["id"] for r in other["records"]] == [r["id"] for r in base["records"]]
        for a, b in zip(base["records"], other["records"]):
            assert a["request"]["messages"] == b["request"]["messages"]
            assert a["request"]["tools"] == b["request"]["tools"]
    keys = ["engine", "version", "gpus", "dtype", "tensor_parallel_size", "max_model_len", "max_num_seqs", "gpu_memory_utilization", "prefix_caching", "speculative_decoding"]
    comparisons = []
    for other in loaded[1:]:
        diffs = {k: [base["run"]["config"]["server"].get(k), other["run"]["config"]["server"].get(k)]
                 for k in keys if base["run"]["config"]["server"].get(k) != other["run"]["config"]["server"].get(k)}
        transitions = collections.Counter((a["valid"], b["valid"]) for a, b in zip(base["scores"], other["scores"]))
        comparisons.append({"reference": base["summary"]["model"], "other": other["summary"]["model"],
            "server_differences": diffs,
            "native_template_defaults": [base["run"].get("native_template_defaults", {}),
                                         other["run"].get("native_template_defaults", {})],
            "chat_template_kwargs": [base["run"].get("chat_template_kwargs", {}),
                                     other["run"].get("chat_template_kwargs", {})],
            "generation_equal": base["run"]["config"]["generation"] == other["run"]["config"]["generation"],
            "both_correct": transitions[(True, True)], "reference_only_correct": transitions[(True, False)],
            "other_only_correct": transitions[(False, True)], "both_incorrect": transitions[(False, False)]})
    paired = []
    for i, row in enumerate(base["answers"]):
        result = {"题目ID": row["题目ID"], "类别": row["类别"], "题目": row["题目"], "官方允许答案": row["官方允许答案"]}
        for data in loaded:
            name = data["summary"]["model"]
            answer = data["answers"][i]
            for field in ["模型答案（工具调用／文本）", "官方判定", "错误分类", "官方错误信息", "人工复核备注", "耗时（秒）", "输出token（含推理）"]:
                result[f"{name} · {field}"] = answer[field]
        paired.append(result)
    with args.output.with_suffix(".csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(paired[0]))
        writer.writeheader()
        writer.writerows(paired)
    info = {"n": len(paired), "split_sha256": base["run"]["split_sha256"],
            "models": [d["summary"] for d in loaded], "paired_comparisons": comparisons,
            "limitations": ["Only the recorded categories, not a full BFCL v4 overall leaderboard score.",
                "These Qwen models differ in generation as well as size; this is not a size-only causal comparison.",
                "One selected run per model; latency is exploratory. See recorded execution conditions for background activity.",
                "Where engine versions differ, costs are not a strictly controlled engine comparison.",
                "Native thinking defaults can differ across model families; no template overrides were supplied."]}
    args.output.with_suffix(".json").write_text(json.dumps(info, indent=2), encoding="utf-8")
    e = lambda x: html.escape(str(x), quote=True)
    cells = []
    for data in loaded:
        s = data["summary"]
        c = data["run"]["config"]["server"]
        thinking = data["run"].get("native_template_defaults", {}).get("enable_thinking")
        thinking_label = {True: "开启", False: "关闭"}.get(thinking, "未记录")
        cells.append(f'<tr><td>{e(s["model"])}</td><td>{s["correct"]}/{s["n"]} ({s["accuracy_attempted"]:.1%})</td>'
                     f'<td>{s["latency_completed_seconds"]["mean"]:.2f}s</td><td>{s["latency_completed_seconds"]["p95"]:.2f}s</td>'
                     f'<td>{s["output_tokens"]["mean"]:.2f}</td><td>{s["allocated_gpu_seconds_attempted"]:.2f}</td>'
                     f'<td>{e(c["dtype"])} / TP{c["tensor_parallel_size"]} / vLLM {e(c["version"])}<br>原生默认思考：{thinking_label}</td></tr>')
    details = []
    for i, row in enumerate(base["answers"]):
        per_model = []
        for data in loaded:
            a = data["answers"][i]
            cls = "pass" if a["官方判定"] == "正确" else "fail"
            per_model.append(f'<td><b class="{cls}">{e(a["官方判定"])}</b> · {float(a["耗时（秒）"]):.3f}s · {e(a["输出token（含推理）"])} tokens'
                             f'<pre>{e(a["模型答案（工具调用／文本）"])}</pre>'
                             f'<details><summary>判定详情</summary><p>{e(a["错误分类"])} · {e(a["人工复核备注"])}</p><pre>{e(a["官方错误信息"])}</pre></details></td>')
        differs = len({d["answers"][i]["官方判定"] for d in loaded}) > 1
        details.append(f'<tr data-different="{str(differs).lower()}"><td><code>{e(row["题目ID"])}</code><br>{e(row["类别"])}'
                       f'<p>{e(row["题目"])}</p><details><summary>官方允许答案</summary><pre>{e(row["官方允许答案"])}</pre></details></td>'
                       + "".join(per_model) + '</tr>')
    categories = ''.join('<tr><td>'+e(CATEGORIES.get(cat, cat))+'</td>'+''.join(
        f'<td>{d["summary"]["categories"][cat]["correct"]}/{d["summary"]["categories"][cat]["n"]}</td>' for d in loaded)+'</tr>'
        for cat in base["summary"]["categories"])
    names = ''.join('<th>'+e(d["summary"]["model"])+'</th>' for d in loaded)
    page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BFCL 模型对比</title><style>body{font:15px/1.6 system-ui,sans-serif;background:#f5f7fb;color:#172238;padding:24px}table{border-collapse:collapse;background:white;width:100%;margin:20px 0}td,th{padding:12px;border:1px solid #dbe3ef;text-align:left;vertical-align:top}th{background:#e9eff9}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px/1.5 monospace}td p{white-space:pre-wrap}summary,a{color:#2159a8}summary{cursor:pointer}.pass{color:#08754b}.fail{color:#b52935}.scroll{overflow:auto}input{padding:10px;font:inherit;margin-right:16px}#paired{min-width:1200px;table-layout:fixed}</style>
<h1>同一组 BFCL 题目的模型对比</h1><p>工具调用未实际执行。成绩覆盖记录中的评测类别，不是完整 BFCL v4 总排行榜成绩。成本为单次实测；速度比较仅供探索。COSTNOTE Qwen 对照同时改变了模型代际和规模。</p>
<p><a href="CSVFILE" download>下载逐题对比 CSV</a> · <a href="JSONFILE">机器可读汇总</a></p>
<div class="scroll"><table><thead><tr><th>模型</th><th>正确率</th><th>平均耗时</th><th>P95</th><th>平均输出 token</th><th>分配 GPU 秒</th><th>配置</th></tr></thead><tbody>SUMMARYROWS</tbody></table></div>
<table><thead><tr><th>类别</th>MODELHEADERS</tr></thead><tbody>CATEGORYROWS</tbody></table>
<input id="search" type="search" placeholder="搜索题目、ID、调用或错误"><label><input id="different" type="checkbox">只看判定不同的题目</label><span id="count"></span>
<div class="scroll"><table id="paired"><thead><tr><th>题目与允许答案</th>MODELHEADERS</tr></thead><tbody>DETAILROWS</tbody></table></div>
<script>const rows=[...document.querySelectorAll('#paired tbody tr')],search=document.querySelector('#search'),different=document.querySelector('#different');function filter(){let n=0;for(const r of rows){r.hidden=!(r.textContent.toLowerCase().includes(search.value.toLowerCase())&&(!different.checked||r.dataset.different==='true'));if(!r.hidden)n++;}document.querySelector('#count').textContent=`显示 ${n}/${rows.length} 题`;}search.addEventListener('input',filter);different.addEventListener('change',filter);filter();</script></html>'''
    import re
    cost_notes = []
    if any(d["run"].get("execution_notes") for d in loaded):
        cost_notes.append("部分运行有背景下载／安装活动，详见运行记录。")
    if any(c["server_differences"] for c in comparisons):
        cost_notes.append("引擎／服务配置有差异，不属于严格控制的速度比较。")
    if len({d["run"].get("native_template_defaults", {}).get("enable_thinking") for d in loaded}) > 1:
        cost_notes.append("各模型保留原生默认思考设置；设置不同也会影响正确率与成本。")
    if all(d["run"]["config"].get("execution_conditions") for d in loaded):
        cost_notes.append("本项目模型下载与环境安装未与本轮测量同时运行。")
    replacements = {"CSVFILE": e(args.output.with_suffix(".csv").name), "JSONFILE": e(args.output.with_suffix(".json").name),
        "COSTNOTE": e(" ".join(cost_notes)),
        "SUMMARYROWS": ''.join(cells), "MODELHEADERS": names, "CATEGORYROWS": categories, "DETAILROWS": ''.join(details)}
    page = re.sub(r'\b(?:CSVFILE|JSONFILE|SUMMARYROWS|MODELHEADERS|CATEGORYROWS|DETAILROWS|COSTNOTE)\b', lambda m: replacements[m[0]], page)
    args.output.with_suffix(".html").write_text(page, encoding="utf-8")
    print(json.dumps({"models": [d["summary"]["model"] for d in loaded], "n": len(paired), "paired_comparisons": comparisons}, ensure_ascii=False))


if __name__ == "__main__":
    main()
