<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Deep One-Class Classification

- **Authors:** Ruff, Lukas; Vandermeulen, Robert A.; Görnitz, Nico; Deecke, Lucas; Siddiqui, Shoaib A.; Binder, Alexander; Müller, Emmanuel; Kloft, Marius
- **Venue / Year:** International Conference on Machine Learning (ICML 2018), PMLR 80 · 2018
- **DOI:** 
- **URL:** https://proceedings.mlr.press/v80/ruff18a.html
- **Code:** https://github.com/lukasruff/DeepSVDD
- **PDF:** https://proceedings.mlr.press/v80/ruff18a/ruff18a.pdf
- **Bibkey:** Ruff_2018
- **Status:** complete

## Abstract
Despite the great advances made by deep learning in many machine learning problems, there is a relative dearth of deep learning approaches for anomaly detection. Those approaches which do exist involve networks trained to perform a task other than anomaly detection, namely generative models or compression, which are in turn adapted for use in anomaly detection; they are not trained on an anomaly detection based objective. In this paper we introduce a new anomaly detection method—Deep Support Vector Data Description—, which is trained on an anomaly detection based objective. The adaptation to the deep regime necessitates that our neural network and training procedure satisfy certain properties, which we demonstrate theoretically. We show the effectiveness of our method on MNIST and CIFAR-10 image benchmark datasets as well as on the detection of adversarial examples of GTSRB stop signs.

## Full text / Extract
> Source: open PMLR proceedings PDF (ICML 2018, PMLR 80:4393–4402). Structured extract; numbers copied from Tables 1–2.

### Objectives
Network φ(·;W): X → F with L hidden layers; hypersphere centre c and radius R.
- **Soft-boundary Deep SVDD:** min_{R,W} R² + (1/(νn)) Σ_i max{0, ‖φ(x_i;W) − c‖² − R²} + (λ/2) Σ_ℓ ‖W^ℓ‖²_F, ν ∈ (0,1].
- **One-Class Deep SVDD** (most training data normal): min_W (1/n) Σ_i ‖φ(x_i;W) − c‖² + (λ/2) Σ_ℓ ‖W^ℓ‖²_F.
- **Anomaly score:** s(x) = ‖φ(x;W*) − c‖² (soft-boundary: optionally minus R*²). W* (and R*) fully characterise the model; no data must be stored for prediction.
- **Optimisation:** SGD/Adam with backpropagation; for soft-boundary, alternate W (k epochs, R fixed) and R (line search) — k = 5.

### Properties (hypersphere collapse)
- Proposition 1: with c free (or c equal to the all-zero-weights output c₀), W* = W₀, R* = 0 is optimal → fix c ≠ c₀; in practice the mean of network outputs from an initial forward pass.
- Proposition 2: any hidden-layer bias term permits a constant mapping to c → use no bias terms.
- Proposition 3: bounded activations can be saturated to emulate a bias → prefer unbounded activations (ReLU / leaky ReLU).
- Proposition 4 (ν-property): ν is an upper bound on the fraction of outliers and a lower bound on the fraction of samples outside or on the boundary.

### Setup
Shallow baselines: Gaussian-kernel OC-SVM/SVDD (γ grid-searched on a 10% hold-out of test samples, ν ∈ {0.01, 0.1}), KDE (bandwidth by 5-fold CV), Isolation Forest (100 trees, ψ = 256), all after PCA keeping 95% variance. Deep baselines: DCAE (same encoder as Deep SVDD, symmetric decoder, MSE) and AnoGAN (DCGAN, latent dim 256). Deep SVDD: no biases, c = mean of initial forward pass, Adam, BatchNorm, DCAE-encoder pre-training, learning rate 10⁻⁴ then 10⁻⁵ (150 + 100 epochs), leaky ReLU α = 0.1, λ = 10⁻⁶. MNIST: CNN with 8×(5×5) and 4×(5×5) filter modules and a 32-unit dense layer; CIFAR-10: 32/64/128 filter modules and a 128-unit dense layer; batch 200. One class normal, others anomalous; n ≈ 6,000 (MNIST) / 5,000 (CIFAR-10) training images; 10,000 test images; global contrast normalisation (L1) and min-max scaling. AUC averaged over 10 seeds.

### Table 1 — AUC (%) mean ± SD over 10 seeds

