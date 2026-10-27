---
title: A machine learning approach to leveraging electronic health records for enhanced
  omics analysis
aliases:
- COMET (EHR + omics)
plans:
- EHR
track: []
year: 2025
relevance: medium
category: ehr
recommended_by: core-reading
views:
- reading-list
- ehr
- overview
tags:
- paper
- plan/EHR
---

# A machine learning approach to leveraging electronic health records for enhanced omics analysis

> COMET (Aghaeepour lab, Stanford): omics studies usually have tens to hundreds of samples while the matching EHR covers tens of thousands — pretrain a GRU on the large EHR-only cohort, transfer its frozen weights into a multimodal EHR + omics network that adaptively blends early and late fusion; on a 61-person pregnancy proteomics cohort (days to labour) and a 559-person UK Biobank cancer proteomics cohort (3-year mortality) it beats a same-architecture baseline without pretraining, and the proteins it relies on agree better with known biology (Abstract; Results).

> COMET(Aghaeepour 组,Stanford):组学研究通常只有几十到几百个样本,而同一来源的 EHR 有数万人 —— 先在「只有 EHR」的大队列上预训练一个 GRU,再把冻结的权重迁移进 EHR + 组学的多模态网络(早融合与晚融合的自适应混合);在 61 人妊娠蛋白组(预测距分娩天数)和 559 人 UK Biobank 癌症蛋白组(预测 3 年死亡)上,预测都优于同结构无预训练的基线,模型看重的蛋白也更符合已知生物学(Abstract;Results)。

## Related papers / 相关论文
- [[_maps/papers/ehr-apollo-arxiv-2026|APOLLO virtual patient]] — EHR pretraining → transfer
- [[_maps/papers/ehr-delphi2m-nature-2025|Delphi-2M]] — UK Biobank EHR modelling

## Concepts / 概念
- [[_maps/concepts/cross-modal|Cross-modal agreement]]
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/spatial-omics|Spatial omics]]

## Deep-read / 精读

![[papers/ehr-comet-natmachintell-2025/deep-read]]
