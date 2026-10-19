<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Diffusion Models for Medical Anomaly Detection

- **Authors:** Julia Wolleb; Florentin Bieder; Robin Sandkühler; Philippe C. Cattin
- **Venue / Year:** Medical Image Computing and Computer Assisted Intervention (MICCAI 2022), LNCS 13438 · 2022
- **DOI:** 10.1007/978-3-031-16452-1_4
- **URL:** https://arxiv.org/abs/2203.04306
- **arXiv:** https://arxiv.org/abs/2203.04306
- **Code:** https://gitlab.com/cian.unibas.ch/diffusion-anomaly
- **Bibkey:** Wolleb2022_220304306
- **Status:** complete

## Abstract
In medical applications, weakly supervised anomaly detection methods are of great interest, as only image-level annotations are required for training. Current anomaly detection methods mainly rely on generative adversarial networks or autoencoder models. Those models are often complicated to train or have difficulties to preserve fine details in the image. We present a novel weakly supervised anomaly detection method based on denoising diffusion implicit models. We combine the deterministic iterative noising and denoising scheme with classifier guidance for image-to-image translation between diseased and healthy subjects. Our method generates very detailed anomaly maps without the need for a complex training procedure. We evaluate our method on the BRATS2020 dataset for brain tumor detection and the CheXpert dataset for detecting pleural effusions.

## Full text / Extract
> Source: open arXiv preprint v2 (2203.04306, 5 Oct 2022). Structured extract. The paper reports Dice/AUROC only as plots (Fig. 4); no numeric results table exists in the text, so none is reproduced here.

### Setting
Two unpaired training sets — healthy subjects and diseased subjects — with image-level labels only (weak supervision). Goal: pixel-wise anomaly map as the difference between a diseased input and a synthetic healthy version that preserves all non-pathological detail.

### Method
- Train a DDPM (formulation of Ho et al. and Nichol & Dhariwal) on healthy and diseased images: U-Net ε_θ predicts noise, MSE loss; T = 1000 steps.
- Pretrain a binary classifier C on noisy images x_t, t ∈ {1,…,T}.
- DDIM sampling with σ_t = 0 is deterministic and can be viewed as an Euler ODE solver; the reversed ODE encodes an image x_0 into noise x_T, from which x_0 is recovered exactly.
- **Algorithm 1 (noise encoding + classifier guidance).** Input x, healthy label h, gradient scale s, noise level L. Encode x to x_L with the reversed DDIM update for t = 0…L−1. Denoise for t = L…1 with ε̂ = ε_θ(x_t,t) − s·√(1−ᾱ_t)·∇_{x_t} log C(h | x_t, t) and the deterministic DDIM step. Anomaly map a = Σ_channels |x − x_0|.
- "The choice of the noise level L and the gradient scale s is crucial for the trade-off between detail-preserving image reconstruction and freedom for translation to a healthy subject."
- Implementation: trained as in Nichol & Dhariwal without augmentation; hyper-parameters from Dhariwal & Nichol's appendix; Adam, hybrid loss, lr 10⁻⁴, batch 10; 128 channels in the first layer, one attention head at resolution 16; 113,681,160 parameters (diffusion) and 5,452,962 (classifier); 50,000 / 20,000 iterations; ≈ one day on an NVIDIA Quadro RTX 6000; PyTorch 1.7.1.

### Data
- **CheXpert**: training 14,179 healthy controls and 16,776 subjects with pleural effusions; 256×256, normalised to [0,1]; test 200 images per class.
- **BRATS2020**: four MR sequences (T1, T2, FLAIR, T1ce) as channels; axial 2D slices padded to 256×256, normalised to [0,1]; lowest 80 and uppermost 26 slices excluded; slices without tumour in the label mask are healthy. Training 5,598 healthy and 10,607 diseased slices; test 1,082 tumour and 705 tumour-free slices.

### Results (as stated)
- Comparators: Fixed-Point GAN (FP-GAN) and the VAE of Chen & Konukoglu; ablation: random-noise DDPM encoding with classifier-guided DDPM sampling. All experiments use s = 100, L = 500.
- The method "generates realistic looking images and preserves all the details of the input image, which leads to a very detailed anomaly map"; other methods change other parts of the image or fail to find the anomaly; DDPM sampling changes the basic anatomy, whereas DDIM noise encoding reconstructs all details.
- A complete image translation takes about 158 s; smaller L or skipped timesteps speed it up but degrade image quality.
- Hyper-parameter sensitivity (BRATS): average Dice (average Otsu thresholding) and AUROC on diseased test slices plotted versus s for L ∈ {250, 500, 750}, with FP-GAN and VAE as horizontal bars (Fig. 4). Too small s cannot remove the tumour; too large s adds artifacts at the brain border; too large L destroys the image; too small L gives too little freedom.
- Healthy input (Fig. 7): "The difference between the input image and the synthetic image is close to zero."
- Discussion: Meissen et al. criticised reconstruction error as an anomaly score (histogram equalisation can outperform neural networks; reconstruction quality correlates poorly with Dice); likelihood-based scores are left to future work.
