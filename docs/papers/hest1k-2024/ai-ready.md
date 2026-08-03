<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# HEST-1k: A Dataset for Spatial Transcriptomics and Histology Image Analysis

- **Authors:** Guillaume Jaume; Paul Doucet; Andrew H. Song; Ming Y. Lu; Cristina Almagro-Pérez; Sophia J. Wagner; Anurag J. Vaidya; Richard J. Chen; Drew F. K. Williamson; Ahrong Kim; Faisal Mahmood
- **Venue / Year:** arXiv preprint · 2024
- **DOI:** 
- **URL:** https://arxiv.org/abs/2406.16192
- **Bibkey:** Jaume2024_240616192
- **Status:** complete

## Abstract
Spatial transcriptomics enables interrogating the molecular composition of tissue with ever-increasing resolution and sensitivity. However, costs, rapidly evolving technology, and lack of standards have constrained computational methods in ST to narrow tasks and small cohorts. In addition, the underlying tissue morphology, as reflected by H&amp;E-stained whole slide images (WSIs), encodes rich information often overlooked in ST studies. Here, we introduce HEST-1k, a collection of 1,229 spatial transcriptomic profiles, each linked to a WSI and extensive metadata. HEST-1k was assembled from 153 public and internal cohorts encompassing 26 organs, two species (Homo Sapiens and Mus Musculus), and 367 cancer samples from 25 cancer types. HEST-1k processing enabled the identification of 2.1 million expression--morphology pairs and over 76 million nuclei. To support its development, we additionally introduce the HEST-Library, a Python package designed to perform a range of actions with HEST samples. We test HEST-1k and Library on three use cases: (1) benchmarking foundation models for pathology (HEST-Benchmark), (2) biomarker exploration, and (3) multimodal representation learning. HEST-1k, HEST-Library, and HEST-Benchmark can be freely accessed at https://github.com/mahmoodlab/hest.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->

