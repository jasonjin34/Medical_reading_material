# A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks

> **Bibkey** `Hendrycks2016_161002136` · **Venue** International Conference on Learning Representations (ICLR 2017) (2017) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/1610.02136> · `status: complete`

---

## One-liner
The founding paper of OOD detection: a trained classifier's **maximum softmax probability (MSP)** is not a usable confidence on its own (an MNIST classifier assigns 91% "confidence" to Gaussian noise), but correctly classified examples have statistically higher MSP than misclassified and out-of-distribution ones, so thresholding MSP detects errors and OOD inputs across vision, NLP and speech. The authors also define standard tasks and metrics (AUROC plus two AUPRs) and show with an "auxiliary decoder + abnormality module" that the baseline can be beaten.

## Problem
Classifiers deployed under train–test distribution mismatch often **fail silently**, producing confident wrong answers; the authors' own example is medical diagnosis, where a model confidently classifies hard cases that should be flagged for a human. Two related problems: (1) **error/success prediction** — can we predict whether the classifier will be wrong on a given test example; (2) **in-/out-of-distribution detection** — can we tell whether a test example comes from a different distribution than the training data. Because softmax uses the fast-growing exponential, small logit changes cause large output changes, so softmax rarely outputs a uniform distribution on OOD inputs.

## Method
**Baseline**: for each test example take the softmax probability of the predicted class (MSP) as the score. For error detection, correct vs misclassified examples are compared; for OOD detection the in-distribution test set is the positive class and OOD examples the negative class (or scores are negated to treat anomalies as positive). KL divergence of the softmax from uniform was also tried and was highly correlated with MSP. **Evaluation**: accuracy is rejected in favour of threshold-free **AUROC** and **AUPR**, reported both with success/in-distribution as positive (AUPR Succ / AUPR In) and with error/OOD as positive (AUPR Err / AUPR Out), alongside a random-detector "Base" value because AUPR depends on the positive-class rate. All AUROCs differ from random with high significance (Wilcoxon rank-sum). For speech (CTC), softmax is computed **ignoring the blank symbol's logit**, which otherwise dominates most time steps. **Abnormality module**: an auxiliary decoder reconstructing the input is trained jointly with the classifier on in-distribution data; these layers are then frozen and a small sigmoid-output network is trained to separate clean examples from **synthetically noised** ones (white/brown/pink noise for TIMIT; blur, rotation, Gaussian noise for MNIST).

## Method lineage
**Paradigm: classifier-based OOD.** It builds directly on empirical observations that softmax confidence is unreliable (Nguyen et al.), and became the default baseline of nearly every later OOD paper: ODIN (temperature scaling + input perturbation), Mahalanobis (`mahalanobis-ood-neurips-2018`, moving to feature-space density), the energy score (`energy-ood-neurips-2020`, which shows log-MSP is a shifted free energy), Outlier Exposure (Hendrycks' own follow-up), and the OpenOOD benchmark (`generalized-ood-survey-ijcv-2024`, which names MSP as the field's origin). The Section-4 abnormality module — a "normal vs abnormal" discriminator trained with synthetic noise as negatives — is an early form of the later **synthetic-anomaly / self-supervised** branch (e.g. DRAEM), and the auxiliary decoder has a **reconstruction** flavour.

## Data
**Vision**: MNIST (3-layer, 256-wide MLP, GELU) and CIFAR-10/100 (40-4 Wide ResNet); OOD = SUN scenes, Omniglot, notMNIST, greyscale CIFAR-10, Gaussian and uniform noise. **NLP**: IMDB sentiment (OOD: Customer Review, Movie Review); 20 Newsgroups / Reuters 8 / Reuters 52 topic classification with held-out subjects as OOD (15/5, 6/2, 40/12); WSJ and Twitter POS tagging (OOD: tweets, English Web Treebank weblogs). **Speech**: TIMIT (bidirectional LSTM + CTC), OOD = TIMIT mixed with Aurora-2 noises (airport, babble, car, …; 30% noise volume, mean SNR ≈ 5) and the Chinese THCHS-30 corpus.

## Key results
- **Error detection** (AUROC, random = 50): MNIST 97, CIFAR-10 93, CIFAR-100 87, while misclassified examples still have mean MSP of 86% / 80% / 66% — MSP alone is a misleading confidence. IMDB 82; 15 Newsgroups 89, Reuters 6 89, Reuters 40 91; WSJ 96, Twitter 89.
- **OOD detection** (AUROC): CIFAR-10/SUN 95, CIFAR-10/Gaussian 97, CIFAR-100/SUN 91, CIFAR-100/Gaussian 88; MNIST/Omniglot 96, /notMNIST 85, /Uniform 99. IMDB/All 94; 15/5 Newsgroups 75 (hardest), Reuters40/12 95; WSJ/Twitter 80, WSJ/Weblog 61 (weblogs are stylistically close to newswire and nearly undetectable); noised TIMIT 98–100, TIMIT/Chinese 85.
- **Abnormality module**: on TIMIT with a fully connected net (noise only raises frame error from 29.69% to 30.43%, so softmax barely helps) mean AUROC rises from 80 (softmax) to 97; on MNIST from 93 to 100. The module was trained on noise types different from the test distortions and still generalized.

