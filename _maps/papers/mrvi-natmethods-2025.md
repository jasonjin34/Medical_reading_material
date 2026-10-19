---
title: Deep generative modeling of sample-level heterogeneity in single-cell genomics
aliases:
- MrVI
plans:
- A
track:
- A3
year: 2025
relevance: medium
category: single-cell
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Deep generative modeling of sample-level heterogeneity in single-cell genomics

> MrVI (multi-resolution variational inference, Yosef lab, built into scvi-tools) is a hierarchical deep generative model with two latent variables: u encodes cell state only (sample-agnostic), z adds sample effects on top of u (free of nuisance factors such as batch). Using counterfactuals — "what would this cell look like had it come from another sample?" — it stratifies samples at single-cell resolution (exploratory) and runs cluster-free DE and DA (comparative), finding sample-level differences that show up only in particular cell subsets in COVID-19, sci-Plex drug-screen and Crohn's disease cohorts.

> MrVI(multi-resolution variational inference,Yosef 组,scvi-tools 内置)是一个两层隐变量的层级深度生成模型:u 只编码细胞状态(与样本无关),z 在 u 基础上加入样本效应(与 batch 等 nuisance 无关);通过反事实——「这个细胞如果来自另一个样本会怎样」——在单细胞分辨率上做样本分层(exploratory)以及不依赖聚类的 DE 与 DA(comparative),在 COVID-19、sci-Plex 药物筛选和克罗恩病队列上发现了只在部分细胞亚群中体现的样本差异。

## Related papers / 相关论文
- [[_maps/papers/healthy-ref-natgenet-2023|Healthy-reference design]] — cites
- [[_maps/papers/resolvi-natmethods-2026|ResolVI]] — scvi-tools generative models
- [[_maps/papers/scrna-natmachintell-2026|Conditional Monge Gap]] — counterfactual effect modelling

## Deep-read / 精读

![[papers/mrvi-natmethods-2025/deep-read]]
