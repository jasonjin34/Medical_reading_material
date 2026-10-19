---
title: 'Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness
  and Hallucination in Large Language Models'
aliases:
- TruthHypo
plans:
- B
track:
- B6
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

# Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models

> TruthHypo builds a biomedical hypothesis-generation benchmark from a temporally split PubTator 3.0 knowledge graph (pre-2023 "seen", post-2024 "unseen") to test whether LLMs propose truthful new relations; the companion KnowHD decomposes each hypothesis and its rationale into atomic claims and checks each against literature and/or the KG — higher groundedness predicts truthfulness, and selecting the most grounded of five candidates improves accuracy.

> TruthHypo 用 PubTator 3.0 知识图按时间切分(2023 前「已见」、2024 后「未见」)构造生物医学假设生成基准,检验 LLM 能否提出真实的新关系;配套的 KnowHD 把假设及其推理拆成原子论断,逐条对照文献/知识图判断是否 grounded —— groundedness 越高的假设越可能为真,用它在 5 个候选中选优可提升准确率。

## Related papers / 相关论文
- [[_maps/papers/deepevidence-natmachintell-2026|DeepEvidence]] — KG + literature grounding
- [[_maps/papers/hypogen-llm-colm-2024|LLM hypothesis generators]] — cites
- [[_maps/papers/paperqa2-arxiv-2024|PaperQA2]] — cites

## Concepts / 概念
- [[_maps/concepts/claim-evidence|Claim → evidence chains]]

## Deep-read / 精读

![[papers/truthhypo-ijcai-2025/deep-read]]
