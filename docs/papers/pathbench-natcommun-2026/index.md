# A benchmark study of vision and pathology foundation models for computational pathology

> **Bibkey** `Bareja_2026` · **Venue** Nature Communications (2026) · **Category** foundation · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41467-026-76004-6> · `status: complete`

---

## One-liner
PathBench evaluates 32 foundation models — general vision (VM), general vision-language (VLM), pathology-specific vision (Path-VM) and pathology-specific vision-language (Path-VLM) — under one standardized frozen-feature + linear-probing protocol across 41 tasks, 53 datasets and >17,500 whole-slide images. Path-VMs lead, Path-VLMs lag, **neither model size nor pretraining scale consistently predicts downstream performance**, and late decision-level ensembling further improves robustness across datasets.

## Problem
Pathology foundation models exploded in two years (CTransPath, Phikon, UNI/UNI2, Virchow, Prov-GigaPath, H-optimus, CONCH, PLIP…), but each is self-evaluated on its own data, tasks and protocol, making them **mutually incomparable** and leaving two questions open: (1) how much does pathology-specific pretraining actually buy over general vision models, and where? (2) do these gains survive outside the training distribution (other institutions, stains, scanners)? Prior benchmarks compared only pathology encoders, or covered few cancer types and weakly-supervised classification only.

## Method
The unified protocol is the backbone: every model is **frozen** for feature extraction, only a **linear probe** is trained downstream, and slide-level predictions aggregate tile features by simple mean pooling — deliberately isolating *representation quality* from fine-tuning tricks. Models span four categories (VM / VLM / Path-VM / Path-VLM), three ViT scales (small/base/large) and three pretraining-data scales (small <0.1M slides, medium 0.1–1M, large ≥1M). The statistics are rigorous: pairwise Welch two-sample t-tests with FDR correction reporting ΔAUROC and 95% CIs; model ranking via task-wise pairwise Wald tests with bootstrap-estimated variance, summarized as performance score = (wins − losses)/(wins + losses) heatmaps. A **fusion model** — late decision-level ensembling of top models by majority voting — is evaluated alongside.

## Data
41 downstream tasks / 53 datasets / >17,500 WSIs, spanning diagnostic subtyping, biomarker status, **transcriptomic subtyping** and **pathway-activation** prediction, in both organ-specific and pan-cancer formulations, across brain, bladder, prostate, **kidney**, breast, lung and more. Evaluation is deliberately split into in-domain vs out-of-domain: **TCGA** (in-domain, 19 tasks) vs **CPTAC + external patch-level benchmarks + institution-specific out-of-domain cohorts** (22 tasks). Kidney appears only as cancer — the TCGA 4-class renal-cell-carcinoma subtyping task (ccRCC / ChRCC / PRCC1 / PRCC2; N=194 train, N=80 test).

## Key results
① **Path-VMs occupy the top tier on TCGA**: Virchow2, Prov-GigaPath, H-optimus-0, UNI and UNI2 consistently rank highest, with distinct tissue specializations — Virchow2 in colon/lung/prostate, Prov-GigaPath in breast/bladder, H-optimus-0 in pan-cancer, UNI in brain/bladder/breast. ② **Rankings shift off TCGA**: modest but consistent reordering on CPTAC and out-of-domain data shows in-domain strength ≠ generalization; the authors state plainly that TCGA very likely contributes to several models' pretraining, so TCGA scores mostly reflect in-domain performance. ③ **Differences among top models are often small and task-dependent**, mostly non-significant after pairwise testing. ④ **Path-VM > Path-VLM**, and Path-VMs remain competitive with general VMs — image–text supervision did not translate into classification advantage. ⑤ **Scale is not the answer**: neither parameter count nor pretraining slide count reliably predicts downstream AUROC. ⑥ **Ensembling works**: the majority-voting fusion model ranks **1st** on cumulative balanced accuracy across TCGA tasks and **2nd** across non-TCGA tasks, evidencing complementary strengths.

