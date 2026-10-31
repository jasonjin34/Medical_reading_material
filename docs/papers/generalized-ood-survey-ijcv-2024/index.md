# Generalized Out-of-Distribution Detection: A Survey

> **Bibkey** `Yang2021_211011334` · **Venue** International Journal of Computer Vision (2024) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1007/s11263-024-02117-4> · `status: complete`

---

## One-liner
Unifies five separately developed sub-fields — anomaly detection (AD), novelty detection (ND), open-set recognition (OSR), OOD detection and outlier detection (OD) — into one "**generalized OOD detection**" framework, distinguishing them along four dichotomies (covariate vs semantic shift, single- vs multi-class ID, whether ID classification is required, inductive vs transductive); systematically reviews OOD methods (classifier outputs, Outlier Exposure, gradients, Bayesian, foundation models, density, distance, reconstruction), runs a unified fair comparison on OpenOOD, and lays out challenges and future directions.

## Problem
Since the term OOD detection emerged in 2017 (the MSP baseline) methods have proliferated, while AD, ND, OSR and OD share motivation and methods yet **develop in isolation**; subtle differences in definitions and settings confuse readers and practitioners, and methods land in different benchmarks and metrics, hard to compare or cross-pollinate. Surveys exist for AD/ND/OSR/OD, but recent OOD methods lacked a systematic summary and a fair cross-sub-field comparison.

## Method
**Unified framework**: first, two kinds of distribution shift — **covariate shift** (P(X) changes, label space fixed: adversarial examples, domain shift, style) and **semantic shift** (P(Y) changes, new classes, which indirectly changes P(X)). The five sub-tasks are then placed by four dichotomies: **AD** treats ID as a whole with no need to distinguish ID classes, split into **sensory AD** (covariate shift only, e.g. MVTec-AD industrial defects) and **semantic AD** (new classes); **ND** (one-/multi-class) concerns semantic anomalies and equals semantic AD; **OSR** = multi-class ND + ID classification; **OOD detection** equals OSR for classification but spans more tasks and solutions and must not hurt ID classification; **OD** is transductive — no train/test split, "ID" is the majority of the observed set. Neighbouring topics: learning with rejection, domain adaptation/generalization (expect covariate shift only and keep predicting), novelty discovery, zero-shot learning, open-world recognition (OSR + incremental learning), and **conformal prediction** (an emerging intersection). **Method review**: (1) classification-based — post-hoc output methods (MSP, ODIN, energy, ReAct, …), Outlier Exposure, gradient-based (GradNorm), Bayesian, and foundation-model OOD (CLIP etc.); (2) density-based; (3) distance-based (Mahalanobis, non-parametric KNN, cosine, …); (4) reconstruction-based; (5) theory. Methods of OSR, AD/ND (density, reconstruction, distance, one-class such as DeepSVDD, self-supervised) and OD are reviewed too. **Experiments**: on OpenOOD, ResNet-18 backbone, unified hyperparameters (SGD, lr 0.1, momentum 0.9, weight decay 5e-4, 100 epochs); CIFAR-10 and CIFAR-100 as ID, each with **near-OOD** (semantic shift only: CIFAR-100/CIFAR-10 and TinyImageNet) and **far-OOD** (MNIST, SVHN, Texture, Places365), removing images that overlap ID semantics (e.g. 1,207 TinyImageNet images belonging to CIFAR-10 classes); AUROC only.

## Method lineage
**A survey spanning all paradigms** — classifier-based OOD (MSP `msp-ood-iclr-2017`, energy `energy-ood-neurips-2020`, ODIN, OE), feature-embedding / distance (Mahalanobis `mahalanobis-ood-neurips-2018`, KNN), density / one-class (DeepSVDD `deep-svdd-icml-2018`), reconstruction / generative, synthetic anomalies / self-supervised (DRAEM `draem-iccv-2021`, CutPaste), and conformal (as a neighbouring topic). Its sensory/semantic anomaly dichotomy is taken from its ref [32] as highlighted in Ruff et al.'s AD review (`ad-unifying-review-procieee-2021`, ref [16]); the experiments rest on OpenOOD (the same team's benchmark, NeurIPS 2022 and v1.5). The cross-modal-consistency paradigm is absent.

## Data
No new data collected. Experiments: CIFAR-10 / CIFAR-100 (50k train, 10k test each) as ID; near-OOD = CIFAR-100 (or CIFAR-10) + TinyImageNet (removing 1,207 / 2,502 semantically overlapping images); far-OOD = MNIST, SVHN, Texture, Places365 (1,305 removed). AD benchmark referenced: MVTec-AD; larger ImageNet OOD benchmarks and the corrected NINCO dataset are discussed.

## Key results
Findings of the OpenOOD fair comparison (Fig. 5, near/far-OOD AUROC):
- **Data augmentation is most effective**: PixMix, CutMix, etc.; PixMix reaches 93.1% on CIFAR-10 near-OOD, the best overall; Ensemble and Mixup also do well.
- **Extra data seems unnecessary**: the best extra-data method (UDG) beats the best extra-data-free method (KNN) only on CIFAR-10 near-OOD, while requiring lots of real outliers (the whole TinyImageNet training set here).
- **Post-hoc methods generally beat training-based ones**, and post-hoc methods since 2021 keep improving; classic MDS (Mahalanobis) does well on MNIST but poorly on CIFAR-10/100, whereas KNN stays strong on MNIST, CIFAR and ImageNet.
- **Some AD methods excel at far-OOD**: DRAEM and CutPaste, designed for MVTec-AD pixel-level appearance differences, score highly on far-OOD (especially with CIFAR-100 as ID).
- **Covariate shift**: cited experiments show most current OOD detectors are more sensitive to covariate than to semantic shift (→ "full-spectrum OOD").

