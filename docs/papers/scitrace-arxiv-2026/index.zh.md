# SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents

> **文献键** `Swaminathan2026_260608234` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2606.08234> · `status: complete`

---

## 一句话
SciTrace(CMU)把安全推理「织进」AI scientist 流水线的每一步:**Safety-Intrinsic Reasoning Loop (SIR)** 在 Thinker → Experimenter → Writer → Reviewer 四个阶段之间维护并传递一个**累积风险状态**,**Compositional Tool-Chain Verifier (CTV)** 在每次工具调用前结合完整调用历史判断「这一串单步无害的操作合起来是否危险」;在 SciSafetyBench 上相对 SafeScientist 把工具调用安全率平均提升 14.3 个百分点,并抓到单步监控漏掉的 78.8% 组合式风险。

## 研究问题
现有 AI scientist 的安全层与核心推理是**结构上分离**的:只检查流水线输出,不参与产出它们的推理。这带来两个失败模式:(1) **风险信号是阶段局部的** —— SafeScientist 的四层防御各自独立,Thinker 阶段的 prompt monitor 标出的双重用途风险只写进本地缓冲,不会传给 Experimenter 与 Writer;(2) **单步监控看不到组合风险** —— 例如「检索病原体基因组」→「查询抗生素耐药数据库」→「请求蛋白结构预测」,每步单独看都能通过,但整条轨迹指向双重用途研究。

## 方法
在 SafeScientist 流水线上叠加两个组件,共享一个**累积风险状态**(SafeScientist 原有的过滤器只作为兜底)。**风险分级**:五级而非二元 —— SAFE、LOW-RISK、WARNING、HIGH-RISK、BLOCK;整体风险取所有信号的最大值,且某些类别组合(如双重用途 + 危险合成)同时出现时**再升一级**(interaction escalation)。**SIR**:每个阶段用结构化模板输入三样东西 —— 当前阶段任务内容、累积风险状态、从安全记忆中检索的历史检查项(仿 AGrail,按关键词重叠取 k 近邻);LLM 输出风险级别、自然语言描述与建议动作(proceed / modify / flag / block);各阶段提示侧重不同(Thinker 看双重用途、Experimenter 看工具与协议安全、Writer 看信息披露、Reviewer 带全量信号做伦理审查)。**CTV**:通过 verified tool proxy 拦截每次工具调用,单次 LLM 调用评三个维度 —— 请求本身是否有害、**该调用与完整历史是否构成危险轨迹(组合风险)**、该调用本身是否安全(改编自 ToolSafe 的 TS-Guard,把 attack-correlation 维度换成组合风险);合成分数映射为 allow / modify / block;被 modify 或 block 时,再用一次 LLM 调用(TS-Flow)给出**安全替代方案**(如把结核分枝杆菌换成非致病的耻垢分枝杆菌)而非硬性中止。风险分类含 9 类(S1 危险物质合成 … S9 组合危险)。SIR 与 CTV 使用与主 agent 相同的底座模型。

## 数据
SciSafetyBench(来自 SafeScientist):240 个高风险科研任务 + 120 个工具相关风险任务,30 个专用科学工具,均匀分布于物理、化学、生物、材料、信息科学、医学六个领域(每领域 40 + 20),按四种风险类型等比例标注(故意恶意、隐蔽危害、非故意后果、多步工具轨迹)。底座模型:Llama-3.1-70B-Instruct、Qwen2.5-72B-Instruct、DeepSeek-V3(本地 vLLM、4-bit AWQ、两张 RTX A5000)与 GPT-4o(API)。指标沿用 SafeScientist:Safety Score(1–5,GPT-4o 判分)、拒绝率、工具调用安全率、Quality/Clarity/Overall(1–5),另加组合风险检出率。

## 主要结果
**主表**(Bare LLM / SafeScientist / SciTrace,工具调用安全率):Llama-3.1-70B 38.5 / 76.3 / 91.2%;Qwen2.5-72B 40.2 / 78.1 / 92.5%;DeepSeek-V3 42.0 / 79.5 / 93.8%;GPT-4o 45.5 / 81.2 / 94.7% —— 平均 +14.3 pp;拒绝率在四个底座上为 92–95%(SafeScientist 85–90%);Safety Score 4.87–4.93;Quality/Overall 等质量指标同时略升(例如 Qwen2.5-72B 的 Overall 3.50 → 3.72)。与 AI Scientist、CycleResearcher、ResearchTown、AI Co-Scientist、Agent Laboratory 相比,这些框架的拒绝率仅 0–22%。**消融**(Qwen2.5-72B):仅 SIR 使 Safety +0.06、拒绝率 +2.5 pp;仅 CTV 使工具安全率 +11.6 pp;二者合用最好。**分领域**:生物(+17.3 pp)与化学(+17.2 pp)提升最大,物理最小(+10.7 pp);信息科学绝对值最低(86.6%)。**组合风险**:SafeScientist 单步全部放行但整条轨迹被判不安全的 80 个任务中,CTV 检出 63 个(78.8%);生物、化学、医学、材料 81–83%,物理 77.8%,信息科学仅 64.3%(数据外泄类模式与 CTV 针对的物理合成类轨迹结构不同)。**拒答分析**:直接拒绝只增加 5.9 pp,提升主要来自安全改道(+12.2 pp)与安全完成(+19.2 pp)。**对抗**:讨论攻击防御成功率平均 39.1% → 65.2%(+26.1 pp);各类攻击拒绝率平均 Llama 48.3 → 73.6%、GPT-4o 55.6 → 79.7%;对恶意讨论 agent 提升最大(+37.3 / +35.5 pp)。**代价**:每次流水线运行延迟增加 36.9–43.8%。

