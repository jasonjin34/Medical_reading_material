# Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup

> **Bibkey** `Dumoulin_2026` · **Venue** Nature (2026) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41586-026-10363-4> · `status: complete`

---

## One-liner
CosMx (1k genes) and **Xenium (5k genes)** single-cell spatial transcriptomics on 64 FFPE kidney samples from 58 patients, integrated with a 150-patient snRNA-seq reference via scVI/scANVI into a >5-million-cell cross-platform DKD spatial atlas; it defines 11 reproducible tissue niches and cell-centred "microenvironments", finds a **profibrotic injured-tubule microenvironment** that expands with disease and tracks lower eGFR, and within it a **B cell-predominant, TLS-like immune microenvironment** marking a faster-progressing DKD subset (B+ DKD, ~8.4%) — yielding a tissue gene signature and a 14-protein plasma panel (UK Biobank external AUC 0.70 vs KFRE 0.63).

## Problem
DKD is the leading cause of kidney failure (develops in ~40% of people with diabetes) but is clinically and molecularly heterogeneous (rapid decline to long-term stability), hampering therapy development and patient selection. Age, sex, eGFR and albuminuria predict outcomes but reveal little biology; genetic risk scores add little; circulating TNFR1/2 track decline but the cellular/spatial context of intrarenal inflammation is unclear. The authors argue that cellular-resolution, near-genome-wide spatial transcriptomics can make tissue architecture computable and reveal pathological subtypes directly from biopsies.

## Method
**Integration**: CosMx 1k (n = 48, +50 custom probes) and Xenium 5k (n = 16, +100 custom probes) share 656 transcripts; each is integrated with the 150-patient snRNA-seq reference via scVI (NB likelihood, 4 hidden layers, 30-d latent) + scANVI (best on the scIB benchmark); **the mean latent distance from each spatial cell to its 10 snRNA nearest neighbours is computed and high-distance cells are discarded before reintegration**; final 3,386,822 CosMx + 951,041 Xenium cells, with 3,000 HVGs imputed from the scANVI latent space. Leiden + marker annotation yields 20 cell types; iPT/PT and iTAL/TAL split by injury signatures. **Niches**: neighbourhood composition aggregated over 20–80 µm radii, ML clustering → 11 niches consistent across platforms; orthogonal validation with COVET (local gene covariance + approximate optimal transport) and NicheCompass; Hotspot for spatial gene–gene correlation and differential correlation. **Microenvironments**: clustering of a given centre cell type (injured tubule iTEC, immune cells) by its neighbourhood. **Downstream**: CellPhoneDB v5 correlated with eGFR/HAVCR1/COL1A1; validation in 843 tubulointerstitial bulk RNA-seq samples; IMC protein validation; integration with a single-cell B cell atlas; IgA immunoprecipitation–MS; TRIDENT B+/B− split by Ward clustering on a 10-gene B cell signature with Kaplan–Meier; elastic-net logistic (SMOTE, 5-fold CV) on plasma proteomics, then Cox models and UK Biobank external validation.

## Data
Spatial: 64 FFPE samples / 58 patients (26% female, mean age 57.3, full GFR range; includes healthy paediatric kidneys); CosMx paired with PAS, Xenium with H&E. snRNA-seq reference: 150 samples, 720,924 cells. Integrated: >5M cells, >200 patients. Validation: Susztaklab Biobank 843 bulk RNA-seq (with pathologist fibrosis scores), TRIDENT (n = 248; B+ 17 / B− 231; plasma proteomics B+ 13 / B− 182), UK Biobank 3,309 participants with diabetes.

