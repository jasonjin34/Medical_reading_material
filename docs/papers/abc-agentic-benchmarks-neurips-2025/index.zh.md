# Establishing Best Practices for Building Rigorous Agentic Benchmarks

> **文献键** `Zhu2025_250702825` · **来源** NeurIPS 2025 Datasets and Benchmarks Track(2025) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2507.02825> · `status: complete`

---

## 一句话
作者把 agent 基准「分数可信」拆成两个条件 —— **task validity**(任务成功 ⇔ 具备目标能力)与 **outcome validity**(评测判定为成功 ⇔ 任务真的成功)—— 并据此写出一份可操作的 **Agentic Benchmark Checklist (ABC)**;用它审查 10 个主流 agent 基准,发现 7 个违反 outcome validity、7 个违反 task validity、10 个全部在结果报告上有缺陷,误差最高可达相对 100%。

## 研究问题
agent 基准与传统多选/文本生成基准根本不同:成功的定义是「端到端完成任务」,结果是代码、文件改动、环境状态、自由文本等**非结构化产物**,需要靠单元测试、字符串匹配、状态匹配、LLM-as-a-Judge 等定制方法来判分。这些判分方法与任务搭建本身都可能出错,导致高估或低估能力。典型例子:SWE-bench-Verified 的单元测试不足,前 50 名中 24% 的排名是错的;τ-bench 中一个**什么都不返回的 trivial agent** 在故意设计成不可完成的任务上被判成功,成功率 38%,超过 GPT-4o agent。领域缺少一份系统、可执行的审查指南。

## 方法
**语料**:17 个被头部 AI 厂商(OpenAI、Anthropic、Amazon、Meta、Google、xAI、Mistral、DeepSeek)使用或获奖的 agent 基准;结合已有的基准缺陷报告、agent 评测框架(如 UK AISI 的 Inspect)以及软件测试最佳实践,加上作者自己造基准(CVE-Bench 等)的经验,整理成 ABC。**ABC 三部分**:(1) **Task validity**(T.1–T.10):工具版本明确、API 可用且失效时终止、运行间残留状态清空、agent 与 ground truth 完全隔离、环境不随时间漂移(不依赖线上网站)、ground truth 经核验、每个任务验证可解、提供 **Oracle solver**、实现中无可被利用的漏洞;(2) **Outcome validity**(O.a–O.i,按产物类型与判分方法分组):字符串匹配要处理语义等价/冗余词/否定词、防止「列出所有可能答案」与猜测;**LLM-as-a-Judge 必须有准确率、自洽性与人类一致性的证据并能抵御对抗输入**;单元测试需人工核验并用覆盖率等客观指标;fuzz 测试要覆盖边界、数据类型、内存布局;E2E 测试防 flaky;状态匹配要包含所有可达成功状态并检查无关状态;(3) **Benchmark reporting**(R.1–R.13):开源数据与 harness、防污染(私有测试集)、说明构念效度、记录缺陷缓解措施并做定性与定量影响分析、**报告置信区间**、给出解读指南、报告非 AI 基线(人类专家)与 **trivial agent(什么都不做的 agent)** 的结果。**打分**:每满足一项得 1 分,按适用项求平均。

## 数据
审查对象为 10 个开源基准,覆盖全部能力类型与判分方法:SWE-bench(单元测试)、SWE-Lancer(E2E 测试)、KernelBench(fuzz 测试)、BIRD(单元测试/答案匹配)、Cybench(答案匹配)、MLE-bench(质量指标)、GAIA(答案匹配)、τ-bench(子串匹配 + 状态匹配)、WebArena(整串/子串匹配 + LLM 判分 + 状态匹配)、OSWorld(状态匹配)。案例研究:CVE-Bench(真实 Web 漏洞利用的网络安全基准)。

## 主要结果
**总体**:10 个基准中 7 个违反 task validity、7 个违反 outcome validity、全部 10 个在报告上不达标;80% 的基准不承认自身设计/实现弱点,没有任何一个满足全部报告条目。**具体新发现**:(1) τ-bench 用平凡状态/子串作为 ground truth(违反 O.b.3、O.g.3),高估 38%;允许 agent 列出所有可能答案(违反 O.b.2),高估 40% —— 航空子集 38%、零售子集 6% 的任务本就不可完成,「什么都不做」即通过;(2) WebArena 子串匹配忽略多余内容、LLM judge 在「N/A」任务上接受空回复且未验证准确性(违反 O.c.1),高估 1.4–5.2%;(3) **SWE-Lancer 未把 agent 与 ground truth 隔离(违反 T.5)**:测试文件在密码保护的 ZIP 中,但目录可列出、内容可覆盖,agent 换成 `assert 1 == 1` 即可**拿到 100% 而不解决任何任务**;(4) KernelBench 的 fuzzer 只改张量数值、不改形状与内存布局(违反 O.e.1/O.e.2),kernel 正确率被高估约 31%(绝对值);(5) OSWorld chrome 部分 46 题中 13 题因网站改版而坏掉,导致 UI-TARS 被低估 28%(绝对值)。**CVE-Bench 修订**:时间型 SQL 注入只检查日志中是否出现 SLEEP(违反 O.g.1),高估 32.5%;outbound server 同 docker 网络可达形成捷径,修复后成功率下降 10%;总体 ABC 使 CVE-Bench 的性能高估减少 33%(绝对值),经网络安全专家确认。

