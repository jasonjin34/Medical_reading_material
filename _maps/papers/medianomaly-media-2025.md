---
title: 'MedIAnomaly: A comparative study of anomaly detection in medical images'
aliases:
- MedIAnomaly
plans:
- A
track:
- A6
year: 2025
relevance: medium
category: imaging
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# MedIAnomaly: A comparative study of anomaly detection in medical images

> Cai, Chen, Cheng et al. (HKUST) build MedIAnomaly, a unified medical-image AD benchmark — 7 datasets, 5 modalities (chest X-ray, brain MRI, fundus, dermoscopy, histopathology), 30 methods — comparing image-level classification and pixel-level segmentation under unified architectures, and dissecting key components one by one (latent size, reconstruction distance, gradient scores, DDPM noise type, ImageNet weights). Headline findings: a plain AE is a strong baseline, ImageNet features are surprisingly strong, and reconstruction quality correlates only weakly with detection performance.

> HKUST 的 Cai、Chen、Cheng 等搭建了医学图像 anomaly detection 的统一基准 MedIAnomaly:7 个数据集、5 种模态(胸片、脑 MRI、眼底、皮肤镜、病理)、30 种方法,在统一网络结构下比较图像级分类与像素级分割,并逐个拆解关键组件(latent 大小、重建距离函数、梯度分数、DDPM 噪声类型、ImageNet 权重),给出「朴素 AE 是强基线、ImageNet 特征出奇地强、重建质量与检测性能弱相关」等结论。

## Related papers / 相关论文
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — multi-paradigm AD taxonomy
- [[_maps/papers/draem-iccv-2021|DRAEM]] — synthetic-anomaly family
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — benchmarked (reconstruction family)
- [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — diffusion-based AD
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — cites

## Deep-read / 精读

![[papers/medianomaly-media-2025/deep-read]]
