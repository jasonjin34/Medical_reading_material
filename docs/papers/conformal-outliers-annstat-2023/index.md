# Testing for Outliers with Conformal p-values

> **Bibkey** `Bates2021_210408279` · **Venue** The Annals of Statistics (2023) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1214/22-AOS2244> · `status: complete`

---

## One-liner
Turns the output of **any** one-class classifier / anomaly scorer into a p-value per test point via split-conformal calibration, and studies these p-values from a **multiple-testing** perspective: classical (marginal) conformal p-values are mutually dependent but PRDS, so Benjamini–Hochberg (even with Storey's correction) still controls the FDR exactly, while Fisher's combination test breaks; it then constructs **calibration-conditionally valid (CCV)** p-values — valid with probability 1−δ for *this* calibration set and mutually independent — and, as a by-product, a simultaneous upper confidence bound on the FPR of any outlier-detection algorithm.

## Problem
Given 2n clean (outlier-free) samples from an unknown P_X, decide which of n_test new independent observations are outliers (not from P_X). One-class classifiers produce scores but no null distribution, no threshold and no guarantee. Conformal inference turns scores into p-values, but: (1) with many test points one needs **FDR** control (the expected fraction of true inliers among reported outliers) — yet classical conformal p-values are only valid **marginally over the calibration set**, and p-values of different test points are dependent through the shared calibration set, whereas FDR procedures usually need independence or specific dependence; (2) for a practitioner with **one** expensive calibration set, "valid on average" is unsatisfying — an unlucky calibration set can make inferences systematically invalid; (3) batch-level global tests ("does this batch contain any outlier?") also need independent p-values.

## Method
**Setup**: split clean data into D_train (fit the scorer ŝ; small score = more outlying) and D_cal (n calibration points); the marginal conformal p-value is û_marg(x) = (1 + #{i ∈ D_cal : ŝ(X_i) ≤ ŝ(x)}) / (n+1), with P[û ≤ t] ≤ t for inliers. **Negative result**: Lemma 1 — for any two inlier test p-values under any transform, the correlation is exactly 1/(n+2); Theorem 1 — with m = γn test points, Fisher's combination test has marginal type-I error → Φ̄(z_{1−α}/√(1+γ)): 20.5% at α = 5%, γ = 3, approaching 50% as γ → ∞; the 90th percentile of the conditional type-I error is 71.7% at γ = 3. A corrected valid critical value is given (Eq. 6). **Positive results**: Theorem 2 — marginal conformal p-values are **PRDS** on the inliers, so BH at level α controls FDR ≤ π₀α (Corollary 1); Theorem 3 — BH with Storey's correction (λ = K/(n+1)) also controls FDR ≤ α (via a new FDR bound). **CCV p-values**: Theorem 4 — if b₁ ≤ … ≤ b_n satisfy P[U_(1) ≤ b₁, …, U_(n) ≤ b_n] ≥ 1−δ for uniform order statistics, adjusting with a piecewise-constant h, û_ccv = h(û_marg), gives P[ P[û_ccv ≤ t | D] ≤ t for all t ] ≥ 1−δ. Three constructions of b: the **generalized Simes inequality** (k = n/2), an **asymptotic** one (empirical-process based), and **Monte Carlo** (simulating uniform order statistics; finite-sample valid and usually the most powerful); DKWM is compared and is looser. CCV p-values are independent given the calibration set, so any independence-assuming multiple-testing procedure applies. **Extensions**: the same bound yields an FPR upper confidence bound **simultaneous over all thresholds t** (Proposition 3), and prediction sets valid simultaneously for all α.

## Method lineage
**Paradigm: conformal / calibrated.** It proposes no new anomaly score; it **wraps any score** (one-class SVM, isolation forest, LOF, or any deep AD/OOD score). It builds on split-conformal inference (Vovk et al.), earlier conformal outlier-detection work, the PRDS theory of BH/Benjamini–Yekutieli, Storey's correction and the tolerance regions of Wilks/Tukey; closest is Vovk (2012) on the conditional validity of inductive conformal predictors (calibration-conditional coverage), but here the bounds hold **simultaneously for all levels**. **Afterwards**: in this repo, `conformal-scrna-bioinformatics-2025` applies it to single-cell annotation — autoencoder reconstruction error as the non-conformity score, conformal p-values to detect cell types absent from the reference, optionally with this paper's calibration-conditional p-values. The survey (`generalized-ood-survey-ijcv-2024`) names the conformal–OOD intersection an emerging direction.

## Data
**Simulation**: a Gaussian mixture in R⁵⁰, X = √a·V + W (a = 1 inliers, a > 1 outliers); per practitioner n_train = 1000, n_cal = 1000; J = 100 independent datasets × L = 100 test sets; scorer = one-class SVM. **Real benchmarks** (isolation forest, contamination = 0.1; one-class SVM and LOF in the appendix): ALOI (d = 27; 283,301 inliers / 1,508 outliers), Cover (10; 286,048 / 2,747), Credit card (30; 284,315 / 492), KDDCup99 (40; 47,913 / 200), Mammography (6; 10,923 / 260), Digits (16; 6,714 / 156), Shuttle (9; 45,586 / 3,511).

## Key results
- **Theory**: Fisher's combination with marginal conformal p-values has marginal type-I error 20.5% at α = 5%, γ = 3; BH and Storey-BH control FDR exactly in the marginal sense; CCV p-values are valid for the given calibration set with probability 1−δ.
- **Simulation** (BH, nominal FDR 0.1, δ = 0.1): CCV p-values keep the conditional FDR controlled for at least 90% of "practitioners"; marginal p-values do not (unless the calibration set is very large); Monte Carlo and Simes adjustments are slightly more powerful than the asymptotic one; all methods control the marginal FDR. Batch detection (batches of 10, Fisher combination + Storey-BH) gives the same picture.
- **Real data** (nominal FDR 0.2, isolation forest + Storey-BH; 90th percentile of the conditional FDR, marginal vs conditional): Credit card 0.228 vs 0.202, KDDCup99 0.23 vs 0.168, Mammography 0.286 vs 0.17, Digits 0.266 vs 0.173, Shuttle 0.228 vs 0.198, Cover 0.297 vs 0.148 — marginal calibration's 90th percentile exceeds the nominal level throughout; the price is power, e.g. Digits mean power 0.417 → 0.096 and Mammography 0.176 → 0.059, while Shuttle loses almost nothing (0.981 vs 0.98). Isolation forest has essentially no power on ALOI (0).

## Contributions
(1) The first systematic study of conformal outlier p-values under multiple testing: dependence (1/(n+2)), failure of Fisher, PRDS ⇒ valid BH, valid Storey-BH; (2) CCV p-values valid with high probability for the given calibration set, simultaneously over all levels, and mutually independent (Simes / asymptotic / Monte Carlo adjustments); (3) finite-sample guarantees via concentration inequalities rather than combinatorial arguments; (4) a simultaneous FPR confidence band for any black-box detector; (5) an open-source Python package.

## Limitations
Requires calibration points and test inliers to be **exchangeable and mutually independent** (the high-probability bounds need i.i.d.) — the premise of every guarantee; only split-conformal is studied (sample splitting costs data efficiency), with jackknife+ or bootstrap left for future work; CCV's stronger guarantee costs power (pronounced on Digits, Mammography); power depends entirely on the base scorer (zero on ALOI) — conformal guarantees validity, not detection ability; structured (mutually dependent) outliers are only discussed.

## Relation to our direction
**This is the statistical layer that turns any Topic-1 anomaly score into "a discovery list with an error-rate guarantee".** Mapping: inliers = cells/spots/H&E patches from a healthy reference (KPMP, the Lake atlas, HuBMAP normal kidney, or normal controls within the cohort under test); D_train fits any scorer (STANDS / MEATRD reconstruction error, Mahalanobis distance, energy, mapQC distance), D_cal provides calibration scores; compute a conformal p-value for every cell in a disease biopsy and run BH across thousands of cells to **control the FDR** — the output is a list of anomalous cells whose FDR has a precise meaning, a natural statistical endpoint for KidneyAnomalyBench. **Batch detection** maps to "does this biopsy / this niche contain any anomalous cell?": the paper shows that Fisher-combining marginal p-values is **invalid** and that CCV p-values or a corrected critical value are needed — crucial for sample-level claims. **The CCV guarantee** matches reality: in practice there is often only one calibration set (one healthy reference), and this paper's guarantee is for *that* reference. **Which assumptions break**: (1) **exchangeability** — calibration cells come from healthy donors, test cells from new donors / batches / platforms; batch effects themselves violate exchangeability, making p-values anti-conservative, so **batch effects get reported as discoveries**; (2) **independence** — cells from one donor and spatially adjacent spots are correlated, while the CCV bounds need i.i.d.; testing after aggregating by donor or niche may be more appropriate; (3) "healthy" cells inside disease biopsies are not strictly from P_X; (4) differing cell-type composition → calibrate per cell type (Mondrian); (5) with **continuous disease states** many cells are mildly shifted, and "outlier = not from P_X" does not coincide with "biologically meaningful anomaly"; (6) doublets, ambient RNA and segmentation errors are also "not from P_X" — conformal will **correctly** report them, so it cannot separate artifact from disease; that step still needs Topic 1's cross-modal agreement. **Direct use in the repo**: `conformal-scrna-bioinformatics-2025` uses autoencoder + conformal p-values to detect out-of-reference cell types with FPR ≤ α₀ and explicitly offers this paper's calibration-conditional p-values (at a cost in power); it also uses departures of the p-values from uniformity to diagnose broken reference–query exchangeability — a ready tool for detecting batch effects. `refmap-eval-biorxiv-2025` (mapQC) builds Z-scores against a null of reference inter-sample distances, a non-conformal version of the same "reference as null" idea; `healthy-ref-natgenet-2023` uses Milo's spatial FDR for neighbourhood-level tests. **For Topic 2**: the calibrated verifier can adopt this framework directly — calibrate verifier scores on a human-checked set of correct claims, compute conformal p-values for the many claims an agent produces, and run BH to control the fraction of false alarms among claims flagged as unsupported; the simultaneous FPR band lets one pick a threshold after the fact without losing the guarantee; and the CCV "single calibration set" view matches benchmark settings like AIRIS WP3 / MLCommons where only one benchmark exists.

## Reusable assets
- **Code:** the authors' Python package (marginal and CCV conformal p-values, with reproduction notebooks).
<https://github.com/msesia/conditional-conformal-pvalues>
- **Formulae:** û_marg = (1 + #{calibration scores ≤ test score})/(n+1); BH or Storey-BH controls FDR; for conditional guarantees use the Monte Carlo CCV adjustment (δ = 0.1).
- **Evaluation design:** the "J practitioners × L test sets" distribution of conditional FDR / power (look at the 90th percentile, not the mean) — good for assessing how stable kidney anomaly calls are across reference draws.

## Follow-ups
- Angelopoulos & Bates, "A gentle introduction to conformal prediction" — the practical primer.
- Weighted / covariate-shift conformal (for batch effects that break exchangeability) and Mondrian (per-cell-type) conformal.
- On KPMP: split training/calibration by donor and check whether conformal p-values stay near-uniform across donors.

## Cite
```bibtex
@article{Bates2021_210408279,
  title = {Testing for Outliers with Conformal p-values},
  author = {Bates, Stephen and Cand{\`e}s, Emmanuel and Lei, Lihua and Romano, Yaniv and Sesia, Matteo},
  journal = {The Annals of Statistics},
  volume = {51},
  number = {1},
  pages = {149--178},
  year = {2023},
  doi = {10.1214/22-AOS2244},
  eprint = {2104.08279},
  archivePrefix = {arXiv},
  url = {https://doi.org/10.1214/22-AOS2244}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
