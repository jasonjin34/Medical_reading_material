<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# A Deep Learning-Based Pathomics Methodology for Quantifying and Characterizing Nucleated Cells in the Bone Marrow Microenvironment

- **Authors:** Spencer Krichevsky, Madhu M. Ouseph, Yuwei Zhang, Ghaith Abu-Zeinah, Joseph M. Scandura, Rajarsi Gupta
- **Venue / Year:** Blood, Vol. 142 (Supplement 1), 65th ASH Annual Meeting, Abstract 2294 · 2023
- **DOI:** 10.1182/blood-2023-191272
- **URL:** https://ashpublications.org/blood/article/142/Supplement%201/2294/499845
- **Bibkey:** pathomics-blood-2023
- **Status:** abstract-only (conference abstract)

## Abstract
> Verbatim abstract as deposited with Crossref (DOI 10.1182/blood-2023-191272); retrieved 2026-10-27. Figures 1–2 referenced in the abstract are not reproduced.

### Introduction

The overall cellularity of the bone marrow (BM) microenvironment is a WHO criterion for differentiating BCRABL- myeloproliferative neoplasms (MPNs) like polycythemia vera (PV) and myelofibrosis (MF) [1]. However, manual assessment by hematopathologists is subjective, not scalable, and only records a single global measure, disregarding BM regional differences. Leveraging pathology slide scanners and deep learning (DL) can address these limitations and reveal valuable insights into MPN subtypes and treatment effects. Despite its potential, computational pathology (Pathomics) in this area remains understudied [2-3].

### Methods

After institutional review from Stony Brook University and Weill Cornell Medicine (WCM), we identified 54 patients (pts) with a manually confirmed PV diagnosis (dx) at WCM (17% newly dx'ed, 61% treated, 17% disease progression). The dataset includes hematoxylin & eosin (H&E) stained whole slide images (WSIs), labs, molecular studies, and pathology report elements (reference standard for biopsy core size and cellularity).

Numeric cellularity measures the ratio of hematopoietic cells to fat cells and excludes inevaluable trabecular bone. Normal cellularity ranges from (100-pt age [y])±20% and PV is characterized by hypercellularity.

We evaluated three DL algorithms for nuclear segmentation: 1) Our U-Net model trained on 5B nuclei from 10 cancer types [4], 2) HistoCartography (HC): a graph neural network trained on 235K nuclei (PanNuke/MoNuSac datasets) [5], and 3) CellPose (CP): a gradient-driven U-Net model trained on 1K nuclei of varied modalities [6]. A color/morphology-based segmenter identified fat cells and evaluable BM regions, excluding vessels/tissue tears. Cellular characteristics (shape, texture, color) were computed and clustered by k-nearest neighbors (kNN) and k-means to explore differences between PV stages.

A tissue-based approach for cellularity estimation derived the proportion of non-fat tissue to evaluable regions. A cell-based approach derived the proportions of nucleated cell and fat cell areas. The study calculated mean differences between biopsy core size estimates, assessed correlation (r) and intra-class correlation (ICC) for numeric cellularity estimates, and Cohen's kappa (κ) for categorical cellularity estimates.

### Results

Measured and estimated biopsy core sizes differed by an acceptable margin (3±4 mm). Tissue-based cellularity estimator results: r=0.2, ICC=0.0, κ=0.2. Cell-based cellularity estimator result: our approach (r=0.7, ICC=0.6, κ=0.7), HC (r=0.7, ICC=0.5, κ=0.6), and CP (r=0.2, ICC=0.2, κ=0.7).

Cell size clusters aligned with known distributions in PV, with the prominent Int1 class (5.1-9μm) likely containing erythrocytes and myeloid progenitors. Overall and cell-sized cellularity heatmaps visualize regional differences (Figure 1). K-means clustering separated new and progressing PV (Figure 2).

### Discussion

DL and classical image analysis were employed to segment nucleated cells, fat cells, and other evaluable regions of hematopoietic tissue. Extracting shape, texture, and color features from segmented nuclei enhances BM microenvironment characterization. This pilot study resulted in a practical and interpretable Pathomics pipeline and downstream analytics as a proof of concept for hypothesis-driven research. Future directions involve applying these insights to a large cohort of diagnosis WSIs from other MPN subtypes and correlating findings with other tools, like immune cell detection models.

### References

[1] Arber DA. Blood. 2016;127(20):2391-405.

[2] Nielsen FS. Cytometry. 2019;95(10):1066-74.

[3] van Eekelen L. Pathology. 2022;54(3):318-27.

[4] Hou L. Sci Data. 2020;7(185)

[5] Jaume G. PMLR. 2021.

[6] Stringer C. Nat Methods. 2021;100-6.

[7] Abousamra S. Front Oncol. 2022.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — this is a conference abstract (ASH 2023 poster, Blood Supplement); no full paper exists. The text above is the complete public abstract content. Landing page (ashpublications.org / ScienceDirect S0006497123088961) returns HTTP 403 to automated fetch; the verbatim abstract above was retrieved from Crossref. If a full poster PDF becomes available, drop `source.pdf` into this folder and re-run extraction.
