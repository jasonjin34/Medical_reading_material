# Detecting anomalous anatomic regions in spatial transcriptomics with STANDS

> **Bibkey** `Xu_2024` · **Venue** Nature Communications (2024) · **Category** spatial · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41467-024-52445-9>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
STANDS 是一个基于 GAN 的多样本空间转录组框架,以"只见过正常组织"的重构模型做异常检测,再对齐、再聚类,de novo 地识别并解剖疾病导致的异常组织域(ATD),无需预设 marker。

## 研究问题 / Problem
从多样本 ST 数据中"检测并解剖异常组织域"(DDATD)能揭示疾病的群体级与个体特异性致病因子。但现有方法要么依赖专家目检/预定义 marker(对新型异常域无效),要么缺乏无 marker 的多样本对齐机制,且严重受限于正常参考 ST 数据稀缺。此前没有方法能在多样本情境下做 de novo DDATD——即在不知道异常长什么样的前提下,同时识别跨样本共享的异常与样本特异的异常,并把它们拆成生物学上不同的亚域。

## 方法 / Method
STANDS 三大组件串联:
(1) **异常检测 C1**——在正常参考数据上训练一个 GAN,用 Graph Attention Network(GAT)编码基因表达、GAT-ResNet 编码组织学图像,再用 Transformer Fusion(TF)块融合多模态嵌入并重构正常 spot;测试时重构误差高的 spot 即异常(anomaly score)。当没有正常 ST 时,可用 scRNA-seq 作为替代参考(cross-modality)。含 memory bank 抑制 mode collapse。
(2) **多样本对齐 C2/C3**——Module II 通过非负映射矩阵 M 在参考与目标 spot 间建立"kin"配对;Module III 学习"style"-divergence 矩阵 S 做批次效应校正,用 style-transfer 把目标数据对齐到参考空间,同时保留原始尺度与语义;训练时排除已检出的异常、测试时再重对齐。
(3) **异常亚型 C3**——把 C1 的嵌入与重构残差融合,用 Discriminatively Enhanced Clustering(DEC)迭代精炼聚类,把异常划为共享或样本特异的亚域。

## 数据 / Data
多平台、多器官:人乳腺(10x Visium:健康 10x-hNB-v05 作参考,肿瘤 10x-hBC-G2/H1、纵向切片 A1–A6);人胰腺(scRNA-seq sc-hPD 作参考 → 10x-hPDAC 胰腺导管腺癌,cross-modality);小鼠胚胎(Slide-seqV2 ssq-mEmb-32/33/34、Stereo-seq Stereo-mEmb-S1/S2/S3);人肝/胰(健康肝 10x-hLCL-C73-C1 作参考 → 原发性硬化性胆管炎 10x-hPSC-A1/C1/D1);人肾细胞癌(10x-hRCC-C2/C3/C4)。模态涵盖空间基因表达 + 配对组织学图像,并支持 scRNA-seq 作参考。

## 主要结果 / Key results
单样本异常检测在 accuracy 与 F1 上稳定超过 Spatial-ID、CAMLU、scPred、CHETAH、scmap 等基线。多样本场景能同时抓到跨数据集共享的异常(如多个数据集里的浸润性癌)与各数据集特有的异常(某数据集的原位癌、另一数据集的脂肪组织)。Cross-modality(scRNA-seq 参考 → Visium 目标)对胰腺癌域检测仍取得最高 accuracy/F1。对齐上 iLISI/BatchKL/ASW_batch/ASW_type 综合优于 Harmony、ComBat、GraphST、STAligner,对齐后 GraphST 聚类 ARI 约 0.23–0.52 且高于基线。亚型划分的 Macro-F1、NMI 及新提出的 Multi-SGD 空间指标均最优。敏感性分析:去掉 1/3 参考 spot 使 AUC 降约 0.05–0.10,去掉 2/3 使假阳性升 2–3 倍,去掉某一正常域类型(如乳腺腺体)使该域假阳性升约 3.3 倍——说明参考的多样性关键。消融显示 memory bank、组织学图像、TF 块、非负映射均有实质贡献。

## 创新点 / Contributions
- 首个多样本 de novo DDATD 框架:无需预定义 marker,只用"正常"参考的重构误差检异常。
- 三合一(检测→对齐→亚型)统一 GAN 架构,融合多模态(GAT 表达 + GAT-ResNet 组织学 + TF fusion)。
- style-transfer + 非负映射矩阵的无 marker 多样本对齐,能剔除不可对齐的异常域再对齐。
- cross-modality:用 scRNA-seq 补正常 ST 参考稀缺。
- 新评测指标 Spatial Grouping Discrepancy(SGD/Multi-SGD),把空间结构纳入评估。

