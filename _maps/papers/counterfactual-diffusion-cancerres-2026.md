---
title: Counterfactual Diffusion Models Provide Interpretable Explanations of Artificial
  Intelligence Models in Pathology
aliases:
- Counterfactual diffusion
plans: []
track: []
year: 2026
relevance: medium
category: histopath
recommended_by: sikander
views:
- sikander
- overview
tags:
- paper
---

# Counterfactual Diffusion Models Provide Interpretable Explanations of Artificial Intelligence Models in Pathology

> MoPaDi (Morphing histoPathology Diffusion) couples a diffusion autoencoder with tile-level logistic-regression or slide-level MIL classifiers: it pushes a tile's latent feature vector along the classifier's decision direction and decodes it with the conditional diffusion model into a counterfactual H&E image ("what would this tile look like if it were class X?"), so pathologists can see the morphologic cues a model relies on. Validated on colorectal (tissue type, MSI), hepatobiliary, lung and breast tasks, with a Shapley-style decomposition showing MSI predictions are driven mostly by morphology rather than stain.

> MoPaDi(Morphing histoPathology Diffusion)把 diffusion autoencoder 与 tile 级 logistic regression / slide 级 MIL 分类器接起来:沿分类器在潜空间里的决策方向推动 tile 的特征向量,再用条件扩散解码器生成"如果它是另一类会长什么样"的 counterfactual H&E 图像,让病理医生直接看到模型依赖的形态学线索;在结直肠(组织类型、MSI)、肝胆、肺、乳腺癌任务上验证,并用 Shapley 式分解说明 MSI 预测主要由形态而非染色驱动。

## Related papers / 相关论文
- [[_maps/papers/diffusion-medical-ad-miccai-2022|Diffusion AD (medical)]] — diffusion counterfactuals
- [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — diffusion on histopathology
- [[_maps/papers/virtual-tissue-2501|Virtual tissues (spatial proteomics)]] — virtual perturbation / revert

## Concepts / 概念
- [[_maps/concepts/perturbation|Perturbation & counterfactual]]
- [[_maps/concepts/virtual-tissue|Virtual tissue / cell]]

## Deep-read / 精读

![[papers/counterfactual-diffusion-cancerres-2026/deep-read]]
