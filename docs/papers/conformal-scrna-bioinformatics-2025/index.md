# Conformal inference for reliable single cell RNA-seq annotation

> **Bibkey** `L_pez_De_Castro_2025` · **Venue** Bioinformatics (2025) · **Category** single-cell · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1093/bioinformatics/btaf521> · `status: complete`

---

## One-liner
Adds distribution-free statistical guarantees to automatic scRNA-seq annotation with conformal prediction: an **autoencoder + conformal p-values** first detects cell types absent from the reference (OOD) with false-positive rate ≤ α₀; the remaining cells get **prediction sets with coverage guarantees** (standard / classwise / cluster Mondrian taxonomies; APS / RAPS / THR non-conformity scores), where set size is the uncertainty. Departures of the conformal p-values from uniformity also diagnose broken reference–query exchangeability.

## Problem
Supervised annotators (scmap, CellTypist, etc.) usually lack reliable uncertainty; existing rejection schemes threshold softmax scores, which are often miscalibrated in neural networks and carry no guarantee. Conformal prediction gives coverage under i.i.d./exchangeability, but novel cell types in the query break that assumption and the guarantee. Only one earlier work applied conformal prediction to single-cell annotation, limited to the standard taxonomy and not handling novel types.

## Method
**Inductive conformal**: the reference is split into training and calibration sets (calibration = 40% of available training samples; another 10% held out as internal test and 15% as validation). **Module 1: OOD detector** — a feed-forward autoencoder trained on the (outlier-free) training set; reconstruction error is the non-conformity score; a new cell's conformal p-value is the fraction of calibration scores at least as large, marginally valid under exchangeability, so **marginal FPR ≤ α₀ is controlled directly**; calibration-conditional p-values (Bates et al. 2023) optionally guarantee FPR ≤ α₀ for this calibration set with probability 1−δ (less power); α₀ can be chosen automatically (Supplement S3.1). **Module 2: conformal annotator** — the base classifier is scmap, CellTypist or a feed-forward net "TorchNet", which must output softmax scores; non-conformity scores are THR, APS and RAPS (κ=1, η=0.01); a p-value is computed per class and the prediction set is all classes with p > α; the standard taxonomy gives marginal coverage, **classwise** (Mondrian) gives per-cell-type conditional coverage (unstable for rare classes), and **cluster** (k-means grouping of classes, Ding et al. 2023) is a compromise. Preprocessing: CPM + log2; TorchNet uses Seurat 2,000 HVGs + Harmony integration.

## Data
Ten batched experiments in total: **lung** — reference is a cross-tissue immune atlas (Domínguez Conde et al. 2022), queries are healthy lung (GSE178360) and lung-cancer patients (GSE127465); **pancreas** — GSE84133, four subjects in turn left out as query (4 experiments); **breast** — GSE180878, 12 prophylactic-mastectomy samples as reference and 4 reduction-mammoplasty samples as query; **mouse gastrulation** — Pijuan-Sala et al. 2019, split by two sequencing batches. QC: types with <60 cells excluded; cells with mitochondrial >10%, ribosomal >60% or haemoglobin >60% removed. Evaluation: leave-one-cell-type-out (one type removed from the reference, kept in the query), α ∈ {0.01, 0.05, 0.1}, 20 random seeds per configuration.

## Key results
- **OOD detection**: with Naive B cells as OOD (1.54% of the healthy-lung query, 1.27% of the lung-tumour query), power is high even at low significance thresholds; the FPR guarantee holds in the healthy query but **not in the tumour query** — disease breaks exchangeability. Other cell types and tissues show similar trends (Supplementary Figs S3–S7).
- **High FDR**: the rarer the OOD cells, the higher the FDR — exchangeable ID cells have uniform p-values, so some are low and swamp the few true positives.
- **Exchangeability diagnosis**: three p-value patterns — a low-p spike when OOD cells are present; a small low-p bump in the OOD-free healthy query (mild batch/biological differences); a clear departure from uniformity in the tumour query (disease-driven covariate shift).
- **Annotation coverage**: on breast, TorchNet is near nominal coverage under all three taxonomies; scmap works under classwise/cluster but fails under standard; CellTypist misses the guarantee (attributed to unaddressed technical variation in preprocessing). Coverage largely holds elsewhere; healthy lung (fully independent reference/query) deviates slightly; the tumour query deviates most.
- **Trade-offs**: standard gives the smallest sets; classwise guarantees per-class coverage with larger sets and higher CovGap for very rare classes; cluster is a compromise but becomes uninformative under very strict coverage; THR is efficient but can return empty sets (= rejection); APS/RAPS are more adaptive.
- **Failure case (pancreas)**: at very low α₀ the detector rarely flags OOD and empirical coverage falls well below nominal; the gap narrows as α₀ grows. In experiment 2, coverage stays low despite good OOD power until a larger α₀ removes a set of **exchangeability-violating ID cells**, at which point the gap closes abruptly.

