# A visual–omics foundation model to bridge histopathology with spatial transcriptomics

> **Bibkey** `Chen_2025_Loki` · **Venue** Nature Methods (2025) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02707-1>
> `status: complete` — 基于 Europe PMC 开放全文(PMC12240810)主文精读;Methods 与 Extended Data 只部分参考。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> OmiCLIP 把每个 Visium spot 的转录组写成「按表达量排序的基因符号句子」,与对应 H&E patch 做 CLIP/CoCa 式对比学习(ST-bank:2.2M 对、1,007 个样本、32 个器官);在此之上的 Loki 平台提供五个模块 —— 组织对齐、组织注释、细胞类型分解、图像↔转录组检索、从 H&E 预测 ST 表达。
<!-- EN --> OmiCLIP writes each Visium spot's transcriptome as a "sentence" of gene symbols ranked by expression and contrastively aligns it with the matching H&E patch in a CLIP/CoCa setup (ST-bank: 2.2M pairs, 1,007 samples, 32 organs); the Loki platform built on top offers five modules — tissue alignment, tissue annotation, cell-type decomposition, image↔transcriptome retrieval and ST expression prediction from H&E.

## 研究问题 / Problem
<!-- ZH --> 病理视觉–语言基础模型(PLIP、CONCH)用的是文字描述,缺少分子信息;而把组织学与组学结合的方法大多是任务专用的,没有一个统一的多模态模型与基础设施能同时处理测序数据与病理图像。
<!-- EN --> Pathology vision–language foundation models (PLIP, CONCH) use text captions that lack molecular insight, while methods combining histology with omics are task-specific; there is no unified multimodal model and infrastructure that handles sequencing and pathology images together.

