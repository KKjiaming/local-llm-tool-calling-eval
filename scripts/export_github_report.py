"""Generate small, GitHub-renderable reports from unchanged full-run artifacts."""
import collections
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "full-single-turn-20261005"
PAGE_TARGET_BYTES = 60 * 1024
PAGE_MAX_CASES = 30
RUNS = ["qwen9b", "qwen27b", "gemma4"]


def pre(value):
    return "<pre>" + html.escape(str(value), quote=False) + "</pre>\n"


def write_csv(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    reports = ROOT / "reports"
    info = json.loads((reports / (PREFIX + ".json")).read_text())
    models = info["models"]
    categories = list(models[0]["categories"])
    with (reports / (PREFIX + ".csv")).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == info["n"] == 3641
    ids = [row["题目ID"] for row in rows]
    assert len(set(ids)) == len(ids)
    grouped = collections.defaultdict(list)
    for row in rows:
        category = next(c for c in sorted(categories, key=len, reverse=True) if row["题目ID"].startswith(c + "_"))
        grouped[category].append(row)
    for model in models:
        name = model["model"]
        assert sum(row[name + " · 官方判定"] == "正确" for row in rows) == model["correct"]
        for category in categories:
            group = model["categories"][category]
            assert len(grouped[category]) == group["n"]
            assert sum(row[name + " · 官方判定"] == "正确" for row in grouped[category]) == group["correct"]

    summary_rows = []
    for model in models:
        latency = model["latency_completed_seconds"]
        summary_rows.append({"model": model["model"], "cases": model["n"], "correct": model["correct"],
                             "accuracy": model["accuracy_attempted"], "mean_latency_seconds": latency["mean"],
                             "median_latency_seconds": latency["median"], "p95_latency_seconds": latency["p95"],
                             "mean_output_tokens": model["output_tokens"]["mean"],
                             "allocated_gpu_seconds": model["allocated_gpu_seconds_attempted"],
                             "outputs_reaching_token_cap": model["truncated_outputs"]})
    write_csv(reports / "metrics.csv", summary_rows)
    category_rows = [{"category": c, "model": m["model"], "cases": m["categories"][c]["n"],
                      "correct": m["categories"][c]["correct"], "accuracy": m["categories"][c]["accuracy_attempted"]}
                     for c in categories for m in models]
    write_csv(reports / "category-metrics.csv", category_rows)

    case_root = reports / "cases"
    case_root.mkdir(exist_ok=True)
    pages = []
    case_index = ["# All 3,641 cases", "", "[Results summary](../README.md) · [Repository README](../../README.md)", "",
                  "Every evaluated case appears exactly once. Select a category, then a page. Each case includes the original question, accepted answer, and all three models' outputs, official verdicts and request costs.", "",
                  "<pre>Correct = 正确; incorrect = 错误. Official diagnostics are retained unchanged.</pre>", "",
                  "| Official category | Cases | Pages |", "|---|---:|---:|"]
    for category in categories:
        folder = case_root / category
        folder.mkdir(exist_ok=True)
        chunks = []
        blocks = []
        chunk_ids = []
        byte_count = 0
        for row in grouped[category]:
            lines = [f"## {row['题目ID']}", "", "| Model | Official verdict | Latency (s) | Output tokens |",
                     "|---|---|---:|---:|"]
            for model in models:
                name = model["model"]
                lines.append(f"| {name.split('/')[-1]} | {row[name + ' · 官方判定']} | {row[name + ' · 耗时（秒）']} | {row[name + ' · 输出token（含推理）']} |")
            lines += ["", "<details>", "<summary>Question and accepted answer</summary>", "", "### Question", "",
                      pre(row["题目"]), "### Official accepted answer", "", pre(row["官方允许答案"]), "</details>", ""]
            for model in models:
                name = model["model"]
                lines += ["<details>", f"<summary>{html.escape(name)} — {html.escape(row[name + ' · 官方判定'])}</summary>", "",
                          "### Model output", "", pre(row[name + " · 模型答案（工具调用／文本）"])]
                if row[name + " · 官方判定"] != "正确":
                    lines += ["### Official diagnostic", "", pre(row[name + " · 官方错误信息"]),
                              "### Provisional error group", "", pre(row[name + " · 错误分类"])]
                if row[name + " · 人工复核备注"]:
                    lines += ["### Review note", "", pre(row[name + " · 人工复核备注"])]
                lines += ["</details>", ""]
            block = "\n".join(lines) + "\n"
            size = len(block.encode())
            if blocks and (byte_count + size > PAGE_TARGET_BYTES or len(blocks) >= PAGE_MAX_CASES):
                chunks.append((blocks, chunk_ids))
                blocks, chunk_ids, byte_count = [], [], 0
            blocks.append(block)
            chunk_ids.append(row["题目ID"])
            byte_count += size
        if blocks:
            chunks.append((blocks, chunk_ids))
        index = [f"# {category}", "", "[All categories](../README.md) · [Summary](../../README.md)", "",
                 f"All {len(grouped[category])} cases in original evaluation order.", "",
                 "| Page | Cases | First ID | Last ID |", "|---|---:|---|---|"]
        for number, (blocks, chunk_ids) in enumerate(chunks, 1):
            filename = f"page-{number:03d}.md"
            navigation = ["[Category index](README.md)", "[All categories](../README.md)"]
            if number > 1:
                navigation.append(f"[Previous](page-{number-1:03d}.md)")
            if number < len(chunks):
                navigation.append(f"[Next](page-{number+1:03d}.md)")
            header = [f"# {category} — page {number}/{len(chunks)}", "", " · ".join(navigation), "",
                      f"{len(chunk_ids)} cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.", ""]
            content = "\n".join(header) + "\n" + "".join(blocks) + "\n" + " · ".join(navigation) + "\n"
            assert len(content.encode()) < 100 * 1024, "A case needs a smaller dedicated report"
            path = folder / filename
            path.write_text(content)
            pages.append({"path": str(path.relative_to(ROOT)), "category": category, "ids": chunk_ids,
                          "bytes": path.stat().st_size})
            index.append(f"| [{number}]({filename}) | {len(chunk_ids)} | `{chunk_ids[0]}` | `{chunk_ids[-1]}` |")
        (folder / "README.md").write_text("\n".join(index) + "\n")
        case_index.append(f"| [{category}]({category}/README.md) | {len(grouped[category])} | {len(chunks)} |")
    assert [case for page in pages for case in page["ids"]] == ids
    (case_root / "README.md").write_text("\n".join(case_index) + "\n")
    (case_root / "manifest.json").write_text(json.dumps({"n": len(ids), "source": PREFIX + ".csv",
        "dataset_sha256": info["split_sha256"], "pages": pages}, indent=2) + "\n")

    summary = ["# Complete single-turn results", "", "[Repository README](../README.md) · [Browse all 3,641 cases](cases/README.md)", "",
               "These pages render directly on GitHub. The large original HTML/CSV/JSONL files are downloadable research artifacts.", "",
               "All three models completed the same 3,641 cases across 13 official BFCL single-turn categories, without request failures. This is not the complete BFCL v4 leaderboard score.", "",
               "## Overall metrics", "", "| Model | Correct / cases | Accuracy | Mean latency | P95 latency | Output cap reached |",
               "|---|---:|---:|---:|---:|---:|"]
    for m in models:
        summary.append(f"| {m['model']} | {m['correct']}/{m['n']} | {m['accuracy_attempted']:.2%} | {m['latency_completed_seconds']['mean']:.3f} s | {m['latency_completed_seconds']['p95']:.3f} s | {m['truncated_outputs']} |")
    summary += ["", "[Small metrics CSV](metrics.csv) · [Small category metrics CSV](category-metrics.csv) · [Full summary JSON](" + PREFIX + ".json)", "",
                "![Per-category correctness](" + PREFIX + "-accuracy.png)", "", "## Category scores", "",
                "| Official category | Cases | Qwen9B | Qwen27B | Gemma |", "|---|---:|---:|---:|---:|"]
    for category in categories:
        cells = [f"{m['categories'][category]['correct']}/{m['categories'][category]['n']} ({m['categories'][category]['accuracy_attempted']:.2%})" for m in models]
        summary.append(f"| [{category}](cases/{category}/README.md) | {models[0]['categories'][category]['n']} | " + " | ".join(cells) + " |")
    summary += ["", "## Recorded costs", "", "![Inference costs](" + PREFIX + "-costs.png)", "",
                "Four RTX 3090 cards, BF16, TP4, concurrency 1. Qwen uses native thinking enabled and vLLM 0.17.1; Gemma uses native thinking disabled and vLLM 0.19.1. These differences confound speed comparisons. Qwen model generation also changes with size.", "",
                "Allocated GPU-seconds mean four times request wall time, not kernel compute time. VRAM is sampled serving allocation, not an exact peak. No integrated energy result or adaptation improvement is reported. Failure groups are provisional, not manually verified full-run diagnoses.", "",
                "## Downloads and reproducibility", "",
                "To read results in the browser, use the summary and case pages above. To use an original large artifact, select its file download button, or save its Raw contents. Download HTML and open it locally to use its search/filter interface.", "",
                "| Full run | Metrics/configuration | Original downloadable outputs |", "|---|---|---|"]
    for short in RUNS:
        folder = f"../results/{short}-{PREFIX}"
        summary.append(f"| {short} | [Run README]({folder}/README.md), [summary]({folder}/summary.json), [configuration]({folder}/run.json) | [raw requests/responses]({folder}/raw.jsonl), [verdicts]({folder}/scored.jsonl), [HTML]({folder}/answers.html), [CSV]({folder}/answers.csv) |")
    summary += ["", f"Combined downloadable artifacts: [HTML]({PREFIX}.html) · [CSV]({PREFIX}.csv).", "",
                "Rebuild these GitHub reports with `python3.11 scripts/export_github_report.py`. It uses existing results, does not run inference, and does not modify official scores or original outputs."]
    (reports / "README.md").write_text("\n".join(summary) + "\n")
    for short, model in zip(RUNS, models):
        folder = ROOT / "results" / f"{short}-{PREFIX}"
        (folder / "README.md").write_text(f"# {model['model']} — complete single-turn run\n\n"
            "[Three-model summary](../../reports/README.md) · [Browse all paired cases](../../reports/cases/README.md)\n\n"
            f"Official per-entry results: **{model['correct']}/{model['n']} ({model['accuracy_attempted']:.2%})**. "
            f"Mean request latency: **{model['latency_completed_seconds']['mean']:.3f} s**. "
            f"Outputs reaching the length cap: **{model['truncated_outputs']}**.\n\n"
            "[Summary JSON](summary.json) and [recorded configuration](run.json) are small browser-readable files. "
            "Large raw/HTML/CSV files are for download; use the paired Markdown pages for reading in GitHub.\n")
    print(json.dumps({"cases": len(ids), "pages": len(pages), "largest_page_bytes": max(p["bytes"] for p in pages),
                      "unchanged_original_scores": [m["correct"] for m in models]}))


if __name__ == "__main__":
    main()