## Key results
- **Cell types**: 20, with cross-platform conserved injury markers — iPT: SOX4, VCAM1, HAVCR1; iTAL: CLU, SLPI, ITGB6; Xenium's higher resolution detects lymphatic endothelium.
- **11 niches**: eGFR correlations — DCT r = 0.61, PT r = 0.52 (positive); immune r = −0.59, iPT r = −0.55 (negative); in DKD, glomerular-niche mesangial and immune cells rise modestly (P = 0.047 / 0.029) and correlate (r = 0.32); NRG1–ERBB3 tracks better function, PLAU–PLAUR and IL-6–IL-6R are enriched in severe disease.
- **Five injured-tubule microenvironments** (proximal, distal, periglomerular, perivascular, profibrotic); the **profibrotic** one is rich in immune and fibroblast neighbours, centred on MMP7+/HAVCR1+/HIF1A+ iPT and MMP7+/ANXA2+/CLU+/ITGB6+ iTAL, expands in DKD and anti-correlates with eGFR (r = −0.6, P < 0.001), with Sirius Red confirming collagen; HBEGF–EGFR and TNFSF10–TNFRSF10B track HAVCR1, JAG2–NOTCH2 and PDGFβ–PDGFRβ track COL1A1 (validated in 843 bulk samples).
- **Immune atlas**: 11 immune types; in DKD plasma cells ×3.1 and B cells ×2.4; in healthy paediatric kidneys most immune cells sit in a "residential" microenvironment dominated by anti-inflammatory macrophages (MRC1, CD163 …), proportionally stable in DKD.
- **B cell-predominant TLS-like microenvironment**: embedded in the profibrotic tubular niche, with CXCL13–CXCR5 and TNFSF13B–TNFRSF13C co-expression, CXCR5+/PDCD1+ TFH-like CD4 T cells, IMC-confirmed CD20+ B with CD4+ T and Ki-67+ proliferating B cells, strong IgD+ naive B enrichment (P = 2.38 × 10⁻¹¹), and AICDA/IRF4 detected by Xenium; IgA immune complexes are enriched for granzymes and complement (C3, C4A, C8B).
- **Translation**: the B cell signature correlates with interstitial fibrosis; in TRIDENT, B+ DKD (8.4%) reaches renal end-points faster over three years (log-rank P = 0.02); the 14-protein B+ DKD plasma panel beats clinical-only Cox models, with UK Biobank external AUC 0.70 vs KFRE 0.63 and markedly higher risk in the top quartile.

## Contributions
- One of the largest human kidney single-cell spatial datasets to date, unifying CosMx + Xenium + snRNA across platforms and modalities.
- Two-level spatial abstraction — multicellular "niches" and cell-centred "microenvironments" — with orthogonal COVET/NicheCompass validation.
- A complete translational chain: spatial discovery (B cell TLS-like niche) → bulk signature → plasma protein panel → biobank validation, proposing biomarker-stratified B cell-targeted trials.

## Limitations
- Panels are not genome-wide (1k / 5k); 3,000 genes are **imputed** from the snRNA reference via scANVI, and imputed expression feeds DEGs, pathways and ligand–receptor analysis — potentially importing reference bias into spatial conclusions.
- **Spatial cells far from the snRNA reference are discarded** during integration — which may remove exactly the genuinely novel or anomalous cells.
- The B+ group is small (17 in TRIDENT, 13 with plasma), associations are not causal, SMOTE on a tiny positive class risks optimism; CosMx and Xenium sample counts are imbalanced (48 vs 16).
- Full spatial data released only upon publication (Zenodo DOI reserved); limited healthy controls (including paediatric kidneys) may confound age with disease.

