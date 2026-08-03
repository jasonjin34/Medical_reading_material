# A Generative Foundation Model for Multimodal Histopathology

> **Bibkey** `Xiang2026_260403635` · **Venue** arXiv preprint (2026) · **Category** foundation · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2604.03635>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> MuPD 是一个把 H&E 组织学、RNA 分子谱、临床文本统一到共享隐空间的生成式病理基础模型,用一个扩散 Transformer 支持文本/图像/RNA 条件的跨模态合成与虚拟染色。
<!-- EN --> MuPD (Multimodal Pathology Diffusion) is a generative pathology foundation model that embeds H&E histology, RNA molecular profiles, and clinical text into a shared latent space, using one diffusion transformer to serve text-/image-/RNA-conditioned cross-modal synthesis and virtual staining.

## 研究问题 / Problem
<!-- ZH --> 复杂疾病的诊疗需要整合组织学、分子和临床数据,但受组织稀缺、检测成本和流程限制,这些模态在实践中常常缺失。已有的补全方法都是针对单一 source→target 对训练的任务专用模型,泛化性差。作者要问:能否用一个在异质病理模态上大规模预训练的统一生成模型,同时超越各类专用方法?
<!-- EN --> Diagnosis of complex disease needs integrated histological, molecular, and clinical data, but these modalities are routinely incomplete due to tissue scarcity, assay cost, and workflow constraints. Prior imputation methods are task-specific models trained on narrow single source→target pairs and generalize poorly. Can one unified generative model, pretrained at scale across heterogeneous pathology modalities, outperform specialized alternatives?

## 方法 / Method
<!-- ZH --> 核心是基于 Scalable Interpolant Transformer (SiT) 的扩散 Transformer,以 H&E 组织学作为"桥接模态"。关键设计:(1) Decoupled Cross-Attention (DCA)——文本、RNA、参考图各走独立的并行注意力流,由中间图像表征作 query,避免异质模态在共享 KV 空间里互相竞争,保留各模态生物特性;(2) 特征对齐——用轻量 CNN projector 把内部特征对齐到预训练病理编码器 Virchow2,叠加 CLS-token 去噪辅助损失做全局语义一致性。图像经冻结 VAE(8× 下采样)编码;AdamW,8×H100,最多 500K 步,bfloat16;classifier-free guidance 用 10% 条件 dropout。RNA 谱归一化为 TPM 后用 pan-cancer 基因签名压缩成 331 个通路级富集分数作为条件。
<!-- EN --> A Diffusion/SiT (Scalable Interpolant Transformer) backbone with H&E as the bridging modality. Key components: (1) Decoupled Cross-Attention (DCA) — text, RNA, and reference-image conditions each flow through independent parallel attention streams queried by intermediate image representations, avoiding competition in a shared KV space; (2) feature alignment — a lightweight CNN projector aligns internal features to the pretrained pathology encoder Virchow2, plus an auxiliary CLS-token denoising loss for global semantics. Frozen VAE with 8× downsampling; AdamW on 8× H100 up to 500K steps in bfloat16; classifier-free guidance with 10% condition dropout. RNA is TPM-normalized then compressed to 331 pathway-level enrichment scores via pan-cancer signatures.

## 数据 / Data
<!-- ZH --> 预训练语料:1 亿张 512×512、20× 的 H&E patch(TCGA、GTEx、PAIP、PLCO);160 万文本–图像对(PathGen-1.6M);1080 万 RNA–图像对(TCGA bulk RNA-seq 与配对 WSI),覆盖 34 个人体器官。评测集:HISTAI、PathMMU、SkinCancer、PanNuke、UniToPatho、LC25000、SICAPv2、MOSAIC 空间转录组、TCGA、HER2Match、IHC4BC、ORION 结直肠癌数据集。
<!-- EN --> Pretraining: 100M H&E patches (512×512, 20×; TCGA, GTEx, PAIP, PLCO); 1.6M text–image pairs (PathGen-1.6M); 10.8M RNA–image pairs (TCGA bulk RNA-seq linked to matched WSIs), spanning 34 human organs. Evaluation: HISTAI, PathMMU, SkinCancer, PanNuke, UniToPatho, LC25000, SICAPv2, MOSAIC spatial transcriptomics, TCGA, HER2Match, IHC4BC, ORION colorectal cancer.

