<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# A Unifying Review of Deep and Shallow Anomaly Detection

- **Authors:** Lukas Ruff; Jacob R. Kauffmann; Robert A. Vandermeulen; Grégoire Montavon; Wojciech Samek; Marius Kloft; Thomas G. Dietterich; Klaus-Robert Müller
- **Venue / Year:** Proceedings of the IEEE · 2021
- **DOI:** 10.1109/JPROC.2021.3052449
- **URL:** https://doi.org/10.1109/JPROC.2021.3052449
- **arXiv:** https://arxiv.org/abs/2009.11732
- **arXiv version used:** v3 (8 Feb 2021)
- **Bibkey:** Ruff2020_200911732
- **Status:** complete

## Abstract
Deep learning approaches to anomaly detection have recently improved the state of the art in detection performance on complex datasets such as large collections of images or text. These results have sparked a renewed interest in the anomaly detection problem and led to the introduction of a great variety of new methods. With the emergence of numerous such methods, including approaches based on generative models, one-class classification, and reconstruction, there is a growing need to bring methods of this field into a systematic and unified perspective. In this review we aim to identify the common underlying principles as well as the assumptions that are often made implicitly by various methods. In particular, we draw connections between classic 'shallow' and novel deep approaches and show how this relation might cross-fertilize or extend both directions. We further provide an empirical assessment of major existing methods that is enriched by the use of recent explainability techniques, and present specific worked-through examples together with practical advice. Finally, we outline critical open challenges and identify specific paths for future research in anomaly detection.

## Full text / Extract
> Source: open arXiv v3 (2009.11732), corresponding to Proc. IEEE 109(5):756–795. Structured extract of definitions, the unifying view, benchmark results and worked examples; the ~40-page survey text is not reproduced in full.

### Definitions
- "An anomaly is an observation that deviates considerably from some concept of normality." Normality = ground-truth law P⁺ with pdf p⁺; anomaly set A = {x ∈ X | p⁺(x) ≤ τ}.
- **Concentration assumption**: high-density regions of normal data are concentrated, anomalies are not; AD is framed as density level-set estimation at level α; anomaly scores rank, thresholds set false-alarm rates.
- **Anomaly types**: point; conditional/contextual (p⁺(x | t) over time, space, graph); group/collective; low-level sensory vs high-level semantic.
- **Data settings**: unsupervised with noise ε and contamination P = (1−η)P⁺ + ηP⁻; semi-supervised (few labelled normals/anomalies, labels often requiring experts such as pathologists); supervised. KDE and OC-SVM implicitly assume a uniform anomaly distribution P⁻.

### Three families (Sections III–V) plus distance-based (VI-C)
- Probabilistic: Gaussian/Mahalanobis, GMM, KDE, energy-based models, VAEs, GANs (AnoGAN: convex combination of reconstruction loss and intermediate-discriminator-feature loss; later GAN adaptations add explicit encoders, e.g. f-AnoGAN), normalizing flows. Full density estimation arguably violates Vapnik's principle.
- One-class classification: OC-SVM, SVDD, Deep SVDD and variants; negative examples — artificial, auxiliary (Outlier Exposure) and true anomalies, in increasing informativeness.
- Reconstruction: PCA, kernel PCA, autoencoders, prototypical clustering.
- Distance-based (lazy) methods: kNN, LOF, Isolation Forest.

### Unifying view (Section VI)
Five modelling dimensions: D1 Loss ℓ(s,y); D2 Model f_θ(x); D3 Feature map φ(x) (input, kernel, neural network); D4 Regularization R(f,φ,θ); D5 Inference mode (frequentist or Bayesian). General objective: min_θ (1/n) Σ ℓ(f_θ(x_i), y_i) + R(f, φ, θ). Comparative points: probabilistic and reconstruction scores rank inliers; one-class methods usually do not, but are "generally more sample-efficient and more robust to non-representative sampling of the normal data". Kernel SVDD and Deep SVDD share the hypersphere model, enabling transfer of semi-supervised and multi-sphere extensions; reconstruction error in a neural feature space is suggested by analogy with kernel PCA.

### Benchmark (Section VII-C, Table V — AUC on MVTec-AD)

