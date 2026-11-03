---
title: AI-guided competitive docking for virtual screening and compound efficacy prediction
aliases:
- Competitive docking (AF3)
plans:
- VS
track: []
year: 2026
relevance: medium
category: drug-discovery
recommended_by: sikander
views:
- virtual-screening
- overview
tags:
- paper
- plan/VS
---

# AI-guided competitive docking for virtual screening and compound efficacy prediction

> The authors note that diffusion-based co-folding models such as AF3 and Boltz-1/2 produce a plausible-looking binding pose for any molecule, and propose two plain but effective criteria: (a) pose convergence — the mean RMSD among poses predicted for the same ligand across several random seeds, where true inhibitors typically fall below 2 Å and within 5 Å of the pocket while unrelated molecules diverge and sit further away; and (b) pairwise competitive docking — co-fold two ligands at once and let whichever occupies the active site win, with the win rate as the CDS (Competitive Docking Score) used to rank inhibitors. Across 17 protein systems (19 binding sites), CDS rankings agree with experimental activity at concordance indices from 0.52 (no correlation) to 0.89 (strong), broadly on par with Boltz-2's own affinity-prediction module. Extended to "All-at-Once" (25–26 molecules competing in one run), screening 3,155 FDA-approved drugs for fluoroquinolones reached 93.5% enrichment with an enrichment factor of 62 after pose filtering.

> 作者发现 AF3 / Boltz-1/2 这类扩散式 co-folding 模型对任何分子都会生成一个看似合理的结合位姿,于是提出两个很朴素但有效的判据:(a) 位姿收敛性——同一配体在多个随机种子下预测位姿彼此的平均 RMSD,真抑制剂通常 < 2 Å 且落在结合口袋 5 Å 内,无关分子则发散且远离;(b) 两两竞争对接(pairwise competitive docking)——一次把两个配体一起放进去共折叠,谁占住活性位点谁赢,胜率即 CDS(Competitive Docking Score),据此排出抑制剂顺序。在 17 个蛋白系统(19 个结合位点)上,CDS 排序与实验活性的一致性指数 c 从 0.52(无相关)到 0.89(强相关),与 Boltz-2 自带的亲和力预测模块总体相当;把这招推广成 "All-at-Once"(一次放 25–26 个分子竞争)后,在 3,155 个 FDA 已批准药物的库里找氟喹诺酮,叠加位姿过滤后富集度达 93.5%、富集因子 62。

## Related papers / 相关论文
- [[_maps/papers/adaptiveflow-natbiotech-2026|AdaptiveFlow]] — docking vs co-folding ranking
- [[_maps/papers/drugclip-science-2026|DrugCLIP]] — prefilter → co-folding re-rank

## Deep-read / 精读

![[papers/competitive-docking-npjdrugdiscov-2026/deep-read]]