## Contributions
(1) The first framework unifying AD, ND, OSR, OOD and OD, with a clear task taxonomy (Figs. 1–2); (2) a comprehensive review of OOD methods, including the foundation-model era; (3) a cross-sub-field fair comparison via OpenOOD; (4) challenges — proper evaluation and benchmarking (specify the OOD type; remove ID-overlapping samples), outlier-free training, the classification–detection trade-off, real large-scale benchmarks — and future directions: cross-sub-task method transfer, combining OOD detection with generalization, open-set noisy labels, broader tasks (segmentation, time series, LLM hallucination), and world / foundation models.

## Limitations
Experiments are CIFAR-scale and AUROC-only, and deliberately exclude pure covariate-shift evaluation (to avoid over-emphasizing covariate-shift detection, the authors say); the framework is illustrated mainly with classification and says little about biomedical, continuous-label or class-free data; conformal gets only a brief neighbouring-topic mention; multi-modal / cross-modal agreement as a detection signal is not covered; as a survey, each method gets a short summary and conclusions depend on OpenOOD's unified hyperparameters.

## Relation to our direction
**This is the vocabulary for defining KidneyAnomalyBench's task types.** Placing the kidney setting on its axes: (1) "cell states absent from the healthy reference" (failed-repair PT, a new immune-infiltrate state) = **semantic shift**; flagging only → ND / semantic AD; flagging while annotating known cells → OSR / OOD detection (reference mapping + rejection). (2) **Batch effects, ambient RNA, doublets, Xenium segmentation errors, H&E stain variation** = **covariate shift** — which we want to be **robust to**, not report. The survey's cited finding that "most OOD detectors are more sensitive to covariate than semantic shift" is exactly the artifact-injection topic's core risk: an untreated detector reports artifacts as disease. Its "full-spectrum OOD" (generalize over covariate shift, detect semantic shift) is a formal statement of the artifact-injection topic's goal of separating artifact from disease via **cross-modal agreement** — and cross-modal agreement itself is missing from the survey's method taxonomy, a gap we can fill. (3) Removing doublets / low-quality cells inside one dataset = **transductive OD**. **Directly reusable for evaluation**: (a) near- vs far-OOD stratification — in kidney, near = mild injury / aPT-like neighbouring states, far = other organs' cells or entirely different tissue; (b) "OOD test sets must not contain ID classes" — most cells in a disease biopsy are actually normal, so labelling an entire disease biopsy as "anomalous" contaminates evaluation the way early OOD benchmarks were, hence KidneyAnomalyBench needs expert validation at the cell/region level; (c) the demand to state which OOD type is being detected. **Methodologically**: "post-hoc beats training-based, KNN is more robust than Mahalanobis" suggests starting with post-hoc distance baselines on scVI / foundation-model embeddings; "extra data seems unnecessary" supports not depending on auxiliary outlier sets. **Related repo papers**: `pathology-ad-bench-mlhealth-2025` and `medianomaly-media-2025` apply the same "unified protocol, fair comparison" idea to pathology / medical imaging; `ad-unifying-review-procieee-2021` is the complementary AD-side review; `conformal-scrna-bioinformatics-2025` realizes the conformal × OOD direction the survey only mentions. **For the agent-trustworthiness topic**: its task taxonomy is a template for an omics-agent **failure taxonomy** (define the shift types before the failure types), and "OOD detection for LLM hallucination" is listed as a future direction directly relevant to the agent-trustworthiness topic's claim verification.

## Reusable assets
- **Code / benchmark:** OpenOOD — a unified framework and leaderboard with implementations of MSP, ODIN, MDS, EBO, ReAct, KNN, DeepSVDD, DRAEM, CutPaste and more — a ready baseline suite for kidney embeddings.
<https://github.com/Jingkang50/OpenOOD>
- **Task taxonomy:** Fig. 1 (four dichotomies) and Fig. 2 (five sub-task diagrams) — directly usable for writing KidneyAnomalyBench task definitions.
- **Benchmark-building rules:** near/far-OOD stratification + removing samples that overlap ID semantics.

## Follow-ups
- The OpenOOD v1.5 report and the full-spectrum OOD paper (covariate-shifted ID) — the setting closest to "robust to batch effects, sensitive to disease".
- Non-parametric KNN OOD (Sun et al., 2022) and ReAct — robust post-hoc methods in the survey.
- The conformal × OOD works the survey cites (its refs [104–106]).

## Cite
```bibtex
@article{Yang2021_211011334,
  title = {Generalized Out-of-Distribution Detection: A Survey},
  author = {Yang, Jingkang and Zhou, Kaiyang and Li, Yixuan and Liu, Ziwei},
  journal = {International Journal of Computer Vision},
  volume = {132},
  pages = {5635--5662},
  year = {2024},
  doi = {10.1007/s11263-024-02117-4},
  eprint = {2110.11334},
  archivePrefix = {arXiv},
  url = {https://doi.org/10.1007/s11263-024-02117-4}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
