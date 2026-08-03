# A Deep Learning-Based Pathomics Methodology for Quantifying and Characterizing Nucleated Cells in the Bone Marrow Microenvironment

> **Bibkey** `pathomics-blood-2023` · **Venue** Blood, ASH 2023 Abstract 2294 (2023) · **Category** pathology · **Relevance** medium · **Access** abstract-only
> **Link** <https://ashpublications.org/blood/article/142/Supplement%201/2294/499845>
> `status: complete` — 会议摘要,无全文正文;以下基于公开摘要撰写。若日后有海报 PDF,放入本文件夹 `source.pdf` 后可补全。

---

## 一句话 / One-liner
<!-- ZH --> 一个把骨髓活检全切片(WSI)中有核细胞、脂肪细胞及可评估造血组织自动分割,并从核形态提取 shape/texture/color 特征的深度学习 pathomics 流程,用于客观、可扩展、分区域地刻画 MPN 骨髓微环境。
<!-- EN --> A deep-learning pathomics pipeline that segments nucleated cells, fat cells, and evaluable hematopoietic regions on bone-marrow whole-slide images and extracts nuclear shape/texture/color features, enabling objective, scalable, region-resolved characterization of the MPN bone-marrow microenvironment.

## 研究问题 / Problem
<!-- ZH --> 骨髓整体细胞密度(cellularity)是 WHO 区分 BCR-ABL 阴性骨髓增殖性肿瘤(MPN,如真性红细胞增多症 PV 与骨髓纤维化 MF)的标准之一,但由病理医生人工评估存在三大缺陷:主观、不可规模化、且只给出单一的全局数值,忽略了骨髓内部的区域异质性。
<!-- EN --> Overall BM cellularity is a WHO criterion for distinguishing BCR-ABL- MPNs (e.g. PV vs. MF), yet manual hematopathologist assessment is subjective, not scalable, and records only a single global measure — discarding intra-marrow regional heterogeneity.

## 方法 / Method
<!-- ZH --> 结合深度学习与经典图像分析:先在骨髓 WSI 上分割出有核细胞、脂肪细胞及其它可评估的造血组织区域;再对分割得到的细胞核提取形状(shape)、纹理(texture)、颜色(color)特征,构建可解释的下游分析。整体是一个 pilot、proof-of-concept 的 pathomics pipeline。(具体网络结构、分割模型、特征维度等细节仅摘要不可得 / abstract-only)
<!-- EN --> Deep learning plus classical image analysis segments nucleated cells, fat cells, and other evaluable hematopoietic regions on BM WSIs; shape, texture, and color features are then extracted from segmented nuclei to feed interpretable downstream analytics. Presented as a pilot / proof-of-concept pipeline. (Network architecture, segmentation model, and feature dimensionality are not disclosed — abstract-only.)

## 数据 / Data
<!-- ZH --> 骨髓活检全切片图像(WSI),涉及 BCR-ABL 阴性 MPN(PV、MF 等)。这是 pilot 研究,未来计划扩展到更大规模、涵盖其它 MPN 亚型的诊断 WSI 队列。具体样本量、染色、扫描来源仅摘要不可得 / abstract-only。
<!-- EN --> Bone-marrow biopsy WSIs from BCR-ABL- MPNs (PV, MF, etc.). A pilot cohort, with planned scale-up to a large cohort of diagnostic WSIs across additional MPN subtypes. Sample size, staining, and scanner details are not public — abstract-only.

## 主要结果 / Key results
<!-- ZH --> 产出了一个实用且可解释的 pathomics pipeline 及下游分析,作为 hypothesis-driven 研究的概念验证;能对骨髓微环境做分区域、量化的刻画。摘要未给出具体分割精度、AUC 或分类等定量指标 / abstract-only。
<!-- EN --> Delivered a practical, interpretable pathomics pipeline with downstream analytics as a proof of concept for hypothesis-driven research, enabling region-resolved quantitative characterization of the BM microenvironment. No segmentation accuracy, AUC, or classification metrics are reported — abstract-only.

## 创新点 / Contributions
- <!-- ZH --> 把单一全局 cellularity 评分升级为分区域、可量化的骨髓微环境刻画,规避人工评估的主观性与不可扩展性。 <!-- EN --> Replaces a single global cellularity score with region-resolved, quantitative BM characterization, removing manual subjectivity and scalability limits.
- <!-- ZH --> 联合深度学习分割 + 经典图像分析 + 核级 shape/texture/color 特征,强调可解释性(interpretable)。 <!-- EN --> Couples DL segmentation with classical image analysis and interpretable nuclear shape/texture/color features.
- <!-- ZH --> 面向 MPN 的端到端 pathomics 流程雏形,可对接免疫细胞检测等其它模型。 <!-- EN --> An MPN-oriented end-to-end pathomics pipeline designed to compose with other models (e.g. immune-cell detection).

