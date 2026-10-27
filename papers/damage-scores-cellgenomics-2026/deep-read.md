# Cell-type-specific damage scores reveal kidney and liver disease trajectories in single-cell and spatial transcriptomics

> **Bibkey** `Padvitski_2026` · **Venue** Cell Genomics (2026) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1016/j.xgen.2026.101337>
> `status: abstract-only` — 发表版(CC BY 4.0)全文页被 Cloudflare 拦截、Europe PMC 无全文;本笔记基于**发表版摘要** + 公开 **bioRxiv 预印本 v2**(10.1101/2025.02.20.639269,2025-11-12,题为 "Single-Cell Resolution of Cellular Damage Illuminates Disease Progression")的页面内容。预印本数字是经工具摘取的,**须对照发表版核实**;发表版新增的昼夜节律与 HDS 阈值细节未能读到。把 `source.pdf` 放入本文件夹后可补全。Beyer / Kann 实验室(科隆大学)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 提出一个通用框架,用**细胞类型特异的连续损伤分数**把单个细胞放在"健康 → 损伤"轴上:从大量小鼠疾病模型中挑出一致变化的 42 个基因,用 AUCell 打分,得到足细胞损伤分数 PDS(CKD/FSGS)与肝细胞损伤分数 HDS(MASLD/NASH);在小鼠与人的 scRNA、snRNA、空间转录组、蛋白组、组织学与临床数据中都能检出疾病相关损伤,能"对齐"不同疾病模型,并在未扰动的对照细胞中也分辨出损伤程度差异。
<!-- EN --> A general framework of **cell-type-specific continuous damage scores** that place individual cells on a health-to-damage axis: 42 genes with consistent changes across many mouse disease models are scored with AUCell, giving the podocyte damage score PDS (CKD/FSGS) and hepatocyte damage score HDS (MASLD/NASH); across mouse and human scRNA, snRNA, spatial transcriptomics, proteomics, histology and clinical data they detect disease-associated damage, align different disease models, and resolve damage variation even among unperturbed control cells.

## 研究问题 / Problem
<!-- ZH --> 退行性疾病通过逐步累积的细胞内在损伤进展,但 bulk 转录组会把它平均掉,而离散的细胞状态注释(如"injured/altered state")又把连续过程切成类别,难以刻画单个细胞在体内的渐进衰退。需要一个可迁移、可跨数据集与跨物种比较的连续损伤度量。
<!-- EN --> Degenerative diseases progress through gradual cell-intrinsic damage, but bulk transcriptomics averages it away and discrete cell-state annotation (e.g. "injured/altered states") chops a continuous process into categories, making it hard to resolve individual cells' gradual decline in vivo. A transferable continuous damage measure, comparable across datasets and species, is needed.

## 方法 / Method
<!-- ZH --> (以下据预印本 v2)**基因选择**:在每个疾病模型内按差异表达 p 值给基因排名,跨模型平均排名;过滤条件为在目标细胞类型中表达、且在 ≥ 75% 研究中方向一致;取前 n 个作为损伤标记基因。**最终签名**:PDS 42 个基因(39 下调、3 上调),HDS 42 个基因(30 下调、12 上调)。**打分**:AUCell 基于排名的方法,按方向合并上调与下调基因,得到单细胞分辨率分数。**验证**:留一模型交叉验证(去掉一个疾病模型的全部样本重算签名,再在被留出模型上检验);稳健性测试(标记基因数 30–200 变化影响很小;随机打乱至多 70% 输入研究仍能区分疾病与对照)。下游:基于 PDS 的通路"指纹"分析、在相同损伤水平下比较不同模型、用足细胞 ATAC 数据构建转录调控网络、GWAS 富集。
<!-- EN --> (From preprint v2.) **Gene selection**: rank genes by differential-expression p value within each disease model, average ranks across models, filter for expression in the target cell type and consistent direction in ≥75% of studies, take the top n as damage markers. **Signatures**: PDS 42 genes (39 down, 3 up), HDS 42 genes (30 down, 12 up). **Scoring**: AUCell rank-based scoring combining up- and down-regulated genes by direction, at single-cell resolution. **Validation**: leave-one-model-out (drop all samples of one model, rebuild the signature, test on the held-out model); robustness (30–200 marker genes changes little; shuffling up to 70% of input studies still separates disease from control). Downstream: PDS-based pathway fingerprinting, comparisons across models at matched damage, a podocyte transcriptional regulatory network from ATAC data, GWAS enrichment.

