# A deep learning algorithm to predict risk of pancreatic cancer from disease trajectories

> **文献键** `Placido_2023` · **来源** Nature Medicine(2023) · **类别** ehr · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41591-023-02332-5> · `status: complete`

---

## 一句话
CancerRiskNet:只用**带时间戳的 ICD 诊断码序列**(disease trajectory),在丹麦全国患者登记(620 万人,23,985 例胰腺癌)上训练 Transformer,预测 3/6/12/36/60 个月内发生胰腺癌的风险;36 个月 AUROC 0.879,排除确诊前 3 个月数据后仍有 0.83;直接迁移到美国退伍军人系统(US-VA)跌到 0.71,本地重训后回到 0.78 —— 明确证明「时间顺序」有信息量,也明确证明「跨医疗系统不能直接搬模型」。

## 研究问题
胰腺癌发病率低但极其凶险,约 80% 确诊时已是局部晚期或远处转移(5 年生存 2–9%),而早期病例可以通过手术+化疗治愈。人群级筛查因发病率低、检查昂贵、假阳性多而不现实;现有监测只覆盖有家族史/胚系突变/胰腺囊肿的少数人。问题是:能否从**常规临床记录中的疾病轨迹**里识别出一小撮高风险人群(例如 100 万人里的前 1,000 名),让昂贵的影像监测变得可负担?此前基于 EHR 的胰腺癌模型只用「是否出现过某诊断码」,不用**时间顺序**;丹麦登记数据的轨迹研究也停留在描述性层面。

## 方法
**输入**:每个病人的 ICD 三位码序列(DNPR 中 ICD-8 与 ICD-10 不做语义映射直接共用,共约 2,000 个 level-3 码)+ 每个诊断的时间戳 + 年龄。**数据增强**:对每个病人取所有「从病史起点开始、长度 ≥5 个诊断、终点不同」的连续子轨迹,终点即「评估时刻」;癌症病人只用确诊前结束的轨迹;非癌症病人只用在其记录结束前 ≥2 年结束的轨迹(避免未确诊癌症混入对照)。训练时按正负样本**平衡采样**。**模型**:三段式 —— embedding(诊断码 → 低维向量,与模型联合训练)→ encoding(GRU 或 Transformer,把轨迹压成一个 "fingerprint" 向量;Transformer 用基于**诊断时年龄与诊断间隔**的余弦 positional embedding,128 个频率)→ prediction(前馈网络输出 3/6/12/36/60 个月五个时间窗的风险)。**损失**:对五个时间点的阶跃函数标签求交叉熵之和 + L2 正则。对照方法:bag-of-words(忽略时间顺序)、MLP、GRU。**数据排除实验**:训练时去掉确诊前 3/6/12 个月内的诊断,检验模型是否只是在「读症状」。**可解释性**:Integrated Gradients(Captum),按距确诊 0–6/6–12/12–24/24–36 个月分层统计各诊断码贡献。**评估**:AUROC + 在「100 万人中前 n 名高风险」操作点上的相对风险 RR(N1000 即前 0.1%)。80/10/10 按病人划分,超参搜索用 AUPRC 选模型,200 次 bootstrap 给 95% CI。

## 数据
**丹麦 DNPR**:1977–2018 年 860 万人、2.29 亿条住院诊断(1977 起住院,1995 起门诊与急诊;不含全科医生记录);经人口连续性过滤(排除格陵兰居民、无稳定住址等)、去掉 temporary/referral 码(8.3%)、去掉 <5 个诊断的病人后,训练用 **620 万人、23,985 例胰腺癌**(ICD-10 C25 / ICD-8 157)。与丹麦癌症登记(DCR)交叉核对,88% 病例重合(作为标签准确度下限)。**US-VA CDW**:1999–2020 年,从 1,590 万人中随机抽 ~300 万,病例定义为「VA 癌症登记 ∩ EHR ICD 码」两者都有(EHR 中有胰腺癌码的人仅 32.4% 在登记中,说明 EHR 码噪声很大),最终 **1,948,209 人、3,418 例**(摘要写约 300 万人 / 3,900 例,指过滤前)。两系统差异显著:VA 轨迹更短(中位 12 年 vs 23 年)但更密(中位 188 条 vs 22 条记录/人)。

