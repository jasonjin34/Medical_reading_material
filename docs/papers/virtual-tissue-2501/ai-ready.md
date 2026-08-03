<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery

- **Authors:** Johann Wenckstern; Eeshaan Jain; Yexiang Cheng; Benedikt von Querfurth; Kiril Vasilev; Matteo Pariset; Phil F. Cheng; Petros Liakopoulos; Olivier Michielin; Andreas Wicki; Gabriele Gut; Charlotte Bunne
- **Venue / Year:** arXiv preprint · 2025
- **DOI:** 
- **URL:** https://arxiv.org/abs/2501.06039
- **Bibkey:** Wenckstern2025_250106039
- **Status:** complete

## Abstract
Spatial proteomics technologies have transformed our understanding of complex tissue architecture in cancer but present unique challenges for computational analysis. Each study uses a different marker panel and protocol, and most methods are tailored to single cohorts, which limits knowledge transfer and robust biomarker discovery. Here we present Virtual Tissues (VirTues), a general-purpose foundation model for spatial proteomics that learns marker-aware, multi-scale representations of proteins, cells, niches and tissues directly from multiplex imaging data. From a single pretrained backbone, VirTues supports marker reconstruction, cell typing and niche annotation, spatial biomarker discovery, and patient stratification, including zero-shot annotation across heterogeneous panels and datasets. In triple-negative breast cancer, VirTues-derived biomarkers predict anti-PD-L1 chemo-immunotherapy response and stratify disease-free survival in an independent cohort, outperforming state-of-the-art biomarkers derived from the same datasets and current clinical stratification schemes.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> source: arXiv HTML full text (https://arxiv.org/html/2501.06039v2) — cleaned extract. Numbers reflect the v2 manuscript (15 IMC datasets / 147 markers / NeoTRIP TNBC), which matches the current abstract.

### Introduction
Tissue heterogeneity, particularly in cancer, manifests across patients, disease stages, and individual tumors through diverse cell phenotypes, states, and spatial organization. Understanding tumor-microenvironment (TME) complexity is critical because tumor development and therapeutic response depend not solely on cancer cells but on their interactions with surrounding tissues. Different cell phenotypes act as promoters or suppressors of tumor progression depending on context, and spatial co-occurrence patterns predict immunotherapy response, disease relapse, and survival.

Multiplexed imaging technologies — conventional immunohistochemistry, multiplexed immunofluorescence, and imaging mass cytometry (IMC) — simultaneously measure dozens to hundreds of proteins in intact tissue sections at subcellular resolution. But each study typically uses customized antibody panels, staining protocols, and imaging platforms, so datasets differ in marker count, identity, dynamic range, and noise. Computational workflows designed for single cohorts/panels struggle to transfer knowledge between cohorts, cancer types, or platforms. VirTues addresses this as a marker-aware, multi-scale foundation model trained on a large collection of IMC and related datasets spanning multiple cancer types and centers, producing unified representations at molecular, cellular, niche, and tissue levels and processing arbitrary study-specific marker panels at inference.

### VirTues Architecture
Three key innovations: (1) protein language model embeddings encoding marker identity; (2) factorized spatial/marker attention scaling to highly-multiplexed data; (3) hierarchical summary tokens enabling multi-scale analysis while maintaining interpretability.

**Tokenization.** Multiplexed images are processed crop-wise into 3-D grids of image tokens representing patches of each marker at each position. Marker tokens derive from protein language models (ESM-2), fused with image tokens through linear projection and addition. This accommodates variable marker combinations while incorporating biological meaning and subcellular spatial marker distribution. Learnable patch summary tokens (initialized with learnable weights, concatenated with input tokens) capture patch-level information and subsequently aggregate into cell, niche, and tissue summary tokens via convolution with cell segmentation masks or direct aggregation.

**Disentangled attention.** The factorized transformer disentangles attention into two complementary components: Marker Attention (restricts token interactions to different channels, learning inter-protein relationships/dependencies) and Spatial Attention (restricts interactions to different positions, capturing tissue architecture). This overcomes the quadratic scaling of standard ViTs across spatial dimensions and channel numbers; performance improves consistently with marker depth (especially the first ~20 markers) whereas modality-agnostic designs plateau or degrade.

**Masked autoencoder pretraining.** Joint encoder-decoder training with three masking strategies: (1) Independent masking — randomly mask patches at different spatial locations for each marker independently, channel-wise ratios 60–100%; (2) Marker masking — mask all tokens of one channel, testing inter-marker relationship learning; (3) Niche masking — mask entire tissue regions across all markers at random positions, evaluating global tissue-architecture understanding. The decoder receives encoded non-masked tokens from the target channel plus all patch summary tokens and predicts channel-wise reconstructions.

**Multi-scale representations.** From the pretrained backbone: Patch summary tokens (local microenvironment composition), Cell summary tokens (aggregate patch info within segmented cell boundaries via convolution), Niche summary tokens (tissue neighborhoods and multicellular interactions), Tissue summary tokens (global tissue architecture/composition).

### Datasets
Trained/evaluated on 15 IMC datasets spanning 8 organ sites, measuring 147 distinct markers (proteins, protein modifications, mRNAs). Pretraining corpus scale: 3,102 patients; 8,887 tissue samples; over 259,000 image crops (256×256 px); over 14.5 million segmented cells (across nine datasets with segmentation masks).

Key datasets:
- Cords et al. (lung cancer): primary lung cohort with fine-grained cell-type annotations and clinical metadata.
- Wang et al. (NeoTRIP TNBC): 138 triple-negative breast cancer patients receiving chemo-immunotherapy (atezolizumab, carboplatin, nab-paclitaxel), 67 with complete pathological response; pre-, on-, and post-treatment timepoints.
- Danenberg et al. (METABRIC breast cancer): ER-positive cohort (n=541), 21-year survival follow-up.
- Rigamonti et al. (lung cancer): withheld dataset with both training markers and novel markers never seen during pretraining, for zero-shot evaluation.
- Hoch et al., Jackson et al., Meyer et al.: additional breast and melanoma datasets with varying marker panels.

### Results — Marker Reconstruction
Across three masking strategies, average Pearson r = 0.723 ± 0.157. Independent masking reconstructs spatially isolated masked regions (e.g., CAV1, CD3E in lung; MTOR, MYC in breast). Marker masking recovers complete expression of entirely masked channels (e.g., ACTA2, CD68 in lung; PTPRC, KRT19 in breast). Niche masking reconstructs complex tissue architectures with coherent marker patterns (e.g., HLA-DRA, FUT4 in lung). VirTues outperforms baselines such as mean channel-intensity reconstruction and highest-correlated-marker prediction.

### Results — Zero-Shot Generalization
On the withheld Rigamonti et al. lung dataset (seen + unseen markers): known markers reach zero-shot r = 0.667 (vs in-domain 0.797); novel markers show larger drops but retain substantial signal. Degradation occurs mainly under marker masking (complete channel occlusion); independent and niche masking barely degrade (Δr = 0.016 and −0.002). This indicates VirTues leverages transferable molecular priors from protein language models plus local spatial cues, enabling practical "virtual augmentation" of marker panels.

### Results — Cell-Level Classification
Cell summary tokens evaluated by linear probing (logistic regression) on Cords et al. (lung), Wang et al. (TNBC), Hoch et al. (melanoma), Danenberg et al. (breast). Average macro-F1 improvement: +6.31% over KRONOS and +65.79% over CA-MAE, with strong performance on rare classes (vessel <1.6%, T cells <6.3%, NK <1.8%, B cells <4.9%). Full-corpus vs single-dataset (Danenberg) training gives largest gains for rare immune populations: B cells +27.9%, myeloids +35.2%, NK +95.6%, T cells +30.4%. Zero-shot cell typing is within ≤0.03 macro-F1 of in-domain across all four datasets. Cross-cohort label transfer (random forest trained on Cords cell types, applied to Rigamonti) reaches macro-F1 0.615, beating KRONOS (0.383) and mean marker intensities (0.490).

### Results — Tissue-Level / Clinical Prediction (ABMIL on patch summary tokens)
Lung (Cords): cancer subtyping 0.856 macro-F1 (+8.9% vs KRONOS, P<0.005); grade 0.530 (+21.8%, P<0.005). Breast (Danenberg): ER status 0.806 (+14.2%, P<0.006); ERBB2 0.648 (+2.0%, P<0.007); grade 0.490 (+15.9%, P<0.008); PAM50 subtyping 0.385 (+8.2%, P<0.1). TNBC treatment response (NeoTRIP): pre-treatment 0.676 macro-F1 (+20.2% vs KRONOS, P<0.008); on-treatment 0.714 (+30.2% vs KRONOS, +31.4% vs CA-MAE, +19.5% vs ResNet, all P<0.005); post-treatment 0.678 (+18.63% vs KRONOS, P<0.005).

### Results — Risk Stratification via TME Structure
ER-positive METABRIC (n=541): patient risk groups identified by clustering phenotype-composition fingerprints (120 k-means clusters) from cell-level embeddings. High-risk (n=265): 99 deaths over 21 years; low-risk (n=276): 58 deaths; log-rank P<0.001. Risk ratios for known multicellular structures in the high-risk group: vascular stroma 0.399 (protective/underrepresented), suppressed expansion 4.464 (adverse), APC-enriched 5.636 (adverse). A purely survival-based split shows only mild APC enrichment (RR 1.472), demonstrating TME-specific signal.

### Results — Patient Retrieval for Clinical Decision Support
Patients encoded via niche summary tokens; optimal-transport (Wasserstein) retrieval of similar cases from a Virtual Tissues Database. On Cords lung: cancer subtype exceeds all baselines in mean precision; grade and relapse status significantly better than random retrieval (McNemar, P<0.05). Cellular composition similarity (L1 distance between cell-type proportions): VirTues lowest distance (best). Molecular composition similarity (sliced Wasserstein on pixel values): VirTues second behind KRONOS.

### Results — Treatment-Response Biomarker Discovery (NeoTRIP)
Cell-state distribution shifts across pre/on/post samples show clear dynamics; responders shift more than non-responders, and shifts attenuate with raw mean intensities (VirTues captures structure beyond first-order signal). Pipeline: (i) embed all pre-treatment cells with VirTues; (ii) multi-resolution Leiden clustering into a hierarchy of phenotypic partitions; (iii) aggregate cells per patient for cluster frequencies; (iv) score each cluster by cross-validated, patient-level out-of-fold AUROC and response risk. Four signatures retained: two response (RS1, RS2), two non-response (NRS1, NRS2). Univariate cross-validated AUROC: RS1 0.783, RS2 0.707, NRS1 0.599, NRS2 0.577. Multivariate (all four): cross-validated AUROC 0.817, +4.53% over Wang et al. spatial predictor (P<0.001), +23–30% over immune-ratio baselines (P<0.001).

Signature biology — RS1: apoptotic cells (+415.33%), DNA-damage markers (+496.69%), PD-L1+GZMB+ cells (+606.75%); apoptotic cells surrounded by ~90% more CD4+ T cells and +222.67% PD-L1+GZMB+ cells. RS2: CD4+ T cells (+409.96%), PD-L1+GZMB+ (+275.25%), PD-L1+IDO+ (+217.74%); CD4+ T cells near +223.96% tumor cells and +292.59% PD-L1+GZMB+ cells. Non-response signatures dominated by tumor cells (+328.49%, +358.00%) with immune/stromal depletion (NRS1 −76.205% fibroblasts; NRS2 −97.085% CD4+ T cells).

### Results — Cross-Cohort Biomarker Transfer
Signatures transferred to an independent TNBC cohort (Meyer et al.), not used in pretraining or discovery: compute VirTues cell embeddings per patient, then apply random-forest classifiers trained on the discovery cohort to assign RS/NRS labels. Response signatures localize to immune-inflamed regions; non-response signatures to immune-excluded/cold areas. Disease-free survival: combined signature frequencies form a single risk score with three strata — low-risk (n=33) 3 events vs high-risk (n=45) 21 events, log-rank P<0.005. Concordance index: VirTues 0.628 > Meyer et al. 0.606 > tumor-to-CD4 0.608 > tumor-to-CD8 0.602 > tumor-to-B 0.569.

### Marker and Spatial Attention Explainability
Spatial attention maps show coherent, anatomically plausible foci in adenocarcinoma vs squamous cell carcinoma, concentrating on tumor-rich epithelial compartments and tumor-immune interfaces, down-weighting stroma. Marker importance scores recapitulate niche biology: immune-infiltrated SCC regions weight panCK, MMP11, CD45RA, CD10; fibroblast-enriched stroma weights Vimentin, smooth muscle actin, Collagen I, CD248; immune-dense regions weight CD45RA, HLA-DR, CD20.

### Key Contributions
1. Marker-aware tokenization integrating protein-LM embeddings with spatially-patched channel information, enabling variable marker combinations with biological meaning. 2. Factorized spatial/marker attention overcoming quadratic scaling for highly-multiplexed data. 3. Multi-scale hierarchical design unifying molecular, cellular, niche, tissue levels. 4. Foundation-model approach: one backbone for marker reconstruction, zero-shot cell typing, niche annotation, tissue retrieval, and biomarker discovery without task-specific fine-tuning.

### Limitations
1. Zero-shot extrapolation degrades for markers with weak biochemical relatedness to the training set; virtual augmentation needs calibration and uncertainty reporting. 2. Rare cell states/architectures remain hard (data scarcity). 3. Survival analyses are largely unadjusted; covariate-adjusted models, proportional-hazards checks across cohorts, and prospective validation needed. 4. Attention maps give partial explanations; causal/perturbational analyses needed. 5. Trained on 15 IMC cohorts / 8 organ sites; broader validation across diseases, protocols, and platforms required. 6. H&E and other complementary modalities operate at different resolution; multimodal fusion is a natural next step.

### Future Directions
Multimodal integration (H&E, IHC, spatial transcriptomics, metabolomics, lipidomics, temporal data) within one foundation model, contingent on robust alignment and molecular embeddings; coupling marker-aware reconstruction with generative models for biologically-constrained virtual multiplexing and panel design.

### Conclusion
VirTues shows foundation models for spatial proteomics need not trade generality for clinical utility. In TNBC, VirTues-derived biomarkers predict anti-PD-L1 chemo-immunotherapy response (AUROC 0.817) and stratify disease-free survival in an independent cohort, outperforming published spatial biomarkers from the same datasets and current clinical stratification schemes, positioning VirTues as a reusable computational layer for spatial proteomics.

### Code, Checkpoints, Data (official repo: github.com/bunnelab/virtues, MIT)
Install via conda (Python 3.12); configure `configs/base_config` (experiment dirs, dataset paths, marker-embedding location, optional W&B). Training data curated as **spora** (31+ spatial-proteomics datasets) with format-conversion guides and example data. Three pretrained checkpoints on Hugging Face Hub: `virtues-sp32` (32 datasets, CC BY-NC 4.0), `virtues-sp31` (31 datasets, MIT), `virtues-imc14` (14 IMC datasets, CC BY-NC 4.0). Three demo notebooks (reconstruction, cell phenotyping, segmentation); `spora-bench` benchmarking library. Code MIT-licensed; model weights vary by training-data restrictions.
