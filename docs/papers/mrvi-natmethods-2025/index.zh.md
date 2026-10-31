# Deep generative modeling of sample-level heterogeneity in single-cell genomics

> **文献键** `Boyeau_2025` · **来源** Nature Methods(2025) · **类别** single-cell · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s41592-025-02808-x> · `status: complete`

---

## 一句话
MrVI(multi-resolution variational inference,Yosef 组,scvi-tools 内置)是一个两层隐变量的层级深度生成模型:**u** 只编码细胞状态(与样本无关),**z** 在 u 基础上加入样本效应(与 batch 等 nuisance 无关);通过**反事实**——「这个细胞如果来自另一个样本会怎样」——在单细胞分辨率上做样本分层(exploratory)以及不依赖聚类的 DE 与 DA(comparative),在 COVID-19、sci-Plex 药物筛选和克罗恩病队列上发现了只在部分细胞亚群中体现的样本差异。

## 研究问题
几百个样本的单细胞队列研究越来越多,但分析通常先把细胞聚类、再对每个簇的频率或伪 bulk 做比较——这依赖聚类分辨率,会漏掉只出现在部分细胞子集、或跨越多个预定义簇的效应。已有的无聚类 DA/DE(Milo、miloDE 等)不考虑 embedding 的不确定性;用 VAE 建模样本协变量的方法又假设效应对所有细胞相同。

## 方法
协变量分两类:**target covariate**(通常是样本 ID,嵌套了疾病状态、处理等所有样本级属性)和 **nuisance covariate**(处理中心、文库技术、研究来源等)。每个细胞 n 有 uₙ(细胞状态,先验为高斯混合而非单峰高斯,有利于大数据整合与注释)和 zₙ = f(uₙ, sₙ)(用 **cross-attention / multi-head attention** 建模样本对细胞状态的异质效应);表达 xₙ 由 zₙ 和 nuisance 协变量解码为负二项分布;以 ELBO 训练。**Exploratory**:对每个细胞计算反事实 p(zₙ | uₙ, s′),各样本反事实表征间的欧氏距离构成**每个细胞的样本距离矩阵**;再按距离矩阵对细胞聚类,找出「诱导相同样本分层」的细胞群,并对样本做层次聚类。**Comparative**:DE——在 z 空间用线性模型回归样本组别,经 decoder 得到每个细胞、每个基因的 LFC;DA——估计每个样本在 u 空间的后验密度 p(uₙ|s′),比较两组样本的对数密度比。可以多变量回归同时校正混杂(如炎症状态、性别、部位)。消融支持 attention 设计(补充图 22)。

## 数据
(1) **半合成**:68k PBMC(10x,3,000 HVG,5 个主簇 A–E)分配给 32 个合成受试者,子集 A 注入沿协变量 1 的层级 DE 效应,子集 B/C 注入沿协变量 2 的 DA 效应;(2) **COVID-19 PBMC**:约 41.9 万细胞,患者与健康对照(Haniffa 组数据);(3) **sci-Plex**(sci-RNA-seq3):3 个细胞系、188 种小分子 × 4 剂量 + vehicle、2 个生物学重复,以「药物+剂量」为 target(每细胞系 752 个「样本」),plate 为 nuisance,过滤后 92 药 × 4 剂量 = 368 个扰动样本,重点分析 A549;(4) **克罗恩病**:46 名患者 + 25 名对照,约 46.3 万细胞,含组织部位、取材方式、10x 化学版本等元数据。

## 主要结果
- **半合成**:z 空间只在子集 A 呈现受试者效应;子集 A 的平均样本距离矩阵重现了模拟的层级树,其他子集距离很小、无结构;基于 PCA/scVI 聚类的组成分析不如 MrVI,且在无效应子集引入非零距离。DA 识别比 Milo 更准(PR 曲线);DE 的 LFC 与 DESeq2 伪 bulk「理想答案」高度相关,明显优于 miloDE。(具体数值在图中,正文未列。)
- **COVID-19**:u 空间整合优于 PCA 与 scVI;按距离矩阵聚类得到 3 群细胞(髓系单核/DC、T/NK、B)。只有**单核/DC 诱导的分层**把患者再分成两组,对应症状出现后天数(DSS)低/高(Mann–Whitney P < 0.05)——MrVI 事先不知道 DSS。DA:患者中非经典 CD16⁺ 单核与 DC 减少;DE 得到 3 个基因模块(早期干扰素模块含 GBP1、IFITM3、IFI27;晚期「回到基线」模块含 CSF3R、LGALS2、HLA-DR;TNF/NFKBIZ 模块)。
- **sci-Plex(A549)**:u 空间与药物无关(主要反映细胞周期),z 空间中 HDAC 抑制剂和 trametinib 形成清晰簇。MrVI 样本距离与 Connectivity Map 的一致性、同药不同剂量的聚集度都优于两种组成型方法;层次聚类得到剂量依赖的 HDAC 抑制剂簇,并把 JQ1(BRD 抑制剂)与两种 JAK2 抑制剂(fedratinib、TG101209)聚在一起——与 JQ1 抑制 JAK–STAT 的文献一致,原研究未发现。
- **克罗恩病狭窄(B2,11 人)**:炎症效应广泛,B2 效应较弱、集中在少数基质亚群,最强在一小群 HIGD1B⁺STEAP4⁺ 周细胞(CDH11、ADAMDEC1、COL1A1、LUM、PDGFRB、TGFBI 上调);内皮细胞丰度下降、ADAMDEC1⁺ 成纤维细胞增加;另发现 CD36⁺ 内皮细胞在 B2 中上调 PDGFRB,呈内皮-周细胞混合表型,提示内皮-间质转化(原研究未报告)。

