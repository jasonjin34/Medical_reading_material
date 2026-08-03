# An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study

> **Bibkey** `Raikhelkar_2026` · **Venue** European Heart Journal - Digital Health (2026) · **Category** imaging · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1093/ehjdh/ztag088> · `status: complete`

---

## One-liner
A pretrained 3D vision transformer (CT-ViT) predicts abnormal left-ventricular ejection fraction (EF < 50%) directly from routine non-gated, non-contrast chest CT, turning scans acquired for unrelated indications into an opportunistic heart-failure screen.

## Problem
Many patients with early systolic dysfunction remain asymptomatic and undiagnosed at exactly the stage when guideline-directed medical therapy prevents progression — a large diagnostic gap. EF is normally read from echocardiography, which must be ordered specifically, whereas non-contrast chest CTs are acquired in huge volumes for unrelated reasons and never used to assess cardiac function. The paper asks whether abnormal EF can be opportunistically detected from those existing CTs with no extra scan and no contrast.

## Method
Framed as binary classification (abnormal EF < 50% vs. normal). The backbone is a pretrained CT-ViT encoder (a 3D vision transformer); inputs are 3D CT volumes normalized to 2×2×2 mm and resampled to 164×164×164 voxels. Each CT is paired with a temporally matched echocardiogram report supplying the EF label for supervised training. Interpretability uses Grad-CAM to produce 3D saliency localizing imaging features linked to reduced LVEF. Evaluation includes standard discrimination metrics plus a head-to-head reader study against experienced thoracic radiologists (accuracy and per-scan time).

## Data
A multi-institutional paired dataset of 34,058 non-contrast CT + echocardiogram-report pairs from two academic centers. Training used 25,948 studies (with a hold-out internal test set); external validation used 8,110 pairs from a separate institution. Internal = Columbia University; external = Weill Cornell. The reader comparison ran on a sampled subset of 90 Columbia scans.

## Key results
Internal hold-out: AUROC 0.786, F1 0.822. External validation: AUROC 0.762, F1 0.812 (generalization largely preserved). Reader study (90 Columbia scans): model F1 0.808 vs. radiologist F1 0.646–0.802 — matching or exceeding experts on accuracy, at ~1 min/scan vs. 2+ min for radiologists. Grad-CAM highlighted clinically recognizable correlates of low EF: enlarged heart, ascending aorta (especially when calcified), dilated superior vena cava, pacemaker presence, and pulmonary-edema infiltrates.

## Contributions
- First demonstration that abnormal LVEF is predictable from static, non-gated, non-contrast chest CT — a new opportunistic-screening use of an otherwise unrelated modality.
- Large real-world, cross-institution paired dataset (34,058) with independent external validation.
- Matches/exceeds expert radiologists with a speed advantage; Grad-CAM offers clinically interpretable evidence.

## Limitations
- Binary only (abnormal vs. normal); no continuous EF regression or finer HFrEF/HFmrEF stratification.
- AUROC ~0.76–0.79 is moderate — not yet standalone-diagnostic; labels come from echo report text with temporal mismatch and reporting noise.
- Two training + one external site limits scanner/population diversity; reader study only 90 scans.
- Full text is paywalled; hyperparameters, ablations, calibration, and threshold choice are abstract-only.

## Relation to our direction
This sits at stage 1 of our pipeline — anomaly detection: deciding that an organ/tissue deviates from normal in medical imaging. Three transferable lessons: (1) the opportunistic-screening paradigm — mining data collected for other purposes to surface unlabeled disease/perturbation signal — mirrors our goal of detecting disease- or drug-perturbed regions in routine histology/spatial-omics; (2) weak-label supervision — using paired clinical readouts (echo EF here) as image labels — parallels weakly supervising virtual-tissue anomaly scores with bulk phenotypes/clinical endpoints; (3) interpretable localization (3D Grad-CAM) grounds "abnormal" in specific anatomy/space, the spatial prior our later virtual-tissue modelling and gene-revert target localization need. Caveat: it is purely supervised classification, not the un-/self-supervised out-of-distribution anomaly detection we favor, and it does not touch the gene-revert inversion stage. The CT-ViT 3D imaging foundation encoder is a useful backbone reference for the imaging branch.

