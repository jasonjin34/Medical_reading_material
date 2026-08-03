# Deep learning-based pathomics signature predicts prognosis and treatment response in gastric cancer: a multicenter retrospective study

> **Bibkey** `Wang_2026` · **Venue** npj Precision Oncology (2026) · **Category** pathology · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s41698-026-01381-6>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
用多尺度图神经网络 + 门控注意力多示例学习(MS-GMIL)直接从胃癌 H&E 全切片中提取病理组学特征,构建可解释的预后签名 PSGC,用于预测总生存并指导化疗/免疫治疗决策。

## 研究问题 / Problem
现行 TNM 分期在胃癌(GC)中提供的预后信息不足,同分期患者结局差异大,难以据此制定个体化治疗。作者希望不依赖人工特征,直接从常规 H&E 切片中挖掘预后信号,并把它变成能指导化疗与免疫治疗决策的可解释指标。

## 方法 / Method
提出 MS-GMIL:多尺度(multi-scale)图神经网络 + 门控注意力(gated attention)机制的多示例学习(MIL),以全切片图像为输入、切片级弱标签监督,直接预测总生存(OS)。将 MS-GMIL 深度特征与传统机器学习结合,最终构建由 **11 个特征**组成的病理组学签名 PSGC。用 SHAP 与 pathogenomics 分析对签名做可解释性归因,并结合转录组数据探究其病理生理机制。(架构公式/超参等细节仅摘要与公开页可得,正文付费。)

## 数据 / Data
多中心回顾性队列,共 **3,138 例**胃癌患者(中位年龄 60 岁,男性占 71.64%,2,248/3,138),分为训练与验证等多个队列。模态:H&E 数字病理全切片(WSI);另有配对转录组数据用于机制分析。具体各中心/队列名称与样本划分数目未在公开页完整呈现(仅摘要可得)。

## 主要结果 / Key results
PSGC 在**所有队列**中均为独立预后因子。高 PSGC 的 II/III 期患者可从化疗获得显著获益,并对免疫治疗有效响应,提示其可作为疗效预测标志物。可解释性分析显示,驱动 PSGC 的主要组织学特征为肿瘤细胞间变(anaplasia)、上皮内瘤变、肿瘤间质纤维化与肠上皮化生;转录组层面与细胞周期调控、耐药通路及癌症进展机制相关。具体判别指标(C-index/HR/AUC/p 值)在公开页不可见(仅摘要可得,不臆造)。

## 创新点 / Contributions
- MS-GMIL:把多尺度图结构与门控注意力 MIL 结合,直接从 WSI 端到端学习预后,而非依赖预定义人工病理特征。
- 大规模多中心验证(3,138 例),PSGC 在所有队列均为独立预后因子。
- 不止预后,还能预测 II/III 期的化疗获益与免疫治疗响应,具临床决策价值。
- SHAP + pathogenomics 双重可解释,把黑箱签名映射到具体组织学特征与分子通路。

## 局限 / Limitations
- 回顾性设计,缺乏前瞻性/随机对照验证;治疗获益结论为分层观察而非 RCT。
- 单一癌种(胃癌)与单一模态(H&E),跨癌种/跨染色泛化性未知。
- 关键定量指标、代码与数据可得性在公开页不可见,难以独立复现。
- 队列以中国单/多中心为主(人群偏倚可能),外部广谱人群适用性待验证。

## 与本研究方向的关系 / Relation to our direction
主要落在 **anomaly-detection / 组织表征**这一环:MS-GMIL 的门控注意力权重本质上是在 WSI 上定位"与预后相关的异常区域",可直接为我们的病理异常检测(哪些切片区域因疾病而改变)提供 attention-based 定位思路与弱监督范式。其 **pathogenomics 桥接**(把病理签名与转录组通路、耐药机制关联)对 **virtual tissue → gene-revert** 环节最有借鉴:它示范了如何将影像表型映射到可干预的分子通路(细胞周期、耐药),这正是"预测调控哪些基因可逆转异常"所需的影像-分子对应关系。可复用为:异常区域注意力定位模块 + 影像→通路关联的分析协议。它不直接做基因逆转预测,但提供了连接病理异常与分子靶点的中间层。

## 可复用资产 / Reusable assets
方法层面可复用:①MS-GMIL 的多尺度图 + 门控注意力 MIL 架构(用于 WSI 弱监督表征/异常定位);②SHAP + pathogenomics 的可解释评测协议(签名→组织学特征→分子通路)。具体的代码仓库、预训练 checkpoint、数据集与 data/code availability 声明在公开页均不可见(仅摘要可得),需获取全文核实。数据规模 3,138 例可作对标基准。

## 待读 / Follow-ups
- 获取全文,核实 MS-GMIL 架构细节(图构建、多尺度融合、注意力公式)与 C-index/HR/AUC 等指标。
- 查 data/code availability,是否开源模型或特征。
- 对比前作 Nat Commun 2022 "Prognostic and predictive value of a pathomics signature in gastric cancer" 以定位增量。

## 引用 / Cite
```bibtex
@article{Wang_2026, title={Deep learning-based pathomics signature predicts prognosis and treatment response in gastric cancer: a multicenter retrospective study}, volume={10}, ISSN={2397-768X}, url={http://dx.doi.org/10.1038/s41698-026-01381-6}, DOI={10.1038/s41698-026-01381-6}, number={1}, journal={npj Precision Oncology}, publisher={Springer Science and Business Media LLC}, author={Wang, Hao and Li, Hao and Ma, Keru and Mo, Genshen and Yan, Meihong and Zhang, Xinyue and Xie, Haonan and Huang, Yuze and Li, Huiying and Xue, Yingwei and Han, Peng and Lou, Shenghan}, year={2026}, month=Apr }
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
