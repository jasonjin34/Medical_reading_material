---
title: Diffusion Models for Medical Anomaly Detection
aliases:
- Diffusion AD (medical)
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

# Diffusion Models for Medical Anomaly Detection

> DDIM's deterministic noising encodes a patient image to noise level L; denoising with classifier guidance then "translates" it to the healthy class, and the difference between input and output is a pixel-level anomaly map — a weakly supervised AD method needing only image-level (healthy/diseased) labels, described by the authors as the first diffusion model for anomaly detection.

> 用 DDIM 的确定性加噪把病人图像编码到噪声水平 L,再在去噪时加分类器引导把它"翻译"成健康类,输入与生成图之差就是像素级异常图 —— 一个只需图像级标签(健康/患病)的弱监督异常检测方法,作者称是首个用于异常检测的扩散模型。

## Related papers / 相关论文
- [[_maps/papers/counterfactual-diffusion-cancerres-2026|Counterfactual diffusion]] — diffusion counterfactuals
- [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — diffusion reconstruct-to-normal AD

## Deep-read / 精读

![[papers/diffusion-medical-ad-miccai-2022/deep-read]]
