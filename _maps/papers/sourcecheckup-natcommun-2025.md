---
title: An automated framework for assessing how well LLMs cite relevant medical references
aliases:
- SourceCheckup
plans:
- B
track:
- B4
year: 2025
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

# An automated framework for assessing how well LLMs cite relevant medical references

> SourceCheckup is a fully automated agent pipeline — generate medical questions → have an LLM answer with sources → parse into independently verifiable statements → download URL contents → have GPT-4o judge each statement–source pair. Across 7 models, 800 questions and ~58K statement–source pairs, 50–90% of responses are not fully supported by the sources they cite; even web-enabled GPT-4o (RAG) is fully supported in only 55% of responses. The automated verifier agrees with a three-doctor consensus 88.7% of the time, above the 86.1% average inter-doctor agreement.

> SourceCheckup 是一条全自动的 agent 流水线:出医学问题 → 让 LLM 作答并给出处 → 拆成独立可验证的 statement → 下载 URL 全文 → 用 GPT-4o 逐对判断「这个来源是否支持这句话」;在 7 个模型、800 题、约 5.8 万个 statement–source 对上发现 50%–90% 的回答并未被其引用完全支持,即便联网的 GPT-4o(RAG)也只有 55% 的回答完全被支持;该自动核验与三位执业医生共识一致率 88.7%,高于医生之间的平均一致率 86.1%。

## Related papers / 相关论文
- [[_maps/papers/citation-faithfulness-arxiv-2026|Citation faithfulness guard]] — cites
- [[_maps/papers/deeptrace-arxiv-2025|DeepTRACE]] — statement × source support
- [[_maps/papers/llm-judge-healthcare-arxiv-2026|LLM-as-judge in healthcare]] — judge vs physician panel
- [[_maps/papers/medragchecker-arxiv-2026|MedRAGChecker]] — claim-level verification
- [[_maps/papers/reference-hallucination-arxiv-2026|Reference hallucinations]] — citation support vs existence

## Concepts / 概念
- [[_maps/concepts/citation-faithfulness|Citation faithfulness]]
- [[_maps/concepts/human-calibration|Human / expert calibration]]

## Deep-read / 精读

![[papers/sourcecheckup-natcommun-2025/deep-read]]