## Reusable assets
**CT-ViT encoder**: the pretrained 3D ViT backbone (from the CT-CLIP / CT-ViT family of chest-CT foundation models) is a reusable imaging-backbone starting point. **Input spec**: 2×2×2 mm normalization + 164×164×164-voxel resampling — directly copyable for 3D CT/volumetric preprocessing. **Eval protocol**: paired CT–clinical-readout labels, internal hold-out + independent external-site validation, plus a human reader study (accuracy + per-scan time) — a cross-institution generalization + expert-comparison template portable to our anomaly-detection evaluation. Dataset and training code are not released (private clinical data, IRB); request from authors/institutions.

## Follow-ups
- Original CT-ViT / CT-CLIP foundation-model paper + weights: availability, license, fitness as a self-supervised backbone for our imaging anomaly detection.
- Obtain full text for architecture details, calibration, thresholds, ablations; confirm EF-label extraction and temporal-window definition.
- Compare adjacent work (ECG- and CXR-based EF) to position the CT branch within multimodal opportunistic screening.

## Figures & tables

The full text and all figures/tables are behind the OUP paywall; per copyright no images are downloaded or re-hosted — figures are linked on the article page (paywalled) only. Key figures/tables are listed below by their original numbering with bilingual captions. Article page: <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677>.

**Fig 1** (paywalled): Data curation and preprocessing flowchart — selection, exclusion, and preprocessing of echocardiogram reports and chest CTs from Columbia University and Weill Cornell. See <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F1>

**Fig 2** (paywalled, method overview): Schematic of the vision-transformer architecture that analyzes 3D chest CT to predict left-ventricular systolic dysfunction. See <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F2>

**Fig 4** (paywalled, main results): Performance evaluation for detecting abnormal EF — ROC curves and AUROC, metrics by demographic subgroup, and confusion matrices. See <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F4>

**Fig 5** (paywalled, interpretability): Grad-CAM saliency maps overlaid on axial CT highlighting regions contributing to the prediction. See <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F5>

_Other figures/tables (paywalled): Fig 3 study design · Fig 6 error-analysis Venn · Fig 7 calibration; Tables 1–4 cohort/acquisition/diagnosis/timing · Table 5 subgroup AUROC · Table 6 RF/XGBoost baselines · Table 7 F1 vs radiologists. All at <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677>_

### Results

**Table 1.** Publicly visible headline numbers (abstract / article-page public content only; full performance tables are paywalled — see original Tables 5–7).

_abstract-only — numbers from the public abstract and article page; paywalled full text not accessed._

| Item | Value |
|---|---|
| Task | Abnormal LVEF (EF < 50%) vs. normal, from non-gated non-contrast chest CT |
| Paired CT + echo studies (total) | 34,058 |
| Training studies | 25,948 |
| External-validation studies | 8,110 |
| AUROC — internal hold-out (Columbia) | 0.786 |
| AUROC — external validation (Weill Cornell) | 0.762 |

## Cite
```bibtex
@article{Raikhelkar_2026, title={An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study}, volume={7}, ISSN={2634-3916}, url={http://dx.doi.org/10.1093/ehjdh/ztag088}, DOI={10.1093/ehjdh/ztag088}, number={6}, journal={European Heart Journal - Digital Health}, publisher={Oxford University Press (OUP)}, author={Raikhelkar, Jayant and Bai, Zilong and Beecy, Ashley N and Richter, Ilan and Liu, Fengbei and Nizam, Nusrat Binta and Kishore, Varsha and Kelsey, Chris and vanMaanen, David and Ruhl, Jeffrey and Tesfuzigta, Naomi and Lancet, Erica and Leb, Jay and Legasto, Alan and Elias, Pierre and Poterucha, Timothy and Kumaraiah, Deepa and Prince, Martin and Wang, Fei and Sayer, Gabriel and Estrin, Deborah and Sabuncu, Mert and Uriel, Nir}, year={2026}, month=June }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
