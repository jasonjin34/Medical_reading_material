---
title: Resolving sensitivity, specificity and signal contamination in Xenium spatial
  transcriptomics
aliases:
- Xenium contamination (SPLIT)
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

# Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics

> Using 41 breast-cancer and NSCLC sections from 27 donors (targeted Breast/Lung/Custom IO panels plus the 5K PRIME panel, with matched snRNA-seq and IHC), the authors systematically characterize Xenium sensitivity, specificity and transcript-spillover contamination, and propose SPLIT: take RCTD doublet-mode cell-type weights and split each contaminated cell's counts into "primary" and "secondary" parts according to reference profiles, keeping the purified primary profile.

> 作者用 27 位供者、41 张乳腺癌与非小细胞肺癌切片(靶向 Breast/Lung/Custom IO 面板 + 5K PRIME 面板,配匹配 snRNA-seq 与 IHC)系统刻画 Xenium 的灵敏度、特异性和转录本溢出(spillover)污染,并提出 SPLIT:用 RCTD doublet 模式的细胞类型权重,把每个被污染细胞的计数按参照谱拆成「主」「次」两部分,只保留主细胞类型的纯化表达。

## Related papers / 相关论文
- [[_maps/papers/ambient-rna-bench-biorxiv-2026|Ambient-RNA benchmark]] — wrong-cell signal contamination
- [[_maps/papers/dkd-spatial-atlas-nature-2026|DKD spatial atlas]] — Xenium artifacts
- [[_maps/papers/nicheformer-natmethods-2025|Nicheformer]] — cites
- [[_maps/papers/ovrlpy-natbiotech-2026|ovrlpy]] — Xenium contamination
- [[_maps/papers/resolvi-natmethods-2026|ResolVI]] — cites
- [[_maps/papers/spatialagent-biorxiv-2025|SpatialAgent]] — Xenium data

## Concepts / 概念
- [[_maps/concepts/doublet|Doublets]]
- [[_maps/concepts/segmentation-error|Segmentation errors]]
- [[_maps/concepts/spillover|Signal spillover]]
- [[_maps/concepts/xenium|Xenium]]

## Deep-read / 精读

![[papers/xenium-split-natmethods-2026/deep-read]]