## 方法 / Method
<!-- ZH --> **数据**:ST-bank —— 113 项研究、1,007 个 10x Visium 样本、约 2.2M 组织 patch 与配对转录组,覆盖 32 个器官,包含健康、癌症、心衰、阿尔茨海默病等状态;QC 保留高分辨率 H&E。**表示**:Ensembl ID 转基因符号、去除 housekeeping 基因,按表达从高到低排序成文本句子(借鉴 GenePT / Cell2Sentence;rank-based 思路借鉴 Geneformer / scFoundation,用以减轻批次效应)。**模型**:基于 CoCa(图像编码器 + 文本编码器 + 多模态融合解码器)微调,对比损失对齐配对的图像/转录组嵌入(768 维)。**Loki 模块**:Align(OmiCLIP 嵌入 + 改进的 coherent point drift,支持 ST↔ST、H&E↔ST);Annotate(H&E patch 与组织特异 bulk RNA-seq 或 marker 基因句子的余弦相似度;可与 PLIP 的文本相似度平均);Decompose(把 Tangram 的优化目标作用在 OmiCLIP 嵌入而非原始表达上,以 scRNA-seq 为参考,支持 ST 模式与纯图像模式,另加 NMS 风格后处理);Retrieve(用图像嵌入在 ST-bank 中检索最相似的转录组);PredEx(以查询图像与参考 ST spots 的相似度为权重,对参考表达做加权和)。多数任务默认在目标切片上微调。
<!-- EN --> **Data**: ST-bank — 113 studies, 1,007 10x Visium samples, ~2.2M tissue patches with paired transcriptomes across 32 organs, spanning healthy, cancer, heart failure and Alzheimer's states; QC keeps high-resolution H&E. **Representation**: Ensembl IDs mapped to symbols, housekeeping genes removed, genes ranked high→low into a text sentence (after GenePT / Cell2Sentence; the rank-based idea follows Geneformer / scFoundation to dampen batch effects). **Model**: fine-tuned from CoCa (image encoder + text encoder + multimodal fusion decoder), contrastive loss aligning paired image/transcriptome embeddings (768-d). **Loki modules**: Align (OmiCLIP embeddings + adapted coherent point drift; ST↔ST and H&E↔ST); Annotate (cosine similarity between H&E patches and tissue-specific bulk RNA-seq or marker-gene sentences; can be averaged with PLIP's text similarity); Decompose (Tangram's objective applied to OmiCLIP embeddings rather than raw expression, scRNA-seq as reference, in ST mode or image-only mode, plus NMS-style refinement); Retrieve (image embedding → nearest transcriptomes in ST-bank); PredEx (similarity-weighted sum of reference-spot expression). Most tasks fine-tune on the target slide by default.

## 数据 / Data
<!-- ZH --> 训练:ST-bank(见上)。评测:与 22 个 SOTA 方法比较,覆盖 5 个模拟数据集、19 个公开实验数据集、4 个自有数据集,包括 8 张相邻小肠切片、2 张相邻卵巢癌肉瘤切片、乳腺癌 Visium + Xenium、自有 TNBC Xenium、结直肠癌 Visium-HD、小鼠脑皮层、CRC7K / WSSS4LUAD / PatchCamelyon / LC25000、39 例正常心脏 ST 等。
<!-- EN --> Training: ST-bank (above). Evaluation: against 22 SOTA methods on 5 simulated, 19 public and 4 in-house datasets — 8 adjacent small-intestine sections, 2 adjacent ovarian carcinosarcoma sections, breast-cancer Visium + Xenium, in-house TNBC Xenium, colorectal cancer Visium-HD, mouse brain cortex, CRC7K / WSSS4LUAD / PatchCamelyon / LC25000, 39 normal-heart ST samples, and more.

## 主要结果 / Key results
- <!-- ZH --> **表示质量**:在 95 个有专家注释的 ST-bank 样本上,对比学习后的 Calinski–Harabasz 分数显著提升(P < 0.001);图像嵌入的聚类优于 UNI 与 GigaPath。对加噪图像与降采样测序深度(11,792 → 4,512 → 615 UMI)稳健。 <!-- EN --> **Representation**: on 95 expert-annotated ST-bank samples, Calinski–Harabasz scores rise significantly after contrastive learning (P < 0.001); image embeddings cluster better than UNI and GigaPath. Robust to noised images and downsampled depth (11,792 → 4,512 → 615 UMI).
- <!-- ZH --> **Align**:小肠 8 切片中位 PCC 0.67–0.80(image→ST)/0.62–0.83(ST→ST),PASTE −0.25–0.39、GPSA 0.27–0.56;卵巢癌肉瘤中位 PCC 0.88/0.86,PASTE 0.26、GPSA 0.43、CAST 0.71;Xenium↔Visium 平均对齐误差 0.08 mm。从头训练只有 PCC 0.53。图像+转录组平均嵌入并不优于单模态。 <!-- EN --> **Align**: small intestine, median PCC 0.67–0.80 (image→ST) / 0.62–0.83 (ST→ST) vs PASTE −0.25–0.39 and GPSA 0.27–0.56; ovarian carcinosarcoma, median PCC 0.88/0.86 vs PASTE 0.26, GPSA 0.43, CAST 0.71; Xenium↔Visium mean error 0.08 mm. Training from scratch reaches only PCC 0.53. Averaging image + transcriptome embeddings does not beat a single modality.
- <!-- ZH --> **Annotate(marker 基因零样本)**:四个病理基准上 F1 0.59–0.96,OpenAI CLIP 0.03–0.34,PLIP 0.5–0.93;Loki+PLIP 平均相似度在四个数据集上都最好(CRC7K 召回率 93%)。 <!-- EN --> **Annotate (zero-shot via marker genes)**: F1 0.59–0.96 on four pathology benchmarks vs OpenAI CLIP 0.03–0.34 and PLIP 0.5–0.93; averaging Loki+PLIP is best on all four (93% recall on CRC7K).
- <!-- ZH --> **Decompose**:TNBC Xenium 基准上 ST 模式与图像模式综合分 1.32/1.11 排前二,Tangram、CARD、Cell2location、RCTD 等 0.87 至 −1.82;把嵌入换成 scGPT / scFoundation / Geneformer 分别排第 6/8/9。 <!-- EN --> **Decompose**: on the TNBC Xenium benchmark, ST and image modes score 1.32/1.11 (top two) vs 0.87 to −1.82 for Tangram, CARD, Cell2location, RCTD etc.; swapping in scGPT / scFoundation / Geneformer embeddings ranks 6th/8th/9th.
- <!-- ZH --> **Retrieve**:肾验证样本 Recall@5% 0.173、Recall@10% 0.297(约为 CLIP/PLIP 的 3.2 倍);独立测试集 Recall@5% 0.117、@10% 0.208。 <!-- EN --> **Retrieve**: kidney validation Recall@5% 0.173, Recall@10% 0.297 (~3.2× CLIP/PLIP); independent test Recall@5% 0.117, @10% 0.208.
- <!-- ZH --> **PredEx**:39 例正常心脏中,MSE 最优 28/39、PCC 最优 16/39(对比 Hist2ST、HisToGene、BLEEP、mclSTExp),且不需要重训。 <!-- EN --> **PredEx**: on 39 normal-heart samples, best MSE in 28/39 and best PCC in 16/39 vs Hist2ST, HisToGene, BLEEP, mclSTExp — without retraining.

## 创新点 / Contributions
- <!-- ZH --> 把「转录组即文本」的思路接入 CLIP 式病理基础模型,首次用公开 ST 规模化预训练视觉–组学对齐。 <!-- EN --> Plugs "transcriptome-as-text" into a CLIP-style pathology foundation model — the first large-scale vision–omics pretraining from public ST.
- <!-- ZH --> 一个共享嵌入空间支撑五类下游任务,允许用 bulk RNA-seq、scRNA-seq 乃至 marker 基因列表去解读 H&E。 <!-- EN --> One shared embedding space powers five downstream tasks, letting bulk RNA-seq, scRNA-seq or even marker lists interpret H&E.
- <!-- ZH --> 公开 ST-bank、模型权重与代码。 <!-- EN --> Releases ST-bank, weights and code.

## 局限 / Limitations
- <!-- ZH --> 预训练规模(百万级)远小于通用 CLIP;罕见病况在 ST-bank 中代表性不足,对齐/分解默认需要在目标切片上微调。 <!-- EN --> Million-scale pretraining is far below general CLIP; rare conditions are underrepresented, so alignment/decomposition default to fine-tuning on the target slide.
- <!-- ZH --> 对比式、非生成式:PredEx 本质是对参考 spots 的检索加权,无法生成真正新的表达谱。 <!-- EN --> Contrastive, not generative: PredEx is similarity-weighted retrieval over reference spots, not true expression generation.
- <!-- ZH --> 只用 top-ranked 基因名,丢失绝对表达量;仅基于 Visium(spot 级,~55 μm),非单细胞分辨率。 <!-- EN --> Uses only top-ranked gene names, losing absolute magnitude; Visium-only (spot level, ~55 μm), not single-cell resolution.
- <!-- ZH --> 部分评测(如 Retrieve)缺乏真正的转录组 ground truth,以图像相似度代理;双模态融合时一个模态主导会抵消收益。 <!-- EN --> Some evaluations (e.g. Retrieve) lack transcriptomic ground truth and use image similarity as proxy; if one modality dominates, fusion gains vanish.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 detect → model → revert,OmiCLIP 提供的是**H&E 与表达共享的嵌入空间**,这对课题 1 的「跨模态一致性」最关键:同一块组织的 H&E 嵌入与转录组嵌入若在共享空间中相互「检索不到」,就是一个天然的跨模态不一致信号;反之二者都偏离健康参考才更可能是真实病变。若有配对的 H&E 与单细胞分辨率空间组学数据,可以用 Loki Align(Xenium→pseudo-Visium 的流程本文已示范)对齐,再用图像/表达嵌入各自的健康分布距离做异常打分,比较两者是否一致。Loki Annotate 的「marker 基因句子零样本标注」可直接拿肾损伤 marker(如 HAVCR1、LCN2、VCAM1)作为文本 prompt 生成弱标签,辅助 KidneyAnomalyBench 的专家标注。需要注意它在肾上只有少量验证样本(Retrieve 的 kidney Recall@10% 0.297),也不是单细胞分辨率。对课题 2,Retrieve 用「图像相似度代替转录组 ground truth」的评测方式,正是 agent 报告中易被当作证据的弱代理,是 claim-to-evidence 校验应当标记的类型。
<!-- EN --> For detect → model → revert, OmiCLIP offers a **shared H&E–expression embedding space**, which matters most for Topic 1's cross-modal agreement: if a tissue region's H&E embedding and transcriptome embedding fail to retrieve each other in the shared space, that is a natural cross-modal disagreement signal; when both deviate from the healthy reference, a real lesion is more likely. Given paired H&E and single-cell-resolution spatial-omics data, so Loki Align (the paper already demonstrates Xenium→pseudo-Visium) could register them, and each modality's distance to its healthy distribution could be scored and compared for agreement. Loki Annotate's zero-shot "marker-gene sentence" labelling could take kidney-injury markers (e.g. HAVCR1, LCN2, VCAM1) as prompts to produce weak labels that assist expert annotation for KidneyAnomalyBench. Caveats: kidney validation is thin (kidney Recall@10% 0.297) and resolution is spot-level, not single-cell. For Topic 2, Retrieve's evaluation — image similarity standing in for transcriptomic ground truth — is exactly the weak proxy agents tend to report as evidence, a type the claim-to-evidence verifier should flag.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** <!-- EN --> **Code:**
<!-- ZH/EN --> <https://github.com/GuangyuWangLab2021/Loki>
- <!-- ZH --> **模型权重与 ST-bank:** <!-- EN --> **Weights and ST-bank:**
<!-- ZH/EN --> <https://huggingface.co/WangGuangyuLab/Loki>
- <!-- ZH --> **评测基线**:PASTE、GPSA、CAST(对齐);Tangram、CARD、Cell2location、RCTD 等(分解);Hist2ST、HisToGene、BLEEP、mclSTExp(表达预测)。 <!-- EN --> **Baselines**: PASTE, GPSA, CAST (alignment); Tangram, CARD, Cell2location, RCTD etc. (decomposition); Hist2ST, HisToGene, BLEEP, mclSTExp (expression prediction).

## 待读 / Follow-ups
- <!-- ZH --> HEST-1k(`hest1k-2024`)与 H&E→表达 benchmark(`he2expr-bench-natcommun-2025`),对照 PredEx 的评测口径。 <!-- EN --> HEST-1k (`hest1k-2024`) and the H&E→expression benchmark (`he2expr-bench-natcommun-2025`) to compare against PredEx's evaluation protocol.
- <!-- ZH --> CONCH、PLIP、UNI(`uni2-h-model`)作为病理图像编码器的替代。 <!-- EN --> CONCH, PLIP and UNI (`uni2-h-model`) as alternative pathology encoders.
- <!-- ZH --> GenePT / Cell2Sentence:「表达即文本」思路的来源。 <!-- EN --> GenePT / Cell2Sentence — origins of the expression-as-text idea.

## 引用 / Cite
```bibtex
@article{Chen_2025_Loki, title={A visual–omics foundation model to bridge histopathology with spatial transcriptomics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02707-1}, DOI={10.1038/s41592-025-02707-1}, number={7}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Chen, Weiqing and Zhang, Pengzhi and Tran, Tu N and Xiao, Yiwei and Li, Shengyu and Shah, Vrutant V. and Cheng, Hao and Brannan, Kristopher W. and Youker, Keith and Lai, Li and Fang, Longhou and Yang, Yu and Le, Nhat-Tu and Abe, Jun-ichi and Chen, Shu-Hsia and Ma, Qin and Chen, Ken and Song, Qianqian and Cooke, John P. and Wang, Guangyu}, year={2025}, month=May, pages={1568–1582} }
```
