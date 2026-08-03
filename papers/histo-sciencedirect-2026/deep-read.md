# Spatial biomarker discovery via interpretable semantic learning in histopathology

> **Bibkey** `histo-sciencedirect-2026` · **Venue**  () · **Category** histopath · **Relevance** high · **Access** paywall
> **Link** <https://www.sciencedirect.com/science/article/pii/S153561082600259X>
> `status: abstract-only` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

> 注 / Note: 虽然 ScienceDirect 页面付费,但本文以 **CC BY 4.0 开放获取** 发表(Cancer Cell 44, 1–18, 2026-08-10, DOI 10.1016/j.ccell.2026.05.014),全文经开放 PDF(White Rose / Elsevier open access)获取,以下内容基于全文,非杜撰。

## 一句话 / One-liner
<!-- ZH --> PathPrism 把结直肠癌全切片图像(WSI)"棱镜式"分解为可解释的语义空间生物标志物谱,用透明线性模型完成预后/突变/疗效预测,并用 VirtualWSI 做语义扰动式虚拟实验。
<!-- EN --> PathPrism is an interpretable computational-pathology framework that "refracts" colorectal-cancer WSIs into a spectrum of semantically defined spatial biomarkers, drives transparent linear models for prognosis/mutation/therapy prediction, and adds VirtualWSI for perturbation-driven (in-silico) exploration.

## 研究问题 / Problem
<!-- 这篇论文要解决什么问题?为什么重要? / What problem, and why it matters. -->
<!-- ZH --> 空间生物标志物(肿瘤微环境中多尺度、多模态的组织模式)对精准肿瘤学至关重要,但因 WSI 复杂、组织异质、空间组织微妙,人工发现慢且难以量化验证。现有深度学习/病理基础模型虽准确却是"黑箱",post-hoc 解释弥散含糊,难以把信号定义、量化、表征为可解释、可验证的生物标志物,阻碍临床转化、LLM 假设生成与"从预测到主动扰动探索"的跃迁。
<!-- EN --> Spatial biomarkers in the tumor microenvironment are decisive for precision oncology, but human discovery does not scale and DL/foundation models are black boxes whose post-hoc explanations are too diffuse to define, quantify, and validate as interpretable biomarkers — blocking clinical translation, LLM-assisted hypothesis generation, and the move from passive prediction to active perturbation.

## 方法 / Method
<!-- 核心方法、模型、数据流。关键公式/架构。 / Core method, model, data pipeline, key architecture. -->
<!-- ZH --> 三级"棱镜"流水线:(1) **PrismNet** —— 基于 UNI 特征 + PCA 的分类器,在 10 万个标注 CRC patch 上训练,把 WSI 语义分割为 8 类组织(ADI/DEB/LYM/MUC/MUS/NORM/STR/TUM);(2) **MacroNet** —— 从语义分割图直接学习宏观组织架构与生存(DSS)的关联,并做多角度解释(saliency 归因、结构保持的反事实扰动);(3) 由 MacroNet 洞见指导,把分割图进一步分解为 **628 个可解释空间特征**(组织空间分数、空间熵、slide-level 图特征:单组织/多组织图的邻接与交互)。在此谱上用 **透明/极简模型** 建模:预后用弹性网 Cox(SPM,及取 top-10 特征的 FSPM),突变/疗效用 L1 逻辑回归。再叠加 **LLM 辅助假设生成**(病理学家—LLM 工作流 + 第二 LLM 审阅)与 **VirtualWSI**(在可解释空间生物标志物图谱内做结构保持的语义通道扰动/区域扰动,做 in-silico 虚拟实验)。
<!-- EN --> A three-stage prism pipeline: PrismNet (UNI features + PCA classifier, trained on 100K annotated CRC patches) segments WSIs into 8 tissue classes; MacroNet learns macro tissue-architecture→survival associations from those maps and is interrogated via saliency attribution and structure-preserving counterfactual perturbation; guided by MacroNet, the maps are decomposed into 628 interpretable spatial features (tissue fractions, spatial entropy, single-/multi-tissue slide-level graph features). Transparent models sit on this spectrum: elastic-net Cox (SPM; FSPM = top-10 features) for prognosis, L1 logistic regression for mutation/therapy. Adds LLM-assisted hypothesis organization and VirtualWSI for structure-preserving semantic perturbation of the spatial-biomarker atlas.

