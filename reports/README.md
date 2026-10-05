# Complete single-turn results

[Repository README](../README.md) · [Browse all 3,641 cases](cases/README.md)

These pages render directly on GitHub. The large original HTML/CSV/JSONL files are downloadable research artifacts.

All three models completed the same 3,641 cases across 13 official BFCL single-turn categories, without request failures. This is not the complete BFCL v4 leaderboard score.

## Overall metrics

| Model | Correct / cases | Accuracy | Mean latency | P95 latency | Output cap reached |
|---|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-9B | 3024/3641 | 83.05% | 2.486 s | 4.824 s | 4 |
| Qwen/Qwen3.8-27B | 2932/3641 | 80.53% | 8.138 s | 22.284 s | 21 |
| google/gemma-4-26B-A4B-it | 2919/3641 | 80.17% | 0.805 s | 3.431 s | 1 |

[Small metrics CSV](metrics.csv) · [Small category metrics CSV](category-metrics.csv) · [Full summary JSON](full-single-turn-20261005.json)

![Per-category correctness](full-single-turn-20261005-accuracy.png)

## Category scores

| Official category | Cases | Qwen9B | Qwen27B | Gemma |
|---|---:|---:|---:|---:|
| [simple_python](cases/simple_python/README.md) | 400 | 378/400 (94.50%) | 367/400 (91.75%) | 374/400 (93.50%) |
| [simple_java](cases/simple_java/README.md) | 100 | 41/100 (41.00%) | 38/100 (38.00%) | 30/100 (30.00%) |
| [simple_javascript](cases/simple_javascript/README.md) | 50 | 19/50 (38.00%) | 16/50 (32.00%) | 19/50 (38.00%) |
| [multiple](cases/multiple/README.md) | 200 | 189/200 (94.50%) | 187/200 (93.50%) | 184/200 (92.00%) |
| [parallel](cases/parallel/README.md) | 200 | 181/200 (90.50%) | 187/200 (93.50%) | 160/200 (80.00%) |
| [parallel_multiple](cases/parallel_multiple/README.md) | 200 | 178/200 (89.00%) | 169/200 (84.50%) | 165/200 (82.50%) |
| [irrelevance](cases/irrelevance/README.md) | 240 | 204/240 (85.00%) | 198/240 (82.50%) | 196/240 (81.67%) |
| [live_simple](cases/live_simple/README.md) | 258 | 220/258 (85.27%) | 221/258 (85.66%) | 215/258 (83.33%) |
| [live_multiple](cases/live_multiple/README.md) | 1053 | 850/1053 (80.72%) | 837/1053 (79.49%) | 846/1053 (80.34%) |
| [live_parallel](cases/live_parallel/README.md) | 16 | 16/16 (100.00%) | 12/16 (75.00%) | 15/16 (93.75%) |
| [live_parallel_multiple](cases/live_parallel_multiple/README.md) | 24 | 18/24 (75.00%) | 17/24 (70.83%) | 17/24 (70.83%) |
| [live_irrelevance](cases/live_irrelevance/README.md) | 884 | 717/884 (81.11%) | 673/884 (76.13%) | 684/884 (77.38%) |
| [live_relevance](cases/live_relevance/README.md) | 16 | 13/16 (81.25%) | 10/16 (62.50%) | 14/16 (87.50%) |

## Recorded costs

![Inference costs](full-single-turn-20261005-costs.png)

Four RTX 3090 cards, BF16, TP4, concurrency 1. Qwen uses native thinking enabled and vLLM 0.17.1; Gemma uses native thinking disabled and vLLM 0.19.1. These differences confound speed comparisons. Qwen model generation also changes with size.

Allocated GPU-seconds mean four times request wall time, not kernel compute time. VRAM is sampled serving allocation, not an exact peak. No integrated energy result or adaptation improvement is reported. Failure groups are provisional, not manually verified full-run diagnoses.

## Downloads and reproducibility

To read results in the browser, use the summary and case pages above. To use an original large artifact, select its file download button, or save its Raw contents. Download HTML and open it locally to use its search/filter interface.

| Full run | Metrics/configuration | Original downloadable outputs |
|---|---|---|
| qwen9b | [Run README](../results/qwen9b-full-single-turn-20261005/README.md), [summary](../results/qwen9b-full-single-turn-20261005/summary.json), [configuration](../results/qwen9b-full-single-turn-20261005/run.json) | [raw requests/responses](../results/qwen9b-full-single-turn-20261005/raw.jsonl), [verdicts](../results/qwen9b-full-single-turn-20261005/scored.jsonl), [HTML](../results/qwen9b-full-single-turn-20261005/answers.html), [CSV](../results/qwen9b-full-single-turn-20261005/answers.csv) |
| qwen27b | [Run README](../results/qwen27b-full-single-turn-20261005/README.md), [summary](../results/qwen27b-full-single-turn-20261005/summary.json), [configuration](../results/qwen27b-full-single-turn-20261005/run.json) | [raw requests/responses](../results/qwen27b-full-single-turn-20261005/raw.jsonl), [verdicts](../results/qwen27b-full-single-turn-20261005/scored.jsonl), [HTML](../results/qwen27b-full-single-turn-20261005/answers.html), [CSV](../results/qwen27b-full-single-turn-20261005/answers.csv) |
| gemma4 | [Run README](../results/gemma4-full-single-turn-20261005/README.md), [summary](../results/gemma4-full-single-turn-20261005/summary.json), [configuration](../results/gemma4-full-single-turn-20261005/run.json) | [raw requests/responses](../results/gemma4-full-single-turn-20261005/raw.jsonl), [verdicts](../results/gemma4-full-single-turn-20261005/scored.jsonl), [HTML](../results/gemma4-full-single-turn-20261005/answers.html), [CSV](../results/gemma4-full-single-turn-20261005/answers.csv) |

Combined downloadable artifacts: [HTML](full-single-turn-20261005.html) · [CSV](full-single-turn-20261005.csv).

Rebuild these GitHub reports with `python3.11 scripts/export_github_report.py`. It uses existing results, does not run inference, and does not modify official scores or original outputs.
