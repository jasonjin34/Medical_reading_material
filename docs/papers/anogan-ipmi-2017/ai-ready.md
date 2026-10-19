<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery

- **Authors:** Thomas Schlegl; Philipp Seeböck; Sebastian M. Waldstein; Ursula Schmidt-Erfurth; Georg Langs
- **Venue / Year:** Information Processing in Medical Imaging (IPMI 2017), LNCS 10265 · 2017
- **DOI:** 10.1007/978-3-319-59050-9_12
- **URL:** https://arxiv.org/abs/1703.05921
- **arXiv:** https://arxiv.org/abs/1703.05921
- **Code (successor, includes iterative z-mapping):** https://github.com/tSchlegl/f-AnoGAN
- **Bibkey:** Schlegl2017_170305921
- **Status:** complete

## Abstract
Obtaining models that capture imaging markers relevant for disease progression and treatment monitoring is challenging. Models are typically based on large amounts of data with annotated examples of known markers aiming at automating detection. High annotation effort and the limitation to a vocabulary of known markers limit the power of such approaches. Here, we perform unsupervised learning to identify anomalies in imaging data as candidates for markers. We propose AnoGAN, a deep convolutional generative adversarial network to learn a manifold of normal anatomical variability, accompanying a novel anomaly scoring scheme based on the mapping from image space to a latent space. Applied to new data, the model labels anomalies, and scores image patches indicating their fit into the learned distribution. Results on optical coherence tomography images of the retina demonstrate that the approach correctly identifies anomalous images, such as images containing retinal fluid or hyperreflective foci.

## Full text / Extract
> Source: open arXiv preprint v1 (1703.05921, "To be published in the proceedings of IPMI 2017"). Structured extract of the key method and result passages; equations given in plain text; numbers copied from Table 1.

### Setting
Given M healthy images I_m, K 2D patches x_{k,m} of size c×c are extracted at random positions; a GAN is trained on these normal patches only to learn the manifold X of normal anatomical variability. At test time unseen patches y_n with binary image-wise labels l_n (used only for evaluation) are scored.

### Method
- **Generative model of normal appearance.** A DCGAN: generator G maps uniformly distributed latent z to images (convolutional decoder of strided convolutions); discriminator D is a standard CNN. Trained with the usual minimax value function V(D,G).
- **Mapping new images to latent space.** GANs give no inverse mapping. For a query image x, start from a random z_1 and update z by backpropagation for Γ steps (G and D fixed) to minimise L(z_γ) = (1−λ)·L_R(z_γ) + λ·L_D(z_γ).
  - Residual loss: L_R(z_γ) = Σ |x − G(z_γ)| (visual dissimilarity).
  - Discrimination loss (proposed, inspired by feature matching): L_D(z_γ) = Σ |f(x) − f(G(z_γ))|, where f is an intermediate discriminator layer — "our approach utilizes the trained discriminator not as classifier but as a feature extractor." A reference variant following Yeh et al. (sigmoid cross-entropy of D(G(z)) against target 1) is evaluated as GAN_R.
- **Anomaly score.** A(x) = (1−λ)·R(x) + λ·D(x), with R and D the residual and discrimination losses at the final iteration Γ. The residual image x_R = |x − G(z_Γ)| identifies anomalous regions.
- **Implementation.** Four fractionally-strided conv layers in G, four conv layers in D, 5×5 filters, channels 512-256-128-64; 20 epochs with Adam; 500 backpropagation steps for latent mapping; λ = 0.1 (chosen on a face dataset). Adapted from bamos/dcgan-completion.tensorflow; TensorFlow, Titan X.

### Data
Clinical SD-OCT retinal volumes, 49 B-scans per volume, 496×512×49 voxels. Training: patches from 270 healthy volumes without fluid. Preprocessing: grey values normalised to [−1, 1]; resized to 22 µm in x (≈256 columns); retina extracted and flattened via layer segmentation. 1,000,000 training patches of 64×64 pixels. Test: 10 healthy and 10 fluid cases, 8,192 patches; voxel-wise expert fluid annotations used only for evaluation; a patch is positive if it contains at least one fluid pixel.

### Key results (Table 1, statistics at the Youden index)

| Model | Precision | Recall | Sensitivity | Specificity | AUC |
|---|---|---|---|---|---|
| aCAE | 0.7005 | 0.7009 | 0.7011 | 0.6659 | 0.73 |
| P_D (DCGAN discriminator output) | 0.8471 | 0.5119 | 0.5124 | 0.8970 | 0.72 |
| GAN_R | 0.8482 | 0.7631 | 0.7634 | 0.8477 | 0.88 |
| AnoGAN | 0.8834 | 0.7277 | 0.7279 | 0.8928 | 0.89 |

- The proposed discrimination score D(x) outperforms the reference D̂(x); overall AUC of AnoGAN and GAN_R is comparable, attributed to the strong residual score R(x).
- aCAEs "tend to over-adapt on anomalous images".
- Residual maps agree with pixel-level fluid annotations; the model additionally identifies hyperreflective foci (HRF), which were not annotated.

### Authors' conclusion and caveat
"While quantitative evaluation based on a subset of anomaly classes is limited, since false positives do not take novel anomalies into account, results demonstrate good sensitivity and the capability to segment anomalies."