## 数据 / Data
<!-- 数据集、模态、规模、来源。 / Datasets, modalities, scale, source. -->
<!-- ZH --> H&E WSI,约 **7,000 例结直肠癌患者、11 个队列**。分割训练/评测:NCT-CRC-HE-100K-NONORM 训练、CRC-VAL-HE-7K 测试(CRC100K,Zenodo)。预后/突变/疗效队列:DACHS(主队列,5 折交叉验证)、MCO、CR07(仅直肠癌、常术前放疗、低 MSI)、TCGA(外部);突变训练用 CORSA/EPIC/WHI/IWHS/CRA,TCGA 测试;化疗队列含 IDEA(Arm A/B)、HeCOG、GECCO consortium。可迁移性验证:乳腺癌(BRCA;含 T-DXd、SG 等 ADC 治疗亚组)。
<!-- EN --> H&E WSIs from ~7,000 CRC patients across 11 cohorts. Segmentation: trained on NCT-CRC-HE-100K-NONORM, tested on CRC-VAL-HE-7K. Prognosis/mutation/therapy: DACHS (primary, 5-fold CV), MCO, CR07 (rectal-only, low MSI), TCGA external; mutation models trained on CORSA/EPIC/WHI/IWHS/CRA and tested on TCGA; chemo cohorts include IDEA (Arm A/B), HeCOG, GECCO. Transferability shown on breast cancer (BRCA), including T-DXd and sacituzumab-govitecan ADC subgroups.

## 主要结果 / Key results
<!-- 关键指标与结论,尽量带数字。 / Headline metrics and conclusions, with numbers where possible. -->
<!-- ZH -->
- 分割:PrismNet 在 CRC-VAL-HE-7K 上 macro-F1 0.948、MCC 0.958、macro-AUROC 0.988。
- 预后:MacroNet 在 DACHS 5 折 C-index 0.716±0.020,与 GigaPath/CHIEF/COBRA/PRISM/attMIL-UNI 等基础模型相当;KM 风险分层 HR = 3.68(MCO)、2.48(CR07)、3.27(TCGA)。
- 单/多组织标志物:TUM graph entropy C-index 0.62/HR 1.97;MUS spatial fraction C-index 0.60/HR 0.57;STR-TUM-EN1、MUS-TUM-EN2(TCGA)C-index 0.73;ADI-TUM-E(CR07)0.69。
- 透明谱模型:SPM 与 FSPM(628→top10)C-index >0.7,与 MacroNet/基础模型相当且可正向解释;与基础模型 embedding 混合时,空间特征贡献约 25% 重要性。
- 突变:MSI 预测 DACHS AUC 0.85(5 折)、7 个外部队列 0.78;TCGA 上 BMPR2/BRAF/TP53 AUC 0.78/0.75/0.66(关键特征 DEB entropy、MUC-TUM 交互)。
- 化疗分层:III 期用 LYM-MUC-CC 区分 ACT 反应,高碎片化 HR 9.08(ACT 更差),低碎片化 HR 0.29(获益),交互 HR 32.45,p=0.001;VirtualWSI 扰动诱导的状态转变可进一步细分获益亚组(HR 0.27,p=0.010)。
<!-- EN --> PrismNet macro-F1 0.948 / AUROC 0.988. MacroNet DSS C-index 0.716 on DACHS; KM HR 3.68/2.48/3.27 (MCO/CR07/TCGA). Individual spatial biomarkers reach C-index up to 0.73. SPM/FSPM C-index >0.7 with direct feature attribution; spatial features add ~25% importance when fused with foundation embeddings. MSI AUC 0.85 (DACHS) / 0.78 (external); BMPR2/BRAF/TP53 AUC 0.78/0.75/0.66 on TCGA. LYM-MUC-CC stratifies stage-III ACT benefit (interaction HR 32.45, p=0.001; high-fragmentation ACT harm HR 9.08, low-fragmentation benefit HR 0.29).

