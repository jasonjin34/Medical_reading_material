---
title: DRÆM – A discriminatively trained reconstruction embedding for surface anomaly
  detection
aliases:
- DRAEM
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

# DRÆM – A discriminatively trained reconstruction embedding for surface anomaly detection

> DRÆM recasts surface anomaly detection from "learn normal only, read the reconstruction error" into a discriminative problem: it pastes "just-out-of-distribution" synthetic anomalies onto normal images (Perlin-noise masks + external textures) and jointly trains a reconstructive sub-network that inpaints them back to normal and a discriminative sub-network that reads "original ⊕ reconstruction" and outputs a pixel-level anomaly map — 98.0% image AUROC and 68.4% pixel AP on MVTec AD, +2.5 and +13.4 points over the previous best.

> DRÆM 把表面异常检测从"只学正常、看重建误差"改成判别问题:在正常图像上用 Perlin 噪声 mask + 外部纹理贴出"刚好越界(just-out-of-distribution)"的合成异常,同时训练一个把异常修复回正常的重建子网络和一个读取"原图 ⊕ 重建图"并输出像素级异常图的判别子网络;MVTec AD 图像级 AUROC 98.0%、像素 AP 68.4%,比此前最好方法分别高 2.5 和 13.4 个百分点。

## Related papers / 相关论文
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] — cites
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] — cites
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — cites
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — AD method on far-OOD
- [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — synthetic-anomaly family
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — cites
- [[_maps/papers/padim-icpr-2020|PaDiM]] — cites
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — cites

## Deep-read / 精读

![[papers/draem-iccv-2021/deep-read]]
