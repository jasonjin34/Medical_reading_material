# Deep learning-based pathomics signature predicts prognosis and treatment response in gastric cancer: a multicenter retrospective study

> **Bibkey** `Wang_2026` · **Venue** npj Precision Oncology (2026) · **Category** pathology · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s41698-026-01381-6> · `status: complete`

---

## One-liner
A multi-scale graph neural network with gated-attention multiple-instance learning (MS-GMIL) reads gastric-cancer H&E whole-slide images directly to build an interpretable pathomics signature (PSGC) that predicts overall survival and stratifies chemo/immunotherapy benefit.

## Problem
TNM staging gives insufficient prognostic resolution in gastric cancer — outcomes vary widely within a stage, complicating individualized treatment. The paper aims to extract prognostic signal directly from routine H&E slides (no hand-crafted features) and turn it into an interpretable index that guides chemotherapy and immunotherapy decisions.

## Method
They propose MS-GMIL: a multi-scale graph neural network coupled with a gated-attention multiple-instance-learning head, taking whole-slide images with slide-level (weak) supervision to predict OS directly. MS-GMIL deep features are combined with traditional ML to build the final **11-feature** pathomics signature (PSGC). SHAP and pathogenomics analyses provide interpretability, and matched transcriptomic data probe the underlying biology. (Full architectural formulas/hyperparameters are paywalled — abstract-level detail only.)

## Data
Multicenter retrospective cohorts totaling **3,138** GC patients (median age 60; 71.64% male, 2,248/3,138), split into training and validation (and additional) cohorts. Modalities: H&E digital whole-slide images, plus paired transcriptomic data for mechanism analysis. Per-center cohort names and exact split sizes are not fully public (abstract-only).

## Key results
PSGC was an independent prognostic factor in **all cohorts**. Stage II/III patients with high PSGC gained considerable chemotherapy benefit and responded effectively to immunotherapy, positioning it as a treatment-response predictor. Interpretability links PSGC to tumor-cell anaplasia, intraepithelial neoplasia, tumor–stroma fibrosis, and intestinal metaplasia; transcriptomically it tracks cell-cycle regulation, drug-resistance pathways, and cancer progression. Exact discrimination metrics (C-index/HR/AUC/p) are not public — abstract-only, not fabricated here.

## Contributions
- MS-GMIL fuses multi-scale graph structure with gated-attention MIL to learn prognosis end-to-end from WSIs rather than predefined hand-crafted features.
- Large multicenter validation (3,138 patients) with PSGC an independent prognostic factor across all cohorts.
- Beyond prognosis, it predicts stage II/III chemotherapy benefit and immunotherapy response — clinically actionable.
- SHAP + pathogenomics interpretability maps the signature to concrete histology and molecular pathways.

## Limitations
- Retrospective design; treatment-benefit claims are stratified observations, not RCT-level evidence.
- Single cancer type (GC) and single modality (H&E); cross-cancer / cross-stain generalization unknown.
- Key quantitative metrics, code, and data-availability are not public — hard to reproduce independently.
- Cohorts appear China-centric, raising population-bias and external-validity questions.

## Relation to our direction
This sits mainly at the **anomaly-detection / tissue-representation** stage: MS-GMIL's gated-attention weights effectively localize prognosis-relevant "abnormal" WSI regions, offering a weakly-supervised, attention-based blueprint for our histopathology anomaly detection (which regions changed due to disease). Its **pathogenomics bridge** — linking the image signature to transcriptomic pathways and drug-resistance mechanisms — is most relevant to the **virtual-tissue → gene-revert** step: it demonstrates mapping an imaging phenotype onto actionable molecular pathways (cell cycle, resistance), exactly the image-to-molecule correspondence needed to predict which genes, if modulated, would revert an anomaly. Reusable as: an attention-based abnormal-region localizer plus an image→pathway association protocol. It does not do gene-revert prediction itself, but supplies the connective layer between pathological anomaly and molecular target.

## Reusable assets
Method-level reuse: (1) the MS-GMIL multi-scale-graph + gated-attention MIL architecture for weakly-supervised WSI representation / anomaly localization; (2) the SHAP + pathogenomics interpretability protocol (signature → histology → molecular pathway). Concrete code repo, pretrained checkpoints, datasets, and data/code-availability statements are not visible publicly (abstract-only) — verify via full text. The 3,138-patient scale is a useful benchmark reference.

## Follow-ups
- Get full text to verify MS-GMIL architecture (graph construction, multi-scale fusion, attention) and metrics (C-index/HR/AUC).
- Check data/code availability — whether model or features are released.
- Compare with the earlier Nat Commun 2022 GC pathomics-signature paper to gauge the delta.

## Figures & tables

**Paywall note:** This is a paywalled npj Precision Oncology article; its figures and body text sit behind the paywall. Per the repo's copyright rule, **no images are downloaded** — only links are given. Exact per-figure numbers and captions are not publicly visible, so none are reproduced/invented here. View them at the source:

· Full article: <https://www.nature.com/articles/s41698-026-01381-6>
· Figures gallery (all figures): <https://www.nature.com/articles/s41698-026-01381-6/figures>
· Per-figure anchors (Nature convention): `…s41698-026-01381-6#Fig1`, `#Fig2`, … (paywalled)

### Results

**Table 1 (abstract-only; no discrimination metrics).** The table below reproduces **only** numbers visible in the public abstract / landing page; specific discrimination metrics (C-index, HR, AUC, p-values) are paywalled and are **not reproduced or fabricated**.

| Item | Value (abstract-only) |
|---|---|
| Total patients (multicenter, retrospective) | 3,138 |
| Male | 71.64% (2,248 / 3,138) |
| Median age | 60 years |
| Model | MS-GMIL — multi-scale graph neural network + gated-attention multiple-instance learning |
| Signature (PSGC) | interpretable, built from 11 features on H&E WSIs |
| Prognostic status | independent prognostic factor in all cohorts |
| Treatment signal | stage II/III high-PSGC → chemotherapy benefit + immunotherapy response |

_Source (abstract only): https://www.nature.com/articles/s41698-026-01381-6 · npj Precision Oncology (2026), paywalled — numbers are taken only from the public abstract, with no body-text or figure/table data._

## Cite
```bibtex
@article{Wang_2026, title={Deep learning-based pathomics signature predicts prognosis and treatment response in gastric cancer: a multicenter retrospective study}, volume={10}, ISSN={2397-768X}, url={http://dx.doi.org/10.1038/s41698-026-01381-6}, DOI={10.1038/s41698-026-01381-6}, number={1}, journal={npj Precision Oncology}, publisher={Springer Science and Business Media LLC}, author={Wang, Hao and Li, Hao and Ma, Keru and Mo, Genshen and Yan, Meihong and Zhang, Xinyue and Xie, Haonan and Huang, Yuze and Li, Huiying and Xue, Yingwei and Han, Peng and Lou, Shenghan}, year={2026}, month=Apr }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
