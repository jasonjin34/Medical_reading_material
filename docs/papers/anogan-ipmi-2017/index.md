# Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery

> **Bibkey** `Schlegl2017_170305921` · **Venue** Information Processing in Medical Imaging (IPMI 2017), LNCS 10265 (2017) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/1703.05921> · `status: complete`

---

## One-liner
AnoGAN trains a DCGAN only on **healthy** retinal OCT patches; at test time it runs 500 gradient-descent steps in latent space to find the "most similar normal image" G(z) for each new patch, and scores anomalies by a weighted sum of a **pixel residual and a residual on intermediate discriminator features**, with the residual image serving as the anomaly map. Per the authors it is the first use of GANs for anomaly detection, and it founds the "learn normal → reconstruct → read the residual" paradigm.

## Problem
Automated detection of imaging markers usually needs large annotated sets of known lesions; annotation is expensive and confines detection to a "vocabulary of known markers" — many diseases lack sufficient markers, or their predictive power is limited. The question: can unsupervised learning on healthy data alone surface **regions that deviate from normal anatomical variability** as candidates for new markers? Earlier AD work used 1D, texture or synthetic data (different from medical images), or a convolutional autoencoder plus one-class SVM (whose hyper-parameter sets the fraction of training points covered).

## Method
**(1) Manifold of normal variability**: random 64×64 patches from M healthy OCT images train a standard DCGAN (G: four fractionally-strided conv layers; D: four conv layers; 5×5 filters; channels 512-256-128-64), with no labels. **(2) Image → latent mapping**: GANs give no inverse, so for a query x the method starts from a random z₁, freezes G and D, and updates only z for Γ=500 steps to minimise L(z) = (1−λ)·L_R + λ·L_D. The **residual loss** L_R = Σ|x − G(z)| enforces visual similarity; for the **discrimination loss** there is a reference version from Yeh et al.'s inpainting (feed G(z) to D and ask for "real") and the proposed **feature-matching version** L_D = Σ|f(x) − f(G(z))| with f an intermediate discriminator layer — using D as a feature extractor, not a classifier. λ=0.1 (chosen in preliminary experiments on a face dataset). **(3) Scoring**: A(x) = (1−λ)·R(x) + λ·D(x) from the final-step losses; the residual image x_R = |x − G(z_Γ)| gives pixel-level localisation.

## Method lineage
**Paradigm: reconstruction / generative.** It builds on DCGAN (Radford et al.), Yeh et al.'s semantic inpainting (latent search) and Salimans et al.'s feature matching; its comparators are an adversarial convolutional autoencoder (aCAE) and the group's earlier CAE + one-class SVM. It directly led to **f-AnoGAN** (same group, 2019: a trained encoder replaces iterative search, WGAN-GP replaces DCGAN) and to the GANomaly / Skip-GANomaly / ADGAN family; Ruff et al.'s unifying review files it as a reconstruction method that treats the generator as a stochastic decoder and latent search as implicit encoding. Later diffusion methods (AnoDDPM, Wolleb et al. 2022) essentially swap "generator + projection onto the normal manifold" for "noise + denoise".

## Data
Clinical high-resolution SD-OCT retinal volumes (49 B-scans per volume, 496×512×49 voxels). Training: 270 healthy subjects' volumes (selected for absence of fluid), preprocessed by grey-value normalisation to [−1,1], resizing to 22 µm in x (≈256 columns), and retina extraction and flattening via layer segmentation, yielding **1,000,000 training patches of 64×64**. Test: 10 further healthy and 10 fluid-containing cases, **8,192 patches** in total; experts' voxel-wise fluid annotations exist for the pathological cases and are used only for evaluation. A patch is positive if at least one pixel is annotated as fluid.

## Key results
**Image-level detection (Table 1, at the Youden point)**: AnoGAN **AUC 0.89**, precision 0.8834, sensitivity 0.7279, specificity 0.8928; GAN_R (same GAN, Yeh-style discrimination loss) AUC 0.88; using the DCGAN discriminator output P_D directly AUC 0.72; aCAE AUC 0.73 (the authors observe aCAEs "over-adapt" and reconstruct anomalies too). **Components**: the proposed feature-matching discrimination score D(x) beats the reference D̂(x), but AnoGAN and GAN_R have similar overall AUC, which the authors attribute to the strong residual score R(x). **Qualitative**: normal patches are reconstructed closely, fluid patches show clear intensity/texture differences; residual maps match fluid annotations and additionally flag unannotated **hyperreflective foci (HRF)**. **Compute**: 500 backprop steps of latent mapping per test image — the speed bottleneck f-AnoGAN later removes.

