---
title: Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in
  Agentic Deep Research
aliases:
- Who is to blame? (citations)
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

# Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

> In multi-agent deep-research (DR) systems information passes through agents like a "telephone game", and both content and citations can be corrupted along the way. This paper locally tests each agent invocation for faithfulness and verifiability relative to its own inputs, so every citation error in the final report can be traced to the agent that introduced it, and typed into four classes (hallucination, uncited input reliance, uncited output, insufficient citations). In Nvidia AI-Q, 84.7% of final-report errors originate at the orchestrator; two simple interventions guided by this raise citation recall by ~5 points without hurting quality.

> 多智能体 deep research(DR)系统里,信息像「传话游戏」一样逐层传递,内容和引用都会在途中被损坏。本文提出局部测试每一次 agent 调用相对其自身输入的忠实性与可验证性,从而把最终报告里的每个引用错误追溯到引入它的那个 agent,并按四类分型(幻觉、依赖未引用输入、输出无引用、引用不足);在 Nvidia AI-Q 上 84.7% 的最终报告错误源自 orchestrator,据此做的两个简单干预使引用召回率提升约 5 个百分点且不损失质量。

## Related papers / 相关论文
- [[_maps/papers/citation-faithfulness-arxiv-2026|Citation faithfulness guard]] — citation faithfulness
- [[_maps/papers/trail-arxiv-2025|TRAIL]] — trace-level error localization

## Concepts / 概念
- [[_maps/concepts/hallucination|Hallucination]]
- [[_maps/concepts/outcome-eval|Final-answer grading]]

## Deep-read / 精读

![[papers/citation-blame-emnlp-2026/deep-read]]
