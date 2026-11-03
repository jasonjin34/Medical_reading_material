# EXSCALATE: An extreme-scale in-silico virtual screening platform to evaluate 1 trillion compounds in 60 hours on 81 PFLOPS supercomputers

> **文献键** `Gadioli2021_211011644` · **来源** arXiv preprint(2021) · **类别** drug-discovery · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2110.11644> · `status: complete`

---

## 一句话
这是一篇**软件工程 / HPC 系统**论文:作者把 Dompé 的 Exscalate 对接平台重写为「每节点一个 MPI 进程 + 节点内 reader→splitter→docker→writer 异步流水线 + CUDA/C++ 异构 worker」,并在外面套一层工作流(用决策树预测每个配体的对接耗时 → 按耗时分桶 → ~3400 个独立 SLURM 作业,每个约 5 分钟),从而在 CINECA-Marconi100 + ENI-HPC5(合计 81 PFLOPS)上于 **60 小时**内把 **700 亿**个小分子对接到 SARS-CoV-2 **12 个病毒蛋白的 15 个结合位点**上,合计约 **1 万亿次**打分,双机吞吐 **5M ligands/s**(单节点约 2.2k ligands/s)。

## 研究问题
在「urgent computing」(疫情期间要尽快找到候选药物)的场景下,虚拟筛选的瓶颈不是化学而是工程:分子可以用已知化学反应在计算机里生成,所以化学库大小只受算力限制;而 TOP500 前五的机器里有四台是 GPU 异构节点,要吃满算力就必须解决一串系统问题——怎么高效用加速器、怎么把数据从存储搬到节点再喂给 GPU、怎么减少节点间通信与进程同步、怎么在节点故障时不丢掉已完成的计算。作者的目标函数很直接:**在给定时间预算内筛完尽可能多的配体**。

## 方法
**(1) 打分算法(四步)**:① 配体预处理——旋转可转键把分子「摊平」,最大化所有原子间内部距离之和(与蛋白无关,可一次性预计算并跨 campaign 复用);② 用**带多次重启的贪心优化**把配体放进结合位点,驱动搜索的打分函数**只考虑几何位阻**,配体柔性被建模、口袋当刚体,实验中每个配体评估 **256 个初始位姿**;③ 以 **RMSD 3 Å** 为阈值对生成位姿聚类,每簇最高分者排前、其余按几何分排序;④ 用 **LiGen 化学打分函数**对**前 30 个位姿**重打分,配体得分 = 最佳位姿得分。复杂度 O(n·m)(n 原子数、m 可转键数);有 C++17(CPU)、OpenACC 与 CUDA 三套实现,NVIDIA GPU 上 CUDA 最快。实测最快与最慢配体类别之间**耗时相差一个数量级以上**;GPU 版耗时对原子数不敏感(硬件并行),但对可转键数敏感(必须串行处理以保持分子几何),且因为按 32 原子为一束组织计算,在 64、96 原子处有阶跃。
**(2) 高吞吐对接应用**:单体式(monolithic)MPI 应用,**每节点一个进程**,进程内用 C++11 线程开一条异步流水线,每 stage 一个专用线程 + 线程安全队列:**reader**(顺序读化学库文件块)→ **splitter**(把块切成单个配体描述)→ **docker**(构建数据结构、对接打分)→ **writer**(把 SMILES + 分数以 CSV 形式攒满缓冲区后批量写出)。只有 docker stage 可以有多个线程并在同一队列上**工作窃取**,且可以混用 CUDA worker 与 CPP worker 来吃节点异构性;一个 GPU 可绑多个 CUDA worker(round-robin)。口袋信息在启动时读一次常驻(C++ 用常量静态内存,CUDA 用 texture memory)。输入文件按**文件大小与进程数静态均分**成 slab(约定:描述起点落在本 slab 内的配体归本进程,最后一个配体的描述可以越界),读是顺序的、对 I/O 友好,但静态划分**消除了 MPI 进程间的工作窃取**,于是应用吞吐 = 最慢进程的吞吐。writer 用 **collective I/O** 合并写请求,发起 I/O 的进程数可配置以降低文件系统压力。软件栈:libdpipe(封装 MPI 与 C++ 线程的高层接口)+ LiGenDock/LiGenScore(领域逻辑)+ MPI/CUDA。**不依赖节点本地存储**(目标机器上没有)——这是与 AutoDock-GPU/Summit 路线的关键区别。
**(3) Exscalate 工作流(补偿应用的弱点)**:把一个覆盖全机的巨型 MPI 作业拆成**一批可并行的小作业**(SLURM/PBS job array),解决两件事——**容错**(MPI 通信域默认在节点故障时终止所有进程,会丢掉大量算力;拆小后只需重跑小作业)与**负载均衡**(大而复杂的配体若聚在一起会严重拖慢对应进程)。流程:SMILES 化学库 → 用**决策树(最大深度 16)**按 SMILES 层面可直接得到的特征(重原子数、环数、链数及其交互项)预测对接耗时 → 按 **10 ms** 为宽度分桶 → 配体预处理(加氢、生成 3D 初始坐标、摊平;一次性、可跨 campaign 复用)→ 生成自定义二进制配体文件 → **一次一个口袋**地在所有配体文件上跑对接应用 → 每个位点一份配体排名。领域专家挑出对多个位点/蛋白都强结合的分子后,因**对接算法是确定性的**,可**按需重算 3D 位姿**,所以只需存 SMILES + 最佳分数。工作流需要两类领域输入:靶蛋白的结合位点(怎么得到被明确划在本文范围之外)和待评估的化学库。

