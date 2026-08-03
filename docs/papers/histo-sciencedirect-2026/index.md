# Spatial biomarker discovery via interpretable semantic learning in histopathology

> **Bibkey** `histo-sciencedirect-2026` · **Venue**  () · **Category** histopath · **Relevance** high · **Access** paywall
> **Link** <https://www.sciencedirect.com/science/article/pii/S153561082600259X>
> `status: abstract-only` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

> 注 / Note: 虽然 ScienceDirect 页面付费,但本文以 **CC BY 4.0 开放获取** 发表(Cancer Cell 44, 1–18, 2026-08-10, DOI 10.1016/j.ccell.2026.05.014),全文经开放 PDF(White Rose / Elsevier open access)获取,以下内容基于全文,非杜撰。

## 一句话 / One-liner
PathPrism is an interpretable computational-pathology framework that "refracts" colorectal-cancer WSIs into a spectrum of semantically defined spatial biomarkers, drives transparent linear models for prognosis/mutation/therapy prediction, and adds VirtualWSI for perturbation-driven (in-silico) exploration.

## 研究问题 / Problem
Spatial biomarkers in the tumor microenvironment are decisive for precision oncology, but human discovery does not scale and DL/foundation models are black boxes whose post-hoc explanations are too diffuse to define, quantify, and validate as interpretable biomarkers — blocking clinical translation, LLM-assisted hypothesis generation, and the move from passive prediction to active perturbation.

## 方法 / Method
A three-stage prism pipeline: PrismNet (UNI features + PCA classifier, trained on 100K annotated CRC patches) segments WSIs into 8 tissue classes; MacroNet learns macro tissue-architecture→survival associations from those maps and is interrogated via saliency attribution and structure-preserving counterfactual perturbation; guided by MacroNet, the maps are decomposed into 628 interpretable spatial features (tissue fractions, spatial entropy, single-/multi-tissue slide-level graph features). Transparent models sit on this spectrum: elastic-net Cox (SPM; FSPM = top-10 features) for prognosis, L1 logistic regression for mutation/therapy. Adds LLM-assisted hypothesis organization and VirtualWSI for structure-preserving semantic perturbation of the spatial-biomarker atlas.

## 数据 / Data
H&E WSIs from ~7,000 CRC patients across 11 cohorts. Segmentation: trained on NCT-CRC-HE-100K-NONORM, tested on CRC-VAL-HE-7K. Prognosis/mutation/therapy: DACHS (primary, 5-fold CV), MCO, CR07 (rectal-only, low MSI), TCGA external; mutation models trained on CORSA/EPIC/WHI/IWHS/CRA and tested on TCGA; chemo cohorts include IDEA (Arm A/B), HeCOG, GECCO. Transferability shown on breast cancer (BRCA), including T-DXd and sacituzumab-govitecan ADC subgroups.

## 主要结果 / Key results
PrismNet macro-F1 0.948 / AUROC 0.988. MacroNet DSS C-index 0.716 on DACHS; KM HR 3.68/2.48/3.27 (MCO/CR07/TCGA). Individual spatial biomarkers reach C-index up to 0.73. SPM/FSPM C-index >0.7 with direct feature attribution; spatial features add ~25% importance when fused with foundation embeddings. MSI AUC 0.85 (DACHS) / 0.78 (external); BMPR2/BRAF/TP53 AUC 0.78/0.75/0.66 on TCGA. LYM-MUC-CC stratifies stage-III ACT benefit (interaction HR 32.45, p=0.001; high-fragmentation ACT harm HR 9.08, low-fragmentation benefit HR 0.29).

## 创新点 / Contributions

## 局限 / Limitations

## 与本研究方向的关系 / Relation to our direction
This paper maps almost one-to-one onto our anomaly→virtual-tissue→gene-revert pipeline for the H&E modality (PI-flagged as important): MacroNet's risk score + saliency + structure-preserving counterfactuals localize disease-driven anomalous regions as named, quantifiable spatial biomarkers (reusable as an interpretable anomaly-scoring/localization baseline). VirtualWSI is essentially a virtual-tissue engine — controlled, structure-preserving semantic-channel perturbation with trajectory visualization in a 628-dim biomarker atlas — the most directly reusable methodology for building counterfactual/virtual tissues (authors stress it is model interrogation, not physical causality). "Revert" here operates at the spatial-biomarker level (e.g., amplifying LYM lowers risk; perturbation-induced ACT-benefit state transitions), not the gene level; the BRCA section only weakly links spatial biomarkers to ERBB2/TOP1/TACSTD2 expression, exposing exactly the missing bridge our work must add: coupling PathPrism's spatial anomaly axes to spatial-omics/gene prediction to name genes whose modulation reverts the anomaly.

## 可复用资产 / Reusable assets

## 待读 / Follow-ups

## 引用 / Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
