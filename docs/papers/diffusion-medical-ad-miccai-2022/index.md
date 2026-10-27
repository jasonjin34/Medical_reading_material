# Diffusion Models for Medical Anomaly Detection

> **Bibkey** `Wolleb2022_220304306` · **Venue** Medical Image Computing and Computer Assisted Intervention (MICCAI 2022), LNCS 13438 (2022) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2203.04306> · `status: complete`

---

## One-liner
DDIM's **deterministic noising** encodes a patient image to noise level L; denoising with **classifier guidance** then "translates" it to the healthy class, and the difference between input and output is a pixel-level anomaly map — a weakly supervised AD method needing only image-level (healthy/diseased) labels, described by the authors as the first diffusion model for anomaly detection.

## Problem
Pixel-wise annotation in medical imaging is hard to get, often missing and biased by annotators, so weakly supervised AD with only image-level labels is attractive. Existing methods relied on autoencoders (blurry reconstructions that lose detail) or GANs (hard to train, heavy tuning, extra cycle-consistency losses and architecture changes for image translation). The core requirement: **change only the pathological region and preserve everything else**, so that "input − translated image" is a clean anomaly map.

## Method
**Two trained components (both use healthy + diseased images with image-level labels only)**: (1) a class-conditional DDPM following Nichol & Dhariwal (T=1000, hybrid loss, Adam, lr 10⁻⁴, batch 10, 128 channels in the first layer, one attention head at resolution 16; 113,681,160 parameters), 50,000 iterations; (2) a binary classifier C trained on **noisy images** x_t for all t (5,452,962 parameters), 20,000 iterations; about one day on a Quadro RTX 6000. **Inference (Algorithm 1)**: given input x, healthy class h, gradient scale s and noise level L — first run DDIM's **reversed ODE** (deterministic updates with σ_t=0) from t=0 to L to "encode the anatomy in noise"; then denoise from L to 0 with classifier guidance ε̂ = ε_θ(x_t,t) − s·√(1−ᾱ_t)·∇log C(h|x_t,t) to obtain the healthy version x₀; **anomaly map** a = Σ_channels |x − x₀|. Key trade-off: too small an L leaves no freedom to remove the tumour, too large destroys the image; too small an s fails to remove it, too large introduces artifacts at the brain border. All experiments use **L=500, s=100**. Ablation: replace deterministic encoding with DDPM stochastic noising (still sampling with classifier guidance).

