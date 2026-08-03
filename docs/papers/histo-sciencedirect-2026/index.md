# Spatial biomarker discovery via interpretable semantic learning in histopathology

> **Bibkey** `histo-sciencedirect-2026` · **Venue** Cancer Cell (2026) · **Category** histopath · **Relevance** high · **Access** open
> **Link** <https://www.sciencedirect.com/science/article/pii/S153561082600259X> · `status: complete`

---

> **Note:** Although the ScienceDirect page is paywalled, this paper is published **open access under CC BY 4.0** (Cancer Cell 44, 1–18, 2026-08-10, DOI 10.1016/j.ccell.2026.05.014); the full text was obtained via the open PDF (White Rose / Elsevier open access).

## One-liner
PathPrism is an interpretable computational-pathology framework that "refracts" colorectal-cancer WSIs into a spectrum of semantically defined spatial biomarkers, drives transparent linear models for prognosis/mutation/therapy prediction, and adds VirtualWSI for perturbation-driven (in-silico) exploration.

## Problem
Spatial biomarkers in the tumor microenvironment are decisive for precision oncology, but human discovery does not scale and DL/foundation models are black boxes whose post-hoc explanations are too diffuse to define, quantify, and validate as interpretable biomarkers — blocking clinical translation, LLM-assisted hypothesis generation, and the move from passive prediction to active perturbation.

## Method
A three-stage prism pipeline: PrismNet (UNI features + PCA classifier, trained on 100K annotated CRC patches) segments WSIs into 8 tissue classes; MacroNet learns macro tissue-architecture→survival associations from those maps and is interrogated via saliency attribution and structure-preserving counterfactual perturbation; guided by MacroNet, the maps are decomposed into 628 interpretable spatial features (tissue fractions, spatial entropy, single-/multi-tissue slide-level graph features). Transparent models sit on this spectrum: elastic-net Cox (SPM; FSPM = top-10 features) for prognosis, L1 logistic regression for mutation/therapy. Adds LLM-assisted hypothesis organization and VirtualWSI for structure-preserving semantic perturbation of the spatial-biomarker atlas.

## Data
H&E WSIs from ~7,000 CRC patients across 11 cohorts. Segmentation: trained on NCT-CRC-HE-100K-NONORM, tested on CRC-VAL-HE-7K. Prognosis/mutation/therapy: DACHS (primary, 5-fold CV), MCO, CR07 (rectal-only, low MSI), TCGA external; mutation models trained on CORSA/EPIC/WHI/IWHS/CRA and tested on TCGA; chemo cohorts include IDEA (Arm A/B), HeCOG, GECCO. Transferability shown on breast cancer (BRCA), including T-DXd and sacituzumab-govitecan ADC subgroups.

## Key results

- Segmentation: PrismNet on CRC-VAL-HE-7K reaches macro-F1 0.948, MCC 0.958, macro-AUROC 0.988.
- Prognosis: MacroNet DSS C-index 0.716±0.020 on DACHS (5-fold), on par with foundation models (GigaPath/CHIEF/COBRA/PRISM/attMIL-UNI); KM risk stratification HR = 3.68 (MCO), 2.48 (CR07), 3.27 (TCGA).
- Single-/multi-tissue biomarkers: TUM graph entropy C-index 0.62/HR 1.97; MUS spatial fraction C-index 0.60/HR 0.57; STR-TUM-EN1, MUS-TUM-EN2 (TCGA) C-index 0.73; ADI-TUM-E (CR07) 0.69.
- Transparent spectrum models: SPM and FSPM (628→top-10) C-index >0.7, on par with MacroNet/foundation models yet forward-interpretable; when fused with foundation-model embeddings, spatial features contribute ~25% of the importance.
- Mutation: MSI prediction DACHS AUC 0.85 (5-fold), 0.78 across 7 external cohorts; on TCGA BMPR2/BRAF/TP53 AUC 0.78/0.75/0.66 (key features: DEB entropy, MUC-TUM interaction).
- Chemo stratification: in stage III, LYM-MUC-CC separates ACT response — high fragmentation HR 9.08 (ACT worse), low fragmentation HR 0.29 (benefit), interaction HR 32.45, p=0.001; VirtualWSI perturbation-induced state transitions further refine the benefiting subgroup (HR 0.27, p=0.010).

## Contributions
- Replaces black-box embeddings with a "semantic segmentation → quantifiable spatial-feature spectrum (628-dim) → transparent linear model" pipeline, achieving **forward interpretability** (predictions attribute directly to specific spatial biomarkers) while still matching SOTA foundation models.
- **VirtualWSI**: a structure-preserving semantic-perturbation framework plus a spatial-biomarker atlas (UMAP), turning pathology from "prediction" into a platform for in-silico exploration / counterfactual experiments.
- Closed-loop discovery: model explanation → quantitative validation of candidate biomarkers → LLM organizes them into structured, testable mechanistic hypotheses (rated by 5 experts).
- Shows that macro spatial architecture encodes molecular information conventionally thought to require cell-level analysis (MSI/BRAF/TP53), and reveals spatial heterogeneity of ACT benefit in stage-III CRC.