> Source: arXiv HTML v1 (https://arxiv.org/html/2406.16192v1). Note: the Abstract above is from a newer version and reports larger headline figures (1,229 profiles / 153 cohorts / 26 organs / 367 cancer samples / ~2.1M pairs / >76M nuclei). The v1 body text below reports earlier figures (1,108 samples / 131 cohorts / 25 organs / 320 cancer samples / 1.5M pairs / ~60M nuclei). Both are preserved faithfully.

### Problem & Motivation
Spatial transcriptomics (ST) has been constrained by high costs and rapidly evolving technology, limiting computational development to narrow tasks and cohorts of only a few patients. The paper identifies three gaps: (1) lack of standardized resources, (2) overlooked tissue morphology in H&E whole-slide images (WSIs), and (3) absence of diverse benchmarks for foundation models beyond diagnostic tasks. The morphology in H&E WSIs is strongly linked to gene expression yet routinely ignored in ST studies.

### Dataset Construction (v1 figures)
Scale & composition:
- 1,108 samples from 131 public and internal cohorts.
- 1.5 million expression–morphology pairs.
- ~60 million detected nuclei (59.6M total; 17.6M neoplastic, 21.5M stromal, 4.9M epithelial, 15.4M inflammatory, 76K necrotic).
- 25 organs across two species: Homo sapiens and Mus musculus.
- 320 cancer samples from 25 cancer types.
- Total size: 825 GB raw data.

Data sources: 10x Genomics (97 samples), NCBI (677), Mendeley (118), Spatial-Research (139), Zenodo (17), internal cohorts (28), miscellaneous (32).

ST technologies used:
- Visium / Visium HD (sequencing-based).
- Xenium (imaging-based, sub-cellular resolution).
- Original Spatial Transcriptomics.

Tissue preparation: both frozen and formalin-fixed paraffin-embedded (FFPE) sections; image magnification standardized at 10×, 20×, and 40× with resolution ≥1.15 μm/pixel.

### HEST-Library (Python package)
Built on Scanpy and AnnData, enabling:
- Format conversion: unifies diverse image formats (JPG, TIFF, OME.TIF, BigTIFF) into pyramidal TIFF compatible with OpenSlide.
- Automatic alignment: YOLOv8-based fiducial detection for Visium samples (119 manually annotated regions); repositioning for non-fiducial samples.
- Resolution detection: infers pixel resolution from inter-spot distances and known spacing.
- Data unification: converts multiple expression formats (CSV, MEX, TXT, h5) to AnnData objects.
- Tissue segmentation: fine-tuned DeepLabV3 with ResNet50 backbone for robust tissue detection.
- Patching: extracts 224×224-pixel patches at 20× magnification around each spot.
- Batch download: query and download subsets via metadata filters.

### Use Case 1: HEST-Benchmark
Task definition — ten gene expression prediction tasks across nine human cancer types and ten organs:
1. IDC (breast, Xenium, 4 patients)
2. PRAD (prostate, Visium, 2 patients, 23 samples)
3. PAAD (pancreas, Xenium, 3 patients)
4. SKCM (skin, Xenium, 2 patients)
5. COAD (colon, Visium, 3 patients, 6 samples)
6. READ (rectum, Visium, 2 patients, 4 samples)
7. ccRCC (kidney, Visium, 24 patients)
8. HCC (liver, Visium, 2 patients)
9. LUAD (lung, Xenium, 2 patients)
10. Lymph node metastasis in IDC (Visium, 4 patients)

Prediction setup: models predict expression of the top 50 most variable genes from 112×112 μm H&E patches; patient-stratified k-fold cross-validation prevents data leakage. Readout: Random Forest regression (70 trees); Ridge regression also evaluated.

Foundation models evaluated (10 total): ResNet50-IN (ConvNet, ImageNet supervised); KimiaNet (ConvNet, supervised classification); Ciga (ConvNet, SimCLR); CTransPath (ViT, MoCov3); Remedis (ViT-Base, iBOT); Phikon (ViT-Base, iBOT); PLIP (ViT-Base, CLIP vision-language); UNI (ViT-Large, 307M, DINOv2); CONCH (ViT-Base, 86M, visual-language fine-tuning); GigaPath (ViT-Giant, 1.13B, DINOv2).

Benchmark results — average Pearson correlation across all tasks: UNI 0.319 (best), GigaPath 0.316, CONCH 0.315, Remedis 0.315, CTransPath 0.295. Task-specific performance ranged from 0.034 (HCC) to 0.613 (SKCM with UNI).

Key findings:
- Vision-language model CONCH showed superior performance with Ridge regression (~+5% absolute over second-best).
- Student-teacher pretraining outperformed supervised approaches.
- ViT-Base (CONCH) matched ViT-Giant (GigaPath) despite ~13× fewer parameters.
- Certain cancers showed low morphology–expression correlation (HCC 0.034–0.060; READ 0.051–0.162).

### Use Case 2: Biomarker Discovery
Analysis: invasive ductal carcinoma (IDC) Xenium samples with CellViT nuclear segmentation/classification.
Key findings:
- Significant correlation between neoplastic nuclear area and GATA3 expression (R=0.47).
- Highest associations for size-related nuclear features; topology/shape features weaker (R<0.2).
- Genes validated: FLNB (R=0.49), TPD52 (R=0.49), FOXA1 (R=0.47).
- Demonstrated morphological heterogeneity correlating with molecular expression patterns.

### Use Case 3: Multimodal Representation Learning
Setup: fine-tuned CONCH on 5 Xenium IDC cases (4 ductal, 1 lobular); 47,051 expression–morphology pairs; 238 common genes; contrastive alignment using InfoNCE loss.
Training recipe: freeze earlier layers, fine-tune last 3 ViT layers; layer-wise learning decay factor 0.7; patch-level augmentation.
Evaluation (BCNB dataset, n=1,058 WSIs for ER/PR/HER2 status prediction via logistic regression), CONCH → CONCH-FT:
- ER AUC 0.881 → 0.884; ER balanced accuracy 0.745 → 0.752.
- PR AUC 0.810 → 0.818; PR balanced accuracy 0.698 → 0.714.
- HER2 AUC 0.715 → 0.724; HER2 balanced accuracy 0.624 → 0.615.
- Embedding rank 144.66 → 146.47.
Disease-specific fine-tuning improved most metrics, demonstrating transfer-learning potential.

### Data Access & Licensing
- License: CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike).
- Repository: GitHub — https://github.com/mahmoodlab/hest
- Platform: HuggingFace Datasets (full dataset or queried subsets, e.g. cancer-type-specific).
- Restrictions: research-only; diagnostic use prohibited; reverse engineering to extract PHI forbidden.

### Limitations
- Inherent noise in ST data; staining and compression artifacts impact quality.
- Batch effects not quantified across samples, datasets, and technologies.
- HEST-Library cannot cover all legacy formats.
- Limited sample sizes for some tasks (HCC 2 patients; PAAD 3 patients).
