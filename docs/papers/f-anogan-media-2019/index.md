# f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks

> **Bibkey** `Schlegl_2019` · **Venue** Medical Image Analysis (2019) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1016/j.media.2019.01.010> · `status: complete`

---

## One-liner
f-AnoGAN replaces AnoGAN's per-image iterative latent search with **a trained encoder E**: train a WGAN-GP on healthy OCT patches, then freeze G and D and train E with a "pixel residual + discriminator-feature residual" objective (izi_f); at test time one forward pass gives the reconstruction G(E(x)) and the anomaly score. Image-level AUC is 0.930, beating AE / AdvAE / ALI and iterative AnoGAN (0.911), while inference drops from 2 days to 20 seconds.

## Problem
Expert labels in clinical imaging are expensive and not every relevant marker is known in advance, so supervised learning only detects annotated lesions. AnoGAN showed that "learn normal, find anomalies by residual" works, but its iterative latent mapping is too slow for large-scale screening or real-time use, and GANs have no image→latent inverse. The question: how to map new images to the GAN's latent space **fast and accurately**, and how encoder-training choices affect detection and localisation.

## Method
**Two training stages, normal data only.** **(1) WGAN-GP**: ResNet-style generator and discriminator with four residual blocks each (G channels 512-256-128-64, D 128-256-512-512, 3×3 convs, layer norm in D), 128-d normal latent; 100,000 iterations (batch 64), five D updates per G update. **(2) Encoder training (G, D frozen)**, three variants: **ziz** — sample z, generate with G, have E recover z (L = ‖z − E(G(z))‖²), never seeing a real image; **izi** — autoencoder-style, L = ‖x − G(E(x))‖²/n; **izi_f (proposed f-AnoGAN)** — izi plus an intermediate discriminator-feature residual, L = ‖x − G(E(x))‖²/n + κ·‖f(x) − f(G(E(x)))‖²/n_d. Rationale: minimising pixel differences alone can map into sparsely sampled latent regions, yielding "unrealistic but low-residual" reconstructions and making the residual an unreliable anomaly marker. A tanh on encoder outputs restricts latents to (−1σ, +1σ). 50,000 encoder iterations (RMSprop). **(3) Scoring**: A(x) = A_R(x) + κ·A_D(x), κ=1; pixel localisation uses |x − G(E(x))|.

## Method lineage
**Paradigm: reconstruction / generative.** A direct successor of AnoGAN (same group, 2017); the authors list three differences: WGAN-GP instead of DCGAN, a learned encoder instead of iterative gradient descent, and a wider set of comparators. ziz is the "latent regressor" baseline from the BiGAN paper (Donahue et al.); the discriminator-feature residual derives from Salimans et al.'s feature matching. The comparator ALI is methodologically equivalent to BiGAN (used for AD by Zenati et al. 2018). It then became **the most-cited GAN baseline** in unsupervised medical AD: MedIAnomaly's taxonomy files it under image reconstruction, and MEATRD (spatial transcriptomics) and AnoPILaD (lymph-node pathology) both use it as a baseline; diffusion methods (AnoDDPM, Wolleb et al. 2022) superseded it within the same "reconstruct to normal" paradigm.

## Data
The same clinical SD-OCT as AnoGAN (Heidelberg Spectralis, 49 B-scans per volume, 496×512×49). Preprocessing: per-volume grey-value normalisation to [−1,1], columns 512→256 (22 µm in x), retina localised by layer segmentation and flattened (thickness normalised only if it exceeds the extracted height). Training: ≈ **850,000 patches of 64×64** from 270 healthy volumes confirmed fluid-free. Test: 10 healthy + 10 fluid cases, **70,000 patches** (70% normal / 30% fluid), with expert pixel-level fluid annotations (evaluation only).

## Key results
**Image-level detection (Table 1, at the Youden point)**: f-AnoGAN **AUC 0.9301**, precision 0.7863, sensitivity 0.8091, specificity 0.9049, F1 0.7975; iterative (≈AnoGAN) AUC 0.9114; AE 0.8688; AdvAE 0.8649; ALI 0.7897; the raw WGAN discriminator output A_D only 0.7504. **Speed**: the iterative scheme (300 updates per image) took **2 days** for 70,000 test images on a Titan X versus **20 seconds** for f-AnoGAN. **Encoders (Table 2)**: izi_f 0.9301 > ziz 0.9066 > izi 0.8874; even when izi/ziz get the discriminator-feature term added at scoring time they reach only 0.8976 / 0.9209, still below izi_f — the discriminator helps already when **training the encoder**. **Pixel localisation**: fluid "segmentation" sensitivity 0.69, specificity 0.75, AUC 0.78 (flagged by the authors as only a coarse indication); AE reconstructions are over-smooth with the worst localisation, while ALI and ziz produce false positives and over-segmentation at the retina–vitreous boundary. **Visual Turing test**: two retina experts separating 50 real from 50 generated normal patches reached mean accuracy **0.44** (below chance), inter-rater agreement 0.58.

