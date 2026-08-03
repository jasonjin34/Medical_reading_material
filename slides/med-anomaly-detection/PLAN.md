# Presentation Plan — Anomaly Detection in Medical Imaging
### State of the Art & Future Directions · internal group talk (English)

> Scope decision: this deck is a **survey of existing work + future directions**.
> It deliberately does **not** foreground any of our own papers — methods are
> presented at the field level and cited to their original authors. Future
> directions are framed as *open research directions for the field* (efficient
> generative backbones, reasoning/interpretability, trustworthy medical
> foundation models), not as our contributions.

## 1. Meta

| | |
|---|---|
| **Audience** | Internal research group (ML + medical imaging background) |
| **Duration** | ~30 min talk + ~5–10 min discussion |
| **Language** | English (slides + narration) |
| **Slide count** | 18 content slides + 1 references appendix |
| **Deliverable** | `index.html` self-contained deck (rebuild the existing file, English, self-paper removed) |
| **Goal** | (1) give the group a clean mental map of *how medical anomaly detection works today*; (2) identify the *open problems*; (3) propose *concrete future directions* the group could pursue |

## 2. Narrative arc (one sentence per act)

1. **Why** — medical AD matters and is hard → the field trains on *normal only*.
2. **What exists** — a taxonomy of four method families, with the two dominant ones (diffusion reconstruction, VLM adaptation) in depth.
3. **What we've learned** — benchmark findings + an honest cross-family comparison.
4. **What's open** — the unsolved problems (specificity, 3D compute, trust, privacy).
5. **Where it's going** — three future directions + a roadmap for the group.

Time budget: ~1.5 min/slide average; front/back matter faster, deep-dive slides (6, 9, 11, 12) slower. Keep ≤ 4 bullets visible at a time; reveal step by step.

---

## 3. Slide-by-slide

Each slide lists: **On-slide** (what appears, revealed as fragments) · **Talking points** (narration) · **Visual** · **~Time**.

### S1 — Title
- **On-slide:** "Anomaly Detection in Medical Imaging — State of the Art & Future Directions" · subtitle "A survey for [group] · [date]" · presenter name.
- **Talking points:** one line on why you picked the topic; set expectation: survey + directions, not a single method.
- **Visual:** clean title, one accent rule. **~0:30**

### S2 — Why medical anomaly detection?
- **On-slide:** clinical motivation (screening, rare-disease/long-tail, triage, opportunistic findings); the label problem (annotation is expensive, exhaustive abnormal labels impossible).
- **Talking points:** contrast with natural-image AD (industrial defect) — medicine adds anatomy, heterogeneity, and safety stakes.
- **Visual:** 3 icons/stat chips (heterogeneity · scarcity · complexity). **~1:30**

### S3 — Problem formulation
- **On-slide:** the *learn-normal, flag-deviation* setup; anomaly **score**; task granularity (image-level detection vs pixel-level localization/segmentation); metrics (AUROC, AP/AUPRC, Dice/IoU, and pixel-AUROC).
- **Talking points:** define unsupervised vs zero-/few-shot; note metric choice matters (foreshadow benchmark slide).
- **Visual:** a simple pipeline diagram: image → model (normal prior) → residual/score → map. **~1:30**

### S4 — Taxonomy of approaches (the map)
- **On-slide:** four families —
  1. **Reconstruction-based** (AE, GAN, **Diffusion**)
  2. **Feature / embedding-based** (ImageNet features, memory banks, kNN/one-class)
  3. **Self-supervised / synthetic-anomaly** (learn to spot planted defects)
  4. **VLM / foundation-model adaptation** (CLIP → medical)
- **Talking points:** this is the map for the next section; the two we'll go deep on are Diffusion (family 1) and VLM adaptation (family 4).
- **Visual:** 2×2 or a labeled tree; highlight the two deep-dive branches. **~1:30**

