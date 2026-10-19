---
title: Deep-learning-based gene perturbation effect prediction does not yet outperform
  simple linear baselines
aliases:
- Linear baselines win
plans:
- A
track:
- A5
year: 2025
relevance: high
category: foundation
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines

> For predicting transcriptomic effects of double perturbations and of unseen single perturbations, none of scGPT, scFoundation, GEARS, CPA, or scBERT / Geneformer / UCE with a linear decoder consistently beats "additive", "no change", "mean" or a simple bilinear model; the only consistent winner is a linear model whose perturbation embedding is pretrained on perturbation data from another cell line.

> 在双扰动与未见单扰动的转录组效应预测上,scGPT、scFoundation、GEARS、CPA 以及接线性解码器的 scBERT / Geneformer / UCE,没有一个稳定超过「加性」「不变」「均值」或一个简单的双线性模型;唯一稳定最好的是在另一细胞系的扰动数据上预训练扰动嵌入的线性模型。

## Related papers / 相关论文
- [[_maps/papers/scfm-zeroshot-genomebiol-2025|scFM zero-shot limits]] — cites
- [[_maps/papers/scrna-natmachintell-2026|Conditional Monge Gap]] — cites
- [[_maps/papers/virtual-cell-challenge|Virtual Cell Challenge]] — perturbation benchmark

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/he-to-expression|H&E → expression prediction]]
- [[_maps/concepts/linear-baseline|Simple / linear baselines]]

## Deep-read / 精读

![[papers/linear-baselines-natmethods-2025/deep-read]]