## 局限 / Limitations
- <!-- ZH --> 仅为 pilot / proof-of-concept,无定量指标、无外部验证。 <!-- EN --> Pilot / proof-of-concept only; no quantitative metrics or external validation.
- <!-- ZH --> 队列规模小、亚型覆盖有限(主要 PV/MF)。 <!-- EN --> Small cohort, limited subtype coverage (mainly PV/MF).
- <!-- ZH --> 会议摘要,方法与数据细节不公开,无代码/权重发布。 <!-- EN --> Conference abstract: method/data details undisclosed, no code or checkpoints released.

## 与本研究方向的关系 / Relation to our direction
<!-- anomaly detection → virtual tissue → revert via gene prediction 这条线上,这篇处在哪一环?能复用什么? -->
<!-- ZH --> 主要落在 **virtual tissue / 组织表征** 这一环的上游——它把骨髓组织解构为「有核细胞 / 脂肪 / 可评估区域」的分割图,并给每个核附上量化的 shape/texture/color 特征,本质上是在为骨髓构建一个可计算的"virtual tissue"表征基底。这种分区域、细胞核级的量化,天然支持下一步的 **anomaly detection**:正常 vs. MPN(或 PV vs. MF)的区域可作为"扰动 vs. 基线"来定位异常区域。但它不涉及基因层面的 revert 预测,也无空间转录组/蛋白组模态。可借鉴的是:核形态特征工程范式、分区域量化思路,以及"pathomics 特征 → 与免疫细胞检测等模型关联"的多模型组合策略,可作为 histopathology 分支上把组织映射为可计算特征的参考。
<!-- EN --> Sits at the upstream of the **virtual-tissue / tissue-representation** stage: it decomposes marrow into a segmentation map (nucleated cells / fat / evaluable regions) and attaches quantitative nuclear shape/texture/color features — effectively a computable "virtual tissue" substrate for bone marrow. Its region-resolved, nucleus-level quantification is a natural feeder for **anomaly detection** (normal vs. MPN, or PV vs. MF regions as perturbed-vs-baseline). It does not touch gene-level revert prediction and carries no spatial-omics modality. Reusable for us: the nuclear feature-engineering paradigm, the region-resolved quantification idea, and the pattern of correlating pathomics features with other detectors (e.g. immune-cell models) as a template for mapping histology into computable features on the pathology branch.

## 可复用资产 / Reusable assets
<!-- ZH --> 无公开代码、权重或数据集(会议摘要)。可复用的是方法学概念:骨髓 WSI 的有核细胞/脂肪分割 + 核级 shape/texture/color 特征 + 可解释下游分析的组合。相关可追踪工作:同组(Scandura lab / Weill Cornell)的 "Correlating Image-Level Nucleomorphologic Features with Molecular Subtypes of Myeloproliferative Neoplasms",可作为该 pipeline 的延续。
<!-- EN --> No public code, checkpoints, or dataset (conference abstract). Reusable at the conceptual level: BM-WSI nucleated/fat segmentation + nucleus-level shape/texture/color features + interpretable downstream analytics. Traceable companion work from the same group (Scandura lab / Weill Cornell): "Correlating Image-Level Nucleomorphologic Features with Molecular Subtypes of Myeloproliferative Neoplasms."

## 待读 / Follow-ups
- <!-- ZH --> 追踪该组是否发表了带定量指标的全文版本(分割精度、亚型分类 AUC)。 <!-- EN --> Track whether the group published a full paper with quantitative metrics (segmentation accuracy, subtype AUC).
- <!-- ZH --> 对照:Haematologica "AI-based quantitative bone marrow pathology analysis for MPN";DSCENet (MICCAI 2024) MPN 亚型多模态分类。 <!-- EN --> Compare with Haematologica "AI-based quantitative BM pathology analysis for MPN" and DSCENet (MICCAI 2024) multimodal MPN subtyping.
- <!-- ZH --> 该组 nucleomorphologic features ↔ MPN 分子亚型 的相关性工作(是否可桥接到基因层面)。 <!-- EN --> The group's nucleomorphologic-features ↔ molecular-subtype work (possible bridge to the gene level).

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

📄 **[AI-ready 全文/full-text extract →](ai-ready.md)**
