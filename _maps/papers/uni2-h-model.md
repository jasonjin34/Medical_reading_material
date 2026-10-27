---
title: MahmoodLab/UNI2-h
aliases:
- UNI2-h
plans:
- A
track:
- A5
year: 2025
relevance: medium
category: foundation
recommended_by: core-reading
views:
- plan-a
- reading-list
- overview
tags:
- paper
- plan/A
---

# MahmoodLab/UNI2-h

> UNI2-h is a pathology vision foundation model from the Mahmood Lab (Harvard / BWH): a 681M-parameter custom ViT-H/14 trained with the DINOv2 recipe on 200M+ H&E and IHC tiles from Mass General Brigham, mapping a 224×224 tissue tile to a 1,536-dim feature for frozen downstream use (model card §"Model Description", §"Training Details").

> UNI2-h 是 Mahmood Lab(Harvard / BWH)发布的病理视觉基础模型:一个 681M 参数的定制 ViT-H/14,用 DINOv2 配方在 Mass General Brigham 的 2 亿+ 个 H&E 与 IHC 图块上自监督训练,把 224×224 组织图块编码为 1,536 维特征,供下游冻结使用(model card §"Model Description"、§"Training Details")。

## Related papers / 相关论文
- [[_maps/papers/fm-arxiv-2604|Generative histopathology FM]] — pathology FM
- [[_maps/papers/kidney-ssl-histology-scirep-2025|Kidney histology SSL]] — UNI embeddings comparison
- [[_maps/papers/pathbench-natcommun-2026|Pathology FM benchmark]] — pathology FM benchmark
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — FM backbone → anomaly det.
- [[_maps/papers/virchow-2024|Virchow]] — pathology FM

## Deep-read / 精读

![[papers/uni2-h-model/deep-read]]
