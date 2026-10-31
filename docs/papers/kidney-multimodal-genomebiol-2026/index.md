# Systematic evaluation of single-cell multimodal data integration enhances cell type resolution and discovery of clinically relevant states in complex tissues

> **Bibkey** `Acera_Mateos_2026` · **Venue** Genome Biology (2026) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1186/s13059-026-04002-4> · `status: complete`

---

## One-liner
On renal cortex from 19 healthy donors the authors run 3' scRNA-seq, 5' scRNA-seq and 10x multiome (snRNA + snATAC) side by side, yielding the 119,744-cell/nucleus benchmark mBDRC, and build scOMM, an interpretable supervised classifier, to systematically compare "horizontal" (sc↔sn RNA), "vertical" (RNA↔ATAC in the same nuclei) and "global" (mosaic/diagonal) integration for resolving kidney cell types and states. Global integration recovers a WFDC2⁺ adaptive-TAL subpopulation and EPO-producing Norn cells that single modalities miss.

## Problem
Large organ atlases (HCA, KPMP, etc.) increasingly mix protocols and modalities — scRNA, snRNA, snATAC — yet there is no systematic assessment of what each modality uniquely contributes to identifying cell types/states, or how much integration actually helps. Previous benchmarks compared experimental methods within one assay class or batch-correction algorithms alone; for a complex tissue like the kidney — fragile cells, gradient-like epithelial continua (DCT/CNT/PC), adaptive/injury states — a real, donor-matched, multi-protocol benchmark was missing.

## Method
**Design**: multicentre; 33 renal-cortex samples (25 from donors with multiple samples = paired, 8 unpaired) from normal tissue at nephrectomy, aliquoted and frozen for 3'/5' scRNA-seq and multiome. A few Smart-seq2 and scNMT-seq runs are reported separately (too little data); MERFISH never produced usable data despite optimisation. **Annotation**: anchored on existing human kidney references (HCA kidney etc.), two levels — L1 (12–14 broad types) and L2 (39 types/states). **scOMM**: a feedforward-network reference-mapping classifier (R package) trained directly on expression values (or peaks / gene activity); feature importance (FI) = relative accuracy drop ≥10 points when a gene is zeroed, giving an interpretable per-modality marker comparison. Benchmarked against Seurat, CHETAH and scmap on kidney, PBMC and heart multiome; closely matches Seurat label transfer. **Integration strategies**: horizontal with scVI (top benchmark score); ATAC harmonisation comparing SnapATAC2 Spectral-MNN, Signac LSI-Harmony, PeakVI and PoissonVI (Spectral-MNN best); vertical comparing SnapATAC2 multi-spectral vs optimised Seurat WNN; global comparing MultiVI (mosaic, uses paired cells) vs GLUE (diagonal, unpaired). **Metrics**: AUC (unsupervised clusters vs scOMM labels at specificity > 0.9), Mahalanobis distance / overlap ratio, binary cLISI (b-cLISI), average silhouette width (AWS), marker detection rate against HCA reference markers. Plus an empirical power analysis (variance decomposition, per-donor mean/variance/detection, purity, silhouette) and LDSC heritability enrichment for hypertension and eGFR in cell-type-specific CREs.

## Data
mBDRC: 119,744 high-quality cells/nuclei from 19 healthy donors (diverse sex, age, BMI) across 33 samples; 97,125 cells/nuclei in the horizontal integration; 11 multiome samples with 37,717 paired nuclei. External validation: an independent public kidney multiome + CosMx spatial dataset (ref. [23] in the paper) and a human heart atlas (3′ sc/snRNA + multiome). Raw data on dbGaP phs004459; integrated data to be released via CELLxGENE.