## 主要结果
- **时间顺序有用**:36 个月窗口,Transformer AUROC **0.879**(0.877–0.880),GRU 0.852,MLP 0.845,bag-of-words 0.807;N1000 处 RR:Transformer **104.7**,MLP 26.6,bag-of-words 2.1。
- **排除临近确诊数据**:训练时排除最后 3/6/12 个月,AUROC 降至 0.843/0.829/0.827 —— 下降但远非崩溃,说明模型不只是在读黄疸、腹痛等晚期症状。
- **全部诊断码 > 已知危险因素**:只用 23 个已知危险因素对应的码,AUROC 0.838 vs 全部 ~2,000 码的 0.879。
- **时间窗越远越难**:12 个月窗口 AUROC 0.908,36 个月 0.879;F1 操作点召回率从距确诊约 1 年的 8% 降到约 3 年的 4%。
- **跨系统迁移**:丹麦模型只做 ICD 映射直接用于 US-VA,AUROC 0.710(RR 57.4);在 VA 上从头训练,AUROC **0.775**(RR 80.4)。结论:医疗系统差异大时需要本地独立训练。
- **现实监测方案**:>50 岁、排除 3 个月数据、12 个月窗口、前 0.1% 高风险,RR = 58.7(DNPR,GRU)/ 33.1(US-VA,Transformer)。100 万人取前 1,000 人(不排除数据)PPV 0.32,约 320 人会发病;保守估计(排除 3 个月,PPV 0.07)约 70 人是此前未被识别的新增高危。
- **特征**:确诊前 0–6 个月主要是黄疸、胆道疾病、腹痛、体重下降、消化器官肿瘤;更早的轨迹中 2 型糖尿病、胆石症、反流病贡献上升。两系统特征部分重叠;剔除慢性胰腺炎患者后 RR 几乎不变。

## 创新点
- 把**疾病轨迹的时间序列**(而不仅是码的出现与否)作为 Transformer 输入,并用年龄 + 间隔做连续时间 positional embedding。
- **多时间窗风险输出**(3–60 个月),直接对接「多早能发现」的临床问题。
- **数据排除协议**:系统地去掉确诊前 3/6/12 个月数据,区分「早期信号」与「症状泄漏」—— 这是此后同类工作(包括 npj 2025 的 LLM-embedding 论文)沿用的评估规范。
- **以 RR@前 0.1% 作为临床操作点**,把模型性能翻译成可负担的监测方案规模。
- 在两个差异很大的国家级系统上做**跨系统迁移 vs 本地重训**的直接对比。

## 局限
- 只用诊断码:没有用药、化验、临床文本、影像(作者明确把这些列为未来提升来源)。
- 跨系统泛化差(0.879 → 0.710),需本地重训;联邦学习只是被提议,未实施。
- 丹麦数据无全科医生记录;VA 是退伍军人人群(男性为主),人群代表性有限。
- 标签依赖登记/编码质量(DNPR 与癌症登记仅 88% 重合;VA EHR 码 PPV 低)。
- 回顾性;成本-收益只在补充材料中做了估算,没有前瞻性验证;IG 特征是相关性而非因果。
- 多时间窗共享表示可能让近端强特征「泄漏」到远端窗口(npj 2025 论文指出本文 0–6 个月与 24–36 个月 top-10 特征有一半以上重叠)。

