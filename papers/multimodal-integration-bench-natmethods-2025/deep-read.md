# Benchmarking single-cell multi-modal data integrations

> **Bibkey** `Fu_2025_MultimodalBench` · **Venue** Nature Methods (2025, Registered Report) · **Category** single-cell · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s41592-025-02737-9>
> `status: complete` — 出版版本需订阅;本精读基于作者公开的 bioRxiv Stage-2 预印本全文(10.1101/2025.04.01.646578,CC BY-NC,2025-04-08)。正式版与预印本的数字可能有细微差别。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> SCMMIB:以 Registered Report 形式,对 40 个单细胞多模态整合算法(拆成 65 个「方法×任务」)在 6 类任务上 —— 配对 RNA+ATAC、配对 RNA+ADT、空间多组学、非配对 RNA+ATAC 对角整合、RNA+ATAC mosaic、RNA+ADT mosaic —— 用 14 个公开数据集派生的 101 个基准数据集评估可用性、准确性与鲁棒性;Seurat v4 WNN(配对 RNA+ATAC)与 GLUE(非配对对角)是各自任务的 SOTA,MIDAS 是 mosaic 跨模态插补的 SOTA。
<!-- EN --> SCMMIB: a Registered Report benchmarking 40 single-cell multimodal integration algorithms (65 method×task combinations) on six tasks — paired RNA+ATAC, paired RNA+ADT, spatial multi-omics, unpaired RNA+ATAC diagonal, RNA+ATAC mosaic and RNA+ADT mosaic — over 101 benchmark datasets derived from 14 public datasets, scoring usability, accuracy and robustness. Seurat v4 WNN (paired RNA+ATAC) and GLUE (unpaired diagonal) are SOTA for their tasks; MIDAS is SOTA for mosaic cross-modality imputation.

## 研究问题 / Problem
<!-- ZH --> 单细胞多模态整合工具已超过 40 个,但各模态维度(几十个 ADT 到几十万个 ATAC peak)与稀疏性差异极大,配对/非配对/mosaic 场景各不相同;此前的 benchmark 只覆盖少数工具(例如 5 个 RNA+ATAC 工具和 4 个 Multiome 引导的 mosaic 工具)。用户缺乏按数据类型、模态、规模、质量选择方法的系统依据。
<!-- EN --> There are 40+ multimodal integration tools, but modalities differ enormously in dimension (tens of ADTs to hundreds of thousands of ATAC peaks) and sparsity, and paired/unpaired/mosaic settings differ; prior benchmarks covered few tools (e.g. 5 RNA+ATAC tools and 4 Multiome-guided mosaic tools). Users lack systematic guidance by data type, modality, size and quality.

## 方法 / Method
<!-- ZH --> **方法集合**:bindSC、GLUE、MultiVI、Multigrate、MOFA+、MIDAS、Seurat v3 CCA / v4 RPCA / v4 WNN / v5 bridge、totalVI、StabMap、SpatialGlue、scMVP、scMDC、uniPort、MaxFuse、SIMBA、cobolt、scMoMaT、scVAEIT 等 40 个。**三维评价**:(1) 可用性 —— 论文/代码/文档质量与是否在预设硬件限制内运行(可扩展性测试至 500,000 细胞;内存上限 500 GB);(2) 准确性 —— 配对任务看联合嵌入的生物保守性与批次去除(scib 类指标,且**不向任何方法提供批次信息**以保证公平,另单独测提供批次参数的影响);非配对/ mosaic 任务把配对数据人为拆成「伪非配对」,以已知的细胞对应作金标准,评估 FOSCTTM、cell match、cell type match 等对齐准确性;支持插补的方法另评插补(scATAC 在细胞层用 AUPR、细胞类型层用 AUROC);(3) 鲁棒性 —— 下采样模拟稀疏度(多梯度 downsample AUC、10% 深度下的准确性)、mosaic 中配对数据规模(3,000–20,000 细胞),以及 5 次重复运行的 SD / CV。
<!-- EN --> **Methods**: 40 including bindSC, GLUE, MultiVI, Multigrate, MOFA+, MIDAS, Seurat v3 CCA / v4 RPCA / v4 WNN / v5 bridge, totalVI, StabMap, SpatialGlue, scMVP, scMDC, uniPort, MaxFuse, SIMBA, cobolt, scMoMaT, scVAEIT. **Three axes**: (1) usability — paper/code/documentation quality and whether a method runs within preset hardware limits (scalability up to 500,000 cells; 500 GB memory cap); (2) accuracy — for paired tasks, biological conservation and batch removal of the joint embedding (scib-style metrics; **no method receives batch labels**, for fairness, with a separate test of the batch parameter); for unpaired/mosaic tasks, paired data are split into "pseudo-unpaired" data with known cell matches as gold standard, scoring FOSCTTM, cell match and cell-type match; imputation-capable methods are scored on imputation (scATAC: AUPR at cell level, AUROC at cell-type level); (3) robustness — downsampling to simulate sparsity (multi-gradient downsample AUC, accuracy at 10% depth), paired-set size in mosaic tasks (3,000–20,000 cells), and SD/CV over five repeated runs.

