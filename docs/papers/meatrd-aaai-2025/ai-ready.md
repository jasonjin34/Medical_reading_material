<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics

- **Authors:** Xu, Kaichen; Wu, Qilong; Lu, Yan; Zheng, Yinan; Li, Wenlin; Tang, Xingjie; Wang, Jun; Sun, Xiaobo
- **Venue / Year:** Proceedings of the AAAI Conference on Artificial Intelligence · 2025
- **DOI:** 10.1609/aaai.v39i12.33409
- **URL:** https://doi.org/10.1609/aaai.v39i12.33409
- **arXiv (extended version):** https://arxiv.org/abs/2412.10659
- **Code:** https://github.com/wqlzuel/MEATRD
- **Bibkey:** Xu_2025
- **Status:** complete

## Abstract
The detection of anomalous tissue regions (ATRs) within affected tissues is crucial in clinical diagnosis and pathological studies. Conventional automated ATR detection methods, primarily based on histology images alone, falter in cases where ATRs and normal tissues have subtle visual differences. The recent spatial transcriptomics (ST) technology profiles gene expressions across tissue regions, offering a molecular perspective for detecting ATRs. However, there is a dearth of ATR detection methods that effectively harness complementary information from both histology images and ST. To address this gap, we propose MEATRD, a novel ATR detection method that integrates histology image and ST data. MEATRD is trained to reconstruct image patches and gene expression profiles of normal tissue spots (inliers) from their multimodal embeddings, followed by learning a one-class classification AD model based on latent multimodal reconstruction errors. This strategy harmonizes the strengths of reconstruction-based and one-class classification approaches. At the heart of MEATRD is an innovative masked graph dual-attention transformer (MGDAT) network, which not only facilitates cross-modality and cross-node information sharing but also addresses the model over-generalization issue commonly seen in reconstruction-based AD methods. Additionally, we demonstrate that modality-specific, task-relevant information is collated and condensed in multimodal bottleneck encoding generated in MGDAT, marking the first theoretical analysis of the informational properties of multimodal bottleneck encoding. Extensive evaluations across eight real ST datasets reveal MEATRD's superior performance in ATR detection, surpassing various state-of-the-art AD methods. Remarkably, MEATRD also proves adept at discerning ATRs that only show slight visual deviations from normal tissues.

## Full text / Extract
> Source: open AAAI-25 proceedings PDF (pp. 12918–12926). The text below is a structured extract of key method and result passages (equations simplified; numbers copied from the paper's tables). Supplementary material (PSC results, MAP-EM thresholding, theory) not included.

### Problem definition
Spots of a reference ST dataset (normal tissue only) and its histology image are used for training; the task is to identify the subset of anomalous spots in a target ST dataset and image, using a model trained exclusively on the reference. Spots are nodes of an unweighted attributed kNN graph (k = 6, matching the hexagonal Visium layout), with node features = [image-patch embedding || gene-expression embedding].

### Method (three stages)
- **Stage I — visual features.** Whole-slide images are cut into 32×32 patches centred on each spot. A Mobile-UNet (downsampling conv + inverted residual blocks; upsampling deconv decoder with shortcuts) is pretrained to reconstruct each patch with L_pretrain = −SSIM(P, P̂) + ||P − P̂||₁. The encoder E1 then yields patch embeddings. Gene data get no pretext stage; a two-layer MLP projects expression in Stage II.
- **Stage II — Masked Graph Dual-Attention Transformer (MGDAT).** For each target node, a subgraph of up to 3-hop neighbours is used (more hops over-smooth, fewer limit information spread). The target node's image and gene attributes are replaced by learnable mask tokens ("target-node masking") to prevent self-information leakage and curb over-generalization. In each block a Transformer over the concatenated modalities produces a low-dimensional fused bottleneck embedding (cross-modal sharing); this is concatenated with each modality's embedding and aggregated over neighbours by graph attention (cross-node sharing). Patches are reconstructed by a ResNet-based deconvolutional decoder and expression by a single-layer GNN decoder. Loss: L_rec = α·Σ(−SSIM + L1) + (1−α)·Σ SCE(x, x̃), with scaled cosine error SCE = (1 − cos(x, x̃))^γ, γ ≥ 1.
- **Stage III — latent multimodal reconstruction-loss discriminator.** Original and reconstructed patches pass through a light ResNet, original and reconstructed expression through an MLP; normalized embeddings are β-weighted and mapped by an FFN; the latent multimodal reconstruction error ℓ_rec = Z_fused − Z̃_fused. A one-class objective collapses inliers' ℓ_rec onto the centre c = mean(ℓ_rec) (L_occ = ||ℓ_rec − c||²). Anomaly score AS_j = ||ℓ_rec,j − c||²; the threshold is chosen automatically by a MAP-EM mixture model.

### Experimental setup
Trained on eight human normal-breast ST datasets (10x-hNB-v03 to v10), tested on eight human breast-cancer ST datasets (10x-hBC-A1 to H1); four primary sclerosing cholangitis (PSC) datasets in the supplement. Baselines: image-based Patch SVDD, SimpleNet, f-AnoGAN; ST-based scmap, CAMLU, PREM, DOMINANT, Spatial-ID; multimodal M3DM. Metrics: AUC and F1 (threshold matched to the true anomaly proportion), mean ± s.d. over five runs.

### Key results (quoted/copied from the paper)
- "MEATRD's superiority over baselines in detecting ATRs across datasets, consistently ranking first in AUC scores and six times in F1 scores. It outperforms the second-best performing method with an average leap of 17.45% in AUC scores and 10.31% in F1 scores."
- Methods using ST data (DOMINANT, scmap, CAMLU) tend to outperform image-only ones; M3DM (multimodal but ignoring spatial relations among spots) does not perform as well as MEATRD.
- Tumour edge visually resembling normal tissue (10x-hBC-I1), mean precision / recall over five runs: MEATRD-β (β 0.5→0.1) 0.693 / 0.895; MEATRD-standard 0.672 / 0.666; DOMINANT 0.648 / 0.780; SimpleNet 0.632 / 0.410; f-AnoGAN 0.000 / 0.000.

**Ablation (mean over 8 breast-cancer datasets)**

| Variant | AUC | F1 |
|---|---|---|
| ST only | 0.631 | 0.667 |
| Image only | 0.497 | 0.544 |
| w/o MGDAT | 0.639 | 0.689 |
| w/o target-node masking | 0.655 | 0.699 |
| w/o reconstruction errors (embeddings into Stage III) | 0.642 | 0.685 |
| w/o one-class stage | 0.584 | 0.631 |
| Full MEATRD | 0.723 | 0.741 |

**Sensitivity (Table 2; defaults are shaded in the PDF — here inferred as the setting matching the full-model 0.723 / 0.741)** — α 0.9/0.5/0.1: AUC 0.678/0.723/0.709, F1 0.696/0.741/0.725; β 0.9/0.5/0.1: AUC 0.654/0.723/0.699, F1 0.668/0.741/0.718; bottleneck 16/64/256: AUC 0.723/0.715/0.682; MGDAT layers 2/3/4: AUC 0.694/0.723/0.533.

### Conclusion (paraphrased)
MEATRD treats spots as graph nodes, fuses image and ST via MGDAT, and combines one-class classification with reconstruction-deviation detection to address reference–target domain shift and over-generalization; it outperforms SOTA AD methods on real ST data including visually subtle ATRs, and the framework is proposed as generalizable to other image + graph multimodal AD tasks.