## 数据 / Data
<!-- ZH --> (据预印本 v2)**小鼠**:足细胞 37 个数据集、9 种足细胞病模型(如 Nphs2mut、Cd2apko、Pdss2mut、阿霉素、NTN、Btbr ob/ob 糖尿病、Wt1 ko/wt);肝细胞约 250 个样本、13 种肝病模型(CCl4、DDC、乙醇、链脲佐菌素、NAFLD 等);Slide-seqV2(Btbr ob/ob,GSE190094)与 Visium(NAFLD 小鼠)。**人**:KPMP snRNA-seq(n = 37,有临床数据)、scRNA-seq(n = 17)、1 个 FSGS Visium 活检;新生成的 Xenium(8 名微小病变或 FSGS 患者,238 个肾小球);NEPTUNE 尿液足细胞;肝 GSE189600(3 健康 / 3 NASH)、GSE210077(3 健康 / 3 纤维化)、2 例脂肪变 Visium。
<!-- EN --> (From preprint v2.) **Mouse**: 37 podocyte datasets over 9 podocytopathy models (e.g. Nphs2mut, Cd2apko, Pdss2mut, doxorubicin, NTN, Btbr ob/ob diabetic, Wt1 ko/wt); ~250 hepatocyte samples over 13 liver models (CCl4, DDC, ethanol, streptozotocin, NAFLD …); Slide-seqV2 (Btbr ob/ob, GSE190094) and Visium (NAFLD mouse). **Human**: KPMP snRNA-seq (n = 37 with clinical data), scRNA-seq (n = 17), one FSGS Visium core; newly generated Xenium (8 minimal-change/FSGS patients, 238 glomeruli); NEPTUNE urine podocytes; liver GSE189600 (3 healthy / 3 NASH), GSE210077 (3 healthy / 3 fibrosis), Visium steatosis from 2 patients.

## 主要结果 / Key results
- <!-- ZH --> **发表版摘要**:PDS 把足细胞损伤与 FSGS 进展联系到**昼夜节律基因表达紊乱**;HDS 在 MASLD/NASH 中识别出一个**损伤阈值**,超过后肝细胞进入衰老、代谢功能障碍状态。 <!-- EN --> **Published abstract**: PDS links podocyte injury and FSGS progression to **circadian gene-expression disruption**; HDS identifies a **damage threshold** in MASLD/NASH beyond which hepatocytes adopt senescent, metabolically dysfunctional states.
- <!-- ZH --> (预印本)**与功能相关**:小鼠 12 个 bulk 肾小球研究中 PDS 与白蛋白尿 Spearman ρ = 0.45(p = 0.017),新 snRNA-seq 数据 ρ = 0.78(p = 1.8 × 10⁻⁶);KPMP 中只有糖尿病状态与 PDS 与 ACR 显著相关;NEPTUNE 尿足细胞 PDS 与 UPCR 相关。 <!-- EN --> (Preprint) **Function**: PDS vs albuminuria Spearman ρ = 0.45 (p = 0.017) across 12 mouse bulk glomerular studies and ρ = 0.78 (p = 1.8 × 10⁻⁶) in new snRNA-seq; in KPMP only diabetic status and PDS correlated with ACR; in NEPTUNE urine podocytes PDS tracks UPCR.
- <!-- ZH --> (预印本)**空间与形态**:人 Xenium 238 个肾小球中 PDS 与足细胞密度负相关、与裂孔隔膜长度相关(p < 0.05);小鼠空间数据中肾小球 PDS 差异显著。 <!-- EN --> (Preprint) **Spatial/morphology**: in 238 human Xenium glomeruli PDS anti-correlates with podocyte density and correlates with slit-diaphragm length (p < 0.05); glomerular PDS differences are significant in mouse spatial data.
- <!-- ZH --> (预印本)**对照细胞也有损伤谱**:对照样本平均损伤更低,但总含一小部分高损伤细胞;PDS 可像白蛋白尿在临床上那样"对齐"不同模型的损伤状态。蛋白组数据上 PDS/HDS 无一例外地分开疾病与对照。 <!-- EN --> (Preprint) **Controls carry damage too**: controls have lower mean damage but always contain a small fraction of high-damage cells; PDS can "align" damage states across models as albuminuria does clinically. On proteomics, PDS/HDS separate disease from control without exception.
- <!-- ZH --> (预印本)**遗传**:PDS 42 基因中 8 个与肾病 GWAS 相关(基因体富集 p = 0.031,含侧翼 p = 0.002);HDS 10/42 与肝 GWAS 相关(p = 0.1,不显著)。 <!-- EN --> (Preprint) **Genetics**: 8/42 PDS genes are kidney-disease GWAS genes (gene-body enrichment p = 0.031; with flanks p = 0.002); 10/42 HDS genes for liver traits (p = 0.1, n.s.).

