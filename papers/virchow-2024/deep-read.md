# A foundation model for clinical-grade computational pathology and rare cancers detection

> **Bibkey** `Vorontsov_2024` · **Venue** Nature Medicine (2024) · **Category** foundation · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s41591-024-03141-0>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> Virchow 是一个在 150 万张全切片图像(WSI)上用 DINOv2 自监督预训练的 632M 参数 ViT-H/14 病理基础模型,可作为冻结的 tile 级特征骨干,支撑泛癌检测、生物标志物预测与细胞识别等下游任务。
<!-- EN --> Virchow is a 632M-parameter ViT-H/14 pathology foundation model self-supervised (DINOv2) on 1.5M whole-slide images, serving as a frozen tile-level backbone for pan-cancer detection, biomarker prediction, and cell identification.

## 研究问题 / Problem
<!-- 这篇论文要解决什么问题?为什么重要? / What problem, and why it matters. -->
<!-- ZH --> 计算病理学的临床落地依赖于对病理图像中高度多样化形态模式的建模,而针对每种组织/癌种单独训练的监督模型需要大量标注、难以覆盖罕见癌。作者提出:一个足够大的通用基础模型能在有限标注下实现临床级性能,尤其是提升罕见癌的检测。
<!-- EN --> Clinical deployment of computational pathology hinges on modelling the highly diverse morphological patterns in tissue images. Tissue-specific supervised models need large labelled datasets and generalise poorly to rare cancers. The paper argues a single large foundation model can reach clinical-grade performance with far less labelled data, especially improving rare-cancer detection.

## 方法 / Method
<!-- 核心方法、模型、数据流。关键公式/架构。 / Core method, model, data pipeline, key architecture. -->
<!-- ZH --> 骨干为 ViT-H/14(632M 参数,32 层,embedding 维度 1,280,16 个注意力头,SwiGLU 激活,启用 LayerScale),用 DINOv2 自监督目标在 fp16 混合精度下预训练。输入 224×224 tile,输出 257 个 token(1 个 class token + 256 个 patch token,每 token 1,280 维);推荐的切片级/tile 级表征为 class token 与 patch token 均值拼接得到的 2,560 维向量。下游通过在冻结特征上训练轻量分类头(如 tile 聚合器)实现泛癌检测、生物标志物预测与细胞识别。
<!-- EN --> The backbone is a ViT-H/14 (632M params, 32 layers, embedding dim 1,280, 16 heads, SwiGLU activation, LayerScale) pretrained with the DINOv2 self-supervised objective in fp16 mixed precision. It ingests 224×224 tiles and emits 257 tokens (1 class + 256 patch tokens, 1,280-dim each); the recommended tile embedding is the 2,560-dim concatenation of the class token and mean-pooled patch tokens. Downstream tasks train lightweight heads/aggregators on the frozen features for pan-cancer detection, biomarker prediction, and cell identification.

## 数据 / Data
<!-- 数据集、模态、规模、来源。 / Datasets, modalities, scale, source. -->
<!-- ZH --> 预训练语料为来自 Memorial Sloan Kettering Cancer Center 的约 150 万张 H&E 全切片图像,扫描分辨率 0.5 微米/像素(20× 放大)。评测覆盖 9 种常见癌与 7 种罕见癌的标本级泛癌检测,以及生物标志物预测与细胞识别任务(具体数据集划分与规模细节在正文,仅摘要可得 / abstract-only)。
<!-- EN --> Pretraining used ~1.5M H&E whole-slide images from Memorial Sloan Kettering Cancer Center, scanned at 0.5 µm/px (20× magnification). Evaluation spans specimen-level pan-cancer detection across 9 common and 7 rare cancers, plus biomarker prediction and cell identification (detailed splits/sizes in the main text — abstract-only here / abstract-only).

## 主要结果 / Key results
<!-- 关键指标与结论,尽量带数字。 / Headline metrics and conclusions, with numbers where possible. -->
<!-- ZH --> 泛癌检测在 9 种常见 + 7 种罕见癌上达到 0.95 的标本级 ROC-AUC。基于 Virchow 冻结特征、使用更少训练数据构建的泛癌检测器,可达到与生产环境中组织特异临床级模型相当的性能,并在部分罕见癌变体上超越它们。作者据此论证大规模基础模型在标注稀缺场景下的价值。(更细粒度的逐任务/逐癌种数字仅摘要可得 / abstract-only)
<!-- EN --> Pan-cancer detection reaches 0.95 specimen-level ROC-AUC across 9 common + 7 rare cancers. A Virchow-based detector trained on less data matches production tissue-specific clinical-grade models and outperforms them on some rare cancer variants, underscoring the foundation-model advantage under limited labels. (Finer per-task/per-cancer numbers are abstract-only / abstract-only.)

## 创新点 / Contributions
- <!-- ZH --> 当时最大的计算病理基础模型(632M ViT-H,1.5M WSI 预训练),证明规模化带来的迁移收益。 <!-- EN --> Largest computational-pathology foundation model at the time (632M ViT-H, 1.5M WSIs), showing scale-driven transfer gains.
- <!-- ZH --> 用单一冻结骨干统一支撑泛癌检测 / 生物标志物 / 细胞识别多任务。 <!-- EN --> A single frozen backbone unifying pan-cancer detection, biomarker prediction, and cell identification.
- <!-- ZH --> 在有限标注下达到临床级性能,并显著改善罕见癌检测。 <!-- EN --> Clinical-grade performance under limited labels, with notable rare-cancer improvements.

