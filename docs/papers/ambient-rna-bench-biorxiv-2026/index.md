# Benchmarking computational decontamination of ambient RNA

> **Bibkey** `Cargnelli_2026` · **Venue** bioRxiv (2026) · **Category** single-cell · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.64898/2026.01.13.699237> · `status: complete`

---

## One-liner
An independent benchmark using simulations, species-mixing experiments of three complexities, a mouse-kidney strain (genotype) mixing experiment and contamination-free negative controls to evaluate 7 ambient-RNA decontamination methods (CellBender, DecontX, FastCAR, scAR, scCDC, SoupX, CellClear) on how much ambient RNA they remove, how much endogenous RNA they keep, and how they change downstream interpretation; no method wins everywhere — CellBender, DecontX (full mode) or SoupX (reduced mode) are recommended — and default decontamination of clean data risks over-correction.

## Problem
Ambient RNA in single-cell/single-nucleus RNA-seq (sxRNA-seq) — RNA released by lysis during dissociation, shearing or detergents, plus barcode swapping in multiplexing, cross-well contamination and reagent contamination — distorts cell classification and gene-level inference. Many decontamination tools exist but no independent benchmark covers them all across datasets; meanwhile standard pipelines such as nf-core run decontamination routinely, **lowering the threshold for applying probabilistic background correction without dataset-specific evaluation** and raising over-correction risk.

## Method
**Ground truth**: in species mixing, UMIs on minor-species genes are ambient and on major-species genes endogenous (keeping cells with ≥75% UMIs from one species); in mouse strain mixing, genotype-specific SNPs (≥2 counts) decide; simulations draw from negative binomials fitted to three cell lines, sampling contaminating UMIs from other types' distributions at a set ambient fraction; negative controls are Smart-seq2 islets and contamination-free simulations. **Two core scores**: the ambient removal score (ARS) and endogenous retain score (ERS), both 0–1. **Downstream evaluation**: neighbourhood quality (Milo purity, LISI), marker selectivity (entropy, Moran's I, Gini), Harmony integration (bASW, batch LISI, PCR, ARI), Azimuth label transfer (high-confidence fraction, ARI, cASW, RMSE). Default parameters throughout; SoupX/DecontX also run in a filtered-matrix-only "reduced" mode; scAR's full mode was computationally intractable.

## Data
7 datasets, 66 samples, 135,314 cells: low-complexity species mixing (10x human 293T + mouse 3T3), medium complexity (human islets spiked with human Jurkat + mouse 32D, GSE147203), high complexity (human islets xenografted into mouse kidney), **a three-strain mouse-kidney mixture** (C57BL/6, 129S1/SvImJ, CAST/EiJ; GSE218853), a Smart-seq2 islet negative control (E-MTAB-5061), and simulations. All public.

## Key results
- **Ambient RNA is pervasive**: across 49 real samples and 97,357 cells/nuclei, 81.56% carry some ambient RNA; **single-nucleus samples average 10.59% vs 5.21% for single-cell**; variation is large within samples, between samples and between studies (mean QCD 0.314 / 0.319 / 0.171).
- **Sources**: a gene's ambient load correlates strongly with its empty-droplet expression (mean R = 0.857); the 10% most frequently expressed genes contribute 82.30% of ambient RNA on average — mostly ubiquitous mature cytoplasmic mRNA. Common QC metrics (exonic, mitochondrial, ribosomal fractions) relate only weakly to per-cell ambient load; even among the top-10% UMI cells, 2.64% are strongly affected (>10% ambient UMIs) — **stringent QC cannot eliminate it**.
- **Removal vs retention**: scAR (mean ARS 0.679) and CellBender (0.604) remove the most ambient RNA, but **scAR also strips ~0.445 of endogenous signal** (mostly low-expressed genes); on contamination-free controls methods remove about as much endogenous signal as on contaminated data. SoupX reduced mode removes more with similar retention; DecontX reduced mode removes slightly less but retains more.
- **Downstream interpretation**: in the most contaminated simulation, only CellBender improves unsupervised recovery of true cell types; DecontX and scAR bring marker module scores close to ground truth (but also "improve" them on clean data, indicating a bias towards cell-type-specific expression); CellBender, scAR, SoupX and DecontX improve neighbourhood quality with negligible effect on negative controls; **scAR worsens integration and markedly affects integration and label transfer on negative controls**. scCDC and FastCAR remove mainly from highly expressed genes with no downstream benefit; CellClear removes about as many endogenous as ambient counts.
- **Recommendations**: ample compute → CellBender (GPU, long runtime, high memory, does its own cell calling); scalability or a specific cell-calling method needed → DecontX full mode; no prior expectation of contamination, or only filtered matrices → SoupX reduced mode (least prone to over-correction when contamination is absent). Priors can come from experiment (snRNA is usually more contaminated) or tools such as AmbiQuant.