## 数据
**靶点**:SARS-CoV-2 蛋白质组主要功能单元中的 12 个蛋白、15 个结合位点,晶体结构取自 PDB(3CL protease/NSP5 = 6LU7、N-protein = 6VYO、NSP3 = 6W02、NSP9 = 6W4B、NSP12 = 7BV2、NSP13 = 6XEZ、NSP15 = 6W01、NSP16 = 6W4H、PL protease = 6W9C、Spike-ACE2 = 6M0J);**NSP6 用 de novo 模型、NSP14 用同源模型**(无晶体结构时生成同源模型)。口袋信息总共只占 29MB,启动时读一次。
**化学库**:700 亿配体。SMILES 格式共 **3.3TB**;对接应用需要更丰富的描述,作者用自定义二进制格式(只存原子坐标、类型、键)代替 TRIPOS Mol2(ASCII、可读性优先),**Mol2 要多占 5–6 倍空间**,二进制全库 **59TB**。若把所有对接位姿都存下来(15 个位点 × 每配体 30 个重打分位姿)需要 **26PB**,因此只存 SMILES + 最佳分数,最终输出 **7.3TB**(结论段写作 64TB,与 §4.1 的 7.3TB 不一致,原文未解释)。**调参用的小数据集**:MEDIATE 网站公开的 "Commercial Compound MW<330",500 万个小分子。**耗时预测模型的数据**:2100 万配体的实测对接时间,80% 训练 / 20% 测试。
**机器**:Marconi100 节点 = 32 核 IBM POWER9 AC922(128 硬件线程)+ 4× NVIDIA V100 + NVLINK 2.0;HPC5 节点 = Intel Xeon Gold 6252 24C(24 核 / 48 硬件线程)+ 4× V100,NVLINK 只用于 GPU 互连;InfiniBand 网络。注:§4 开头把库规模写成「70 million ligands」,与摘要/结论的 700 亿矛盾,应为笔误。

## 主要结果
- **规模**:60 小时、两机合计 81 PFLOPS、700 亿配体 × 15 个结合位点 ≈ 1 万亿次对接打分,作者称这是当时**最大的一次虚拟筛选 campaign**。
- **吞吐**:单节点平均 **2.2k ligands/s**,双机合计 **5M ligands/s**。逐位点(表 2):Marconi100 上每节点 2427–2499 ligands/s(如 PLPRO 2496、3CL 2427),整机约 1.94–2.00M ligands/s;HPC5 上每节点 1965–2010,整机约 2.95–3.02M ligands/s;NSP13ortho 在两台机器上各算了一部分(每节点 2454/1987)。机器吞吐是用「跑完整库的墙上时间 ÷ 配体数」算的,**包含所有执行开销**。
- **异构 worker 扫描(Marconi100 单节点,图 7)**:吞吐在 **CUDA worker 数较多**时达到峰值(约 2.4k ligands/s),而**把 CPP worker 数加到匹配硬件线程数反而伤性能**(128 CPP worker 时掉到 664–985 ligands/s)。结论:在本案例里**CPU 最好用来支撑加速器与 I/O,而不是参与计算本身**;另外单个 CUDA worker 吃不满一块 GPU(worker 要先解析配体描述、初始化数据结构才能发 kernel),多 worker 才能把这些开销隐藏掉。
- **耗时预测模型**:决策树在 2100 万配体上的**平均误差可忽略(−0.00088 ms)、标准差 3.81 ms**;因为单配体预测仍有误差,工作流按 10 ms 分桶来吸收波动——负载均衡只需要平均行为对。
- **作业划分**:输入被切成 **~3400 个作业**,每个 32 个 MPI 进程、约 5 分钟、只针对一个结合位点;位点被**顺序**评估。全机运行时测到的单节点吞吐与扫描调参时基本一致,说明平台确实把可用资源都用上了。
- **产出公开**:每个靶点筛出的最有希望的化合物集合发布在 MEDIATE 门户,供全球研究者在缩小后的集合上开展更细致的 de novo campaign。

