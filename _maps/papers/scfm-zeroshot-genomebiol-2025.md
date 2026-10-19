---
title: Zero-shot evaluation reveals limitations of single-cell foundation models
aliases:
- scFM zero-shot limits
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

# Zero-shot evaluation reveals limitations of single-cell foundation models

> Using scGPT and Geneformer cell embeddings zero-shot — no fine-tuning — for cell-type clustering and batch integration, both generally underperform simply selecting HVGs, Harmony and scVI across five datasets; they even struggle at their own pretraining task (masked expression reconstruction) — scGPT without cell embeddings does worse than predicting the mean.

> 不做任何微调、直接用 scGPT 与 Geneformer 的细胞嵌入做细胞类型聚类与批次整合,它们在五个数据集上普遍不如「选 HVG」、Harmony 与 scVI;连预训练任务本身(掩码表达重建)也做得勉强 —— scGPT 不加细胞嵌入时甚至不如「预测均值」。

## Related papers / 相关论文
- [[_maps/papers/linear-baselines-natmethods-2025|Linear baselines win]] — cites
- [[_maps/papers/nephrobase-biorxiv-2025|Nephrobase Cell+]] — single-cell FM evaluation
- [[_maps/papers/nicheformer-natmethods-2025|Nicheformer]] — cites

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/zero-shot|Zero-shot use]]

## Deep-read / 精读

![[papers/scfm-zeroshot-genomebiol-2025/deep-read]]