## 局限 / Limitations
- 高度依赖正常参考的质量与多样性;参考覆盖不足会显著抬高假阳性(实验显示可达 3.3×)。
- GAN 训练存在 mode collapse 风险,需 memory bank 缓解;整体流程较重、组件多。
- 检测/亚型的生物学意义仍需下游注释与湿实验佐证;论文未提供预训练权重。
- 主要在肿瘤/发育/纤维化数据验证,对更多病理与平台的泛化待测。

## 与本研究方向的关系 / Relation to our direction
这篇正好坐在我们 pipeline 的**第一环:anomaly detection**,而且是空间转录组模态、直接检测"因疾病改变的组织区域",高度对口。它的"只学正常、以重构误差判异常"范式,本质就是把正常组织当作 virtual normal tissue 模型,与我们"virtual tissue modelling"的思路一脉相承——STANDS 的 GAN 生成器可视为正常组织的生成式先验,重构残差即"偏离正常的程度",可直接作为异常评分与后续 revert 目标的定位图。对齐组件(style-transfer + 非负映射)解决了多样本批次问题,是我们做群体级 vs 个体特异异常必须的一环。**可直接复用于**:(a) 异常区域检测的强基线/骨干;(b) 其新指标 SGD/Multi-SGD 作为空间感知的评测协议;(c) cross-modality 参考思路(scRNA-seq → ST)缓解正常样本稀缺。**缺口**:它做到"检测 + 亚型",但没有做"预测哪些基因若被调控可 revert 异常"——这正是我们要在其重构残差/生成器之上接续的 gene-revert 环节(例如把生成器反演为"如何把异常 spot 拉回正常流形"的扰动方向)。

## 可复用资产 / Reusable assets
- **代码 / Code:** <https://github.com/Catchxu/STANDS> — GPL-3.0, Python 3.9+, `git clone … && python3 setup.py install`. 文档与 6 个教程(单/多数据集检测、对齐、亚型):<https://catchxu.github.io/STANDS/>。
- **评测协议 / Eval protocol:** Spatial Grouping Discrepancy (SGD: SGD_degree + SGD_cc) 与 Multi-SGD;并配 iLISI / BatchKL / ASW_batch / ASW_type / ARI / Macro-F1 / NMI 一整套。
- **数据集 / Datasets:** 10x-hNB-v05, 10x-hBC-G2/H1/A1–A6, sc-hPD, 10x-hPDAC, ssq-mEmb-32/33/34, Stereo-mEmb-S1/S2/S3, 10x-hLCL-C73-C1, 10x-hPSC-A1/C1/D1, 10x-hRCC-C2/C3/C4(具体登录号见论文 Data availability)。
- **架构模块 / Modules:** GAT 表达编码器、GAT-ResNet 组织学编码器、Transformer Fusion 块、memory-bank GAN、非负映射对齐、style-transfer、DEC 亚型聚类——均可拆件复用。
- **预训练 / Checkpoints:** 文档建议在大规模公共 ST 上预训练,但未发布现成权重(need to pretrain yourself)。

## 待读 / Follow-ups
- 精读 Supplementary:M/S 矩阵与 style-transfer 的具体损失与训练细节。 Read supplementary for exact M/S losses and style-transfer training.
- 跑通 GitHub 教程,评估把重构残差/生成器反演成 gene-revert 扰动方向的可行性。 Run the repo tutorials; test inverting the generator/residuals into gene-revert perturbation directions.
- 对比更近的 ST 异常检测/foundation-model 方法,定位 STANDS 作为骨干的取舍。 Compare with newer ST anomaly-detection / foundation-model methods to position STANDS as a backbone.
- 复现 SGD/Multi-SGD 指标,纳入我们自己的评测套件。 Reproduce SGD/Multi-SGD and fold into our eval suite.

## 引用 / Cite
```bibtex
@article{Xu_2024, title={Detecting anomalous anatomic regions in spatial transcriptomics with STANDS}, volume={15}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-024-52445-9}, DOI={10.1038/s41467-024-52445-9}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Xu, Kaichen and Lu, Yan and Hou, Suyang and Liu, Kainan and Du, Yihang and Huang, Mengqian and Feng, Hao and Wu, Hao and Sun, Xiaobo}, year={2024}, month=Sept }
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
