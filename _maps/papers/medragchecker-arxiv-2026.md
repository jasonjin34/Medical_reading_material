---
title: 'MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented
  Generation'
aliases:
- MedRAGChecker
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

# MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation

> MedRAGChecker decomposes long-form biomedical RAG answers into atomic claims (SPO triples) and verifies each with a distilled NLI checker plus a knowledge-graph (KG) consistency signal, fusing them via selective gating only when NLI confidently entails while the KG confidently conflicts. The headline finding is that KG coverage decides whether the KG helps or hurts: DRKG (62.7% coverage) inflates the hallucination rate to 34.2%, while BioPortal (94.2% coverage) lowers it to 25.2%.

> MedRAGChecker 把生物医学 RAG 的长答案拆成原子 claim(SPO 三元组),用「蒸馏出的 NLI 检查器 + 知识图谱(KG)一致性信号」逐条核验,并用 selective gating 只在「NLI 很确信蕴含、KG 很确信冲突」时才融合 KG —— 核心发现是 KG 覆盖率决定 KG 是帮忙还是添乱:覆盖率 62.7% 的 DRKG 把幻觉率推高到 34.2%,覆盖率 94.2% 的 BioPortal 把它压到 25.2%。

## Related papers / 相关论文
- [[_maps/papers/deepevidence-natmachintell-2026|DeepEvidence]] — KG evidence grounding
- [[_maps/papers/medical-hallucination-arxiv-2025|Medical hallucinations]] — medical hallucination detection
- [[_maps/papers/scirigor-arxiv-2026|SciRIGOR]] — claim-to-evidence verification
- [[_maps/papers/sourcecheckup-natcommun-2025|SourceCheckup]] — claim-level verification

## Concepts / 概念
- [[_maps/concepts/claim-evidence|Claim → evidence chains]]
- [[_maps/concepts/human-calibration|Human / expert calibration]]
- [[_maps/concepts/safety|Safety & hazards]]

## Deep-read / 精读

![[papers/medragchecker-arxiv-2026/deep-read]]