## 创新点 / Contributions
- <!-- ZH --> 把"损伤"定义为跨模型共识的**连续、细胞类型特异**的单细胞分数,而非离散状态标签。 <!-- EN --> Defines damage as a cross-model consensus **continuous, cell-type-specific** single-cell score rather than a discrete state label.
- <!-- ZH --> 留一模型验证 + 打乱研究的稳健性测试,说明签名能泛化到未见过的疾病模型。 <!-- EN --> Leave-one-model-out validation and study-shuffling robustness show generalization to unseen disease models.
- <!-- ZH --> 一个分数横跨 sc/sn/空间/蛋白/组织学/临床模态与小鼠→人,可在相同损伤水平下比较不同病因。 <!-- EN --> One score spans sc/sn/spatial/proteomic/histology/clinical modalities and mouse→human, enabling comparisons across aetiologies at matched damage.

## 局限 / Limitations
- <!-- ZH --> 签名源自小鼠模型,人类验证队列部分很小(肝 3 vs 3)。 <!-- EN --> Signatures derive from mouse models; some human validation cohorts are tiny (liver 3 vs 3).
- <!-- ZH --> sc 与 sn 数据的 PDS 基线有小差异(作者归因于组织消化损伤)—— 说明分数会受**技术/处理伪影**影响。 <!-- EN --> PDS baselines differ slightly between sc and sn data (attributed to tissue-digestion damage) — the score is sensitive to **technical/processing artifacts**.
- <!-- ZH --> 肝细胞伪时间轨迹被分区(zonation)主导,可能掩盖损伤信号。 <!-- EN --> Hepatocyte pseudotime is dominated by zonation, potentially masking damage.
- <!-- ZH --> 只针对足细胞与肝细胞两种细胞类型;是"已知损伤方向"的监督式签名,不能发现签名之外的新异常。 <!-- EN --> Covers only podocytes and hepatocytes; a supervised "known damage direction" signature that cannot discover anomalies outside it.
- <!-- ZH --> 本笔记未读到发表版全文,上述细节需核实。 <!-- EN --> Published full text not read here; details need verification.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是 **课题 1** 最直接的"已知方向"对照:我们的异常检测是无监督的"离健康参照有多远",而 PDS 是有监督的"沿共识损伤方向走了多远"。两者组合很有价值:(1) **作为基线与弱标签** —— 在待测肾样本与 KPMP/Lake 数据上,检测器给出的足细胞异常分数应与 PDS 显著相关;不相关的高异常细胞要么是新型异常、要么是伪影 —— 正是需要跨模态一致性(snATAC、Xenium 足细胞密度、H&E 形态)来裁决的部分;(2) 它报告"sc 与 sn 基线不同、归因于消化损伤",以及"对照样本总有一小部分高损伤细胞" —— 这与 Lake 2023 "参照组织中也有 altered states"一致,是 KidneyAnomalyBench 必须区分的**取样/解离伪影 vs 真实损伤**;(3) 它的 Xenium 验证(PDS vs 足细胞密度、裂孔隔膜长度)示范了**转录组分数与形态学读数的跨模态对齐**,可以直接借作我们的验证协议。对 **detect → model → revert**:连续损伤轴就是 virtual tissue 里一个天然的"状态坐标",revert 的目标可以表述为"把 PDS 降回对照分布";发表版提出的 HDS 阈值(超过即衰老)提示存在**可逆窗口**,对选择回退干预的时机很关键。对 **课题 2**:它是 agent 可调用的简单、可复现工具(签名 + AUCell),适合测试 rerun stability 与"agent 是否正确报告了分数的适用范围(仅足细胞/肝细胞、小鼠来源)"。
<!-- EN --> This is **Topic 1's** most direct "known-direction" counterpart: our anomaly detection is unsupervised "how far from the healthy reference", whereas PDS is supervised "how far along the consensus damage direction". Combining them is valuable: (1) **baseline and weak label** — on the kidney samples to be tested and on KPMP/Lake data, a detector's podocyte anomaly score should correlate with PDS; high-anomaly cells that do *not* correlate are either new anomaly types or artifacts — exactly what cross-modal agreement (snATAC, Xenium podocyte density, H&E morphology) must adjudicate; (2) its report that sc vs sn baselines differ due to digestion damage, and that controls always contain a few high-damage cells, matches Lake 2023's "altered states in reference tissue" — the **procurement/dissociation artifact vs true damage** distinction KidneyAnomalyBench must test; (3) its Xenium validation (PDS vs podocyte density and slit-diaphragm length) shows **cross-modal alignment of a transcriptomic score with morphological readouts**, a validation protocol to reuse. For **detect → model → revert**: the continuous damage axis is a natural "state coordinate" in a virtual tissue, and reverting can be phrased as "bring PDS back into the control distribution"; the published HDS threshold (beyond which cells turn senescent) suggests a **reversibility window**, crucial for timing revert interventions. For **Topic 2**: it is a simple, reproducible tool (signature + AUCell) an agent can call — good for testing rerun stability and whether the agent correctly states its scope (podocytes/hepatocytes only, mouse-derived).

