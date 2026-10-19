---
title: 'Generalized Out-of-Distribution Detection: A Survey'
aliases:
- Generalized OOD survey
plans:
- A
track:
- A0
year: 2024
relevance: high
category: anomaly
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Generalized Out-of-Distribution Detection: A Survey

> Unifies five separately developed sub-fields — anomaly detection (AD), novelty detection (ND), open-set recognition (OSR), OOD detection and outlier detection (OD) — into one "generalized OOD detection" framework, distinguishing them along four dichotomies (covariate vs semantic shift, single- vs multi-class ID, whether ID classification is required, inductive vs transductive); systematically reviews OOD methods (classifier outputs, Outlier Exposure, gradients, Bayesian, foundation models, density, distance, reconstruction), runs a unified fair comparison on OpenOOD, and lays out challenges and future directions.

> 把异常检测(AD)、新颖性检测(ND)、开集识别(OSR)、OOD 检测和离群检测(OD)五个各自发展的子领域统一进一个「广义 OOD 检测」框架,用四个二分维度(检测协变量偏移还是语义偏移、ID 是单类还是多类、是否需要 ID 分类、归纳还是直推)厘清它们的区别;系统综述 OOD 检测方法(分类器输出、Outlier Exposure、梯度、贝叶斯、基础模型、密度、距离、重构),在 OpenOOD 上做统一公平对比,并列出挑战与未来方向。

## Related papers / 相关论文
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — sensory / semantic anomaly split
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] — one-class AD reviewed
- [[_maps/papers/draem-iccv-2021|DRAEM]] — AD method on far-OOD
- [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] — post-hoc output-based OOD
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — distance-based OOD
- [[_maps/papers/msp-ood-iclr-2017|MSP baseline]] — baseline in OpenOOD
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — sensory-AD benchmark

## Deep-read / 精读

![[papers/generalized-ood-survey-ijcv-2024/deep-read]]
