# Systematic evaluation of single-cell multimodal data integration enhances cell type resolution and discovery of clinically relevant states in complex tissues

> **文献键** `Acera_Mateos_2026` · **来源** Genome Biology(2026) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1186/s13059-026-04002-4> · `status: complete`

---

## 一句话
作者在 19 位健康供体的肾皮质上同时做 3' scRNA-seq、5' scRNA-seq 与 10x multiome(snRNA + snATAC),得到 119,744 个细胞/核的基准数据集 mBDRC,并开发可解释的监督式分类器 scOMM,系统比较「水平(sc↔sn RNA)」「垂直(RNA↔ATAC 同一细胞)」「全局(mosaic/diagonal)」三类整合策略对肾细胞类型/状态分辨率的贡献;全局整合找回了单一模态里看不到的 WFDC2⁺ aTAL 亚群与产 EPO 的 Norn 细胞。

## 研究问题
大型器官图谱(HCA、KPMP 等)越来越多地混用 scRNA、snRNA、snATAC 等不同协议与模态,但「每种模态对识别哪些细胞类型/状态有独特贡献、整合到底带来多少增益」缺少系统评估。以往的 benchmark 多是在同一类 assay 内比较实验方法,或只比较批次校正算法;对肾这种细胞脆弱、上皮亚型呈连续梯度(DCT/CNT/PC)、存在 adaptive/injury 状态的复杂组织,缺乏有配对供体、多协议的真实基准数据。

## 方法
**实验设计**:多中心;33 份肾皮质样本(25 份来自有多份样本的供体 = paired,8 份 unpaired),来源于肾切除术中的正常组织,分装冷冻后分别做 3'/5' scRNA-seq 和 multiome。另有少量 Smart-seq2、scNMT-seq(数据不足,仅作补充);MERFISH 多次优化仍未得到可用数据。**注释**:锚定已有人肾参考(HCA kidney 等),两级注释 L1(12–14 个大类)与 L2(39 个类型/状态)。**scOMM**:基于前馈神经网络的参考映射分类器(R 包),直接在表达值(或 peaks / gene activity)上训练;用「把某基因置零后准确率下降 ≥10 个相对点」定义 feature importance(FI),从而可解释地比较各模态的 marker 贡献。在肾、PBMC、心脏 multiome 上对比 Seurat、CHETAH、scmap,与 Seurat label transfer 精度接近。**整合策略**:水平整合用 scVI(benchmark 最高分);ATAC 横向整合比较 SnapATAC2 Spectral-MNN、Signac LSI-Harmony、PeakVI、PoissonVI(Spectral-MNN 最好);垂直整合比较 SnapATAC2 multi-spectral 与优化后的 Seurat WNN;全局整合比较 MultiVI(mosaic,利用配对细胞)与 GLUE(diagonal,非配对)。**指标**:AUC(无监督聚类 vs scOMM 标签,specificity > 0.9)、Mahalanobis 距离 / 重叠比、binary cLISI(b-cLISI)、平均轮廓宽度(AWS)、marker 检出率(对照 HCA 参考 marker)。另做经验功效分析(方差分解、per-donor 均值/方差/检出率、purity、silhouette),以及用 LDSC 在细胞类型特异 CRE 上做高血压 / eGFR 遗传力富集。

## 数据
mBDRC:119,744 个高质量细胞/核,19 位健康供体(性别、年龄、BMI 多样),33 份样本;水平整合 97,125 个细胞/核;multiome 11 份样本 37,717 个配对核。外部验证:一个独立的公开肾 multiome + CosMx 空间转录组数据集(论文引用 [23]),以及一个人心脏图谱(3′ sc/snRNA + multiome)。原始数据 dbGaP phs004459;整合数据将通过 CELLxGENE 发布。

