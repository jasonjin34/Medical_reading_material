---
title: 'MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial
  Transcriptomics'
aliases:
- MEATRD
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

# MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics

> MEATRD is a follow-up from the STANDS group (Xu, Sun et al.): trained only on normal tissue, it treats each Visium spot as a graph node, reconstructs both its H&E patch and its gene expression (core: a masked graph dual-attention transformer, MGDAT, with target-node masking), then trains a Deep-SVDD-style one-class classifier on latent multimodal reconstruction errors for anomaly scoring. On 8 human breast-cancer ST datasets it reaches mean AUC 0.723 / F1 0.741, beating 9 image, ST and multimodal baselines, and catches visually subtle tumour edges.

> MEATRD 是 STANDS 同组(Xu、Sun 等)的后续工作:只用正常组织训练,把每个 Visium spot 作为图节点,同时重建其 H&E 图块与基因表达(核心是带目标节点 masking 的图双注意力 Transformer,MGDAT),再在潜在多模态重建误差上训练 Deep-SVDD 式的单类分类器做异常打分;在 8 个人乳腺癌 ST 数据上平均 AUC 0.723 / F1 0.741,超过 9 个图像、ST 与多模态基线,并能抓住肉眼难辨的肿瘤边缘。

## Related papers / 相关论文
- [[_maps/papers/hest1k-2024|HEST-1k]] — paired H&E + ST
- [[_maps/papers/sardine-bioinformatics-2025|Sardine]] — anomalous region detection
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — cites

## Concepts / 概念
- [[_maps/concepts/anomalous-region|Anomalous tissue regions]]
- [[_maps/concepts/cross-modal|Cross-modal agreement]]

## Deep-read / 精读

![[papers/meatrd-aaai-2025/deep-read]]
