# Accelerating scientific discovery with Co-Scientist

> **文献键** `Gottweis_2026` · **来源** Nature(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41586-026-10644-y> · `status: complete`

---

## 一句话
Google 的 Co-Scientist 是一个基于 Gemini 2.0 的多智能体「结构化科学思考引擎」:Supervisor 在异步任务队列里调度 Generation、Reflection、Ranking、Proximity、Evolution、Meta-review 六类 agent,以「生成–辩论–进化」加 Elo 锦标赛不断扩展 test-time compute 来自我改进假设;在 AML 药物重定位(KIRA6 对 KG-1a 的 IC50 10 nM,较非 AML 对照有 18 倍窗口)、肝纤维化表观靶点(人肝类器官中 2/3 有效)与细菌 cf-PICI 机制(2 天内独立重现未发表发现)三个场景做了湿实验验证。

## 研究问题
科研面临「广度与深度」的两难:课题需要越来越深的专业知识,而突破又常来自跨学科的广博联系,文献爆炸让个人难以两者兼得。已有 LLM 工具多停留在文献总结与 deep research,而本文要回答:能否让 AI 系统**生成真正新颖、可检验的研究假设与实验方案**,并通过扩展推理时计算让假设质量持续提升,最终经得起湿实验检验?

## 方法
**四个组件**:自然语言交互界面(科学家设定目标、约束、反馈,也可提交自己的假设)、异步任务框架(Supervisor 管理队列并分配资源)、专门 agent、持久化 context memory(长程推理与故障重启)。研究目标先被解析为 research plan configuration(偏好、约束、评价标准);默认标准为与目标一致、合理性、新颖性、可检验性、安全性。**六类 agent**:Generation(网页检索文献、模拟专家辩论、迭代识别可检验的中间假设、按 meta-review 反馈扩展搜索方向);Reflection(扮演同行评审——初审不用工具快速淘汰、全审带检索、**deep verification 把假设拆成假设前提与子前提逐条独立验证**、observation review 看能否解释长尾实验观察、simulation review 逐步模拟机制或实验、tournament review 吸收锦标赛中的复发问题);Ranking(Elo 锦标赛,新假设初始 1200 分,头部假设用多轮科学辩论两两比较以减轻顺序偏差,低排名用单轮比较;借助 Proximity 优先比较相似假设);Proximity(构建假设相似图,去重与聚类);Evolution(基于检索补强、改进可行性、组合、简化、发散思考,**只生成新假设不覆盖旧假设**,新假设须重新参赛);Meta-review(汇总所有评审与辩论中的共性问题,作为反馈追加进其他 agent 的提示——无需反向传播的「学习」,并最终生成研究综述)。架构与底座模型无关,本文用 Gemini 2.0。

## 数据
**自动评测**:截至 2025-02-03 输入系统的 203 个研究目标(以生物医学为主,也有数学、物理),按生成时间分 10 个桶看 Elo 变化;其中 15 个由 7 位生物医学专家(博士后或教职)策划的困难目标,与专家「最佳猜测」及 Gemini 2.0 Pro / Flash Thinking、OpenAI o1、o3-mini-high、DeepSeek R1 同场比 Elo;11 个目标做专家盲评。**湿实验**:AML——从 2,300 个已批准药物 × 34 种癌症中检索重定位候选,4 个 AML 细胞系(MOLM-13、KG-1a、HL-60、NOMO-1)+ 非 AML 淋巴母细胞系 TK6;肝纤维化——人肝类器官 + 活细胞成像;AMR——cf-PICI 宿主范围机制。

## 主要结果
- **test-time compute 扩展**:203 个目标上,最佳 Elo 与 top-10 平均 Elo 随计算时间持续上升,未见饱和;15 个困难目标上 Co-Scientist 最终明显超过其他前沿 LLM/推理模型和专家最佳猜测(o3-mini-high、DeepSeek R1 以更少计算取得有竞争力的结果);从专家最佳猜测出发迭代,也能把它改进到超过自生成解的 Elo(初步结论)。
- **专家盲评**(11 个目标):Co-Scientist 平均偏好排名 2.36(1 最好、4 最差),新颖性 3.64/5、影响力 3.09/5,均为最高;4 个 LLM 评委也都最偏好其输出。作者强调这些是主观评估、样本很小。
- **消融**:给 Reflection 接检索工具能有效防止「看似新颖但不合理」的幻觉假设;Ranking 用科学辩论提示显著改善排序并降低位置偏差;Evolution 的迭代改进显著提升质量。
- **AML 重定位(专家参与)**:30 个高排名候选交给肿瘤学家,选出 5 个(binimetinib、pacritinib、cerivastatin、pravastatin、富马酸二甲酯),其中 binimetinib、pacritinib、cerivastatin 抑制活力;binimetinib 在除 NOMO-1 外的 AML 系 IC50 低至 2 nM,在 TK6 中高得多。
- **AML 自主单药(无 DepMap、无专家反馈,要求无既往临床前证据)**:专家从排名中选 3 个(nanvuranlat、KIRA6、leflunomide);IRE1α 抑制剂 KIRA6 在 KG-1a IC50 10 nM、NOMO-1 144 nM、HL-60 870 nM、MOLM-13 1,750 nM,TK6 180 nM——KG-1a 与 TK6 之间约 18 倍;另两个药效果有限。系统自评 KIRA6 新颖性为「中等」(IRE1α 在 AML 已有研究,但该药没有)。
- **联合用药**:7 个组合在 MOLM-13 中多为协同(如 JNJ-64619178 + selinexor;JQ1 + olaparib + MSA2),在 TP53 突变的 KG-1a 中协同与拮抗混杂。
- **肝纤维化**:专家从排名中选 3 个表观修饰靶点及对应药物,其中 2 个在人肝类器官中有显著抗纤维化活性且无细胞毒性;其一 vorinostat 已获 FDA 批准(另一癌症适应症)。**AMR**:仅凭少量背景,系统的最高排名假设是「cf-PICI 与多种噬菌体尾部相互作用以扩大宿主范围」,与同期未发表的实验发现一致,用时 2 天。

## 创新点
- 把 test-time compute 扩展范式系统地用于科学假设生成:异步多 agent + 自我对弈辩论 + Elo 锦标赛 + 进化,质量随计算持续上升。
- Reflection 的多种评审模式,尤其 **deep verification(把假设拆成前提与子前提逐条验证)**,是 claim 分解式验证的一个具体工程实现。
- Meta-review 把评审中的共性问题追加进提示,实现无需微调的跨轮「学习」。
- 三个复杂度递增的生物医学场景都做了端到端湿实验验证,并保持 scientist-in-the-loop。

## 局限
- **评价主要靠 Elo 自评**,Elo 并非客观真值;专家盲评只有 11 个目标、偏好与评分主观;作者明说需要更客观、自动化的评价指标。
- 湿实验验证是初步的:细胞系级别的可行性检查,样本少、由专家挑选候选(选择偏差),不等于体内疗效;作者也指出 binimetinib 在既往 II 期中单药疗效有限。
- 只能访问开放获取文献,缺乏负结果;来源文献质量参差,可能传播错误或不可复现的发现;作者把「能把 claim 追溯到来源中具体图表或数据的 provenance 能力」列为关键未来方向。
- 继承底座模型的幻觉与事实性问题;不能直接对公共数据库与多模态数据做推理和数据分析(列为未来工作)。

## 与本研究方向的关系
在 detect → model → revert 里,Co-Scientist 对应的是 **revert 的「提名」环节**:给定疾病与约束,提出哪些靶点/药物可能把病理表型拉回正常,并由湿实验检验——其肝纤维化案例(在人肝类器官里找抗纤维化的表观靶点)几乎就是「肾间质纤维化逆转靶点」的同构问题。但它只吃文献、不吃数据,所以无法利用我们在 detect/model 阶段得到的异常区域与虚拟组织扰动结果;一条自然的接口是把我们的空间组学异常与扰动预测作为「research goal 的上下文 + Reflection 的 observation review 证据」输入。对 **Agent 可信度课题** 这篇是关键对照:**(1) Elo 自评 ≠ 正确性**——系统用自己的锦标赛评价自己的假设,正是 Agent 可信度课题要用外部、校准过的 verifier 取代的环节;**(2) deep verification 的「前提分解 + 逐条验证」** 与我们的 claim-to-evidence 验证同构,但它验证的对象是文献前提,我们要验证的是「agent 对肾脏组学数据的分析结论」是否被数据与代码支撑;**(3) 作者自陈的 provenance 缺口**(把 claim 追溯到来源中的具体图表/数据)正是 Agent 可信度课题的出发点;**(4) 新颖性自评**(KIRA6「中等新颖」)是一个可检验的校准问题——系统的新颖性/置信度打分是否与专家判断一致,可纳入 calibrated verifier 的评估。另外,所有湿实验候选都经专家挑选,意味着论文报告的「命中率」混入了人类筛选,评估 agent 时要把人机贡献拆开。

## 可复用资产
- **论文与预印本:** Nature 开放全文与 arXiv 2502.18864(早期版本,可对比改动)。抽取到的正文未给出公开代码库链接——不确定是否开源,需查原文 Code availability。
<https://arxiv.org/abs/2502.18864>
- **可借用设计:** Reflection 的六种评审模式(尤其 deep verification)、Elo 锦标赛 + 辩论式两两比较、Evolution「只新增不覆盖」、Meta-review 提示反馈环。
- **评测协议:** 专家策划目标 + 专家最佳猜测同场 Elo + 盲评(新颖性/影响力 5 分制 + 偏好排名)+ LLM 评委交叉。

## 待读
- 同期的 Robin(`robin-nature-2026`)与 Kosmos(`kosmos-arxiv-2025`)——一个加入数据分析闭环、一个用 world model 做长程数据驱动发现,与本文形成「只读文献 → 读文献 + 分析数据」的对照。
- 肝纤维化配套论文(Guan et al.,人肝类器官)与 AMR 配套论文(Penadés 组 cf-PICI),看湿实验细节与人机分工。
- Supplementary Note 10.6/10.7 的 deep verification 示例,作为 claim 分解模板。

## 引用
```bibtex
@article{Gottweis_2026, title={Accelerating scientific discovery with Co-Scientist}, volume={655}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10644-y}, DOI={10.1038/s41586-026-10644-y}, number={8122}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Gottweis, Juraj and Weng, Wei-Hung and Daryin, Alexander and Tu, Tao and Sirkovic, Petar and Myaskovsky, Artiom and Glowaty, Grzegorz and Weissenberger, Felix and Orlandi, Alessio and Popovici, Dan and Palepu, Anil and Rong, Keran and Tanno, Ryutaro and Saab, Khaled and Zhang, Fan and Blum, Jacob and Carroll, Andrew and Kulkarni, Kavita and Tomašev, Nenad and Zverinski, Dina and Rendulic, Ivor and Vedadi, Elahe and Hasler, Florian and Rimanic, Luka and Boia, Marina and Budiselic, Ivan and Feinstein, Ben and Bellaiche, Mathias and Sheffer, Tom and Freyberg, Jan and Ratcliff, Jeremy and Bertolli, Ottavia and Chou, Katherine and Hassidim, Avinatan and Gokturk, Burak and Vahdat, Amin and Guan, Yuan and Dhillon, Vikram and Vaishnav, Eeshit Dhaval and Lee, Byron and Costa, Tiago R. D. and Penadés, José R. and Peltz, Gary and Matias, Yossi and Manyika, James and Hassabis, Demis and Xu, Yunhan and Kohli, Pushmeet and Pawlosky, Annalisa and Karthikesalingam, Alan and Natarajan, Vivek}, year={2026}, month=May, pages={487–496} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
