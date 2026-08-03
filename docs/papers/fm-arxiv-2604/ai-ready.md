<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# A Generative Foundation Model for Multimodal Histopathology

- **Authors:** Jinxi Xiang; Mingjie Li; Siyu Hou; Yijiang Chen; Xiangde Luo; Yuanfeng Ji; Xiang Zhou; Ehsan Adeli; Akshay Chaudhari; Curtis P. Langlotz; Kilian M. Pohl; Ruijiang Li
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 
- **URL:** https://arxiv.org/abs/2604.03635
- **Bibkey:** Xiang2026_260403635
- **Status:** complete

## Abstract
Accurate diagnosis and treatment of complex diseases require integrating histological, molecular, and clinical data, yet in practice these modalities are often incomplete owing to tissue scarcity, assay cost, and workflow constraints. Existing computational approaches attempt to impute missing modalities from available data but rely on task-specific models trained on narrow, single source-target pairs, limiting their generalizability. Here we introduce MuPD (Multimodal Pathology Diffusion), a generative foundation model that embeds hematoxylin and eosin (H&amp;E)-stained histology, molecular RNA profiles, and clinical text into a shared latent space through a diffusion transformer with decoupled cross-modal attention. Pretrained on 100 million histology image patches, 1.6 million text-histology pairs, and 10.8 million RNA-histology pairs spanning 34 human organs, MuPD supports diverse cross-modal synthesis tasks with minimal or no task-specific fine-tuning. For text-conditioned and image-to-image generation, MuPD synthesizes histologically faithful tissue architectures, reducing Fréchet inception distance (FID) scores by 50% relative to domain-specific models and improving few-shot classification accuracy by up to 47% through synthetic data augmentation. For RNA-conditioned histology generation, MuPD reduces FID by 23% compared with the next-best method while preserving cell-type distributions across five cancer types. As a virtual stainer, MuPD translates H&amp;E images to immunohistochemistry and multiplex immunofluorescence, improving average marker correlation by 37% over existing approaches. These results demonstrate that a single, unified generative model pretrained across heterogeneous pathology modalities can substantially outperform specialized alternatives, providing a scalable computational framework for multimodal histopathology.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->

**Affiliations:** Stanford University School of Medicine; Yale University.

**Note on naming:** The abstract names the model **MuPD (Multimodal Pathology Diffusion)**; some passages of the HTML render it **MUPAD**. Both refer to the same model.

### Introduction
Modern pathology requires integrating multiple data modalities — H&E histology, immunohistochemistry (IHC), multiplex immunofluorescence (mIF), and molecular profiling. Acquiring complete multimodal datasets remains impractical due to tissue scarcity, assay cost, and workflow constraints. Existing computational approaches rely on task-specific models trained on narrow paired (single source→target) datasets, which limits generalizability. The paper argues that a single, unified generative model trained at scale on heterogeneous pathology modalities can substantially outperform specialized alternatives. MuPD establishes H&E histology as the central bridging modality, enabling coherent cross-modal synthesis across transcriptomics, proteomics, tissue-preparation protocols, and clinical text. The architecture is a Diffusion Transformer with decoupled cross-modal attention that processes text, RNA, and image embeddings through separate attention streams.

### Method

**Architecture.** MuPD is built on a Scalable Interpolant Transformer (SiT) that jointly conditions image generation on transcriptomics, text, and reference images.

**Decoupled Cross-Attention (DCA).** Rather than forcing heterogeneous modalities to compete within a shared key–value space, DCA processes each modality through independent parallel attention streams queried by intermediate image representations. This preserves the unique biological characteristics of each modality while enabling flexible conditioning.

**Feature Alignment.** The model aligns its internal features with a pretrained pathology encoder (Virchow2) through a lightweight CNN projector, combining spatial alignment with an auxiliary CLS-token denoising loss for global semantic consistency.

**Training details.** Trained with AdamW on 8× H100 GPUs for up to 500K steps in bfloat16. Images are encoded via a frozen VAE with 8× downsampling. Classifier-free guidance uses 10% condition dropout.

### Datasets