## Key results
- **sn vs sc power analysis**: assay explains a median 24% of expression variance, cell type 13%, assay×cell-type interaction 6%, donor only 3% — protocol differences dwarf donor differences. snRNA-seq measures more genes (lower dropout), detects more cells and gives purer clusters, so for most cell types in fragile kidney tissue it carries more information; the interaction term shows the two are complementary.
- **Horizontal integration**: PT subtypes (PT-S1, aPT, PT-S3) are best captured by snRNA; TAL (C-TAL, aTAL) by 3' scRNA; continuous/low-abundance MD, DCT1, CNT by 5' scRNA. Integration raises Mahalanobis separation for most populations and b-cLISI for CNT/DCT/PC (>0.8 after integration for snRNA and 5' scRNA). snRNA has the highest marker detection rate (~0.5 for POD, PC, DCT); the integrated model balances protocols and finds unique markers (e.g. PTP4A1 for CNT-PC).
- **Vertical integration**: WNN weights RNA in almost every cell type, diluting ATAC; multi-spectral gives higher silhouettes with a near-additive complementary effect (notably POD, PEC, C-TAL, IC-B) and higher b-cLISI in aPT, CNT-PC, DCT1. Among scOMM variants, the peaks-based Bridge model has the highest AUC; gene-activity Cross-Modality is worst; genes+peaks Integrated does not beat Bridge.
- **Global integration**: MultiVI (mosaic) and GLUE (diagonal) do not differ significantly and overall do not beat simpler combinations, but help adaptive states — aTAL1 b-cLISI rises from 0.45 (vertical) to 0.61 (mosaic). Reclustering reveals a 3'-scRNA-dominated WFDC2⁺ aTAL1_0 (WFDC2/HE4 is a proposed lupus-nephritis/CKD serum biomarker) and very rare EPO-producing Norn cells within aFIB (DCN, TIMP1, CFD), both nearly invisible in snRNA.
- **External replication**: in an independent dataset, Norn and WFDC2⁺ aTAL1_0 signatures are significantly up in disease samples (p < 0.01 / p < 0.001), localise in CosMx to fibroblasts and the Loop of Henle respectively, and are enriched in fibrotic/injured epithelial niches; scOMM projection recovers both. In the external kidney data ATAC embeddings separate adaptive populations better (aTAL1 b-LISI 0.69 vs RNA 0.55; aPT 0.81 vs 0.66), while RNA better separates distal tubule (CNT, DCT1).
- **Heritability**: MD cells are strongly enriched for both hypertension and eGFR; endothelium and VSMC/pericytes only for hypertension; adding transcription signal to CRE selection (Sets 2/3) gives significantly higher enrichment.

## Contributions
- The first donor-matched, four-protocol (3'/5' scRNA, snRNA, snATAC) renal-cortex multimodal benchmark, mBDRC.
- scOMM: an interpretable reference-mapping tool for per-modality marker contribution.
- Practical, cell-type-aware guidelines on which protocol/integration resolves which populations.
- Recovers two disease-associated rare states (WFDC2⁺ aTAL, Norn) and validates them externally and spatially.

## Limitations
- Limited matched samples across protocols; donor heterogeneity confounds analyses such as GRN/TF inference.
- No true ground truth for cell identity; relies on expert annotation and simulated scenarios.
- Healthy tissue only; Smart-seq2/scNMT-seq not optimised for frozen kidney, MERFISH failed; generalisation to other tissues is limited (despite a heart check).
- Some protocol-specific detection of aTAL/Norn could partly reflect sensitivity; the authors argue biology, but technical bias is not fully excluded.

## Relation to our direction
This is the artifact-injection topic's most direct "data-layer" reference: for a multi-modal design of this kind (snRNA + snATAC, plus Xenium + H&E), this paper quantifies, on healthy donors, which kidney cell states are visible only in some modalities. For the **detect** stage of detect → model → revert it gives two hard constraints: **(1) protocol effects (median 24%) dwarf donor effects (3%)**, so any anomaly score must be aligned along the assay axis first or the model will flag protocol differences as anomalies; **(2) cross-modal disagreement is not always artefact** — adaptive/rare states like aTAL and Norn are seen only in some modalities, and they rise in disease. That is exactly where the artifact-injection topic's "cross-modal agreement separates artefacts from disease" needs refinement: disagreement should not be read as artefact by default but weighed against cell-type-specific modality sensitivity priors (the paper gives an empirical table: PT→snRNA, TAL→3', MD/DCT/CNT→5', adaptive→ATAC). mBDRC as a **healthy reference** can serve the normal-distribution modelling for KidneyAnomalyBench; WFDC2⁺ aTAL1_0 and Norn are candidate expert-verifiable "known-positive anomalous states". For the agent-trustworthiness topic, scOMM's feature importance and the finding that integration does not always help supply ready counter-examples to typical agent over-claims (e.g. "multimodal integration is always better") for an omics-specific failure taxonomy and claim-to-evidence test cases.

## Reusable assets
- **Analysis code** (MIT):
<https://github.com/mereulab/sc-multimodal-integration-benchmark> · Zenodo 10.5281/zenodo.17475964
- **scOMM** (R package):
<https://github.com/mereulab/scOMM> · Zenodo 10.5281/zenodo.18061150
- **Data**: raw data on dbGaP phs004459 (controlled access); integrated object slated for CELLxGENE.
- **Metric suite**: AUC@specificity>0.9, Mahalanobis overlap ratio, b-cLISI, AWS, FI threshold 10 — reusable for evaluating our own cross-modal integration.

## Follow-ups
- The independent kidney multiome + CosMx dataset (ref. [23]) — check whether it can serve as an external test set for the artifact-injection topic (possibly related to KPMP / the Lake atlas).
- Lake et al. 2023 kidney atlas (`lake-kidney-atlas-nature-2023`), to which the L1/L2 annotation is anchored.
- MultiVI, GLUE, SnapATAC2, and Lee et al.'s paired/unpaired RNA+ATAC integration benchmark.

## Cite
```bibtex
@article{Acera_Mateos_2026, title={Systematic evaluation of single-cell multimodal data integration enhances cell type resolution and discovery of clinically relevant states in complex tissues}, volume={27}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-026-04002-4}, DOI={10.1186/s13059-026-04002-4}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Acera-Mateos, Mario and Adiconis, Xian and Li, Jessica-Kanglin and Marchese, Domenica and Caratù, Ginevra and Hon, Chung-Chau and Tiwari, Prabha and Kojima, Miki and Vieth, Beate and Murphy, Michael A. and Simmons, Sean K. and Lefevre, Thomas and Claes, Irene and O’Connor, Christopher L. and Menon, Rajasree and Otto, Edgar A. and Ando, Yoshinari and Vandereyken, Katy and Kretzler, Matthias and Bitzer, Markus and Fraenkel, Ernest and Voet, Thierry and Enard, Wolfgang and Carninci, Piero and Heyn, Holger and Levin, Joshua Z. and Mereu, Elisabetta}, year={2026}, month=Mar }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