## Contributions
- One conformal framework for both novel-type detection (hypothesis testing with FPR control) and uncertainty-aware annotation (prediction sets with coverage).
- A systematic comparison of three Mondrian taxonomies × three non-conformity scores × three base classifiers over 10 experiments.
- Uses uniformity of conformal p-values as a **diagnostic for exchangeability / covariate shift**.
- Prediction sets support human-in-the-loop use: singletons auto-annotated, larger sets narrowed by experts.

## Limitations
- Guarantees hold only under exchangeability, which disease queries — exactly the case we care about — break.
- High FDR when OOD cells are rare; low detection power in turn breaks annotation coverage.
- Only marginal (or per-class) coverage, not per-cell; classwise is unstable for very rare classes.
- The OOD detector is a plain autoencoder; automatic α₀ selection may stop before all OOD cells are found.
- scRNA-seq only with a limited range of base models; most quantitative results live in figures.

## Relation to our direction
This adds **statistical guarantees** to the detect stage. Most "anomalies" in this direction are continuous scores (reconstruction error, mapQC Z, Sardine likelihood); the paper shows how conformal p-values turn any anomaly score into a **test with FPR control** — directly applicable to MEATRD/STANDS-style reconstruction errors or Topic 1's own snRNA/snATAC/Xenium scores, so KidneyAnomalyBench can report FPR/power/FDR at α₀ = 0.05, not just AUROC. More important is the **negative result**: disease samples break exchangeability and shift the whole p-value distribution — so an "anomaly" can be real disease cells or a global covariate shift (batch, protocol), the same issue mapQC (`refmap-eval-biorxiv-2025`) raises; Topic 1's cross-modal agreement is a natural second criterion beyond p-values. For **Topic 2**, this is almost a single-cell prototype of a "calibrated verifier": set size = uncertainty, empty set = abstention, p-value uniformity = distribution-shift alarm; when verifying an agent's cell-annotation claims, the verifier can require conformal sets rather than single labels as evidence and lower confidence automatically when p-values look non-uniform.

## Reusable assets
- **Code** (conformalized single-cell annotator):
<https://github.com/digital-medicine-research-group-UNAV/conformalized_single_cell_annotator>
- **Archive**:
<https://doi.org/10.5281/zenodo.15870599>
- **Eval protocol**: leave-one-cell-type-out; Power/FPR/FDR (detection), coverage, CovGap, mean set size (annotation); TorchCP used for the cluster taxonomy.

## Follow-ups
- Bates et al. 2023 (conformal outlier detection, calibration-conditional p-values).
- Khatri & Bonn 2022 (first single-cell conformal annotation); Sun et al. 2024 (conformal for spatial transcriptomics).
- Weighted / covariate-shift-robust conformal methods for disease queries.
- CARA (`scatac-novel-genomeres-2026`): novel-type detection for scATAC, to compare uncertainty mechanisms.

## Cite
```bibtex
@article{L_pez_De_Castro_2025, title={Conformal inference for reliable single cell RNA-seq annotation}, volume={41}, ISSN={1367-4811}, url={http://dx.doi.org/10.1093/bioinformatics/btaf521}, DOI={10.1093/bioinformatics/btaf521}, number={10}, journal={Bioinformatics}, publisher={Oxford University Press (OUP)}, author={López-De-Castro, Marcos and García-Galindo, Alberto and González-Gomariz, José and Armañanzas, Rubén}, editor={Mathelier, Anthony}, year={2025}, month=Sept }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
