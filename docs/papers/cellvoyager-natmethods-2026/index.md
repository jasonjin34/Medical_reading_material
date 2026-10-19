# CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data

> **Bibkey** `Alber_2026` · **Venue** Nature Methods (2026) · **Category** agents · **Relevance** high · **Access** paywall
> **Link** <https://doi.org/10.1038/s41592-026-03029-6> · `status: complete`

---

## One-liner
CellVoyager (Zou lab, Stanford) is an agent that autonomously explores scRNA-seq data inside a Jupyter notebook: given a published paper and its data, it extracts which analyses were already done, then generates **different** hypotheses and analysis plans ("exploration blueprints"), self-critiques, executes code, reads figures with a vision-language model and replans. It beats its base LLMs on CellBench at predicting the analyses authors performed, and in three re-analysis case studies scored by the original authors it surfaced new hypotheses such as elevated pyroptosis scores in CD8+ T cells in COVID-19 and transcriptional noise in the aging SVZ.

## Problem
Existing single-cell agents (CellAgent, CompBioAgent, AutoBA, BIA) mainly execute user commands, so they are bounded by the user's imagination and ignore analyses the researcher has already done — limiting them as collaborators. Vast published scRNA-seq data likely hide unexplored signal, but systematic manual re-analysis is infeasible. Can an agent, **conditioned on prior analyses**, autonomously propose and run new, biologically meaningful ones?

## Method
**Inputs**: a processed scRNA-seq AnnData, a background report (here the full published paper) and a Python environment spec (scanpy, scvi-tools, celltypist, …). The agent first summarises the paper into "biological background / analyses performed / dataset details" and uses only that summary thereafter. **Exploration loop**: generate a blueprint (hypothesis + stepwise plan + first-step code) → self-critique and revise (one round here) → append code cells to the notebook and execute; on error, up to 3 fix attempts, else replan around it; on success, text and image outputs go to a VLM whose interpretation is written back as markdown and drives replanning; at most 8 steps per analysis (typically 5–8 in the case studies). Analyses run sequentially, each conditioned on the list of past hypotheses to avoid repeats; a final report picks the most promising results. **CellBench**: gemini-2.5-pro-preview extracts each paper's background and all single-cell analyses; given only the background, a model/agent predicts the analyses, and an LLM judge scores matches (two PhD students re-checked 47 outputs, agreeing with the judge 89% and 85%). For CellBench, only CellVoyager's ideation stage runs (no code).

## Data
**CellBench** (preprint): 50 published papers focused on scRNA-seq, 483 analyses; the published abstract reports 76 studies. **Cases**: (1) a COVID-19 PBMC atlas (7 severe patients + 6 healthy controls); (2) a human endometrium menstrual-cycle atlas (73,180 cells, 29 donors, Fluidigm C1 + 10x); (3) adult mouse subventricular zone (SVZ) scRNA-seq across ages with single-cell aging clocks. Each case generated 8 analyses; the 5 with the highest fraction of successfully executed cells went to one original author for rubric-based review.

## Key results
**CellBench (preprint)**: with GPT-4o as engine, CellVoyager beats GPT-4o itself by **16%** micro-averaged (p<0.01) and **19.33%** macro-averaged (p<0.001); the o3-mini engine is slightly lower but not significantly so, and o3-mini is used for the case studies. Published abstract: up to **23%** over GPT-4o and o3-mini on 76 studies. **Expert review (15 analyses)**: mean creativity **2.8/4** (COVID 2.8, endometrium 3.4, SVZ 2.4); **12/15** hypotheses judged worth further study (the preprint abstract says 80%); "biologically meaningful" 3/5, 2/5, 3/5 respectively. **Findings**: elevated pyroptosis gene scores in COVID-19 CD8+ T cells (p=0.001; redone after the original author asked for donor-level pseudobulking first); in endometrium, after author feedback, 40 ligand–receptor correlations with TGF-β and FGF2–FGFR1 on top; in SVZ, only a marginal noise–age correlation in astrocyte-qNSCs (r=0.047, p=0.0135), but a young-vs-old split across all cell types shows significantly higher transcriptional noise in oligodendrocytes, microglia and mural cells (p<0.001). Control: Google Colab's Data Science Agent produced no meaningful results on the same inputs. Each analysis takes ~30 min.

## Contributions
- **Exploration conditioned on prior analyses**: the paper is a map of covered ground and the agent seeks the gaps — a clean problem definition for autonomous re-analysis of public data.
- Notebook-native auditable traces: each step = description + code + output + VLM interpretation; the notebook is the full report.
- CellBench: a scalable benchmark of ideation quality via "predict the analyses the authors performed."
- Review by the original authors plus human-in-the-loop feedback (1–2 comments meaningfully improve analyses).

## Limitations
- Small review: 3 papers × 5 analyses, one author reviewer each, unblinded and with no comparable review of a baseline agent; "findings" are unvalidated and some are weak (SVZ r=0.047).
- **Statistical rigour relied on humans**: the initial COVID analysis tested at cell level until the author asked for donor-level pseudobulking — classic single-cell pseudo-replication that the agent did not catch itself.
- CellBench relies on LLM extraction plus an LLM judge and measures ideation, not execution correctness.
- Sequential, ~30 min per analysis; leans on popular packages like scanpy and adapts poorly to niche/in-house tools; scRNA-seq only. In HeurekaBench's independent evaluation it trails Biomni and BixBench-Agent on open-ended questions because of fixed step budgets and limited code-fixing.

## Relation to our direction
CellVoyager's setting — "given a published paper and its data, find analyses the authors did not run" — is isomorphic to a **Plan A** sub-problem: systematically searching public data such as KPMP / the Lake kidney atlas for anomalous cell states or disease programmes the original papers did not report. But it also shows exactly where such "autonomous discovery" needs constraints: it tests cells as independent samples (pseudo-replication), reports weak signals like r=0.047 as findings, and novelty is scored only subjectively by the original author. For **Plan B** it is an ideal **audit target**: its notebook trace places the "claim" (markdown interpretation) next to the "evidence" (code + output + figure), which is exactly the input a claim-to-evidence checker needs — does each VLM interpretation follow from its output, is the statistical unit right (cell vs. donor), do reruns reach the same conclusion. These error types (pseudo-replication, effect-size inflation, single-modality inference, treating VLM figure-reading as evidence) can become entries in the omics failure taxonomy directly. On the detect → model → revert chain it sits at "data to hypothesis"; its outputs should pass data-level reliability filters (QC, batch, ambient RNA) and the verifier before entering perturbation/reversion ranking.

## Reusable assets
- **Code + CellBench:** case-study code and the CellBench evaluation set.
<https://github.com/zou-group/CellVoyager>
- **Preprint full text:** includes all prompts (Appendix Figs 3–17).
<https://doi.org/10.1101/2025.06.03.657517>
- **Review rubric:** creativity (1–4) / biologically useful / correct methods / worth following (Appendix Fig. 1), adaptable as a Plan B human-annotation rubric.

## Follow-ups
- The published version's extensions: 76-study CellBench and the expert-evaluation details ("consistently rated creative and scientifically sound").
- HeurekaBench's failure analysis of CellVoyager (fixed steps, code fixing).
- Comparator single-cell agents: CellAgent, BIA, AutoBA.

## Cite
```bibtex
@article{Alber_2026, title={CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data}, volume={23}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-026-03029-6}, DOI={10.1038/s41592-026-03029-6}, number={4}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Alber, Samuel and Chen, Bowen and Sun, Eric and Isakova, Alina and Wilk, Aaron J. and Zou, James}, year={2026}, month=Mar, pages={749–759} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
