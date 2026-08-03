<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Detecting anomalous anatomic regions in spatial transcriptomics with STANDS

- **Authors:** Xu, Kaichen; Lu, Yan; Hou, Suyang; Liu, Kainan; Du, Yihang; Huang, Mengqian; Feng, Hao; Wu, Hao; Sun, Xiaobo
- **Venue / Year:** Nature Communications · 2024
- **DOI:** 10.1038/s41467-024-52445-9
- **URL:** https://doi.org/10.1038/s41467-024-52445-9
- **Bibkey:** Xu_2024
- **Status:** complete

## Abstract
Detection and Dissection of Anomalous Tissue Domains (DDATD) from multi-sample spatial transcriptomics (ST) data provides unprecedented opportunities to characterize anomalous tissue domains (ATDs), revealing both population-level and individual-specific pathogenic factors for understanding pathogenic heterogeneities behind diseases. However, no current methods can perform de novo DDATD from ST data, especially in the multi-sample context. Here, we introduce STANDS, an innovative framework based on Generative Adversarial Networks which integrates three core tasks in multi-sample DDATD: detecting, aligning, and subtyping ATDs. STANDS incorporates multimodal-learning, transfer-learning, and style-transfer techniques to effectively address major challenges in multi-sample DDATD, including complications caused by unalignable ATDs, under-utilization of multimodal information, and scarcity of normal ST datasets necessary for comparative analysis. Extensive benchmarks from diverse datasets demonstrate STAND’s superiority in identifying both common and individual-specific ATDs and further dissecting them into biologically distinct subdomains. STANDS also provides clues to developing ATDs visually indistinguishable from surrounding normal tissues. The authors introduce STANDS, a GAN-based framework that integrates three core tasks for the multi-sample detection and dissection of anomalous tissue domains from spatial transcriptomics data, revealing pathogenic heterogeneity behind diseases.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->

_Source: Nature Communications 15:8223 (2024), open access, extracted via Europe PMC full-text (PMCID PMC11413068). Some article-specific dataset accession numbers and per-figure numbers live in the paper's Data availability / Supplementary; the cleaned narrative below faithfully captures the abstract, framework, datasets, results, and availability._

### Introduction
STANDS addresses Detection and Dissection of Anomalous Tissue Domains (DDATD) from multi-sample spatial transcriptomics (ST) data — characterizing biologically heterogeneous anomalous tissue domains (ATDs) across multiple tissue samples, revealing population-level and individual-specific pathogenic factors. Key limitations of prior approaches:
- Reliance on expert visual inspection or computer-vision algorithms.
- Dependence on "expert-defined" anomaly markers, unavailable for novel domain types.
- Lack of a marker-free, multi-sample ST alignment mechanism.
- Scarcity of normal reference ST datasets for comparison.

No prior method could perform de novo DDATD from ST data, especially in the multi-sample context (jointly detecting shared vs. sample-specific anomalies and subtyping them).

### STANDS Framework Architecture
STANDS (Spatial Transcriptomics Anomaly Detection and Subtyping) is a GAN-based framework integrating three core tasks: detecting, aligning, and subtyping ATDs. It combines multimodal learning, transfer learning, and style-transfer techniques.

**Component I — Anomaly Detection.**
- Trains a GAN module on reference (normal) datasets to reconstruct normal spots.
- Uses multimodal embeddings combining gene expression and histology images.
- Gene-expression embeddings via a Graph Attention Network (GAT).
- Histology-image embeddings via a GAT-ResNet hybrid network.
- A Transformer Fusion (TF) block integrates the multimodal representations.
- Anomalies are spots with elevated reconstruction errors (anomaly scores).
- Can use scRNA-seq as a surrogate reference when normal ST data are unavailable (cross-modality).
- A memory bank reduces mode-collapse tendency.

**Component II — Multi-Sample Alignment.**
- Module II creates "kin" pairs between reference and target spots via a non-negative mapping matrix M.
- Module III learns a "style"-divergence matrix S for batch-effect correction.
- Style-transfer aligns target datasets into the reference data space, preserving original scale and semantic integrity.
- Detected anomalies are excluded during training and realigned during testing.

