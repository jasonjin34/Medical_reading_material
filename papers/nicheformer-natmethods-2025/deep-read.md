# Nicheformer: a foundation model for single-cell and spatial omics

> **Bibkey** `Tejada_Lapuerta_2025` · **Venue** Nature Methods (2025) · **Category** foundation · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02814-z>
> `status: complete` — 基于 Europe PMC 开放全文(PMC12695652)主文精读;Methods 与 Extended Data 只部分参考。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> Nicheformer 是一个 49.3M 参数的 Transformer 基础模型,在 SpatialCorpus-110M(57.06M 解离细胞 + 53.8M 成像空间细胞,人和小鼠,73 个组织)上用排序基因 token + 物种/模态/技术上下文 token 预训练;在新设计的空间任务(niche/区域标签、邻域组成、邻域密度)上,linear probing 与微调都优于 Geneformer、scGPT、UCE、CellPLM、scVI、PCA,并能把空间上下文迁移到 scRNA-seq 上。
<!-- EN --> Nicheformer is a 49.3M-parameter transformer foundation model pretrained on SpatialCorpus-110M (57.06M dissociated + 53.8M image-based spatial cells, human and mouse, 73 tissues) with ranked gene tokens plus species/modality/technology context tokens. On newly designed spatial tasks (niche/region labels, neighbourhood composition, neighbourhood density) both linear probing and fine-tuning beat Geneformer, scGPT, UCE, CellPLM, scVI and PCA, and it transfers spatial context onto scRNA-seq.

## 研究问题 / Problem
<!-- ZH --> 现有单细胞基础模型只在解离数据上训练,忽略细胞的空间关系(CellPLM 例外,但数据量小且未在空间任务上微调)。成像空间转录组已达到可大规模学习的程度,问题是能否学到一个「空间感知」的细胞表示,并把空间信息迁移到海量的非空间 scRNA-seq 上。
<!-- EN --> Existing single-cell foundation models train on dissociated data only and ignore spatial relationships (CellPLM is an exception, but small and not fine-tuned on spatial tasks). Image-based spatial transcriptomics is now large enough to learn from at scale; can a spatially aware cell representation be learned and transferred to the vast body of non-spatial scRNA-seq?

## 方法 / Method
<!-- ZH --> **表示**:人鼠直系同源 + 物种特异基因构成 20,310 个 gene token(16,981 直系同源、151 小鼠特异、3,178 人特异);每个细胞按「相对语料中该技术非零均值」排序成 token 序列(Geneformer 式 rank encoding),技术特异均值分别对解离、MERFISH、Xenium、CosMx、ISS 计算以缓解技术偏差;加入物种、模态、技术上下文 token。**架构**:上下文长度 1,500,12 层 encoder,16 头,FFN 1,024,512 维嵌入,49.3M 参数;预训练目标为(掩码)细胞重建。预训练**不使用空间坐标**,只用表达。**下游**:linear probing(冻结嵌入 + 线性头)与微调;任务包括 niche / 区域分类(含不确定性)、以固定半径定义的邻域组成(平均 10/20/50/100 个邻居)与邻域密度回归,以及空间→解离的标签迁移。另做 attention 分析(层级分工;MERFISH 小鼠脑 AVPV 中性别二态基因的注意力差异)与预训练数据消融(仅解离、仅人、仅鼠)。
<!-- EN --> **Representation**: 20,310 gene tokens from human–mouse orthologues plus species-specific genes (16,981 orthologous, 151 mouse-specific, 3,178 human-specific); each cell becomes a token sequence ranked relative to the technology-specific non-zero mean in the corpus (Geneformer-style rank encoding), with separate means for dissociated, MERFISH, Xenium, CosMx and ISS to counter technology bias; plus species, modality and technology context tokens. **Architecture**: context 1,500, 12 encoder layers, 16 heads, FFN 1,024, 512-d embedding, 49.3M parameters; pretrained on (masked) cell reconstruction. Pretraining uses **no spatial coordinates**, expression only. **Downstream**: linear probing (frozen embedding + linear head) and fine-tuning; tasks include niche/region classification (with uncertainty), fixed-radius neighbourhood composition (on average 10/20/50/100 neighbours) and density regression, and spatial→dissociated label transfer. Also attention analysis (layer specialisation; sex-dimorphic gene attention in the MERFISH mouse-brain AVPV) and pretraining-data ablations (dissociated-only, human-only, mouse-only).

