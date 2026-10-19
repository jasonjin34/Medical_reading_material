---
title: Unbiased self supervised learning of kidney histology reveals phenotypic and
  prognostic insights
aliases:
- Kidney histology SSL
plans:
- A
track:
- A6
year: 2025
relevance: medium
category: histopath
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Unbiased self supervised learning of kidney histology reveals phenotypic and prognostic insights

> NYU (Tsirigos lab) with JHU/UPenn applies Histomorphological Phenotype Learning (HPL), a self-supervised framework first built for lung-cancer H&E, to 1,421 PAS-stained kidney WSIs: with no pathologist labels, tile embeddings are clustered into histomorphological phenotype clusters (HPCs) and each slide becomes a vector of HPC area fractions. The clusters are visually consistent across five internal/external sets, track pathologist quantifications such as interstitial fibrosis (MIL AUC 0.83), and predict kidney-function decline in the TRIDENT diabetic-nephropathy cohort.

> NYU(Tsirigos 组)与 JHU/UPenn 把原本为肺癌 H&E 开发的自监督框架 Histomorphological Phenotype Learning(HPL)用到 1,421 张 PAS 染色肾脏 WSI 上:不用任何病理标注,把 tile 嵌入聚成「组织形态表型簇」(HPC),每张切片表示为各 HPC 的面积占比向量;这些簇跨 5 个内外部队列视觉一致、与间质纤维化等病理定量相关(MIL 预测纤维化 AUC 0.83),并能预测 TRIDENT 糖尿病肾病队列的肾功能下降。

## Related papers / 相关论文
- [[_maps/papers/lake-kidney-atlas-nature-2023|Kidney atlas (Lake 2023)]] — histology vs molecular atlas
- [[_maps/papers/uni2-h-model|UNI2-h]] — UNI embeddings comparison

## Concepts / 概念
- [[_maps/concepts/batch-effect|Batch effects]]
- [[_maps/concepts/expert-validation|Expert validation]]

## Deep-read / 精读

![[papers/kidney-ssl-histology-scirep-2025/deep-read]]
