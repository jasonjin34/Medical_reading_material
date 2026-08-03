# Boehringer-Ingelheim/anomaly-detection-in-histology

> **Bibkey** `histo-anomaly-bi-repo` · **Venue** GitHub (2022) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://github.com/Boehringer-Ingelheim/anomaly-detection-in-histology>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> Boehringer Ingelheim 开源的 PyTorch 代码库,只用「健康组织」训练表征,再用 one-class 分类器在组织病理全切片上检测药物毒性引起的异常改变。
<!-- EN --> An open-source PyTorch repo from Boehringer Ingelheim that learns representations from healthy tissue only, then applies one-class classifiers to flag drug-induced histological anomalies in whole-slide images. Companion code to Zingman et al., *Medical Image Analysis* 2024.

## 研究问题 / Problem
<!-- ZH --> 在药物开发的毒性评估中,异常(病变)样本稀少且难以穷举标注,监督分类不可行。目标是仅凭大量健康组织学习一个足够判别的表征,使任何偏离「正常」的组织都能被检出——用于早期化合物毒性筛查,减少昂贵的后期失败。
<!-- EN --> In drug-development toxicity assessment, abnormal/lesion samples are scarce and cannot be exhaustively labeled, so supervised classification fails. The goal is to learn a discriminative representation from abundant healthy tissue alone so that any deviation from "normal" is detectable, enabling early-stage compound toxicity screening.

## 方法 / Method
<!-- ZH --> 分两阶段。(1) 表征学习:在健康组织上训练 CNN(EfficientNet-B0,320px 输入),辅助任务是区分健康组织的物种/器官/染色剂——这些标签可从元数据自动获得,无需额外标注;并加 center-loss 正则,使同类表征更紧致、利于异常检测。(2) 异常检测:在训练好的 CNN 深层特征上拟合 one-class SVM,对新切片打异常分。支持 H&E 与 Masson 三色两种染色。代码入口:`train_cnn.py`、`anomaly_detector.py`、`model_use_example.py`,配置在 `configs/`。
<!-- EN --> Two stages. (1) Representation learning: a CNN (EfficientNet-B0, 320px input) is trained on healthy tissue with an auxiliary task of discriminating species/organ/staining — labels obtained automatically from metadata, no extra annotation — plus a center-loss term to make same-class features compact and anomaly-friendly. (2) Detection: a one-class SVM is fit on deep features to score new slides. Supports H&E and Masson's Trichrome. Entry points: `train_cnn.py`, `anomaly_detector.py`, `model_use_example.py`; configs under `configs/`.

## 数据 / Data
<!-- ZH --> 训练:多物种、多器官、多染色的健康组织。评测:正常小鼠肝 vs. NAFLD(非酒精性脂肪肝)病变样本——一个已公开的肝脏异常数据集。数据托管在 OSF:<https://osf.io/gqutd/>。
<!-- EN --> Training on healthy tissue spanning multiple species, organs, and stains. Evaluation on normal mouse liver vs. NAFLD pathology (a published liver-anomaly dataset). Data hosted on OSF: <https://osf.io/gqutd/>.

## 主要结果 / Key results
<!-- ZH --> 肝脏异常检测:H&E 平衡准确率 94.20%、AU-ROC 97.33%、F1 94.09%;Masson 三色 平衡准确率 97.51%、AU-ROC 99.03%、F1 97.51%。论文称其超过常规 anomaly-detection 基线,并与专门为肝脏定量设计的方法相当。
<!-- EN --> Liver anomaly detection: H&E — balanced accuracy 94.20%, AU-ROC 97.33%, F1 94.09%; Masson's Trichrome — 97.51% / 99.03% / 97.51%. The paper reports it beats established anomaly-detection baselines and matches methods purpose-built for liver-lesion quantification.

## 创新点 / Contributions
- <!-- ZH --> 用健康样本元数据(物种/器官/染色)自动构造辅助分类任务来学表征,零额外标注。<!-- EN --> Auxiliary task built from free healthy-sample metadata (species/organ/stain) — representation learning with zero extra labels.
- <!-- ZH --> center-loss 正则 + one-class SVM 的组合显著提升病理异常检出。<!-- EN --> Center-loss regularization + one-class SVM combination markedly improves lesion detection.
- <!-- ZH --> 完整可复现工程:代码 + OSF 数据 + 预训练权重 + 评测脚本,MIT 许可。<!-- EN --> Fully reproducible package: code + OSF data + checkpoints + eval scripts, MIT-licensed.

