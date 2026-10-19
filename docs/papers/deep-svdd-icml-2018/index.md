# Deep One-Class Classification

> **Bibkey** `Ruff_2018` · **Venue** International Conference on Machine Learning (ICML 2018), PMLR 80 (2018) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://proceedings.mlr.press/v80/ruff18a.html> · `status: complete`

---

## One-liner
Deep SVDD is, per the authors, the first deep method trained **directly on an anomaly-detection objective**: a network φ is trained so that normal data's representations fall into a minimum-volume hypersphere around a fixed centre c, and the test-time anomaly score is ‖φ(x) − c‖². The paper also proves which design choices cause "hypersphere collapse" (bias terms, bounded activations, a learnable centre) and the ν-property of the soft-boundary variant.

## Problem
Classical methods (OC-SVM, KDE) fail on high-dimensional, data-rich problems due to poor scalability and the curse of dimensionality, and need heavy feature engineering; kernel methods scale at least quadratically and must store support vectors. Deep AD at the time (autoencoders, AnoGAN, etc.) was **trained for another task** (generation or compression) and scored with heuristics such as reconstruction error — not an AD objective; autoencoders also need a compression level that is hard to choose without supervision. The question: can one define a **minimum-volume** AD objective like SVDD, but with features learned end-to-end by a deep network?

## Method
**Objectives** (network φ: X → F with weights W): **soft-boundary Deep SVDD** — min R² + (1/νn)·Σ max{0, ‖φ(xᵢ;W) − c‖² − R²} + (λ/2)·Σ‖W^ℓ‖²_F, with ν ∈ (0,1] trading sphere volume against boundary violations; **One-Class Deep SVDD** (assuming the training data are mostly normal) — min (1/n)·Σ‖φ(xᵢ;W) − c‖² + weight decay, i.e. shrink the mean distance of all representations to c. Anomaly score s(x) = ‖φ(x;W*) − c‖² (soft-boundary: optionally minus R*²). Inference is a forward pass and **stores no training data**. **Optimisation**: SGD/Adam; for soft-boundary, alternate between W and R (solve R by line search every k=5 epochs). **Anti-collapse theory**: Proposition 1 — if c is a free variable, all-zero weights with R=0 is optimal, so c must be fixed and differ from the all-zero-weights output (in practice the mean of an initial forward pass); Proposition 2 — any hidden-layer **bias term** lets the net learn a constant map, so all biases are removed; Proposition 3 — **bounded activations** (e.g. sigmoid) can be saturated to emulate a bias, so unbounded ones (ReLU / leaky ReLU) are preferred; Proposition 4 — in soft-boundary Deep SVDD, ν upper-bounds the fraction of outliers and lower-bounds the fraction on or outside the boundary (ν-property). **Details**: LeNet-type CNNs initialised from a trained convolutional autoencoder (DCAE) encoder (pre-training), BatchNorm, leaky ReLU (α=0.1), two-phase learning rate 10⁻⁴ → 10⁻⁵ (150+100 epochs), λ=10⁻⁶.

