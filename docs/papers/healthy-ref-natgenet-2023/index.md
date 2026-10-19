# Precise identification of cell states altered in disease using healthy single-cell references

> **Bibkey** `Dann_2023` · **Venue** Nature Genetics (2023) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41588-023-01523-7> · `status: complete`

---

## One-liner
When using a "healthy reference" to find disease-altered cell states, which reference should you use? The authors give a systematic answer: **learn the latent space on a large healthy atlas (scVI + scArches mapping), then run differential-abundance testing (Milo) against matched controls only** — the ACR (atlas-to-control reference) design. It beats atlas-only (false positives explode) and control-only (misses multiple altered states), and with an atlas available, the number of controls can be cut without inflating FDR.

## Problem
The standard workflow integrates disease and healthy data in one latent space and then runs differential analysis on matched cell states. Reference choice is crucial but under-studied: Human Cell Atlas-scale atlases cover many states but differ from disease cohorts in demographics and protocols, risking confounded false positives; matched controls are hard to collect, few in number, and when used for integration can miss rare states and overfit sample noise. Can an atlas replace controls, and how should the two be combined?

## Method
Three-step workflow: (1) train a dimensionality-reduction model (scVI, 5,000 HVGs, n_latent=30) on an "embedding reference"; (2) map the query (incl. disease samples) into that latent space with scArches transfer learning; (3) run neighbourhood-level differential abundance (DA) with Milo (10% spatial FDR). Three reference designs are compared: **AR** (atlas for both embedding and DA), **CR** (control for both; split into CR scArches with query mapping and CR scVI trained jointly on concatenated control+disease), and **ACR** (atlas for embedding, control for DA). Ground truth comes from **out-of-reference (OOR)** simulations: from healthy PBMCs of 13 studies / 1,248 donors, one study is split at random into pseudo-disease (16 donors) and control (13 donors), the other 12 studies (1,219 donors, 513,565 cells) form the atlas; one cell type is removed from control and atlas so it becomes a disease-specific OOR state. A "mixed OOR" scenario removes classical monocytes plus a PCA-split "shifted" OOR state. Alternative criteria (latent distance, label-transfer uncertainty) are compared in Supplementary Note 2.1.

## Data
Simulation: 13 healthy-PBMC 10x studies from CELLxGENE, downsampled to 500 cells/sample, ~597k high-quality cells, 16 cell types (atlas 513,565 / control 5,671 / pseudo-disease 7,505 cells), 15 OOR states tested. Real data 1: COVID-19 PBMC cohort (90 patients, 23 healthy volunteers; 48,083 disease, 14,426 control cells) plus a 12-study, 1,219-donor PBMC atlas. Real data 2: idiopathic pulmonary fibrosis (IPF) lung parenchyma scRNA-seq (32 IPF, 28 control, 18 COPD; 144,404 IPF, 95,303 control cells) plus the core Human Lung Cell Atlas (HLCA, 584,844 cells).

## Key results
- **Single OOR state**: ACR sensitively detects neighbourhoods with high OOR fraction; AR inflates false positives (significant even where the OOR fraction is 0); CR scArches has higher FDR than ACR; CR scVI is comparable to ACR. Integration quality barely differs across designs; conclusions hold with other DA methods; all methods need roughly ≥250 cells per cell type to detect an OOR state.
- **CR scVI's good showing is driven by feature selection**: HVGs chosen on control+disease include OOR markers; when HVG source is controlled, only CR scVI drops substantially (control+disease HVGs overlap 81% with control-only and 68% with atlas-only on average). In the **multiple-OOR** simulations ACR is best.
- **Robustness**: ACR beats CR as the control cohort shrinks (t-test on AUPRC distributions P < 0.01); ACR sensitivity is stable once the atlas has ≥~10,000 cells; without controls performance depends more on atlas size (AUPRC–size R² = 0.69 for AR vs 0.4 for ACR), and AR's FPR rises with smaller atlases.
- **COVID-19**: ACR correlates DA logFC more strongly with the mean IFN signature (Pearson R 0.63 vs CR 0.52; Fisher z P < 2.2×10⁻¹⁶); it separates IFNhi and IFNlo COVID-associated CD14⁺ monocyte states: IFNhi most prominent in mild/asymptomatic (vs healthy, Wilcoxon P = 1.19×10⁻⁷), IFNlo (HLA-DRlo S100Ahi dysfunctional monocytes) dominant in moderate-to-critical disease; CR cannot separate normal IFNlo from severe IFNlo.
- **IPF**: ACR beats AR/CR in detecting profibrotic SPP1⁺ macrophages and diagnostic-signature-high stromal/epithelial states; CR wrongly prioritizes neighbourhoods with significantly fewer samples (residual batch effects). ACR separates two distinct aberrant states in parenchyma — KRT5⁺KRT17hi aberrant basal cells vs KRT5⁻KRT17⁺ basaloid cells — with 981 DEGs (FDR 5%), some of which are drug targets in trials (e.g. CSF2, CCL2).

