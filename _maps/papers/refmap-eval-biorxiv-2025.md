---
title: Automated evaluation of single-cell reference atlas mappings enables the identification
  of disease-associated cell states
aliases:
- Reference-mapping QC
plans:
- A
track:
- A3
year: 2025
relevance: high
category: single-cell
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Automated evaluation of single-cell reference atlas mappings enables the identification of disease-associated cell states

> MapQC (Theis lab) uses the healthy reference atlas's own inter-sample variation as a null distribution to judge whether a query→reference mapping succeeded: query control samples should sit at a "normal" distance from the reference (mapQC score < 2), and case samples should be "abnormally" distant in some cells (> 2). It catches residual batch effects invisible in UMAPs, prevents artifacts from being reported as disease states, and is more interpretable than repurposed integration metrics (LISI, kBET, etc.).

> MapQC(Theis 组)用健康参照 atlas 自身的样本间差异作为零分布,来判断一次 query→reference 映射是否成功:query 的 control 样本应与参照「正常地远」(mapQC 分数 < 2),case 样本应在部分细胞中「异常地远」(> 2)。它能检出 UMAP 看不出来的残留 batch effect,防止把 artifact 报告成疾病状态,而且比重新拿来用的整合指标(LISI、kBET 等)更可解释。

## Related papers / 相关论文
- [[_maps/papers/conformal-outliers-annstat-2023|Conformal p-values]] — healthy reference as the null
- [[_maps/papers/conformal-scrna-bioinformatics-2025|Conformal annotation]] — reference–query shift
- [[_maps/papers/healthy-ref-natgenet-2023|Healthy-reference design]] — cites
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — distance to a reference distribution

## Concepts / 概念
- [[_maps/concepts/ambient-rna|Ambient RNA]]
- [[_maps/concepts/batch-effect|Batch effects]]
- [[_maps/concepts/doublet|Doublets]]
- [[_maps/concepts/healthy-reference|Healthy reference atlas]]
- [[_maps/concepts/mapping-uncertainty|Reference-mapping uncertainty]]

## Deep-read / 精读

![[papers/refmap-eval-biorxiv-2025/deep-read]]