## 创新点
- **用「小作业数组 + 预测驱动的分桶」替代巨型 MPI 作业**:一个同时解容错与负载均衡的朴素但有效的设计——MPI 层面做不到的跨进程工作窃取,被搬到调度器层面用 job array 近似实现。
- **把「对接耗时」本身当成可学习的量**:用 SMILES 层面即可获取的特征(重原子/环/链)训练决策树预测耗时再据此分桶,是 campaign 规划里一个很干净、可直接搬用的 cost model。
- **节点内异步流水线 + 可混搭的 CUDA/CPP worker**:在不用节点本地存储的前提下吃满 GPU 异构节点,并给出「CPU 该当 I/O 与喂数据的仆役」这一实测结论。
- **确定性算法 ⇒ 用「SMILES + 最佳分数」替代位姿存储**:把 26PB 的存储需求压到 7.3TB,位姿按需重算。这是极大规模筛选里关键的「可复算而非可存储」思路。
- **自定义紧凑二进制配体格式**:比 TRIPOS Mol2 省 5–6 倍空间,把全库压到 59TB。

## 局限
- **科学产出完全未评估**:论文明说是从软件工程角度写的,通篇只有吞吐、存储、预测误差,**没有任何 enrichment、命中率、已知活性分子 recovery,也没有体外验证**;「最有希望的化合物」由领域专家在排名之后挑选,挑选标准与结果不在本文。
- **打分函数很粗**:驱动搜索的只是几何位阻分,口袋被当作刚体,只重打分前 30 个位姿——这是为吞吐刻意做的精度妥协,论文没有量化它在精度上的代价(例如与 AutoDock 类方法的对比)。
- **静态数据划分抹掉了跨进程工作窃取**,应用吞吐被最慢进程锁死;分桶只是部分缓解(单配体预测的标准差 3.81 ms 仍在)。
- **一次只跑一个口袋、位点顺序评估**,库被完整扫过 15 遍;没有任何「先筛一部分再决定继续投多少算力」的自适应机制——所有 700 亿配体都被对接了所有 15 个位点。
- **可复现性门槛极高**:需要两台欧洲顶级超算、59TB 输入;Exscalate/LiGenDock/LiGenScore 是 Dompé 的专有栈,论文未给代码链接。
- **数字内部不一致**:输出规模 7.3TB(§4.1)vs 64TB(结论);库规模在 §4 开头写成 70 million。引用时应以摘要/结论的 700 亿与 §4.1 的逐项推算为准,并注明此不一致。

## 与本研究方向的关系
对 Hayat lab(Uniklinik Aachen)的「**Autonomous scientific orchestration of virtual screening**」课题(LLM agent + 分子基础模型 + docking + active learning,给定蛋白结构自动规划/执行/改进筛选 campaign、找出合适化合物),这篇是**被编排的那一层的上限参考**,同时也是「为什么需要 agent」的最好反面教材。
- **它是穷举 baseline,我们要做的是自适应替代品。** EXSCALATE 把 700 亿 × 15 个位点全算了一遍,靠的是 81 PFLOPS;active-learning 式筛选的全部价值就在于用极小一部分算力拿到相近的 top-k。所以它给我们一个干净的**对照轴**:在同一个库/靶点上,「全量 docking 的 top-k」是 agent 流水线的 ground truth,而**compute-to-recall 曲线**(花多少次 docking 调用、恢复多少 top-k)就是评价指标。
- **耗时预测模型可以直接搬进 agent 的 planner。** 一个会规划的 agent 必须能回答「这批 1e6 个分子在这个口袋上要花多久、够不够预算」。本文的决策树(重原子数/环数/链数 → 对接毫秒数,平均误差 ≈0、σ=3.81 ms)就是这个 **cost model** 的现成形态,而且只需要 SMILES、不需要先做 3D 预处理——正适合 planner 在决定是否展开某个批次之前调用。按预测耗时分桶、以及「用 10 ms 粒度吸收预测误差」这个技巧,对我们做批次调度同样适用。
- **把 docking 当作可编排的工具,需要的正是这里的工程契约。** 一次一个口袋的作业粒度(~5 分钟 × 32 进程)天然就是 agent 可以发起、取消、重试的**动作单元**;确定性算法 +「只存 SMILES+分数、位姿按需重算」给 agent 一个极便宜的状态表示(不必在记忆里携带几十 TB 的位姿);小作业数组的容错语义让长程 campaign 中途失败不至于全盘重来。这些都是我们设计 docking 工具接口时该照抄的约定。
- **多位点 / 多蛋白是天然的 agent 决策空间。** 本文为 12 个蛋白准备了 15 个位点,其中 NSP6 用 de novo 模型、NSP14 用同源模型——这正是我们「给定蛋白结构」场景里的真实情况(结构质量不齐)。它顺序、均等地对待所有位点;而 orchestrator 该做的恰恰是**不均等**:按位点的结构置信度(de novo/同源 vs 晶体)与早期命中富集情况,决定继续投多少算力、要不要换位点、要不要先补一次结构预测。「口袋识别」在本文被明确划到范围之外,而在我们的流水线里它应当是 agent 的第一步。
- **它也给出了我们必须回答的问题。** EXSCALATE 完全没报科学指标,所以不能用它来论证「大 = 好」;反过来,如果 agent 流水线要宣称优于穷举,就必须自带它所缺的东西——enrichment/命中率、已知活性 recovery,以及对打分粗糙性(几何位阻 + 刚性口袋)的误差传播分析。与 `competitive-docking-npjdrugdiscov-2026` 对读很有用:后者用 co-folding 模型在十几个体系上量化了排序与实验的一致性(c-index 0.52–0.89),但只能跑几百个配体。两篇正好标出我们流水线里「便宜而粗」与「贵而准」两档打分的两端,而多档打分器之间的**级联决策**(先用谁、何时升级、何时放弃)正是 orchestrator 的核心职责。

