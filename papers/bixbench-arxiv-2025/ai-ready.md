<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology

- **Authors:** Ludovico Mitchener; Jon M Laurent; Alex Andonian; Benjamin Tenmann; Siddharth Narayanan; Geemi P Wellawatte; Andrew White; Lorenzo Sani; Samuel G Rodriques
- **Affiliations:** FutureHouse (San Francisco); ScienceMachine (London)
- **Venue / Year:** arXiv preprint · 2025 (v1 2025-02-28; v3 2025-10-08)
- **arXiv:** 2503.00096
- **URL:** https://arxiv.org/abs/2503.00096
- **Bibkey:** Mitchener2025_250300096
- **Status:** complete (extract from arXiv v3 full text)

## Abstract (v3 PDF)
Large Language Models (LLMs) and LLM-based agents show great promise in accelerating scientific research. Existing benchmarks for measuring this potential and guiding future development continue to evolve from pure recall and rote knowledge tasks, towards more practical work such as literature review and experimental planning. Bioinformatics is a domain where fully autonomous AI-driven discovery may be near, but no extensive benchmarks for measuring progress have been introduced to date. We therefore present the Bioinformatics Benchmark (BixBench), a dataset comprising over 60 real-world scenarios of practical biological data analysis with over 200 associated open-answer questions designed to measure the ability of LLM-based agents to explore biological datasets, perform long, multi-step analytical trajectories, and interpret the nuanced results of those analyses. We evaluate the performance of two frontier LLMs (GPT-4o and Claude 3.5 Sonnet) using a custom agent framework we open source. We find that even the latest frontier models achieve only 21% accuracy in the open-answer regime, and marginally better than random in a multiple-choice setting. By exposing the current limitations of frontier models, we hope BixBench can spur the development of agents capable of conducting rigorous bioinformatic analysis and accelerate scientific discovery.

(Note: the v1 abstract reported "over 50 scenarios", "nearly 300 questions" and "17% accuracy"; the v3 body reports 61 capsules, 205 questions and 21%.)

## Full text / Extract

### Contributions (authors)
1. An expert-curated set of 61 analytical scenarios and 205 open-answer questions in bioinformatics and computational biology (https://huggingface.co/datasets/futurehouse/BixBench).
2. A framework for assessing AI agents in biological data analysis, including key metrics and calibrations (https://github.com/Future-House/BixBench).
3. An open-source agent framework for writing and executing Python, R and bash code in a Jupyter notebook environment.

### Benchmark creation
- **Analysts:** PhD holders or candidates in bioinformatics and related fields, recruited via professional networks, bioinformatics paper authors and affiliated institutions.
- **Capsules:** each has (1) a hypothesis or research question, (2) input data, (3) analysis code (Jupyter via Google Colab; Python, R or bash), plus a result (a few sentences) and an answer (true/false: was the hypothesis supported). Analysts recapitulated published analyses or produced de novo trajectories. Capsules were reviewed by the authors and in some cases other analysts.
- **Task generation:** Claude 3.5 Sonnet (20241022) drafted MCQs from a modified notebook plus hypothesis and result — two rounds of four, eight drafts per capsule. Expert reviewers approved/rejected with full edit access and access to the original capsule. Duplicate filtering by an LLM in triplicate (~95% concordance), repeated until no duplicates were flagged. Final: 205 questions over 61 capsules, 1–7 per capsule (mean 3.8).

### Evaluation
- Agent receives an empty Jupyter notebook, input data files and the questions. Implemented on Aviary (SimpleAgent). Pre-built Docker container BixBench-env:v1.0 with many Python/R/bash bioinformatics packages. Tools: `edit_cell` (modify and execute a cell), `list_workdir` (recursive listing), `submit_answer`. Each edit triggers a full notebook rerun.
- **Open-answer:** judge LLM (Claude 3.5 Sonnet) compares the submitted answer to ground truth; binary score. Each capsule is run five times in parallel.
- **MCQ:** after analysis, a second LLM receives the notebook, question with options and the open answer, and picks an option; optional "Insufficient information" refusal. Majority voting over the five runs; precision = correct / answered (non-refused).
- 305 trajectories per model × modality; two models (GPT-4o, Claude 3.5 Sonnet) × two modalities (with/without images) = 1,220 trajectories. Reasoning models (o1, DeepSeek R1) struggled in pilots with long contexts and structured tool output and were not included.

### Results
- Open-answer accuracy: Claude 3.5 Sonnet 21% vs GPT-4o 15%.
- MCQ with refusal: both models very close to random — tendency to opt out in complex analyses.
- MCQ without refusal: higher and above random; authors speculate this is largely due to answering via recall rather than the analysis.
- Performance does not surpass the pure-recall baseline (questions answered without any notebook).
- Majority voting: no significant change as vote counts accumulate, with or without refusal.
- Vision ablation (agent prompted not to produce plots): no significant effect; models were observed to interpret notebook plots poorly.

### Future work (authors)
Broader sampling of workflows and data types; evaluating additional (reasoning) models; a human-expert baseline (not yet collected).
