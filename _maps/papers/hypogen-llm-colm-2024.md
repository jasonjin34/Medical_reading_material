---
title: 'Large Language Models as Biomedical Hypothesis Generators: A Comprehensive
  Evaluation'
aliases:
- LLM hypothesis generators
plans:
- B
track:
- B6
year: 2024
relevance: high
category: agents
recommended_by: sikander
views:
- plan-b
- sikander
- overview
tags:
- paper
- plan/B
---

# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

> Using a biomedical background → hypothesis dataset split by publication date (pre-Jan-2023 = train/seen, Aug-2023 = unseen), the paper systematically evaluates LLM hypothesis generation in zero-shot, few-shot, fine-tuned, tool-use and multi-agent settings, introduces four rubric metrics (Novelty, Relevance, Significance, Verifiability; scored by GPT-4 and checked against human experts), and finds LLMs can propose novel, later-validated hypotheses even on unseen literature — with "uncertainty" (measured by SelfBLEU) trading novelty against verifiability.

> 用按发表时间切分(2023 年 1 月前 = 训练/seen,2023 年 8 月 = unseen)的生物医学「背景知识 → 假设」配对数据集,系统评测 LLM 在 zero-shot / few-shot / 微调 / 工具调用 / 多智能体设置下的假设生成能力,提出 Novelty、Relevance、Significance、Verifiability 四维评分(GPT-4 打分并与人类专家对齐),发现 LLM 在未见文献上也能提出新颖且后来被验证的假设,而"不确定性"(SelfBLEU 衡量)在新颖性与可验证性之间形成权衡。

## Related papers / 相关论文
- [[_maps/papers/co-scientist-nature-2026|Co-Scientist]] — hypothesis generation
- [[_maps/papers/semnovel-jbi-2025|SemNovel]] — novelty of biomedical ideas
- [[_maps/papers/truthhypo-ijcai-2025|TruthHypo]] — cites

## Concepts / 概念
- [[_maps/concepts/benchmark-validity|Benchmark validity]]
- [[_maps/concepts/multi-agent|Multi-agent systems]]
- [[_maps/concepts/novelty|Novelty]]
- [[_maps/concepts/omics-agent|Single-cell analysis agents]]
- [[_maps/concepts/trajectory-eval|Trajectory-level evaluation]]

## Deep-read / 精读

![[papers/hypogen-llm-colm-2024/deep-read]]
