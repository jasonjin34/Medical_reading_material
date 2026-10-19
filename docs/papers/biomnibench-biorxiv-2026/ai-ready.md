<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research

- **Authors:** Qu, Yuanhao; Lu, Yingzhou; Tu, Xinming; Zhang, Serena; She, Tianwei; Shaw, Alexander Glenn; Shih, Jou-Ho; Zhao, Bingqing; Shen, Minjie; Yang, Haochen; Yan, Jielin; Zhang, Rongchuan; Wu, Xinze; Li, Tingting; Zhou, Bin; Wang, Ning; Ma, Adam; Cong, Le; Hu, Xiaobo; Jiang, Yuan; Dong, Jiayun; Peng, Tao; Leskovec, Jure; Huang, Kexin
- **Venue / Year:** bioRxiv (preprint, CC-BY 4.0) · 2026
- **DOI:** 10.64898/2026.05.12.724604
- **URL:** https://doi.org/10.64898/2026.05.12.724604
- **Bibkey:** Qu_2026
- **Status:** complete (extract from bioRxiv v1 full text)

## Abstract
LLM agents now perform real biomedical research, but evaluating them rigorously is hard. Outcome-only benchmarks fail in two ways. First, a correct final answer can come from memorization, reward hacking, or wrong reasoning that produces the right number by chance. Second, valid alternative analyses are marked wrong simply because they differ from the reference. We introduce BiomniBench, a process-level evaluation framework that scores the full agent trajectory against expert-designed, task-specific rubrics. Our first release, BiomniBench-DA, contains 100 data-analysis tasks across 17 task types, 5 disease areas, and a general-biology category, each based on a paper from journals such as Nature, Cell, and Science and co-developed with an original author or a domain expert. Benchmarking frontier and open-weight models across four agent harnesses reveals three findings. Frontier and open-weight bases cluster within a few points of each other, with substantial headroom for all models. The agent harness shifts scores by more than the gap between successive model generations. Agents reliably ground claims in real sources yet consistently fall short on method selection, biological interpretation, and scientific reasoning. BiomniBench is the first process-level benchmark for LLM agents in biomedical research, providing the dimension-level diagnostics that outcome scoring cannot.

Dataset: huggingface.co/datasets/phylobio/BiomniBench-DA

## Full text / Extract

### Design principles
(1) Ground tasks in real-world research — every task is derived from published research and requires multi-step reasoning, method selection and interpretation. (2) Evaluate the process, not just the output — rubrics score the quality of analytical decisions at each step. (3) Accommodate multiple valid approaches — each rubric encodes alternative analytical paths.

### Curation pipeline
- **User-trace analysis:** 32,014 user queries from the open-source Biomni platform, LLM-classified (multi-label). Data analysis 63.3%, literature research 55.0%, experimental design 26.2%, quick factual queries 25.1%, manuscript writing 15.4% (77.0% of queries carry more than one intent).
- **Paper selection:** 21 publications (Nature, Cell, Science and family journals, or preprints of similar calibre) with publicly available data (GEO, ArrayExpress, supplements).
- **Expert curation:** an original author or a domain expert with 5+ years' experience formulates the questions and prepares the dataset.
- **Ground truth:** expert reference trace as Jupyter notebook or R Markdown, verified to run on the public data and reviewed across multiple rounds.
- **Rubric:** 5–10 criteria per task, each anchored at a key decision point and tagged to one or more of six dimensions (data handling, method selection, statistical rigor, biological interpretation, scientific reasoning, source reliability). Levels: A = fully correct; B = right intention, minor mistake or partial match (usually half credit); C = skipped or wrong (zero). Levels enumerate multiple correct alternatives.

### Evaluation protocol
Tasks run in the Harbor execution framework (Docker container, Python 3 and R, 2 CPUs, internet access, one-hour budget). Agents must write `trace.md` (decisions, code, intermediate findings, interpretation, references) and `answer.txt`. The instruction forbids searching for or reading the source publication; spot-checks showed no clear evidence of paper-derived shortcuts. An LLM judge selects one A/B/C level per criterion (returns only the categorical level plus a one-sentence reason); points and the 0–100 task score are computed programmatically. Each configuration is run three times on all 100 tasks; Score = mean over tasks of per-task means; ± = SD across the three replicate means; per-task SD = mean within-task SD across reruns. Failed tasks are retried once, then scored zero.

### Judge validation (597 criteria, 35 tasks, vs internal-expert A/B/C ratings)
| Judge | Exact acc. | Linear κ | Quadratic κ |
|---|---|---|---|
| Gemini 3.1 Pro | 0.82 | 0.70 | 0.73 |
| Qwen 3.6 | 0.80 | 0.64 | 0.69 |
| GPT-5.4 | 0.69 | 0.55 | 0.62 |
| Claude Opus 4.6 | 0.70 | 0.47 | 0.51 |
| DeepSeek V3.2 | 0.60 | 0.35 | 0.40 |

