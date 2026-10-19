# Unbiased self supervised learning of kidney histology reveals phenotypic and prognostic insights

> **文献键** `Pandit_2025` · **来源** Scientific Reports(2025) · **类别** histopath · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s41598-025-19193-2> · `status: complete`

---

## 一句话
NYU(Tsirigos 组)与 JHU/UPenn 把原本为肺癌 H&E 开发的自监督框架 Histomorphological Phenotype Learning(HPL)用到 1,421 张 PAS 染色肾脏 WSI 上:不用任何病理标注,把 tile 嵌入聚成「组织形态表型簇」(HPC),每张切片表示为各 HPC 的面积占比向量;这些簇跨 5 个内外部队列视觉一致、与间质纤维化等病理定量相关(MIL 预测纤维化 AUC 0.83),并能预测 TRIDENT 糖尿病肾病队列的肾功能下降。

## 研究问题
计算病理多依赖监督学习,标注昂贵且主观(例:肺癌分类需 39 位病理医生在 4,704 张 WSI 上勾画),而肾脏病理医生尤其稀缺,许多机构一个驻院肾病理医生都没有。问题是:能否在**与疾病亚型无关**的前提下,不用专家标签,得到可复现的肾组织模式,并让这些模式复现病理医生的切片级评估、关联临床结局与基因型?

## 方法
**预处理**:DeepPATH 切 224×224 非重叠 tile,去掉背景 >50% 的 tile,Reinhard 染色归一化;在 5×、10×、20× 三个倍率分别建模。**自监督**:Barlow Twins(ResNet 层 + 一个 self-attention 层),同一 tile 两种增强视图,使交叉相关矩阵逼近单位阵,输出 128 维嵌入;按验证 loss 停在 epoch 30。**两轮 Leiden 聚类**:第一轮高分辨率,人工识别并剔除伪影簇(模糊、边缘、非组织),这些标签也用于在外部集上去除伪影 tile;第二轮对剩余组织 tile 聚类,用 disruption score(簇内到质心距离)在验证集上取 elbow 定簇数,得到 5×/10×/20× 分别 77/100/99 个 HPC。**切片表示**:每个元素 = 某 HPC 占组织面积的百分比。**下游**:与病理定量做 Spearman 相关(Bonferroni);以 HPC 组成为特征训练 CLAM(MIL)预测间质纤维化 >5%;Kaplan–Meier 与 Cox 模型(LASSO 选出 4 个 HPC)预测 ESKD/eGFR 下降 ≥40%;患者层面按欧氏距离层次聚类为 5 组,比较临床变量与 3 个 SNP(UMOD rs12917707、SLC34A1 rs6420094、SLC7A9 rs12460876)。另与 ImageNet ResNet-50 和 UNI 嵌入做对比。

## 数据
共 1,421 张 PAS WSI、21 个队列。**开发集**:UPenn 739 例肾切除楔形活检的非肿瘤组织,按糖尿病史与 eGFR 分层均分为训练 247 / 验证 246 / 测试 246(平均 61 岁,eGFR 67,35.2% 糖尿病)。**一年后获得的外部集**:独立测试集 262 张(UPenn 组织、NYU 扫描,不同扫描仪);DDKT 已故供肾移植前穿刺 181 张(106 名供者,其中 75 对左右肾);TRIDENT 糖尿病肾病临床穿刺 239 张(19 家机构,含纵向随访)。tile 数量:5× 425,807、10× 1,670,210、20× 6,748,666。

## 主要结果
- **跨队列一致**:tile-set 匹配测试(21 人参与),专家平均正确率 94.2%(SD 11.7%),非专家 90.0%(SD 13.1%);DDKT 中同一供者左右肾的切片向量距离显著小于不同供者(p = 4.5e-23)。
- **复现病理定量**:与间质纤维化相关的 HPC 在验证、测试、独立测试与 TRIDENT 中保持相关,高亮区域与病理医生勾画的纤维化区一致;CLAM 预测纤维化 >5% 的 AUC 在测试集 0.79、独立测试集 0.83。HPL 簇与纤维化的关联显著强于 ResNet-50 与 UNI 嵌入的簇;UNI 簇在 TRIDENT 同一组织的 PAS 与 H&E 切片上呈现**染色特异与患者特异的批次效应**。
- **预后**:TRIDENT 中 HPC 49(盲评病理医生注释为 IFTA 背景下的球性硬化)高三分位者肾功能下降更多,HPC 53(形态正常的近端小管)高三分位者更少。Cox 模型:临床基线(年龄、性别、ACR、eGFR;N = 182)c-statistic 0.82 → 加 4 个 HPC 后 0.84;组织学基线(纤维化、RPS 评分、上皮增生;N = 177)0.76 → 0.80。
- **患者分组**:5 个患者组中,第 4 组(标志簇为髓质形态的 HPC 8)eGFR 显著更低(p = 2.0e-10)、尿蛋白更高(p = 0.008);第 0 组 1 型糖尿病比例更高(p = 0.006);第 1 组 SLC34A1 rs6420094 等位基因频率不同。

