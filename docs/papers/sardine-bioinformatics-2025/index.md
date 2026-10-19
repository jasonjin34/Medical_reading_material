# Anomaly detection in spatial transcriptomics via spatially localized density comparison

> **Bibkey** `Hu_2025` · **Venue** Bioinformatics (2025) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1093/bioinformatics/btaf242> · `status: complete`

---

## One-liner
Sardine formalizes "anomalous-region detection across conditions" in spatial transcriptomics as the **spatially localized differential abundance region problem (SDARP)**: on multi-condition slices aligned to a common coordinate system, it takes a spatial neighbourhood around every spot, estimates densities on the expression-manifold kNN graph with MELD-style graph smoothing, and compares local densities between conditions — producing an interpretable anomaly score where 0.5 = no change and →1 = anomalous. It is more accurate and more spatially coherent than MELD, Vespucci and STANDS on simulations and two mouse Visium datasets.

## Problem
Disease, inflammation and drugs shift cell-type/state composition, often in spatially localized regions. Single-cell DA methods (Milo, MELD, CNA) ignore space; existing spatial methods — STANDS (GAN-based, needs histology) and Vespucci (random forests in local windows) — rely on heuristic scores. Classical spatial scan statistics (Kulldorff) target point processes and do not fit high-dimensional sparse ST data.

## Method
**Formalization**: each spot's (expression x, location s) is drawn from a per-condition joint density; assuming the conditions are **spatially registered** (identical spatial marginals), the posterior P(Z=1|x,s) depends only on the conditional expression densities f₀(x|s), f₁(x|s). Since each location has only one or two points, conditioning is done on a spatial region R: f_k(x|R). **Two components**: (i) a **spatial anomaly family** — for spot i, Rᵢ is the r nearest spots from each condition (equal counts per condition); (ii) a **plug-in density estimator** — on the kNN graph of all conditions' expression data, uniform mass is placed on that condition's points inside Rᵢ and smoothed with Laplacian regularization (as in MELD, parameters α, β) to get f̃₀(x|Rᵢ), f̃₁(x|Rᵢ). Normalizing gives a relative likelihood Q̃; the **anomaly score is the mean Q̃ over perturbed-condition spots in Rᵢ**, equal to 0.5 when densities match. Extends naturally to >2 conditions (normalize across all). Slices must first be aligned (e.g. STalign).

## Data
**Simulation**: 33×33 grid, two spatial patterns (checkerboard, spiral) × several expression distributions (d=100 multivariate normal, S-curve manifold, spiral manifold); inside the anomaly the two conditions are sampled differently. **Real data**: (1) mouse cerebral cortex before/after stab injury, Visium (Koupourtidou et al. 2024, GSE226211), 2 replicates per condition, aligned with STalign; (2) mouse lumbar spinal cord after injury plus epidural electrical stimulation (EES) rehab, Visium (Kathe et al. 2022, GSE184369), 4 conditions, 6 pairwise comparisons, grey matter only.

## Key results
- **Simulation** (β=10, knn=8, window r=30): Sardine has the lowest MSE in all 4 settings (e.g. S-curve checkerboard 0.039 vs 0.138 for MELD/Vespucci) and the highest ROC AUC in 3/4 (S-curve checkerboard 0.984 vs MELD 0.485, Vespucci 0.456; spiral-manifold checkerboard 0.985 vs 0.672 / 0.819); the one exception is multivariate-normal + spiral anomaly (0.810 vs MELD 0.817).
- **Runtime**: ~30 s per simulated dataset vs ~1 s for MELD and >20 min for Vespucci.
- **Mouse cortex stab**: Sardine's anomalous region follows the laminar cortex and covers the wound; STANDS misses the wound entirely and highlights the hippocampus. Spatial coherence (Moran's I): Sardine 0.883, Vespucci 0.825, MELD 0.259, STANDS 0.147. Sardine correlates best with reactive-astrocyte and microglia markers. Significant GSEA gene sets: Sardine 650, Vespucci 26, MELD 0, STANDS 1 — including abnormal acute inflammation (FDR 2.1×10⁻⁴) and abnormal innate immunity (FDR 4.2×10⁻⁵).
- **Spinal cord**: Sardine has the highest Moran's I in all 6 comparisons (0.715–0.913; Vespucci 0.544–0.884; MELD ≤0.101); for EESREHAB vs EESREHAB-walking, significant GSEA sets are Sardine 88, Vespucci 4, MELD 0 (e.g. impaired synaptic plasticity FDR 0.007). Joint multi-condition likelihoods have Moran's I 0.841–0.910.

