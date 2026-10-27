# Robust annotation and discovery of novel cell types in single-cell ATAC-seq data through cross-modal reference alignment

> **Bibkey** `Cao_2026` · **Venue** Genome Research 36(10) (2026) · **Category** single-cell · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1101/gr.281981.126>
> `status: abstract-only` — 全文在 Genome Research 付费墙后(Europe PMC 无开放全文,未找到预印本);以下仅基于摘要(PubMed 42665446)与书目信息,**不含任何正文数值**。把 PDF 放到本文件夹的 `source.pdf` 后可补全。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> CARA 是一个跨模态贝叶斯框架,把 scRNA-seq 参照中的细胞类型知识迁移到 scATAC-seq:在 scRNA 上预训练,在目标 scATAC 上做半监督学习,配合分布对齐、动态类别加权和新细胞类型检测,同时完成注释、批次校正和**识别参照中不存在的(新的、稀有的或异常的)细胞群**。
<!-- EN --> CARA is a cross-modal Bayesian framework that transfers cell-type knowledge from an scRNA-seq reference to scATAC-seq: pretraining on scRNA, semi-supervised learning on the target scATAC, plus distribution alignment, dynamic class weighting and novel-type detection — jointly annotating, batch-correcting and **flagging populations absent from the reference (novel, rare or aberrant)**.

## 研究问题 / Problem
<!-- ZH --> scATAC-seq 注释比 scRNA-seq 难:数据极度稀疏、维度高、带标签的 scATAC 参照稀缺,且数据集间批次效应明显。需要一种不依赖大量 scATAC 标签的注释方法,同时能发现参照外的细胞类型。
<!-- EN --> scATAC-seq annotation is harder than scRNA-seq: extreme sparsity, high dimensionality, scarce labelled scATAC references and strong batch effects across datasets. A method is needed that does not rely on many scATAC labels and can also discover cell types outside the reference.

## 方法 / Method
<!-- ZH --> 据摘要:(1) 在 scRNA-seq 参照上预训练;(2) 在目标 scATAC-seq 上半监督学习;(3) 分布对齐(跨模态 / 跨批次);(4) 动态类别加权;(5) 新细胞类型检测——利用**多维不确定性**与**潜空间聚类**识别参照细胞类型空间之外的群体;(6) 采用「组学特异的生成框架」,因此可推广到单细胞 DNA 甲基化等以基因为中心的模态。具体模型结构、不确定性如何计算、阈值如何定,摘要中没有,**需要读全文**。
<!-- EN --> Per the abstract: (1) pretraining on an scRNA-seq reference; (2) semi-supervised learning on target scATAC-seq; (3) distribution alignment (cross-modal / cross-batch); (4) dynamic class weighting; (5) novel-type detection — using **multidimensional uncertainty** and **latent-space clustering** to find populations outside the reference cell-type space; (6) an omic-specific generative framework, which lets it generalize to gene-centric modalities such as single-cell DNA methylation. Model architecture, how uncertainty is computed and how thresholds are set are not in the abstract — **full text needed**.

## 数据 / Data
<!-- ZH --> 摘要只说「多个基准数据集」,另有造血分化轨迹重建和单细胞 DNA 甲基化数据的应用;具体数据集未知(付费墙)。
<!-- EN --> The abstract mentions only "diverse benchmark data sets", plus a haematopoietic differentiation trajectory and single-cell DNA methylation applications; specific datasets are unknown (paywall).

## 主要结果 / Key results
- <!-- ZH --> 跨多个基准数据集持续优于基线方法,对批次效应稳健(摘要原话,**无具体数值**)。 <!-- EN --> Consistently outperforms baselines across diverse benchmarks and is robust to batch effects (abstract claim, **no numbers available**).
- <!-- ZH --> 跨模态对齐保留了细粒度谱系结构,可重建造血分化轨迹。 <!-- EN --> Cross-modal alignment preserves fine-grained lineage structure, enabling reconstruction of the haematopoietic differentiation trajectory.
- <!-- ZH --> 能识别参照外的新的、稀有的或异常群体,作为后续生物学验证与**扰动**的候选。 <!-- EN --> Identifies novel, rare or aberrant populations outside the reference as candidates for biological validation and **perturbation**.
- <!-- ZH --> 在单细胞 DNA 甲基化数据上同样能准确迁移知识并检测新细胞类型。 <!-- EN --> Transfers knowledge accurately and detects novel types in single-cell DNA methylation data as well.

## 创新点 / Contributions
- <!-- ZH --> 把注释、批次校正、新类型检测统一到一个跨模态(RNA→ATAC)框架中。 <!-- EN --> Unifies annotation, batch correction and novel-type detection in one cross-modal (RNA→ATAC) framework.
- <!-- ZH --> 用多维不确定性 + 潜空间聚类做开放集识别,而非只用分类置信度。 <!-- EN --> Open-set recognition via multidimensional uncertainty plus latent-space clustering, not classification confidence alone.
- <!-- ZH --> 可推广到 DNA 甲基化等其他表观模态。 <!-- EN --> Generalizes to other epigenomic modalities such as DNA methylation.