## Contributions
- A learned encoder for single-step image→latent mapping, making GAN-based AD usable for high-throughput screening.
- Discriminator-guided encoder training (izi_f) and a systematic comparison of ziz / izi / izi_f.
- A deliberately fair comparison against AE, AdvAE, ALI, iterative mapping and discriminator-only scoring under matched architectures.
- An expert visual Turing test for generation quality instead of the Inception Score, which does not transfer to medical images.

## Limitations
- Per the authors: pixel-level numbers are only coarse — annotations cover only part of the possible anomalies, so false-positive estimates are unreliable and "false positives" may be true unannotated anomalies.
- Works on 64×64 patches only; clinicians read whole B-scans, so the Turing test does not generalise to full images; full-slice generation is left for future work.
- The authors state the precondition explicitly: **large amounts of normal data** and **test distribution equal to training distribution** — any domain shift is read as anomaly.
- One organ, one device, one anomaly type (fluid); depends on layer-segmentation preprocessing.
- The authors position it mainly for normal/abnormal separation and **coarse localisation** (region proposals for expert review), not precise segmentation.

## Relation to our direction
f-AnoGAN is the engineered version of "learn normal → amortised projection onto the normal manifold → read the residual", and matters here in two ways. **First, as a proto-virtual-tissue**: E compresses any observation to a "normal latent", G restores "what it would look like if healthy", and G(E(x)) − x is the revert direction — the same idea as MrVI's counterfactual ("what would this cell look like had it come from another sample"), except f-AnoGAN has no conditioning variable and does not separate cell state from sample effects. **Second, as a mandatory the artifact-injection topic baseline.** **Mapping to kidney omics**: training set = snRNA cells from KPMP/HuBMAP healthy references (features can be scVI latents or foundation-model embeddings) or healthy H&E patches; score = reconstruction residual of expression/patch plus discriminator-feature residual. **Which assumptions break**: the authors' own "test distribution equals training distribution" fails on multi-centre kidney biopsies — batch, sequencing depth and tissue preservation all inflate residuals, so the reference's own inter-sample variation must first serve as a null, as in MapQC (refmap-eval); ambient RNA and doublets, plus Xenium transcript spillover and segmentation errors (see xenium-split, ovrlpy), produce off-manifold profiles that score as high as real lesions; PT injury is a continuous axis (see the continuous damage scores in damage-scores), and f-AnoGAN's residual is continuous too, so thresholds need calibration; OCT has pixel-level fluid labels but kidney data have no matching cell-level gold standard — exactly the gap KidneyAnomalyBench's expert adjudication fills. **Cross-modal agreement**: on one Xenium section, train one f-AnoGAN on H&E patches and one on expression, treat regions where **both** residuals are high as disease candidates and single-modality highs as artifact candidates — the most direct way the artifact-injection topic could turn f-AnoGAN from an anomaly detector into an artifact-vs-disease discriminator. **Evidence already in the repo**: MEATRD uses f-AnoGAN as an image baseline and it scores precision/recall 0 / 0 on a visually subtle breast-tumour edge; in AnoPILaD (histo-miccai-2025) f-AnoGAN reaches only AUC 0.229 / 0.174 on lymph-node LH and Camelyon16 (below chance); MedIAnomaly likewise finds most AE/GAN methods essentially fail on Camelyon16 without ImageNet weights. Conclusion: on kidney tissue it is a **classic baseline that must be reported**, not the main method.

## Reusable assets
- **Code:** official TensorFlow 1.2 / Python 2.7 implementation (WGAN-GP training, izi_f encoder training, anomaly scoring), with the accepted manuscript PDF in the repo.
<https://github.com/tSchlegl/f-AnoGAN>
- **Data:** clinical OCT not public.
- **Eval protocol:** Table 1's metric set (precision/sensitivity/specificity/F1 at the Youden point + AUC) and the visual Turing test — adaptable as a blinded "generated-normal vs real-normal" test for kidney pathologists to check whether the normal model covers healthy variability.

## Follow-ups
- The AnoGAN original (anogan-ipmi-2017 in this repo).
- Simarro Viana et al.'s 3D f-AnoGAN (mentioned in MedIAnomaly), relevant for volumetric / serial-section data.
- AnoDDPM and Wolleb et al. 2022 (diffusion-medical-ad-miccai-2022 in this repo): how diffusion supersedes GANs within the same paradigm.

## Cite
```bibtex
@article{Schlegl_2019, title={f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks}, volume={54}, ISSN={1361-8415}, url={http://dx.doi.org/10.1016/j.media.2019.01.010}, DOI={10.1016/j.media.2019.01.010}, journal={Medical Image Analysis}, publisher={Elsevier BV}, author={Schlegl, Thomas and Seeböck, Philipp and Waldstein, Sebastian M. and Langs, Georg and Schmidt-Erfurth, Ursula}, year={2019}, month=May, pages={30–44} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
