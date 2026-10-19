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
recommended_by: sikander
views:
- sikander
- ehr
- overview
tags:
- paper
- plan/EHR
---

# A machine learning approach to leveraging electronic health records for enhanced omics analysis

> COMET (Aghaeepour lab, Stanford): omics studies often have tens to hundreds of samples while the same hospital's EHR covers tens of thousands — pretrain a GRU on the large EHR-only cohort, transfer its weights into a multimodal EHR + omics network that blends early and late fusion, and both prediction and the biological plausibility of selected proteins improve, in a 61-person pregnancy proteomics cohort and a 559-person UK Biobank cancer proteomics cohort.

> COMET(Aghaeepour 组,Stanford):组学研究往往只有几十到几百个样本,而同一医院的 EHR 有几万人 —— 先在「只有 EHR」的大队列上预训练一个 GRU,再把权重迁移进 EHR + 组学的多模态网络(早融合与晚融合混合),在 61 人妊娠蛋白组和 559 人 UK Biobank 癌症蛋白组上都提升了预测,并让模型挑出的蛋白更符合已知生物学。

## Related papers / 相关论文
- [[_maps/papers/ehr-apollo-arxiv-2026|APOLLO virtual patient]] — EHR pretraining → transfer
- [[_maps/papers/ehr-delphi2m-nature-2025|Delphi-2M]] — UK Biobank EHR modelling

## Concepts / 概念
- [[_maps/concepts/cross-modal|Cross-modal agreement]]
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/spatial-omics|Spatial omics]]

## Deep-read / 精读

![[papers/ehr-comet-natmachintell-2025/deep-read]]