## 局限 / Limitations
- <!-- ZH --> **本条目仅基于摘要**,无法评估实验设计、基线选择和数值。 <!-- EN --> **This entry rests on the abstract only**; experimental design, baselines and numbers cannot be assessed.
- <!-- ZH --> 从摘要推断:依赖 scRNA 参照的完整性,且 RNA→ATAC 的特征映射(如 gene activity)本身有信息损失——需全文确认作者如何处理。 <!-- EN --> Inferred from the abstract: depends on the completeness of the scRNA reference, and the RNA→ATAC feature bridge (e.g. gene activity) loses information — the full text must confirm how this is handled.
- <!-- ZH --> 「新的 / 稀有 / 异常」群体只是候选,摘要未提湿实验验证。 <!-- EN --> "Novel / rare / aberrant" populations are candidates only; the abstract mentions no wet-lab validation.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是本批次里唯一面向 **scATAC** 的异常/新类型检测方法,对 **课题 1** 有直接位置:肾脏多模态设计常包含 snATAC,而 KPMP / Lake atlas 的 snRNA 参照远比 ATAC 参照完善——CARA 的「RNA 参照 → ATAC 目标」迁移正好对应这种不对称。更关键的是**跨模态一致性**:如果 snRNA 侧(mapQC / Milo / MrVI)和 snATAC 侧(CARA 的「参照外」判定)在同一批细胞上都给出异常,这比单模态信号更可能是真实疾病状态;只在一个模态出现则更可能是 artifact(如 snRNA 的环境 RNA,或 ATAC 的低 TSS 富集)。CARA 的「多维不确定性」也可与 conformal 注释(`conformal-scrna-bioinformatics-2025`)的统计保证对比。对 **课题 2**:摘要把「异常群体」直接称为「扰动候选」——这是一个需要 verifier 检查的推理跳跃(从「参照外」到「有因果意义的可扰动靶点」)。读到全文前不宜作为基线依据。
<!-- EN --> This is the only **scATAC** anomaly/novel-type method in this batch and has a direct slot in **Topic 1**: multi-modal kidney designs often include snATAC, while KPMP / Lake-atlas snRNA references are far more mature than ATAC ones — CARA's "RNA reference → ATAC target" transfer matches that asymmetry. More importantly, **cross-modal agreement**: if the snRNA side (mapQC / Milo / MrVI) and the snATAC side (CARA's "out-of-reference" call) both flag the same cells, that is more likely a real disease state than either signal alone; anomaly in only one modality is more likely artifact (e.g. ambient RNA in snRNA, low TSS enrichment in ATAC). CARA's "multidimensional uncertainty" can also be contrasted with the statistical guarantees of conformal annotation (`conformal-scrna-bioinformatics-2025`). For **Topic 2**: the abstract calls aberrant populations "candidates for perturbation" — an inferential leap (from "out-of-reference" to "causally meaningful, perturbable target") that a verifier should check. Not to be used as a baseline until the full text is read.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码**:摘要未给出代码链接;待全文确认(未找到公开仓库,不臆测)。 <!-- EN --> **Code**: no link in the abstract; to be confirmed from the full text (no public repo found; not guessed).
- <!-- ZH --> **摘要来源**:PubMed 42665446。 <!-- EN --> **Abstract source**: PubMed 42665446.
<!-- ZH/EN --> <https://pubmed.ncbi.nlm.nih.gov/42665446/>

## 待读 / Follow-ups
- <!-- ZH --> **获取全文 PDF**(机构访问),补全方法、数据集与数值。 <!-- EN --> **Get the full-text PDF** (institutional access) to fill in methods, datasets and numbers.
- <!-- ZH --> 同期 Genome Research 的 RNA→ATAC 标签迁移方法 scSHEFT(10.1101/gr.280410.125),以及 SemiLT(10.1002/advs.202507846),作为对比。 <!-- EN --> Contemporary RNA→ATAC label-transfer methods for comparison: scSHEFT in Genome Research (10.1101/gr.280410.125) and SemiLT (10.1002/advs.202507846).
- <!-- ZH --> 在 KPMP snRNA → 待测肾样本 snATAC 上测试新类型检测。 <!-- EN --> Test novel-type detection from KPMP snRNA → snATAC of the kidney samples to be tested.

## 引用 / Cite
```bibtex
@article{Cao_2026, title={Robust annotation and discovery of novel cell types in single-cell ATAC-seq data through cross-modal reference alignment}, volume={36}, ISSN={1549-5469}, url={http://dx.doi.org/10.1101/gr.281981.126}, DOI={10.1101/gr.281981.126}, number={10}, journal={Genome Research}, publisher={Cold Spring Harbor Laboratory}, author={Cao, Lan and Zhang, Wenhao and Zhou, Feng and He, Yushuang and Long, Yongyu and Chen, Shengquan and Wang, Ying}, year={2026}, month=Aug, pages={2037–2052} }
```
