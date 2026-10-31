# Energy-based Out-of-distribution Detection

> **Bibkey** `Liu2020_201003759` · **Venue** Advances in Neural Information Processing Systems 33 (NeurIPS 2020) (2020) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2010.03759> · `status: complete`

---

## One-liner
Interpret a classifier's logits as an energy-based model: the free energy E(x) = −T·logsumexp(f(x)/T) is aligned with input density, whereas log-MSP is just the energy of "logits minus the max logit", a biased score. So **replace softmax confidence with energy** — no training, no hyperparameters — and average FPR95 on CIFAR-10 drops by 18.03%; with auxiliary outlier data, **energy-bounded fine-tuning** with two squared hinge losses widens the ID/OOD energy gap and beats Outlier Exposure.

## Problem
OOD detection that relies on softmax confidence suffers because networks can give arbitrarily high confidence to inputs far from the training data (the softmax posterior has a label-overfitted output space). Explicit density estimation is unreliable too: deep generative models can assign higher likelihood to OOD data (Nalisnick et al.), and JEM-style generative estimation of log p(x) needs normalized densities and is unstable to optimize. The question: can a purely discriminative classifier yield an OOD score that is density-aligned and easy to use?

## Method
**Energy function**: for K-class logits f(x), define E(x, y) = −f_y(x) and the free energy E(x; f) = −T·log Σᵢ e^{fᵢ(x)/T} (the log of the softmax denominator). Via the Gibbs distribution, p(x) ∝ e^{−E(x)/T}, so lower energy → higher density. An NLL-trained classifier pushes ID energy down (the gradient pushes the true class's energy down and pulls the others up). **Inference-time score**: threshold −E(x; f) at τ (chosen on ID data so most ID inputs pass); high energy → OOD. One logsumexp, T = 1, nothing to tune. **Link to softmax**: log max_y p(y|x) = E(x; f) + f_max(x) — for ID data E is low and f_max high, so the two partly cancel; MSP is a biased energy shifted by the max logit. **Energy-bounded training**: objective = cross-entropy + λ·L_energy with L_energy = E_ID[max(0, E(x_in) − m_in)²] + E_OOD[max(0, m_out − E(x_out))²], two separate margins (m_in ∈ {−3, −5, −7}, m_out ∈ {−15, −19, −23, −27}, chosen by validation FPR95); λ = 0.1, 10 epochs, LR 0.001 with cosine decay; auxiliary outliers from 80 Million Tiny Images (deduplicated against CIFAR). A single-margin hinge was tried and trained less stably.

## Method lineage
**Paradigm: classifier-based OOD**, with the trained variant belonging to the Outlier-Exposure branch that uses auxiliary outliers. It builds directly on the MSP baseline (`msp-ood-iclr-2017`, ref [13]), ODIN (temperature scaling — here, larger T makes energy worse) and Outlier Exposure (pushing OOD softmax toward uniform), and contrasts with JEM. Mahalanobis (`mahalanobis-ood-neurips-2018`) appears as a baseline in Table 2. **Afterwards**: the survey (`generalized-ood-survey-ijcv-2024`) lists it as a representative post-hoc output-based method, followed by JointEnergy (multi-label) and ReAct (activation truncation boosting energy and other scores); it appears in the OpenOOD benchmark as EBO.

## Data
ID: CIFAR-10, CIFAR-100, SVHN (standard splits), WideResNet. Six OOD test sets: Textures, SVHN, Places365, LSUN-Crop, LSUN-Resize, iSUN. Auxiliary outliers: 80 Million Tiny Images. CelebA is added for the generative-model comparison.

## Key results
- **An illustrative example**: a CIFAR-10 image and an SVHN image get nearly identical softmax confidence (1.0 vs 0.99) but negative energies of 11.19 vs 7.11.
- **Pre-trained, no fine-tuning** (WideResNet, averaged over six OOD sets): CIFAR-10 FPR95 drops from 51.04 (MSP) to 33.01 (−18.03), AUROC 90.90 → 91.88; ODIN 35.71, Mahalanobis 37.08 (AUROC 91.09 / 93.27). CIFAR-100 FPR95: MSP 80.41, energy 73.60, ODIN 74.64, Mahalanobis 54.04. With SVHN as ID, energy beats softmax by 8.69 FPR95 points.
- **Fine-tuning**: on CIFAR-10, energy fine-tuning FPR95 3.32 (AUROC 98.92) vs OE 8.53 (98.30), a 5.20 drop; on CIFAR-100, 47.55 vs OE 58.10 (10.55 drop), AUROC 88.46 vs 85.19. In the SVHN illustration FPR95: softmax 48.49 → energy 35.59 (pre-trained); OE 4.36 → energy fine-tuning 1.04.
- **Accuracy preserved**: CIFAR-10 test error 4.98% for energy fine-tuning (text; 4.87 in Table 2) vs 5.32% OE vs 5.16% pre-trained.
- **vs generative / hybrid models** (CIFAR-10, AUROC): energy score 0.91 SVHN / 0.87 CIFAR-100 / 0.78 CelebA, energy fine-tuning 0.99 / 0.94 / 1.00; JEM-softmax 0.89 / 0.87 / 0.79; class-conditional Glow 0.64 / 0.65 / 0.54.
- **Temperature**: raising T from 1 to 1000 makes predictions more uniform and energy less separable — T = 1 is best.

## Contributions
(1) An exact relation between MSP and free energy, explaining why MSP is biased; (2) a parameter-free, plug-in post-hoc OOD score; (3) a training objective that directly optimizes the ID/OOD energy gap, works with auxiliary outliers and leaves the semantic class space unchanged; (4) a density interpretation inside a discriminative framework, sidestepping generative-model training.

## Limitations
"Density alignment" holds only up to a normalizing constant — the logits are not trained as a true density; the fine-tuned variant needs a large auxiliary outlier set (80M Tiny Images) with careful deduplication, and the survey lists dependence on auxiliary outliers as a major open challenge; on CIFAR-100 the pre-trained energy score is still clearly worse than Mahalanobis (73.60 vs 54.04 FPR95); validated only on 32×32 image classification; the authors name going beyond image classification as future work.

## Relation to our direction
**Mapping onto kidney omics**: any cell-type annotator trained on a healthy reference (KPMP, the Lake atlas), or an H&E tissue-type classifier, yields a free energy per cell/spot/patch; it uses the overall logit magnitude that MSP throws away, so it is a stronger, equally free Topic-1 baseline. **Energy fine-tuning is the kidney version of Outlier Exposure**: it needs an auxiliary outlier set — e.g. cells from non-kidney organ atlases or H&E patches of other tissues — which is exactly what `histo-nejmai-2024` does (an OE binary classifier separating normal GI patches from heterogeneous out-of-domain tissue patches, its best method). **Which assumptions break**: (1) **logit magnitude is coupled to data quality** — low-UMI, high-mito or ambient-RNA-contaminated cells carry weak signal, small logits → high energy → flagged as OOD, so energy may mostly detect **low-quality cells** rather than disease states; (2) **batch effects** rescale logits the same way; (3) **the auxiliary outlier set decides what the detector learns** — using empty droplets, doublets or other technical noise as outliers turns it into a QC tool, while other organs' cells teach "organ identity" rather than "kidney pathology" — neither equals disease; (4) continuous disease states have no clean ID/OOD energy boundary, so the two-margin setup needs rethinking. Energy therefore fits as a **per-modality score**, with the artifact-injection topic's cross-modal agreement (snRNA vs snATAC, Xenium vs H&E) filtering quality-driven alarms. **For the agent-trustworthiness topic**: logsumexp-type uncertainty scores can be applied to LLM token logits, and the survey lists using OOD detection against LLM hallucination as a future direction — but this paper's lesson that logit magnitude is not correctness applies too: the verifier needs its own calibration.

## Reusable assets
- **Code:** official implementation (energy score and energy-bounded fine-tuning).
<https://github.com/wetliu/energy_ood>
- **One-line score:** `-torch.logsumexp(logits, dim=1)` (T = 1) — drop-in for any kidney annotator's outputs.
- **Training recipe:** cross-entropy + 0.1 × two-margin squared hinge; set margins near the pre-trained model's mean ID/OOD energies.

## Follow-ups
- The Outlier Exposure paper (Hendrycks et al., 2019) and ReAct (Sun et al., 2021) — energy's two most common companions.
- On kidney data, test how strongly energy correlates with UMI count / mito fraction; a strong correlation means it measures quality, not disease.

## Cite
```bibtex
@inproceedings{Liu2020_201003759,
  title = {Energy-based Out-of-distribution Detection},
  author = {Liu, Weitang and Wang, Xiaoyun and Owens, John D. and Li, Yixuan},
  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS 2020)},
  year = {2020},
  eprint = {2010.03759},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2010.03759}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
