# Automated evaluation of single-cell reference atlas mappings enables the identification of disease-associated cell states

> **Bibkey** `Sikkema_2025` · **Venue** bioRxiv (2025) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1101/2025.05.23.655749> · `status: complete`

---

## One-liner
MapQC (Theis lab) uses the **healthy reference atlas's own inter-sample variation as a null distribution** to judge whether a query→reference mapping succeeded: query control samples should sit at a "normal" distance from the reference (mapQC score < 2), and case samples should be "abnormally" distant in some cells (> 2). It catches residual batch effects invisible in UMAPs, prevents artifacts from being reported as disease states, and is more interpretable than repurposed integration metrics (LISI, kBET, etc.).

## Problem
Mapping disease/perturbation queries onto healthy reference atlases (scArches, Symphony, Azimuth) is standard practice, but success cannot be predicted in advance (dissociation protocol, assay, mapping parameters). Failures come in two kinds: **under-integration** (residual batch effects; artifacts read as disease states) and **over-integration** (disease signal erased). Existing metrics either check preservation of the query's own structure (at odds with the point of mapping) or are integration metrics such as LISI and kBET, which lack absolute thresholds — and all ignore that **healthy populations themselves vary between samples**.

## Method
Two assumptions: (A1) the healthy atlas covers most variation in the healthy population; (A2) disease differs from health in at least some cell types. These yield two testable hypotheses: (H1) query controls should be as similar to reference samples as reference samples are to each other; (H2) case samples should be less similar in some cell types. **Computation**: sample random centre cells in the integrated embedding and form large neighbourhoods; within each, compute inter-sample **energy distance (E-distance)**; a sample's distance to the reference is its mean distance to all reference samples (for reference samples, same-dataset samples are excluded to avoid within-dataset bias); **Z-score** against the neighbourhood's null distribution of reference samples' own distances (outliers beyond 3.5×IQR removed); a cell's mapQC score is its sample's mean normalized distance across all neighbourhoods containing it. **Reading**: > 2 means distant from the reference (residual batch or out-of-reference biology). Successful mapping = controls mostly < 2 while some case cells > 2; controls also > 2 → under-integration; cases as close as controls → over-integration. Wasserstein distance (>48 h per mapping, infeasible) and mean pairwise distance (variance-confounded) were tried before settling on E-distance.

## Data
(1) An IPF dataset (5 IPF patients, 6 controls) mapped to the Human Lung Cell Atlas (HLCA); (2) an Asherman syndrome (AS) endometrial dataset (6 healthy, 9 AS donors) mapped to the Human Endometrial Cell Atlas (HECA). Mapping via scArches.

## Key results
- **IPF → HLCA (default mapping)**: many query control cells score > 2, indicating residual batch effects invisible in the UMAP (e.g. blood-vessel endothelium). Standard clustering of endothelial cells yields a "disease-specific" cluster whose DEGs are mostly experimental artifacts: ambient RNA (B-cell-derived IGKC, IGHA1), dissociation stress (FOSB), ribosomal proteins (RPS4Y1).
- **AS → HECA**: 93.9% of query control cells score < 2, but two query-dominated clusters (94% and 97% query cells) stay > 2, and cluster 21 holds 74% of the "AS epithelium" cells reported in the original study. Further analysis shows low-quality cells (low total counts, no specific markers, low MALAT1 in cluster 25, doublet-like stroma + epithelium co-expression in disease cells) — i.e. **the originally reported disease-specific state is likely a low-quality-cell / doublet artifact**.
- **Improving the mapping**: fraction of query control cells > 2: original 28.4%; max KL weight 2 → 100%, 0.1 → 49.1% (both worse); batch covariate sample instead of dataset → 17.1%; plus recovering 69 input genes lost during gene-annotation harmonization → 9.3%. In this mapping, 23.7% of IPF cells score > 2 (vs 9.3% of controls).
- **Disease states in the successful mapping**: smooth muscle cells score high in 26% of IPF vs 2% of control cells, with specific genes (IGFBP2, FAM162B, CCL21, etc.) replicated in other IPF datasets; SPP1hi alveolar macrophages are correctly flagged as disease-specific (invisible in UMAP); the originally reported CTHRC1hi fibroblasts map close to the reference — 7 healthy reference donors have mean CTHRC1 ≥ the IPF donors — showing that a larger healthy population corrects false calls.
- **Against existing metrics**: cluster preservation, wiq-kNN-corr and donor LISI barely differ between the best and worst mappings (in the worst, query controls separate fully even in the UMAP and mapQC flags 100% as distant); kBET gives near-minimal scores for almost all cells in both (oversensitive); batch LISI shifts dramatically when query cells are downsampled to 1% or 10%, while mapQC stays largely stable.

