<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Robust annotation and discovery of novel cell types in single-cell ATAC-seq data through cross-modal reference alignment

- **Authors:** Cao, Lan; Zhang, Wenhao; Zhou, Feng; He, Yushuang; Long, Yongyu; Chen, Shengquan; Wang, Ying
- **Venue / Year:** Genome Research · 2026
- **DOI:** 10.1101/gr.281981.126
- **URL:** https://doi.org/10.1101/gr.281981.126
- **Bibkey:** Cao_2026
- **Status:** abstract-only (Genome Research paywall; no open preprint found; abstract from PubMed 42665446)

## Abstract
Accurate cell-type annotation is essential for revealing the dynamic, cell-type-specific accessibility of regulatory elements from single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq) data. However, unlike the more mature single-cell RNA-sequencing (scRNA-seq) cell-type annotation workflows, scATAC-seq cell-type annotation remains challenging owing to extreme sparsity, high dimensionality, the scarcity of labeled scATAC references, and pronounced batch effects across data sets. To enable annotation without relying on extensive scATAC labels, we introduce CARA, a cross-modal Bayesian framework that transfers cell-type knowledge from scRNA-seq to scATAC-seq. CARA simultaneously enables cell-type annotation, batch correction, and detection of cell types absent from the reference by combining pretraining on scRNA-seq data and semisupervised learning on target scATAC-seq data, along with distribution alignment, dynamic class weighting, and novel cell-type detection. Across diverse benchmark data sets, CARA consistently outperforms baseline methods, remaining robust to batch effects. CARA's cross-modal alignment and robust annotation strategy preserve fine-grained lineage structure, enabling reconstruction of the hematopoietic differentiation trajectory. Through multidimensional uncertainty and latent-space clustering, CARA identifies novel, rare, or aberrant populations outside the reference cell-type space, providing candidates for further biological validation and perturbation. Using an omic-specific generative framework and distribution alignment, CARA delivers accurate knowledge transfer and detects novel cell types in single-cell DNA methylation data, demonstrating generalization capability to gene-centric modalities. Ultimately, CARA offers a powerful and flexible solution for cross-modal cell-type annotation in complex single-cell settings, facilitating the discovery of novel cell types and mechanistic insight into cell-type-specific regulation across diverse analyses.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — full text behind the Genome Research paywall (vol. 36, no. 10, pp. 2037–2052). No methods, datasets or numbers beyond the abstract are available here. Drop `source.pdf` into this folder and re-run extraction to enrich.
