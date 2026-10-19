# DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence

> **文献键** `NarayananVenkit2025_250904499` · **来源** arXiv preprint(2025) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2509.04499> · `status: complete`

---

## 一句话
DeepTRACE 把先前用户研究中社区识别出的生成式搜索/deep research 失效案例,转化为覆盖「答案文本 · 来源 · 引用」的 **8 个可计算指标**,核心是两张矩阵 —— **引用矩阵**(statement 引了哪些来源)与**事实支持矩阵**(哪些来源真的支持该 statement);在 303 个问题 × 9 个公开系统上发现:deep research 降低了过度自信,但在辩论题上仍高度片面,无支持 statement 比例很高,引用准确率只有 40%–80%。

## 研究问题
生成式搜索引擎(GSE)与 deep research agent(DR)宣称提供有出处的综合,但用户频繁遇到过度自信、来源薄弱、引用混乱;LLM 会幻觉、检索常给出错误引用、参数化知识难以与检索内容分离,还会**谄媚**(迎合查询暗含的立场)。现有基准多评孤立组件(检索或摘要),或像 DeepResearch Bench、BrowseComp-Plus 那样只看任务完成度,评价标准完全由研究者定义、缺少终端用户输入。作者主张一种「社会技术」视角:从真实用户识别的 16 个失效案例出发,端到端审计系统如何推理、引用与使用证据。

## 方法
**预处理**:用自动浏览器脚本抓取查询、答案、行内引用与来源 URL;LLM(GPT-5)把答案拆为 statement,并标注 **Query Relevance**(是否含答案要素)与 **Pro/Con**(仅辩论题);LLM judge 给答案打 1–5 的 **Answer Confidence**;Jina Reader 抓取来源全文(约 15% 因付费墙/404 失败,排除);构建引用矩阵与事实支持矩阵(LLM judge 判断每个 statement–source 对)。**8 个指标**:I One-Sided Answer(辩论题无正反两面即为片面);II Overconfident Answer(片面且置信度=5);III Relevant Statement 比例;IV Uncited Sources(列出却未被引用的来源);V Unsupported Statements(相关 statement 中无任何来源支持的比例);VI **Source Necessity**(把支持矩阵转成二部图,用 Hopcroft–Karp 求最小顶点覆盖,得到「必要来源」比例);VII **Citation Accuracy** = Σ(引用 ⊙ 支持)/Σ引用;VIII **Citation Thoroughness** = Σ(引用 ⊙ 支持)/Σ支持。每个指标按用户研究得出的阈值标为可接受/临界/有问题。

## 数据
DeepTRACE 数据集 303 题:**辩论题 168 道**(来自无党派平台 ProCon.org)+ **专业题 135 道**(用户研究中气象、医学、HCI 等领域专家提出、需多跳检索)。9 个系统:GSE 为 You.com、BingChat/Copilot、Perplexity、GPT-4.5;DR 为 GPT-5 Deep Research、YouChat DR、Perplexity DR、Copilot Think Deeper、Gemini DR,另含 GPT-5 web search。共 2,727 个样本(数据截至 2025-08-27);约 8 万次事实支持判断。LLM judge 验证:置信度评分与人工 Pearson r=0.72,事实支持判断与人工 r=0.62(各 100 例,两名标注者)。

## 主要结果
**GSE**:辩论题片面率约 50%–90%(Perplexity 83.4%、GPT-4.5 90.4%),Perplexity 过度自信 81.6%;无支持 statement 23.1%–47.0%;引用准确率 39.8%–68.3%;BingChat 平均列 4.0 个来源,但 36.2% 未被引用、只有约一半必要。**DR**:片面率仍 54.7%–94.8%(GPT-5 DR 54.67%、Copilot TD 94.8%),但过度自信普遍 <20%(唯一的相对优势);相关 statement 除 GPT-5 DR(87.5%)外均 <50%(Gemini DR 12.4%);**无支持 statement**:GPT-5 DR 12.5%,其他 53.6%(Gemini)到 97.5%(Perplexity DR);引用准确率 31.4%–79.1%;引用彻底度 GPT-5 DR 87.5%、YouChat DR 83.5%,其余 9.1%–27.1%。GPT-5 DR 在多数维度上最好,说明「接近理想」是可达的。**跨系统结论**:更多来源、更长答案并不带来更可靠的 grounding,反而导致「搜索疲劳」;DR 对同一议题正反两种问法都给出一边倒答案,呈现谄媚。(注:正文称 Gemini DR 引用准确率 40.3%,与表中 50.3% 不一致,此处以表为准并存疑。)

## 创新点
- 引用矩阵 × 事实支持矩阵的形式化:Citation Accuracy(引得对不对)与 Thoroughness(该引的引没引)成为一对类似 precision/recall 的指标。
- Source Necessity 用最小顶点覆盖识别「凑数来源」,区分「列了很多」与「真正需要」。
- 从用户研究出发设计指标和阈值(社会技术评估),而非研究者拍脑袋。
- 把片面性、过度自信、谄媚纳入 deep research 的可靠性审计。

## 局限
- 事实支持判断依赖 LLM judge,与人工只有中等相关(r=0.62),作者自陈为限制因素。
- 系统输出靠网页抓取脚本获得,随界面改版而失效;约 15% 来源无法抓取被排除;结果是 2025-08 的时点快照。
- 未实现用户研究中「界面」类发现的指标;阈值来自单一用户研究。
- 正文与表格存在个别数值不一致(见上);主要面向通用/辩论信息检索,非生物医学专用。

## 与本研究方向的关系
对 **Plan B** 的价值在于**指标设计**而非结论。两张矩阵可以直接迁移到「agent 分析肾脏组学后的报告」:行 = 报告中的原子结论,列 = agent 产出的分析产物(DE 表、聚类、空间统计图、引用文献);引用矩阵记录 agent 自称依据了什么,支持矩阵记录 verifier 判定实际能支持什么。由此,**Citation Accuracy** 衡量「agent 引用的产物是否真的支持该结论」,**Thoroughness** 衡量「有证据却没被引用」,**Unsupported Statements** 正是 Plan B 核心的「无证据结论」率,**Source Necessity** 可识别 agent 为显得严谨而附上的冗余分析。片面性/谄媚指标对应一个组学特有的失效模式:当用户问「这个区域是不是疾病导致的?」时,agent 只汇报支持性证据、忽略伪影解释(这正是 Plan A 中跨模态一致性要排除的情形)。它的人工-judge 相关只有 0.62,也提醒 Plan B:verifier 本身必须先校准、再部署。与 Plan A 无直接关系。

## 可复用资产
- **数据集:** DeepTRACE 303 题(168 辩论 + 135 专业),论文称公开发布(正文未给仓库链接)。
- **指标定义:** 8 个指标的公式(式 1–8)与阈值表(附录 B)。
- **工具:** Jina Reader 抓取来源全文;Hopcroft–Karp 最小顶点覆盖。
<https://jina.ai/reader/>

## 待读
- Narayanan Venkit et al. (2025) 原始用户研究 —— 16 个失效案例与设计建议的出处。
- Liu et al. (2023) 对生成式搜索引擎的可验证性审计。
- 与本仓库 deep-research-hallucination-arxiv-2026(过程级)对读:DeepTRACE 只看最终报告。

## 引用
```bibtex
@misc{NarayananVenkit2025_250904499,
  title = {DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence},
  author = {Narayanan Venkit, Pranav and Laban, Philippe and Zhou, Yilun and Huang, Kung-Hsiang and Mao, Yixin and Wu, Chien-Sheng},
  year = {2025},
  eprint = {2509.04499},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2509.04499}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