## 局限 / Limitations
- <!-- ZH --> 预训练数据来自单一机构(MSKCC),存在扫描仪/染色/人群的域偏移风险,跨机构泛化需外部验证。 <!-- EN --> Single-institution (MSKCC) pretraining risks scanner/stain/population domain shift; cross-site generalisation needs external validation.
- <!-- ZH --> 仅 H&E、20× 单一放大倍率,未覆盖 IHC、多重免疫荧光、多放大倍率等模态。 <!-- EN --> H&E-only at a single 20× magnification; no IHC, multiplex-IF, or multi-scale coverage.
- <!-- ZH --> 骨干体量大(632M),tile 级推理算力/存储成本高。 <!-- EN --> The 632M backbone is compute/storage-heavy for tile-level inference.
- <!-- ZH --> 正文全文与逐任务细节因付费墙不可得。 <!-- EN --> Full main text and per-task detail are behind a paywall.

## 与本研究方向的关系 / Relation to our direction
<!-- anomaly detection → virtual tissue → revert via gene prediction 这条线上,这篇处在哪一环?能复用什么? -->
<!-- ZH --> Virchow 直接服务于流水线的第一环——**异常检测**中的组织病理模态。它是一个即插即用、可复用的**特征骨干**:把 H&E WSI 切成 224×224 tile,提取 2,560 维嵌入,即可为下游 anomaly detection(如在正常组织嵌入分布上做 one-class / 重构 / 密度估计,把偏离正常流形的 tile/区域标记为疾病或药物扰动导致的异常)提供强表征,免去从零训练。其泛癌检测头本身就是一种"疾病 vs 正常"判别器,可作为弱监督异常评分的起点。它不覆盖 virtual tissue 建模或 gene-revert 预测(那需要空间转录组/单细胞模态),但可作为把组织学异常区域与空间-omics 对齐的视觉编码器,连接影像异常与后续基因层面的反转分析。
<!-- EN --> Virchow plugs directly into stage one of our pipeline — **anomaly detection** on the histopathology modality. It is a drop-in, reusable **feature backbone**: tile an H&E WSI into 224×224 patches, extract 2,560-dim embeddings, and feed downstream anomaly detectors (one-class / reconstruction / density models over the distribution of normal-tissue embeddings, flagging tiles/regions off the normal manifold as disease- or perturbation-driven anomalies), avoiding training from scratch. Its pan-cancer detection head is itself a disease-vs-normal discriminator usable as a starting weak-supervision anomaly score. It does not cover virtual-tissue modelling or gene-revert prediction (which need spatial-omics/single-cell modalities), but can act as the visual encoder that aligns histologic anomaly regions with spatial-omics for the downstream gene-level revert analysis.

## 可复用资产 / Reusable assets
<!-- 代码、预训练模型、数据集、评测协议。 / Code, checkpoints, datasets, eval protocols. -->
<!-- ZH --> - 预训练权重公开于 Hugging Face:`paige-ai/Virchow`(经门控访问),可用 `timm` 直接加载为冻结特征提取器;后续版本 `paige-ai/Virchow2`。
- 输出规格:257 token(1 class + 256 patch,1,280 维/token),推荐 2,560 维 tile 嵌入;dense patch token 可用于分割。
- 注意许可:模型卡显示 Apache-2.0,但 Paige 的 Virchow 系权重历来附带非商用/研究性质门控条款,商用前务必核对 HF 上的实际 license 与使用条款。
<!-- EN --> - Pretrained weights on Hugging Face: `paige-ai/Virchow` (gated access), loadable via `timm` as a frozen extractor; successor `paige-ai/Virchow2`.
- Output spec: 257 tokens (1 class + 256 patch, 1,280-dim each), recommended 2,560-dim tile embedding; dense patch tokens usable for segmentation.
- License caveat: the model card lists Apache-2.0, but Paige's Virchow weights have historically carried non-commercial/research gating — verify the actual HF license and terms before any commercial use.

## 待读 / Follow-ups
- <!-- ZH/EN --> Virchow2 / Virchow2G(更大规模、更多机构数据)对比论文与模型卡。
- <!-- ZH/EN --> 其他病理基础模型基准:UNI (MahmoodLab), CONCH, GigaPath (Prov-GigaPath), Phikon — 与 Virchow 的 tile-embedding 迁移对比。
- <!-- ZH/EN --> 在冻结 Virchow 嵌入上做无监督异常检测的可行性验证(one-class SVM / PatchCore / 正常流形密度估计)。
- <!-- ZH/EN --> 正文中泛癌检测的逐癌种 AUC、外部机构验证与标注效率曲线(需获取全文)。

## 引用 / Cite
```bibtex
@article{Vorontsov_2024, title={A foundation model for clinical-grade computational pathology and rare cancers detection}, volume={30}, ISSN={1546-170X}, url={http://dx.doi.org/10.1038/s41591-024-03141-0}, DOI={10.1038/s41591-024-03141-0}, number={10}, journal={Nature Medicine}, publisher={Springer Science and Business Media LLC}, author={Vorontsov, Eugene and Bozkurt, Alican and Casson, Adam and Shaikovski, George and Zelechowski, Michal and Severson, Kristen and Zimmermann, Eric and Hall, James and Tenenholtz, Neil and Fusi, Nicolo and Yang, Ellen and Mathieu, Philippe and van Eck, Alexander and Lee, Donghun and Viret, Julian and Robert, Eric and Wang, Yi Kan and Kunz, Jeremy D. and Lee, Matthew C. H. and Bernhard, Jan H. and Godrich, Ran A. and Oakley, Gerard and Millar, Ewan and Hanna, Matthew and Wen, Hannah and Retamero, Juan A. and Moye, William A. and Yousfi, Razik and Kanan, Christopher and Klimstra, David S. and Rothrock, Brandon and Liu, Siqi and Fuchs, Thomas J.}, year={2024}, month=July, pages={2924–2935} }
```