## 创新点
- 把 HPL 从肺癌 H&E 迁移到异质性极高的 PAS 肾组织,并在 21 个队列、不同扫描仪与活检类型(楔形→穿刺)上外部验证。
- 用「切片 = HPC 组成向量」这种可解释表示,同时打通病理定量、预后(Cox)与基因型关联三条下游。
- 显式的「伪影簇」识别与剔除步骤,以及跨队列一致性的人类匹配测试,是无监督表型可信度的两种实用检验。

## 局限
- 训练集来自肾切除楔形活检(多为常见的糖尿病/高血压改变),不含穿刺活检与罕见病因,也不含移植受者,覆盖不了真实肾病谱。
- 仅 PAS 染色;倍率与簇数的取舍(可解释性 vs 覆盖度)未充分探索;HPC 解释依赖病理医生事后看图。
- 预后提升幅度不大(c-statistic +0.02 / +0.04),且基于同一 TRIDENT 队列做选择与评估,未见独立外部验证;SNP 分析样本小(N = 183)且只有 3 个位点。
- 数据不公开(需向通讯作者申请)。

## 与本研究方向的关系
这篇不是 anomaly detection,但它是 Plan A 在**组织学侧的「正常/表型图谱」先例**:不用标注、在大规模肾组织上学出可复现的形态簇,并证明这些簇对应真实病理(纤维化、硬化)。对 detect → model → revert 有三点用处:**(1) 参考分布的构造**——「HPC 组成向量」本身就是一种组织状态的低维表示,若用健康/参考肾组织拟合其分布,偏离即可作为切片或区域级 anomaly score,这是一条简单、可解释的 baseline;**(2) 伪影 vs 疾病**——作者靠人工识别伪影簇来剔除模糊、边缘等 tile,这恰好是 Plan A 想自动化的步骤:我们的假设是用 H&E 与 Xenium/snRNA 的**跨模态一致性**区分伪影与病变,而本文「人工挑伪影簇」可作为对照;**(3) foundation model 的批次效应**——UNI 簇在同一组织的 PAS 与 H&E 上出现染色与患者特异的批次效应,提醒我们直接用通用病理 FM 的嵌入做异常分数,很可能把染色/批次差异误报为异常,KidneyAnomalyBench 需要专门的「同组织不同染色/批次」对照集。TRIDENT 是糖尿病肾病队列,与 DKD 空间图谱(`dkd-spatial-atlas-nature-2026`)和我们院内活检同属 CKD 范畴,其 IFTA/硬化相关簇可作为「已知异常」的弱标签。对 Plan B 的关联较弱,唯一的点是:这种 HPC → 临床结局的关联正是 agent 分析肾脏数据时常见的「统计显著但效应小」的结论类型,适合作为 claim 校验的案例。

## 可复用资产
- **代码:** HPL 流程(Barlow Twins + Leiden + 切片组成向量)。
<https://github.com/AdalbertoCq/Histomorphological-Phenotype-Learning>
- **HPC 代表 tile 浏览:** 所有倍率与队列的代表性 tile。
<https://genome.med.nyu.edu/public/pmedlab/SSL_kidney/representative_tiles>
- **评估设计:** tile-set 匹配测试(跨队列一致性)、左右肾配对距离检验、HPC → Cox 增量 c-statistic,可借用于评估无监督肾组织表示。
- **数据:** 不公开,需向通讯作者申请。

## 待读
- HPL 原文(Quiros et al.,肺癌 H&E)。
- 用 UNI2-h(`uni2-h-model`)替换 Barlow Twins backbone 并做染色批次校正后,重复「纤维化关联强度」对比。
- KPMP 是否有可公开的 PAS WSI 能复现这套 HPC 图谱,作为 Plan A 的外部参考。

## 引用
```bibtex
@article{Pandit_2025, title={Unbiased self supervised learning of kidney histology reveals phenotypic and prognostic insights}, volume={15}, ISSN={2045-2322}, url={http://dx.doi.org/10.1038/s41598-025-19193-2}, DOI={10.1038/s41598-025-19193-2}, number={1}, journal={Scientific Reports}, publisher={Springer Science and Business Media LLC}, author={Pandit, Krutika and Coudray, Nicolas and Quiros, Adalberto Claudio and Surapaneni, Aditya and Upadhyay, Dhairya and Vanguri, Rami Sesha and Hirohama, Daigoro and Mohandes, Samer and Schlosser, Pascal and Thiessen-Philbrook, Heather and Wen, Yumeng and Parikh, Chirag R. and Rhee, Eugene P. and Waikar, Sushrut S. and Schmidt, Insa and Rosenberg, Avi Z. and Palmer, Matthew B. and Susztak, Katalin and Grams, Morgan E. and Tsirigos, Aristotelis and {TRIDENT Study Investigators}}, year={2025}, month=Oct }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
