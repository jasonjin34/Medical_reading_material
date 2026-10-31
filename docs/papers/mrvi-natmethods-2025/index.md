# Deep generative modeling of sample-level heterogeneity in single-cell genomics

> **Bibkey** `Boyeau_2025` · **Venue** Nature Methods (2025) · **Category** single-cell · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02808-x> · `status: complete`

---

## One-liner
MrVI (multi-resolution variational inference, Yosef lab, built into scvi-tools) is a hierarchical deep generative model with two latent variables: **u** encodes cell state only (sample-agnostic), **z** adds sample effects on top of u (free of nuisance factors such as batch). Using **counterfactuals** — "what would this cell look like had it come from another sample?" — it stratifies samples at single-cell resolution (exploratory) and runs cluster-free DE and DA (comparative), finding sample-level differences that show up only in particular cell subsets in COVID-19, sci-Plex drug-screen and Crohn's disease cohorts.

## Problem
Single-cell cohort studies with hundreds of samples are increasingly common, but analyses usually cluster cells first and then compare per-cluster frequencies or pseudobulk — dependent on cluster resolution, missing effects confined to subsets of cells or spanning predefined clusters. Existing cluster-free DA/DE methods (Milo, miloDE) ignore embedding uncertainty; VAE models of sample covariates assume the effect is identical for every cell.

## Method
Covariates come in two kinds: the **target covariate** (usually sample ID, nesting disease status, treatment and all other sample-level attributes) and **nuisance covariates** (processing site, library technology, study of origin). Each cell n has uₙ (cell state, with a mixture-of-Gaussians prior rather than a unimodal Gaussian, helping large-scale integration and annotation) and zₙ = f(uₙ, sₙ) (**cross-attention / multi-head attention** models heterogeneous sample effects on cell state); expression xₙ is decoded from zₙ and nuisance covariates as negative binomial; trained by the ELBO. **Exploratory**: for each cell, counterfactuals p(zₙ | uₙ, s′) are computed; Euclidean distances between samples' counterfactual representations form a **per-cell sample-distance matrix**; cells are clustered by these matrices to find cell groups that induce the same sample stratification, and samples are hierarchically clustered. **Comparative**: DE — a linear model in z space regresses on sample groups and the decoder gives per-cell, per-gene LFCs; DA — per-sample posterior densities p(uₙ|s′) in u space are compared as log density ratios between sample groups. Multivariate regression can adjust for confounders (inflammation, sex, location). Ablations support the attention design (Supplementary Fig. 22).

## Data
(1) **Semi-synthetic**: 68k PBMCs (10x, 3,000 HVGs, five main clusters A–E) assigned to 32 synthetic subjects; subset A carries hierarchical DE along covariate 1, subsets B/C carry DA along covariate 2; (2) **COVID-19 PBMC**: ~419k cells from patients and healthy controls (Haniffa lab data); (3) **sci-Plex** (sci-RNA-seq3): 3 cell lines, 188 small molecules × 4 doses + vehicle, 2 biological replicates; "drug + dose" as target (752 "samples" per line), plate as nuisance; after filtering, 92 drugs × 4 doses = 368 perturbation samples, focus on A549; (4) **Crohn's disease**: 46 patients + 25 controls, ~463k cells, with tissue location, collection method and 10x chemistry metadata.

## Key results
- **Semi-synthetic**: z space shows subject effects only in subset A; subset A's averaged sample-distance matrix recovers the simulated hierarchy while other subsets show small, structureless distances; composition analyses based on PCA/scVI clusters do worse and introduce non-zero distances in effect-free subsets. DA identification beats Milo (PR curves); DE LFCs correlate highly with the DESeq2 pseudobulk "oracle", clearly beating miloDE. (Exact values are in figures, not the text.)
- **COVID-19**: u-space integration beats PCA and scVI; clustering by distance matrices gives three cell groups (myeloid monocytes/DCs, T/NK, B). Only the **monocyte/DC-induced stratification** further splits patients into two groups matching low/high days since symptom onset (DSS) (Mann–Whitney P < 0.05) — with no DSS input. DA: non-classical CD16⁺ monocytes and DCs decrease in patients; DE yields three gene modules (early interferon: GBP1, IFITM3, IFI27; later "return to baseline": CSF3R, LGALS2, HLA-DR; and TNF/NFKBIZ).
- **sci-Plex (A549)**: u space is drug-agnostic (mainly cell cycle), while HDAC inhibitors and trametinib form clear clusters in z space. MrVI sample distances agree better with the Connectivity Map and group doses of the same drug more tightly than two composition baselines; hierarchical clustering yields dose-dependent HDAC-inhibitor clusters and groups JQ1 (a BRD inhibitor) with two JAK2 inhibitors (fedratinib, TG101209) — consistent with reports that JQ1 inhibits JAK–STAT, and missed by the original study.
- **Crohn's stenosis (B2, 11 patients)**: inflammation has broad effects, while B2's effect is milder and confined to a few stromal subsets, strongest in a small HIGD1B⁺STEAP4⁺ pericyte population (CDH11, ADAMDEC1, COL1A1, LUM, PDGFRB, TGFBI up); endothelial populations decrease and ADAMDEC1⁺ fibroblasts increase; CD36⁺ endothelial cells upregulate PDGFRB in B2 with a mixed endothelial–pericyte phenotype, suggesting endothelial-to-mesenchymal transition (not reported originally).

