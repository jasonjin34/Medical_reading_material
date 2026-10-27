---
title: Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide
  Marker Discovery
aliases:
- AnoGAN
plans:
- A
track:
- A0
year: 2017
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

# Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery

> AnoGAN trains a DCGAN only on healthy retinal OCT patches; at test time it runs 500 gradient-descent steps in latent space to find the "most similar normal image" G(z) for each new patch, and scores anomalies by a weighted sum of a pixel residual and a residual on intermediate discriminator features, with the residual image serving as the anomaly map. Per the authors it is the first use of GANs for anomaly detection, and it founds the "learn normal → reconstruct → read the residual" paradigm.

> AnoGAN 只在健康视网膜 OCT 图块上训练一个 DCGAN,测试时对每张新图块在 latent space 里做 500 步梯度下降找到"最像它的正常图像" G(z),用像素残差 + 判别器中间层特征残差的加权和作异常分数、残差图作异常定位 —— 这是把 GAN 用于异常检测的首个工作(作者自述),也是"学正常 → 重建 → 看残差"这一范式的奠基论文。

## Related papers / 相关论文
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — reviewed: GAN reconstruction
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] — AnoGAN as deep baseline
- [[_maps/papers/draem-iccv-2021|DRAEM]] — cites
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — adds an encoder + WGAN to AnoGAN
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — GAN baseline
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — GAN on normal data; reconstruction-residual score

## Deep-read / 精读

![[papers/anogan-ipmi-2017/deep-read]]
