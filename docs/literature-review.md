# Literature Review
### Anomaly-detection-based virtual tissue modelling

Direction: detect image / spatial-omics regions changed by disease or drug perturbation (**anomaly detection**) → model tissue as a manipulable **virtual tissue** → predict the key genes / perturbations that **revert** the anomaly (validated in the wet lab).

This review organises the 18 items along a three-stage pipeline plus the cross-cutting **foundation-model** and **data** substrate, ending with gaps and recommendations. Each item links to its close-reading.

---

## Stage 1 — Anomaly detection

**Core idea.** Learn the distribution of *normal* tissue and score departures from it — the *learn normal, flag deviation* recipe. This is the first step of localizing change.

- [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md) — **STANDS** (Nat. Commun. 2024): multi-sample detect→align→subtype of anomalous domains in **spatial transcriptomics**; GAN reconstruction error is the anomaly score. The closest on-modality reference. Code `Catchxu/STANDS` (GPL-3.0).
- [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md) — **NEJM AI 2024**, clinical-grade histopathology anomaly detection. Outlier-Exposure + ResNet-18 best; stomach slide-AUROC 95.0%, colon 91.0%, robust external validation; auto-clears 36% of normal slides at 100% sensitivity.
- [`histo-miccai-2025`](papers/histo-miccai-2025/index.md) — **AnoPILaD** (MICCAI 2025): a latent diffusion model that reconstructs *back to normal*; input-vs-reconstruction discrepancy = anomaly; patch-AUC 0.959. This **reconstruct-to-normal** idea is an image-domain prototype of virtual-tissue reversion, bridging stages 1↔2. Code `QuIIL/AnoPILaD` (MIT).
- [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md) — **PathPrism** (Cancer Cell 2026, open access). Interpretable semantic learning + **structure-preserving counterfactuals** (VirtualWSI) over a 628-dim spatial-biomarker atlas — spanning stage 1 (risk/saliency) and stage 2 (semantic virtual tissue). Code `KatherLab/PathPrism`. Flagged "important".
- [`histo-anomaly-bi-repo`](papers/histo-anomaly-bi-repo/index.md) — Boehringer engineering baseline: deep features of healthy tissue + one-class SVM, 94% balanced accuracy on H&E. A reusable **histopath anomaly-detection baseline** and template (MIT).
- [`imaging-nature-2026`](papers/imaging-nature-2026/index.md) ★ and [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md) — **cross-modal methodological analogues**: an ECG deep-learning biomarker for sudden cardiac death (Nature 2026) and abnormal ejection fraction from non-contrast chest CT (CT–LVEF, AUROC 0.79). Cardiac modality, but the "opportunistically detect anomalies from routine exams" paradigm transfers.

**Takeaway.** Mature *learn-normal, flag-anomaly* methods already exist for histology and spatial-omics (STANDS, AnoPILaD, NEJM-AI); the diffusion/counterfactual ones (AnoPILaD, PathPrism) naturally point at "how to turn the anomaly back to normal" — the bridge to stages 2 and 3.

---

## Stage 2 — Virtual-tissue modelling

**Core idea.** Represent tissue as a queryable, interventionable generative model that supports *in silico* perturbation.

- [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md) ★ — **VirTues** (arXiv 2501). A multi-scale, marker-aware "virtual tissue" Transformer; 15 IMC datasets / 147 markers / 3,102 patients; reconstruction r=0.723, cell-typing +6.3% over KRONOS, TNBC AUROC 0.817. **The core "virtual tissue" paper** here; its MAE reconstruction error doubles as an anomaly score (links to stage 1). Code `bunnelab/virtues` (MIT) + HF checkpoints.
- [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md) ★ — **MintFlow** (bioRxiv 2025). A flow-matching model that **disentangles** spatial expression into intrinsic + microenvironment-induced parts (X = X_int + X_mic) and supports *in silico* tissue perturbation: deleting TLS macrophages "de-exhausts" T cells and flips a TCGA survival signal from p=0.0073 (worse) to p=0.0034 (benefit). **Bridges stages 2 and 3.** Code `Lotfollahi-lab/mintflow`.

**Takeaway.** VirTues gives the skeleton for turning tissue into a model; MintFlow gives the mechanism for causal intervention that reverts phenotype — together they are almost a stage-2→3 prototype for this direction.

---

## Stage 3 — Revert via gene & perturbation prediction