## 数据 / Data
<!-- ZH --> SpatialCorpus-110M:解离部分基于 CELLxGENE Census(33.47M)并新增 180 个数据集(GEO、sfaira、HCA),来自 6,000+ 供体;空间部分为 MERFISH、Xenium、CosMx、ISS,15 个组织、158 个个体、10,600+ 切片,其中脑占 60.46%(32.1M)、肺 9.95%;55.23% 无注释;健康 64.07%、癌症 31.98%。数据未整合,保留原始输入。下游评测:MERFISH 小鼠脑(17 区域、8 niche)、CosMx 人肝与人肺、Xenium 人肺与结肠(健康 vs 腺癌)、小鼠运动皮层 scRNA-seq。
<!-- EN --> SpatialCorpus-110M: the dissociated part builds on CELLxGENE Census (33.47M) plus 180 added datasets (GEO, sfaira, HCA) from 6,000+ donors; the spatial part covers MERFISH, Xenium, CosMx and ISS across 15 tissues, 158 individuals and 10,600+ sections — brain 60.46% (32.1M), lung 9.95%; 55.23% unannotated; 64.07% healthy, 31.98% cancer. Datasets are not integrated; raw inputs are kept. Downstream: MERFISH mouse brain (17 regions, 8 niches), CosMx human liver and lung, Xenium human lung and colon (healthy vs adenocarcinoma), mouse motor-cortex scRNA-seq.

## 主要结果 / Key results
- <!-- ZH --> **预训练消融**:只用解离数据(即使是空间数据量的三倍)在下游空间任务上显著更差;只用单一物种的模型在另一物种上表现差 —— 在细胞数相同时,数据多样性是关键(ANOVA,FDR 校正后显著)。 <!-- EN --> **Pretraining ablations**: dissociated-only pretraining (even 3× the spatial data volume) is significantly worse on spatial tasks; single-species models do poorly on the other species — at equal cell counts, data diversity is what matters (ANOVA, FDR-significant).
- <!-- ZH --> **niche / 区域标签**:MERFISH 小鼠脑留出切片上,微调 Nicheformer macro F1 最高;但多主成分 PCA 的 linear probing 与 Nicheformer linear probing 基本持平,在区域预测上甚至超过它。CosMx 肝上 linear probing 不如 scVI/PCA(肝在语料中稀少),扩展预训练后改善。 <!-- EN --> **Niche/region labels**: on held-out MERFISH mouse-brain sections, fine-tuned Nicheformer has the best macro F1; but PCA with many components roughly matches Nicheformer linear probing and even beats it on region prediction. On CosMx liver, linear probing trails scVI/PCA (liver is rare in the corpus), improving with extended pretraining.
- <!-- ZH --> **空间→解离迁移**:从 33 类 MERFISH 细胞类型中正确选出运动皮层相关的 9 类,整体低不确定性;深层谷氨酸能神经元有误分。 <!-- EN --> **Spatial→dissociated transfer**: correctly selects the 9 motor-cortex cell types out of 33 MERFISH types with low overall uncertainty; some deep-layer glutamatergic neurons are misassigned.
- <!-- ZH --> **邻域组成**:在脑、肝、肺三个器官、四种邻域尺度上,微调 Nicheformer 的 MAE 系统性最低;Nicheformer linear probing 次之,优于 Geneformer、scGPT、UCE、CellPLM、scVI、PCA。误差与细胞类型丰度、区域特异性强相关(稀有、分布复杂的中脑/下丘脑类型最差)。肝的大半径下,在语料子集上训练的 scVI 与微调 Nicheformer 持平。 <!-- EN --> **Neighbourhood composition**: across brain, liver and lung at four scales, fine-tuned Nicheformer has systematically lowest MAE; Nicheformer linear probing is next, beating Geneformer, scGPT, UCE, CellPLM, scVI and PCA. Error tracks cell-type abundance and regional specificity (rare, regionally diverse midbrain/hypothalamic types are worst). At large radii in liver, scVI trained on a corpus subset matches fine-tuned Nicheformer.
- <!-- ZH --> **邻域密度**:Xenium 肺与结肠中癌症切片平均邻域密度更高(结肠 12.3 vs 10.7,肺 12.1 vs 10.7);scVI 与 PCA 的 linear probing R² 为负,Nicheformer 在 MAE 与 R² 上更好,并能定位肿瘤区高密度。 <!-- EN --> **Neighbourhood density**: cancer sections have higher mean neighbourhood density in Xenium (colon 12.3 vs 10.7; lung 12.1 vs 10.7); scVI and PCA linear probing give negative R², while Nicheformer is better on MAE and R² and localises dense tumour regions.

