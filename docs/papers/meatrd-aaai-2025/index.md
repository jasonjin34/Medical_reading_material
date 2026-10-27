# MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics

> **Bibkey** `Xu_2025` · **Venue** Proceedings of the AAAI Conference on Artificial Intelligence (2025) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1609/aaai.v39i12.33409> · `status: complete`

---

## One-liner
MEATRD is a follow-up from the STANDS group (Xu, Sun et al.): **trained only on normal tissue**, it treats each Visium spot as a graph node, reconstructs both its H&E patch and its gene expression (core: a masked graph dual-attention transformer, MGDAT, with target-node masking), then trains a Deep-SVDD-style one-class classifier on **latent multimodal reconstruction errors** for anomaly scoring. On 8 human breast-cancer ST datasets it reaches mean AUC 0.723 / F1 0.741, beating 9 image, ST and multimodal baselines, and catches visually subtle tumour edges.

## Problem
Anomalous tissue region (ATR) detection traditionally uses H&E alone, but histology is complex, ATRs can look nearly normal, and staining varies — image-only methods fail on visually normal-looking regions such as tumour edges. ST offers a molecular view but is noisy with many dropouts; the only ST-only method, Spatial-ID, relies on classification uncertainty and confuses similarity among normal tissues with anomaly. What is missing is a method that fuses image and ST and is robust both to **over-generalization** in reconstruction methods (anomalies reconstructed too well) and to **reference–target domain shift** in one-class methods.

## Method
Setting: train on normal reference ST + images, find anomalous spots in a target slice. Three stages: **Stage I** — cut a 32×32 patch around each spot and pretrain a Mobile-UNet image encoder (SSIM perceptual + L1 loss); genes get no pretext stage, just a two-layer MLP projection. **Stage II** — spots are nodes of a kNN graph (k=6, hexagonal layout), with a 3-hop subgraph per target node; **the target node's image and gene features are both replaced by learnable mask tokens** to prevent self-information leakage (curbing over-generalization); each MGDAT block first uses a Transformer over the concatenated modalities to produce a low-dimensional **fused bottleneck embedding** (cross-modal), then concatenates it with each modality's embedding for graph-attention aggregation (cross-node); a ResNet deconvolutional decoder rebuilds the patch and a single-layer GNN decoder rebuilds expression, with loss α·(SSIM+L1) + (1−α)·scaled cosine error (SCE). **Stage III** — light ResNet / MLP encoders map originals and reconstructions to a latent space; the β-weighted fused difference is the **latent multimodal reconstruction error**, and normal spots' errors are collapsed to a hypersphere centre c (Deep SVDD style); the anomaly score is the distance to c, thresholded automatically with a MAP-EM mixture model. The supplement gives a theoretical analysis of the bottleneck embedding's information properties.

## Data
Training: 8 human normal-breast 10x Visium datasets (10x-hNB-v03 to v10); testing: 8 human breast-cancer 10x Visium datasets (10x-hBC-A1 to H1), plus 10x-hBC-I1 (with a tumour edge visually similar to normal tissue) for a case study; 4 primary sclerosing cholangitis (PSC) datasets are reported in the supplement.

## Key results
- **8 breast-cancer datasets**: MEATRD ranks first in AUC on every dataset and first in F1 on 6/8; mean AUC 0.723, F1 0.741. The authors report average gains over the runner-up of 17.45% AUC and 10.31% F1. Baselines are image-based (Patch SVDD, SimpleNet, f-AnoGAN), ST-based (scmap, CAMLU, PREM, DOMINANT, Spatial-ID) and multimodal M3DM; the PDF table shows the graph method DOMINANT as the best baseline by mean AUC (~0.55).
- **General pattern**: methods using ST generally beat image-only ones; the multimodal M3DM, which ignores spatial relations between spots, trails MEATRD — spatial context matters.
- **Visually subtle tumour edge (10x-hBC-I1)**: MEATRD-β (image weight β 0.5→0.1) gets precision 0.693 / recall 0.895, standard MEATRD 0.672 / 0.666, DOMINANT 0.648 / 0.780, SimpleNet 0.632 / 0.410, f-AnoGAN 0 / 0 — here the image adds little and ST should be weighted more.
- **Ablation (mean AUC / F1)**: full 0.723 / 0.741; ST only 0.631 / 0.667; image only 0.497 / 0.544; w/o MGDAT 0.639 / 0.689; w/o target-node masking 0.655 / 0.699; w/o reconstruction-error input (embeddings instead) 0.642 / 0.685; w/o one-class stage 0.584 / 0.631. Four MGDAT layers collapse performance (0.533 / 0.565).

