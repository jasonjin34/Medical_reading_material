# An atlas of healthy and injured cell states and niches in the human kidney

> **文献键** `Lake_2023` · **来源** Nature(2023) · **类别** spatial · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41586-023-05769-3> · `status: complete`

---

## 一句话
KPMP / HuBMAP / HCA 联合构建的人肾多模态单细胞 + 空间图谱:> 40 万个细胞/细胞核(snRNA、scRNA、SNARE-seq2 双组学),配合 Slide-seq2、Visium 与大规模 3D 成像,覆盖 45 名健康参照供体与 48 名 AKI/CKD 患者,定义 51 种主要细胞类型和 **28 种损伤相关的"altered states"**(cycling、adaptive/maladaptive repair、transitioning、degenerative),把它们定位到损伤 niche,并发现 TAL/PT 的 adaptive 修复签名可预测肾功能下降。

## 研究问题
肾损伤后小管与间质发生动态的急慢性改变,成功修复与 maladaptive repair 的平衡决定了 AKI → CKD → 肾衰竭的进程。要理解这个过程,需要在单细胞分辨率上界定**健康参照状态**与**损伤后的改变状态**,知道它们在组织中的位置、邻域与相互作用,并把它们与临床结局联系起来。已有图谱多聚焦健康细胞类型的整合,缺少系统的、跨技术交叉验证的损伤状态定义与空间定位。

## 方法
**单细胞多组学**:10x Chromium v3 单核(snCv3)与单细胞(scCv3)RNA-seq,以及 SNARE-seq2(同一细胞核的 RNA + 染色质可及性)。snCv3 先做无监督聚类(100 个群 → 77 个 subclass),再作为锚把 scCv3 与 SNARE2 映射到同一 embedding 并转移标签。**Altered states** 依据既往研究与已知损伤特征(Supplementary Table 10)人工界定,并通过映射到小鼠 AKI(IRI)时间序列模型来确认其时间进程。**空间**:Slide-seq2(10 µm bead,6 人 67 个 puck)、Visium(55 µm spot,22 人 23 个样本)做反卷积/标签转移与共定位分析;3D 多重免疫荧光 + 无标记细胞术(3DTC,含 SHG 胶原信号)对 15 名个体做邻域分析(约 1.2M 邻域)与社区检测得到 niche。**下游**:轨迹推断与 RNA velocity、模块检测、SNARE2 的 chromVAR 转录因子活性与 GRN(含模拟 TF 扰动)、配体–受体互作、GWAS/eQTL 富集;临床关联用 NEPTUNE 队列(生存分析,ESRD 或 eGFR 下降 40% 的复合终点)与 ERCB 队列。为减少采样/技术偏差,很多样本用多于一种技术处理以做交叉验证。

## 数据
摘要层面:45 名健康参照供体、48 名患者,> 40 万高质量细胞/细胞核;整合转录组分析覆盖 58 个参照组织(35 名供体)与 52 个疾病组织(36 名患者)。样本来源包括健康参照(肿瘤肾切除旁组织、死亡供体、活体供体活检)与 KPMP 的 AKI/CKD 活检;单细胞实验用了 15 例 CKD、12 例 AKI、18 例活体供体活检核心。Visium 共 146,460 个 spot(22 人);3DTC 分类 1,540,563 个细胞、14 类细胞、14 个 niche。临床:NEPTUNE(正文 193 例、图注 199 例)、ERCB 131 例。

## 主要结果
- **细胞类型**:51 种主要(canonical)细胞类型,含稀有与此前未描述的群体,并附 marker、开放染色质与 TF motif 图谱;Slide-seq/Visium 重现肾小体、JGA、皮髓质过渡(ATL→M-TAL→C-TAL)等空间组织。
- **28 种 altered states**:degenerative 状态高表达 SPP1、CST3、CLU、IGFBP7,共享 FOS/JUN 签名,在小鼠损伤后早期出现、恢复后消退;adaptive PT(aPT:VCAM1、DCDC2、HAVCR1)对应啮齿类 failed repair;新发现 **adaptive TAL(aTAL:PROM1/CD133、DCDC2、ITGB6)**,在小鼠 AKI 后持续 6 周;间质 altered states 包括 MyoF、cycMyoF 与 aFIB(POSTN、FAP、ACTA2、胶原)。**重要提醒**:altered states 也出现在参照组织中,可能来自取样时缺血应激或正常衰老。
- **空间损伤 niche**:Visium 中 altered 签名在 AKI/CKD 显著富集;免疫与间质细胞更常与 altered 上皮共定位;3DTC 中 CD3+ T 细胞几乎只出现在含上皮退化与纤维化的邻域(N13),髓系细胞(CD68+)出现在较健康、正在修复的区域。
- **修复轨迹与信号**:aEpi 轨迹从去分化到成熟,富集 Wnt、Notch、TGF-β、EGF、MAPK、JAK/STAT、NF-κB;GRN 提示 TFAP2B(原文写作 "TRAP2B",即 AP-2β)关键,模拟扰动 TFAP2B 会打断修复轨迹;aTAL 早期修复态先与免疫、中期与间质互作(NRG1/NRG3、NECTIN2、BMP6、IGF1)。
- **临床关联**:NEPTUNE 中按状态分数分层的 Kaplan–Meier:aPT P = 0.021、**aTAL P = 0.003**、degenerative P = 0.55(log-rank trend);ERCB 中糖尿病、高血压、FSGS 患者 aPT 与 aPT–aTAL 共同签名高于活体供体(糖尿病组在校正年龄、性别、eGFR 后仍更高)。eGFR/CKD 因果变异富集于 TAL 调控区(ESRR motif)。作者提醒临床样本量小,应谨慎解读。