## 数据 / Data
<!-- ZH --> 14 个公开数据集 → 101 个基准数据集,覆盖免疫、肾、皮肤、脑等,1,000–700,000 细胞,2–143 个批次:NeurIPS 2021 BMMC Multiome 与 CITE-seq(GSE194122)、HSPC Multiome/CITE-seq(Kaggle Open Problems)、SHARE-seq 皮肤、COVID-19 CITE-seq、人 WBC CITE-seq、10x NSCLC CITE-seq、**10x 肾癌 CITE-seq**、10x 小鼠脑与 PBMC Multiome;空间多组学:SPOTS 小鼠脾、小鼠胸腺、人淋巴结。处理后的输入数据在 Figshare 公开。
<!-- EN --> 14 public datasets → 101 benchmark datasets spanning immune, kidney, skin and brain, 1,000–700,000 cells, 2–143 batches: NeurIPS 2021 BMMC Multiome and CITE-seq (GSE194122), HSPC Multiome/CITE-seq (Kaggle Open Problems), SHARE-seq skin, COVID-19 CITE-seq, human WBC CITE-seq, 10x NSCLC CITE-seq, **10x kidney-cancer CITE-seq**, 10x mouse brain and PBMC Multiome; spatial multi-omics: SPOTS mouse spleen, mouse thymus, human lymph node. Processed inputs are on Figshare.

## 主要结果 / Key results
- <!-- ZH --> **配对 RNA+ATAC**:生物保守性前三 Seurat v4 WNN、scMDC、scMVP;批次去除前三 Seurat v4、scDEC、scMVP,但排名随数据集变化;只有 MultiVI、uniPort、scMVP 能跑 500k 细胞。为 MultiVI 提供批次信息可改善 5 项批次指标中的 4 项。稀疏鲁棒性:Seurat v4 WNN、Multigrate、scMVAE、scMVP 最好;scDEC 的重复运行变异最大。插补:scMVP(RNA)与 DCCA(ATAC)最好。 <!-- EN --> **Paired RNA+ATAC**: top biological conservation Seurat v4 WNN, scMDC, scMVP; top batch removal Seurat v4, scDEC, scMVP, though rankings vary by dataset; only MultiVI, uniPort and scMVP ran at 500k cells. Supplying batch labels improves 4 of 5 batch metrics for MultiVI. Sparsity robustness: Seurat v4 WNN, Multigrate, scMVAE, scMVP best; scDEC has the largest run-to-run variation. Imputation: scMVP (RNA) and DCCA (ATAC) best.
- <!-- ZH --> **配对 RNA+ADT**:totalVI、Seurat v4 WNN、bindSC 生物保守性最好;但 totalVI 在混合批次数据上不给批次信息时跌至 10 个方法中第 8;提供批次后 totalVI 的 graph iLISI 0.1→0.4、ARI 0.37→0.62,Multigrate iLISI 0.22→0.43、ARI 0.32→0.50。空间多组学中 SpatialGlue 最好,但批次去除不如 Harmony 与 STAligner。 <!-- EN --> **Paired RNA+ADT**: totalVI, Seurat v4 WNN and bindSC best on biological conservation; but totalVI drops to 8th of 10 on mixed-batch data without batch labels; with batch labels totalVI graph iLISI goes 0.1→0.4 and ARI 0.37→0.62, Multigrate iLISI 0.22→0.43 and ARI 0.32→0.50. In spatial multi-omics SpatialGlue is best, but trails Harmony and STAligner on batch removal.
- <!-- ZH --> **非配对 RNA+ATAC 对角**:14 个方法中 9 个依赖从 ATAC 计算的 gene activity matrix(GAM),而 Signac/Seurat 的 GAM 函数都无法处理 500k 细胞,只有 GLUE 能跑;GLUE 在对齐准确性上全面最好,可用性、准确性与低深度鲁棒性综合第一。 <!-- EN --> **Unpaired RNA+ATAC diagonal**: 9 of 14 methods need an ATAC-derived gene activity matrix (GAM), and neither Signac's nor Seurat's GAM function handles 500k cells, so only GLUE runs; GLUE is best on alignment accuracy across all datasets and first overall on usability, accuracy and low-depth robustness.
- <!-- ZH --> **RNA+ATAC mosaic**:MultiVI、MIDAS、cobolt 嵌入准确性最好;利用配对细胞后,Seurat v5 Bridge 与 MultiVI 在 BMMC 上的 FOSCTTM(中位 3.7% / 3.8% vs GLUE 3.9%)与细胞类型匹配(L1 89.2% / 89.4% vs 86.3%;L2 84.2% / 82.9% vs 74.5%)优于 GLUE。MIDAS 的跨模态插补显著最好,接近给予 10% 目标模态数据的配对插补方法。 <!-- EN --> **RNA+ATAC mosaic**: MultiVI, MIDAS and cobolt best on embedding accuracy; leveraging paired cells, Seurat v5 Bridge and MultiVI beat GLUE on BMMC FOSCTTM (median 3.7% / 3.8% vs 3.9%) and cell-type matching (L1 89.2% / 89.4% vs 86.3%; L2 84.2% / 82.9% vs 74.5%). MIDAS cross-modality imputation is clearly best, approaching paired imputation methods given 10% of the target modality.
- <!-- ZH --> **RNA+ADT mosaic**:MIDAS 与 StabMap 嵌入准确性最好;MIDAS 插补全面领先(包括 totalVI);但 MIDAS 资源消耗巨大(最大数据 >10 h、80 GB),StabMap 约 2 分钟、5 GB。 <!-- EN --> **RNA+ADT mosaic**: MIDAS and StabMap best on embedding accuracy; MIDAS leads imputation (including over totalVI); but MIDAS is costly (>10 h and 80 GB on the largest set) vs StabMap (~2 min, 5 GB).
- <!-- ZH --> **重复性**:非深度方法输出完全一致;深度方法只有在源码固定随机种子时(uniPort、MultiVI、Multigrate、SCALEX)才稳定,其余部分指标 SD > 0.05。 <!-- EN --> **Reproducibility**: non-deep methods are fully deterministic; deep methods are stable only when the source code fixes a random seed (uniPort, MultiVI, Multigrate, SCALEX); others show SD > 0.05 on some metrics.