## Contributions
- First use of GANs for anomaly/novelty detection (per the authors): learn a manifold of normal anatomical variability from healthy data only.
- A latent-space mapping that tackles GANs' pre-image problem, with **matching of intermediate discriminator features** as the discrimination loss (D as feature extractor).
- A combined anomaly score A(x) derived directly from the mapping loss, plus a residual map — image-level decisions and pixel-level localisation at once.
- Frames "anomaly = marker candidate", surfacing unannotated lesions (HRF) rather than only re-detecting known classes.

## Limitations
- **Very slow inference**: 500 gradient steps per sample; f-AnoGAN later reports an equivalent iterative scheme took 2 days for 70,000 images.
- Evaluation uses one annotated anomaly class (fluid); the authors concede "false positives" may be unannotated true anomalies, biasing quantitative evaluation.
- Only image-level ROC/AUC is quantitative; pixel-level segmentation is qualitative; λ was chosen on a face dataset, not tuned on OCT.
- Small 64×64 patches, one device, one organ; DCGAN training is unstable and fails on small data (the Deep SVDD paper reports AnoGAN's DCGAN did not converge on 780 GTSRB images).
- Relies on layer segmentation and flattening — a segmentation failure becomes an "anomaly" by construction.

## Relation to our direction
AnoGAN is the **conceptual prototype** for the whole **detect → model → revert** chain: G is a "generative model of normal tissue", G(z*) is "what this sample would look like if healthy", and the residual is "what disease changed". That is virtual tissue in its simplest form — a model that can only generate normal, plus an operation projecting an observation back onto the normal manifold; the difference before and after projection is naturally the revert direction. **Mapping to Plan A (kidney omics)**: samples can be snRNA/snATAC cells, Xenium cells or Visium spots, or H&E patches; the "healthy training set" is KPMP/HuBMAP healthy living-donor tissue or reference samples from the Lake atlas; the feature space need not be raw counts — scVI latents or foundation-model embeddings (UNI2-h-type for H&E) work. **Which assumptions break**: (1) **batch effects** — a new donor's/batch's systematic shift sits off the normal manifold and is scored as anomalous; reference mapping (see refmap-eval) or removing batch directions from the residual is needed first. (2) **ambient RNA, doublets, Xenium segmentation errors** — the resulting "chimeric" profiles also leave the normal manifold, and AnoGAN will faithfully rank them highest; this is Plan A's core problem: **anomalous ≠ diseased**. (3) **continuous disease states** — PT injury and failed repair are gradients with no OCT-fluid-style present/absent; A(x) is continuous and its threshold needs calibration (see conformal-scrna). (4) **no pixel-level gold standard** — AnoGAN itself concedes "false positives may be unannotated true anomalies", which is exactly why KidneyAnomalyBench needs case-by-case expert adjudication rather than label-based AUC alone. (5) 500 optimisation steps per sample is infeasible for millions of cells. **Plan A's cross-modal agreement grafts on directly**: compute an H&E residual and an expression residual for the same tissue; true lesions should appear in **both** modalities, whereas ambient or segmentation artifacts usually appear in only one — use "agreeing residuals" to separate disease from artifact. **Existing repo adaptations**: STANDS (spatial-natcommun-2024) trains a GAN on a normal reference to reconstruct spots, scores anomalies by reconstruction error, and adds a memory bank against mode collapse; MEATRD and histo-miccai-2025 both use f-AnoGAN (AnoGAN's successor) as a baseline, and it performs very poorly on breast ST and lymph-node pathology — raw GAN reconstruction is at best a weak baseline on tissue data.

## Reusable assets
- **Code:** no official repo in the paper; the authors adapted bamos/dcgan-completion.tensorflow. The official f-AnoGAN code (which includes the iterative z-mapping comparator) is the practical choice.
<https://github.com/tSchlegl/f-AnoGAN>
- **Data:** the clinical OCT data are not public.
- **Eval protocol:** "patch positive if any pixel is positive" image-level labels plus precision/sensitivity/specificity at the Youden point — a template for KidneyAnomalyBench cell/region-level labels.

## Follow-ups
- f-AnoGAN (f-anogan-media-2019 in this repo): speed/accuracy after an encoder replaces iterative search.
- Seeböck et al. 2016 (CAE + one-class SVM, the group's predecessor) and Zenati et al. 2018 (BiGAN anomaly detection).
- GANomaly / Skip-GANomaly (reconstruction baselines in pathology-ad-bench).

## Cite
```bibtex
@inproceedings{Schlegl2017_170305921,
  title = {Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery},
  author = {Schlegl, Thomas and Seeb{\"o}ck, Philipp and Waldstein, Sebastian M. and Schmidt-Erfurth, Ursula and Langs, Georg},
  booktitle = {Information Processing in Medical Imaging (IPMI 2017)},
  series = {Lecture Notes in Computer Science},
  volume = {10265},
  pages = {146--157},
  publisher = {Springer},
  year = {2017},
  doi = {10.1007/978-3-319-59050-9_12},
  eprint = {1703.05921},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1703.05921}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