| Class | Gaussian | MVE | PCA | KDE | SVDD | kPCA | AGAN | DOCC | AE |
|---|---|---|---|---|---|---|---|---|---|
| carpet | 48.8 | 63.5 | 45.6 | 34.8 | 48.7 | 41.9 | 83.1 | 90.6 | 36.8 |
| grid | 60.6 | 67.8 | 81.8 | 71.7 | 80.4 | 76.7 | 91.7 | 52.4 | 74.6 |
| leather | 39.6 | 49.5 | 60.3 | 41.5 | 57.3 | 61.1 | 58.6 | 78.3 | 64.0 |
| tile | 68.5 | 79.7 | 56.4 | 68.9 | 73.3 | 63.2 | 74.1 | 96.5 | 51.8 |
| wood | 54.0 | 80.1 | 90.4 | 94.7 | 94.1 | 90.6 | 74.5 | 91.6 | 88.5 |
| bottle | 78.9 | 67.0 | 97.4 | 83.3 | 89.3 | 96.3 | 90.6 | 99.6 | 95.0 |
| cable | 56.5 | 71.9 | 77.6 | 66.9 | 73.1 | 75.6 | 69.7 | 90.9 | 57.3 |
| capsule | 71.6 | 65.1 | 75.7 | 56.2 | 61.3 | 71.5 | 60.7 | 91.0 | 52.5 |
| hazelnut | 67.6 | 80.4 | 89.1 | 69.9 | 74.3 | 83.8 | 96.4 | 95.0 | 90.5 |
| metal nut | 54.7 | 45.1 | 56.4 | 33.3 | 54.3 | 59.0 | 79.3 | 85.2 | 45.5 |
| pill | 65.5 | 71.5 | 82.5 | 69.1 | 76.2 | 80.7 | 64.6 | 80.4 | 76.0 |
| screw | 53.5 | 35.5 | 67.9 | 36.9 | 8.6 | 46.7 | 99.6 | 86.9 | 77.9 |
| toothbrush | 93.9 | 76.1 | 98.3 | 93.3 | 96.1 | 98.3 | 70.8 | 96.4 | 49.4 |
| transistor | 70.2 | 64.8 | 81.8 | 72.4 | 74.8 | 80.0 | 78.8 | 90.8 | 51.2 |
| zipper | 50.1 | 65.2 | 82.8 | 61.4 | 68.6 | 81.0 | 69.7 | 92.4 | 35.0 |

"A first striking observation is the heterogeneity in performance of the various methods on the different corruptions and defect classes." AGAN performs generally well on MNIST-C but is systematically outperformed by DOCC on MVTec-AD. DOCC = whitened representations after the first fully connected layer of a pre-trained VGG16 (MVTec-AD) or an EMNIST-letters CNN (MNIST-C).

### Worked example 1 — Thyroid (Section VIII-A)
ODDS Thyroid: n = 3,772, D = 6, 93 anomalies (~2.5%), 60:10:30 split. OC-SVM with RBF kernel, ν = 0.15 chosen from risk considerations and robustness to contamination. Without feature scaling, best validation AUC 83.9% at γ = (2⁻⁵D)⁻¹. After robust scaling (median and IQR, training statistics only): validation AUC 98.6% at γ = (2²D)⁻¹; test AUC 99.2%, false-alarm rate 14.8%, miss rate zero. Recommendations: assess risks of false alarms and missed anomalies; apply feature scaling; apply XAI to analyse predictions.

### Worked example 2 — MVTec 'wood' and Clever Hans (Section VIII-B)
KDE is the best of nine models on 'wood' (AUC 94.7). LRP/neuralization explanations show KDE attends to vertical wood stripes rather than the liquid-stain defect — a "Clever Hans" effect from a spurious correlation. Remedies: data extension, model extension, ensembles. Replacing the Gaussian kernel by a Mahalanobis kernel (horizontal blur) raises the mean cosine similarity of explanations to ground truth from 0.34 to 0.38, and AUC drops to 87%, "a more realistic estimate of the generalization abilities of the KDE model".

### Outlook (Section IX)
Unexplored combinations of modelling dimensions; bridging AD with OOD detection, calibration, uncertainty estimation and adversarial robustness ("the OOD problem reduces to determining whether x lies outside regions of high density in P⁺, which is exactly the anomaly detection problem"); interpretability and trustworthiness; the need for challenging and open datasets (MVTec-AD and the Medical Out-of-Distribution Analysis Challenge cited as examples; repurposed classification datasets criticised); weak supervision and self-supervised learning; foundation and theory.