## 创新点
- 把安全从「阶段局部过滤器」改为**跨阶段传递的累积状态**,并引入分级风险与组合升级规则。
- **轨迹级**工具验证:判断的是「这一步 + 之前所有步」而非单步。
- 用纠正性反馈给出安全替代方案,在提升安全的同时不明显牺牲科研产出质量。

## 局限
- **评估高度依赖 GPT-4o 作为判分者**:作者在 60 个任务上的非正式验证显示与人工标签的 Pearson r 在物理/材料约 0.62、生物/化学约 0.81;尚无领域专家一致性研究与跨 judge 稳健性检验(作者自承)。
- 只在 SciSafetyBench 一个基准上评测,且建立在 SafeScientist 之上;「组合逃逸」本身也由 GPT-4o 判定,存在 judge 循环依赖。
- 安全记忆按关键词重叠检索,会漏掉语义相近但措辞不同的风险;S9 组合危险偏向物理合成,对数据隐私类轨迹检出低。
- 延迟增加约 37–44%;本地底座使用 4-bit 量化,可能影响与原论文结果的可比性。
- 主表数值在四个底座间非常整齐,但正文未报告多次运行方差(CI 在附录)。

## 与本研究方向的关系
主题是**安全**(双重用途、危险合成),与 Plan B 的**正确性**(claim 是否被证据支持)不同,但其**架构思想可以直接迁移到 Plan B 的 claim-to-evidence verifier**。(1) **累积状态跨阶段传递** ↔ 组学分析里,QC 阶段发现的问题(例如某批样本 ambient RNA 偏高、某 Xenium 切片配准差)常在下游 DE 与通路分析中被「遗忘」,最终 claim 却仍建立在这些样本之上;一个「累积可信度状态」(而非累积风险状态)在 QC → 聚类 → 注释 → DE → 结论各阶段传递,最后由 verifier 判断 claim 是否依赖了被标记的数据 —— 这正是 Plan A 的「跨模态一致性区分 artifact 与疾病」在 agent 层面的对应物。(2) **组合式检查** ↔ 组学中「每一步单看都合理、合起来得出错误结论」的典型情况:先按疾病状态做 batch correction、再在校正后数据上做疾病 DE(信号被循环利用);CTV 式「结合完整历史判断当前一步」正是检测这种问题的形式。(3) **五级风险 + 改道而非拒绝** ↔ verifier 输出不应只有「对/错」,而应有 supported / weakly supported / unsupported / contradicted 等分级,并给出「要支持这个 claim 还需要做什么分析」的建议。(4) **反面教材**:整套评估由 GPT-4o 判分、与人工 r 只有 0.62–0.81 —— 恰好说明 Plan B 需要**校准过、有专家标注验证的 verifier**,而不是又一个未经验证的 LLM judge(呼应 ABC 的 O.c.1)。对 Plan A 关系较远。

## 可复用资产
- **项目网站:** 未在论文正文中找到代码仓库链接。
<https://opensciagent.github.io/SciTrace/>
- **设计模式:** 五级风险 + 组合升级规则;SIR 三输入模板;CTV 三维评分 + TS-Flow 纠正反馈 —— 可改写为「累积可信度状态 + 轨迹级 claim 检查」。
- **基准:** SciSafetyBench(来自 SafeScientist),含医学与生物领域任务。

## 待读
- SafeScientist(Zhu et al., 2025)与 SciSafetyBench 原文。
- ToolSafe(TS-Guard / TS-Flow)与 AGrail:CTV 与 SIR 的直接来源。
- 附录 A(打分函数与阈值)、D(敏感性)、H(bootstrap CI)。

## 引用
```bibtex
@misc{Swaminathan2026_260608234,
  title = {SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents},
  author = {Tanush Swaminathan and Runmin Jiang and Letian Zhang and Min Xu},
  year = {2026},
  eprint = {2606.08234},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2606.08234}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
