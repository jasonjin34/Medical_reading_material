# Benchmarking single-cell multi-modal data integrations

> **Bibkey** `Fu_2025_MultimodalBench` · **Venue** Nature Methods (2025) · **Category** single-cell · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s41592-025-02737-9> · `status: complete`

---

## One-liner
SCMMIB: a Registered Report benchmarking 40 single-cell multimodal integration algorithms (65 method×task combinations) on six tasks — paired RNA+ATAC, paired RNA+ADT, spatial multi-omics, unpaired RNA+ATAC diagonal, RNA+ATAC mosaic and RNA+ADT mosaic — over 101 benchmark datasets derived from 14 public datasets, scoring usability, accuracy and robustness. Seurat v4 WNN (paired RNA+ATAC) and GLUE (unpaired diagonal) are SOTA for their tasks; MIDAS is SOTA for mosaic cross-modality imputation.

## Problem
There are 40+ multimodal integration tools, but modalities differ enormously in dimension (tens of ADTs to hundreds of thousands of ATAC peaks) and sparsity, and paired/unpaired/mosaic settings differ; prior benchmarks covered few tools (e.g. 5 RNA+ATAC tools and 4 Multiome-guided mosaic tools). Users lack systematic guidance by data type, modality, size and quality.

## Method
**Methods**: 40 including bindSC, GLUE, MultiVI, Multigrate, MOFA+, MIDAS, Seurat v3 CCA / v4 RPCA / v4 WNN / v5 bridge, totalVI, StabMap, SpatialGlue, scMVP, scMDC, uniPort, MaxFuse, SIMBA, cobolt, scMoMaT, scVAEIT. **Three axes**: (1) usability — paper/code/documentation quality and whether a method runs within preset hardware limits (scalability up to 500,000 cells; 500 GB memory cap); (2) accuracy — for paired tasks, biological conservation and batch removal of the joint embedding (scib-style metrics; **no method receives batch labels**, for fairness, with a separate test of the batch parameter); for unpaired/mosaic tasks, paired data are split into "pseudo-unpaired" data with known cell matches as gold standard, scoring FOSCTTM, cell match and cell-type match; imputation-capable methods are scored on imputation (scATAC: AUPR at cell level, AUROC at cell-type level); (3) robustness — downsampling to simulate sparsity (multi-gradient downsample AUC, accuracy at 10% depth), paired-set size in mosaic tasks (3,000–20,000 cells), and SD/CV over five repeated runs.

## Data
14 public datasets → 101 benchmark datasets spanning immune, kidney, skin and brain, 1,000–700,000 cells, 2–143 batches: NeurIPS 2021 BMMC Multiome and CITE-seq (GSE194122), HSPC Multiome/CITE-seq (Kaggle Open Problems), SHARE-seq skin, COVID-19 CITE-seq, human WBC CITE-seq, 10x NSCLC CITE-seq, **10x kidney-cancer CITE-seq**, 10x mouse brain and PBMC Multiome; spatial multi-omics: SPOTS mouse spleen, mouse thymus, human lymph node. Processed inputs are on Figshare.

## Key results
- **Paired RNA+ATAC**: top biological conservation Seurat v4 WNN, scMDC, scMVP; top batch removal Seurat v4, scDEC, scMVP, though rankings vary by dataset; only MultiVI, uniPort and scMVP ran at 500k cells. Supplying batch labels improves 4 of 5 batch metrics for MultiVI. Sparsity robustness: Seurat v4 WNN, Multigrate, scMVAE, scMVP best; scDEC has the largest run-to-run variation. Imputation: scMVP (RNA) and DCCA (ATAC) best.
- **Paired RNA+ADT**: totalVI, Seurat v4 WNN and bindSC best on biological conservation; but totalVI drops to 8th of 10 on mixed-batch data without batch labels; with batch labels totalVI graph iLISI goes 0.1→0.4 and ARI 0.37→0.62, Multigrate iLISI 0.22→0.43 and ARI 0.32→0.50. In spatial multi-omics SpatialGlue is best, but trails Harmony and STAligner on batch removal.
- **Unpaired RNA+ATAC diagonal**: 9 of 14 methods need an ATAC-derived gene activity matrix (GAM), and neither Signac's nor Seurat's GAM function handles 500k cells, so only GLUE runs; GLUE is best on alignment accuracy across all datasets and first overall on usability, accuracy and low-depth robustness.
- **RNA+ATAC mosaic**: MultiVI, MIDAS and cobolt best on embedding accuracy; leveraging paired cells, Seurat v5 Bridge and MultiVI beat GLUE on BMMC FOSCTTM (median 3.7% / 3.8% vs 3.9%) and cell-type matching (L1 89.2% / 89.4% vs 86.3%; L2 84.2% / 82.9% vs 74.5%). MIDAS cross-modality imputation is clearly best, approaching paired imputation methods given 10% of the target modality.
- **RNA+ADT mosaic**: MIDAS and StabMap best on embedding accuracy; MIDAS leads imputation (including over totalVI); but MIDAS is costly (>10 h and 80 GB on the largest set) vs StabMap (~2 min, 5 GB).
- **Reproducibility**: non-deep methods are fully deterministic; deep methods are stable only when the source code fixes a random seed (uniPort, MultiVI, Multigrate, SCALEX); others show SD > 0.05 on some metrics.