## Contributions
- Splits "how to use a healthy reference" into two independent choices — embedding reference vs DA reference — and gives a clear ACR recommendation.
- An OOR simulation framework built by splitting real data, preserving real donor/library effects — a ground-truth benchmark for disease-state detection.
- Quantifies how atlas size, control count and HVG selection drive false positives, giving cohort-design guidelines (fewer controls needed when an atlas exists).
- Advocates that atlas builders share trained embedding models for scArches-style mapping.

## Limitations
- Relies on two assumptions: every state in the controls is present in the atlas, and disease alters only a fraction of cell types.
- Simulated OOR states are "removed types" or "split halves" — more discrete than real continuous disease shifts; detection needs ~≥250 cells, limiting rare states.
- scRNA-seq only, PBMC and lung only; no spatial, multimodal or ATAC data.
- Matched controls are still required; options without controls are only discussed in the supplement.

## Relation to our direction
This is a **methodological cornerstone** for the detect stage: we treat disease-altered cell states as anomalies, and this paper tells us how to define "normal" — **the atlas defines the coordinate system, matched controls define the statistical null**. For **Plan A** (kidney-omics anomaly detection) it is directly usable: use KPMP / the Lake kidney atlas / HuBMAP as the embedding reference, map the in-house 95-biopsy snRNA into it, and use matched healthy samples (in-house or KPMP, e.g. tumour-nephrectomy normal tissue) as the DA controls; the OOR simulation (remove one cell type from healthy data) can be repurposed as the synthetic ground-truth arm of **KidneyAnomalyBench**, complementing expert labels. It also documents a key failure mode — batch/protocol differences mistaken for disease under the AR design — which is exactly why Plan A uses **cross-modal agreement** (snRNA vs snATAC vs Xenium) to separate artifacts from disease: single-modality DA significance is not enough. For **Plan B** (trustworthy biomedical agents), it yields concrete claim-to-evidence checks: when an agent claims "a disease-specific cell state was found," a verifier should check the reference design (matched controls? HVGs selected on disease data? suspiciously few samples per neighbourhood?) — all entries for an omics-specific failure taxonomy.

## Reusable assets
- **Reproducibility code** (OOR design benchmark):
<https://github.com/MarioniLab/oor_design_reproducibility>
- **milopy** (Python Milo differential abundance):
<https://github.com/emdann/milopy>
- **Data**: processed PBMC data on Zenodo; HLCA reproducibility repo.
<https://zenodo.org/record/6337966> · <https://github.com/LungCellAtlas/HLCA_reproducibility>
- **Protocol**: scVI (5,000 HVGs) + scArches mapping + Milo DA (10% spatial FDR) + AUPRC/FDR/TPR evaluation.

## Follow-ups
- MapQC (`refmap-eval-biorxiv-2025` in this repo): automatically judges mapping success on top of an ACR-style design — a direct follow-up.
- MrVI (`mrvi-natmethods-2025`): cluster-free sample-level DA/DE, to compare against Milo.
- Supplementary Notes 2.1 / 2.3: alternatives without controls (latent distance, label-transfer uncertainty).
- Reproduce ACR vs CR on kidney data (Lake atlas + KPMP).

## Cite
```bibtex
@article{Dann_2023, title={Precise identification of cell states altered in disease using healthy single-cell references}, volume={55}, ISSN={1546-1718}, url={http://dx.doi.org/10.1038/s41588-023-01523-7}, DOI={10.1038/s41588-023-01523-7}, number={11}, journal={Nature Genetics}, publisher={Springer Science and Business Media LLC}, author={Dann, Emma and Cujba, Ana-Maria and Oliver, Amanda J. and Meyer, Kerstin B. and Teichmann, Sarah A. and Marioni, John C.}, year={2023}, month=Oct, pages={1998–2008} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