## 可复用资产
- **代码:** 论文未给出 Exscalate / LiGenDock / LiGenScore / libdpipe 的公开仓库链接(Dompé 专有栈)。被引用的第三方组件可查:scikit-learn(决策树)、MPI、CUDA、SLURM、OpenPBS。
- **数据:** EXSCALATE4CoV 项目站;MEDIATE 门户(本次 campaign 的知识公开发布处,含每靶点筛出的最有希望化合物集合);调参用的公开数据集 "Commercial Compound MW<330"(500 万分子,来自 MEDIATE);数据下载页。
<https://www.exscalate4cov.eu/>
<https://mediate.exscalate4cov.eu>
<https://mediate.exscalate4cov.eu/data.html>
- **结构:** 表 1 的 PDB 编号可直接用作我们 docking 工具的回归测试靶点:6LU7、6VYO、6W02、6W4B、7BV2、6XEZ、6W01、6W4H、6W9C、6M0J(NSP6、NSP14 无晶体结构)。
- **模型:** 无公开 checkpoint。可借用的是**方法形态**而非权重:SMILES 特征 → 决策树(深度 16)→ 对接耗时,用作 planner 的 cost model。
- **可借用设计:** reader→splitter→docker→writer 异步流水线 + 节点内工作窃取;CUDA/CPP worker 混搭比例的扫描方法;collective I/O + 可配置 I/O 进程数;用 job array 换取容错与均衡;确定性算法下「只存 SMILES+分数、位姿按需重算」;紧凑二进制配体格式(vs Mol2 省 5–6×)。

## 待读
- AutoDock-GPU 在 Summit 上的十亿分子 campaign(LeGrand et al. 2020;Glaser et al., *IJHPCA* 2021),本文最直接的对照工作:它用节点本地 NVMe、FireWorks 编排、RFScore-VS 重打分、BlazingSQL 做统计——**它的编排层比 Exscalate 更接近「可被 agent 驱动的工作流」**,值得按工具接口的角度细读。
- Gervasoni et al., *IJMS* 2020(Pockets 2.0,SARS-CoV-2 可成药空腔的全面测绘):本文把「怎么得到结合位点」划在范围外,而这正是我们流水线的第一步。
- Beato et al. 2013(LiGenDock 打分函数与实验设计优化)与 Vitali et al., *J. Supercomput.* 2019 / PBio 2018(用 OpenACC/OpenMP 加速同一几何对接方法):要判断「几何位阻 + 刚性口袋」这档打分有多粗,得读这两条线。
- Rocco et al., *J. Supercomput.* 2021(Legio:embarrassingly parallel MPI 应用的容错)——若我们的 orchestrator 要直接管 MPI 级别的作业而不只是提交 job array,这是容错语义的参考。
- EXSCALATE4CoV 是否发表过**科学结果**论文(体外/体内验证了哪些化合物)?本文完全没报,这决定了我们能不能把它当作「穷举筛选的科学产出」参照。

## 引用
```bibtex
@misc{Gadioli2021_211011644,
  title = {EXSCALATE: An extreme-scale in-silico virtual screening platform to evaluate 1 trillion compounds in 60 hours on 81 PFLOPS supercomputers},
  author = {Davide Gadioli and Emanuele Vitali and Federico Ficarelli and Chiara Latini and Candida Manelfi and Carmine Talarico and Cristina Silvano and Carlo Cavazzoni and Gianluca Palermo and Andrea Rosario Beccari},
  year = {2021},
  eprint = {2110.11644},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2110.11644}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