## Contributions
- The broadest multimodal integration benchmark to date (40 algorithms, six tasks, 101 datasets), pre-registered as a Registered Report.
- The "pseudo-unpaired" design: paired data's true correspondences serve as gold standard for unpaired/mosaic tasks.
- Includes scalability, batch-parameter effects and run-to-run stability, with an evaluation Python package, reproducible pipeline and interactive website.

## Limitations
- Spatial multi-omics covers only 3 methods with scarce data; other epigenetic modalities (e.g. methylation) not covered.
- Effect of input dimensionality not fully assessed; hardware limits may differ from users' setups.
- Pseudo-unpaired data come from the same cells, so the difficulty of truly unpaired data (different samples/donors) may be underestimated.
- Data are immune/blood-heavy, with kidney represented only by one 10x kidney-cancer CITE-seq set; this read is based on the preprint.

## Relation to our direction
For Plan A this is the "method map" for choosing an integration backbone. Our 95 biopsies are snRNA + snATAC (multiome, paired) + Xenium (spatial) + H&E, to be merged with external unpaired data such as KPMP/Lake — mapping exactly onto the paper's paired RNA+ATAC (recommends Seurat v4 WNN, MultiVI), unpaired diagonal (GLUE) and mosaic (MultiVI, Seurat v5 Bridge, MIDAS) tasks. The contrast with `kidney-multimodal-genomebiol-2026` is instructive: on kidney, WNN over-weights RNA and multi-spectral is better — SOTA from blood data does not necessarily transfer to kidney, so KidneyAnomalyBench needs its own kidney-specific integration choice. For "cross-modal agreement separates artefacts from disease", the "pseudo-unpaired + known correspondence" design is directly borrowable: use multiome's true pairing as gold standard to quantify the mismatch rate (FOSCTTM) introduced by integration itself — the **noise floor** for cross-modal disagreement scores; disagreement below that floor should not be called anomalous. Another key fact is that methods like totalVI degrade sharply without batch labels, so batch must be modelled explicitly before anomaly scoring. For Plan B, "deep methods without fixed seeds show SD > 0.05" maps directly to rerun stability: conclusions agents reach with these tools need repeated runs, and "unfixed random seed → unstable conclusion" belongs in the omics-specific failure taxonomy.

## Reusable assets
- **Evaluation-metric Python package and figure scripts:**
<https://github.com/bm2-lab/SCMMI_Benchmark>
- **Pipeline for running all methods:**
<https://github.com/bm2-lab/SCMMIB_pipeline>
- **Interactive results website:**
<https://bm2-lab.github.io/SCMMIB-reproducibility/>
- **Processed inputs** (Figshare) and the pre-registered protocol (Springer Nature Figshare 26789572).
- **Preprint full text:**
<https://doi.org/10.1101/2025.04.01.646578>

## Follow-ups
- The MIDAS, GLUE, MultiVI and Seurat v5 bridge papers.
- The cited 14-method cross-modality prediction benchmark (which omitted MIDAS).
- Novel cell-type discovery in scATAC via cross-modal references (`scatac-novel-genomeres-2026`).

## Cite
```bibtex
@article{Fu_2025_MultimodalBench, title={Benchmarking single-cell multi-modal data integrations}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02737-9}, DOI={10.1038/s41592-025-02737-9}, number={11}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Fu, Shaliu and Wang, Shuguang and Si, Duanmiao and Li, Gaoyang and Gao, Yawei and Liu, Qi}, year={2025}, month=July, pages={2437–2448} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
