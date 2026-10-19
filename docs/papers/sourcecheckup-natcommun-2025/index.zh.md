# An automated framework for assessing how well LLMs cite relevant medical references

> **文献键** `Wu_2025` · **来源** Nature Communications(2025) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41467-025-58551-6> · `status: complete`

---

## 一句话
SourceCheckup 是一条全自动的 agent 流水线:出医学问题 → 让 LLM 作答并给出处 → 拆成独立可验证的 statement → 下载 URL 全文 → 用 GPT-4o 逐对判断「这个来源是否支持这句话」;在 7 个模型、800 题、约 5.8 万个 statement–source 对上发现 **50%–90% 的回答并未被其引用完全支持**,即便联网的 GPT-4o(RAG)也只有 55% 的回答完全被支持;该自动核验与三位执业医生共识一致率 88.7%,高于医生之间的平均一致率 86.1%。

## 研究问题
LLM 已能按要求给出出处,RAG 还能实时搜索,但**给出的来源是否真的支持其医学陈述**一直缺乏系统度量。人工专家标注昂贵、难以复现,且跟不上模型迭代;临床医生把「不能给出可靠出处」列为不信任 LLM 的首要原因,FDA 等监管也需要可审计的出处。作者刻意只评估「陈述是否扎根于可验证来源」,而非「陈述本身对不对」—— 因为医学真值本身常有争议(如网球肘好发年龄有多个重叠答案)。

## 方法
四个模块(均以 GPT-4o 为骨干):**(1) 问题生成** —— 从 400 篇 MayoClinic 页面各生成 1 题,加上 400 条 Reddit r/AskDocs 真实提问,共 800 题(避免 MedQA/PubMedQA 固定题集被记忆);**(2) LLM 作答** —— 要求简短回答 + 结构化来源列表(GPT-4o RAG 需显式要求使用 Bing 搜索);**(3) Statement 与 URL 解析** —— 拆成独立可验证的 statement,下载 URL(仅保留 HTTP 200,PDF 转文本,超 128K token 的丢弃,约 0.1%);**(4) Source Verification** —— 对 M 条 statement × N 个来源做全部 M×N 对的 1-1 判断,statement 至少被一个来源支持即算 supported。三个指标:**Source URL Validity**、**Statement-level Support**、**Response-level Support**(该回答所有 statement 都被支持),延伸自 AIS(Attributable to Identified Sources)。另做 **SourceCleanup** agent:给定不被支持的 statement 与其来源,自动删改为被支持的版本。并以 Claude Sonnet 3.5 复刻全流程检验对 GPT-4o 的偏倚。

## 数据
800 题(400 MayoClinic 生成 + 400 Reddit r/AskDocs);约 5.8 万 statement–source 对(来自 800 余篇参考文档);医生标注 400 对 statement–source;额外 HealthSearchQA 300 题验证、100 题端到端人工评估。被评模型:GPT-4o(RAG)、GPT-4o(API)、Claude v2.1、Mistral Medium、Gemini Ultra 1.0(RAG)、Gemini Pro(API)及 Mixtral-8x7b;Llama-2-70b 与 Meditron-7b 因几乎不产出 URL(<5%、<1%)被移出主结果。

## 主要结果
**核验器可靠**:与医生共识一致率 88.7%,医生间平均 86.1%,无显著差异(p=0.21);Claude Sonnet 3.5 当核验器一致率 87.0%(与 GPT-4o 无显著差异,p=0.52),两者互相一致 90.1%;开源 Llama 3.1 70B 仅 79.3%。问题生成 100/100 被医生判为合格,statement 解析 330/330、329/330 正确。**模型表现**:GPT-4o(RAG)最好,但 **response-level support 只有 55%**;Gemini Ultra 1.0(RAG)仅 34.5%;Gemini Pro API 约 10%;无联网模型的 URL 有效率仅 40%–70%(GPT-4o API 约 70%)。GPT-4o(RAG)即便被明确要求,也有 >20% 回答不给来源。对 110 个被判「不支持」的 GPT-4o(RAG)对,医生同意率 95.8%(105/110 确认不支持)。**题源效应**:GPT-4o(RAG)在 MayoClinic 题上 response-level support 接近 80%,在 Reddit 题上降到约 30%(p<0.001);HealthSearchQA 上 statement-level 75.7%、response-level 38.4%;端到端人工评估 40.4% vs SourceCheckup 42.4%,高度吻合。将来源合并后,95.1% 原本不支持的 statement 依旧不被支持。**SourceCleanup**:150 条不支持 statement 中删除 34.7%,其余 98 条修改后 85.7% 被支持,合计 90.7% 被删除或正确修改。约 92% 的引用来自美国网站。