## Contributions
- Models sample effects as cell-state-dependent (via attention) rather than a uniform shift.
- Uses counterfactuals to unify integration, sample stratification, DE and DA — all cluster-free, with uncertainty.
- "A sample-distance matrix per cell": different cell subsets can induce different sample stratifications, revealing locally expressed patient subtypes.
- One framework for patient cohorts and perturbation screens (target = drug × dose).

## Limitations
- RNA only; multimodal (e.g. ATAC) extension is only future work.
- Under hard integration (Crohn's: colon vs ileum, mucosa vs lamina propria), default settings preserve cell states worse than scVI; a label-aware variant is needed.
- DE/DA are inferred through the generative model; raw-data checks exist for some cases, but results are model-dependent; hyperparameters (u, z dimensions) were tuned with prior knowledge on sci-Plex.
- Few quantitative metrics in the text, mostly figure-based; discoveries (e.g. EndMT pericyte-like state) are not experimentally validated.

## Relation to our direction
MrVI spans the detect and model stages. **Detect**: its local DA (log density ratios) and per-cell sample-distance matrices answer "which cells, in which samples, deviate from normal" — a generative alternative to Milo (`healthy-ref-natgenet-2023`) and a single-cell, sample-level anomaly baseline for KidneyAnomalyBench. **Model**: the counterfactual structure (u unaffected by sample, z affected) is the manipulable representation a virtual tissue wants — "moving" a patient's cells into a healthy sample's condition and watching expression change is a computational prototype of the revert stage; the sci-Plex part shows drugs as target covariates to group perturbation effects. For **the artifact-injection topic**: kidney-biopsy data are typically multi-site and multi-batch; MrVI's nuisance/target split can treat processing batch as nuisance and patient as target, to test patient stratifications expressed only in certain nephron cells (e.g. injured proximal tubule); but MrVI is RNA-only, so cross-modal agreement with snATAC/Xenium must be checked separately. For **the agent-trustworthiness topic**: MrVI's DE comes from a generative model, not raw counts; if an agent cites model LFCs as evidence, a verifier should check for raw-data support (the paper does this itself, which can serve as the standard).

## Reusable assets
- **Software**: MrVI ships in scvi-tools.
<https://scvi-tools.org/>
- **Reproducibility code**:
<https://github.com/YosefLab/mrvi-reproducibility/tree/v0.1.0>
- **Data**: COVID-19 (Haniffa) h5ad, sci-Plex (figshare), Crohn's atlas (Broad Single Cell Portal SCP1884), 10x 68k PBMC.
<https://singlecell.broadinstitute.org/single_cell/study/SCP1884/human-cd-atlas-study-between-colon-and-terminal-ileum>
- **Metrics**: Connectivity Map concordance (silhouette) and intra-drug-across-dose distance percentile — reusable for evaluating perturbation representations.

## Follow-ups
- Model details and hyperparameter sensitivity in Methods and the supplement (Supplementary Tables 2–3).
- A head-to-head with Milo, miloDE and CNA on kidney data.
- Compare counterfactual prediction with perturbation models (Conditional Monge Gap in `scrna-natmachintell-2026`, `linear-baselines-natmethods-2025`).

## Cite
```bibtex
@article{Boyeau_2025, title={Deep generative modeling of sample-level heterogeneity in single-cell genomics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02808-x}, DOI={10.1038/s41592-025-02808-x}, number={11}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Boyeau, Pierre and Hong, Justin and Gayoso, Adam and Kim, Martin and McFaline-Figueroa, José L. and Jordan, Michael I. and Azizi, Elham and Ergen, Can and Yosef, Nir}, year={2025}, month=Oct, pages={2264–2274} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