**Core idea.** Solve the inverse problem: which perturbation pushes an anomalous state back to normal.

- [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md) — **Conditional Monge Gap** (Nat. Mach. Intell. 2026). Optimal-transport learning of generalizable single-cell perturbation maps — predicting how a cell state moves under perturbation, exactly the tool needed to revert anomalies. Open-source `AI4SCR/conditional-monge-gap`.
- [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md) — MintFlow's reprogramming echoes the same goal at **spatial scale** (see stage 2).
- [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md) — the **Arc Institute Virtual Cell Challenge** (2025). Task: context generalization — predict single-gene CRISPR effects in held-out H1 hESCs; STATE baseline, DES/PDS/MAE metrics. A **public benchmark** for our perturbation models (caveat: single-cell scale only).

**Takeaway.** Perturbation prediction has tools (Monge-Gap) and a benchmark (VCC) at single-cell scale, and a spatial-scale start (MintFlow); wiring the *anomaly-detection residual* into the *perturbation-prediction input* is the most original piece of this direction.

---

## Cross-cutting — Foundation backbones

Pathology foundation models recur as feature extractors (Stage 1) and representation backbones (Stage 2).

- [`virchow-2024`](papers/virchow-2024/index.md) — **Virchow** (Nat. Med. 2024): ViT-H/14, 632M params, DINOv2 pretraining on ~1.5M H&E WSIs; specimen-AUC 0.95 across 9 common + 7 rare cancers. A frozen feature backbone (weights are gated; verify the license before commercial use).
- [`uni2-h-model`](papers/uni2-h-model/index.md) — **UNI2-h** (MahmoodLab, HF): a pathology foundation model, one-line `timm` load, drop-in patch embeddings.
- [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md) — a **generative multimodal histopathology foundation model** (arXiv 2604) that brings generation into pathology FMs, resonating with stage-2 generative virtual tissue.

---

## Cross-cutting — Data & applications

- [`hest1k-2024`](papers/hest1k-2024/index.md) — **HEST-1k**, a large paired **histology↔spatial-transcriptomics** dataset (>1,200 profiles / 26 organs) + HEST-Benchmark. It aligns H&E morphology with molecular expression — the **shared data substrate** for stage 1 (anomaly labeling) and stage 2 (image→molecule); lacks perturbation/revert data (pair with Perturb-seq). CC BY-NC-SA 4.0.
- [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/index.md), [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md), [`pathomics-repo`](papers/pathomics-repo/index.md) — **Pathomics applications**: a gastric-cancer prognosis/response signature (3,138 patients, MS-GMIL), bone-marrow microenvironment cell quantification (ASH 2023 abstract), and multimodal pathology+omics survival prediction (PathOmics, MICCAI 2023). They exemplify the image→molecule→clinic chain.

---

## Synthesis & gaps

1. **Mature components exist per stage but are not yet a closed loop.** Anomaly detection (STANDS / AnoPILaD / NEJM-AI), virtual tissue (VirTues), and perturbation-revert (MintFlow / Monge-Gap) are independent; **the opportunity is an end-to-end detect → model → revert pipeline.**
2. **"Reconstruct back to normal" recurs** (AnoPILaD's diffusion, PathPrism's counterfactuals, MintFlow's in-silico deletion, VirTues' MAE residual) — it unifies anomaly detection and reversion and is worth adopting as the methodological spine.
3. **Modality bridging hinges on data.** HEST-1k offers H&E↔ST pairs but **no perturbation labels**; it must be joined with single-cell perturbation data (VCC / Perturb-seq) to train spatial-scale reversion.
4. **Foundation models are a free head start.** Virchow / UNI2 / the generative FM serve as feature backbones, saving pretraining from scratch.
5. **The anomaly-detection paradigm is unsettled.** Clinical imaging is mostly **supervised** (CT–LVEF, ECG) while histology favours **un-/self-supervised OOD**; this direction should commit to the latter to handle *unknown* anomalies.

**Suggested next steps.** (a) Use VirTues/MintFlow as the stage-2 skeleton and drive stage 1 from their reconstruction residuals; (b) prototype "anomaly residual → perturbation prediction" on HEST-1k + VCC; (c) use AnoPILaD/PathPrism counterfactuals for image-domain visual validation; (d) enter the Virtual Cell Challenge for a common benchmark.

---

## Citations
All BibTeX in [`references.bib`](references.bib); inter-paper links in [`relationships`](relationships.md).
