# A Deep Learning-Based Pathomics Methodology for Quantifying and Characterizing Nucleated Cells in the Bone Marrow Microenvironment

> **Bibkey** `pathomics-blood-2023` · **Venue** Blood, ASH 2023 Abstract 2294 (2023) · **Category** pathology · **Relevance** medium · **Access** abstract-only
> **Link** <https://ashpublications.org/blood/article/142/Supplement%201/2294/499845>
> `status: complete` — 会议摘要,无全文正文;以下基于公开摘要撰写。若日后有海报 PDF,放入本文件夹 `source.pdf` 后可补全。

---

## 一句话 / One-liner
一个把骨髓活检全切片(WSI)中有核细胞、脂肪细胞及可评估造血组织自动分割,并从核形态提取 shape/texture/color 特征的深度学习 pathomics 流程,用于客观、可扩展、分区域地刻画 MPN 骨髓微环境。

## 研究问题 / Problem
骨髓整体细胞密度(cellularity)是 WHO 区分 BCR-ABL 阴性骨髓增殖性肿瘤(MPN,如真性红细胞增多症 PV 与骨髓纤维化 MF)的标准之一,但由病理医生人工评估存在三大缺陷:主观、不可规模化、且只给出单一的全局数值,忽略了骨髓内部的区域异质性。

## 方法 / Method
结合深度学习与经典图像分析:先在骨髓 WSI 上分割出有核细胞、脂肪细胞及其它可评估的造血组织区域;再对分割得到的细胞核提取形状(shape)、纹理(texture)、颜色(color)特征,构建可解释的下游分析。整体是一个 pilot、proof-of-concept 的 pathomics pipeline。(具体网络结构、分割模型、特征维度等细节仅摘要不可得 / abstract-only)

## 数据 / Data
骨髓活检全切片图像(WSI),涉及 BCR-ABL 阴性 MPN(PV、MF 等)。这是 pilot 研究,未来计划扩展到更大规模、涵盖其它 MPN 亚型的诊断 WSI 队列。具体样本量、染色、扫描来源仅摘要不可得 / abstract-only。

## 主要结果 / Key results
产出了一个实用且可解释的 pathomics pipeline 及下游分析,作为 hypothesis-driven 研究的概念验证;能对骨髓微环境做分区域、量化的刻画。摘要未给出具体分割精度、AUC 或分类等定量指标 / abstract-only。

## 创新点 / Contributions
- 把单一全局 cellularity 评分升级为分区域、可量化的骨髓微环境刻画,规避人工评估的主观性与不可扩展性。
- 联合深度学习分割 + 经典图像分析 + 核级 shape/texture/color 特征,强调可解释性(interpretable)。
- 面向 MPN 的端到端 pathomics 流程雏形,可对接免疫细胞检测等其它模型。

## 局限 / Limitations
- 仅为 pilot / proof-of-concept,无定量指标、无外部验证。
- 队列规模小、亚型覆盖有限(主要 PV/MF)。
- 会议摘要,方法与数据细节不公开,无代码/权重发布。

## 与本研究方向的关系 / Relation to our direction
主要落在 **virtual tissue / 组织表征** 这一环的上游——它把骨髓组织解构为「有核细胞 / 脂肪 / 可评估区域」的分割图,并给每个核附上量化的 shape/texture/color 特征,本质上是在为骨髓构建一个可计算的"virtual tissue"表征基底。这种分区域、细胞核级的量化,天然支持下一步的 **anomaly detection**:正常 vs. MPN(或 PV vs. MF)的区域可作为"扰动 vs. 基线"来定位异常区域。但它不涉及基因层面的 revert 预测,也无空间转录组/蛋白组模态。可借鉴的是:核形态特征工程范式、分区域量化思路,以及"pathomics 特征 → 与免疫细胞检测等模型关联"的多模型组合策略,可作为 histopathology 分支上把组织映射为可计算特征的参考。

## 可复用资产 / Reusable assets
无公开代码、权重或数据集(会议摘要)。可复用的是方法学概念:骨髓 WSI 的有核细胞/脂肪分割 + 核级 shape/texture/color 特征 + 可解释下游分析的组合。相关可追踪工作:同组(Scandura lab / Weill Cornell)的 "Correlating Image-Level Nucleomorphologic Features with Molecular Subtypes of Myeloproliferative Neoplasms",可作为该 pipeline 的延续。

## 待读 / Follow-ups
- 追踪该组是否发表了带定量指标的全文版本(分割精度、亚型分类 AUC)。
- 对照:Haematologica "AI-based quantitative bone marrow pathology analysis for MPN";DSCENet (MICCAI 2024) MPN 亚型多模态分类。
- 该组 nucleomorphologic features ↔ MPN 分子亚型 的相关性工作(是否可桥接到基因层面)。

## 引用 / Cite
```bibtex
@article{krichevsky2023pathomics,
  title   = {A Deep Learning-Based Pathomics Methodology for Quantifying and Characterizing Nucleated Cells in the Bone Marrow Microenvironment},
  author  = {Krichevsky, Spencer and Ouseph, Madhu M. and Zhang, Yuwei and Abu-Zeinah, Ghaith and Scandura, Joseph M. and Gupta, Rajarsi},
  journal = {Blood},
  volume  = {142},
  number  = {Supplement 1},
  pages   = {2294},
  year    = {2023},
  doi     = {10.1182/blood-2023-191272},
  note    = {65th ASH Annual Meeting, Abstract 2294}
}
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