## 创新点
- 把 agent 评测的严谨性形式化为 task validity 与 outcome validity 两个等价条件,配一张「操作流程 vs 概念流程」图。
- 首份可逐项打勾的 agent 基准清单(task / outcome / reporting 三部分),按产物类型与判分方法给出具体检查项。
- 在 10 个主流基准上量化出新的缺陷,并给出可复现的实验。
- 用 CVE-Bench 展示「在建基准时」如何用 ABC 修正,而不只是事后审计。

## 局限
- 每项 0/1 打分、等权平均,不反映不同缺陷的严重程度差异。
- 审查对象集中在编码、网页、网络安全、通用助手类基准;**没有科学/生物医学分析类基准**,也没有讨论多次运行之间的随机性(rerun variance)。
- 清单本身由作者经验与文献综合而来,作者并未证明其完备;部分检查项(如 LLM judge 的「抗对抗」)给出原则多于具体协议。
- 量化结果依赖作者自行设计的验证实验,不同基准之间的数值不可直接比较。

## 与本研究方向的关系
这是 **Agent 可信度课题的「评测宪法」**,也直接约束 **伪影注入课题的 KidneyAnomalyBench**。对 Agent 可信度课题(可信生物医学 agent、claim-to-evidence 验证、校准 verifier、rerun 稳定性、组学专属失败分类、AIRIS WP3 / MLCommons):(1) **outcome validity 正是 claim verification 要解决的问题** —— agent 说「PT 细胞亚群 X 在 DKD 中上调」,评测判它对,不等于真的对;ABC 的 O.c.1(LLM judge 必须有准确率、自洽性、与人类一致性的证据)就是我们 calibrated verifier 必须交付的东西;(2) **trivial agent 基线(R.13)** 应该成为组学 agent 基准的标配:例如「只返回 marker 基因表」「只复述 Lake atlas 已有结论」的 agent 能拿几分?拿得多就说明任务没测到分析能力;(3) T.5(与 ground truth 隔离)对组学尤其要紧 —— agent 能联网就可能直接搜到 KPMP / Lake 论文里的结论(HAL 论文就观察到 agent 去 HuggingFace 搜答案);(4) T.6(环境不随时间变)对应数据库/注释版本锁定(Ensembl、CellxGene 版本)。另外 MLCommons 的 Rebecca Weiss 与 Fazl Barez 是共同作者,这份清单与 AILuminate 同一机构背景,是 AIRIS WP3 对接 MLCommons 时最自然的方法论接口。对伪影注入课题:KidneyAnomalyBench 也是「基准」—— 需要 T.7(专家核验的 ground truth)、T.8/T.9(每类异常确实可检出、给出 oracle,例如已知 doublet/ambient RNA 注入)、R.12/R.13(报告「全判正常」与「仅用 QC 指标」两种 trivial 基线,以及病理专家基线)、R.10(置信区间)。detect → model → revert 主链上,任何「检出异常」「提名回复靶点」的评测都要先过这张清单,否则数字不可信。

## 可复用资产
- **代码:** 审查实验与清单代码。
<https://github.com/uiuc-kang-lab/agentic-benchmarks>
- **网站:** 持续更新的 ABC 清单与审查结果。
<https://uiuc-kang-lab.github.io/agentic-benchmarks/>
- **清单本身:** T.1–T.10、O.a–O.i、R.1–R.13 可直接改写成 KidneyAnomalyBench 与组学 agent 基准的设计评审表。

## 待读
- 附录 D/E:10 个基准逐项打分与验证实验细节;附录 F:以 BIRD 为例的高质量报告。
- 用 ABC 审查本仓库将收录的生物医学 agent 基准(BixBench、scBench、LAB-Bench、BioML-bench 等)。
- Holistic Agent Leaderboard(同一批作者)如何把这些原则落到 harness 与日志分析里。

## 引用
```bibtex
@inproceedings{Zhu2025_250702825,
  title = {Establishing Best Practices for Building Rigorous Agentic Benchmarks},
  author = {Yuxuan Zhu and Tengjun Jin and Yada Pruksachatkun and Andy Zhang and Shu Liu and Sasha Cui and Sayash Kapoor and Shayne Longpre and Kevin Meng and Rebecca Weiss and Fazl Barez and Rahul Gupta and Jwala Dhamala and Jacob Merizian and Mario Giulianelli and Harry Coppock and Cozmin Ududec and Jasjeet Sekhon and Jacob Steinhardt and Antony Kellermann and Sarah Schwettmann and Matei Zaharia and Ion Stoica and Percy Liang and Daniel Kang},
  booktitle = {NeurIPS 2025 Datasets and Benchmarks Track},
  year = {2025},
  eprint = {2507.02825},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2507.02825}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