## Contributions
- First mapping-quality metric to explicitly model **natural inter-sample variation in the healthy population**, with an absolute, interpretable threshold (Z > 2).
- Neighbourhood-level nulls: normal variation differs by cell type/state, so normalization is local.
- Control test (under-integration) and case test (over-integration) judge success in both directions; mapping-method-agnostic, cell-level resolution.
- Concretely shows that published "disease-specific states" can be artifacts (AS epithelium, CTHRC1hi fibroblasts).

## Limitations
- Requires query control samples generated with the same protocol as the cases.
- Assumes the reference covers the query population's healthy variation — only true for large atlases; if the reference covers a subpopulation (e.g. European ancestry only), biology is confused with batch.
- Strong batch effects inside the reference inflate the null and mask query batch effects of similar strength.
- Assumes control and case batch effects in the query are of similar size; full confounding cannot be solved by any data-driven metric.
- Only two case studies (lung, endometrium); the Z>2 threshold relies on an approximately Gaussian null; preprint, not peer reviewed.

## Relation to our direction
This is **one of Plan A's key "artifact vs disease" tools** and a direct continuation of the ACR design in Dann et al. (`healthy-ref-natgenet-2023`): mapQC is essentially a sample-level anomaly score with the healthy atlas as its null (> 2 = anomalous), and its main contribution is to show that **such an anomaly can come from batch / ambient RNA / dissociation stress / doublets rather than disease**, with the control test to tell them apart. Plan A can map the in-house 95-biopsy snRNA onto the Lake kidney atlas / KPMP reference and use mapQC to check that controls (KPMP reference tissue or in-house normal tissue) look normal; this paper's artifact gene list from the IPF endothelial cluster (IGKC, IGHA1, FOSB, RPS4Y1) and the low-quality-cell signatures from AS (low counts, low MALAT1, dual-lineage co-expression) can become KidneyAnomalyBench's **artifact classes** and negative labels. Combined with cross-modal agreement: a population with mapQC > 2 in snRNA but no matching anomaly in snATAC / Xenium is more likely an artifact. For **Plan B**: "a published disease-specific state was actually an artifact" is exactly what claim-to-evidence verification should catch — when an agent claims a disease state, the verifier should demand mapQC-style control-test evidence; mapQC's Z-score is also a naturally calibratable confidence signal and a candidate input feature for a calibrated verifier.

## Reusable assets
- **mapQC package**:
<https://github.com/theislab/mapqc>
- **Reproducibility code**:
<https://github.com/theislab/mapqc_reproducibility/tree/v0.1.0-manuscript>
- **Decision rule**: controls < 2 & some cases > 2 = success; controls > 2 = under-integration; cases ≈ controls = over-integration.
- **Artifact markers**: ambient RNA (IGKC, IGHA1), dissociation stress (FOSB), ribosomal (RPS4Y1), low counts / low MALAT1 / dual-lineage co-expression.

## Follow-ups
- Dann et al. 2023 (`healthy-ref-natgenet-2023`) — the basis for "a few matched controls sharply reduce false positives."
- Ambient-RNA decontamination benchmark (`ambient-rna-bench-biorxiv-2026`): re-test mapQC after decontamination.
- Run mapQC on kidney references (Lake atlas, KPMP) to find cell types that integrate poorly by default (like NK/T cells in HLCA).
- Watch whether the published version extends to ATAC / spatial data.

## Cite
```bibtex
@article{Sikkema_2025, title={Automated evaluation of single-cell reference atlas mappings enables the identification of disease-associated cell states}, url={http://dx.doi.org/10.1101/2025.05.23.655749}, DOI={10.1101/2025.05.23.655749}, journal={bioRxiv}, publisher={Cold Spring Harbor Laboratory}, author={Sikkema, Lisa and Lkandushi, Mariam and Scarcella, Daniele and Moinfar, Amir Ali and Engelmann, Jan and Theis, Fabian J.}, year={2025}, month=May }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