## 创新点 / Contributions
- <!-- ZH --> 第一个在大规模解离 + 成像空间数据上联合预训练的单细胞基础模型,及其公开语料 SpatialCorpus-110M。 <!-- EN --> The first single-cell foundation model jointly pretrained on large-scale dissociated + image-based spatial data, with the public SpatialCorpus-110M.
- <!-- ZH --> 一组新的「空间感知」下游任务(niche/区域标签、邻域组成与密度)作为基准。 <!-- EN --> A new set of spatially aware downstream tasks (niche/region labels, neighbourhood composition and density) as a benchmark.
- <!-- ZH --> 证明仅解离数据无法学到空间变异;技术特异的 rank 归一化处理平台偏差。 <!-- EN --> Shows dissociated data alone cannot capture spatial variation; technology-specific rank normalisation handles platform bias.

## 局限 / Limitations
- <!-- ZH --> 性能依赖细胞/组织在语料中的丰度;语料以脑为主(60%),**未见肾**数据被重点评测。 <!-- EN --> Performance depends on cell/tissue abundance in the corpus; the corpus is brain-dominated (60%), and **kidney** is not among the evaluated tissues.
- <!-- ZH --> 预训练不显式使用空间坐标/邻域图;元数据 token 被排除在最终嵌入外,可能损失表达能力。 <!-- EN --> Pretraining does not use spatial coordinates or neighbour graphs; metadata tokens are excluded from the final embedding, possibly limiting expressivity.
- <!-- ZH --> 部分任务上 PCA / scVI 是强竞争者(linear probing 层面),作者自己的任务集也承认不够全面。 <!-- EN --> PCA / scVI are strong competitors on some tasks (at the linear-probing level); the authors concede their task set is not comprehensive.
- <!-- ZH --> 可解释性(attention 分析)仍是初步的。 <!-- EN --> Interpretability (attention analysis) is preliminary.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 detect → model → revert 的 **model** 阶段,Nicheformer 提供了把「细胞」与「它的邻域」放在同一表示里的路径:我们的 95 例活检中 snRNA/snATAC 是解离的,只有 Xenium 带空间 —— Nicheformer 的空间→解离迁移,原则上可以给 snRNA 细胞推断「所处 niche / 邻域组成」,从而在没有空间测量的样本上也能定义空间层面的异常(例如损伤小管周围免疫浸润的邻域)。对 Plan A 的异常检测有两点具体价值:**(1) 邻域组成/密度预测误差本身可作为异常信号** —— 若一个细胞的表达预测出的邻域与实测(Xenium)邻域显著不符,这是一种「表达–空间」跨模态不一致;**(2) 技术特异 rank 归一化**直接处理了 Xenium vs snRNA 的平台偏差,与本仓库 `kidney-multimodal-genomebiol-2026` 的协议效应结论互补。但需警惕:语料以脑为主、肾稀缺,作者在肝上已观察到 linear probing 不如 scVI/PCA,肾上很可能需要扩展预训练;且 PCA 在多个任务上是强基线 —— 与 `scfm-zeroshot-genomebiol-2025` 的结论一致,评测时必须带上 PCA/scVI。对 Plan B,「Nicheformer 预测该 snRNA 细胞位于某 niche」这类推断性空间 claim 需要附带不确定性(本文提供了分类不确定性),是 verifier 校准的好用例。
<!-- EN --> For the **model** stage of detect → model → revert, Nicheformer offers a way to put a cell and its neighbourhood in one representation. In our 95 biopsies snRNA/snATAC are dissociated and only Xenium is spatial; Nicheformer's spatial→dissociated transfer could in principle infer the niche/neighbourhood composition of snRNA cells, letting us define spatial-level anomalies (e.g. immune-infiltrated neighbourhoods around injured tubules) even in samples without spatial measurements. Two concrete uses for Plan A anomaly detection: **(1) neighbourhood composition/density prediction error is itself an anomaly signal** — if the neighbourhood predicted from a cell's expression disagrees with its measured (Xenium) neighbourhood, that is an expression–space cross-modal disagreement; **(2) technology-specific rank normalisation** directly addresses Xenium-vs-snRNA platform bias, complementing the protocol-effect findings in `kidney-multimodal-genomebiol-2026`. Caveats: the corpus is brain-dominated and kidney-poor; the authors already see linear probing trail scVI/PCA on liver, so kidney likely needs extended pretraining; and PCA is a strong baseline on several tasks — consistent with `scfm-zeroshot-genomebiol-2025`, PCA/scVI must be in any evaluation. For Plan B, inferential spatial claims like "Nicheformer places this snRNA cell in niche X" should carry uncertainty (the paper provides classification uncertainty) — a good calibration test case for the verifier.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码与模型:** <!-- EN --> **Code and model:**
<!-- ZH/EN --> <https://github.com/theislab/nicheformer>
- <!-- ZH --> **数据处理代码:** <!-- EN --> **Data-processing code:**
<!-- ZH/EN --> <https://github.com/theislab/nicheformer-data>
- <!-- ZH --> **SpatialCorpus-110M:** <!-- EN --> **SpatialCorpus-110M:**
<!-- ZH/EN --> <https://huggingface.co/datasets/theislab/SpatialCorpus-110M>
- <!-- ZH --> **空间下游任务定义**:固定半径邻域组成/密度、niche/区域标签 + 不确定性 —— 可直接移植到肾 Xenium。 <!-- EN --> **Spatial downstream task definitions**: fixed-radius neighbourhood composition/density, niche/region labels + uncertainty — directly portable to kidney Xenium.

