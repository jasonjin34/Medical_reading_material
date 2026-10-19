---
title: Testing for Outliers with Conformal p-values
aliases:
- Conformal p-values
plans:
- A
track:
- A0
year: 2023
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

# Testing for Outliers with Conformal p-values

> Turns the output of any one-class classifier / anomaly scorer into a p-value per test point via split-conformal calibration, and studies these p-values from a multiple-testing perspective: classical (marginal) conformal p-values are mutually dependent but PRDS, so Benjamini–Hochberg (even with Storey's correction) still controls the FDR exactly, while Fisher's combination test breaks; it then constructs calibration-conditionally valid (CCV) p-values — valid with probability 1−δ for *this* calibration set and mutually independent — and, as a by-product, a simultaneous upper confidence bound on the FPR of any outlier-detection algorithm.

> 把任意一类分类器 / 异常打分器的输出,经 split-conformal 校准变成每个测试点的 p 值,并从多重检验角度研究它们:证明经典(边际)conformal p 值虽然彼此相关,但满足 PRDS,因此 Benjamini–Hochberg(含 Storey 修正)仍精确控制 FDR,而 Fisher 合并检验会失效;再提出校准条件有效(calibration-conditional valid, CCV)的 p 值——以概率 1−δ 对「这一份」校准集有效,且彼此独立——并顺带给出任意异常检测算法 FPR 的同时置信上界。

## Related papers / 相关论文
- [[_maps/papers/conformal-scrna-bioinformatics-2025|Conformal annotation]] — cites
- [[_maps/papers/refmap-eval-biorxiv-2025|Reference-mapping QC]] — healthy reference as the null

## Deep-read / 精读

![[papers/conformal-outliers-annstat-2023/deep-read]]
