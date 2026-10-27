# TRAIL: Trace Reasoning and Agentic Issue Localization

> **文献键** `Deshpande2025_250508638` · **来源** arXiv preprint(2025) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2505.08638> · `status: complete`

---

## 一句话
Patronus AI 提出一套 agent 错误分类(推理 / 规划与协调 / 系统执行三大类),并发布 TRAIL:148 条人工逐 span 标注的 OpenTelemetry 结构化 agent 轨迹(来自 GAIA 与 SWE-bench Lite,共 841 个错误);让 LLM 当「轨迹调试员」去定位并分类错误时,最好的 Gemini-2.5-Pro 联合准确率也只有约 11%。

## 研究问题
agent 工作流越来越长、越来越复杂,现有评测依赖人工、领域特定地翻阅冗长轨迹,不可扩展;而错误分析又夹杂外部工具输出与 LLM 推理,比传统软件调试更难。已有轨迹分析(如 MAST)多基于解析后的非结构化文本,不代表真实框架输出的 OpenTelemetry 结构化日志;已有分类偏重推理与协调,缺少 API 错误、资源管理、任务编排等**系统执行与规划**类错误。

## 方法
**分类体系**:(1) **推理错误** —— 幻觉(纯语言幻觉、工具相关幻觉)、信息处理(检索不佳、工具输出误读)、决策(问题识别错误、工具选择错误)、输出生成(格式错误、违反指令);(2) **系统执行错误** —— 配置问题(工具定义错误、环境配置错误)、API 与系统问题(限流 429、认证 401/403、服务 500、资源不存在 404)、资源管理(资源耗尽、超时);(3) **规划与协调错误** —— 上下文管理(上下文处理失败、资源滥用/重复调用)、任务管理(目标偏离、任务编排错误)。每个错误标注位置(span id)、证据、描述与影响级别(LOW/MEDIUM/HIGH)。**轨迹构造**:GAIA 用 HuggingFace OpenDeepResearch 分层多 agent(manager + search agent,o3-mini 作底座);SWE-bench 用单 CodeAct agent(claude-3-7-sonnet,沙箱 + Python 解释器 + gitingest),并加入输出长度限制等约束以**有机诱发错误**;全部用 OpenInference(OpenTelemetry 衍生标准)记录。**标注**:4 名有软件工程与日志调试经验的标注员,另用 63 条轨迹测一致性(报告为「高」,具体数字在附录)。**评测任务**:给 LLM 完整原始 JSON 轨迹,让它输出错误类别与位置;指标为类别 F1、定位准确率、联合准确率,以及与人工评分的 Pearson 相关;结果为三次运行平均。

## 数据
148 条轨迹(共 1,987 个 OpenTelemetry span,其中 575 个至少含一个错误),841 个错误,平均每条 5.68 个;标注后 114 条 GAIA 轨迹与 30 条 SWE-bench 轨迹含错误。输出生成类错误最多 —— 格式错误与违反指令合计 353/841(约 42%);系统执行类错误稀少但往往难以恢复。原始输入极长:GAIA 轨迹平均约 26–31 万 token、最长 266 万–825 万 token(随 tokenizer 不同);SWE-bench 平均约 47–56 万 token —— 经常超过模型上下文上限。MIT 许可开源。

## 主要结果
**LLM 作为轨迹调试员表现很差**:最好的 Gemini-2.5-Pro 联合准确率在 GAIA 上约 18%、SWE-bench 上约 5%(合并约 11%);八个模型中三个无法装下完整上下文(SWE-bench 部分标为 CLE)。**长上下文是主因之一**:所有指标与输入长度负相关(定位准确率 Pearson −0.379 / Spearman −0.508;联合准确率 −0.291 / −0.349;类别 F1 −0.296 / −0.225)。**推理有帮助**:除 o1 外,推理模型在类别 F1 与定位准确率上均优于非推理模型,联合准确率是最佳非推理模型的 1.5–8 倍;o3 降低 reasoning effort(high → medium → low)时类别 F1 由 0.296 → 0.277 → 0.264 单调下降。**分类别**:上下文处理失败几乎所有模型 F1 为 0(仅 Claude-3.7-Sonnet 0.18);工具选择错误多数 0.00–0.08(o3 0.53 例外);任务编排普遍 0.00–0.08(Gemini-2.5-Flash 0.47 例外);纯语言幻觉相对容易(0.14–0.59)。