## 创新点
- 第一个跨 snRNA/scRNA/SNARE2/Slide-seq/Visium/3D 成像**交叉验证**的人肾健康 + 损伤图谱,并统一到同一套注释。
- 系统定义并命名 altered states(cycling / adaptive / transitioning / degenerative),成为后续肾脏单细胞工作的通用词汇与参照。
- 发现 aTAL 状态并把 TAL 提升为肾病进展的核心节段。
- 公开 Azimuth 参照映射、cellxgene、KPMP Atlas Explorer 等可交互资源。

## 局限
- Altered states 由先验知识人工界定,并非无监督发现;而且也出现在"健康"参照中(取样缺血、衰老),说明健康/异常边界本身是模糊的。
- 临床关联样本量小(作者自述),且是关联非因果;部分时间进程推断依赖小鼠 IRI 模型。
- Visium 55 µm spot 分辨率有限,只能做共定位而非单细胞空间分析;不包含 Xenium 等亚细胞空间平台。
- KPMP 原始测序数据为受控访问;不同来源(肾切除、死亡供体、活检)存在采样差异。

## 与本研究方向的关系
这是 **Plan A 的参照骨架**。detect → model → revert 中的"detect"需要一个"什么是正常"的参照流形,而 Lake 2023 正是肾脏领域事实上的健康参照 + 损伤状态标注:(1) **Azimuth 健康参照**可直接作为异常检测的 reference(把我们 95 例活检的 snRNA 映射上去,映射置信度低/距离远即候选异常);(2) **28 个 altered states 提供"已知异常"的弱标签** —— KidneyAnomalyBench 可以用它们做第一层评测(检测器能否在不看标签的情况下把 aPT/aTAL/degenerative 排在前面),再把"Lake 标签之外"的高异常分数细胞作为待专家验证的新发现;(3) 它自陈 altered states 也出现在参照组织里(取样缺血、衰老) —— 这正是 Plan A "跨模态一致性区分伪影与疾病"要解决的混淆:单一模态上看起来"受损"的细胞,若 snATAC/Xenium/H&E 不一致,更可能是取样伪影;(4) 同一样本多技术交叉验证的设计,是我们 snRNA + snATAC + Xenium + H&E 设计的直接前例;(5) 它是 NIH Kidney AI 挑战所用 KPMP open 数据的主要来源之一,其细胞状态可用于挑战第 3 项评审标准的患者分层。对 "model/revert":TFAP2B 模拟扰动打断修复轨迹,是 GRN 层面"虚拟扰动"的早期示例,可与 virtual tissue 的扰动预测对照。对 **Plan B**,它是 agent 分析肾脏组学时最常被引用的"已知结论"来源,可用来构造 claim-to-evidence 的 ground truth(例如"aTAL 标记为 PROM1/DCDC2/ITGB6")与检测"复述文献 vs 从数据得出"的测试。

## 可复用资产
- **数据(处理后):** GEO Superseries GSE183279(snCv3、scCv3、SNARE2、Slide-seq、Visium)。
<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE183279>
- **参照映射:** Azimuth 人肾参照(snCv3 健康参照)。
<https://azimuth.hubmapconsortium.org/>
- **可视化:** cellxgene 集合与 KPMP Atlas Explorer;3D 成像细胞术数据在 Zenodo。
<https://cellxgene.cziscience.com/collections/bcb61471-2a44-4d00-a0af-ff085512674c> · <https://atlas.kpmp.org/explorer/> · <https://doi.org/10.5281/zenodo.7120941>
- **代码:** 复现图表的代码。
<https://github.com/KPMP/Cell-State-Atlas-2022>
- **原始数据:** KPMP repository(原始测序受控访问,3D 成像原始数据可自由下载)。
<https://atlas.kpmp.org/repository/>

## 待读
- Kirita 等小鼠 AKI 时间序列(本文用于验证 altered states 的时间进程)。
- 后续用 Lake 参照做损伤打分的工作:本仓库的 damage-scores(Padvitski 2026)、CellSpectra(Klötzer 2025)与 DKD 空间图谱(Dumoulin 2026)。
- KPMP 后续的 Xenium / 多组学发布,以及 HuBMAP 肾脏数据,以对齐我们的模态组合。