## 创新点 / Contributions
- <!-- ZH --> 用"语义分割 → 可量化空间特征谱(628 维)→ 透明线性模型"取代黑箱 embedding,实现 **前向可解释**(预测可直接归因到具体空间标志物),性能仍与 SOTA 基础模型相当。/ Forward-interpretable pipeline matching black-box foundation models.
- <!-- ZH --> **VirtualWSI**:结构保持的语义扰动框架 + 空间生物标志物图谱(UMAP atlas),把病理从"预测"变成可 in-silico 探索/反事实实验的平台。/ VirtualWSI perturbation + spatial-biomarker atlas for in-silico experimentation.
- <!-- ZH --> 闭环发现:模型解释 → 候选标志物量化验证 → LLM 组织成结构化、可实验的机制假设(5 位专家评审)。/ Closed-loop discovery with LLM-organized, expert-rated hypotheses.
- <!-- ZH --> 证明宏观空间架构编码了传统认为需细胞级分析的分子信息(MSI/BRAF/TP53),并揭示 III 期 CRC 中 ACT 获益的空间异质性。/ Macro-architecture encodes molecular status and reveals chemo-benefit heterogeneity.

## 局限 / Limitations
- <!-- ZH --> 依赖预定义语义组织类别,只能捕捉所选分割类别内的空间模式;迁移到新瘤种需重新标注、训练、验证 PrismNet(如 BRCA)。/ Bounded by predefined segmentation categories; new tumor types need re-annotation.
- <!-- ZH --> VirtualWSI 的语义扰动是"模型审讯"式探索,**不代表生物因果或物理可实现的组织状态**。/ Perturbations are exploratory model interrogation, not causal/physically realizable.
- <!-- ZH --> 预后模型性能处于"中等"区间(C-index ~0.7),ACT 等下游生物学解读均为假设生成、需进一步验证。/ Moderate accuracy; downstream biology is hypothesis-generating.
- <!-- ZH --> LLM 仅组织假设,不产生经验证的生物学结论。/ LLM organizes but does not validate hypotheses.

## 与本研究方向的关系 / Relation to our direction
<!-- anomaly detection → virtual tissue → revert via gene prediction 这条线上,这篇处在哪一环?能复用什么? -->
<!-- ZH --> 这篇几乎是我们"异常检测 → 虚拟组织 → 基因/干预回复异常"三段式路线在纯组织学(H&E)模态上的一个可解释范式,PI 标注为重点,值得逐环对照:
- **异常检测环**:MacroNet 的风险打分 + saliency 归因 + 结构保持反事实扰动,本质上定位"因疾病而改变、驱动不良预后"的空间区域(如 STR/TUM 无序、invasive front、SARIFA-like 浸润、LYM 连通性碎片化)。这正是我们要的"检测因疾病/扰动而变化的组织区域",且给出的是**可量化、可命名的空间标志物**而非扩散的热图 —— 直接可迁移为异常评分与异常定位的可解释基线。
- **虚拟组织环**:**VirtualWSI 就是一个"virtual tissue"引擎**——在保持全局结构的前提下对语义通道(如 MUC、LYM)做连续强度扰动,并把样本在 628 维空间生物标志物 atlas 中的轨迹可视化。它给出了"如何在可解释隐空间里对组织做受控编辑并观察表型漂移"的完整工程范式,是我们建虚拟组织/反事实组织最直接的方法学参照(注意:作者明确其为模型审讯,非物理因果)。
- **回复/干预环**:本文的"revert"发生在**空间标志物层面**而非基因层面 —— 例如"增大 LYM 一致降低风险分""增加 NORM/LYM 降低高风险患者风险",以及扰动诱导的 ACT 获益状态转变。它演示了"扰动哪个空间轴能把高风险表型推回低风险"的闭环,但**缺少到具体基因/药物靶点的映射**。BRCA 部分把空间标志物(STR-ACL、ADI-NEC-BT2)与 ERBB2/TOP1/TACSTD2 表达做了相关(但相关性"modest"),提示"空间标志物 ↔ 基因表达"这一桥的可行性与不足 —— 这正是我们要补的关键一环:把 PathPrism 的空间异常轴与空间转录组/基因预测耦合,预测"调控哪些基因可逆转异常"。
- **总结定位**:PathPrism 覆盖我们路线的前两环(异常检测、虚拟组织)且提供了可解释、可扰动的组织表示;第三环(基因层面的 revert)是明确的接口与空白点。可把它当作 H&E 模态的可解释异常/虚拟组织骨架,再对接我们的空间-omics 基因预测模块。
<!-- EN --> This paper maps almost one-to-one onto our anomaly→virtual-tissue→gene-revert pipeline for the H&E modality (PI-flagged as important): MacroNet's risk score + saliency + structure-preserving counterfactuals localize disease-driven anomalous regions as named, quantifiable spatial biomarkers (reusable as an interpretable anomaly-scoring/localization baseline). VirtualWSI is essentially a virtual-tissue engine — controlled, structure-preserving semantic-channel perturbation with trajectory visualization in a 628-dim biomarker atlas — the most directly reusable methodology for building counterfactual/virtual tissues (authors stress it is model interrogation, not physical causality). "Revert" here operates at the spatial-biomarker level (e.g., amplifying LYM lowers risk; perturbation-induced ACT-benefit state transitions), not the gene level; the BRCA section only weakly links spatial biomarkers to ERBB2/TOP1/TACSTD2 expression, exposing exactly the missing bridge our work must add: coupling PathPrism's spatial anomaly axes to spatial-omics/gene prediction to name genes whose modulation reverts the anomaly.