## 可复用资产 / Reusable assets
- <!-- ZH --> **签名:** PDS / HDS 各 42 个基因(见论文补充表;须从发表版获取)。 <!-- EN --> **Signatures:** PDS / HDS, 42 genes each (supplementary tables; obtain from the published version).
- <!-- ZH --> **代码(作者 Paula Unger Avila 的 GitHub,未在论文中核实对应关系):** HDS 相关脚本仓库。 <!-- EN --> **Code (GitHub of co-author Paula Unger Avila; correspondence to the paper not verified):** HDS script repositories.
<!-- ZH/EN --> <https://github.com/PauUng/HepatocyteDamageScore> · <https://github.com/PauUng/hepatocyte-damage-score-paper>
- <!-- ZH --> **数据:** KPMP、GSE190094(Slide-seqV2)、GSE189600、GSE210077 等公开数据;新 Xenium 数据见发表版数据声明。 <!-- EN --> **Data:** public KPMP, GSE190094 (Slide-seqV2), GSE189600, GSE210077; new Xenium data per the published data statement.
- <!-- ZH --> **预印本:** <!-- EN --> **Preprint:**
<!-- ZH/EN --> <https://doi.org/10.1101/2025.02.20.639269>

## 待读 / Follow-ups
- <!-- ZH --> 获取发表版 PDF,核实数字、昼夜节律机制与 HDS 阈值,补全代码/数据可用性。 <!-- EN --> Get the published PDF to verify numbers, the circadian mechanism and HDS threshold, and code/data availability.
- <!-- ZH --> 把 PDS 思路扩展到 PT/TAL(对照 Lake 2023 的 aPT/aTAL 与 CellSpectra 的通路协调分数)。 <!-- EN --> Extend the PDS idea to PT/TAL (cf. Lake 2023 aPT/aTAL and CellSpectra pathway-coordination scores).
- <!-- ZH --> 比较"监督式损伤分数"与"无监督参照距离"在肾脏 Xenium 数据上的一致性。 <!-- EN --> Compare supervised damage scores with unsupervised reference distance on kidney Xenium data.

## 引用 / Cite
```bibtex
@article{Padvitski_2026, title={Cell-type-specific damage scores reveal kidney and liver disease trajectories in single-cell and spatial transcriptomics}, volume={6}, ISSN={2666-979X}, url={http://dx.doi.org/10.1016/j.xgen.2026.101337}, DOI={10.1016/j.xgen.2026.101337}, number={10}, journal={Cell Genomics}, publisher={Elsevier BV}, author={Padvitski, Tsimafei and Unger Avila, Paula and Chen, He and Özel, Cem and Braun, Fabian and Kroll, Marie-Kristin and Vossen, Christian and Wienand, Peter and Butt, Linus and Unnersjö-Jess, David and Schumacher, Anna-Lena and Folz-Donahue, Kat and Göbel, Heike and Kuppe, Christoph and Müller, Roman-Ulrich and Westermark, Pål Olof and Brinkkötter, Paul Thomas and Schermer, Bernhard and Benzing, Thomas and Wunderlich, Frank Thomas and Kann, Martin and Beyer, Andreas}, year={2026}, month=Oct, pages={101337} }
```
