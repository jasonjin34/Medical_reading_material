---
title: 'Nicheformer: a foundation model for single-cell and spatial omics'
aliases:
- Nicheformer
plans:
- A
track:
- A5
year: 2025
relevance: medium
category: foundation
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Nicheformer: a foundation model for single-cell and spatial omics

> Nicheformer is a 49.3M-parameter transformer foundation model pretrained on SpatialCorpus-110M (57.06M dissociated + 53.8M image-based spatial cells, human and mouse, 73 tissues) with ranked gene tokens plus species/modality/technology context tokens. On newly designed spatial tasks (niche/region labels, neighbourhood composition, neighbourhood density) both linear probing and fine-tuning beat Geneformer, scGPT, UCE, CellPLM, scVI and PCA, and it transfers spatial context onto scRNA-seq.

> Nicheformer 是一个 49.3M 参数的 Transformer 基础模型,在 SpatialCorpus-110M(57.06M 解离细胞 + 53.8M 成像空间细胞,人和小鼠,73 个组织)上用排序基因 token + 物种/模态/技术上下文 token 预训练;在新设计的空间任务(niche/区域标签、邻域组成、邻域密度)上,linear probing 与微调都优于 Geneformer、scGPT、UCE、CellPLM、scVI、PCA,并能把空间上下文迁移到 scRNA-seq 上。

## Related papers / 相关论文
- [[_maps/papers/scfm-zeroshot-genomebiol-2025|scFM zero-shot limits]] — cites
- [[_maps/papers/xenium-split-natmethods-2026|Xenium contamination (SPLIT)]] — cites

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/segmentation-error|Segmentation errors]]
- [[_maps/concepts/xenium|Xenium]]

## Deep-read / 精读

![[papers/nicheformer-natmethods-2025/deep-read]]
