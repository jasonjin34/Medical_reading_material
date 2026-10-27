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
recommended_by: core-reading
views:
- plan-a
- reading-list
- overview
tags:
- paper
- plan/A
---

# Pathology-Informed Latent Diffusion Model for Anomaly Detection in Lymph Node Metastasis

> AnoPILaD fine-tunes a text-conditioned latent diffusion model (Stable Diffusion v1.5 + LoRA) on normal lymph-node patches only; at inference the pathology vision-language model CONCH picks the 5 best-matching of 74 "normal tissue" keywords as a prompt, the input is reconstructed toward normal, and the input–reconstruction difference is the anomaly score (the paper does not name the distance; the released code computes latent-space MSE and pixel LPIPS) — patch AUC 0.9587 on gastric lymph nodes and 0.8884 cross-organ on breast lymph nodes (Camelyon16).

> AnoPILaD:只用正常淋巴结图块微调一个文本条件的潜空间扩散模型(Stable Diffusion v1.5 + LoRA),推理时用病理视觉-语言模型 CONCH 从 74 个"正常组织关键词"里挑出最贴切的 5 个作为提示,把输入"重建成正常样子",输入与重建的差异就是异常分(论文未说明用哪种距离;公开代码计算潜空间 MSE 和像素级 LPIPS 两种分数);在胃淋巴结上 patch-AUC 0.9587,跨器官到乳腺淋巴结(Camelyon16)仍有 0.8884。

## Related papers / 相关论文
- [[_maps/papers/counterfactual-diffusion-cancerres-2026|Counterfactual diffusion]] — diffusion on histopathology
- [[_maps/papers/diffusion-medical-ad-miccai-2022|Diffusion AD (medical)]] — diffusion reconstruct-to-normal AD
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — baseline vs latent diffusion
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — histopath anomaly det.
- [[_maps/papers/histo-sciencedirect-2026|Spatial biomarker discovery]] — reconstruct-to-normal
- [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — diffusion-based AD

## Concepts / 概念
- [[_maps/concepts/expert-validation|Expert validation]]
- [[_maps/concepts/ood-detection|OOD / novelty detection]]

## Deep-read / 精读

![[papers/histo-miccai-2025/deep-read]]