## 局限 / Limitations
- <!-- ZH --> 验证集中在肝脏(小鼠肝 / NAFLD),向其他器官与病变类型的迁移未在此库充分展示。<!-- EN --> Validation centers on liver (mouse liver / NAFLD); transfer to other organs/lesion types not demonstrated here.
- <!-- ZH --> 仅输出「异常 / 分数」,不定位或解释是哪些基因/通路驱动;非生成、不可逆推。<!-- EN --> Outputs an anomaly score only — no localization of driving genes/pathways; not generative and not invertible.
- <!-- ZH --> 依赖 patch 级 CNN 表征,分辨率(320px)与染色两类,泛化到新染色/扫描仪需重训。<!-- EN --> Relies on patch-level CNN features at fixed 320px and two stains; new stains/scanners likely need retraining.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 直接对应流水线的**第一环:anomaly detection**。这是一个「只学正常、检出偏离」范式在组织病理上的干净、经过工业验证的实现,正是我们要在图像/空间组学上检测「疾病或药物扰动导致改变的区域」的思路。可直接借鉴:(a) 用元数据自动构造辅助任务学表征的策略,可迁移到我们自己的 histopath/空间组学正常图谱;(b) center-loss + one-class 的异常打分协议可作为基线。但它止步于「打分」,不涉及 virtual tissue 建模,也不做 gene-revert 预测——后两环需要我们在其检出的异常区域之上另接空间组学/生成模型。可作为 histopath 模态异常检测的 baseline 与工程模板。
<!-- EN --> Maps squarely onto **stage 1: anomaly detection**. It is a clean, industrially validated instance of the "learn-normal, flag-deviation" paradigm on histopathology — exactly our approach for detecting disease/drug-perturbed regions. Reusable: (a) the metadata-driven auxiliary-task representation trick, portable to our own histopath/spatial-omics normal atlases; (b) the center-loss + one-class scoring protocol as a baseline. It stops at scoring — no virtual-tissue modeling, no gene-revert prediction — so stages 2–3 must be layered on top of its detected regions. Best used as a histopath-modality baseline and engineering template.

## 可复用资产 / Reusable assets
- <!-- ZH --> 代码库(MIT):`train_cnn.py` / `anomaly_detector.py` / `model_use_example.py`,配置 `configs/cfg_training_cnn.py`、`configs/cfg_anomaly_detector.py`。<!-- EN --> MIT-licensed repo with training, detection, and feature-extraction scripts + configs.
- <!-- ZH --> 预训练产物:CNN 权重(`.pt`)、one-class SVM(`.pkl`)。<!-- EN --> Pretrained CNN weights (`.pt`) and one-class SVM classifiers (`.pkl`).
- <!-- ZH --> 数据集(OSF):<https://osf.io/gqutd/>,含正常小鼠肝与 NAFLD 评测集。<!-- EN --> OSF dataset <https://osf.io/gqutd/> (normal mouse liver + NAFLD eval set).
- <!-- ZH --> 评测协议:balanced accuracy / AU-ROC / F1,可直接复用为异常检测评测标准。<!-- EN --> Eval protocol (balanced accuracy / AU-ROC / F1) reusable as an anomaly-detection benchmark.

## 待读 / Follow-ups
- <!-- ZH --> 精读配套论文 Zingman et al., *Medical Image Analysis* 92 (2024) 103067,arXiv:2210.07675——看 center-loss 消融与基线对比细节。<!-- EN --> Read the companion paper (DOI 10.1016/j.media.2023.103067; arXiv:2210.07675) for center-loss ablations and baseline comparisons.
- <!-- ZH --> 评估把该表征替换为病理 foundation model(如 UNI/CONCH/Virchow)后异常检测是否更强。<!-- EN --> Test swapping the CNN for a pathology foundation model (UNI/CONCH/Virchow) as the feature extractor.
- <!-- ZH --> 探索在检出的异常 patch 上对接空间转录组以进入 virtual-tissue / gene-revert 环节。<!-- EN --> Explore coupling detected anomaly patches with spatial transcriptomics toward the virtual-tissue / gene-revert stages.

## 引用 / Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文/full-text extract →](ai-ready.md)**