## 主要结果 / Key results
<!-- ZH --> 图像到图像:FID 305.12 vs PixCell 602.45(约 49% 提升),相似度 0.63 vs 0.46。文本到图像:FID 576.30 vs PathLDM 1029.62(约 44%),对齐 0.53 vs 0.41。合成数据增强:PanNuke 10-shot 准确率 0.492→0.724(+47.2%),SkinCancer 0.790→0.850;检索 R@10 大幅提升。空间转录组→H&E(五种癌):膀胱癌 FID 724.6 vs GeneFlow 1012.5(约 28%),细胞类型分布 Wasserstein 距离显著更低。冻切→FFPE(肺):FID 323.7 vs AI-FFPE 435.3(约 26%)。H&E→IHC:ER FID 124.18 vs CycleGAN 256.76,临床 AUC Ki67 0.9772、HER2 0.9556。H&E→mIF:平均 patch PCC 0.238 vs GigaTIME 0.198;slide 级 0.464 vs 0.339;PD-L1 patch PCC 0.218。消融:去掉 DCA 换共享注意力使 FID 恶化 7.9–13.6%;CNN 空间对齐+CLS 去噪优于 REPA(相似度 0.424 vs 0.243)。
<!-- EN --> Image→image FID 305.12 vs PixCell 602.45 (~49%), similarity 0.63 vs 0.46. Text→image FID 576.30 vs PathLDM 1029.62 (~44%), alignment 0.53 vs 0.41. Augmentation: PanNuke 10-shot 0.492→0.724 (+47.2%), SkinCancer 0.790→0.850; large retrieval R@10 gains. Spatial-transcriptomics→H&E (5 cancers): bladder FID 724.6 vs GeneFlow 1012.5 (~28%), lower cell-type Wasserstein distances. Frozen→FFPE (lung) FID 323.7 vs AI-FFPE 435.3 (~26%). H&E→IHC: ER FID 124.18 vs CycleGAN 256.76; clinical AUC Ki67 0.9772, HER2 0.9556. H&E→mIF: patch PCC 0.238 vs GigaTIME 0.198; slide-level 0.464 vs 0.339; PD-L1 patch PCC 0.218. Ablations: shared attention worsens FID 7.9–13.6%; CNN spatial + CLS denoising beats REPA (0.424 vs 0.243).

## 创新点 / Contributions
- <!-- ZH --> 单一统一生成基础模型跨 H&E/RNA/文本/IHC/mIF 多任务,minimal 或 zero fine-tuning 即用;把多个专用任务重新解读为同一跨模态生物分布的投影。
  <!-- EN --> A single unified generative FM covering H&E/RNA/text/IHC/mIF with minimal or no task-specific fine-tuning; reframes disparate tasks as projections of one shared cross-modal biological distribution.
- <!-- ZH --> Decoupled Cross-Attention:异质条件各自独立注意力流,避免共享 KV 竞争(消融证实其价值)。
  <!-- EN --> Decoupled Cross-Attention keeps heterogeneous conditions in separate streams instead of a shared KV space (validated by ablation).
- <!-- ZH --> 与 Virchow2 的特征对齐 + CLS-token 去噪损失,提升生成的语义与病理保真度;超大规模预训练(1 亿 patch、34 器官)。
  <!-- EN --> Virchow2 feature alignment plus CLS-token denoising for semantic/pathological fidelity; very large-scale pretraining (100M patches, 34 organs).

## 局限 / Limitations
- <!-- ZH --> 扩散模型本质随机,在分布漂移下可能产生解剖上不合理的输出。
  <!-- EN --> Diffusion is inherently stochastic; may hallucinate anatomically implausible outputs under distribution shift.
