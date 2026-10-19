---
title: Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis
aliases:
- Citation faithfulness guard
plans:
- B
track:
- B4
year: 2026
relevance: high
category: agents
recommended_by: ''
views:
- plan-b
- overview
tags:
- paper
- plan/B
---

# Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis

> Literature-synthesis agents like OpenScholar and PaperQA2, and their benchmarks, all check whether citations hold — but nobody audits whether the checker itself is reliable. This paper shows that on identical agent outputs the unsupported-citation rate ranges from ~3% to ~18% depending only on verifier strictness; verifiers agree on what is supported but barely agree on what to flag (negative-specific agreement 0.27–0.30). The authors give a gold-anchored evaluation protocol and a split-conformal guard that places a distribution-free, finite-sample guarantee on the catch rate of truly unsupported citations, and show that whether the guarantee transfers is governed by calibration-negative difficulty.

> OpenScholar、PaperQA2 这类文献综合 agent 及其基准都会「检查引用是否成立」,但没人审计这个检查器本身是否可靠。本文证明:同一批 agent 输出,仅因 verifier 严格度不同,未支持引用率就在 约 3% 到约 18% 之间变动;verifier 们在「哪些被支持」上一致,在「该标记哪些」上却几乎不一致(negative-specific agreement 0.27–0.30)。作者给出以人工金标准为锚的评估协议 + 一个 split-conformal 守卫,对「漏过标记规则的真正未支持引用」给出无分布、有限样本的捕获率保证,并指出保证能否迁移取决于校准负样本的难度。

## Related papers / 相关论文
- [[_maps/papers/citation-blame-emnlp-2026|Who is to blame? (citations)]] — citation faithfulness
- [[_maps/papers/conformal-scrna-bioinformatics-2025|Conformal annotation]] — conformal guarantees
- [[_maps/papers/paperqa2-arxiv-2024|PaperQA2]] — audits PaperQA2 citations
- [[_maps/papers/reference-hallucination-arxiv-2026|Reference hallucinations]] — citation reliability
- [[_maps/papers/robin-nature-2026|Robin]] — cites
- [[_maps/papers/sourcecheckup-natcommun-2025|SourceCheckup]] — cites
- [[_maps/papers/virtual-lab-nature-2025|Virtual Lab]] — cites

## Concepts / 概念
- [[_maps/concepts/citation-faithfulness|Citation faithfulness]]

## Deep-read / 精读

![[papers/citation-faithfulness-arxiv-2026/deep-read]]