**Component III — Anomaly Subtyping.**
- Fuses Component-I embeddings with reconstruction residuals.
- Applies Discriminatively Enhanced Clustering (DEC), iteratively refining cluster assignments and centroids.
- Groups anomalies into biologically distinct subdomains (shared across samples or sample-specific).

### Datasets Used
- **Human breast (10x Visium):** 10x-hNB-v05 = healthy breast reference (4 normal domain types); 10x-hBC-G2 = breast cancer (cancer in situ, invasive cancer); 10x-hBC-H1 = breast cancer (invasive cancer, adipose tissue); 10x-hBC-A1..A6 = vertical breast-cancer slices.
- **Human pancreas:** sc-hPD = scRNA-seq from healthy pancreatic ducts (reference); 10x-hPDAC = pancreatic ductal adenocarcinoma (target) — cross-modality.
- **Mouse embryo:** ssq-mEmb-32/33/34 (Slide-seqV2); Stereo-mEmb-S1/S2/S3 (Stereo-seq).
- **Human liver/pancreas:** 10x-hLCL-C73-C1 = healthy liver reference; 10x-hPSC-A1/C1/D1 = primary sclerosing cholangitis (vertical slices).
- **Human kidney:** 10x-hRCC-C2/C3/C4 = renal cell carcinoma.

Modalities: spatial gene expression plus paired histology images; scRNA-seq supported as a reference.

### Key Metrics and Results
**Single-dataset anomaly detection.** STANDS outperforms Spatial-ID, CAMLU, scPred, CHETAH, and scmap on accuracy and F1-scores. A novel Spatial Grouping Discrepancy (SGD) metric incorporates spatial relationships.

**Multi-dataset detection.** Identifies both shared ATDs (invasive cancer across datasets) and unique ATDs (cancer in situ in one dataset, adipose tissue in another) while maintaining superior accuracy.

**Cross-modality detection.** Using a scRNA-seq reference for 10x Visium ST targets achieves competitive/best performance; identifies pancreatic cancerous domains with the highest accuracy and F1.

**Alignment.** Batch-mixing metrics: integration LISI (iLISI, higher better), batch-corrected KL divergence (BatchKL, lower better), adjusted silhouette width (ASW_batch). Domain-type separation: ASW_type (higher better). STANDS achieves the highest scores vs. Harmony, ComBat, GraphST, STAligner. Post-alignment GraphST clustering ARI typically ~0.23–0.52 for STANDS, above benchmarks.

**Subtyping.** Highest Macro-F1 and Normalized Mutual Information (NMI); most accurate spatial arrangement by Multi-SGD.

**Reference-data sensitivity.** Removing 1/3 of reference spots decreases AUC by ~0.05–0.10; removing 2/3 increases false positives 2–3×; removing a diverse domain type (e.g., breast glands) causes ~3.3× more false positives for that domain type.

**Ablations.** Removing the memory bank reduces accuracy and increases mode-collapse tendency; removing histology decreases F1 by ~0.05–0.15 and raises false positives in sparse normal domains; removing the TF block reduces detection accuracy and subtyping quality; non-negative mapping beats MNN for batch correction (ASW_batch differences ~0.10).

**New evaluation metrics.** Spatial Grouping Discrepancy (SGD) — degree (SGD_degree) and clustering coefficient (SGD_cc) — treats spatial organization as a critical evaluation component beyond conventional clustering metrics. Multi-SGD extends this to multi-dataset scenarios with heatmap visualization of label-correspondence quality.

### Code and Data Availability
- **Code:** https://github.com/Catchxu/STANDS (GPL-3.0; Python 3.9+; `git clone … && cd STANDS/ && python3 setup.py install`).
- **Documentation & tutorials:** https://catchxu.github.io/STANDS/ (six use-case tutorials: single/multi-dataset detection, alignment, subtyping).
- **Pretrained models:** documentation recommends pretraining on large-scale public ST datasets; no ready-made checkpoints released.
- **Contact:** kaichenxu358@gmail.com or GitHub issues.
- **Data:** dataset accession numbers listed in the paper's Data availability section.

### Publication Details
Nature Communications, vol. 15, article 8223; published 19 Sept 2024; DOI 10.1038/s41467-024-52445-9; PMID 39300113; PMCID PMC11413068. Article license: CC BY-NC-ND 4.0.