## Contributions
- First rigorous formulation of ST anomaly detection as a local two-sample / density-comparison problem (SDARP), bridging single-cell DA theory and spatial scan statistics.
- The anomaly score has a probabilistic meaning (0.5 = no difference), interpretable across methods and conditions, without a binary classifier.
- Modular: both the spatial anomaly family and the density estimator are swappable; native multi-condition support.
- Needs no histology — only expression plus registered coordinates.

## Limitations
- **Requires slices from different conditions registered to one coordinate system**; many aligners assume expression correspondence, which may be too strong across conditions (exactly where anomalies exist) — the authors suggest joint alignment + detection.
- No spot-level ground truth on real data; evaluation uses indirect proxies (Moran's I, marker correlation, GSEA hit counts) — spatial coherence is not correctness.
- Validated only on mouse Visium (55 µm spots); single-cell resolution (Xenium, etc.) may need re-tuning or new anomaly families.
- Requires control-condition slices — a case-vs-control comparison, not reference-free detection on a single patient slice.

## Relation to our direction
Sardine is the **spatial statistical baseline** for the detect stage: it continues the Milo-DA logic of Dann et al. (`healthy-ref-natgenet-2023`) but moves the neighbourhood from expression space to physical space, and contrasts with deep reconstruction/discriminative methods like STANDS (`spatial-natcommun-2024`) and MEATRD (`meatrd-aaai-2025`), which need histology while Sardine does not. For **Plan A**: on in-house Xenium (plus KPMP spatial data), Sardine can serve as the "image-free, probabilistically meaningful" baseline in KidneyAnomalyBench; its 0.5 neutral point is convenient for **cross-modal agreement** against snRNA / snATAC anomaly scores (a region deviating from 0.5 in several modalities counts as disease; deviation in only one is more likely artifact). Caveat for kidney biopsies: registering biopsies from different patients is far harder than mouse brain sections (sampling site, cortex/medulla ratio), and registration error would be scored as anomaly — a failure mode Plan A must test explicitly. For **Plan B**: the evaluation itself is a cautionary case — "higher Moran's I + more GSEA hits = more plausible" is indirect evidence; if an agent claims "anomalous region found" on such proxies, a calibrated verifier should lower confidence and ask for ground-truth validation.

## Reusable assets
- **Code** (Python 3):
<https://github.com/raphael-group/spatial_anomaly_detection>
- **Data**: mouse cortex stab GSE226211; spinal cord injury GSE184369.
- **Eval protocol**: synthetic-manifold ST simulations (checkerboard/spiral × normal/S-curve/spiral), AUROC + MSE against 0.5/1 targets, Moran's I and GSEA on real data.

## Follow-ups
- The Vespucci (Teo et al. 2024) and MELD (Burkhardt et al. 2021) papers.
- Landa et al. 2020 local two-sample testing (the statistical basis, Supplement S4).
- STalign and other cross-condition aligners, and follow-ups on joint alignment + anomaly detection.
- Test Sardine on single-cell-resolution Xenium kidney tissue.

## Cite
```bibtex
@article{Hu_2025, title={Anomaly detection in spatial transcriptomics via spatially localized density comparison}, volume={41}, ISSN={1367-4811}, url={http://dx.doi.org/10.1093/bioinformatics/btaf242}, DOI={10.1093/bioinformatics/btaf242}, number={Supplement_1}, journal={Bioinformatics}, publisher={Oxford University Press (OUP)}, author={Hu, Gary and Gold, Julian and Chitra, Uthsav and Joshi, Sunay and Raphael, Benjamin J}, year={2025}, month=July, pages={i493–i501} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