## 创新点
- 覆盖推理、规划、系统执行三层的细粒度 agent 错误分类,补上了 API / 资源 / 编排类错误。
- 首个基于 OpenTelemetry 结构化日志、逐 span 定位的人工标注轨迹基准,具有生态效度。
- 证明「LLM-as-a-judge 读轨迹」在长上下文下严重失效,为可扩展轨迹评估设定了难度基线。

## 局限
- 只有文本模态;只来自两个基准(GAIA、SWE-bench Lite)和两种 agent 配置,轨迹数(148)偏少。
- 长尾类别样本极少,而这些往往是高影响错误;作者建议合成数据补足。
- 部分错误是通过提示约束人为诱发,与自然发生错误的分布可能不同。
- 正文只说标注一致性「高」,具体数字在附录;来自公司研究团队,配套商业产品。

## 与本研究方向的关系
主要服务 **课题 2 的「组学专属失败分类」与 verifier 设计**。(1) **分类模板**:TRAIL 的三层结构(推理 / 规划协调 / 系统执行)可以直接作为骨架,往下挂组学专属叶子 —— 推理层加「统计检验误用」「把批次/环境 RNA 当生物信号」「cluster 注释幻觉」;系统执行层加「参考基因组/注释版本不匹配」「内存耗尽(大 h5ad)」;规划层加「跳过 QC 直接做 DE」「跨模态(snRNA vs snATAC vs Xenium)结论不一致却未检查」。(2) **任务形式**:TRAIL 把评测定义为「定位到哪一个 span 出错 + 什么类型」—— 这比「最终答案对不对」更接近 claim-to-evidence:我们要的 verifier 也要指出**哪一步分析支撑不了哪个 claim**。(3) **难度警示**:最强模型联合准确率只有约 11%,且性能随轨迹长度下降 —— 组学 agent 的轨迹(大表格输出、长代码)只会更长,所以 verifier 不能只是「把整条轨迹丢给一个 LLM」,需要分段、结构化检索或专用模型。(4) OpenTelemetry/OpenInference 记录格式值得在课题 2 的 rerun 实验中直接采用,便于与 TRAIL、HAL 工具链对接。对课题 1 关系较远;但「错误要带位置与证据」的标注规范同样适合 KidneyAnomalyBench 的专家标注(异常必须定位到 spot/细胞/区域并给出证据)。

## 可复用资产
- **数据:** TRAIL 数据集(MIT)。
<https://huggingface.co/datasets/PatronusAI/TRAIL>
- **分类体系:** 图 1 / 第 3 节的错误类别定义,可直接改写为组学 agent 失败分类的上层结构。
- **标注格式:** category / location / evidence / description / impact 五字段 JSON,可直接用于我们的轨迹标注。

## 待读
- 附录 A.7 的标注一致性具体数字;A.4 的 reasoning effort 消融全表。
- 与 MAST 的分类对照(TRAIL 自称补足 MAST 缺少的执行与规划类)。
- 后续是否有面向科学/生物信息 agent 的轨迹标注基准。

## 引用
```bibtex
@misc{Deshpande2025_250508638,
  title = {TRAIL: Trace Reasoning and Agentic Issue Localization},
  author = {Darshan Deshpande and Varun Gangal and Hersh Mehta and Jitin Krishnan and Anand Kannappan and Rebecca Qian},
  year = {2025},
  eprint = {2505.08638},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2505.08638}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
