---
title: 'PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization'
aliases:
- PaDiM
plans:
- A
track:
- A0
year: 2021
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

# PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization

> PaDiM trains no network at all: it embeds every patch position with multi-layer features from an ImageNet-pretrained CNN, fits one multivariate Gaussian N(μ_ij, Σ_ij) per position over the normal training images, and at test time scores each patch by its Mahalanobis distance to produce an anomaly map — reaching 97.5% pixel AUROC / 92.1% PRO on MVTec AD with inference cost independent of training-set size.

> PaDiM 不训练任何网络:用 ImageNet 预训练 CNN 的多层特征给每个 patch 位置做 embedding,在每个位置上对正常训练图像拟合一个多元高斯 N(μ_ij, Σ_ij),测试时用 Mahalanobis 距离作为 patch 级异常分数,得到异常图;在 MVTec AD 上做到 97.5% 像素级 AUROC / 92.1% PRO,且推理成本与训练集大小无关。

## Related papers / 相关论文
- [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — flow likelihood generalises PaDiM's Gaussian
- [[_maps/papers/draem-iccv-2021|DRAEM]] — cites
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — Mahalanobis scoring on pretrained features
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — main benchmark
- [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — memory bank generalises per-position Gaussians
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — cites

## Deep-read / 精读

![[papers/padim-icpr-2020/deep-read]]