## Limitations
- Depends on predefined semantic tissue categories and can only capture spatial patterns within the chosen segmentation classes; transferring to a new tumor type requires re-annotating, retraining, and validating PrismNet (e.g., BRCA).
- VirtualWSI's semantic perturbations are "model-interrogation" exploration and **do not represent biological causality or physically realizable tissue states**.
- Prognostic performance sits in a "moderate" range (C-index ~0.7); downstream biological interpretations such as ACT are hypothesis-generating and need further validation.
- The LLM only organizes hypotheses; it does not produce validated biological conclusions.

## Relation to our direction
This paper is almost an interpretable instantiation of our three-stage "anomaly detection → virtual tissue → gene/intervention revert" route in the pure-histology (H&E) modality; PI-flagged as important and worth comparing stage by stage:
- **Anomaly-detection stage**: MacroNet's risk score + saliency attribution + structure-preserving counterfactual perturbation essentially localize the spatial regions "changed by disease and driving poor prognosis" (e.g., STR/TUM disorder, invasive front, SARIFA-like invasion, fragmented LYM connectivity). This is exactly the "detect tissue regions changed by disease/perturbation" that we want, and it yields **quantifiable, nameable spatial biomarkers** rather than diffuse heatmaps — directly reusable as an interpretable baseline for anomaly scoring and localization.
- **Virtual-tissue stage**: **VirtualWSI is essentially a "virtual tissue" engine** — it applies continuous intensity perturbations to semantic channels (e.g., MUC, LYM) while preserving global structure, and visualizes each sample's trajectory within the 628-dim spatial-biomarker atlas. It provides a complete engineering paradigm for "how to make controlled edits to tissue in an interpretable latent space and observe phenotype drift," the most direct methodological reference for building our virtual/counterfactual tissues (note: the authors explicitly frame it as model interrogation, not physical causality).
- **Revert/intervention stage**: here "revert" happens at the **spatial-biomarker level** rather than the gene level — e.g., "increasing LYM consistently lowers the risk score," "adding NORM/LYM lowers risk for high-risk patients," and perturbation-induced ACT-benefit state transitions. It demonstrates the closed loop of "which spatial axis to perturb to push a high-risk phenotype back to low-risk," but **lacks mapping to specific genes/drug targets**. The BRCA section correlates spatial biomarkers (STR-ACL, ADI-NEC-BT2) with ERBB2/TOP1/TACSTD2 expression (though the correlations are "modest"), hinting at both the feasibility and the shortfall of the "spatial biomarker ↔ gene expression" bridge — exactly the key link we must add: coupling PathPrism's spatial anomaly axes with spatial transcriptomics/gene prediction to predict "which genes to modulate to reverse the anomaly."
- **Overall positioning**: PathPrism covers the first two stages of our route (anomaly detection, virtual tissue) and provides an interpretable, perturbable tissue representation; the third stage (gene-level revert) is a clear interface and gap. It can serve as the interpretable-anomaly/virtual-tissue skeleton for the H&E modality, to which we then attach our spatial-omics gene-prediction module.

## Reusable assets
- **Code**: full PathPrism pipeline <https://github.com/KatherLab/PathPrism> (incl. PrismNet, MacroNet, 628 spatial-feature extraction, SPM/FSPM, VirtualWSI, LLM workflow). Related: STAMP pipeline <https://github.com/KatherLab/STAMP>.
- **Data/eval**: CRC100K segmentation data (NCT-CRC-HE-100K-NONORM train / CRC-VAL-HE-7K test, Zenodo record 1214456); TCGA-CRC/CPTAC WSI + molecular data (public via GDC, cBioPortal). Eval protocol: 5-fold CV + external-cohort bootstrap 95% CI; prognosis C-index, KM/HR; classification AUROC/AUC; SHAP feature contributions.
- **Reusable components**: efficient UNI+PCA patch semantic-segmentation configuration; 8-class CRC tissue ontology; single-/multi-tissue slide-level graph-feature definitions (Tables S2/S3); Cox interaction framework (identifying ACT-benefit predictive biomarkers); structure-preserving counterfactual/semantic-perturbation implementation (VirtualWSI).
- **Restricted data**: DACHS, MCO, CR07, IDEA, HeCOG, GECCO are sensitive and require application through each institution's / consortium's process.

## Follow-ups
- Close-read the STAR Methods: PrismNet (UNI+PCA configuration, partial-annotation transfer), MacroNet architecture and saliency, and the exact definitions of the 628 graph features (Figure S4A, Tables S2/S3).
- The concrete perturbation-operator implementation of VirtualWSI (channel intensity α, structure-preserving constraints); assess whether it can be adapted into a virtual-tissue / counterfactual generator for spatial-omics.
- Reproduce github.com/KatherLab/PathPrism, running CRC100K segmentation + DACHS/TCGA prognosis end-to-end as our H&E anomaly-detection baseline.
- Integration point: extend "spatial-biomarker ↔ gene" correlation analyses such as STR-ACL↔ERBB2/TOP1 and ADI-NEC-BT2↔TACSTD2 into a predictive gene-revert model (combined with spatial transcriptomics).
- Related reading: the companion Cancer Cell piece "From prediction to interpretation in computational pathology" (S1535-6108(26)00290-4) and Cell "virtual spatial tumor profiling from histopathology" (S0092-8674(26)00590-8).

## Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
