# DRÆM – A discriminatively trained reconstruction embedding for surface anomaly detection

> **Bibkey** `Zavrtanik2021_210807610` · **Venue** 2021 IEEE/CVF International Conference on Computer Vision (ICCV) (2021) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2108.07610> · `status: complete`

---

## One-liner
DRÆM recasts surface anomaly detection from "learn normal only, read the reconstruction error" into a **discriminative problem**: it pastes "just-out-of-distribution" synthetic anomalies onto normal images (Perlin-noise masks + external textures) and jointly trains a reconstructive sub-network that inpaints them back to normal and a discriminative sub-network that reads "original ⊕ reconstruction" and outputs a pixel-level anomaly map — 98.0% image AUROC and 68.4% pixel AP on MVTec AD, +2.5 and +13.4 points over the previous best.

## Problem
Surface anomalies occupy a small fraction of pixels and are often close to the normal distribution. Reconstruction methods (AEs, GANs, AnoGAN/f-AnoGAN) train on normal data only and rely on "anomalies reconstruct badly", yet near-normal anomalies are often reconstructed well (over-generalization), and anomaly maps need hand-crafted post-processing (e.g., SSIM comparison), so features cannot be optimized for detection. Conversely, training a segmenter directly on synthetic anomalies **over-fits the synthetic appearance** and generalizes poorly to real defects. DRÆM asks how to train discriminatively end-to-end, without real anomalies, and still generalize to them.

## Method
**Reconstructive sub-network**: an encoder–decoder taking the simulator-corrupted image I_a and restoring the original normal image I, with loss λ·SSIM loss + L2 (SSIM accounting for neighbouring-pixel dependence). It learns to rewrite local anomalous patterns as normal while leaving normal regions untouched. **Discriminative sub-network**: a U-Net-like net taking the channel-wise concatenation of I_a and the reconstruction I_r; since the reconstruction "normalizes" anomalies, their joint appearance differs strongly there, so the network **learns a local-appearance-conditioned distance function** instead of a hand-crafted SSIM; supervised with Focal Loss on the pixel mask. Total loss = L_rec + L_seg. **Anomaly simulator**: Perlin noise gives random shapes, binarized at a random threshold into mask M_a; textures come from the domain-unrelated DTD texture dataset, with 3 random RandAugment-style ops (from posterize, sharpness, solarize, equalize, brightness, colour, auto-contrast); blending I_a = M̄_a⊙I + (1−β)(M_a⊙I) + β(M_a⊙A) with opacity β ∈ [0.1, 1.0] — low β yields subtle perturbations that tighten the decision boundary. The simulator also yields a pixel-perfect mask. **Inference**: the map M_o is mean-filtered (s_f×s_f) and its maximum is the image score η. Trained 700 epochs, lr 1e-4 (×0.1 at epochs 400 and 600), with (−45°, 45°) rotation augmentation on normal images.

