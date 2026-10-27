# BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology

> **Bibkey** `Mitchener2025_250300096` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2503.00096> · `status: complete`

---

## One-liner
BixBench (FutureHouse + ScienceMachine) is one of the first agent benchmarks for **open-ended bioinformatics data analysis**: 61 real analysis "capsules" (data + hypothesis + reference notebook) built by PhD-level analysts, with 205 open-answer questions; the agent explores the data in an empty Jupyter notebook and answers. GPT-4o and Claude 3.5 Sonnet reach at best **21%** open-answer accuracy, and near-random in the MCQ setting with an "insufficient information" option.

## Problem
Science-agent benchmarks are moving from recall QA to practical tasks like literature review and experiment planning, but bioinformatics — which the authors see as the field where fully autonomous discovery may arrive first — lacks a broad benchmark of an agent's ability to explore datasets, run long multi-step analyses and interpret nuanced results. Existing data-science benchmarks either use a simple reward (training loss in RE-Bench) or artificially constrain artifacts and statistical choices (BLADE).

## Method
**Capsules**: PhD-level (or candidate) bioinformatics analysts, working in a Google Colab template notebook, recapitulate published analyses or run de novo analyses on data they provide; each capsule has a research question/hypothesis, input data and analysis code, plus a result description and a true/false answer on whether the hypothesis held; reviewed by the authors and other analysts. **Questions**: Claude 3.5 Sonnet drafts MCQs from a modified notebook plus hypothesis/result, two rounds of four per capsule; experts approve/reject with full edit access (seeing the original capsule); an LLM de-duplicates in triplicate (~95% concordance). Final: 205 questions, 1–7 per capsule (mean 3.8). **Environment**: Aviary (FutureHouse's language-agent gym) SimpleAgent; a Docker image pre-loaded with Python/R/bash bioinformatics packages (BixBench-env:v1.0); three tools `edit_cell`, `list_workdir`, `submit_answer`; every edit reruns the whole notebook. **Two scoring regimes**: (1) open-answer — a judge LLM (Claude 3.5 Sonnet) compares the answer with ground truth, binary score, each capsule run 5 times in parallel; (2) MCQ — a second LLM reads the full notebook and open answer and picks an option, optionally an "Insufficient information" refusal; majority vote over 5 runs, with precision over non-refused answers. A "no notebook, pure recall" baseline is also reported. 1,220 trajectories in total (305 × 2 models × with/without images).

## Data
61 capsules and 205 questions spanning a range of self-selected analysis categories (histogram in Fig. 2, e.g. differential expression, clustering); data files are heterogeneous in format and layout (csv, rds, …), so agents must navigate and pick libraries themselves. Questions are designed to require completing an analysis rather than recall. Dataset on HuggingFace; evaluation code open source.

## Key results
**Open-answer**: Claude 3.5 Sonnet **21%** vs GPT-4o **15%**. **MCQ with refusal**: both near random — models tend to opt out ("insufficient information") in complex analytical contexts; **MCQ without refusal**: performance rises above random, which the authors attribute largely to **answering from recall rather than from the analysis**; and no setting **beats the "no-notebook, pure recall" baseline**. Majority voting over 5 runs gives no significant gain as votes accumulate. **Image ablation**: forbidding plots made no significant difference (the authors note models interpret notebook plots poorly). Reasoning models (o1, DeepSeek R1) struggled in pilot tests with long contexts and structured tool use and were excluded. No human-expert baseline is provided.

## Contributions
- 61 expert-curated open-ended bioinformatics scenarios with real data and reference notebooks, plus 205 open-answer questions.
- An open-source notebook-style agent environment (Aviary + Docker + three tools) for reproducibly evaluating Python/R/bash trajectories.
- Uses a **refusal option** and a **pure-recall baseline** as calibration, revealing that MCQ scores are inflated by recall and that models opt out when allowed.
- Five parallel runs per capsule, providing per-question rerun-consistency data (App. Figs 7–8).

## Limitations
- **Final-answer only** (binary), so it cannot separate "sound method, slightly off" from "wrong method, lucky answer" — exactly BiomniBench's critique.
- Questions are LLM-drafted then human-reviewed, and the judge is an LLM (the same Claude 3.5 Sonnet as one evaluated model), with no reported judge–human agreement.
- Only two models and one simple scaffold; no human baseline; coverage is admittedly far from comprehensive.
- Numbers changed across versions (v1: 50+ scenarios / ~300 questions / 17%; v3: 61 / 205 / 21%); cite the version.

## Relation to our direction
For **Topic 2**, BixBench is the archetype of outcome-level evaluation and a natural **control** for our claim-to-evidence verification: it shows (1) MCQ scores are inflated by recall — its pure-recall baseline and refusal option should be adopted in our protocol to tell whether an agent's conclusion comes from the omics analysis it ran or from prior knowledge; (2) its per-question accuracy across five parallel runs (App. Figs 7–8) is early evidence for rerun stability. Its gap: it never checks whether intermediate conclusions in the notebook are supported by the data, and it does not calibrate its judge — precisely what Topic 2's calibrated verifier adds. For **Topic 1**, its capsule structure (hypothesis + data + reference notebook + true/false conclusion) is a good template for packaging analyses on KPMP/Lake public data as reusable tasks; if KidneyAnomalyBench grows an "agent analyses the anomalous region" track, the capsule format and Aviary environment can be reused directly. For the detect → model → revert line, it says agents are far from reliable at bioinformatics (best 21%) and can only be assistants whose output is verified.

## Reusable assets
- **Dataset:** BixBench (capsules + questions).
<https://huggingface.co/datasets/futurehouse/BixBench>
- **Eval harness and code:**
<https://github.com/Future-House/BixBench>
- **Agent environment:** Aviary (SimpleAgent) + the BixBench-env Docker image.
- **Protocol ideas:** pure-recall baseline, refusal option, 5-run majority vote, precision vs accuracy.

## Follow-ups
- Aviary (arXiv 2412.21154) and LAB-Bench (lab-bench-arxiv-2024), the same team's prior work.
- Later agent systems that report BixBench scores, and how scores move with model generations.
- ScienceAgentBench, DiscoveryBench and CORE-Bench (reproducibility) as comparators.

## Cite
```bibtex
@misc{Mitchener2025_250300096,
  title = {BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology},
  author = {Ludovico Mitchener and Jon M Laurent and Alex Andonian and Benjamin Tenmann and Siddharth Narayanan and Geemi P Wellawatte and Andrew White and Lorenzo Sani and Samuel G Rodriques},
  year = {2025},
  eprint = {2503.00096},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.00096}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
