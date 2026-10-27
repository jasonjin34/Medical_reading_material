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
recommended_by: core-reading
views:
- plan-b
- reading-list
- overview
tags:
- paper
- plan/B
---

# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

> The authors automatically extract "background → hypothesis" pairs from PubMed papers, split them by publication date (before Jan 2023 = train/seen, Aug 2023 = unseen) so test data cannot have been seen in training, and systematically evaluate 2023-era LLMs at proposing biomedical hypotheses zero-shot, few-shot, fine-tuned, with tools and as a multi-agent system, scoring Novelty / Relevance / Significance / Verifiability on 0–3 (LLM judge + human experts) (Abstract; §2–4).

> 作者从 PubMed 文献中自动抽取「背景知识 → 假设」配对,按发表时间切分(2023 年 1 月前 = 训练/seen,2023 年 8 月 = unseen)以避免测试数据被模型训练见过,系统评测 2023 年代 LLM 在 zero-shot、few-shot、微调、工具调用和多智能体设置下提出生物医学假设的能力,用 Novelty / Relevance / Significance / Verifiability 四个 0–3 分维度(LLM 评审 + 人类专家)打分(Abstract;§2–4)。

## Related papers / 相关论文
- [[_maps/papers/co-scientist-nature-2026|Co-Scientist]] — hypothesis generation
- [[_maps/papers/semnovel-jbi-2025|SemNovel]] — novelty of biomedical ideas
- [[_maps/papers/truthhypo-ijcai-2025|TruthHypo]] — cites

## Concepts / 概念
- [[_maps/concepts/llm-judge|LLM-as-judge]]
- [[_maps/concepts/multi-agent|Multi-agent systems]]
- [[_maps/concepts/novelty|Novelty]]

## Deep-read / 精读

![[papers/hypogen-llm-colm-2024/deep-read]]