- <!-- ZH --> 计算生物标志物需与实验室测量做前瞻性一致性验证;当前定位为 hypothesis-generating,非诊断级。
  <!-- EN --> Computational biomarkers need prospective concordance validation vs. lab assays; positioned as hypothesis-generating, not diagnostic.
- <!-- ZH --> RNA 条件来自 bulk RNA-seq(非单细胞/空间高分辨),且压缩为 331 通路分数会损失基因级细节;未见公开代码/权重承诺。
  <!-- EN --> RNA conditioning is bulk (not single-cell/high-res spatial) and compressed to 331 pathway scores, losing gene-level detail; no stated public code/weights.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这篇主要落在**virtual tissue 建模**这一环,并直接触及**gene→组织表型**的方向。它证明了组织形态学隐含分子信息:RNA/通路条件能生成保持细胞类型分布的 H&E,H&E 又能反推 IHC/mIF 免疫标志物空间分布。对我们的用途:(1) 作为生成式"虚拟组织"引擎,可在给定分子/通路条件下合成对应组织图像——若把"基因扰动→组织外观改变"作为条件建模,原则上可用于模拟 revert(施加基因/通路变化后组织形态如何变化),是 gene-revert 假设生成的候选工具;(2) DCA 的多模态条件融合思路可迁移到我们的 spatial-omics 条件建模;(3) 但它做的是**正向生成/imputation**,不含显式**anomaly detection**,也不直接输出"要调哪些基因才能 revert 异常"的方向——需要我们在其上加入异常评分与逆向优化。总体:强的 virtual-tissue backbone,弱在 anomaly-detection 与 gene-revert 的因果/优化环节。
<!-- EN --> This sits mainly in the **virtual-tissue modeling** stage and touches the **gene→tissue-phenotype** link. It shows morphology encodes molecular information: RNA/pathway conditions generate H&E that preserves cell-type distributions, and H&E maps back to IHC/mIF immune-marker localization. For us: (1) as a generative "virtual tissue" engine that synthesizes tissue images under molecular/pathway conditions — if perturbations are cast as conditions, it could in principle simulate revert (how tissue morphology shifts after a gene/pathway change), a candidate for gene-revert hypothesis generation; (2) DCA's multimodal conditioning transfers to our spatial-omics conditioning; (3) but it does **forward generation/imputation only** — no explicit **anomaly detection**, and it does not output "which genes to modulate to revert an anomaly"; we would need to bolt on anomaly scoring and inverse optimization. Net: strong virtual-tissue backbone, weak on the anomaly-detection and causal gene-revert stages.

## 可复用资产 / Reusable assets
<!-- ZH --> 模型/代码/权重:论文未明确公开(需向作者或后续版本确认)。可直接复用的外部资产与协议:预训练编码器 **Virchow2**(特征对齐目标)、**PathGen-1.6M** 文本–图像对、**TCGA/GTEx/PAIP/PLCO** H&E、**MOSAIC** 空间转录组、**PanNuke/UniToPatho/LC25000/SICAPv2/SkinCancer** 分类基准、**IHC4BC/HER2Match/ORION** 虚拟染色基准。评测协议可复用:FID/KID + 图文对齐、few-shot(10-shot)分类增益、细胞类型分布 Wasserstein 距离、标志物 PCC(patch/slide 级)、IHC 临床 AUC(Ki67/HER2)。方法组件可复用:SiT 扩散主干、Decoupled Cross-Attention、CNN+CLS-token 对齐损失、RNA→331 通路富集分数编码。
<!-- EN --> Model/code/weights: not explicitly released in the paper (confirm with authors / later version). Reusable external assets & protocols: pretrained encoder **Virchow2** (alignment target); **PathGen-1.6M** text–image pairs; **TCGA/GTEx/PAIP/PLCO** H&E; **MOSAIC** spatial transcriptomics; classification benchmarks **PanNuke/UniToPatho/LC25000/SICAPv2/SkinCancer**; virtual-staining benchmarks **IHC4BC/HER2Match/ORION**. Reusable eval protocols: FID/KID + text–image alignment, few-shot (10-shot) classification lift, cell-type Wasserstein distance, marker PCC (patch/slide), IHC clinical AUC (Ki67/HER2). Reusable method pieces: SiT diffusion backbone, Decoupled Cross-Attention, CNN+CLS-token alignment loss, RNA→331-pathway-score encoding.