## Method lineage
**Paradigm: reconstruction / generative** (more precisely, weakly supervised **conditional translation to healthy**, with a classifier-based component via guidance). It builds on DDPM (Ho et al.), improved DDPM (Nichol & Dhariwal), DDIM (Song et al.: deterministic sampling as an ODE solve, enabling invertible encoding) and Dhariwal & Nichol's classifier guidance; comparators are Fixed-Point GAN (GAN image translation) and Chen & Konukoglu's constrained adversarial autoencoder VAE. Versus AnoGAN / f-AnoGAN: still "project to normal, take the residual", but (a) it needs diseased samples and image-level labels to train the classifier — no longer "normal-only"; (b) deterministic DDIM encoding preserves detail, replacing GAN latent search or an encoder. Together with the same-year AnoDDPM (purely unsupervised, partial noising, simplex noise) it opened diffusion-based AD; in this repo AnoPILaD (histo-miccai-2025, following AnoDDPM's partial noising plus text conditioning) and MoPaDi (counterfactual-diffusion-cancerres-2026, a diffusion autoencoder plus classifier directions for counterfactuals) sit in the same "diffusion + conditioning → normal/counterfactual version" lineage, though neither states it builds on this paper.

## Data
**CheXpert** (chest X-ray, pleural effusion): training 14,179 healthy controls + 16,776 effusion patients, 256×256, normalised to [0,1]; test 200 images per class. **BRATS2020** (brain-tumour MRI, four channels T1, T2, FLAIR, T1ce): axial 2D slices only, padded to 256×256 and normalised; the lowest 80 and uppermost 26 slices excluded; a slice with no tumour in the label mask is healthy, otherwise diseased; training 5,598 healthy + 10,607 diseased slices, test 1,082 tumour + 705 tumour-free slices. Pixel labels are used for evaluation only, on BRATS.

## Key results
**Qualitative (Figs 2, 3)**: versus FP-GAN, VAE and the DDPM stochastic-sampling ablation, the method produces more realistic healthy images that preserve all input detail, giving very detailed anomaly maps; the others either alter other image regions or miss the anomaly; DDPM stochastic noising changes basic anatomy, whereas deterministic DDIM encoding reconstructs every detail. **Healthy input (Fig 7)**: tumour-free slices are left nearly unchanged with an anomaly map close to zero — the key self-check for "change only the lesion". **Hyper-parameter sensitivity (Fig 4)**: on BRATS, Dice (average Otsu threshold) and AUROC on diseased slices are plotted against s for L=250/500/750, with FP-GAN and VAE as horizontal bars; **no numeric table is given in the text**, only curves. **Speed**: one full translation takes about **158 s**, dominated by iterative generation; smaller L or skipped steps speed it up but degrade image quality. The authors also acknowledge prior criticism of reconstruction error as an anomaly score (simple histogram equalisation can beat neural networks, and reconstruction quality correlates poorly with Dice) and plan to explore likelihood-based scores.

## Contributions
- The first diffusion model for (medical) anomaly detection, per the authors.
- **Deterministic DDIM encoding + classifier-guided denoising** for detail-preserving patient→healthy translation.
- No changes to the original DDPM loss or training scheme, so moving to new datasets is straightforward.
- Makes L (encoding depth) and s (guidance strength) explicit knobs for "fidelity vs translation freedom", with a visual sensitivity analysis.

## Limitations
- Thin quantitative evaluation: only Dice/AUROC curves on BRATS, no numeric table or confidence intervals; CheXpert results are qualitative only.
- Weakly supervised, not unsupervised: it needs diseased samples and image-level labels for the classifier — "anomaly" is defined as "what the classifier deems diseased", with no guarantee for unseen anomaly types.
- About 158 s per image, hard to scale to whole slides or millions of cells.
- 2D slices only; sensitive to L and s, whose optimum is data-dependent; large s creates artifacts at the brain border.
- Still scores by "input − reconstruction", an approach the authors acknowledge has been criticised.

## Relation to our direction
This is the most intuitive **image-level** demonstration of **revert** in detect → model → revert: it explicitly generates "what this tissue would look like if healthy", and the difference is both the anomaly map and "the change to be reverted". Its value here is the **conditional translation** operation itself — "healthy" as a steerable condition, not merely "trained on normal data". **Mapping to Topic 1**: at the H&E level it transfers almost directly — train a diffusion model and a noisy classifier on KPMP/HuBMAP healthy and CKD/AKI biopsy H&E patches and translate diseased patches to healthy; at the expression level, the same classifier guidance on a diffusion model over scVI / foundation-model latents yields "a healthy counterfactual for each cell", whose difference is a candidate revert-gene direction (akin to MrVI's sample counterfactuals). **Which assumptions break**: (1) **meaning of image-level labels**: "diseased" in a kidney biopsy is a patient-level diagnosis, and most patches/cells in the section are still normal — the noisy classifier learns a noisy "disease probability", and the guidance direction can carry batch or centre differences (if patients and healthy donors come from different centres, the classifier learns the centre, not the disease); healthy and diseased samples must be batch-balanced, or the classifier given a batch-adversarial term. (2) **ambient RNA / doublets / segmentation errors**: the classifier will also "translate away" these in expression space, so artifacts and lesions share one difference map — Topic 1's cross-modal agreement can gate this: count as disease only where the H&E translation difference and the expression translation difference co-occur. (3) **continuous disease states**: s controls "how far towards healthy", which is actually useful on a continuous injury axis — differences at several s can be read as a dose–response along the axis; without calibration, though, s has no biological meaning. (4) **no pixel/cell-level gold standard**: the paper's quantitative evaluation relies on BRATS tumour masks, which kidney data lack; KidneyAnomalyBench needs experts to judge whether the translated "healthy version" is plausible. (5) **compute**: 158 s per image means whole slides or millions of cells require latent diffusion or few-step sampling. **Related work already in the repo**: AnoPILaD (histo-miccai-2025) uses LoRA-tuned Stable Diffusion with pathology-VLM text conditioning and AnoDDPM-style partial noising to reconstruct normal lymph-node morphology; MoPaDi (counterfactual-diffusion-cancerres-2026) uses a diffusion autoencoder moved along classifier directions to produce pathology counterfactuals for explanation rather than detection — neither states it builds on this paper, but together they show "diffusion + conditioning → healthy/counterfactual version" is viable on pathology images; MedIAnomaly also reports DDPM-type methods clearly ahead of AE/GAN on Camelyon16.

## Reusable assets
- **Code:** official implementation (GitLab address given in the paper; follows the improved-diffusion / guided-diffusion settings).
<https://gitlab.com/cian.unibas.ch/diffusion-anomaly>
- **Data:** BRATS2020 and CheXpert are public datasets (registration required).
- **Eval ideas:** the "healthy input → near-zero anomaly map" self-check (Fig 7) and the L/s sensitivity sweep — both usable as mandatory checks for a kidney translation model.

## Follow-ups
- AnoDDPM (Wyatt et al., CVPRW 2022): unsupervised, simplex-noise diffusion AD, the basis of AnoPILaD.
- Meissen et al.'s critique of reconstruction error as an anomaly score (ref. [15] here: histogram equalisation can beat neural networks).
- histo-miccai-2025 and counterfactual-diffusion-cancerres-2026 in this repo: two uses of diffusion on pathology images (detection vs explanation).

## Cite
```bibtex
@inproceedings{Wolleb2022_220304306,
  title = {Diffusion Models for Medical Anomaly Detection},
  author = {Wolleb, Julia and Bieder, Florentin and Sandk{\"u}hler, Robin and Cattin, Philippe C.},
  booktitle = {Medical Image Computing and Computer Assisted Intervention (MICCAI 2022)},
  series = {Lecture Notes in Computer Science},
  volume = {13438},
  pages = {35--45},
  publisher = {Springer},
  year = {2022},
  doi = {10.1007/978-3-031-16452-1_4},
  eprint = {2203.04306},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2203.04306}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