Failure modes: Claude Opus 4.6 rates 39% of human-B as A; Qwen 3.6 rates 43% of human-B as A; GPT-5.4 rates 24% of human-A as B; DeepSeek V3.2 B-recall 21% (39% of human-B pushed to C). Gemini 3.1 Pro diagonal recalls 87%/76%/73%.

### Dataset statistics
Disease areas: oncology 47%, metabolic and endocrine 17%, immunology 14%, general biology 10%, neurology 8% (ALS), cardiovascular 4%. Six most common task types (55%): association testing 11%, mutation analysis 10%, multi-omic integration 10%, pathway enrichment 8%, differential expression 8%, clustering 8%. Long tail: predictive modeling, cell composition, survival, chromatin profiling, signature scoring, longitudinal, cross-cohort comparison, GWAS–eQTL colocalization, TCR repertoire, co-expression networks, cell–cell communication.

### Results — Terminus-2 harness, 9 models (Table 1)
| Model | Score (mean ± SD) | Per-task SD | Time/task | Cost/task | Turns |
|---|---|---|---|---|---|
| Claude Opus 4.7 | 63.94 ± 0.30 | 7.3 | 8.0m | $0.87 | 15 |
| GPT-5.5 | 63.57 ± 1.79 | 9.4 | 11.4m | $1.98 | 16 |
| Claude Opus 4.6 | 63.16 ± 1.56 | 8.3 | 17.0m | $1.79 | 24 |
| Claude Sonnet 4.6 | 62.35 ± 0.65 | 7.5 | 13.6m | $0.94 | 20 |
| GLM-5.1 | 60.39 ± 0.67 | 8.8 | 10.6m | $0.58 | 20 |
| Qwen 3.6 | 59.47 ± 1.19 | 8.2 | 23.6m | $1.01 | 22 |
| Kimi K2.6 | 59.15 ± 0.54 | 9.8 | 25.0m | $0.85 | 31 |
| GPT-5.4 | 55.19 ± 0.94 | 11.5 | 12.6m | $1.08 | 13 |
| Gemini 3.1 Pro | 44.27 ± 0.92 | 7.5 | 4.9m | $0.37 | 12 |

### Results — cross-harness (Table 2)
| Harness | Model | Score | Per-task SD | Time | Cost | Turns |
|---|---|---|---|---|---|---|
| Claude Code | Opus 4.7 | 73.34 ± 0.41 | 8.6 | 10.2m | $2.52 | 34 |
| Claude Code | Opus 4.6 | 69.51 ± 1.32 | 7.9 | 8.3m | $1.29 | 17 |
| Codex CLI | GPT-5.4 | 68.69 ± 0.56 | 8.6 | 14.3m | $2.30 | 82 |
| Codex CLI | GPT-5.5 | 67.59 ± 0.87 | 8.7 | 8.8m | $4.58 | 53 |
| Claude Code | Sonnet 4.6 | 66.39 ± 0.50 | 7.8 | 8.4m | $0.92 | 23 |
| Gemini CLI | Gemini 3.1 Pro | 49.83 ± 1.33 | 8.9 | 5.4m | – | – |

GPT-5.4: 68.69 (Codex CLI) vs 55.19 (Terminus-2), a 13.5-point spread attributable to the harness. Opus 4.7: 73.34 (Claude Code) vs 63.94 (Terminus-2), 9.4 points. Generational gap Opus 4.7 vs 4.6 under Claude Code: 3.8 points.

### Anatomy of performance
Hardest task types: GWAS–eQTL (best 65), pathway enrichment (best 67). Near-saturated: cell composition (max 91, min 70), mutation analysis (max 86). Largest harness gap: cross-cohort comparison (Claude Code 32–53 vs Codex CLI 51–56). By dimension: source reliability 88–98% of available points; data handling 58–78%; method selection 44–67% (lowest); statistical rigor, biological interpretation, scientific reasoning 45–74%. Recurring failures (App. C): wrong method selection (Kruskal–Wallis/Mann–Whitney used to claim a monotonic trend; Jonckheere–Terpstra gives p ≈ 0.40), flawed biological interpretation (proteome-wide summary instead of anchoring to the named disease phenotypes), poor scientific reasoning (a multi-step normality-test/weighting procedure replaced by a single correlation).

### Limitations (authors)
Rubric construction is expert-intensive and cannot enumerate every defensible path; the LLM judge (κ = 0.70) is not a substitute for expert judgment on the most subjective dimensions — supplement high-stakes evaluation with human review; per-item construction cost is substantial. Future releases: experimental design, literature synthesis, protocol optimization; longer-horizon multi-turn tasks.