## Contributions
- Chains the reconstruction and one-class paradigms: one-class classification on reconstruction errors (not instance embeddings) addresses both over-generalization and domain shift.
- MGDAT: fused bottleneck for cross-modal sharing + graph attention for cross-spot sharing + target-node masking against leakage.
- Theoretical analysis that the multimodal bottleneck collects and condenses modality-specific, task-relevant information (Supplement D).
- Shows ST can detect visually inconspicuous ATRs, with a tunable modality weight β.

## Limitations
- Evaluation is almost entirely breast-cancer Visium (PSC only in the supplement); ATR labels are region-level pathology annotations, and tumour is a relatively "easy" anomaly.
- Claims to be the "first" method integrating histology and ST for ATR detection, yet the group's earlier STANDS (also image + ST) is not among the main-text baselines — an incomplete comparison.
- The best modality weight β depends on the scenario (β=0.1 for tumour edges), with no answer for choosing β without labels.
- Thresholding relies on a MAP-EM mixture that assumes a gap between normal and anomalous scores; F1 is evaluated at the true anomaly proportion, which is unknown in deployment.
- 32×32 patches at spot (55 µm) resolution; single-cell-resolution platforms are not addressed.

## Relation to our direction
MEATRD is the representative **multimodal (H&E + ST), normal-only-trained** method for the detect stage, sibling to STANDS (`spatial-natcommun-2024`) and complementary to the statistical route of Sardine (`sardine-bioinformatics-2025`). The most direct lesson for **Topic 1** concerns **cross-modal agreement**: the 10x-hBC-I1 case shows that "normal-looking image + abnormal expression" is a real disease signal (tumour edge), not an artifact — so Topic 1 cannot treat every cross-modal disagreement as artifact; it must separate "invisible in image but consistently abnormal across molecular modalities" (disease) from "abnormal in only one molecular modality and correlated with QC metrics" (artifact). Paired Xenium + H&E matches MEATRD's input form, making it a multimodal deep baseline for KidneyAnomalyBench (with spots replaced by cells or bins and KPMP / HuBMAP normal kidney as the reference). The unsupervised choice of β and the threshold's dependence on the true anomaly fraction are exactly what an expert-validated benchmark can help calibrate. For **Topic 2**: "first-ever" claims alongside a missing baseline (STANDS) are textbook targets for claim-to-evidence checking — a verifier should flag inconsistency between novelty claims and related-work coverage.

## Reusable assets
- **Code**:
<https://github.com/wqlzuel/MEATRD>
- **Extended version (with supplement)**:
<https://arxiv.org/abs/2412.10659>
- **Benchmark setup**: train on normal breast 10x-hNB-v03–v10 → test on breast cancer 10x-hBC-A1–H1, AUC + F1 (threshold = true anomaly proportion), mean ± s.d. over 5 runs; the 9-baseline list is reusable.

## Follow-ups
- The arXiv supplement: PSC results, MAP-EM thresholding, bottleneck theory, complexity analysis.
- A head-to-head with STANDS on the same data (not done here).
- Spatial-ID, CAMLU, DOMINANT papers — ST / graph anomaly baselines.
- Whether swapping the Mobile-UNet encoder for a pathology foundation model (UNI2-h, Virchow) helps.

## Cite
```bibtex
@article{Xu_2025, title={MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics}, volume={39}, ISSN={2159-5399}, url={http://dx.doi.org/10.1609/aaai.v39i12.33409}, DOI={10.1609/aaai.v39i12.33409}, number={12}, journal={Proceedings of the AAAI Conference on Artificial Intelligence}, publisher={Association for the Advancement of Artificial Intelligence (AAAI)}, author={Xu, Kaichen and Wu, Qilong and Lu, Yan and Zheng, Yinan and Li, Wenlin and Tang, Xingjie and Wang, Jun and Sun, Xiaobo}, year={2025}, month=Apr, pages={12918–12926} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