## 与本研究方向的关系
**对 Mount Sinai EHR(数百万病人)项目,这是 PI 指定的起点模板**,原因很直接:它定义了「用疾病轨迹做早期风险预测」的完整、可复现的最小方案 —— 只要 ICD 码 + 时间戳就能跑,而这正是 Sinai 数据里最干净、最先能拿到的部分。可以直接照搬的是 **评估协议** 而不只是模型:(1) 从每个病人截取多个评估时刻的子轨迹;(2) 对照组在记录结束前 2 年截断;(3) **排除确诊前 3/6/12 个月** 检验症状泄漏;(4) 报告 RR@前 0.1% 这种能对接临床资源的操作点;(5) 跨系统迁移 vs 本地重训。Sinai 是美国城市学术医疗中心,其编码密度与就诊模式更接近 US-VA 而非丹麦登记,所以本文「跨系统 AUROC 跌到 0.71、本地重训回到 0.78」的结论直接提示:**应在 Sinai 上本地训练,并把公开模型的直接迁移当作基线**。**与心-代谢-肾(cardiometabolic-kidney)方向的连接**:本文把 2 型糖尿病识别为远期胰腺癌风险因子,而轨迹模型这一套(多时间窗、数据排除、IG 分层归因)可以原样换成 CKD 进展、DKD、心衰、透析等终点 —— 这是实验室 Novo 资助的 cardiometabolic-kidney 智能体/基础模型最自然的 EHR 端任务。与本方向 detect → model → revert 的关系:轨迹模型是**病人尺度的 "detect"**(在临床表现前发现偏离正常轨迹的人),它给出「谁、何时」;组织尺度的 virtual tissue 与 revert 需要回答「为什么、改什么」—— 而本文作者也明确说 IG 特征不是因果,这正是两者之间需要接口的地方(例如从 EHR 高风险人群中挑选有活检/组学数据的人,做 Plan A 式的组织异常检测)。对 Plan B(可信 agent):本文的 data-exclusion 与跨系统检验,是 agent 生成 EHR 风险结论时应被强制执行的「反泄漏」核查项。

## 可复用资产
- **代码:** CancerRiskNet(PyTorch 1.9、Captum 0.3.1 做 IG)。
<https://github.com/BrunakSanderLabs/CancerRiskNet>
- **数据:** DNPR 需向丹麦卫生数据局申请(3–6 个月);US-VA 需经 VINCI 审批(≥6 个月)。不公开。
- **评估协议:** 多评估时刻子轨迹增强、对照 2 年截断、3/6/12 个月数据排除、RR@N1000、MI-CLAIM 报告清单(补充表 6)。

## 待读
- 补充材料中的成本估算(Supplementary Notes)与全部模型比较表(Supplementary Table 3)。
- 同组 Delphi-2M(Nature 2025,Brunak 共同作者)把单病种扩展到 >1,000 种疾病的生成式轨迹模型 —— 见本仓库 `ehr-delphi2m-nature-2025`。
- 引用中 ref 23(急性肾损伤进展预测)—— 与肾病终点直接相关,值得补读。
- 把同一协议换到 CKD/DKD 终点的已有工作(待检索)。

## 引用
```bibtex
@article{Placido_2023, title={A deep learning algorithm to predict risk of pancreatic cancer from disease trajectories}, volume={29}, ISSN={1546-170X}, url={http://dx.doi.org/10.1038/s41591-023-02332-5}, DOI={10.1038/s41591-023-02332-5}, number={5}, journal={Nature Medicine}, publisher={Springer Science and Business Media LLC}, author={Placido, Davide and Yuan, Bo and Hjaltelin, Jessica X. and Zheng, Chunlei and Haue, Amalie D. and Chmura, Piotr J. and Yuan, Chen and Kim, Jihye and Umeton, Renato and Antell, Gregory and Chowdhury, Alexander and Franz, Alexandra and Brais, Lauren and Andrews, Elizabeth and Marks, Debora S. and Regev, Aviv and Ayandeh, Siamack and Brophy, Mary T. and Do, Nhan V. and Kraft, Peter and Wolpin, Brian M. and Rosenthal, Michael H. and Fillmore, Nathanael R. and Brunak, Søren and Sander, Chris}, year={2023}, month=May, pages={1113–1122} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