## 创新点 / Contributions
- <!-- ZH --> 迄今覆盖最广的多模态整合 benchmark(40 个算法、6 类任务、101 个数据集),并以 Registered Report 形式预注册协议。 <!-- EN --> The broadest multimodal integration benchmark to date (40 algorithms, six tasks, 101 datasets), pre-registered as a Registered Report.
- <!-- ZH --> 「伪非配对」设计:用配对数据的真实对应关系作为非配对/mosaic 任务的金标准。 <!-- EN --> The "pseudo-unpaired" design: paired data's true correspondences serve as gold standard for unpaired/mosaic tasks.
- <!-- ZH --> 把可扩展性、批次参数、重复运行稳定性纳入评价,并提供评测 Python 包、复现流水线与交互网站。 <!-- EN --> Includes scalability, batch-parameter effects and run-to-run stability, with an evaluation Python package, reproducible pipeline and interactive website.

## 局限 / Limitations
- <!-- ZH --> 空间多组学部分只有 3 个方法、数据稀缺;未覆盖 RNA+甲基化等其他表观模态。 <!-- EN --> Spatial multi-omics covers only 3 methods with scarce data; other epigenetic modalities (e.g. methylation) not covered.
- <!-- ZH --> 输入维度的影响未充分评估;硬件限制(GPU、内存)可能与用户环境不同。 <!-- EN --> Effect of input dimensionality not fully assessed; hardware limits may differ from users' setups.
- <!-- ZH --> 「伪非配对」数据来自同一批细胞,真实非配对数据(不同样本、不同供体)的难度可能被低估。 <!-- EN --> Pseudo-unpaired data come from the same cells, so the difficulty of truly unpaired data (different samples/donors) may be underestimated.
- <!-- ZH --> 数据以免疫/血液为主,肾只有一个 10x 肾癌 CITE-seq;本精读基于预印本。 <!-- EN --> Data are immune/blood-heavy, with kidney represented only by one 10x kidney-cancer CITE-seq set; this read is based on the preprint.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 Plan A,这是选择整合骨干的「方法地图」:我们的 95 例活检是 snRNA + snATAC(multiome,配对)+ Xenium(空间)+ H&E,且会与 KPMP/Lake 等外部非配对数据合并 —— 正好对应本文的配对 RNA+ATAC(推荐 Seurat v4 WNN、MultiVI)、非配对对角(GLUE)与 mosaic(MultiVI、Seurat v5 Bridge、MIDAS)三类任务。与 `kidney-multimodal-genomebiol-2026` 对照很有意思:后者在肾上发现 WNN 过度偏向 RNA、multi-spectral 更好 —— 说明在血液数据上得到的 SOTA 不一定迁移到肾,KidneyAnomalyBench 需要自己做一次肾上的整合选型。对「跨模态一致性区分伪影与疾病」,本文的「伪非配对 + 已知对应」设计可以直接借用:用 multiome 的真实配对作为金标准,量化整合本身引入的错配率(FOSCTTM),这就是跨模态不一致打分的**噪声底线** —— 低于这个底线的不一致不应被判为异常。另一个关键事实是「不给批次信息时 totalVI 等方法性能大幅下降」,意味着异常打分前必须显式建模批次。对 Plan B,「深度方法未固定随机种子时 SD > 0.05」直接对应 rerun stability:agent 用这些工具得出的结论需要多次重跑验证,这可以写入组学特异失败分类(「随机种子未固定导致结论不稳定」)。
<!-- EN --> For Plan A this is the "method map" for choosing an integration backbone. Our 95 biopsies are snRNA + snATAC (multiome, paired) + Xenium (spatial) + H&E, to be merged with external unpaired data such as KPMP/Lake — mapping exactly onto the paper's paired RNA+ATAC (recommends Seurat v4 WNN, MultiVI), unpaired diagonal (GLUE) and mosaic (MultiVI, Seurat v5 Bridge, MIDAS) tasks. The contrast with `kidney-multimodal-genomebiol-2026` is instructive: on kidney, WNN over-weights RNA and multi-spectral is better — SOTA from blood data does not necessarily transfer to kidney, so KidneyAnomalyBench needs its own kidney-specific integration choice. For "cross-modal agreement separates artefacts from disease", the "pseudo-unpaired + known correspondence" design is directly borrowable: use multiome's true pairing as gold standard to quantify the mismatch rate (FOSCTTM) introduced by integration itself — the **noise floor** for cross-modal disagreement scores; disagreement below that floor should not be called anomalous. Another key fact is that methods like totalVI degrade sharply without batch labels, so batch must be modelled explicitly before anomaly scoring. For Plan B, "deep methods without fixed seeds show SD > 0.05" maps directly to rerun stability: conclusions agents reach with these tools need repeated runs, and "unfixed random seed → unstable conclusion" belongs in the omics-specific failure taxonomy.