## 主要结果
- **sn vs sc 功效分析**:表达方差中 assay 解释中位 24%、细胞类型 13%、assay×细胞类型交互 6%、供体仅 3% —— 协议差异远大于供体差异。snRNA-seq 测到更多基因(dropout 更低)、更多细胞、簇纯度更高,在肾这类脆弱组织里多数细胞类型上信息量更大;但交互项说明两者互补。
- **水平整合**:PT 亚型(PT-S1、aPT、PT-S3)在 snRNA 中最准;TAL(C-TAL、aTAL)在 3' scRNA 中最准;MD、DCT1、CNT 等连续/低丰度群在 5' scRNA 中最好。整合后 Mahalanobis 距离多数升高,b-cLISI 在 CNT/DCT/PC 上提升(snRNA 与 5' scRNA 整合后 >0.8)。snRNA 的 marker 检出率在 POD、PC、DCT 约 0.5,为各协议最高;整合模型平衡各协议,并检出独有 marker(如 CNT-PC 的 PTP4A1)。
- **垂直整合**:WNN 几乎在所有细胞类型上都偏向 RNA 权重,稀释了 ATAC 贡献;multi-spectral 的轮廓分数更高,呈近似「加性」的互补效应(尤其 POD、PEC、C-TAL、IC-B),b-cLISI 在 aPT、CNT-PC、DCT1 上更高。scOMM 三变体中,直接用 peaks 的 Bridge 模型 AUC 最高;gene-activity 的 Cross-Modality 模型最差;genes+peaks 的 Integrated 模型并未超过 Bridge。
- **全局整合**:MultiVI(mosaic)与 GLUE(diagonal)无显著差异,且总体上并不优于更简单的组合;但对 adaptive 状态有利 —— aTAL1 的 b-cLISI 从垂直整合的 0.45 升至 mosaic 的 0.61。重聚类发现以 3' scRNA 为主的 WFDC2⁺ aTAL1_0(WFDC2/HE4 曾被提为狼疮肾炎与 CKD 血清标志物),以及 aFIB 中极罕见的产 EPO 的 Norn 细胞(DCN、TIMP1、CFD),两者在 snRNA 中几乎看不到。
- **外部复现**:在独立数据集中,Norn 与 WFDC2⁺ aTAL1_0 签名在疾病样本中显著上调(p < 0.01 / p < 0.001),在 CosMx 中分别定位于纤维母细胞与 Loop of Henle,并富集于纤维化 / 损伤上皮 niche;scOMM 投影也找回了两群。在外部肾数据中,ATAC 嵌入更好地分开 adaptive 群(aTAL1 b-LISI 0.69 vs RNA 0.55;aPT 0.81 vs 0.66),RNA 更好地分开远端小管(CNT、DCT1)。
- **遗传力**:MD 细胞对高血压与 eGFR 均有强富集;内皮与 VSMC/周细胞只富集高血压;在 CRE 选择中加入转录信号(Set 2/3)得到显著更高的遗传力富集。

## 创新点
- 首个供体匹配、四协议(3'/5' scRNA、snRNA、snATAC)的肾皮质多模态基准数据集 mBDRC。
- scOMM:可解释、按模态比较 marker 贡献的参考映射工具。
- 针对细胞类型特性给出整合策略的实用指南:哪类细胞该用哪种协议/整合方式。
- 找回并在外部数据与空间上验证了两个疾病相关的罕见状态(WFDC2⁺ aTAL、Norn)。

## 局限
- 跨协议的配对样本数有限,供体异质性会干扰 GRN/TF 推断等分析。
- 细胞类型识别缺少真正的 ground truth,只能依赖专家注释与模拟场景。
- 仅健康组织;Smart-seq2/scNMT-seq 未针对冷冻肾优化,MERFISH 失败;对其他组织的泛化有限(虽然在心脏上做了验证)。
- 部分 aTAL/Norn 的检出差异可能部分来自协议敏感性,作者认为是生物学差异,但无法完全排除技术偏倚。

## 与本研究方向的关系
这是伪影注入课题最直接的「数据层」参考:对 snRNA + snATAC(+ Xenium + H&E)这类多模态设计,这篇用健康供体量化了「哪些肾细胞状态只在某个模态里可见」。对 detect → model → revert 中的 **detect** 阶段,它给出两条硬约束:**(1) 协议效应(中位 24%)远大于供体效应(3%)**,所以任何「异常」打分都必须先在 assay 维度上对齐,否则模型会把协议差异当作异常;**(2) 模态间不一致并不总是伪影** —— aTAL、Norn 这类 adaptive/rare 状态恰恰只在部分模态中被看见,而它们在疾病样本中上调。这正是伪影注入课题「cross-modal agreement 区分伪影与疾病」需要细化的地方:不能简单把「跨模态不一致」判为伪影,而应结合细胞类型特异的模态灵敏度先验(本文给出了 PT→snRNA、TAL→3'、MD/DCT/CNT→5'、adaptive→ATAC 的经验表)。mBDRC 作为**健康参考**,可直接用于 KidneyAnomalyBench 的正常分布建模;WFDC2⁺ aTAL1_0 与 Norn 可作为专家可验证的「已知阳性异常状态」候选。对 Agent 可信度课题,scOMM 的 feature importance 与「整合并非总是提升」的结论,是 agent 在分析肾组学时常犯的过度结论的现成反例(例如声称「多模态整合必然更好」),可纳入组学特异的失败分类与 claim-to-evidence 校验用例。

## 可复用资产
- **分析代码**(MIT):
<https://github.com/mereulab/sc-multimodal-integration-benchmark> · Zenodo 10.5281/zenodo.17475964
- **scOMM**(R 包):
<https://github.com/mereulab/scOMM> · Zenodo 10.5281/zenodo.18061150
- **数据**:原始数据 dbGaP phs004459(受控访问);整合对象计划上 CELLxGENE。
- **评测指标组合**:AUC@specificity>0.9、Mahalanobis 重叠比、b-cLISI、AWS、FI 阈值 10 —— 可直接复用于评估我们自己的跨模态整合。

## 待读
- 论文引用 [23] 的独立肾 multiome + CosMx 数据集(可能与 KPMP / Lake 图谱相关),核对是否可作为伪影注入课题外部测试集。
- Lake et al. 2023 肾图谱(`lake-kidney-atlas-nature-2023`),本文 L1/L2 注释与之对齐。
- MultiVI、GLUE、SnapATAC2 原文,以及 Lee et al. 的 paired/unpaired RNA+ATAC 整合 benchmark。

## 引用
```bibtex
@article{Acera_Mateos_2026, title={Systematic evaluation of single-cell multimodal data integration enhances cell type resolution and discovery of clinically relevant states in complex tissues}, volume={27}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-026-04002-4}, DOI={10.1186/s13059-026-04002-4}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Acera-Mateos, Mario and Adiconis, Xian and Li, Jessica-Kanglin and Marchese, Domenica and Caratù, Ginevra and Hon, Chung-Chau and Tiwari, Prabha and Kojima, Miki and Vieth, Beate and Murphy, Michael A. and Simmons, Sean K. and Lefevre, Thomas and Claes, Irene and O’Connor, Christopher L. and Menon, Rajasree and Otto, Edgar A. and Ando, Yoshinari and Vandereyken, Katy and Kretzler, Matthias and Bitzer, Markus and Fraenkel, Ernest and Voet, Thierry and Enard, Wolfgang and Carninci, Piero and Heyn, Holger and Levin, Joshua Z. and Mereu, Elisabetta}, year={2026}, month=Mar }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
