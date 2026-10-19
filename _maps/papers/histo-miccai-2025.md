---
title: Pathology-Informed Latent Diffusion Model for Anomaly Detection in Lymph Node
  Metastasis
aliases:
- Latent-diffusion AD
plans:
- A
track:
- A6
year: 2025
relevance: medium
category: histopath
recommended_by: sikander
views:
- plan-a
- sikander
- overview
tags:
- paper
- plan/A
---

# Pathology-Informed Latent Diffusion Model for Anomaly Detection in Lymph Node Metastasis

> AnoPILaD is a pathology-informed latent diffusion model: a VLM (CONCH) selects normal-tissue keywords that condition an LDM's reconstruction toward normal morphology, and the input-vs-reconstruction discrepancy serves as an unsupervised anomaly score for lymph-node metastasis.

> AnoPILaD:用病理关键词提示(CONCH 视觉-语言模型选词)引导潜空间扩散模型(Stable Diffusion v1.5 + LoRA)重建"正常样"淋巴结组织,再以重建差异作为异常分数,实现无监督的转移灶检测。

## Related papers / 相关论文
- [[_maps/papers/counterfactual-diffusion-cancerres-2026|Counterfactual diffusion]] — diffusion on histopathology
- [[_maps/papers/diffusion-medical-ad-miccai-2022|Diffusion AD (medical)]] — diffusion reconstruct-to-normal AD
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — baseline vs latent diffusion
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — histopath anomaly det.
- [[_maps/papers/histo-sciencedirect-2026|Spatial biomarker discovery]] — reconstruct-to-normal
- [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — diffusion-based AD

## Concepts / 概念
- [[_maps/concepts/ood-detection|OOD / novelty detection]]

## Deep-read / 精读

![[papers/histo-miccai-2025/deep-read]]