## Method lineage
**Paradigm: density / one-class.** It lifts Tax & Duin's kernel SVDD (minimum enclosing hypersphere) and Schölkopf et al.'s OC-SVM / ν-property onto deep features. The authors split prior work into "mixed" (learn a representation, then a shallow detector, e.g. DBN + OC-SVM) and "fully deep" (reconstruction error directly); Deep SVDD is fully deep and its objective is AD itself. It led to Deep SAD (semi-supervised, using a few labelled anomalies), multi-sphere extensions and Patch SVDD (one of MEATRD's image baselines); the 2021 unifying review by Ruff et al. lists it next to kernel SVDD as the same "hypersphere model" to show how improvements transfer between shallow and deep methods. "One-class on frozen/learned features" in pathology and spatial omics (BI's center-loss + OC-SVM, MEATRD's Deep-SVDD-style scoring) descends from this line.

## Data
**One-class MNIST and CIFAR-10**: one class is normal and the other nine are anomalies; train on that class's training samples only (≈6,000 for MNIST, 5,000 for CIFAR-10), compute AUC on the standard 10,000-image test set; preprocessing is L1 global contrast normalisation + min-max scaling. **GTSRB stop-sign adversarial detection**: 780 normal stop signs for training; test 270 normal + 20 Boundary-Attack adversarial examples; 10% border cropped, resized to 32×32. Comparators: OC-SVM/SVDD (Gaussian kernel, γ grid-searched on a small hold-out of 10% of test samples — which the authors note gives shallow SVDD a small supervised advantage), KDE, Isolation Forest (all three after PCA keeping 95% variance), DCAE and AnoGAN. Results are averaged over 10 seeds.

## Key results
**MNIST (Table 1)**: One-Class Deep SVDD is best on 8 of 10 classes, tied with OC-SVM on class 4 (94.9), and below OC-SVM only on class 0 (98.0 vs 98.6); e.g. class 2: 91.7±0.8 (OC-SVM 82.5, IF 88.6, DCAE 85.4, AnoGAN 85.0); class 8: 93.9±1.6 (OC-SVM 88.9). **CIFAR-10**: "mixed" — Deep SVDD is best on AUTOMOBILE 65.9, CAT 59.1, DOG 65.7, HORSE 67.3; but on DEER (KDE 66.2 vs 60.9), FROG (KDE 74.9 vs 67.7) and TRUCK (KDE 76.0 vs 73.1) **shallow KDE / SVDD win**, AnoGAN is best on AIRPLANE (67.1) and BIRD (52.9), and DCAE on SHIP (76.8). The authors' explanation: these classes have strong **global structure** (e.g. trucks split horizontally into road and sky), for which local CNN features may be ill-suited — architecture choice matters. The one-class variant slightly beats soft-boundary on both datasets (the training data really are anomaly-free). **GTSRB (Table 2)**: One-Class Deep SVDD is best at **80.3±2.8**, then DCAE 79.1, soft-boundary 77.8, IF 73.8, OC-SVM 67.5, KDE 60.5; **AnoGAN's DCGAN did not converge on so little data**, so it has no result. Deep methods show larger standard deviations (SGD randomness).

## Contributions
- The first fully deep one-class objective: representation learning jointly optimised with a minimum-volume hypersphere.
- A systematic account of "hypersphere collapse" (free centre, bias terms, bounded activations) with design rules — still the checklist for any "compress the normal" method.
- Proves the ν-property for soft-boundary Deep SVDD, letting a prior on training-set contamination enter the model.
- The model is fully characterised by its weights — no stored training data, low memory and fast inference.

## Limitations
- Evaluated only on classification datasets repurposed as one-class tasks (MNIST / CIFAR-10 / GTSRB), where anomalies are "other classes" — far from subtle real-world anomalies (a habit the 2021 Ruff et al. review itself criticises).
- Not consistently better than shallow methods on CIFAR-10; sensitive to architecture, with larger SGD-induced variance.
- Anti-collapse requires removing biases, fixing the centre and DCAE pre-training — representation quality depends heavily on pre-training; a single hypersphere models one "normal mode" and fits multi-modal normal distributions (many cell types) poorly.
- Gives sample-level scores only — no localisation or explanation.

## Relation to our direction
Deep SVDD gives the **detect** stage its cleanest scoring form — "normal = compact region, anomaly = distance to centre" — and maps one-to-one onto Plan A's most likely workhorse: **one-class scoring on frozen foundation-model embeddings**. **Mapping to kidney omics**: samples = snRNA cells, Xenium cells, Visium spots or H&E patches; "normal training set" = KPMP/HuBMAP healthy references; φ = a small network on top of scVI latents or H&E foundation-model embeddings; anomaly score = distance to the "normal centre". **Which assumptions break**: (1) **one sphere vs many cell types**: normal kidney already contains dozens of states (PT, TAL, podocytes, endothelium, immune…), so a single centre c will flag "rare but normal" cell types; one sphere **per cell type**, or a multi-centre / conditional variant, is required (complementing healthy-ref's "learn the latent on a healthy atlas, then compare against matched controls"). (2) **batch effects**: a new batch's global shift moves away from c — reference mapping and a MapQC-style inter-sample null are needed first. (3) **contamination**: "healthy" donor tissue also contains doublets, ambient-dominated cells and Xenium segmentation/spillover errors (see xenium-split, ovrlpy); the soft-boundary ν can encode a prior on "what fraction of the training set is artifact", making it a better fit for kidney data than the one-class variant. (4) **continuous disease states**: ‖φ(x) − c‖² is continuous with no definition of where "anomalous" starts — conformal calibration (conformal-scrna) turns scores into p-values with FPR guarantees. (5) **no gold standard**: unlike the paper's "other class = anomaly", kidney data have no ready labels; KidneyAnomalyBench's expert adjudication is a precondition for evaluation. **Cross-modal agreement**: build one sphere on H&E embeddings and one on expression embeddings of the same tissue; both distances large → disease candidate, only one large → artifact candidate (e.g. segmentation errors only on the expression side, staining/folds only on the image side). **Existing repo adaptations**: MEATRD (meatrd-aaai-2025) trains a Deep-SVDD-style one-class classifier on latent multimodal reconstruction errors and scores by distance to a centre c; BI's histo-anomaly-bi-repo fits a one-class SVM (shallow SVDD's sibling) on center-loss-trained CNN features; histo-nejmai-2024 compares kNN and one-class fine-tuning on foundation-model features and lists Deep SVDD as a follow-up for spatial omics; MedIAnomaly finds "frozen ImageNet ResNet + one-class classifier" lands top-3 on nearly every dataset — supporting "frozen foundation-model embeddings + one-class scoring" as Plan A's default strong baseline.

## Reusable assets
- **Code:** the authors' Deep SVDD implementation (address given in the paper).
<https://github.com/lukasruff/DeepSVDD>
- **Design checklist:** fixed centre (initial forward-pass mean), no biases, unbounded activations, autoencoder pre-training — check each for any kidney model that "compresses normal embeddings".
- **Eval protocol:** one-class setups with mean ± SD over 10 seeds; KDE / IF / OC-SVM (on 95%-variance PCA) as mandatory shallow baselines.

## Follow-ups
- Deep SAD (Ruff et al., ICLR 2020): the semi-supervised extension with a few labelled anomalies — relevant to the handful of expert-confirmed cases in KidneyAnomalyBench.
- Patch SVDD (Yi & Yoon, ACCV 2020): patch-level SVDD, an image baseline in MEATRD.
- The 2021 Ruff et al. unifying review (ad-unifying-review-procieee-2021 in this repo).

## Cite
```bibtex
@inproceedings{Ruff_2018,
  title = {Deep One-Class Classification},
  author = {Ruff, Lukas and Vandermeulen, Robert A. and G{\"o}rnitz, Nico and Deecke, Lucas and Siddiqui, Shoaib A. and Binder, Alexander and M{\"u}ller, Emmanuel and Kloft, Marius},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
  series = {Proceedings of Machine Learning Research},
  volume = {80},
  pages = {4393--4402},
  publisher = {PMLR},
  year = {2018},
  url = {https://proceedings.mlr.press/v80/ruff18a.html}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
