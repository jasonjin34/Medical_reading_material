---
title: Towards Total Recall in Industrial Anomaly Detection
aliases:
- PatchCore
plans:
- A
track:
- A0
year: 2022
relevance: high
category: anomaly
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Towards Total Recall in Industrial Anomaly Detection

> PatchCore stores mid-level, neighbourhood-aggregated patch features of all normal training images in a memory bank, shrinks it to 1–25% with greedy coreset subsampling at almost no loss, and scores a test image by the distance of its most anomalous patch to that patch's nearest normal neighbour — 99.1% image AUROC on MVTec AD (up to 99.6% with an ensemble), more than halving PaDiM's error.

> PatchCore 把所有正常训练图像的中层、局部邻域聚合的 patch 特征存进一个 memory bank,用 greedy coreset 子采样把它压缩到 1–25% 而几乎不掉性能,测试时以"最远的那个 patch 到其最近正常邻居的距离"作为图像异常分数;在 MVTec AD 上图像级 AUROC 99.1%(集成可达 99.6%),把 PaDiM 的误差减半以上。

## Related papers / 相关论文
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — pretrained features + kNN distance
- [[_maps/papers/meatrd-aaai-2025|MEATRD]] — cites
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — main benchmark
- [[_maps/papers/padim-icpr-2020|PaDiM]] — memory bank generalises per-position Gaussians
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — cites
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — memory bank of normal features

## Deep-read / 精读

![[papers/patchcore-cvpr-2022/deep-read]]
