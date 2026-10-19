---
title: Anomaly detection in spatial transcriptomics via spatially localized density
  comparison
aliases:
- Sardine
plans:
- A
track:
- A3
year: 2025
relevance: high
category: spatial
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Anomaly detection in spatial transcriptomics via spatially localized density comparison

> Sardine formalizes "anomalous-region detection across conditions" in spatial transcriptomics as the spatially localized differential abundance region problem (SDARP): on multi-condition slices aligned to a common coordinate system, it takes a spatial neighbourhood around every spot, estimates densities on the expression-manifold kNN graph with MELD-style graph smoothing, and compares local densities between conditions — producing an interpretable anomaly score where 0.5 = no change and →1 = anomalous. It is more accurate and more spatially coherent than MELD, Vespucci and STANDS on simulations and two mouse Visium datasets.

> Sardine 把空间转录组的「条件间异常区域检测」形式化为空间局部化差异丰度问题(SDARP):在对齐到同一坐标系的多条件切片上,对每个 spot 取空间邻域、在表达流形 kNN 图上用 MELD 式图平滑做密度估计,比较两条件的局部密度,得到 0.5 = 无变化、→1 = 异常的可解释 anomaly score;在模拟和两个小鼠 Visium 数据上比 MELD、Vespucci、STANDS 更准、更空间连贯。

## Related papers / 相关论文
- [[_maps/papers/meatrd-aaai-2025|MEATRD]] — anomalous region detection
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — spatial anomaly detection

## Concepts / 概念
- [[_maps/concepts/anomalous-region|Anomalous tissue regions]]

## Deep-read / 精读

![[papers/sardine-bioinformatics-2025/deep-read]]
