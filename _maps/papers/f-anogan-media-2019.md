---
title: 'f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial
  networks'
aliases:
- f-AnoGAN
plans:
- A
track:
- A0
year: 2019
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

# f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks

> f-AnoGAN replaces AnoGAN's per-image iterative latent search with a trained encoder E: train a WGAN-GP on healthy OCT patches, then freeze G and D and train E with a "pixel residual + discriminator-feature residual" objective (izi_f); at test time one forward pass gives the reconstruction G(E(x)) and the anomaly score. Image-level AUC is 0.930, beating AE / AdvAE / ALI and iterative AnoGAN (0.911), while inference drops from 2 days to 20 seconds.

> f-AnoGAN 把 AnoGAN 的"每张图 latent 迭代搜索"换成一个训练好的编码器 E:先在健康 OCT 图块上训练 WGAN-GP,再固定 G 和 D、用"像素残差 + 判别器特征残差"(izi_f)训练 E,测试时一次前向即得重建 G(E(x)) 与异常分数;图像级 AUC 0.930,优于 AE / AdvAE / ALI 与迭代式 AnoGAN(0.911),而推理从 2 天缩到 20 秒。

## Related papers / 相关论文
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — reviewed: GAN + explicit encoder
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] — adds an encoder + WGAN to AnoGAN
- [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — baseline vs latent diffusion
- [[_maps/papers/meatrd-aaai-2025|MEATRD]] — cites
- [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — benchmarked (reconstruction family)

## Deep-read / 精读

![[papers/f-anogan-media-2019/deep-read]]
