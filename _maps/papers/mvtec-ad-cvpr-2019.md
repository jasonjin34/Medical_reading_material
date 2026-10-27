---
title: MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection
aliases:
- MVTec AD
plans:
- A
track:
- A0
year: 2019
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

# MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection

> MVTec AD is the first unsupervised anomaly-detection dataset aimed at real industrial inspection with multiple objects, multiple defect types and pixel-precise ground truth: 15 categories (5 textures + 10 objects), 5,354 high-resolution images, 73 defect types and 1,888 hand-annotated anomalous regions, with defect-free images only in training. The paper also benchmarks AnoGAN, L2/SSIM autoencoders, a CNN feature dictionary, a GMM texture model and a variation model, concluding that no method works well on every category. It became the standard benchmark for virtually all visual AD methods since, including PaDiM, PatchCore, DRÆM and CFLOW-AD.

> MVTec AD 是第一个面向真实工业检测、多物体、多缺陷、带像素级真值的无监督异常检测数据集:15 个类别(5 纹理 + 10 物体)、5,354 张高分辨率图像、73 种缺陷、1,888 个手工标注的异常区域;训练集只含无缺陷图像。论文同时给出 AnoGAN、L2/SSIM 自编码器、CNN 特征字典、GMM 纹理模型、variation model 的初始基准,结论是没有一种方法在所有类别上都好。它此后成为 PaDiM、PatchCore、DRÆM、CFLOW-AD 等几乎所有视觉 AD 方法的标准评测集。

## Related papers / 相关论文
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — benchmarks on MVTec AD
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] — GAN baseline
- [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — main benchmark
- [[_maps/papers/draem-iccv-2021|DRAEM]] — cites
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — sensory-AD benchmark
- [[_maps/papers/meatrd-aaai-2025|MEATRD]] — cites
- [[_maps/papers/padim-icpr-2020|PaDiM]] — main benchmark
- [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — main benchmark
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — cites

## Deep-read / 精读

![[papers/mvtec-ad-cvpr-2019/deep-read]]
