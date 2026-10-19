# INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent

> **Bibkey** `Li2024_241218174` · **Venue** arXiv preprint (2024) · **Category** other · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2412.18174> · `status: abstract-only`

---

## One-liner
InvestorBench is the first benchmark built specifically to evaluate LLM-based agents on financial decision-making: one unified agent framework, a task suite spanning stocks, cryptocurrencies and ETFs, a head-to-head comparison across thirteen backbone LLMs, and open-source multimodal datasets and environments.

## Problem
LLM agents show clear promise in financial decision-making, but the field is stuck on two things: (1) **no general agent framework adaptable across financial tasks**, and (2) **no standardized benchmark or consistent datasets** for assessing agent performance — everyone builds their own environment, picks their own assets and defines their own metrics, so results are incomparable.

## Method
The paper proposes a generalizable LLM-agent framework and instantiates it across decision tasks on different financial products, backed by a full suite of decision environments and curated open-source multimodal datasets (market data, text, etc.). The core evaluation design **treats the backbone as the variable**: thirteen different LLMs are plugged in and compared on reasoning and decision-making across market regimes and tasks.

## Data
Covers multiple asset classes — single equities, cryptocurrencies and ETFs — with curated open-source multimodal datasets and matching decision environments, forming a publicly accessible evaluation platform.

## Key results
The primary contribution is **the benchmark itself** rather than a single winner: a systematic sweep over thirteen backbones × market environments × tasks yields a capability profile for LLM agents in financial decision-making, on a reproducible comparison platform. (Exact scores require the full text.)

## Contributions
- The first standardized benchmark for LLM-agent financial decision-making.
- A unified agent framework plus a multi-asset task suite, making results comparable across tasks.
- A thirteen-backbone controlled sweep that separates agent design from base-model capability.
- Open-source multimodal datasets and environments that lower the reproduction barrier.

## Limitations
- The domain is finance, not biomedicine — **task semantics are irrelevant here**; only the evaluation methodology transfers.
- Ground truth is defined by market returns — inherently noisy and non-stationary, unlike expert-annotated biological labels.
- A preprint with no peer-reviewed version seen; the abstract reports no concrete metric values.

## Relation to our direction
No topical overlap with detect → model → revert; the sole reason to keep it is that **it is a methodological sample of how to build an agent benchmark**. Three things worth copying: (1) **treating the backbone as an explicit variable** in a thirteen-model sweep — the mirror image of DeepEvidence's "one shared base LLM," both aimed at separating agent design from model strength; (2) the delivery shape — framework + task suite + environments + data released together — as the completeness bar for a benchmark; (3) it demonstrates how to establish a standard in a field that has none, isomorphic to this direction's position in non-tumor pathology / omics anomaly detection. **Take no biological content from it.**

## Reusable assets
- **Paper and code entry point:** the arXiv preprint.
<https://arxiv.org/abs/2412.18174>
- **Eval design:** a multi-backbone sweep (13 LLMs) under one agent framework, a multi-asset task suite and open environments.

## Follow-ups
- Check the ACL 2025 version (aclanthology.org/2025.acl-long.126/) to confirm whether it is the published form of the same work and fill in the metrics.
- Extract its task definitions and metric templates to see whether they can be recast as a skeleton for biomedical agent evaluation.

## Cite
```bibtex
@misc{Li2024_241218174,
  title = {INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent},
  author = {Haohang Li and Yupeng Cao and Yangyang Yu and Shashidhar Reddy Javaji and Zhiyang Deng and Yueru He and Yuechen Jiang and Zining Zhu and Koduvayur Subbalakshmi and Guojun Xiong and Jimin Huang and Lingfei Qian and Xueqing Peng and Qianqian Xie and Jordan W. Suchow},
  year = {2024},
  eprint = {2412.18174},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2412.18174}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
