---
title: 'ResolVI: addressing noise and bias in spatial transcriptomics'
aliases:
- ResolVI
plans:
- A
- B
track:
- A2
- B7
year: 2026
relevance: high
category: spatial
recommended_by: ''
views:
- plan-a
- plan-b
- bridge
- overview
tags:
- paper
- plan/A
- plan/B
---

# ResolVI: addressing noise and bias in spatial transcriptomics

> resolVI is a VAE-based generative model in scvi-tools that sits downstream of any segmentation algorithm and decomposes each cell's observed counts into three parts — the cell's true expression, expression "diffused" in from neighbouring cells, and a per-slice constant non-specific background — removing spurious co-expression caused by molecule misassignment while producing a batch-corrected probabilistic latent representation that supports differential expression and differential niche-abundance testing.

> resolVI 是 scvi-tools 里的一个 VAE 生成模型,接在任意分割算法之后,把每个细胞的观测计数拆成三部分 —— 细胞自身的真实表达、从邻近细胞「扩散」进来的表达、以及每张切片恒定的非特异背景 —— 从而去除分子错配导致的虚假共表达,同时给出批次校正后的概率潜在表示,支持差异表达和空间邻域丰度检验。

## Related papers / 相关论文
- [[_maps/papers/mrvi-natmethods-2025|MrVI]] — scvi-tools generative models
- [[_maps/papers/ovrlpy-natbiotech-2026|ovrlpy]] — cites
- [[_maps/papers/xenium-split-natmethods-2026|Xenium contamination (SPLIT)]] — cites

## Concepts / 概念
- [[_maps/concepts/batch-effect|Batch effects]]
- [[_maps/concepts/benchmark-validity|Benchmark validity]]
- [[_maps/concepts/segmentation-error|Segmentation errors]]
- [[_maps/concepts/xenium|Xenium]]

## Deep-read / 精读

![[papers/resolvi-natmethods-2026/deep-read]]