## 创新点
- 把「引用是否支持陈述」做成**可自动、可复现、经医生面板验证**的度量,而不是一次性人工审计。
- 三级指标(URL 有效 → statement 支持 → response 全支持)把「链接存在」「单句有据」「整答可信」分开。
- 证明「RAG 不是银弹」:联网能消灭 URL 幻觉,却不能保证内容被支持。
- 公开 800 题、5.8 万对与医生标注作为社区资源;SourceCleanup 展示了「核验后修复」闭环。

## 局限
- 各自动模块(出题、解析、抽引、核验)误差会累积;医生之间本就不完全一致,单点数据有噪声。
- 1-1 statement–source 映射不计「多来源合成才支持」的情况(作者检验后影响很小:95.1% 仍不支持)。
- 只测「是否被来源支持」,不测正确性;作者提醒可被「逐字照抄来源」这种平凡策略刷满,应与质量指标并用。
- 评测模型较旧(2024 年初);题源以美国网站为主;部分网站 404/付费墙影响 URL 有效性判断。
- 核验器本身用 GPT-4o,同家族自评存在潜在偏倚(作者用 Claude 复刻部分缓解)。

## 与本研究方向的关系
对 **Plan B** 而言,SourceCheckup 提供了「claim-to-evidence 核验器」的**验证范式**,比方法本身更值得抄:(1) 先证明自动核验器与专家面板的一致率**不低于专家之间的一致率**,再用它规模化评估 —— 这正是 Plan B「校准 verifier」需要的论证结构,只是我们的「专家」是肾脏病理/组学专家,「来源」是 agent 的分析产物与 KPMP/Lake 等参考数据;(2) 三级指标可以直接映射为组学版:**产物存在**(agent 引用的文件/图/表是否真实生成)→ **单条结论被支持**(该结论能否从产物中复现)→ **整份报告全支持**;(3) Reddit vs MayoClinic 的巨大落差提示:**开放式、需要多源综合的问题**(正对应「这个异常区域是疾病还是伪影」这类 Plan A 问题)最容易出现无据陈述,benchmark 应刻意包含此类题。SourceCleanup 的「核验 → 删改」闭环可作为 agent 自我修正的基线。它不涉及数值/统计结论与重复运行稳定性,这两点是 Plan B 需要补的空白。

## 可复用资产
- **代码与全部 prompts:**
<https://github.com/kevinwu23/SourceCheckup>
<https://doi.org/10.5281/zenodo.15015209>
- **数据:** 800 题、回答、解析出的 statement、5.8 万 statement–source 对与医生标注(Google Drive,非商业研究用途;原始网页因版权未包含)。
<https://drive.google.com/drive/folders/1a-i974g3XzLCtZLpTLBbqAwK0olpd5JY>
- **评测协议:** Source URL Validity / Statement-level Support / Response-level Support;核验器 vs 医生面板一致率 vs 医生间一致率。

## 待读
- ALCE(Gao et al.)、AttributedQA、AIS(Rashkin et al.)—— 归因评估的基础定义。
- 本仓库 reference-hallucination-arxiv-2026 对本文「RAG 模型不会 URL 幻觉」的结论做了修正,两篇对读。
- 补充表 4/8/10(各模型完整数值、样本量、未被使用的 URL 比例)。

## 引用
```bibtex
@article{Wu_2025, title={An automated framework for assessing how well LLMs cite relevant medical references}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-58551-6}, DOI={10.1038/s41467-025-58551-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Wu, Kevin and Wu, Eric and Wei, Kevin and Zhang, Angela and Casasola, Allison and Nguyen, Teresa and Riantawan, Sith and Shi, Patricia and Ho, Daniel and Zou, James}, year={2025}, month=Apr }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