## 可复用资产 / Reusable assets
<!-- 代码、预训练模型、数据集、评测协议。 / Code, checkpoints, datasets, eval protocols. -->
- <!-- ZH --> **代码**:PathPrism 全流水线 <https://github.com/KatherLab/PathPrism>(含 PrismNet、MacroNet、628 空间特征提取、SPM/FSPM、VirtualWSI、LLM 工作流)。相关:STAMP 流水线 <https://github.com/KatherLab/STAMP>。
- <!-- ZH --> **数据/评测**:CRC100K 分割数据(NCT-CRC-HE-100K-NONORM 训练 / CRC-VAL-HE-7K 测试,Zenodo record 1214456);TCGA-CRC/CPTAC WSI+分子数据(GDC、cBioPortal 公开)。评测协议:5 折 CV + 外部队列 bootstrap 95% CI;预后 C-index、KM/HR;分类 AUROC/AUC;SHAP 特征贡献。
- <!-- ZH --> **可复用组件**:UNI+PCA 的高效 patch 语义分割配置;8 类 CRC 组织本体;单/多组织 slide-level 图特征定义(Tables S2/S3);Cox interaction 框架(识别 ACT-benefit 预测标志物);结构保持反事实/语义扰动实现(VirtualWSI)。
- <!-- ZH --> **受限数据**:DACHS、MCO、CR07、IDEA、HeCOG、GECCO 为敏感数据,需按各机构/consortium 流程申请。

## 待读 / Follow-ups
- <!-- ZH --> 精读 STAR Methods:PrismNet(UNI+PCA 配置、部分标注迁移)、MacroNet 架构与 saliency、628 图特征的精确定义(Figure S4A、Tables S2/S3)。
- <!-- ZH --> VirtualWSI 的具体扰动算子实现(通道强度 α、结构保持约束),评估能否改造为空间-omics 的虚拟组织/反事实生成器。
- <!-- ZH --> 复现 github.com/KatherLab/PathPrism,跑通 CRC100K 分割 + DACHS/TCGA 预后,作为我们 H&E 异常检测基线。
- <!-- ZH --> 对接点:把 STR-ACL↔ERBB2/TOP1、ADI-NEC-BT2↔TACSTD2 这类"空间标志物↔基因"相关分析扩展为预测式基因回复模型(结合空间转录组)。
- <!-- ZH --> 关联阅读:同期 Cancer Cell "From prediction to interpretation in computational pathology"(S1535-6108(26)00290-4)与 Cell "virtual spatial tumor profiling from histopathology"(S0092-8674(26)00590-8)。

## 引用 / Cite
```bibtex
% no BibTeX fetched
```
