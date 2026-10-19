# Enhancing EHR-based pancreatic cancer prediction with LLM-derived embeddings

> **文献键** `Park_2025` · **来源** npj Digital Medicine(2025) · **类别** ehr · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s41746-025-01869-8> · `status: complete`

---

## 一句话
在 CancerRiskNet 式的胰腺癌轨迹 Transformer 里,把随机初始化的诊断码嵌入换成**LLM 对 OMOP 概念名称的文本嵌入**(OpenAI text-embedding-3-small),在 Columbia(CUMC)与 Cedars-Sinai(CSMC)两家美国院内 EHR 上,6–12 个月预测 AUROC 分别从 0.59/0.82 提升到 0.67/0.86;再排除确诊前 0–3 个月数据,升到 0.82/0.89。

## 研究问题
胰腺癌 5 年生存仅 13%,早期确诊可升至 44%;但筛查只覆盖家族史/胚系变异人群(仅 5–10% 病例),MRI/CT 不可能在一般人群中普查。EHR 的纵向病史可能藏有早期信号。受 GenePT(用 GPT 对基因 NCBI 描述做嵌入)启发,作者假设:**LLM 对医学概念名称的语义嵌入**能比从头学的嵌入更好地表示诊断码,从而提升早期预测 —— 尤其在单个医院这种比国家登记小得多、更异质的数据上。另一个问题是**临近确诊数据造成的泄漏**:多时间窗共享模型里,近端强信号会「渗透」到远端窗口。

## 方法
**数据格式**:OMOP CDM 的诊断(condition)序列 + 记录时年龄作为 positional encoding。**嵌入来源**(用于初始化诊断码嵌入):(a) baseline:PyTorch nn.Embedding 随机初始化;(b) RGCN:在 OMOP 祖先-后代层级构成的知识图上训练关系图卷积网络得到概念嵌入;(c) **GPT**:OpenAI text-embedding-3-small 对 OMOP 概念名称编码,32 维与 1536 维两种;(d) Mistral:SFR-Embedding-Mistral(4096 维)。每种再分冻结 vs 微调,共 12 个模型。**两种任务形式**:(1) **多标签模型**(仿 CancerRiskNet)同时预测 0–3、3–6、6–12、12–36、36–60 个月五个窗口;评估时每个窗口只用确诊恰落在该窗口的病例,避免近端病例抬高远端分数;另训练一个**排除 0–3 个月数据**的版本(这部分数据转去扩充 3–6 个月窗口)。(2) **二分类模型**(3–6、6–12、12–36 个月各一个),用**数据增强**:把近端病例的最近记录逐条删除,直到最后一条记录落入目标窗口,以扩充远端窗口的病例数。60/20/20 划分;bootstrap 95% CI;LIME 解释;并与传统危险因素(CA19-9、2 型糖尿病、胰腺炎)和已知胚系变异比较 PPV。

## 数据
**CUMC**(哥伦比亚大学医学中心)3,300 例 / 785,335 对照;**CSMC**(Cedars-Sinai 医学中心,洛杉矶 —— 注意**不是** Mount Sinai)1,781 例 / 484,515 对照。病例为胰腺恶性肿瘤诊断码且无其他癌症史;对照排除任何癌症相关词、近 2 年内诊断、<5 条诊断记录、<18 或 >100 岁。CSMC 有遗传数据:1,500 名携带胰腺癌相关变异者,其中 130 人患胰腺癌(数据集中保留 50 人)。**留出测试集中远端窗口病例极少**:CUMC 6–12 个月仅 23 例、36–60 个月 14 例;CSMC 6–12 个月 18 例、36–60 个月 7 例。HIPAA 禁止共享 EHR,两中心通过共享代码分别运行。

## 主要结果
- **6–12 个月(多标签,含 0–3 个月数据)**:CUMC baseline 0.592 → GPT-1536 **0.673**;CSMC 0.819 → **0.858**。CUMC 上 RGCN 0.647,Mistral 0.598(但 Mistral max-F1 最高,p = 0.035)。
- **排除 0–3 个月后(GPT-1536)**:6–12 个月 CUMC **0.819**、CSMC **0.893**;但 3–6 个月反而下降(CUMC 0.856→0.763,CSMC 0.884→0.870)—— 说明晚期症状可前推到约 6 个月,但不会更早。
- **嵌入维度**:GPT 32 维常与 1536 维相当甚至更好;Mistral 4096 维并不稳定占优;微调对 32 维帮助大、对 1536 维帮助小。
- **与 CancerRiskNet 对比(36 个月内)**:baseline AUROC 0.694(CUMC)/ 0.744(CSMC)vs CancerRiskNet 0.88;排除 0–3 个月后 0.737/0.771 vs 0.83;加 LLM 嵌入后 **0.761/0.811** —— 院内数据仍低于丹麦国家登记。
- **临床效用(CUMC,6–12 个月二分类,338 例 / 157,067 对照)**:GPT 模型 max-F1 点 PPV **0.141**(22 TP / 134 FP)vs「任一传统危险因素」PPV **0.004**(96 TP / 24,950 FP);要检出 50% 病例需筛查 17% 人群。**但 CSMC 上 GPT 模型 max-F1 点 PPV 只有 0.012**(baseline 0.084)—— 摘要中的 0.141 只对应 CUMC。
- **补充传统危险因素**:模型检出的病例中,CUMC 超过 50%、CSMC 超过 85% 既无传统危险因素也无已知胚系变异。
- **特征**:LIME 显示 GPT 嵌入模型更偏向临床可解释特征(baseline 常出现骨折等无关项);二分类模型在 6–12 与 12–36 个月窗口都把**肾脏/输尿管疾病**与肝病列为前列特征。

