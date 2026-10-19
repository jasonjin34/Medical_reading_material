---
title: Identifying 3D signal overlaps in spatial transcriptomics data with ovrlpy
aliases:
- ovrlpy
plans:
- A
track:
- A2
year: 2026
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

# Identifying 3D signal overlaps in spatial transcriptomics data with ovrlpy

> ovrlpy computationally "splits" a 5–15-µm imaging-based spatial-transcriptomics section into virtual top and bottom sub-slices and compares their local expression similarity, producing an unsupervised, segmentation-free vertical signal integrity (VSI) map that localizes vertically overlapping cells (z-axis doublets), tissue folds and inaccurate segmentation.

> ovrlpy 把成像型空间转录组的 5–15 µm 厚切片在计算上「虚拟切成上下两层」,比较上下层的局部表达相似度,得到一张无监督、无需分割的垂直信号完整性(VSI)图,用来定位垂直重叠细胞(z 轴双细胞)、组织褶皱和不准确的细胞分割。

## Related papers / 相关论文
- [[_maps/papers/resolvi-natmethods-2026|ResolVI]] — cites
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — technical vs anatomic anomaly map
- [[_maps/papers/xenium-split-natmethods-2026|Xenium contamination (SPLIT)]] — Xenium contamination

## Concepts / 概念
- [[_maps/concepts/anomalous-region|Anomalous tissue regions]]
- [[_maps/concepts/doublet|Doublets]]
- [[_maps/concepts/spillover|Signal spillover]]
- [[_maps/concepts/xenium|Xenium]]

## Deep-read / 精读

![[papers/ovrlpy-natbiotech-2026/deep-read]]