## 待读 / Follow-ups
- <!-- ZH --> 是否放出代码/权重?查 arXiv 后续版本与作者主页(Ruijiang Li lab, Stanford)。
  <!-- EN --> Check for code/checkpoint release in later versions and the Ruijiang Li lab page.
- <!-- ZH --> Virchow2、PixCell、GeneFlow、PathLDM、AI-FFPE、GigaTIME、HistoPlexer 等 baseline 原文。
  <!-- EN --> Read baselines: Virchow2, PixCell, GeneFlow, PathLDM, AI-FFPE, GigaTIME, HistoPlexer.
- <!-- ZH --> RNA→331 通路富集的具体签名与可否换成单细胞/空间高分辨条件。
  <!-- EN --> How the 331 pathway signatures are built; feasibility of single-cell/spatial-resolution conditioning.
- <!-- ZH --> 能否把扰动/revert 建成条件并加异常评分与逆向优化(与本方向直接相关)。
  <!-- EN --> Can perturbation/revert be cast as a condition + anomaly scoring + inverse optimization on top of MuPD.

## 图表 / Figures & tables

![Study overview and architecture](figures/fig1.png)
<!-- ZH --> **图1.** 研究总览:(a) MuPD 框架,以 H&E 组织学作为桥接模态,整合分子转录组/蛋白质组、组织结构与临床文本,实现跨物理尺度的跨模态生成;(b) 覆盖 34 器官的预训练数据(1 亿 H&E patch、160 万文本–图像对、1080 万 RNA–图像对);(c) 采用带解耦跨模态注意力(DCA)的 DiT,图像/文本/RNA 条件走并行注意力流;(d) 与其它方法的基准对比。
<!-- EN --> **Fig 1.** Study overview: (a) the MuPD framework with H&E as the bridging modality integrating transcriptomics/proteomics, tissue architecture, and clinical text for cross-scale synthesis; (b) 34-organ pretraining corpus (100M H&E patches, 1.6M text–image, 10.8M RNA–image pairs); (c) DiT with decoupled cross-modal attention (DCA) processing image/text/RNA conditioning in parallel streams; (d) benchmarking against other methods.
<!-- ZH/EN --> _Source: https://arxiv.org/html/2604.03635v1/figs/fig1-overview.png  ·  License: arXiv (author-posted preprint)_

![Image- and text-conditioned generation](figures/fig2.png)
<!-- ZH --> **图2.** 图像/文本条件生成:(a) 图像到图像生成,MuPD 比各基线更忠实地保留真实生物结构;(b) 文本到图像生成,从文本 prompt 准确重建细粒度组织学特征。
<!-- EN --> **Fig 2.** Image- and text-conditioned generation: (a) image-to-image generation where MuPD preserves authentic biological structures with higher fidelity than baselines; (b) text-to-image generation reconstructing fine-grained histological features from text prompts.
<!-- ZH/EN --> _Source: https://arxiv.org/html/2604.03635v1/figs/fig2-text2image-image2image.png  ·  License: arXiv (author-posted preprint)_

![H&E generation from spatial transcriptomics](figures/fig3.png)
<!-- ZH --> **图3.** 由空间转录组生成 H&E:(a) 五种癌症的 FID;(b) 合成与真实图像的细胞类型组成对比(Wasserstein 距离);(c) MuPD 与 GeneFlow 的 Wasserstein 距离对比;(d) 匹配空间转录组条件下真实/合成 H&E 图像对示例。
<!-- EN --> **Fig 3.** H&E generation from spatial transcriptomics: (a) FID across five cancer types; (b) cell-type composition in synthetic vs. real images (Wasserstein distance); (c) Wasserstein-distance comparison between MuPD and GeneFlow; (d) representative real/synthetic H&E pairs conditioned on matched spatial transcriptomics.
<!-- ZH/EN --> _Source: https://arxiv.org/html/2604.03635v1/figs/fig5-st2image.png  ·  License: arXiv (author-posted preprint)_