## Contributions
(1) Formalizes error detection and OOD detection as two standard tasks with a simple, cross-domain MSP baseline; (2) sets the evaluation norm: AUROC + both AUPRs + random baselines + reporting the underlying classifier's accuracy (an always-wrong classifier gets maximal AUPR with errors as positives); (3) urges testing across tasks and architectures, not vision only; (4) shows via the abnormality module that the baseline can be beaten, opening the field.

## Limitations
MSP needs a trained classifier and only reads the output layer — OOD points far from the decision boundary can still get high MSP (the opening that the Mahalanobis and energy papers exploit). Near-OOD (stylistically similar weblogs, related news topics) is weak (AUROC 61–75). Early OOD sets may contain images of ID classes, distorting evaluation (the survey flags exactly this). The abnormality module depends on the chosen synthetic noise and is shown only on TIMIT and MNIST. All experiments use small circa-2016 models.

## Relation to our direction
**Mapping onto kidney omics**: samples = single cells or Visium/Xenium spots; the "classifier" = a cell-type annotator trained on a healthy reference (KPMP / the Lake atlas / HuBMAP normal kidney) — scANVI, CellTypist, or an MLP on the scVI latent — or a patch-level tissue classifier on H&E. Low MSP = "this cell resembles no reference class", i.e. a candidate anomaly / novel state. It is the cheapest Plan-A detect baseline, available for free from any annotation pipeline. **Which assumptions break**: (1) **continuous disease states** — kidney injury is a continuum PT → aPT/injured PT → failed repair; intermediate cells sit between classes, so low MSP reflects **class ambiguity**, not novelty — MSP conflates aleatoric ambiguity with genuine OOD; (2) **doublets** are mixtures of two classes and get low MSP — flagged as "anomalous" although they are technical artifacts; (3) **ambient RNA / low-quality cells** also depress MSP; (4) **batch effects** rescale logits, so normal cells from a new donor can score low. Used alone, MSP will report artifacts as disease — precisely why Plan A uses **cross-modal agreement** (do snRNA and snATAC, or Xenium and H&E, both fire?) to separate artifacts from disease; MSP serves as a per-modality baseline score. **Directly reusable**: the paper's evaluation norm — AUROC + AUPR-Out (anomaly as positive, since anomalies are rare) + random baselines + reporting annotator accuracy — should go verbatim into the KidneyAnomalyBench protocol; the error-detection half maps to "flag cells the annotator likely mislabelled". **Repo papers already adapting the idea**: `conformal-scrna-bioinformatics-2025` explicitly criticizes thresholding softmax scores as guarantee-free and uses conformal p-values instead; `histo-nejmai-2024`'s best method is the anomaly-class probability of an Outlier Exposure binary classifier (a trained version of the MSP idea); `scatac-novel-genomeres-2026` (CARA) flags out-of-reference novel types. **For Plan B**: MSP is the archetype of "use the model's own confidence as the verifier signal", and its core lesson — raw confidence is uncalibrated (91% on noise) — carries over to agents' / LLMs' self-reported confidence, supporting Plan B's need for a **separately calibrated verifier** rather than trusting agent confidence.

## Reusable assets
- **Code:** the authors' experiment code.
<https://github.com/hendrycks/error-detection>
- **Eval protocol:** AUROC + AUPR-In/Out (or Succ/Err) + random baselines + underlying classifier accuracy; Wilcoxon rank-sum test.
- **Baseline implementation:** MSP has a standard implementation in OpenOOD — a zero-cost baseline for any kidney annotator.
<https://github.com/Jingkang50/OpenOOD>

## Follow-ups
- ODIN (Liang et al., temperature scaling + input perturbation) and Outlier Exposure (Hendrycks et al., 2019) — not yet in the repo; the latter is the core of `histo-nejmai-2024`.
- Train an annotator on the KPMP healthy reference and measure MSP AUROC separately for doublets, low-quality cells and aPT states, quantifying how much artifact is mistaken for anomaly.

## Cite
```bibtex
@inproceedings{Hendrycks2016_161002136,
  title = {A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks},
  author = {Hendrycks, Dan and Gimpel, Kevin},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2017},
  eprint = {1610.02136},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1610.02136}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