| Normal class | OC-SVM/SVDD | KDE | IF | DCAE | AnoGAN | Soft-bound. Deep SVDD | One-class Deep SVDD |
|---|---|---|---|---|---|---|---|
| 0 | 98.6±0.0 | 97.1±0.0 | 98.0±0.3 | 97.6±0.7 | 96.6±1.3 | 97.8±0.7 | 98.0±0.7 |
| 1 | 99.5±0.0 | 98.9±0.0 | 97.3±0.4 | 98.3±0.6 | 99.2±0.6 | 99.6±0.1 | 99.7±0.1 |
| 2 | 82.5±0.1 | 79.0±0.0 | 88.6±0.5 | 85.4±2.4 | 85.0±2.9 | 89.5±1.2 | 91.7±0.8 |
| 3 | 88.1±0.0 | 86.2±0.0 | 89.9±0.4 | 86.7±0.9 | 88.7±2.1 | 90.3±2.1 | 91.9±1.5 |
| 4 | 94.9±0.0 | 87.9±0.0 | 92.7±0.6 | 86.5±2.0 | 89.4±1.3 | 93.8±1.5 | 94.9±0.8 |
| 5 | 77.1±0.0 | 73.8±0.0 | 85.5±0.8 | 78.2±2.7 | 88.3±2.9 | 85.8±2.5 | 88.5±0.9 |
| 6 | 96.5±0.0 | 87.6±0.0 | 95.6±0.3 | 94.6±0.5 | 94.7±2.7 | 98.0±0.4 | 98.3±0.5 |
| 7 | 93.7±0.0 | 91.4±0.0 | 92.0±0.4 | 92.3±1.0 | 93.5±1.8 | 92.7±1.4 | 94.6±0.9 |
| 8 | 88.9±0.0 | 79.2±0.0 | 89.9±0.4 | 86.5±1.6 | 84.9±2.1 | 92.9±1.4 | 93.9±1.6 |
| 9 | 93.1±0.0 | 88.2±0.0 | 93.5±0.3 | 90.4±1.8 | 92.4±1.1 | 94.9±0.6 | 96.5±0.3 |
| airplane | 61.6±0.9 | 61.2±0.0 | 60.1±0.7 | 59.1±5.1 | 67.1±2.5 | 61.7±4.2 | 61.7±4.1 |
| automobile | 63.8±0.6 | 64.0±0.0 | 50.8±0.6 | 57.4±2.9 | 54.7±3.4 | 64.8±1.4 | 65.9±2.1 |
| bird | 50.0±0.5 | 50.1±0.0 | 49.2±0.4 | 48.9±2.4 | 52.9±3.0 | 49.5±1.4 | 50.8±0.8 |
| cat | 55.9±1.3 | 56.4±0.0 | 55.1±0.4 | 58.4±1.2 | 54.5±1.9 | 56.0±1.1 | 59.1±1.4 |
| deer | 66.0±0.7 | 66.2±0.0 | 49.8±0.4 | 54.0±1.3 | 65.1±3.2 | 59.1±1.1 | 60.9±1.1 |
| dog | 62.4±0.8 | 62.4±0.0 | 58.5±0.4 | 62.2±1.8 | 60.3±2.6 | 62.1±2.4 | 65.7±2.5 |
| frog | 74.7±0.3 | 74.9±0.0 | 42.9±0.6 | 51.2±5.2 | 58.5±1.4 | 67.8±2.4 | 67.7±2.6 |
| horse | 62.6±0.6 | 62.6±0.0 | 55.1±0.7 | 58.6±2.9 | 62.5±0.8 | 65.2±1.0 | 67.3±0.9 |
| ship | 74.9±0.4 | 75.1±0.0 | 74.2±0.6 | 76.8±1.4 | 75.8±4.1 | 75.6±1.7 | 75.9±1.2 |
| truck | 75.9±0.3 | 76.0±0.0 | 58.9±0.7 | 67.3±3.0 | 66.5±2.8 | 71.0±1.1 | 73.1±1.2 |

Authors: "Deep SVDD clearly outperforms both its shallow and deep competitors on MNIST. On CIFAR-10 the picture is mixed." Shallow SVDD and KDE beat deep methods on three CIFAR-10 classes whose normal examples have strong global structure (e.g. TRUCK, DEER, FROG). One-Class Deep SVDD slightly beats soft-boundary on both datasets.

### Table 2 — GTSRB stop signs with Boundary-Attack adversarial examples (AUC %, 10 seeds)
Training: 780 normal stop signs; test: 270 normal + 20 adversarial; 10% border cropped, 32×32. OC-SVM/SVDD 67.5±1.2; KDE 60.5±1.7; IF 73.8±0.9; DCAE 79.1±3.0; AnoGAN — (DCGAN did not converge, dataset too small); soft-boundary Deep SVDD 77.8±4.9; One-class Deep SVDD 80.3±2.8.
