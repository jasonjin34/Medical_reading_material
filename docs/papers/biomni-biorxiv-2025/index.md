# Biomni: A General-Purpose Biomedical AI Agent

> **Bibkey** `Huang2025_Biomni` · **Venue** bioRxiv (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1101/2025.05.30.656746> · `status: complete`

---

## One-liner
Biomni is the Leskovec-lab general-purpose biomedical agent: an "action discovery agent" mines tasks/tools/databases from 2,500 bioRxiv papers across 25 subfields, which after human verification become the unified environment **Biomni-E1** (150 specialised tools + 105 software packages + 59 databases); a CodeAct-based agent **Biomni-A1** (retrieve a tool subset → plan → write and execute code → iterate) then solves cross-domain tasks zero-shot, with one CRISPR-cloning case validated at the bench. It has become the **default baseline** for later biomedical-agent papers.

## Problem
Existing biomedical agents are mostly specialist workflows for narrow tasks and generalise poorly across subfields; general LLMs lack an environment that **explicitly defines the biomedical action space** (tools, databases, software, wet-lab protocols) and an architecture that composes actions in it without hard-coded templates. The question: can one build a "virtual AI biologist" that works zero-shot across genetics, genomics, pharmacology, microbiology and clinical genomics?

## Method
**(1) Action discovery**: the 100 most recent papers in each of bioRxiv's 25 subject categories (2,500 total) are chunk-read by an LLM that extracts tasks, software and databases; ~1,900 recurring tasks are manually de-duplicated and trivial "few lines of code" tasks dropped, keeping expertise-heavy ones (wet-lab protocols, AI predictors). **(2) Biomni-E1**: human scientists plus web-enabled software-engineering agents implement each tool, each required to pass a defined test case and a five-point checklist (name, docs, LLM-readable research-log output, test, non-triviality). Large relational databases (PDB, OpenTargets, ClinVar) each get **one** natural-language query function (an LLM parses the schema and writes the query); API-less databases go into a local data lake as pandas DataFrames; software lives in one container supporting Python/R/Bash. **(3) Biomni-A1**: CodeAct-based — a separate LLM retriever selects the relevant subset of tools/data/software (to keep context short), the agent writes a numbered plan, then iteratively writes and runs code, reads observations and revises until convergence. The key design is **code as the universal action interface** (loops, parallelism, conditionals, non-standard signatures) rather than classic function calling.

## Data
**QA benchmarks**: LAB-Bench DbQA and SeqQA (45-question dev set used to tune interfaces, 315 held-out test questions, averaged over three runs; the authors say they used a 12.5% subset because of API cost) and a 52-question HLE subset across 14 bio/med subfields (no dev set). **Eight new real-world tasks**: variant prioritisation (Open Targets Genetics), GWAS causal gene (Shringarpure et al.), CRISPR screen design (Schmidt et al., IL-2 screen, 18,939 candidate genes), rare-disease diagnosis and patient gene prioritisation (MyGene2 / Alsentzer et al.), drug repurposing (Huang et al., scored against clinicians' off-label prescribing in an EHR), scRNA-seq annotation (CellxGene etc., 20k–50k cells), microbiome differential abundance (5 datasets). **Case studies**: wearables from 30 people (458 Excel files, CGM + temperature; plus 227 nights of sleep from 10 people and 652 lipid / 731 metabolite / 1,470 protein features), a human embryonic skeleton snRNA+snATAC multiome (~336,000 nuclei, 5–11 weeks), a cloning benchmark and a B2M sgRNA wet-lab run.

## Key results
**LAB-Bench**: DbQA **74.4%** (human experts 74.7%, ReAct+Code 40.8%); SeqQA **81.9%** (humans 78.8%). **HLE subset**: **17.3%** (base LLM 6.0%, coding agent 12.8%, literature agent 12.2%). **Eight real-world tasks** (Claude Sonnet 3.7 backbone): average relative gain of **402.3%** over the base LLM, **43.0%** over ReAct+Code and **20.4%** over its own ReAct ablation — code-centric planning plus environment grounding carry most of the gain; tasks take 6–24 steps using 0–4 specialised tools, 1–8 packages and 0–3 data-lake items. **Cases**: wearables — mean post-meal temperature rise 2.19°C (median 1.10°C; range −0.11 to 15.56°C); multiome — an autonomous 10-step pySCENIC/GRNBoost2/cisTarget/AUCell + ATAC-filtering GRN run (~5 h) that recovers known regulation (e.g. RUNX2) and flags AUTS2, ZFHX3, PBX1 as broadly active across skeletal lineages (the authors note PBX1 is already a known skeletal regulator); cloning — blinded review rates Biomni on par with a senior human expert in accuracy/completeness and clearly above a trainee; the B2M sgRNA protocol executed verbatim yielded two picked colonies with perfect Sanger alignment.

## Contributions
- **Mines the action space from literature** and then human-verifies it into an executable environment — environment building as a scalable pipeline rather than hand-listed tools.
- "One function per database + LLM-generated query" wrapping, which keeps the tool count manageable.
- Code-as-action (CodeAct) + retrieval-based tool selection + adaptive planning, systematically beating ReAct-style chaining zero-shot across domains.
- A rare **wet-lab closed-loop check** (cloning protocol executed verbatim and sequence-confirmed).
- Open code, Harvard Dataverse data and a web UI, making it easy to reuse as a baseline.

## Limitations
- Self-reported: tasks cover only a subset of the field; action discovery uses only recent papers and may miss classic methods; still below experts on tasks needing clinical judgement, novel experimental reasoning or deep synthesis.
- **Coarse evaluation**: only a 12.5% LAB-Bench subset; the eight real tasks mostly use one backbone and are reported as relative gains; case-study "discoveries" (new TFs, sleep patterns) are checked only by the authors reading traces and code, not independently validated.
- The cloning benchmark is described inconsistently (10 tasks in Results vs. 20 open-ended questions and three experts in Methods).
- **No uncertainty, rerun-stability or claim-to-evidence checking**: conclusions carry no confidence and run-to-run stability is not analysed.
- Later independent evaluations show a limited ceiling: in HeurekaBench it is among the stronger of three single-cell agents yet scores only ~2.3–2.6/5 on open-ended correctness; in SpatialAgent v2's heart MERFISH annotation it shows label collapse toward endothelial cells (overall accuracy 0.394).

## Relation to our direction
Biomni sits at the **analysis-execution layer** of detect → model → revert: it neither detects anomalies nor builds a virtual tissue, but it is the de-facto baseline for "an agent that runs an omics analysis end-to-end and emits a biological conclusion." It matters most for **Plan B (trustworthy biomedical agents)**: it is the archetypal system to audit — one that autonomously writes code over kidney snRNA/snATAC/Xenium-like data and outputs "novel regulator / novel pattern" claims, yet has **no** claim-to-evidence checking, no calibrated confidence and no rerun-stability analysis. Its multiome case (snRNA+snATAC GRN, with hallucination judged by humans reading traces) is almost exactly the "verifier" setting Plan B wants to automate; it can be ported into kidney tasks: run Biomni on KPMP/Lake data for GRN or DE analysis, then have our verifier check each claim against the data, measure agreement across reruns, and file failures into an omics-specific taxonomy (batch/ambient RNA read as biology, regulation inferred from one modality, etc.). For **Plan A** the value is indirect: Biomni-E1's one-function-per-database and data-lake design is an engineering template for plugging KidneyAnomalyBench and KPMP/HuBMAP references into an agent environment — but its label collapse on spatial annotation is a warning, since in anomaly detection such systematic bias would absorb genuine lesion cell states into common classes. For the revert stage, its CRISPR screen-design task (choose perturbations from ~19k genes) and the wet-lab cloning loop are an early demonstration that "agent nominates perturbation → bench validates" is feasible as engineering.

## Reusable assets
- **Code:** open-source Biomni (environment + agent).
<https://github.com/snap-stanford/biomni>
- **Data:** all data used by Biomni (data lake etc.).
<https://doi.org/10.7910/DVN/CE4ZYG>
- **Web UI:** hosted demo (not for protected health information).
<https://biomni.stanford.edu>
- **Eval protocol:** prompts and metrics for the eight zero-shot real-world tasks (Methods), usable as Plan B baseline task templates.

## Follow-ups
- The tool inventory (Supp. Tables 1–30) and trace analyses (Supp. Figs 6–16) — which single-cell/spatial tools are already built in.
- Independent evaluations of Biomni in BiomniBench (`biomnibench-biorxiv-2026`) and HeurekaBench.
- The CodeAct paper, and later Biomni versions (RL training, multimodal inputs).

## Cite
```bibtex
@article{Huang2025_Biomni, title={Biomni: A General-Purpose Biomedical AI Agent}, url={http://dx.doi.org/10.1101/2025.05.30.656746}, DOI={10.1101/2025.05.30.656746}, journal={bioRxiv}, publisher={openRxiv}, author={Huang, Kexin and Zhang, Serena and Wang, Hanchen and Qu, Yuanhao and Lu, Yingzhou and Roohani, Yusuf and Li, Ryan and Qiu, Lin and Li, Gavin and Zhang, Junze and Yin, Di and Marwaha, Shruti and Carter, Jennefer N. and Zhou, Xin and Wheeler, Matthew and Bernstein, Jonathan A. and Wang, Mengdi and He, Peng and Zhou, Jingtian and Snyder, Michael and Cong, Le and Regev, Aviv and Leskovec, Jure}, year={2025}, month=June }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
