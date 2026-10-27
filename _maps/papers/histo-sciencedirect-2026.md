---
title: Spatial biomarker discovery via interpretable semantic learning in histopathology
aliases:
- Spatial biomarker discovery
plans: []
track: []
year: 2026
relevance: high
category: histopath
recommended_by: sikander
views:
- sikander
- overview
tags:
- paper
---

# Spatial biomarker discovery via interpretable semantic learning in histopathology

> PathPrism segments colorectal-cancer H&E whole-slide images (WSIs) into 8-class tissue maps, turns each map into 628 mathematically defined spatial features (tissue fractions, spatial entropy, tissue-graph features), and fits linear models for prognosis, mutations and chemotherapy benefit; VirtualWSI then perturbs the tissue map ("grow / shrink one tissue class") and tracks how risk and features move.

> PathPrism 先把结直肠癌 H&E 全切片(WSI)分割成 8 类组织的语义图,再把语义图拆成 628 个有数学定义的空间特征(组织占比、空间熵、组织图特征),用线性模型预测预后、突变和化疗获益;VirtualWSI 在这张语义图上做"放大/缩小某类组织"的虚拟扰动,观察风险分和特征如何变化。

## Related papers / 相关论文
- [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — reconstruct-to-normal

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/perturbation|Perturbation & counterfactual]]

## Deep-read / 精读

![[papers/histo-sciencedirect-2026/deep-read]]