## Contributions
- The first independent benchmark across 7 methods and multiple ground-truth designs, explicitly including **contamination-free negative controls** to measure over-correction.
- Separates "removal" and "retention" into two scores (ARS/ERS) and exposes systematic biases toward high- or low-expressed genes.
- Provides an actionable decision rule (compute, available matrices, contamination prior).

## Limitations
- Default parameters only, no tuning; scAR full mode did not finish.
- Only three Smart-seq2 negative-control samples (others could not run through all methods).
- Species/strain-mixing ground truth only sees cross-species/cross-genotype contamination, not within-genotype; simulations use only three cell lines.
- Preprint, not peer-reviewed; abstract versions differ on the recommended methods (see header); the code repo is described as "will be made" available.

## Relation to our direction
For **Topic 1**: kidney-biopsy omics commonly uses **snRNA** (single-nucleus), and this paper shows single-nucleus data carry about twice the ambient contamination of single-cell (10.59% vs 5.21%), dominated by the most ubiquitously expressed mRNAs — in kidney that typically means abundant tubular transcripts "leaking" into every cell type. This directly manufactures false anomalies (e.g. immune cells or podocytes "expressing" PT markers), so ambient RNA should be an explicit source in KidneyAnomalyBench's "technical artifact" class. Usable designs: **(1)** the ARS/ERS + negative-control framework converts directly into an evaluation of "are anomalies stable after de-artifacting, and does decontamination introduce false anomalies on clean data?"; **(2)** the paper's mouse-kidney strain-mixing data (GSE218853) give **real ground truth for ambient RNA in kidney**, usable to calibrate an anomaly detector's sensitivity to ambient artifacts; **(3)** cross-modal agreement — paired snATAC is not affected by the same RNA-release mechanism, so an "anomaly" present in snRNA without corresponding accessibility in the same nucleus's ATAC may flag an ambient artifact (this inference is our hypothesis; the paper does not test ATAC). **Over-correction is equally dangerous**: some methods artificially sharpen cell-type specificity, which could "clean away" genuine mixed/transitional states such as injured PT. For **Topic 2**: "decontamination switched on by default in the pipeline without checking whether contamination exists" is a very concrete agent failure mode, and the paper's decision rule (establish a contamination prior, choose by available matrices) can be written directly as verifier checks.

## Reusable assets
- **Code:** benchmark repository (stated to be released, with all scripts and the dataset list).
<https://github.com/madsen-lab/AmbientRemovalBenchmark>
- **Data:** mouse-kidney strain mixing (GSE218853) — ground truth for kidney ambient RNA; species mixing GSE147203; negative control E-MTAB-5061.
<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218853>
- **Eval protocol:** ARS/ERS dual scores + negative controls + four downstream task families.

## Follow-ups
- The CellBender, DecontX and SoupX papers; AmbiQuant (sample-level contamination estimation).
- The original study behind GSE218853 (mouse-kidney strain mixing) and how it defines ambient ground truth.
- Contrast with spatial spillover/diffusion correction (`resolvi-natmethods-2026`, `xenium-split-natmethods-2026`): both are "signal from the wrong cell", with different mechanisms.

## Cite
```bibtex
@article{Cargnelli_2026, title={Benchmarking computational decontamination of ambient RNA}, url={http://dx.doi.org/10.64898/2026.01.13.699237}, DOI={10.64898/2026.01.13.699237}, journal={bioRxiv}, publisher={openRxiv}, author={Cargnelli, Cecilie Bøgh and Nielsen, Jakob Vennike and Skat Madsen, Jesper Grud}, year={2026}, month=Jan }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