## Relation to our direction
This is almost isomorphic to **the artifact-injection topic's** data: Xenium 5k + H&E + an snRNA reference matches a multi-modal design of this kind (snRNA + snATAC + Xenium + H&E), so its pipeline (scVI/scANVI integration, 20–80 µm multiscale neighbourhoods, niche/microenvironment abstraction, COVET/NicheCompass validation) is a direct baseline for our spatial analysis. From the **detect** perspective, though, it exposes two issues that are the artifact-injection topic's entry point: (1) **it discards spatial cells far from the reference as an integration-quality problem** — for anomaly detection these are precisely the candidates; the artifact-injection topic should make "latent distance to reference" an explicit anomaly score and use cross-modal agreement (is the H&E morphology / snATAC accessibility at that location also abnormal?) to decide segmentation/probe artifact vs disease signal, rather than dropping them; (2) it relies on **imputed expression** downstream, so KidneyAnomalyBench should include checks for imputed-vs-measured disagreement. Its B cell TLS-like niche is an excellent **"known rare anomaly" gold standard**: present in only ~8.4% of patients, spatially clustered, with IMC protein evidence — usable as a seeded/expert-validated finding to test whether an unsupervised detector ranks it in the top-k (matching the NIH Kidney AI challenge's judging metrics). For **model → revert**: the profibrotic ligand–receptor axes (HBEGF–EGFR, JAG2–NOTCH2, PDGFβ–PDGFRβ) and B cell targeting are candidate "revert" perturbations; a virtual tissue could simulate whether blocking them shifts microenvironment composition back toward the healthier proximal/distal states. For **the agent-trustworthiness topic**, the conclusion chain (spatial → bulk → plasma → biobank) is good material for multi-hop claim-to-evidence tests: if an agent claims "B+ DKD progresses faster", the verifier should trace it to the small TRIDENT n = 17 and log-rank P = 0.02 evidence strength.

## Reusable assets
- **Code:** all analysis code.
<https://github.com/Woopsydaisy/Spatial-Human-Kidney-Map>
- **Data:** snRNA-seq reference (Zenodo 15007208), single-cell B cell atlas (Zenodo 11468564), bulk (GSE115098), full spatial data (Zenodo 18674907, released on publication), Susztak lab browser.
<https://zenodo.org/records/15007208> · <https://zenodo.org/records/11468564> · <https://doi.org/10.5281/zenodo.18674907> · <http://www.susztaklab.com>
- **Probe design:** the 50 CosMx and 100 Xenium kidney custom probes listed in Methods, a reference for designing a kidney Xenium panel.
- **Method baselines:** scVI/scANVI cross-platform integration, COVET, NicheCompass, Hotspot, CellPhoneDB v5.

## Follow-ups
- CellSpectra (Klötzer 2025, same lab) — patient-level pathway-coordination anomalies, complementary to niche analysis here.
- NicheCompass and COVET papers — can they directly yield niche-level anomaly scores?
- Xenium segmentation/probe-artifact work in this round (xenium-split, ovrlpy, resolVI) to explain "far-from-reference" cells.

## Cite
```bibtex
@article{Dumoulin_2026, title={Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup}, volume={653}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10363-4}, DOI={10.1038/s41586-026-10363-4}, number={8116}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Dumoulin, Bernhard and Levinsohn, Jonathan and Klötzer, Konstantin A. and Li, Chenyu and Mao, Liran and Ha, Eunji and Mohandes, Samer and Nguyen, Thao and Paruzzo, Luca and Hirohama, Daigoro and Fang, Victoria and Bhoj, Vijay G. and Parhiz, Hamideh and Andrade-Silva, Magaiver and Abedini, Amin and Bergeson, Andi and Traum, Daniel and May, Michael J. and Kaestner, Klaus H. and Ruella, Marco and McAllister, Fiona Elizabeth and Hakimi, A. Ari and Li, Mingyao and Palmer, Matthew and Wherry, E. John and Hunter, Christopher A. and Cancro, Michael Paul and Townsend, Raymond and Coppock, Gaia and Singh, Manisha and Ross, Michael and Tumlin, James and Campbell, Kirk and Mottl, Amy and Argyropoulos, Christos and Isakova, Tamara and Almaani, Salem and Avasare, Rupali and Lafayette, Richard and Scialla, Julia and Luciano, Randy and Bansal, Shweta and Brosius, Frank and Mehta, Ankit and Lenz, Oliver and Kopyt, Nelson and Canetta, Piettro and Kretzler, Matthias and Schelling, Jeffrey and Hofherr, Alexis and Pullen, Steven S. and Thorley, Andrew and Shang, Ching and Hu, Erding and Karihaloo, Anil and Devalaraja-Narashimha, Kishor and Susztak, Katalin}, year={2026}, month=Apr, pages={1158–1169} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