## 创新点
- 把「样本效应」建模为细胞状态依赖的(attention),而不是对所有细胞相同的偏移。
- 以反事实为核心统一了整合、样本分层、DE 与 DA,全部不需要预先聚类,并带不确定性。
- 「每个细胞一个样本距离矩阵」:让不同细胞亚群给出不同的样本分层,发现只在局部体现的患者亚型。
- 同一框架适用于患者队列和扰动筛选(target = 药物 × 剂量)。

## 局限
- 只支持 RNA;多模态(如 ATAC)扩展仅是讨论中的未来方向。
- 复杂整合(克罗恩病:结肠 vs 回肠、黏膜 vs 固有层)下默认设置的细胞状态保留不如 scVI,需引入细胞类型标签的变体。
- DE/DA 由生成模型推断,虽在部分情形用原始数据验证,但仍有模型依赖;超参(u、z 维度)在 sci-Plex 上借助先验知识调优。
- 正文定量指标较少,大部分比较在图中;发现(如 EndMT 周细胞样状态)尚未实验验证。

## 与本研究方向的关系
MrVI 在本方向上横跨 detect 与 model 两阶段。**detect**:它的局部 DA(对数密度比)和每细胞样本距离矩阵,本质上是「哪些细胞、在哪些样本里偏离了正常」——是 Milo(`healthy-ref-natgenet-2023`)的生成式替代,可在 KidneyAnomalyBench 中作为单细胞层面的样本级异常基线。**model**:「u 不受样本影响、z 受样本影响」的反事实结构正是 virtual tissue 想要的可操控表征——把一个患者的细胞「换到」健康样本条件下看表达如何变化,就是 revert 阶段「把异常拉回正常」的计算原型;sci-Plex 部分又展示了把药物当 target 协变量来分组扰动效应。对 **伪影注入课题**:肾活检数据常是多中心、多批次的,MrVI 的 nuisance/target 分离可以把处理批次当 nuisance、患者当 target,检验「只在某些肾单位细胞(如近端小管损伤态)中体现的患者分层」;但 MrVI 只做 RNA,与 snATAC/Xenium 的跨模态一致性需要另行比较。对 **Agent 可信度课题**:MrVI 的 DE 结果来自生成模型而非原始计数,agent 若直接引用模型 LFC 作为证据,verifier 应检查是否有原始数据层面的佐证(本文自己做了这一步,可作为标准)。

## 可复用资产
- **软件**:MrVI 已集成在 scvi-tools。
<https://scvi-tools.org/>
- **复现代码**:
<https://github.com/YosefLab/mrvi-reproducibility/tree/v0.1.0>
- **数据**:COVID-19(Haniffa)h5ad、sci-Plex(figshare)、克罗恩病图谱(Broad Single Cell Portal SCP1884)、10x 68k PBMC。
<https://singlecell.broadinstitute.org/single_cell/study/SCP1884/human-cd-atlas-study-between-colon-and-terminal-ileum>
- **评价指标**:与 Connectivity Map 一致性(silhouette)、同药跨剂量距离百分位——可借用于评价扰动表征。

## 待读
- Methods 与补充材料中的模型细节、超参敏感性(补充表 2–3)。
- 与 Milo、miloDE 和 CNA 在肾脏数据上的直接比较。
- 与扰动模型(`scrna-natmachintell-2026` 的 Conditional Monge Gap、`linear-baselines-natmethods-2025`)比较反事实预测能力。

## 引用
```bibtex
@article{Boyeau_2025, title={Deep generative modeling of sample-level heterogeneity in single-cell genomics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02808-x}, DOI={10.1038/s41592-025-02808-x}, number={11}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Boyeau, Pierre and Hong, Justin and Gayoso, Adam and Kim, Martin and McFaline-Figueroa, José L. and Jordan, Michael I. and Azizi, Elham and Ergen, Can and Yosef, Nir}, year={2025}, month=Oct, pages={2264–2274} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
