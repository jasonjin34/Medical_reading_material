---
title: 'SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents'
aliases:
- SciTrace
plans:
- B
track:
- B7
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

# SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents

> SciTrace (CMU) weaves safety reasoning into every stage of an AI-scientist pipeline: a Safety-Intrinsic Reasoning Loop (SIR) maintains and propagates a cumulative risk state across the Thinker → Experimenter → Writer → Reviewer stages, and a Compositional Tool-Chain Verifier (CTV) checks each tool call against the full call history to ask whether a sequence of individually benign steps adds up to something dangerous. On SciSafetyBench it raises tool-call safety by 14.3 points on average over SafeScientist and catches 78.8% of the compositional risks that single-step monitors miss.

> SciTrace(CMU)把安全推理「织进」AI scientist 流水线的每一步:Safety-Intrinsic Reasoning Loop (SIR) 在 Thinker → Experimenter → Writer → Reviewer 四个阶段之间维护并传递一个累积风险状态,Compositional Tool-Chain Verifier (CTV) 在每次工具调用前结合完整调用历史判断「这一串单步无害的操作合起来是否危险」;在 SciSafetyBench 上相对 SafeScientist 把工具调用安全率平均提升 14.3 个百分点,并抓到单步监控漏掉的 78.8% 组合式风险。

## Related papers / 相关论文
- [[_maps/papers/ailuminate-arxiv-2025|AILuminate]] — hazard taxonomy
- [[_maps/papers/trail-arxiv-2025|TRAIL]] — trajectory-level verification

## Concepts / 概念
- [[_maps/concepts/research-agent|AI scientist agents]]
- [[_maps/concepts/safety|Safety & hazards]]

## Deep-read / 精读

![[papers/scitrace-arxiv-2026/deep-read]]
