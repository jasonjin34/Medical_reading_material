---
title: Deep contrastive learning enables genome-wide virtual screening
aliases:
- DrugCLIP
plans:
- VS
track: []
year: 2026
relevance: high
category: drug-discovery
recommended_by: sikander
views:
- virtual-screening
- overview
tags:
- paper
- plan/VS
---

# Deep contrastive learning enables genome-wide virtual screening

> DrugCLIP recasts virtual screening from pairwise-scoring regression into a dense-retrieval problem: contrastive learning embeds protein pockets and molecules into one vector space, the compound library can be pre-encoded, and screening needs only one pocket embedding plus cosine-similarity retrieval, taking complexity from O(M×N) to O(M+N) — up to 10 million times faster than docking per the Science abstract. It beats docking and deep-learning baselines on DUD-E and LIT-PCBA; in the wet lab it reached a 15% hit rate for NET (norepinephrine transporter) with two inhibitors' complex structures solved, and a 17.5% hit rate for TRIP12 — a target with no holo structure and no known small-molecule binders — using only AlphaFold2-predicted structures. The screening results for ~10,000 human proteins against 500 million compounds are released as the open database GenomeScreenDB.

> DrugCLIP 把虚拟筛选从"逐对打分的回归问题"改写成"稠密检索问题":用对比学习把蛋白口袋和分子编码到同一个向量空间,分子库可以预先编码好,筛选时只需算一次口袋向量再做余弦相似度检索,复杂度从 O(M×N) 降到 O(M+N),比对接快到 Science 摘要所说的"最多 1,000 万倍";在 DUD-E 与 LIT-PCBA 上超过对接与各类深度学习基线,湿实验上 NET(去甲肾上腺素转运体)命中率 15%、两个抑制剂解出了与靶点的复合物结构,TRIP12(无 holo 结构、无已知小分子配体的靶点)仅用 AlphaFold2 预测结构就拿到 17.5% 命中率;最后把约 1 万个人类蛋白 × 5 亿化合物的筛选结果做成开放数据库 GenomeScreenDB。

## Related papers / 相关论文
- [[_maps/papers/adaptiveflow-natbiotech-2026|AdaptiveFlow]] — Enamine REAL library
- [[_maps/papers/co-scientist-nature-2026|Co-Scientist]] — AI-proposed candidates → wet lab
- [[_maps/papers/competitive-docking-npjdrugdiscov-2026|Competitive docking (AF3)]] — prefilter → co-folding re-rank

## Deep-read / 精读

![[papers/drugclip-science-2026/deep-read]]