Pretraining corpus:
- 100 million 512×512 H&E patches at 20× magnification from TCGA, GTEx, PAIP, and PLCO.
- 1.6 million text–image pairs from PathGen-1.6M.
- 10.8 million RNA–image pairs from TCGA bulk RNA-seq linked to matched whole-slide images.

RNA profiles are normalized to TPM and compressed into 331 pathway-level enrichment scores using pan-cancer gene signatures. Pretraining spans 34 human organs.

Evaluation datasets: HISTAI, PathMMU, SkinCancer, PanNuke, UniToPatho, LC25000, SICAPv2, MOSAIC spatial transcriptomics, TCGA, HER2Match, IHC4BC, and the ORION colorectal cancer dataset.

### Results

**Image-to-image generation** (vs. PixCell, Stable Diffusion 3.5, FLUX.2):
- Image–Image similarity 0.63 vs. PixCell 0.46.
- FID 305.12 vs. PixCell 602.45 (≈49% improvement).

**Text-to-image generation** (vs. PathLDM, SD v3.5, FLUX.2):
- FID 576.30 vs. PathLDM 1029.62 (≈44% improvement).
- Text–image alignment 0.53 vs. PathLDM 0.41.

**Synthetic data augmentation (few-shot classification):**
- PanNuke (10-shot): accuracy 0.492 → 0.724 (+47.2%).
- SkinCancer (10-shot): 0.790 → 0.850.
- Vision–language retrieval (Book dataset): image→text R@10 6.14% → 15.94%; text→image R@10 4.77% → 16.76%.

**Spatial-transcriptomics → H&E generation** (vs. GeneFlow, five cancer types):
- Bladder cancer FID 724.6 vs. GeneFlow 1012.5 (≈28% improvement).
- Cell-type distribution preserved with markedly lower Wasserstein distances.

**Fresh-frozen → FFPE translation** (lung): FID 323.7 vs. AI-FFPE 435.3 (≈26% relative reduction).

**H&E → IHC translation** (five markers, FID/KID):
- ER marker FID 124.18 vs. CycleGAN 256.76.
- Clinical utility (AUC): Ki67 0.9772, HER2 0.9556.

**H&E → mIF translation** (Pearson correlation, PCC):
- Average patch PCC 0.238 vs. GigaTIME 0.198 and HistoPlexer 0.071.
- Slide-level PCC 0.464 vs. GigaTIME 0.339.
- Superior on immune markers (e.g., PD-L1 patch PCC 0.218).

**Ablation studies.**
- Decoupled Cross-Attention: replacing DCA with shared cross-attention degraded performance — relative FID reductions of 13.6% (image→image), 7.9% (text→image), 12.4% (RNA→image).
- Alignment loss: CNN-based spatial alignment with CLS-token denoising outperformed alternatives — image similarity 0.424 vs. REPA 0.243 at 100K steps.

### Discussion
The paper argues that superficially distinct pathology generation tasks are projections of a shared cross-modal biological distribution; a unified model trained at sufficient scale can represent this distribution directly, enabling transferable knowledge across tasks. Routine H&E histology appears to encode latent molecular information — tissue morphology reflects underlying transcriptional programs and protein expression. MuPD's preservation of cell-type composition during RNA-conditioned generation, and its localization of immune markers from morphology alone, provide empirical evidence for this principle. Virtual-staining results show that even structurally degraded frozen sections retain enough morphological information to recover diagnostically faithful architecture when informed by appropriate tissue priors.

### Limitations and Future Directions
Diffusion models are inherently stochastic and may produce anatomically implausible outputs under distribution shift. Clinical deployment requires prospective validation of computational biomarker concordance with laboratory measurements. The work is hypothesis-generating rather than diagnostic until validated across representative populations.

### Conclusion
MuPD advances understanding of the information content encoded in routine histology and expands diagnostic access where specialized assays are unavailable. By explicitly modeling joint distributions across histological, molecular, and clinical modalities, it provides scalable infrastructure for training future discriminative models on synthetic multimodal data. As pretraining corpora expand and additional modalities are incorporated, unified generative frameworks represent core infrastructure for computational pathology.