![Virtual H&E-to-IHC staining](figures/fig4.png)
<!-- ZH --> **图4.** 虚拟 H&E→IHC 染色与临床验证:(a) 多标志物虚拟 IHC 生成示例;(b) FID/KID 体现分布保真度与感知质量;(c) IHC4BC 上预测真实临床生物标志物的 AUC。
<!-- EN --> **Fig 4.** Virtual H&E-to-IHC translation and clinical validation: (a) multi-stain virtual IHC examples; (b) FID and KID for distributional fidelity and perceptual quality; (c) clinical utility on IHC4BC predicting ground-truth biomarkers by AUC.
<!-- ZH/EN --> _Source: https://arxiv.org/html/2604.03635v1/figs/fig6-he2ihc.png  ·  License: arXiv (author-posted preprint)_

### 结果表 / Results

<!-- ZH --> **表1.** 跨模态生成主结果:MuPD 对比各任务次优基线(FID 越低越好;相似度/对齐越高越好)。
<!-- EN --> **Table 1.** Headline cross-modal generation results: MuPD vs. the next-best baseline per task (lower FID is better; higher similarity/alignment is better).

| Task | Metric | MuPD | Best baseline | Rel. gain |
|---|---|---|---|---|
| Image → image | FID ↓ | 305.12 | 602.45 (PixCell) | ~49% |
| Image → image | Similarity ↑ | 0.63 | 0.46 (PixCell) | — |
| Text → image | FID ↓ | 576.30 | 1029.62 (PathLDM) | ~44% |
| Text → image | Text–image alignment ↑ | 0.53 | 0.41 (PathLDM) | — |
| Spatial transcriptomics → H&E (bladder) | FID ↓ | 724.6 | 1012.5 (GeneFlow) | ~28% |
| Frozen → FFPE (lung) | FID ↓ | 323.7 | 435.3 (AI-FFPE) | ~26% |
| H&E → IHC (ER marker) | FID ↓ | 124.18 | 256.76 (CycleGAN) | ~52% |
| H&E → mIF | Patch PCC ↑ | 0.238 | 0.198 (GigaTIME) | ~20% |
| H&E → mIF | Slide-level PCC ↑ | 0.464 | 0.339 (GigaTIME) | ~37% |

<!-- ZH --> **表2.** 下游价值:合成数据增强的少样本分类(10-shot 准确率)与虚拟染色的临床效用(AUC)。
<!-- EN --> **Table 2.** Downstream value: synthetic-data augmentation for few-shot classification (10-shot accuracy) and virtual-staining clinical utility (AUC).

| Evaluation | Metric | Baseline / w-MuPD |
|---|---|---|
| PanNuke, 10-shot | Accuracy ↑ | 0.492 → 0.724 (+47.2%) |
| SkinCancer, 10-shot | Accuracy ↑ | 0.790 → 0.850 |
| H&E → IHC, Ki67 | Clinical AUC ↑ | 0.9772 |
| H&E → IHC, HER2 | Clinical AUC ↑ | 0.9556 |

<!-- ZH --> _Source: https://arxiv.org/abs/2604.03635 (arXiv HTML v1)  ·  License: arXiv (author-posted preprint). 数值忠实转录自论文文本。_
<!-- EN --> _Source: https://arxiv.org/abs/2604.03635 (arXiv HTML v1)  ·  License: arXiv (author-posted preprint). Numerical values are faithfully transcribed from the paper text._

## 引用 / Cite
```bibtex
@misc{Xiang2026_260403635,
  title = {A Generative Foundation Model for Multimodal Histopathology},
  author = {Jinxi Xiang and Mingjie Li and Siyu Hou and Yijiang Chen and Xiangde Luo and Yuanfeng Ji and Xiang Zhou and Ehsan Adeli and Akshay Chaudhari and Curtis P. Langlotz and Kilian M. Pohl and Ruijiang Li},
  year = {2026},
  eprint = {2604.03635},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2604.03635}
}
```