## 可复用资产 / Reusable assets
- <!-- ZH --> **评测指标 Python 包与作图脚本:** <!-- EN --> **Evaluation-metric Python package and figure scripts:**
<!-- ZH/EN --> <https://github.com/bm2-lab/SCMMI_Benchmark>
- <!-- ZH --> **全部方法的运行流水线:** <!-- EN --> **Pipeline for running all methods:**
<!-- ZH/EN --> <https://github.com/bm2-lab/SCMMIB_pipeline>
- <!-- ZH --> **交互式结果网站:** <!-- EN --> **Interactive results website:**
<!-- ZH/EN --> <https://bm2-lab.github.io/SCMMIB-reproducibility/>
- <!-- ZH --> **处理后的输入数据**(Figshare)与预注册协议(Springer Nature Figshare 26789572)。 <!-- EN --> **Processed inputs** (Figshare) and the pre-registered protocol (Springer Nature Figshare 26789572).
- <!-- ZH --> **预印本全文:** <!-- EN --> **Preprint full text:**
<!-- ZH/EN --> <https://doi.org/10.1101/2025.04.01.646578>

## 待读 / Follow-ups
- <!-- ZH --> MIDAS、GLUE、MultiVI、Seurat v5 bridge 原文。 <!-- EN --> The MIDAS, GLUE, MultiVI and Seurat v5 bridge papers.
- <!-- ZH --> 文中引用的 14 方法跨模态预测 benchmark(未包含 MIDAS)。 <!-- EN --> The cited 14-method cross-modality prediction benchmark (which omitted MIDAS).
- <!-- ZH --> 用 scATAC 跨模态参考做新细胞类型发现(`scatac-novel-genomeres-2026`)。 <!-- EN --> Novel cell-type discovery in scATAC via cross-modal references (`scatac-novel-genomeres-2026`).

## 引用 / Cite
```bibtex
@article{Fu_2025_MultimodalBench, title={Benchmarking single-cell multi-modal data integrations}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02737-9}, DOI={10.1038/s41592-025-02737-9}, number={11}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Fu, Shaliu and Wang, Shuguang and Si, Duanmiao and Li, Gaoyang and Gao, Yawei and Liu, Qi}, year={2025}, month=July, pages={2437–2448} }
```