### S5 — Reconstruction-based (classical): AE & GAN
- **On-slide:** core assumption (normal-trained generator can't rebuild pathology → residual = anomaly); AnoGAN / f-AnoGAN lineage; failure modes (mode collapse, "identity shortcut" where the net copies the anomaly through).
- **Talking points:** why quality/coverage limits pushed the field toward diffusion.
- **Visual:** input vs pseudo-healthy vs residual triptych (schematic, not a real patient image). **~1:30**

### S6 — Reconstruction-based (diffusion) ★ deep dive
- **On-slide:** DDPM in one line (forward noising / learned reverse denoising; better mode coverage & fidelity than GAN); **AnoDDPM** — partial diffusion + multi-scale **Simplex noise** to *control anomaly size* (Gaussian noise erases low-freq, misses large lesions); reported gains (Dice +25.5%, IoU +17.6% on T1 MRI); **AutoDDPM** — automatic **mask–stitch–resample** for seamless healthy in-painting.
- **Talking points:** diffusion is now the dominant reconstruction backbone; explain the *size-control* insight simply.
- **Visual:** noising/denoising strip; a "noise scale ↔ anomaly size" annotation. **~2:00**

### S7 — The reconstruction dilemma & guided restoration
- **On-slide:** the **noise/fidelity trade-off** — high noise erases pathology *and* healthy anatomy → false positives, low specificity; solutions: **THOR** (temporal harmonization / implicit guidance to re-integrate healthy tissue), latent-space + **rectified-flow** restoration for 3D volumes (compute + context).
- **Talking points:** this is the central practical pain point for clinical deployment; guidance/latent trends are the response.
- **Visual:** a "too little vs too much noise" curve with a specificity axis. **~2:00**

### S8 — Feature-based & self-supervised (brief)
- **On-slide:** embedding/memory-bank methods (frozen ImageNet/medical features + kNN/one-class; e.g. PatchCore-style) — strong, simple baselines; self-supervised **synthetic-anomaly** methods (CutPaste / FPI / Poisson-blending adapted to medical) that turn AD into a proxy classification/segmentation task.
- **Talking points:** these are the "boringly strong" baselines that new methods must beat; set up the benchmark slide's finding that simple features are competitive.
- **Visual:** two mini-cards (memory bank · synthetic anomaly). **~1:30**

### S9 — VLM / foundation-model adaptation I ★ deep dive
- **On-slide:** the **domain gap** (natural ↔ medical → zero-shot CLIP collapses); **MVFA-AD (CVPR 2024)** — lightweight **multi-level residual adapters** + **pixel-level vision–language alignment**; re-focuses attention from generic object semantics to local abnormality; strong zero-/few-shot generalization to unseen modalities/organs (zero-shot AUC +6.24%, few-shot +7.33%).
- **Talking points:** the appeal is generalization across modalities from little data — the opposite trade-off from per-dataset reconstruction models.
- **Visual:** CLIP encoder + adapter blocks diagram; a "generic→local" attention arrow. **~2:00**

### S10 — VLM / foundation-model adaptation II
- **On-slide:** **MediCLIP (MICCAI 2024)** — few-shot, *no real anomalies*: synthesize disease-like perturbations + learnable prompts + visual residual adapters → CLIP becomes a medical detector; broader trend toward **medical foundation models** (pathology/radiology FMs) as reusable backbones.
- **Talking points:** connects to our reading list's foundation-model thread; note gating/compute realities.
- **Visual:** synthetic-anomaly + prompt-tuning schematic. **~1:30**

### S11 — Benchmarks & evaluation lessons ★
- **On-slide:** **MedIAnomaly (MedIA 2025)** — 5 modalities / 7 datasets / 30 methods. Findings: (a) **distance/metric matters** — SSIM/LPIPS/perceptual > pixel-wise L2 (semantic > photometric); (b) **ImageNet-pretrained features are a strong base** even without medical-specific design; (c) many simple methods are **surprisingly competitive** → beware over-claiming.
- **Talking points:** this reframes the whole field — evaluation choices can dominate method choices; argue for standardized, multi-metric benchmarking.
- **Visual:** small results-style table (method family × metric, qualitative). **~2:00**

### S12 — What works today: cross-family comparison ★
- **On-slide:** comparison table across the four families —
  | Family | Data need | Localization | Interpretability | Compute | Generalization |
  reconstruction-diffusion / feature-memory / self-supervised / VLM-adaptation.
- **Talking points:** honest trade-offs; there is no single winner — pick by modality, data regime, and deployment constraint.
- **Visual:** the table, one row highlighted per column's "best". **~2:00**

### S13 — Open challenges
- **On-slide:** (1) **specificity / false positives** (the noise dilemma); (2) **3D / volumetric** compute; (3) **interpretability & clinical trust** (heatmaps ≠ reasons); (4) **domain shift** (scanner/site/stain); (5) **evaluation gaps** (no unified protocol, label noise); (6) **privacy & safety** of medical foundation models trained on patient data.
- **Talking points:** these six frame the future-work section — each future direction answers one or more.
- **Visual:** 6 compact chips, color-coded to the three future directions. **~1:30**

### S14 — Future direction 1: efficient generative backbones
- **On-slide:** diffusion **SDE → latent flow matching / rectified flows** (ODE, fewer steps, 3D-friendly); efficiency via **step distillation** and **model compression/pruning**; goal: high-fidelity pseudo-healthy restoration at volumetric scale without the noise-paradox.
- **Talking points:** answers challenges (1) specificity and (2) 3D compute; keep vendor-neutral (no self-paper).
- **Visual:** SDE→ODE arrow; "steps ↓, context ↑" annotation. **~1:30**

### S15 — Future direction 2: beyond pixels — reasoning & interpretability
- **On-slide:** move from black-box residual/embedding to **structured, knowledge-grounded reasoning**: perception (VLM extracts anatomical facts) → reasoning (rules / knowledge graphs / logic) → **natural-language, auditable rationales**; agentic/interactive diagnosis.
- **Talking points:** answers challenge (3) trust; note this is an emerging field direction (neuro-symbolic AD, VLM-explained AD) — cite as a trend, not our work.
- **Visual:** two-layer "perceive → reason → explain" diagram. **~1:30**

### S16 — Future direction 3: trustworthy medical foundation models
- **On-slide:** as hospitals pretrain large models on PACS/pathology data — **privacy** (memorization → data-extraction attacks; machine **unlearning**) and **safety/behavioral control** (prevent harmful/unethical generation); **regulatory compliance** (GDPR/PHI).
- **Talking points:** answers challenges (5)/(6); frame as prerequisites for real deployment; general field framing.
- **Visual:** shield/lock motif; "safety · privacy · compliance" trio. **~1:30**

### S17 — Roadmap synthesis
- **On-slide:** a **near-term vs long-term** map (or a small timeline): near-term = better benchmarks + latent-diffusion/flow baselines + FM adapters; long-term = reasoning-grounded, trustworthy, 3D-native systems. Call out **1–2 concrete things the group could prototype next quarter**.
- **Talking points:** make it actionable — this is the "so what do *we* do" slide.
- **Visual:** 2×2 (impact × effort) or a timeline with 3–4 milestones. **~1:30**

### S18 — Summary & discussion
- **On-slide:** 3 takeaways —
  1. medical AD ≈ *learn-normal, flag-deviation*; two dominant engines: **diffusion reconstruction** & **VLM adaptation**;
  2. the field's real bottlenecks are **specificity, 3D compute, trust, and privacy** — not raw accuracy;
  3. the frontier is **efficient generative + reasoning-grounded + trustworthy** medical models.
  Then 2–3 open questions for the group.
- **Visual:** clean closing; discussion prompt. **~1:00**

### S19 — References (appendix)
- MedIAnomaly (Cai et al., *Medical Image Analysis*, 2025) · AnoDDPM (Wyatt et al., CVPRW 2022) · AutoDDPM / "Mask, Stitch, and Re-Sample" (Bercea et al., 2023) · THOR (Bercea et al., MICCAI 2024) · MVFA-AD (Huang et al., CVPR 2024) · MediCLIP (Zhang et al., MICCAI 2024). Foundations: DDPM (Ho et al., 2020), CLIP (Radford et al., 2021), AnoGAN/f-AnoGAN (Schlegl et al., 2017/2019), PatchCore (Roth et al., 2022), rectified/latent-flow 3D localisation (2024–25).

---

## 4. Design system (for the rebuild)

- **Language:** English only. Reuse the existing deck engine (keyboard nav, fragments, speaker notes toggle) — just swap content and drop the self-research slides.
- **Look:** keep clean/minimal; light background, one indigo + one teal accent, system fonts, generous whitespace, ≤4 bullets/step. Stat chips for the few numbers (Dice +25.5%, AUC +6.24%, etc.).
- **Visuals:** prefer **schematic diagrams built in CSS/SVG** over copyrighted figures. If a paper figure is wanted, use only open-access/arXiv/CC-BY sources with a visible citation; never paywalled figures.
- **Speaker notes:** one or two English narration prompts per slide (via the `N` toggle) so the talk flows.

## 5. What changed vs the first draft

- **Removed:** the "our research" section (LogicAD/EcoDiff/Minimalist Erasure/UniForget) and the self-centred comparison table.
- **Added:** feature-based & self-supervised family (S8), an explicit taxonomy (S4), a cross-family comparison (S12), an open-challenges slide (S13), and a group-facing roadmap (S17).
- **Reframed:** future directions as neutral field-level trends (efficient generative backbones · reasoning/interpretability · trustworthy FMs).

## 6. Build options (pick before I build)

1. **Figures:** all-schematic (fastest, zero copyright risk) — *recommended* — or add a few open-access figures with citations.
2. **Depth:** 18 slides as above, or trim to 16 (merge S8 into S5, S10 into S9).
3. **Roadmap specificity:** keep generic, or tailor S17 to this group's actual projects (tell me them and I'll make it concrete).
4. **Handout:** add a print stylesheet to export all slides to a PDF.
