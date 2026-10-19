---
title: Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep
  Research Agents
aliases:
- Reference hallucinations
plans:
- B
track:
- B4
year: 2026
relevance: medium
category: agents
recommended_by: ''
views:
- plan-b
- overview
tags:
- paper
- plan/B
---

# Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

> Quantifies citation-URL reliability across 10 models/agents on DRBench (53,090 URLs) and 3 models on ExpertQA (168,021 URLs, 32 fields): 3–13% of cited URLs are hallucinated (no Wayback Machine record — likely never existed) and 5–18% are non-resolving; deep research agents cite the most and hallucinate the most. The authors release urlhealth, an 83-line tool that, used for agentic self-correction, cuts non-resolving URLs 6–79× to under 1%.

> 在 10 个模型/agent(DRBench,53,090 个 URL)和 3 个模型(ExpertQA,168,021 个 URL,32 个学科)上量化引用 URL 的可靠性:3%–13% 的引用 URL 是幻觉(Wayback Machine 无任何存档、很可能从未存在),5%–18% 无法解析;deep research agent 引用最多、幻觉率也最高;作者发布 83 行的 urlhealth 工具,作为 agent 的自我纠错工具可把无法解析的 URL 降低 6–79×、到 1% 以下。

## Related papers / 相关论文
- [[_maps/papers/citation-faithfulness-arxiv-2026|Citation faithfulness guard]] — citation reliability
- [[_maps/papers/sourcecheckup-natcommun-2025|SourceCheckup]] — citation support vs existence

## Concepts / 概念
- [[_maps/concepts/hallucination|Hallucination]]
- [[_maps/concepts/research-agent|AI scientist agents]]

## Deep-read / 精读

![[papers/reference-hallucination-arxiv-2026/deep-read]]