## Contributions
- The broadest pathology-FM comparison to date: 32 models × 4 categories × 41 tasks × 53 datasets under one comparable protocol.
- Explicit separation of in-domain (TCGA) from non-TCGA evaluation, treating leakage risk as a design premise rather than an afterthought.
- Task set goes beyond weakly-supervised classification into **molecular-level** prediction: pathway activation and transcriptomic subtyping.
- A rigorous statistical comparison framework (Welch + FDR, bootstrap Wald, win/loss heatmaps, 95% CIs) instead of a single column of means.
- An actionable conclusion: late decision-level ensembling beats chasing a single larger model.

## Limitations
- Linear probing only — benchmarks representation quality, not the ceiling under task-specific fine-tuning.
- Overlap between public data (TCGA/CPTAC) and pretraining corpora cannot be fully excluded, potentially inflating in-domain estimates.
- Scaling analyses use coarse proxies (parameter count, slide count) that ignore data composition and quality.
- Slide-level mean pooling can attenuate localized discriminative signals.
- **Every task is oncologic**; non-tumor disease (fibrosis, chronic organ disease) and **anomaly-detection-style** tasks are entirely absent from the benchmark.

## Relation to our direction
This paper sits on none of the detect → model → revert stages; it occupies the **orthogonal evaluation layer**: which backbone, and how to compare fairly. Three uses. **First, backbone selection**: our tissue-anomaly work needs a WSI encoder, and PathBench supplies statistically tested rankings plus tissue-specific strengths (note its only kidney task is RCC subtyping), showing UNI2/Virchow2/Prov-GigaPath/H-optimus-0 are one tier with often non-significant gaps — so **don't agonize over the pick, ensemble instead**. **Second, a protocol template** for any benchmark we build: frozen features + linear probe as the honest baseline, explicit in-domain vs out-of-domain split, pairwise statistical testing rather than bare means — all directly transferable to anomaly-detection or cross-modality prediction tasks. **Third and most important, its findings support "the bottleneck is not model capacity"**: scale does not predict performance, pathology VLMs underperform, and ensembles beat single models — consistent with this repo's direction and an argument for investing in data quality and evaluation protocol over bigger models. **The gap is the opportunity**: all 41 tasks are oncologic; non-tumor disease and anomaly-detection tasks are absent from this ecosystem — exactly the slot this direction can fill.

## Reusable assets
- **Code:** MIT-licensed, including processed benchmark results and figure source data; parts adapted from facebookresearch/dino (Apache-2.0).
<https://github.com/gevaertlab/benchmarking-path-models>
- **Live benchmark:** the PathBench leaderboard.
<https://pathbench.stanford.edu/>
- **Data:** TCGA (GDC portal), CPTAC (CPTAC Data Portal), NLST (The Cancer Imaging Archive) and other external / out-of-domain cohorts.
- **Eval protocol:** frozen features + linear probe, mean-pooling slide aggregation, Welch t + FDR, bootstrap Wald pairwise wins/losses with performance score, majority-voting fusion.

## Follow-ups
- Read the two prior benchmarks it compares against (refs 50/51) and the recent five-cancer benchmark (ref 60) for task-design differences.
- Pull the original Virchow2 / Prov-GigaPath / H-optimus-0 papers to fill the Path-VM entries this repo lacks (virchow-2024 and uni2-h-model are already in).
- Run their repo to see whether the linear-probe pipeline can be pointed at non-tumor tasks and anomaly scores directly.

## Cite
```bibtex
@article{Bareja_2026, title={A benchmark study of vision and pathology foundation models for computational pathology}, volume={17}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-026-76004-6}, DOI={10.1038/s41467-026-76004-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Bareja, Rohan and Carrillo-Perez, Francisco and Zheng, Yuanning and Pizurica, Marija and Nandi, Tarak Nath and Tian, Lu and Shen, Jeanne and Madduri, Ravi and Gevaert, Olivier}, year={2026}, month=July }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
