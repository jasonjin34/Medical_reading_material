# Benchmarking large language models for biomedical natural language processing applications and recommendations

> **文献键** `Chen_2025` · **来源** Nature Communications(2025) · **类别** other · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s41467-025-56989-2> · `status: abstract-only`

---

## 一句话
在 12 个 BioNLP 基准、6 类应用上系统评测四个 LLM(GPT 与 LLaMA 代表)的 zero-shot / few-shot / 微调表现,并与 BERT、BART 的传统微调对比,结论是:**多数任务上传统微调仍胜过零样本或少样本 LLM**,GPT-4 只在医学问答等推理型任务上占优,开源 LLM 必须微调才能追平;同时系统记录了信息缺失与幻觉问题。

## 研究问题
生物医学文献增长使人工知识整理难以为继,BioNLP 负责自动化这件事。LLM 在通用领域表现亮眼,但**在 BioNLP 任务上到底行不行并不清楚** —— 缺基准、缺实用指南,也缺对成本与失败模式的量化。

## 方法
对四个 LLM(GPT 与 LLaMA 系代表)在三种使用模式下评测:zero-shot、few-shot、微调;基线是 BERT / BART 的传统微调。除了准确率,还专门检查**不一致性、信息缺失、幻觉**三类失败模式,并做成本分析 —— 这三项使它不只是排行榜,而是一份使用建议。

## 数据
12 个 BioNLP 基准,覆盖 6 类应用(命名实体识别、关系抽取、文本分类、问答、摘要等生物医学 NLP 常见任务族)。

## 主要结果
① **传统微调在多数任务上胜过零样本/少样本 LLM** —— 领域内小模型 + 标注数据仍是强基线。② 闭源 LLM(GPT-4)在**推理型任务**(如医学问答)上表现突出。③ 开源 LLM 仍需微调才能补上差距。④ LLM 输出中普遍存在**信息缺失与幻觉**。⑤ 成本分析提示:LLM 方案在很多任务上性价比并不占优。

## 创新点
- 覆盖广的 BioNLP 系统评测(12 基准 × 6 应用 × 3 使用模式),并给出实用建议而非只报分数。
- 把**幻觉与信息缺失**作为一等评测对象显式量化。
- 纳入成本分析,把「能不能用」和「值不值得用」分开回答。
- 明确保留传统微调基线,给出诚实的对照。

## 局限
- 模型迭代极快,2025 年的具体结论(尤其闭源模型分数)会迅速过时。
- 只覆盖文本模态的 BioNLP 任务,不涉及影像或组学。
- 幻觉与信息缺失的判定标准依赖人工与任务定义,跨任务可比性有限。

## 与本研究方向的关系
与主链无内容交集,但它提供了本方向**反复引用的一个论据**:在有标注的专业任务上,**领域内微调的小模型仍能打败通用大模型** —— 换句话说,瓶颈常在数据与任务定义,而不在模型容量。这与 PathBench 在影像侧得到的「规模不预测性能」是同一结论的两个侧面,可以互相印证。方法论上可迁移的是它把**幻觉与信息缺失做成显式评测维度**的做法:如果之后要评估一个会引用证据的 agent,「漏了什么」和「编了什么」必须和准确率并列成为指标,而不是附注。

## 可复用资产
- **评测协议:** 12 个 BioNLP 基准 × zero-shot / few-shot / fine-tune 三模式 × 传统微调基线,外加幻觉、信息缺失与成本三项分析维度。
- **论文(开放获取):**
<https://doi.org/10.1038/s41467-025-56989-2>

## 待读
- 取全文,记下 12 个基准的具体名单与幻觉判定标准,便于日后设计生物医学 agent 的失败模式指标。
- 与本仓库的 DeepEvidence 条目对读:后者用 agent 架构提升证据类任务表现,本篇则给出「不用 agent 时的地板」。

## 引用
```bibtex
@article{Chen_2025, title={Benchmarking large language models for biomedical natural language processing applications and recommendations}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-56989-2}, DOI={10.1038/s41467-025-56989-2}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Chen, Qingyu and Hu, Yan and Peng, Xueqing and Xie, Qianqian and Jin, Qiao and Gilson, Aidan and Singer, Maxwell B. and Ai, Xuguang and Lai, Po-Ting and Wang, Zhizheng and Keloth, Vipina K. and Raja, Kalpana and Huang, Jimin and He, Huan and Lin, Fongci and Du, Jingcheng and Zhang, Rui and Zheng, W. Jim and Adelman, Ron A. and Lu, Zhiyong and Xu, Hua}, year={2025}, month=Apr }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
