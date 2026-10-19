---
title: 'CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional
  Normalizing Flows'
aliases:
- CFLOW-AD
plans:
- A
track:
- A0
year: 2022
relevance: medium
category: anomaly
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows

> CFLOW-AD trains, for each scale of an ImageNet-pretrained CNN encoder, a normalizing-flow decoder conditioned on positional encoding that estimates the exact log-likelihood of each patch feature as the anomaly score. The authors show that under a multivariate-Gaussian prior the flow objective reduces to the Mahalanobis distance (so PaDiM is a special case), and CFLOW-AD reaches 98.26% detection AUROC, 98.62% localization AUROC and 94.60% AUPRO on MVTec while being ~10× faster and smaller than PaDiM/SPADE in the same setting.

> CFLOW-AD 在 ImageNet 预训练 CNN 编码器的多尺度特征上,为每个尺度训练一个以位置编码为条件的 normalizing flow 解码器,直接估计每个 patch 特征的精确对数似然作为异常分数;作者证明在多元高斯先验下 flow 目标退化为 Mahalanobis 距离(即 PaDiM 是其特例),而 CFLOW-AD 在 MVTec 上达到 98.26% 检测 AUROC、98.62% 定位 AUROC、94.60% AUPRO,并比同设置的 PaDiM/SPADE 快且小约 10 倍。

## Related papers / 相关论文
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — Gaussian prior as special case
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — main benchmark
- [[_maps/papers/padim-icpr-2020|PaDiM]] — flow likelihood generalises PaDiM's Gaussian
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — cites
- [[_maps/papers/sardine-bioinformatics-2025|Sardine]] — density-based anomaly scoring

## Deep-read / 精读

![[papers/cflow-ad-wacv-2022/deep-read]]
