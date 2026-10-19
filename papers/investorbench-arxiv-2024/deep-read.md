# INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent

> **Bibkey** `Li2024_241218174` · **Venue** arXiv preprint (2024) · **Category** other · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2412.18174>
> `status: abstract-only` — 精读基于摘要与公开落地页;把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> InvestorBench 是首个专门评测 LLM agent 金融决策能力的基准:一套统一的 agent 框架 + 覆盖股票/加密货币/ETF 的任务族 + 十三个不同底座模型的横向对比 + 开源多模态数据与环境。
<!-- EN --> InvestorBench is the first benchmark built specifically to evaluate LLM-based agents on financial decision-making: one unified agent framework, a task suite spanning stocks, cryptocurrencies and ETFs, a head-to-head comparison across thirteen backbone LLMs, and open-source multimodal datasets and environments.

## 研究问题 / Problem
<!-- ZH --> LLM agent 在金融决策上潜力明显,但领域卡在两件事上:(1) **缺乏可适配多种金融任务的通用 agent 框架**;(2) **缺乏标准基准与一致的数据集**来评估 agent 表现 —— 各家自建环境、自选标的、自定指标,结果无法互相比较。
<!-- EN --> LLM agents show clear promise in financial decision-making, but the field is stuck on two things: (1) **no general agent framework adaptable across financial tasks**, and (2) **no standardized benchmark or consistent datasets** for assessing agent performance — everyone builds their own environment, picks their own assets and defines their own metrics, so results are incomparable.

## 方法 / Method
<!-- ZH --> 提出一个可泛化的 LLM agent 框架,并把它实例化到不同金融产品的决策任务上;配套构建一整套决策环境与开源多模态数据集(市场行情、文本等)。评测设计的核心是**把底座模型作为变量**:用十三个不同 LLM 做 backbone,在多种市场环境与任务下比较其推理与决策能力。
<!-- EN --> The paper proposes a generalizable LLM-agent framework and instantiates it across decision tasks on different financial products, backed by a full suite of decision environments and curated open-source multimodal datasets (market data, text, etc.). The core evaluation design **treats the backbone as the variable**: thirteen different LLMs are plugged in and compared on reasoning and decision-making across market regimes and tasks.

## 数据 / Data
<!-- ZH --> 覆盖多类金融产品:单一股票、加密货币、ETF;数据为策划整理的开源多模态集合,并配有对应的决策环境,构成一个可公开访问的评测平台。
<!-- EN --> Covers multiple asset classes — single equities, cryptocurrencies and ETFs — with curated open-source multimodal datasets and matching decision environments, forming a publicly accessible evaluation platform.

## 主要结果 / Key results
<!-- ZH --> 主要产出是**基准本身**而非单一模型的胜负:通过十三个底座模型 × 多市场环境 × 多任务的系统评测,给出 LLM agent 在金融决策上的能力画像与可复现的比较平台。(具体分数需查全文。)
<!-- EN --> The primary contribution is **the benchmark itself** rather than a single winner: a systematic sweep over thirteen backbones × market environments × tasks yields a capability profile for LLM agents in financial decision-making, on a reproducible comparison platform. (Exact scores require the full text.)

## 创新点 / Contributions
- <!-- ZH --> 首个面向 LLM agent 金融决策的标准基准。 <!-- EN --> The first standardized benchmark for LLM-agent financial decision-making.
- <!-- ZH --> 统一 agent 框架 + 多资产任务族,使不同任务下的结果可比。 <!-- EN --> A unified agent framework plus a multi-asset task suite, making results comparable across tasks.
- <!-- ZH --> 十三个底座模型的系统对照,把「agent 设计」与「底座能力」分开看。 <!-- EN --> A thirteen-backbone controlled sweep that separates agent design from base-model capability.
- <!-- ZH --> 开源多模态数据集与环境,降低复现门槛。 <!-- EN --> Open-source multimodal datasets and environments that lower the reproduction barrier.

## 局限 / Limitations
- <!-- ZH --> 领域是金融而非生物医学,**任务语义与本方向无关**,可迁移的只有评测方法论。 <!-- EN --> The domain is finance, not biomedicine — **task semantics are irrelevant here**; only the evaluation methodology transfers.
- <!-- ZH --> 金融决策的 ground truth 由市场回报定义,天然含噪且非平稳,与生物学的专家标注性质不同。 <!-- EN --> Ground truth is defined by market returns — inherently noisy and non-stationary, unlike expert-annotated biological labels.
- <!-- ZH --> 预印本,未见同行评议版本;摘要未给具体指标数值。 <!-- EN --> A preprint with no peer-reviewed version seen; the abstract reports no concrete metric values.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 与 detect → model → revert 主链**没有内容上的交集**,收录它的理由只有一个:**它是「怎么给 agent 建基准」的方法论样本**。三点值得抄:(1) **把底座模型当作显式变量**做横扫(十三个 LLM),这与 DeepEvidence「所有系统统一底座」是同一问题的两种解法 —— 前者穷举、后者控制,都是为了分清赢在 agent 设计还是赢在模型;(2) **框架 + 任务族 + 环境 + 数据一起开源**的交付形态,是做 benchmark 该有的完整度;(3) 它示范了在一个「尚无标准」的领域里如何先立标准 —— 与本方向在非肿瘤病理/组学异常检测上无基准可用的处境同构。**不要从它这里拿任何生物学内容。**
<!-- EN --> No topical overlap with detect → model → revert; the sole reason to keep it is that **it is a methodological sample of how to build an agent benchmark**. Three things worth copying: (1) **treating the backbone as an explicit variable** in a thirteen-model sweep — the mirror image of DeepEvidence's "one shared base LLM," both aimed at separating agent design from model strength; (2) the delivery shape — framework + task suite + environments + data released together — as the completeness bar for a benchmark; (3) it demonstrates how to establish a standard in a field that has none, isomorphic to this direction's position in non-tumor pathology / omics anomaly detection. **Take no biological content from it.**

## 可复用资产 / Reusable assets
- <!-- ZH --> **论文与代码入口:** arXiv 预印本。 <!-- EN --> **Paper and code entry point:** the arXiv preprint.
<!-- ZH/EN --> <https://arxiv.org/abs/2412.18174>
- <!-- ZH --> **评测设计:** 统一 agent 框架下的多底座横扫(13 LLM)+ 多资产任务族 + 开源环境。 <!-- EN --> **Eval design:** a multi-backbone sweep (13 LLMs) under one agent framework, a multi-asset task suite and open environments.

## 待读 / Follow-ups
- <!-- ZH --> 查 ACL 2025 版本(aclanthology.org/2025.acl-long.126/),核对是否为同一工作的正式发表版并补齐指标。 <!-- EN --> Check the ACL 2025 version (aclanthology.org/2025.acl-long.126/) to confirm whether it is the published form of the same work and fill in the metrics.
- <!-- ZH --> 提取它的任务定义与指标模板,看能否改造成生物医学 agent 的评测骨架。 <!-- EN --> Extract its task definitions and metric templates to see whether they can be recast as a skeleton for biomedical agent evaluation.

## 引用 / Cite
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
