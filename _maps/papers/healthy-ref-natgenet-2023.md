---
title: Precise identification of cell states altered in disease using healthy single-cell
  references
aliases:
- Healthy-reference design
plans:
- A
track:
- A3
year: 2023
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

# Precise identification of cell states altered in disease using healthy single-cell references

> When using a "healthy reference" to find disease-altered cell states, which reference should you use? The authors give a systematic answer: learn the latent space on a large healthy atlas (scVI + scArches mapping), then run differential-abundance testing (Milo) against matched controls only — the ACR (atlas-to-control reference) design. It beats atlas-only (false positives explode) and control-only (misses multiple altered states), and with an atlas available, the number of controls can be cut without inflating FDR.

> 用「健康参照」找疾病改变的细胞状态时,参照该怎么选?作者给出系统答案:用大规模健康 atlas 学 latent space(scVI + scArches 映射),再只拿匹配的 control 样本做差异丰度检验(Milo)——即 ACR(atlas-to-control reference)设计;它比只用 atlas(假阳性暴涨)或只用 control(漏掉多种异常状态)都更准,且有 atlas 时可以少采 control 而不增加 FDR。

## Related papers / 相关论文
- [[_maps/papers/lake-kidney-atlas-nature-2023|Kidney atlas (Lake 2023)]] — healthy atlas reference
- [[_maps/papers/mrvi-natmethods-2025|MrVI]] — cites
- [[_maps/papers/refmap-eval-biorxiv-2025|Reference-mapping QC]] — cites

## Concepts / 概念
- [[_maps/concepts/disease-cell-state|Injured / failed-repair states]]
- [[_maps/concepts/healthy-reference|Healthy reference atlas]]

## Deep-read / 精读

![[papers/healthy-ref-natgenet-2023/deep-read]]
