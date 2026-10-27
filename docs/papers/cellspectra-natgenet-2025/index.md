# Analysis of individual patient pathway coordination in a cross-species single-cell kidney atlas

> **Bibkey** `Klotzer_2025` · **Venue** Nature Genetics (2025) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41588-025-02285-0> · `status: complete`

---

## One-liner
Two things: (1) **SISKA 1.0** — a cross-species single-nucleus kidney atlas (human, mouse, rat; >1M cells, >140 samples) with 21 main cell types and ~80 cross-species-conserved cell states; (2) **CellSpectra** — a **single-sample** statistic: for each cell type × pathway, the first SVD axis of the reference samples' pseudobulk matrix defines the "coordination pattern"; a query sample is regressed onto it, and lowered R² plus a χ² test flags loss of coordination in that sample. This powers a **patient-level single-cell functional profiling report**, rodent-model selection for a patient, and — in a folic-acid kidney-injury model — the CellSpectra-nominated TNF pathway was targeted with etanercept, improving kidney function.

## Problem
Bringing single-cell data into the clinic requires finding cell-type-specific, targetable changes in **individual patients** and knowing which animal model best mirrors a given patient. Existing pathway analyses aggregate single-gene mean/variance changes (e.g. GSEA) and suffer from sparsity, technical variability and single-sample statistics; the correspondence between rodent models and patients is not quantified.

## Method
**SISKA integration**: ~12k one-to-one orthologues; scVI integration of human (H-CKD, DKD, AKI, healthy), mouse (AKI time course, DKD, folic acid) and rat (ZSF1 diabetic, DOCA hypertensive) snRNA-seq; MetaMarker for conserved markers, MetaNeighbor for independent validation; cell-state resolution chosen by requiring presence in ≥2 species. **CellSpectra**: for a cell type and gene set, a sample × gene pseudobulk matrix (≥10 cells per sample, normalized + log); SVD on the reference, first gene-loading vector v* as an "eigensample"; each query sample is regressed on v* to get R²; the reference R² distribution comes from **leave-one-out** (to avoid double-dipping); significance is parametric — residuals ε_sg ~ N(0, σ_g²) with σ_g estimated from reference residuals, the query's standardized squared residual sum follows χ² with G−1 df, per-gene contribution capped at CHISQ.MAX = 4 for robustness; FDR correction. **On-the-fly reference**: for each query, reference cells are subsampled to match its total counts (3 pseudo-replicates) to stop cell-number/capture-rate inflation. **Driver genes**: ranked by standardized residuals (report_genes()). **Quality report**: LOO R² mean/median/SD and variance explained by v*.

## Data
SISKA: >1M cells, >140 samples, three species; extended human atlas: 150 healthy and diseased samples, >700k cells (including Penn nephrology biopsies and KPMP), labels transferred with scANVI; profiling compares >100 patient samples to 47 healthy references. Public data: KPMP, GSE211785, GSE209821 (ZSF1 rat), GSE183839 (DOCA rat), GSE184652 (DKD mouse), GSE139107 (mouse AKI time course), new GSE291551; an NSCLC atlas (CELLxGENE).

## Key results
- **Atlas**: 21 main cell types, >900 conserved markers (852 unique to one type), ~80 conserved states; humans have markedly fewer PTS3 cells.
- **Coordination**: for most functional gene sets v* explains >75% of variance; "Regulation of glomerular filtration" is highly concordant in rodent vs human podocytes but not other cell types; PEC "Regulation of protein kinase C signaling" is more human-like in rat than mouse; **no single rodent model is best across all functions**.
- **Single-sample detection**: in the mouse AKI time course, PT "Response to ischemia" loses coordination at 4 h and 12 h after reperfusion but not at later times or in diabetic mice; the more severe db/db + AAV-Renin model has more affected pathways than db/db.
- **Treatment effects**: podocyte coordination changes in diabetic rats are almost fully reversed by an sGC activator but not a stimulator (matching phenotypes in the original study); podocyte "SMAD protein signal transduction" is restored only by the activator.
- **Experimental validation**: in folic-acid mice the number of significant gene sets tracks PT histological damage; CellSpectra detects mTOR and TNF changes in most samples where GSEA finds few; **etanercept (TNF inhibitor) significantly lowered BUN** in folic-acid injury (n = 5 per group). The authors note CellSpectra itself does not give the direction of change.
- **Patient profiles**: PT "Vasculature Development" is altered in >70% of diseased samples; hypertensive patients show DCT_CNT_CD "Sodium Ion Transport" changes (SCN3A, SLC23A2, SLC24A1, SCNN1B; NEDD4L) absent in non-hypertensives; ADPKD has the highest prevalence of TNF and mTOR changes and "Water Transport" changes with CFTR/aquaporins (consistent with tolvaptan efficacy); in lung cancer, malignant cells show far more coordination changes than non-malignant epithelium, LUSC more than LUAD.

