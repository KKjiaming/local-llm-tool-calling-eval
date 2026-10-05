"""Standalone study figures generated exclusively from completed raw runs."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    loaded = []
    for run_dir in args.runs:
        summary = json.loads((run_dir / "summary.json").read_text())
        run = json.loads((run_dir / "run.json").read_text())
        raw = [json.loads(s) for s in (run_dir / "raw.jsonl").read_text().splitlines()]
        assert len(raw) == summary["n"] and run["status"].startswith("completed")
        loaded.append((summary, run, raw))
    assert len({r[1]["split_sha256"] for r in loaded}) == 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "pdf.fonttype": 42, "svg.fonttype": "none"})
    colors = ["#2b6cb0", "#dd6b20", "#238b63", "#864cbf"]
    categories = list(loaded[0][0]["categories"])
    category_labels = {"simple_python":"Single Python", "simple_java":"Single Java", "simple_javascript":"Single JS",
                       "multiple":"Multiple tools", "parallel":"Parallel", "parallel_multiple":"Parallel multiple",
                       "irrelevance":"Irrelevance", "live_simple":"Live simple", "live_multiple":"Live multiple",
                       "live_parallel":"Live parallel", "live_parallel_multiple":"Live parallel multiple",
                       "live_irrelevance":"Live irrelevance", "live_relevance":"Live relevance"}
    labels = [category_labels.get(category, category) for category in categories]
    n = loaded[0][0]["n"]
    fig, axis = plt.subplots(figsize=(max(11, len(categories)*1.2), 6))
    x = np.arange(len(categories))
    width = 0.75 / len(loaded)
    for i, (summary, _, _) in enumerate(loaded):
        values = [summary["categories"][c]["accuracy_attempted"]*100 for c in categories]
        bars = axis.bar(x+(i-(len(loaded)-1)/2)*width, values, width, color=colors[i%len(colors)],
                        label=f"{summary['model'].split('/')[-1]} ({summary['correct']}/{summary['n']} overall)")
        for bar, category in zip(bars, categories):
            group = summary["categories"][category]
            axis.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{group['correct']}/{group['n']}",
                      ha="center", va="bottom", fontsize=8)
    axis.set(xticks=x, xticklabels=labels, ylim=(0, 114), ylabel="Official per-category accuracy (%)",
             title=f"Tool-calling correctness on {n:,} fixed BFCL cases")
    if len(categories) > 6:
        axis.tick_params(axis='x', labelrotation=20)
    axis.set_yticks([0, 25, 50, 75, 100])
    axis.grid(axis="y", alpha=0.15)
    axis.set_axisbelow(True)
    axis.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=min(3,len(loaded)), frameon=False)
    fig.text(0.01,0.01,"Recorded evaluation categories; not the BFCL v4 overall score. One selected run per model; official scores unchanged.",fontsize=9)
    fig.tight_layout(rect=(0,0.09,1,1))
    for extension in ("png", "pdf", "svg"):
        fig.savefig(args.output.parent/(args.output.name+f"-accuracy.{extension}"), dpi=180)
    plt.close(fig)
    fig, axes = plt.subplots(1,2,figsize=(11,5.5))
    distributions = [[r['latency_seconds'] for r in raw if r['status']=='completed'] for _,_,raw in loaded]
    names = [summary['model'].split('/')[-1] for summary,_,_ in loaded]
    axes[0].boxplot(distributions, tick_labels=names, showmeans=True)
    axes[0].set(ylabel="End-to-end request latency (seconds)", title="Warmed latency distribution")
    axes[0].tick_params(axis='x',labelrotation=12)
    axes[0].grid(axis="y", alpha=0.15)
    tokens = [summary['output_tokens']['mean'] for summary,_,_ in loaded]
    bars = axes[1].bar(names,tokens,color=colors[:len(loaded)])
    axes[1].set(ylabel="Mean output tokens (including reasoning)",title="Generated output usage")
    axes[1].tick_params(axis='x',labelrotation=12)
    for bar,value in zip(bars,tokens): axes[1].text(bar.get_x()+bar.get_width()/2,bar.get_height()+3,f"{value:.1f}",ha='center',fontsize=9)
    axes[1].set_ylim(0,max(tokens)*1.2)
    fig.suptitle("Exploratory inference costs: four RTX 3090 cards, BF16, TP4, concurrency 1")
    isolated = all(run['config'].get('execution_conditions') for _,run,_ in loaded)
    context = ("No project download or package installation ran during these measurements."
               if isolated else "Check each run's execution notes for background download/install activity.")
    fig.text(0.01,0.045,context+" Engine differences can confound latency.",fontsize=8)
    fig.text(0.01,0.02,"Native thinking defaults may differ; tokens from different tokenizers are not equivalent units of work.",fontsize=8)
    fig.tight_layout(rect=(0,0.09,1,0.95))
    for extension in ("png", "pdf", "svg"):
        fig.savefig(args.output.parent/(args.output.name+f"-costs.{extension}"),dpi=180)
    plt.close(fig)
    print(f"Wrote accuracy and cost figures under {args.output.parent}")


if __name__ == "__main__":
    main()