## 创新点
- 用**LLM 对概念名称的文本嵌入**初始化 EHR 码嵌入 —— 零额外训练成本,可直接插入任何 EHR 序列模型。
- 系统比较嵌入来源(随机 / 知识图 RGCN / GPT / Mistral)、维度与冻结-微调。
- 明确指出并处理**多标签多时间窗模型的泄漏**:按窗口限定评估病例、排除 0–3 个月数据、二分类 + 截断式数据增强。
- 双中心、仅共享代码不共享数据的验证模式;报告 PPV 与「需要筛查多少人」的临床口径。

## 局限
- **远端窗口病例极少**(留出集 6–12 个月仅 18–23 例),CI 很宽(如 CUMC 0.673 [0.559, 0.776]);部分增益未达显著。
- **两站点结论不一致**:GPT 嵌入在 CSMC 稳定提升,在 CUMC 不一致;CSMC 上的 PPV 反而低于 baseline。
- 只用诊断序列,无化验、用药、文本;家族史等关键危险因素在非结构化记录里,未利用。
- 评估队列中的患病率(215/10 万)远高于真实人群(约 32/10 万),真实 PPV 会更低。
- 依赖闭源 OpenAI 嵌入 API(概念名称虽不含 PHI,但可复现性与版本稳定性受限)。

## 与本研究方向的关系
**对 Sinai EHR 项目,这篇最接近「我们自己会遇到的处境」**:单个美国学术医疗中心、OMOP 格式、几十万到百万级病人,而不是丹麦那种完整的国家登记 —— 本文显示同一任务在院内数据上 AUROC 明显低于 CancerRiskNet,而两家医院之间的结论也不一致。可直接借用的三件事:(1) **LLM 概念名称嵌入作为初始化**,成本几乎为零,Sinai 的 OMOP 概念表可以直接生成;值得同时测试开源嵌入模型以避免闭源依赖;(2) **反泄漏评估**:按窗口限定评估病例 + 排除 0–3 个月 + 截断式增强 —— 这比只报一个 AUROC 严格得多;(3) **报告口径**:PPV、「检出 50% 需要筛查多少人」。需要警惕的是:摘要只报 CUMC 的 PPV 0.141,而 CSMC 上 PPV 只有 0.012 —— 这正是 Plan B「claim-to-evidence 校验」应当抓住的选择性报告类型,可作为 omics/EHR agent 失败分类中的一个具体样例。**与心-代谢-肾方向**:二分类模型把**肾脏疾病**列为胰腺癌 6–36 个月前的早期特征,作者解读为多器官系统性信号 —— 这提示在 Sinai 上做心-代谢-肾轨迹模型时,肾相关码本身就是跨病种的强信号;反过来,这套「LLM 嵌入 + 多窗口 + 反泄漏」流程可原样用于 CKD/DKD 进展预测。与 detect → model → revert:这是 EHR 层的 detect,改进点在表示(把医学知识注入嵌入),而非因果。

## 可复用资产
- **代码:** 胰腺癌 Transformer(两中心共用)。
<https://github.com/jp4147/pdac_tf>
- **数据:** HIPAA 限制,不共享。
- **嵌入模型:** OpenAI text-embedding-3-small(32/1536 维)、Salesforce/SFR-Embedding-Mistral;OMOP 层级 RGCN(补充说明 2)。

## 待读
- GenePT(启发本文的基因文本嵌入工作)。
- 文中 ref 13:肾脏异常作为胰腺癌早期系统表现的研究。
- 补充说明 4–5:跨模型一致高风险人群的分析(多模型共识作为筛查人群定义)。
- 与 `ehr-pancreatic-trajectory-natmed-2023`(CancerRiskNet)逐项对照阅读。

## 引用
```bibtex
@article{Park_2025, title={Enhancing EHR-based pancreatic cancer prediction with LLM-derived embeddings}, volume={8}, ISSN={2398-6352}, url={http://dx.doi.org/10.1038/s41746-025-01869-8}, DOI={10.1038/s41746-025-01869-8}, number={1}, journal={npj Digital Medicine}, publisher={Springer Science and Business Media LLC}, author={Park, Jiheum and Patterson, Jason and Acitores Cortina, Jose M. and Gu, Tian and Hur, Chin and Tatonetti, Nicholas}, year={2025}, month=July }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