## Contributions
- A **single-sample, statistically calibrated** pathway-level deviation test: not "up/enriched" but "does the relative expression pattern among genes deviate from the reference".
- Uses cross-species conservation to set cell-state resolution, and coordination R² to quantify functional similarity between rodent models and patients.
- On-the-fly reference subsampling controls cell-number/depth confounding; every query ships with a quality report.
- Closes the loop from computational nomination to animal intervention (etanercept).

## Limitations
- Linear assumptions (SVD + regression) may miss non-linear structure; multiple computational layers risk overfitting (acknowledged).
- Detects loss of coordination but **not direction**; relies on GO/KEGG gene sets not designed for coordination; rare cell types suffer from sparsity.
- Cross-species limited to ~12k orthologues; most human predictions lack interventional validation; missing clinical metadata such as medication; references not yet age/sex-matched.
- Thousands of sample × pathway × cell-type tests: multiple testing and dependence make "number of significant pathways" a severity proxy to use with care.

## Relation to our direction
CellSpectra is essentially a **single-sample anomaly detector at cell-type × pathway granularity**: reference = healthy coordination pattern, anomaly = standardized residuals of a query relative to it (χ² test), plus driver-gene explanations — nearly an off-the-shelf single-cell version of the "interpretable, calibrated patient-level anomaly report" **Topic 1** wants. Directly reusable: (1) **a strong Topic 1 baseline** — run CellSpectra on snRNA from the kidney samples to be tested (or KPMP / Lake 2023 disease samples) with KPMP/Lake healthy samples as reference; our method should beat it on expert-validated anomalies or at least add spatial/cross-modal dimensions it lacks; (2) **on-the-fly reference subsampling** addresses "false anomalies from cell-number/capture differences" — a confound KidneyAnomalyBench must test; (3) its χ² single-sample test and quality report are a comparable implementation of a "calibrated anomaly score"; (4) **cross-modal extension** is our increment: CellSpectra sees only snRNA, whereas consistent deviation in other modalities from the same patient (e.g. chromatin accessibility or spatial omics) is what makes disease more likely than artifact. For **detect → model → revert** it walks the whole chain: detect loss of coordination → pick the matching model cross-species → block TNF with etanercept and improve BUN (wet-lab revert validation); the sGC activator "reversing" podocyte coordination shows **coordination recovery as a revert readout**. For **Topic 2**: the Functional Profiling Report is exactly what an agent might be asked to produce or interpret; its admission that it gives no direction is a classic overclaim a claim-to-evidence verifier must catch (e.g. an agent calling a "coordination change" a "pathway activation").

## Reusable assets
- **Code:** CellSpectra R package and tutorials; SISKA integration and reproduction code.
<https://github.com/kloetzerka/CellSpectra> · <https://github.com/susztaklab/SISKA>
- **Data:** five atlases (SISKA, human extension, human/mouse/rat-only) and unpublished human biopsy snRNA on Zenodo (paper ref. 97); GEO: GSE211785, GSE209821, GSE183839, GSE184652, GSE139107, GSE291551.
- **Web tool:** cross-species gene expression and R² browser.
<http://www.susztaklab.com>

## Follow-ups
- Dumoulin 2026 DKD spatial atlas (same lab) — extend CellSpectra to niche/microenvironment-level coordination.
- Compare with Padvitski 2026 continuous damage scores (PDS): supervised damage direction vs direction-free coordination deviation.
- MetaNeighbor / MetaMarker papers; single-sample pathway baselines (e.g. singscore, GSVA).

## Cite
```bibtex
@article{Klotzer_2025, title={Analysis of individual patient pathway coordination in a cross-species single-cell kidney atlas}, volume={57}, ISSN={1546-1718}, url={http://dx.doi.org/10.1038/s41588-025-02285-0}, DOI={10.1038/s41588-025-02285-0}, number={8}, journal={Nature Genetics}, publisher={Springer Science and Business Media LLC}, author={Klötzer, Konstantin A. and Abedini, Amin and Li, Shen and Balzer, Michael S. and Liang, Xiujie and Levinsohn, Jonathan and Ha, Eunji and Dumoulin, Bernhard and Hogan, Jonathan J. and Quinn, Ghazal and Bloom, Roy D. and Schuller, Max and Eller, Kathrin and Halmos, Balazs and Zhang, Nancy R. and Susztak, Katalin}, year={2025}, month=Aug, pages={1922–1934} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