## 引用
```bibtex
@article{Lake_2023, title={An atlas of healthy and injured cell states and niches in the human kidney}, volume={619}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-023-05769-3}, DOI={10.1038/s41586-023-05769-3}, number={7970}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Lake, Blue B. and Menon, Rajasree and Winfree, Seth and Hu, Qiwen and Melo Ferreira, Ricardo and Kalhor, Kian and Barwinska, Daria and Otto, Edgar A. and Ferkowicz, Michael and Diep, Dinh and Plongthongkum, Nongluk and Knoten, Amanda and Urata, Sarah and Mariani, Laura H. and Naik, Abhijit S. and Eddy, Sean and Zhang, Bo and Wu, Yan and Salamon, Diane and Williams, James C. and Wang, Xin and Balderrama, Karol S. and Hoover, Paul J. and Murray, Evan and Marshall, Jamie L. and Noel, Teia and Vijayan, Anitha and Hartman, Austin and Chen, Fei and Waikar, Sushrut S. and Rosas, Sylvia E. and Wilson, Francis P. and Palevsky, Paul M. and Kiryluk, Krzysztof and Sedor, John R. and Toto, Robert D. and Parikh, Chirag R. and Kim, Eric H. and Satija, Rahul and Greka, Anna and Macosko, Evan Z. and Kharchenko, Peter V. and Gaut, Joseph P. and Hodgin, Jeffrey B. and Knight, Richard and Lecker, Stewart H. and Stillman, Isaac and Amodu, Afolarin A. and Ilori, Titlayo and Maikhor, Shana and Schmidt, Insa and McMahon, Gearoid M. and Weins, Astrid and Hacohen, Nir and Bush, Lakeshia and Gonzalez-Vicente, Agustin and Taliercio, Jonathan and O’toole, John and Poggio, Emilio and Cooperman, Leslie and Jolly, Stacey and Herlitz, Leal and Nguyen, Jane and Palmer, Ellen and Sendrey, Dianna and Spates-Harden, Kassandra and Appelbaum, Paul and Barasch, Jonathan M. and Bomback, Andrew S. and D’Agati, Vivette D. and Mehl, Karla and Canetta, Pietro A. and Shang, Ning and Balderes, Olivia and Kudose, Satoru and Barisoni, Laura and Alexandrov, Theodore and Cheng, Yinghua and Dunn, Kenneth W. and Kelly, Katherine J. and Sutton, Timothy A. and Wen, Yumeng and Corona-Villalobos, Celia P. and Menez, Steven and Rosenberg, Avi and Atta, Mohammed and Johansen, Camille and Sun, Jennifer and Roy, Neil and Williams, Mark and Azeloglu, Evren U. and He, Cijang and Iyengar, Ravi and Hansen, Jens and Xiong, Yuguang and Rovin, Brad and Parikh, Samir and Madhavan, Sethu M. and Anderton, Christopher R. and Pasa-Tolic, Ljiljana and Velickovic, Dusan and Troyanskaya, Olga and Sealfon, Rachel and Tuttle, Katherine R. and Laszik, Zoltan G. and Nolan, Garry and Sarwal, Minnie and Anjani, Kavya and Sigdel, Tara and Ascani, Heather and Balis, Ulysses G. J. and Lienczewski, Chrysta and Steck, Becky and He, Yougqun and Schaub, Jennifer and Blanc, Victoria M. and Murugan, Raghavan and Randhawa, Parmjeet and Rosengart, Matthew and Tublin, Mitchell and Vita, Tina and Kellum, John A. and Hall, Daniel E. and Elder, Michele M. and Winters, James and Gilliam, Matthew and Alpers, Charles E. and Blank, Kristina N. and Carson, Jonas and De Boer, Ian H. and Dighe, Ashveena L. and Himmelfarb, Jonathan and Mooney, Sean D. and Shankland, Stuart and Williams, Kayleen and Park, Christopher and Dowd, Frederick and McClelland, Robyn L. and Daniel, Stephen and Hoofnagle, Andrew N. and Wilcox, Adam and Bansal, Shweta and Sharma, Kumar and Venkatachalam, Manjeri and Zhang, Guanshi and Pamreddy, Annapurna and Kakade, Vijaykumar R. and Moledina, Dennis and Shaw, Melissa M. and Ugwuowo, Ugochukwu and Arora, Tanima and Ardayfio, Joseph and Bebiak, Jack and Brown, Keith and Campbell, Catherine E. and Saul, John and Shpigel, Anna and Stutzke, Christy and Koewler, Robert and Campbell, Taneisha and Hayashi, Lynda and Jefferson, Nichole and Pinkeney, Roy and Roberts, Glenda V. and Eadon, Michael T. and Dagher, Pierre C. and El-Achkar, Tarek M. and Zhang, Kun and Kretzler, Matthias and Jain, Sanjay}, year={2023}, month=July, pages={585–594} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
