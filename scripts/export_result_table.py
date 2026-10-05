"""Export a completed subset as a standalone HTML table and Excel-readable CSV."""
import argparse
import csv
import datetime
import hashlib
import html
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from experiment_io import input_path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "vendor/gorilla/berkeley-function-call-leaderboard/bfcl_eval/data"
CATEGORIES = {
    "simple_python": "单工具", "multiple": "多工具选择", "parallel": "并行调用",
    "parallel_multiple": "多工具并行", "irrelevance": "不应调用工具", "live_multiple": "真实工具选择",
    "simple_java": "单工具 Java", "simple_javascript": "单工具 JavaScript",
    "live_simple": "真实单工具", "live_parallel": "真实并行调用",
    "live_parallel_multiple": "真实多工具并行", "live_irrelevance": "真实无关工具",
    "live_relevance": "真实应调用工具",
}
GROUPS = {
    "correct": "正确", "arguments_or_call_count": "参数／调用数量不匹配",
    "tool_selection": "工具集合不匹配", "unnecessary_call": "不必要调用",
    "format_or_parse": "格式／解析错误", "inference_error": "推理失败",
    "missing_or_invalid_call": "缺少有效工具调用",
}


def load_lines(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def pretty(value):
    return json.dumps(value, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    out = args.run_dir.resolve()
    run = json.loads((out / "run.json").read_text())
    summary = json.loads((out / "summary.json").read_text())
    split = input_path(run)
    selected = load_lines(split)
    raw_list, score_list = load_lines(out / "raw.jsonl"), load_lines(out / "scored.jsonl")
    raw = {r["id"]: r for r in raw_list}
    scored = {r["id"]: r for r in score_list}
    expected_ids = {r["entry"]["id"] for r in selected}
    assert len(raw_list) == len(raw) == len(selected) == summary["n"]
    assert len(score_list) == len(scored) and set(raw) == set(scored) == expected_ids
    assert sum(r["valid"] for r in score_list) == summary["correct"]
    # Load only answers matching the evaluated split; do not inspect held-out cases.
    answers = {}
    for category in run["config"]["categories"]:
        if "relevance" in category:
            continue
        questions = load_lines(DATA / f"BFCL_v4_{category}.json")
        gold = load_lines(DATA / "possible_answer" / f"BFCL_v4_{category}.json")
        assert len(questions) == len(gold)
        for question, answer in zip(questions, gold):
            if question["id"] in expected_ids:
                answers[question["id"]] = answer["ground_truth"]
    rows = []
    review_path = out / "manual_review.json"
    review_notes = json.loads(review_path.read_text(encoding="utf-8")) if review_path.exists() else {}
    for index, selected_row in enumerate(selected, 1):
        key = selected_row["entry"]["id"]
        record, score = raw[key], scored[key]
        choice = (record.get("response", {}).get("choices") or [{}])[0]
        message = choice.get("message") or {}
        calls = message.get("tool_calls") or []
        output = []
        for call in calls:
            function = call["function"]
            try:
                arguments = json.loads(function["arguments"])
            except json.JSONDecodeError:
                arguments = function["arguments"]
            output.append({"name": function["name"], "arguments": arguments})
        rendered = pretty(output) if calls else "未调用工具\n" + (message.get("content") or "（无文本回复）")
        if calls and message.get("content"):
            rendered = "文本回复：\n" + message["content"] + "\n\n工具调用：\n" + rendered
        if record["status"] != "completed":
            rendered = "推理失败：" + record.get("error", "未记录原因")
        usage = record.get("response", {}).get("usage") or {}
        verdict = score.get("official_verdict") or {}
        status = "正确" if score["official_valid"] is True else "错误" if score["official_valid"] is False else "未评分"
        notes = review_notes.get(key, "")
        rows.append({
            "序号": index, "题目ID": key, "类别": CATEGORIES.get(score["category"], score["category"]),
            "原始类别": score["category"],
            "题目": "\n\n".join(f"{m['role']}: {m.get('content', '')}" for m in record["request"]["messages"]),
            "模型答案（工具调用／文本）": rendered,
            "官方允许答案": ("不应调用工具" if "irrelevance" in score["category"] else
                          "应生成非空有效工具调用（官方仅检查相关性）" if score["category"] == "live_relevance" else pretty(answers[key])),
            "官方判定": status, "错误分类": GROUPS.get(score["error_group"], score["error_group"]),
            "官方错误信息": pretty(verdict.get("error", [])) if not score["valid"] else "",
            "人工复核备注": notes, "耗时（秒）": round(record["latency_seconds"], 6),
            "输入token": usage.get("prompt_tokens", ""), "输出token（含推理）": usage.get("completion_tokens", ""),
            "完成原因": choice.get("finish_reason", ""),
        })
    with (out / "answers.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    e = lambda v: html.escape(str(v), quote=True)
    categories = "".join(f'<option value="{e(k)}">{e(v)}</option>' for k, v in CATEGORIES.items() if k in summary["categories"])
    overview = "".join(
        f'<tr><td>{e(CATEGORIES.get(k,k))}</td><td>{v["correct"]}/{v["n"]}</td><td>{v["accuracy_attempted"]:.1%}</td></tr>'
        for k, v in summary["categories"].items())
    table_rows = []
    for row in rows:
        result_class = "pass" if row["官方判定"] == "正确" else "fail"
        error_details = ""
        if row["官方错误信息"]:
            error_details = '<details><summary>官方错误详情</summary><pre>' + e(row["官方错误信息"]) + '</pre></details>'
        table_rows.append(
            f'<tr data-category="{e(row["原始类别"])}" data-status="{result_class}">'
            f'<td>{row["序号"]}<br><code>{e(row["题目ID"])}</code><br>{e(row["类别"])}</td>'
            f'<td class="question">{e(row["题目"])}</td>'
            f'<td><pre>{e(row["模型答案（工具调用／文本）"])}</pre></td>'
            f'<td><details><summary>查看允许值</summary><pre>{e(row["官方允许答案"])}</pre></details></td>'
            f'<td><strong class="{result_class}">{e(row["官方判定"])}</strong><br>{e(row["错误分类"])}'
            f'<p>{e(row["人工复核备注"])}</p>{error_details}</td>'
            f'<td>{row["耗时（秒）"]:.3f}s<br>{row["输出token（含推理）"]} tokens<br>{e(row["完成原因"])}</td></tr>')
    page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>MODEL BFCL 答案与结果</title>
<style>
body{font:15px/1.6 system-ui,sans-serif;color:#182238;background:#f4f6fa;margin:0;padding:28px}
main{max-width:1800px;margin:auto}h1{margin:0 0 8px;font-size:26px}.panel{background:white;border:1px solid #dce3ef;border-radius:10px;padding:18px;margin:18px 0}
.cards{display:flex;gap:18px;flex-wrap:wrap}.card{min-width:150px}.card b{display:block;font-size:25px}.muted{color:#546279}
table{border-collapse:collapse;width:100%;background:white}th,td{text-align:left;vertical-align:top;border-bottom:1px solid #dce3ef;padding:12px}th{background:#e8eef8;position:sticky;top:0}pre{white-space:pre-wrap;overflow-wrap:anywhere;margin:0;font:12px/1.6 ui-monospace,monospace}code{overflow-wrap:anywhere}.question{white-space:pre-wrap;min-width:230px}
.pass{color:#08754b}.fail{color:#b52935}.controls{display:flex;gap:12px;flex-wrap:wrap}input,select{padding:10px;border:1px solid #aebdd2;border-radius:5px;background:white;font:inherit}input{min-width:260px;flex:1}summary{cursor:pointer;color:#2159a8}.scroll{overflow:auto}#answers{min-width:1250px;table-layout:fixed}#answers th:nth-child(1){width:150px}#answers th:nth-child(6){width:100px}.overview{max-width:520px}a{color:#2159a8}td p{font-size:13px}
</style><main><h1>MODEL · BFCL 逐题答案与结果</h1>
<p class="muted">RUNINFO · 非完整 BFCL 排行榜成绩</p>
<div class="panel cards">CARDS</div>
<div class="panel"><b>如何阅读</b><p>模型答案是生成的工具名称与参数，工具没有实际执行。官方允许答案中的参数数组表示可接受值，并非唯一标准回复。工具名称的点号可能在 API 中转为下划线；判定由官方评分器完成。</p>
<p>输出 token 包含推理生成。部分错误存在题目、工具说明与答案歧义，人工备注供复核使用，官方成绩未修改。</p>
<p><a href="answers.csv" download>下载完整 CSV（Excel 可打开）</a> · <a href="summary.json">汇总 JSON</a> · <a href="raw.jsonl">原始逐题输出</a></p>
<table class="overview"><thead><tr><th>类别</th><th>正确／题数</th><th>正确率</th></tr></thead><tbody>OVERVIEW</tbody></table></div>
<div class="panel controls"><input id="search" type="search" placeholder="搜索题目、调用、ID 或错误信息" aria-label="搜索">
<select id="category" aria-label="类别"><option value="">全部类别</option>CATEGORIES</select>
<select id="status" aria-label="结果"><option value="">全部结果</option><option value="fail">只看错误</option><option value="pass">只看正确</option></select><span id="count"></span></div>
<div class="scroll"><table id="answers"><thead><tr><th>序号 / ID / 类别</th><th>题目</th><th>模型答案</th><th>官方允许答案</th><th>判定与复核</th><th>耗时 / 输出</th></tr></thead><tbody>ROWS</tbody></table></div>
<p class="muted">来源：同目录 run.json、raw.jsonl、scored.jsonl、summary.json；官方 BFCL 固定版本的允许答案。搜索与筛选完全在本地进行，无外部依赖。</p></main>
<script>
const rows=[...document.querySelectorAll('#answers tbody tr')];
const search=document.querySelector('#search'), category=document.querySelector('#category'), status=document.querySelector('#status');
function filter(){const term=search.value.toLowerCase();let count=0;for(const row of rows){const show=(!category.value||row.dataset.category===category.value)&&(!status.value||row.dataset.status===status.value)&&row.textContent.toLowerCase().includes(term);row.hidden=!show;if(show)count++;}document.querySelector('#count').textContent=`显示 ${count} / ${rows.length} 题`;}
for(const control of [search,category,status])control.addEventListener('input',filter);filter();
</script></html>'''
    cards = (f'<div class="card">官方正确率<b>{summary["correct"]}/{summary["n"]} · {summary["accuracy_attempted"]:.0%}</b></div>'
             f'<div class="card">平均耗时<b>{summary["latency_completed_seconds"]["mean"]:.2f}s</b></div>'
             f'<div class="card">平均输出<b>{summary["output_tokens"]["mean"]:.2f} tokens</b></div>'
             f'<div class="card">完成 / 截断<b>{summary["official_scored_n"]} / {summary["truncated_outputs"]}</b></div>')
    # Substitute once: model text must never be interpreted as a template marker.
    import re
    server = run["config"]["server"]
    date = datetime.datetime.fromisoformat(run["start_utc"]).astimezone(ZoneInfo("Asia/Shanghai")).date()
    scope = "完整所选单轮类别" if run.get("dataset_path") else "子集"
    info = f"固定 {summary['n']} 题 {run['split']} {scope} · {date} · {len(server['gpus'])} 张 GPU / {server['dtype']} / TP{server['tensor_parallel_size']}"
    replacements = {"CARDS": cards, "OVERVIEW": overview, "CATEGORIES": categories, "ROWS": "\n".join(table_rows),
                    "MODEL": e(run["model"]), "RUNINFO": e(info)}
    page = re.sub(r"\b(?:CARDS|OVERVIEW|CATEGORIES|ROWS|MODEL|RUNINFO)\b", lambda m: replacements[m[0]], page)
    (out / "answers.html").write_text(page, encoding="utf-8")
    print(json.dumps({"rows": len(rows), "correct": summary["correct"], "html": str(out / "answers.html"), "csv": str(out / "answers.csv")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
