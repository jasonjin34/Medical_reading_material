<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks

- **Authors:** Schlegl, Thomas; Seeböck, Philipp; Waldstein, Sebastian M.; Langs, Georg; Schmidt-Erfurth, Ursula
- **Venue / Year:** Medical Image Analysis · 2019
- **DOI:** 10.1016/j.media.2019.01.010
- **URL:** https://doi.org/10.1016/j.media.2019.01.010
- **Code:** https://github.com/tSchlegl/f-AnoGAN
- **Open copy:** accepted manuscript (CC-BY-NC-ND 4.0) in the code repo, paper/f-AnoGAN.pdf
- **Bibkey:** Schlegl_2019
- **Status:** complete

## Abstract
Obtaining expert labels in clinical imaging is difficult since exhaustive annotation is time‐consuming. Furthermore, not all possibly relevant markers may be known and sufficiently well described a priori to even guide annotation. While supervised learning yields good results if expert labeled training data is available, the visual variability, and thus the vocabulary of findings, we can detect and exploit, is limited to the annotated lesions. Here, we present fast AnoGAN (f‐AnoGAN), a generative adversarial network (GAN) based unsupervised learning approach capable of identifying anomalous images and image segments, that can serve as imaging biomarker candidates. We build a generative model of healthy training data, and propose and evaluate a fast mapping technique of new data to the GAN's latent space. The mapping is based on a trained encoder, and anomalies are detected via a combined anomaly score based on the building blocks of the trained model – comprising a discriminator feature residual error and an image reconstruction error. In the experiments on optical coherence tomography data, we compare the proposed method with alternative approaches, and provide comprehensive empirical evidence that f‐AnoGAN outperforms alternative approaches and yields high anomaly detection accuracy. In addition, a visual Turing test with two retina experts showed that the generated images are indistinguishable from real normal retinal OCT images. The f‐AnoGAN code is available at https://github.com/tSchlegl/f‐AnoGAN.

## Full text / Extract
> Source: the authors' accepted manuscript (CC-BY-NC-ND 4.0) distributed in the official code repository; publisher version is paywalled. Structured extract; numbers copied from Tables 1–2 and the text.

### Contribution (as stated)
Fast anomaly detection based on GAN training on normal image appearance, followed by an encoder training step enabling single-step mapping from images to latent space. Differences from AnoGAN: (1) improved WGAN (WGAN-GP) instead of DCGAN; (2) a learned mapping replaces iterative gradient descent; (3) a broader experimental comparison.

### Encoder training variants (G and D frozen)
- **ziz** (z → image → z): L_ziz(z) = (1/d)·‖z − E(G(z))‖²; resembles the "latent regressor" of Donahue et al.; the encoder never sees real images.
- **izi** (image → z → image): L_izi(x) = (1/n)·‖x − G(E(x))‖²; trained on normal images only.
- **izi_f** (proposed): L_izif(x) = (1/n)·‖x − G(E(x))‖² + (κ/n_d)·‖f(x) − f(G(E(x)))‖², f = intermediate discriminator features. Rationale: minimising pixel residuals alone can map into sparsely sampled latent regions and yield unrealistic reconstructions with small residuals even for anomalous images.

### Anomaly score
A(x) = A_R(x) + κ·A_D(x), A_R = (1/n)‖x − G(E(x))‖², A_D = (1/n_d)‖f(x) − f(G(E(x)))‖²; pixel-level localisation from |x − G(E(x))|. For izi and ziz the score reduces to A_R. Discriminator-only baseline: A_D = |m̂ − D(x_u)|, m̂ = mean D output over 32,000 training images.

### Implementation
WGAN-GP, 128-d normal latent; ResNet generator and discriminator with four residual blocks each (G 512-256-128-64, D 128-256-512-512 filters; 3×3; layer norm in D); 100,000 WGAN iterations, batch 64, 5 D updates per G update (Adam); 50,000 encoder iterations (RMSprop); κ = 1.0; encoder outputs passed through tanh to restrict to (−1σ, +1σ). Python 2.7, TensorFlow 1.2, Titan X.

### Data
Same SD-OCT data as AnoGAN (Heidelberg Spectralis; 49 B-scans; 496×512×49). Per-volume normalisation to [−1,1], 512→256 columns (22 µm), retina extraction and flattening. ≈850,000 training patches (64×64) from 270 healthy volumes; test set of 10 healthy + 10 fluid volumes, 70,000 patches (70% normal / 30% fluid), pixel-level expert fluid annotations for evaluation only.

### Key results
**Table 1 — image-level detection (Youden index)**

| Model | Precision | Sensitivity | Specificity | F-score | AUC |
|---|---|---|---|---|---|
| AE | 0.6824 | 0.7195 | 0.8550 | 0.7005 | 0.8688 |
| AdvAE | 0.6405 | 0.7856 | 0.8092 | 0.7057 | 0.8649 |
| ALI | 0.5063 | 0.7434 | 0.6863 | 0.6023 | 0.7897 |
| A_D | 0.4909 | 0.6831 | 0.6931 | 0.5713 | 0.7504 |
| iterative | 0.7202 | 0.8049 | 0.8645 | 0.7602 | 0.9114 |
| f-AnoGAN | 0.7863 | 0.8091 | 0.9049 | 0.7975 | 0.9301 |

**Table 2 — encoder training (same WGAN)**

| Encoder | Precision | Sensitivity | Specificity | F-score | AUC |
|---|---|---|---|---|---|
| ziz | 0.7047 | 0.8146 | 0.8522 | 0.7557 | 0.9066 |
| izi | 0.7018 | 0.7497 | 0.8621 | 0.7250 | 0.8874 |
| izi_f | 0.7863 | 0.8091 | 0.9049 | 0.7975 | 0.9301 |

- With the full f-AnoGAN score applied after izi / ziz training: izi F-score 0.7328, AUC 0.8976; ziz F-score 0.7830, AUC 0.9209 — still below izi_f.
- Runtime: iterative mapping with 300 updates for each of 70,000 test images took 2 days on a Titan X; f-AnoGAN took 20 seconds.
- Pixel-level fluid "segmentation": sensitivity 0.69, specificity 0.75, AUC 0.78 ("only a coarse indication").
- Visual Turing test (50 real + 50 generated normal patches, two retina experts): mean accuracy 0.44, inter-rater consensus 0.58.

### Limitations / scope (as stated)
Annotations cover only part of possible anomalies, so false-positive estimates are unreliable. Clinical OCT diagnosis is not performed at 64×64 scale. The method applies "whenever large amounts of normal medical (imaging) data are available for GAN training and the test distribution equals the training distribution"; main use is normal/anomalous distinction plus coarse localisation as region proposals for expert review.
