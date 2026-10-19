# INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent

> **文献键** `Li2024_241218174` · **来源** arXiv preprint(2024) · **类别** other · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2412.18174> · `status: abstract-only`

---

## 一句话
InvestorBench 是首个专门评测 LLM agent 金融决策能力的基准:一套统一的 agent 框架 + 覆盖股票/加密货币/ETF 的任务族 + 十三个不同底座模型的横向对比 + 开源多模态数据与环境。

## 研究问题
LLM agent 在金融决策上潜力明显,但领域卡在两件事上:(1) **缺乏可适配多种金融任务的通用 agent 框架**;(2) **缺乏标准基准与一致的数据集**来评估 agent 表现 —— 各家自建环境、自选标的、自定指标,结果无法互相比较。

## 方法
提出一个可泛化的 LLM agent 框架,并把它实例化到不同金融产品的决策任务上;配套构建一整套决策环境与开源多模态数据集(市场行情、文本等)。评测设计的核心是**把底座模型作为变量**:用十三个不同 LLM 做 backbone,在多种市场环境与任务下比较其推理与决策能力。

## 数据
覆盖多类金融产品:单一股票、加密货币、ETF;数据为策划整理的开源多模态集合,并配有对应的决策环境,构成一个可公开访问的评测平台。

## 主要结果
主要产出是**基准本身**而非单一模型的胜负:通过十三个底座模型 × 多市场环境 × 多任务的系统评测,给出 LLM agent 在金融决策上的能力画像与可复现的比较平台。(具体分数需查全文。)

## 创新点
- 首个面向 LLM agent 金融决策的标准基准。
- 统一 agent 框架 + 多资产任务族,使不同任务下的结果可比。
- 十三个底座模型的系统对照,把「agent 设计」与「底座能力」分开看。
- 开源多模态数据集与环境,降低复现门槛。

## 局限
- 领域是金融而非生物医学,**任务语义与本方向无关**,可迁移的只有评测方法论。
- 金融决策的 ground truth 由市场回报定义,天然含噪且非平稳,与生物学的专家标注性质不同。
- 预印本,未见同行评议版本;摘要未给具体指标数值。

## 与本研究方向的关系
与 detect → model → revert 主链**没有内容上的交集**,收录它的理由只有一个:**它是「怎么给 agent 建基准」的方法论样本**。三点值得抄:(1) **把底座模型当作显式变量**做横扫(十三个 LLM),这与 DeepEvidence「所有系统统一底座」是同一问题的两种解法 —— 前者穷举、后者控制,都是为了分清赢在 agent 设计还是赢在模型;(2) **框架 + 任务族 + 环境 + 数据一起开源**的交付形态,是做 benchmark 该有的完整度;(3) 它示范了在一个「尚无标准」的领域里如何先立标准 —— 与本方向在非肿瘤病理/组学异常检测上无基准可用的处境同构。**不要从它这里拿任何生物学内容。**

## 可复用资产
- **论文与代码入口:** arXiv 预印本。
<https://arxiv.org/abs/2412.18174>
- **评测设计:** 统一 agent 框架下的多底座横扫(13 LLM)+ 多资产任务族 + 开源环境。

## 待读
- 查 ACL 2025 版本(aclanthology.org/2025.acl-long.126/),核对是否为同一工作的正式发表版并补齐指标。
- 提取它的任务定义与指标模板,看能否改造成生物医学 agent 的评测骨架。

## 引用
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

📄 **[AI-ready 全文提取 →](ai-ready.md)**