## 待读 / Follow-ups
- <!-- ZH --> CellPLM(另一个使用空间数据的单细胞基础模型)。 <!-- EN --> CellPLM (the other single-cell foundation model using spatial data).
- <!-- ZH --> 空间异常检测基线 STANDS(`spatial-natcommun-2024`),看能否用 Nicheformer 嵌入替换其特征。 <!-- EN --> The spatial anomaly-detection baseline STANDS (`spatial-natcommun-2024`) — could Nicheformer embeddings replace its features?
- <!-- ZH --> Xenium 分割/伪影相关工作(`xenium-split-natmethods-2026`、`ovrlpy-natbiotech-2026`),邻域计算会受分割误差影响。 <!-- EN --> Xenium segmentation/artefact work (`xenium-split-natmethods-2026`, `ovrlpy-natbiotech-2026`) — neighbourhood computation is sensitive to segmentation errors.

## 引用 / Cite
```bibtex
@article{Tejada_Lapuerta_2025, title={Nicheformer: a foundation model for single-cell and spatial omics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02814-z}, DOI={10.1038/s41592-025-02814-z}, number={12}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Tejada-Lapuerta, Alejandro and Schaar, Anna C. and Gutgesell, Robert and Palla, Giovanni and Halle, Lennard and Minaeva, Mariia and Vornholz, Larsen and Dony, Leander and Drummer, Francesca and Richter, Till and Bahrami, Mojtaba and Theis, Fabian J.}, year={2025}, month=Oct, pages={2525–2538} }
```
