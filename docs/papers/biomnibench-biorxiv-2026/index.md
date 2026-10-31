# BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research

> **Bibkey** `Qu_2026` · **Venue** bioRxiv (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.64898/2026.05.12.724604> · `status: complete`

---

## One-liner
BiomniBench is a **process-level** benchmark for biomedical agents: instead of scoring only the final answer, an LLM judge grades the agent's full analytical trajectory (`trace.md` + `answer.txt`) against expert-written (often original-author-written), task-specific A/B/C rubrics. The first release, BiomniBench-DA, has 100 data-analysis tasks built on the public data of Nature/Cell/Science-tier papers. The best configuration (Claude Code + Opus 4.7) reaches only 73.34/100, and **the agent harness moves scores more than a model generation does**.

## Problem
Existing biomedical-agent benchmarks (HLE, BixBench, BioML-bench, scBench, SpatialBench, …) almost all score the final answer only. The authors argue this fails twice: (1) a correct answer can come from memorization/contamination, reward hacking, or wrong reasoning that lands on the right number by chance — an agent can return a clean volcano plot and a confident interpretation while its trace shows wrong normalization, ignored batch effects and a fabricated citation; (2) real research is open-ended, so matching a single reference penalizes defensible alternative analyses. In biology these flaws propagate silently into wet-lab and drug-development decisions.

## Method
**Five-stage curation**: (1) analyse 32,014 real user queries from the open-source Biomni platform (LLM-classified, multi-label): data analysis is 63.3%, ahead of literature research 55.0% and experimental design 26.2% → data analysis is the first release; (2) select 21 papers by task-type match, disease/method diversity, public data (GEO/ArrayExpress/supplements) and high-impact venue; (3) for each paper recruit **an original author or a domain expert with 5+ years' experience** to pose questions and prepare data — not necessarily reproducing the paper, possibly asking what the data supports but the paper did not address; (4) the expert writes a reference trace (Jupyter/R Markdown), multi-round reviewed and verified to run on the public data; (5) 5–10 rubric criteria per task, each anchored at a key analytical decision and tagged to one or more of six dimensions — **data handling, method selection, statistical rigor, biological interpretation, scientific reasoning, source reliability** — with three levels A (fully correct) / B (right intention, minor error; usually half credit) / C (skipped or wrong; zero), each level enumerating acceptable alternatives. **Protocol**: tasks run in the Harbor sandbox (Docker, Python 3 + R, 2 CPUs, internet, 1-hour budget); agents must write `trace.md` (decisions with rationale, real code, intermediate counts, references) and `answer.txt`; searching for the source paper is explicitly forbidden. **The LLM judge** outputs only an A/B/C level (+ one-sentence reason) per criterion; points are computed programmatically. Judge selection: five candidates vs. internal-expert ratings on 597 criteria from 35 tasks; Gemini 3.1 Pro was best (exact acc 0.82, linear κ 0.70, quadratic κ 0.73). Every configuration is **rerun three times** over all 100 tasks, reporting mean ± across-rerun SD and per-task SD.

## Data
BiomniBench-DA: 100 tasks, 17 task types, 5 disease areas + general biology, from 21 papers (Cancer Cell, Cell, Nature, Nature Medicine, Science, PNAS, …). Disease split: oncology 47% (CRC, NSCLC, melanoma, pan-cancer proteogenomics), metabolic/endocrine 17%, immunology 14%, general biology 10%, neurology 8% (ALS), cardiovascular 4%. The six most common types (55%): association testing 11%, mutation analysis 10%, multi-omic integration 10%, pathway enrichment 8%, differential expression 8%, clustering 8%; the long tail includes survival, cell composition, GWAS–eQTL colocalization, TCR repertoire, cell–cell communication. **There are no kidney tasks.** The dataset is public on HuggingFace.

## Key results
**Fixed harness (Terminus-2, 9 models, 3 reruns)**: Claude Opus 4.7 63.94 ± 0.30, GPT-5.5 63.57 ± 1.79, Opus 4.6 63.16 ± 1.56, Sonnet 4.6 62.35 ± 0.65 — the top four within 1.6 points; open-weight GLM-5.1 60.39, Qwen 3.6 59.47, Kimi K2.6 59.15 trail by only 3–5 points at lower cost (GLM-5.1 $0.58/task vs Opus 4.7 $0.87); GPT-5.4 55.19; Gemini 3.1 Pro is an outlier at 44.27 (shortest traces: median 4.9 min, 12 turns). **Per-task SD is 7.3–11.5 points**, i.e. large rerun-to-rerun variability on the same task. **Cross-harness**: Claude Code + Opus 4.7 73.34 ± 0.41 (best), Claude Code + Opus 4.6 69.51, Codex CLI + GPT-5.4 68.69, Codex CLI + GPT-5.5 67.59, Claude Code + Sonnet 4.6 66.39, Gemini CLI + Gemini 3.1 Pro 49.83. Same model, different harness: GPT-5.4 gains **13.5 points** under Codex CLI vs Terminus-2 and Opus 4.7 gains 9.4 under Claude Code — both larger than the Opus 4.7 vs 4.6 generational gap (3.8). The price is more turns and cost (GPT-5.4 13 → 82 turns; GPT-5.5 $1.98 → $4.58). **By task type**: GWAS–eQTL (best 65) and pathway enrichment (best 67) are universally hard; cell composition (max 91) and mutation analysis (max 86) are near-saturated; cross-cohort comparison shows the largest harness gap. **By dimension**: source reliability earns 88–98% of points, data handling 58–78%, **method selection is lowest (44–67%)**, and statistical rigor / biological interpretation / scientific reasoning sit at 45–74%. Three recurring failures: wrong method (claiming a monotonic trend from Kruskal–Wallis when a Jonckheere–Terpstra trend test gives p ≈ 0.40), unfocused biological interpretation (not anchoring to the named disease phenotypes), and collapsed reasoning (replacing a multi-step normality-test + weighting procedure with one correlation). Judge failure modes: Opus 4.6 and Qwen 3.6 are lenient (39%/43% of human-B rated A), GPT-5.4 is harsh, DeepSeek V3.2 nearly eliminates the B class.

## Contributions
- The first **process-level** benchmark for biomedical agents: full trajectories scored on six dimensions, separating "flawed method, right answer" from "rigorous method, slightly off".
- Tasks and rubrics co-built with original authors/senior experts; each rubric level enumerates valid alternatives so defensible divergence is not penalized.
- Benchmark coverage driven by a real usage distribution (32k Biomni logs) rather than invented tasks.
- Treats the judge as an instrument to validate: five candidates against human gold, with κ and per-judge bias patterns reported.
- A strict rerun protocol (three full reruns, across-rerun and per-task SD), quantifying that harness effects exceed generational model effects.

## Limitations
- Rubric construction is expensive expert labour and cannot enumerate every defensible path; correct approaches outside the rubric may still be penalized.
- The LLM judge agrees with humans overall (κ = 0.70) but cannot replace experts on the most subjective dimensions; the authors recommend human review for high-stakes use.
- The judge was validated against **the same internal experts who wrote the rubrics**, on only 35 tasks; selection and scoring may share biases.
- Data analysis only, single-shot execution; oncology is nearly half, with no kidney, no dedicated spatial-omics, and no imaging tasks.
- "Do not read the source paper" is enforced only by instruction plus spot-checks ("no clear evidence" of shortcuts); contamination is not quantitatively excluded.
- High source-reliability scores (88–98%) mean citations are "identifiable", not that each one was checked to actually support its claim.

## Relation to our direction
For **the agent-trustworthiness topic** this is one of the most direct reference points. Three hooks: **(1) the six process dimensions** (especially method selection and statistical rigor) are a ready starting point for an omics-specific failure taxonomy — on top of which we add kidney-omics failure types: unhandled ambient RNA / doublets, ignored snRNA–snATAC disagreement, testing per cell instead of per sample (pseudoreplication), Xenium segmentation artifacts read as biology. Its da-1-1 rubric criterion 3, "aggregate proportions per patient, not per cell", is exactly the pseudoreplication template. **(2) Its reported per-task SD of 7.3–11.5 points** is ready-made evidence for our rerun-stability axis: the same configuration on the same task can swing ~10 points across reruns, which justifies rerun stability as a trust signal. **(3) Its gap is the agent-trustworthiness topic's entry point**: source reliability checks only that citations are "identifiable", not whether **each claim is supported by the cited evidence or the data actually run** — exactly what claim-to-evidence verification with a calibrated verifier adds; and its judge is compared only against the same experts who wrote the rubrics, with no calibration or coverage guarantee. For **the artifact-injection topic**, BiomniBench-DA has no kidney tasks, so a "kidney process-level benchmark" on KPMP/Lake/HuBMAP data with nephropathologist/nephrologist-authored rubrics is an open gap; KidneyAnomalyBench's expert validation can borrow its five-stage curation (usage → paper selection → expert questions → reference trace → A/B/C rubric). For the lab's detect → model → revert line, it is a reminder that if agents are to nominate reversal targets, evaluation must inspect the process (method choice, biological interpretation), not just the final gene list.

## Reusable assets
- **Dataset:** BiomniBench-DA (100 tasks, data, rubrics).
<https://huggingface.co/datasets/phylobio/BiomniBench-DA>
- **Execution framework:** Harbor (containerized agent evaluation supporting Codex CLI / Terminus-2 / Claude Code / Gemini CLI).
<https://github.com/harbor-framework/harbor>
- **Protocol templates:** the mandatory `trace.md` structure (objective, data sources, per-step decision + rationale + code + intermediate counts, results, references), the A/B/C rubric format, the judge prompt (App. A.4) and judge-validation table (App. B).
- **Rerun statistics:** three full reruns, separating across-rerun SD from per-task SD — directly reusable as a rerun-stability reporting format.

## Follow-ups
- The Biomni paper (biomni-biorxiv-2025) and BenchGuard (Tu et al. 2026, arXiv 2604.24955, automated auditing of noisy benchmark ground truth).
- Concurrent GeneBench, CompBioBench, BioMysteryBench, BioAgent Bench and LAB-Bench2 (arXiv 2604.09554).
- Track the announced experimental-design / literature-synthesis releases and any multi-turn human-in-the-loop setting.

## Cite
```bibtex
@article{Qu_2026, title={BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research}, url={http://dx.doi.org/10.64898/2026.05.12.724604}, DOI={10.64898/2026.05.12.724604}, publisher={openRxiv}, author={Qu, Yuanhao and Lu, Yingzhou and Tu, Xinming and Zhang, Serena and She, Tianwei and Shaw, Alexander Glenn and Shih, Jou-Ho and Zhao, Bingqing and Shen, Minjie and Yang, Haochen and Yan, Jielin and Zhang, Rongchuan and Wu, Xinze and Li, Tingting and Zhou, Bin and Wang, Ning and Ma, Adam and Cong, Le and Hu, Xiaobo and Jiang, Yuan and Dong, Jiayun and Peng, Tao and Leskovec, Jure and Huang, Kexin}, year={2026}, month=May }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