## Method lineage
**Paradigm: synthetic anomalies / self-supervised** (a hybrid with a reconstructive helper, but the core discriminative signal comes from synthetic anomalies). **Builds on**: the reconstruction line (Bergmann et al.'s SSIM-AE, GANomaly, AnoGAN, f-AnoGAN — cited and used as foils) and the authors' own RIAD (inpainting reconstruction); contemporaneous CutPaste is also synthetic-anomaly self-supervision. DRÆM's key difference: synthetic anomalies **need not be realistic**, only just-out-of-distribution, and the discriminator learns "extent of deviation from normal" rather than anomaly appearance. **Led to**: a standard synthetic-anomaly baseline (pathology-ad-bench-mlhealth-2025 benchmarks DRAEM alongside CutPaste as synthetic-anomaly methods; the one-stage SSL family in medianomaly-media-2025 — FPI/NSA/PII/AnatPaste — follows the same idea); many later industrial methods reuse its Perlin-mask + external-texture simulator.

## Data
**MVTec AD** (15 classes, normal-only training); **DAGM 2007** (10 synthetic texture classes with coarse ellipse defect labels, used to compare against supervised methods; image classification only). Texture source for simulation: **DTD** (Describable Textures Dataset), swapped for ImageNet in an ablation.

## Key results
- **Image detection (MVTec AUROC)**: DRÆM averages **98.0%**, best on 9 of 15 classes, vs PaDiM 95.5%, Rippel et al. (MAD) 94.4%, RIAD 91.7%, Uninformed Students 87.7%, GANomaly 78.2%. Weaker classes: transistor 93.1%, cable 91.8% (missing-part anomalies are hardest).
- **Localization (pixel AUROC / AP)**: DRÆM 97.3 / **68.4** vs PaDiM 97.4 / 55.0, RIAD 94.2 / 48.2, US 93.9 / 45.5 — AUROC on par, AP +13.4 points; the authors stress that with few anomalous pixels AUROC is dominated by normal pixels and AP is more appropriate.
- **Ablations (det. / loc. AUROC / AP)**: discriminative net alone 93.9 / 92.7 / 62.5 (over-fits synthetic anomalies); reconstructive net + SSIM alone 83.9 / 89.7 / 47.5; swapping in the supervised defect network of Božič et al. 92.8 / 93.9 / 60.7; ImageNet as texture source 97.9 / 97.0 / 67.9; **plain colour patches** instead of textures still 96.2 / 92.6 / 56.5; rectangular masks instead of Perlin 96.9 / 96.8 / 65.1; no augmentation or opacity randomization 97.4 / 94.5 / 64.3; β randomization only 97.9 / 97.1 / 68.4. Fewer than 10 texture images suffice for high performance.
- **DAGM**: DRÆM image AUROC 99.0%, classification accuracy 98.5% — best unsupervised (PaDiM 95.0% / 95.7%), close to fully supervised (Božič et al. 100%), and better-localized than supervised methods trained on coarse labels.

## Contributions
- Casts surface AD primarily as a **discriminative problem**, learning a distance function on the joint "original + reconstruction" embedding without hand-crafted post-processing.
- The **"just-out-of-distribution" synthetic-anomaly** principle: simulations need not be realistic — Perlin masks + unrelated textures + random opacity suffice; even plain colour patches reach near-SOTA in ablation.
- Pixel AP as the better metric for highly imbalanced localization.

## Limitations
- Missing parts and background-like anomalies are hard (e.g., cut transistor leads); some errors stem from ambiguous ground-truth masks.
- Requires training two networks from scratch for 700 epochs, one model per class — far costlier than training-free PaDiM/PatchCore.
- The simulator targets **texture/appearance** anomalies (local pastes); it has no mechanism for logical/structural (missing, misplaced) or semantic anomalies.
- "Simulations need not be realistic" is shown only on industrial surfaces; transfer to complex tissue morphology is untested.

## Relation to our direction
DRÆM's main value for Topic 1 is not the network but the idea of **training and evaluating with synthetic perturbations of known ground truth** — which maps directly onto KidneyAnomalyBench's ground-truth layer. **Mapping to kidney omics**: samples = cells/spots; normal training set = healthy reference; "Perlin mask" = a randomly chosen spatially connected region on a Xenium/Visium section; "external texture paste" = injected expression shifts inside that region (scaling a gene set in the injury direction, mixing in another cell type's profile, changing cell density or composition); "opacity β" = perturbation strength, low β being subclinical change; on H&E the Perlin + texture simulator ports unchanged for patch-level synthetic anomalies. The reconstructive sub-network corresponds to a model that "restores a cell/neighbourhood to its healthy state" — which is also what the revert stage wants: **the difference between the reconstructed healthy version and the observation is the change to be reverted**. **What breaks**: (1) DRÆM's simulations need not be realistic because industrial defects are local appearance changes; kidney disease (fibrosis, PT injury) is a **continuous, diffuse** state change, so "just out of distribution" is ill-defined and the discriminator may learn the signature of the synthetic perturbation rather than disease; (2) if synthetic perturbations look like technical artifacts (ambient RNA = "mixed-in expression of another type", doublets = "two cells blended", segmentation errors = misassigned transcripts), the model conflates artifact with disease — but this is also an opportunity: **deliberately simulate ambient/doublet/segmentation errors as one synthetic "artifact" class and injury-direction shifts as another, and train the model to tell them apart**, mirroring Topic 1's artifact-vs-disease separation; (3) omics has no pixel masks, but synthetic perturbations come with masks, enabling PRO/AP-type metrics. **Existing repo papers with the same idea**: pathology-ad-bench-mlhealth-2025 benchmarks DRAEM directly and builds known-ground-truth synthetic pathology by overlaying patterns on normal Unitopatho patches; medianomaly-media-2025 systematically compares synthetic-anomaly SSL methods (CutPaste, FPI, NSA, PII, AnatPaste) and finds reconstruction clearly beats SSL for segmentation (a plain AE beats every one-stage SSL segmenter on BraTS2021) and that **more realistic synthetic anomalies help** (two-stage AnatPaste over CutPaste: +20.2% AUC on RSNA) — the opposite of DRÆM's "need not be realistic", and an important caution for DRÆM-style methods in biomedicine; the artifact models in ambient-rna-bench-biorxiv-2026 / xenium-split-natmethods-2026 / ovrlpy-natbiotech-2026 could serve as generators for "artifact-type" synthetic perturbations.

## Reusable assets
- **Code:** official PyTorch implementation (training, evaluation, and per-class pretrained MVTec models).
<https://github.com/VitjanZ/DRAEM>
- **Library:** the DRAEM implementation in anomalib (used by pathology-ad-bench-mlhealth-2025).
<https://github.com/open-edge-platform/anomalib>
- **Simulator recipe:** Perlin mask (random threshold) + external texture + 3 random augmentations + β ∈ [0.1, 1] blending — rewritable as a "region × expression perturbation × strength" generator on spatial-omics sections.
- **Data:** the DTD texture dataset (anomaly source).

## Follow-ups
- CutPaste (Li et al., CVPR 2021) — the contemporaneous synthetic-anomaly self-supervised method, for comparison.
- The authors' RIAD (Pattern Recognition 2020) and their later DSR (dual subspace re-projection, aimed at near-in-distribution anomalies).
- Design KidneyAnomalyBench's synthetic layer: injury-direction perturbations vs ambient/doublet/segmentation-artifact perturbations, each with spatial masks.

## Cite
```bibtex
@inproceedings{Zavrtanik2021_210807610,
  title = {{DR{\AE}M} -- A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection},
  author = {Zavrtanik, Vitjan and Kristan, Matej and Sko{\v{c}}aj, Danijel},
  booktitle = {2021 IEEE/CVF International Conference on Computer Vision (ICCV)},
  pages = {8310--8319},
  publisher = {IEEE},
  year = {2021},
  doi = {10.1109/ICCV48922.2021.00822},
  eprint = {2108.07610},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2108.07610}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
