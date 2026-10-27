# MahmoodLab/UNI2-h

> **Bibkey** `MahmoodLab_UNI2h` · **Venue** Hugging Face model card · **Category** foundation · **Relevance** medium · **Access** open (gated download)
> **Link** <https://huggingface.co/MahmoodLab/UNI2-h>
> `status: complete` — 依据公开的 Hugging Face 模型卡全文(2026-10-27 抓取;权重文件需申请)。模型卡本身没有基准数字;官方 GitHub 仓库 README 有实验室自报的 UNI2-h 基准表(未经同行评审),本库的 PathBench 论文是独立评测。

---

## 一句话 / One-liner
<!-- ZH --> UNI2-h 是 Mahmood Lab(Harvard / BWH)发布的病理视觉基础模型:一个 681M 参数的定制 ViT-H/14,用 DINOv2 配方在 Mass General Brigham 的 2 亿+ 个 H&E 与 IHC 图块上自监督训练,把 224×224 组织图块编码为 1,536 维特征,供下游冻结使用(model card §"Model Description"、§"Training Details")。
<!-- EN --> UNI2-h is a pathology vision foundation model from the Mahmood Lab (Harvard / BWH): a 681M-parameter custom ViT-H/14 trained with the DINOv2 recipe on 200M+ H&E and IHC tiles from Mass General Brigham, mapping a 224×224 tissue tile to a 1,536-dim feature for frozen downstream use (model card §"Model Description", §"Training Details").

## 要点 / Takeaways
- <!-- ZH --> 这是一个模型卡,不是论文:Hugging Face 卡上没有基准数字,但卡上 Repository 链接指向的 GitHub 仓库(mahmoodlab/UNI)README 有 §"Benchmarking UNI 2",给出 UNI2-h 与 UNI、Virchow 2、h-optimus、Prov-GigaPath 等的 ROI 与 slide 基准表(实验室自报)。卡要求引用 UNI 论文(Chen et al., Nature Medicine 2024),该论文描述的是前代 UNI(GitHub README 模型表:UNI 发布于 03/2024,UNI2-h 发布于 01/2025)。 <!-- EN --> This is a model card, not a paper: the Hugging Face card has no benchmark numbers, but the GitHub repository it links (mahmoodlab/UNI) has a README section "Benchmarking UNI 2" with lab-reported ROI and slide benchmark tables comparing UNI2-h with UNI, Virchow 2, h-optimus, Prov-GigaPath and others. The card asks users to cite the UNI paper (Chen et al., Nature Medicine 2024), which describes the earlier UNI (GitHub README model table: UNI released 03/2024, UNI2-h 01/2025).
- <!-- ZH --> 训练数据:"2 亿+ 图块,来自 30 万+ 张 H&E 和 IHC 切片"(Training Details);同一张卡在 Model Description 中写"35 万+ 张"——卡内自相矛盾。 <!-- EN --> Training data: "over 200 million tiles from over 300k H&E and IHC slides" (Training Details); the same card says "over 350k" in Model Description — an internal inconsistency.
- <!-- ZH --> 架构:depth 24、24 头、embed_dim 1,536、SwiGLU FFN、8 个 register token、681M 参数;目标 = DINO 自蒸馏(multi-crop)+ iBOT masked image modeling + KoLeo 正则(Training Details;timm_kwargs)。 <!-- EN --> Architecture: depth 24, 24 heads, embed_dim 1,536, SwiGLU FFN, 8 register tokens, 681M params; objective = DINO self-distillation (multi-crop) + iBOT masked image modelling + KoLeo regularisation (Training Details; timm_kwargs).
- <!-- ZH --> 用法:冻结 CLS 特征做 linear probe / kNN / SimpleShot 分类、最近邻检索、MIL slide 分类;分割建议微调(ViTDet 或 ViT-Adapter)(Direct / Downstream Use)。官方提供 TCGA、CPTAC、PANDA 的预提取特征。 <!-- EN --> Usage: frozen CLS features for linear-probe / kNN / SimpleShot classification, nearest-neighbour retrieval and MIL slide classification; fine-tuning recommended for segmentation (ViTDet or ViT-Adapter) (Direct / Downstream Use). Pre-extracted features are provided for TCGA, CPTAC and PANDA.
- <!-- ZH --> 许可很严:CC-BY-NC-ND 4.0,仅限非商业学术研究;不得分发、发布或复制模型副本;个人邮箱(@gmail 等)申请会被拒,需机构邮箱(License; Requesting Access)。 <!-- EN --> Strict licence: CC-BY-NC-ND 4.0, non-commercial academic research only; no distributing, publishing or reproducing a copy of the model; personal e-mail (@gmail etc.) requests are denied, an institutional e-mail is required (License; Requesting Access).
- <!-- ZH --> 独立评测(PathBench,本库 `pathbench-natcommun-2026`):UNI2 在 TCGA 任务平均 AUROC 0.824(Fig. 1b);在全部 TCGA 任务上,UNI、UNI2、Virchow2、Prov-GigaPath、H-optimus-0 之间的 AUROC、AUPRC、敏感度、特异度经 Wald 检验无统计学差异(Supplementary Fig. 4a/c/e/g)。把 22 个非 TCGA 任务合起来看,差异也大多不显著,唯一显著的是 Virchow2 与 UNI2 的敏感度(Supplementary Fig. 4f);但若只看其中 8 个非 TCGA patch 级任务,Virchow2 与 UNI2 的 AUROC 差异显著(FDR 校正 p < 0.001)(Fig. 2b;Results)。 <!-- EN --> Independent evaluation (PathBench, `pathbench-natcommun-2026` in this library): UNI2 has mean TCGA AUROC 0.824 (Fig. 1b); across all TCGA tasks, Wald tests found no statistical differences in AUROC, AUPRC, sensitivity or specificity among UNI, UNI2, Virchow2, Prov-GigaPath and H-optimus-0 (Supplementary Fig. 4a/c/e/g). Pooled over the 22 non-TCGA tasks, differences were also largely non-significant, the only significant one being Virchow2 vs UNI2 for sensitivity (Supplementary Fig. 4f); restricted to the 8 non-TCGA patch-level tasks, however, Virchow2 vs UNI2 differed significantly in AUROC (FDR-adjusted p < 0.001) (Fig. 2b; Results).

## 研究问题 / Problem
<!-- ZH --> 模型卡本身不陈述研究问题,只定位为"用于组织病理图像多用途评估的预训练视觉 backbone"(Model Description)。我们的理解:它要解决的是计算病理中每个任务都从头训练、标注昂贵的问题——提供一个通用的 tile 级 encoder,下游只需轻量的线性头或 MIL 头。
<!-- EN --> The card states no research question; it positions the model as a "pretrained vision backbone for multi-purpose evaluation on histopathology images" (Model Description). Our reading: the target problem is that each pathology task is otherwise trained from scratch with costly labels — a general tile-level encoder lets downstream work use only light linear or MIL heads.

## 方法 / Method
<!-- ZH --> 1) **输入**:组织病理 ROI / tile,预处理为 resize 到 224、ImageNet 均值方差归一化(How To Use)。
<!-- ZH --> 2) **架构**:定制 ViT-H/14——patch 14、img 224、depth 24、num_heads 24、embed_dim 1,536、mlp_ratio 2.66667×2 的 SwiGLUPacked FFN(SiLU 激活)、init_values 1e-5、reg_tokens 8(8 个 register token)、no_embed_class、dynamic_img_size;共 681M 参数(timm_kwargs;Training Details)。本地加载代码里的 timm 基础名为 `vit_giant_patch14_224`。
<!-- ZH --> 3) **自监督目标**:DINOv2 配方——带 multi-crop 的 DINO 自蒸馏损失 + iBOT 掩码图像建模损失 + [CLS] token 上的 KoLeo 正则(Training Details)。卡上只给出这三个损失的名称,不解释其细节;细节见 DINOv2 原论文。
<!-- ZH --> 4) **训练设置**:bf16 + PyTorch-FSDP 混合精度;"大量 A100 80GB、大量 GPU 小时";MGB ERIS 计算平台(Training Details)。卡上没有给出 batch size、步数、倍率或器官分布。
<!-- ZH --> 5) **输出与下游**:每个 tile 输出 [1, 1536] 的特征;可直接用于 linear probe、kNN、SimpleShot(最近类中心)、最近邻检索,以及在一张 WSI 的一袋 CLS token 上训练 MIL 分类器;分割任务推荐微调(Direct / Downstream Use)。
<!-- EN --> 1) **Input**: histopathology ROIs / tiles, resized to 224 and normalised with ImageNet mean and std (How To Use).
<!-- EN --> 2) **Architecture**: custom ViT-H/14 — patch 14, img 224, depth 24, num_heads 24, embed_dim 1,536, SwiGLUPacked FFN with mlp_ratio 2.66667×2 and SiLU, init_values 1e-5, reg_tokens 8 (8 register tokens), no_embed_class, dynamic_img_size; 681M parameters (timm_kwargs; Training Details). The local-loading code uses the timm base name `vit_giant_patch14_224`.
<!-- EN --> 3) **Self-supervised objective**: the DINOv2 recipe — DINO self-distillation loss with multi-crop + iBOT masked image modelling loss + KoLeo regularisation on [CLS] tokens (Training Details). The card only names these three losses and does not explain them; see the DINOv2 paper for details.
<!-- EN --> 4) **Training setup**: bf16 with PyTorch-FSDP mixed precision; "lots of Nvidia A100 80GB for lots of GPU hours"; MGB ERIS research computing (Training Details). No batch size, steps, magnification or organ mix is given.
<!-- EN --> 5) **Output and downstream**: a [1, 1536] feature per tile, used for linear probing, kNN, SimpleShot (nearest centroid), nearest-neighbour retrieval, and MIL classifiers on a bag of CLS tokens per WSI; fine-tuning is recommended for segmentation (Direct / Downstream Use).

## 方法图 / Method diagram
```mermaid
flowchart LR
  A["MGB slides<br/>H&E and IHC"] --> B["200M+ tiles<br/>tile size not stated"]
  B --> C["ViT-H/14 681M<br/>DINOv2: DINO + iBOT + KoLeo"]
  I["Inference: tile resized to 224,<br/>ImageNet normalisation"] --> C
  C --> D["Frozen CLS feature<br/>1536-d per tile"]
  D --> E["Linear probe, kNN,<br/>SimpleShot, retrieval"]
  D --> F["MIL slide classifier"]
  C --> G["Fine-tune for segmentation<br/>ViTDet or ViT-Adapter"]
```

## 数据 / Data
<!-- ZH --> **预训练**:2 亿+ 图块,采样自 Mass General Brigham 的 H&E 与 IHC 切片——Training Details 写"30 万+ 张",Model Description 写"35 万+ 张 diverse"(卡内不一致;PathBench Table 2 记为 0.35M WSI、200M patch;该表的参数量写 ~632M,与卡上的 681M 不同)。卡上没有染色比例、倍率、器官或疾病分布。**预提取特征**:官方在 `MahmoodLab/UNI2-h-features` 提供 TCGA、CPTAC、PANDA 的 UNI2-h 嵌入(Pre-Extracted Embeddings)。
<!-- EN --> **Pretraining**: 200M+ tiles sampled from Mass General Brigham H&E and IHC slides — "over 300k" in Training Details, "over 350k diverse" in Model Description (inconsistent within the card; PathBench Table 2 lists 0.35M WSIs and 200M patches; that table gives ~632M parameters, unlike the card's 681M). No stain ratio, magnification, organ or disease breakdown is given. **Pre-extracted features**: UNI2-h embeddings for TCGA, CPTAC and PANDA at `MahmoodLab/UNI2-h-features` (Pre-Extracted Embeddings).

## 主要结果 / Key results
- <!-- ZH --> Hugging Face 模型卡:**没有定量结果**,只说冻结特征"在 ROI 分类、检索和 slide 分类上可获得有竞争力的结果"(Direct Use)。 <!-- EN --> Hugging Face model card: **no quantitative results**; it only says frozen features give "competitive results" on ROI classification, retrieval and slide classification (Direct Use).
- <!-- ZH --> GitHub README §"Benchmarking UNI 2"(实验室自报,README 未写明所用指标):ROI 基准 UNI → UNI2-h:HEST 0.386 → 0.414、CRC-100K-Raw 0.925 → 0.957、TCGA Uniform Tumor 0.595 → 0.675、C17-WILDS 0.972 → 0.977、Kather MSI 0.679 → 0.722;slide 基准:EBRAINS 0.682 → 0.711、PANDA 0.944 → 0.946、IHC ER/PR(内部)0.776 → 0.794。表中同时列出 Virchow 2、Virchow、UNI2-g-preview、h-optimus、Prov-GigaPath、CONCH、MUSK。协议:每个任务对 3 个学习率(1e-5、5e-5、1e-4)扫参,按验证集最优报告测试结果;所有模型用全局表征(如 CLS token),不做测试时增强。 <!-- EN --> GitHub README §"Benchmarking UNI 2" (lab-reported; the README does not name the metric): ROI benchmarks UNI → UNI2-h: HEST 0.386 → 0.414, CRC-100K-Raw 0.925 → 0.957, TCGA Uniform Tumor 0.595 → 0.675, C17-WILDS 0.972 → 0.977, Kather MSI 0.679 → 0.722; slide benchmarks: EBRAINS 0.682 → 0.711, PANDA 0.944 → 0.946, IHC ER/PR (internal) 0.776 → 0.794. The tables also list Virchow 2, Virchow, UNI2-g-preview, h-optimus, Prov-GigaPath, CONCH and MUSK. Protocol: for each task, a sweep over 3 learning rates (1e-5, 5e-5, 1e-4), reporting test performance of the best model on validation; all models use the global representation (e.g. CLS token) without test-time augmentation.
- <!-- ZH --> PathBench(独立第三方,linear probe + mean pooling):TCGA 19 个任务平均 AUROC 0.824(95% CI 0.779–0.868),位列前五;非 TCGA 22 个任务 0.824(95% CI 0.751–0.897)(PathBench Fig. 1b–c)。 <!-- EN --> PathBench (independent, linear probe + mean pooling): mean AUROC 0.824 (95% CI 0.779–0.868) on 19 TCGA tasks, in the top five; 0.824 (95% CI 0.751–0.897) on 22 non-TCGA tasks (PathBench Fig. 1b–c).
- <!-- ZH --> PathBench:非 TCGA patch 级任务平均 AUROC 0.953(仅次于 Virchow2 的 0.962);按累计 balanced accuracy,UNI2 从 TCGA 第 6 降到非 TCGA 第 9(PathBench Fig. 2b;Fig. 5a–b)。 <!-- EN --> PathBench: mean AUROC 0.953 on non-TCGA patch-level tasks (second to Virchow2 at 0.962); by cumulative balanced accuracy UNI2 drops from 6th on TCGA to 9th on non-TCGA tasks (PathBench Fig. 2b; Fig. 5a–b).

## 创新点 / Contributions
- <!-- ZH --> 相对前代 UNI:UNI 是 ViT-L/16(GitHub README 模型表),在 Mass-100K 上训练——来自 100,426 张诊断用 H&E WSI 的 1 亿+ 组织图块(UNI 论文);UNI2-h 换成更大的 ViT-H/14-reg8(681M、SwiGLU、8 个 register token),数据增至 2 亿+ 图块并加入 IHC(模型卡;GitHub README)。README 基准表中 UNI2-h 在全部 8 项上高于 UNI(见上)。 <!-- EN --> Compared with the earlier UNI: UNI is a ViT-L/16 (GitHub README model table) trained on Mass-100K — over 100 million tissue patches from 100,426 diagnostic H&E WSIs (UNI paper); UNI2-h moves to a larger ViT-H/14-reg8 (681M, SwiGLU, 8 register tokens) and 200M+ tiles including IHC (model card; GitHub README). In the README benchmark tables UNI2-h scores above UNI on all 8 tasks (see above).
- <!-- ZH --> 工程上即插即用:timm 一行加载,附预提取的 TCGA / CPTAC / PANDA 特征和 CLAM、LGSSL 等配套仓库(Software Dependencies)。 <!-- EN --> Plug-and-play engineering: one-line timm loading, pre-extracted TCGA / CPTAC / PANDA features, companion repos such as CLAM and LGSSL (Software Dependencies).

## 局限 / Limitations
- <!-- ZH --> 卡上:CC-BY-NC-ND 4.0,仅限非商业学术研究;禁止对模型及其衍生物(包括用 UNI 2 输出训练的模型、由 UNI 2 构建的数据集)做任何商业使用、出售或变现;下载即同意不分发、发布或复制模型副本(License)。 <!-- EN --> On the card: CC-BY-NC-ND 4.0, non-commercial academic research only; any commercial use, sale or monetization of the model and its derivatives (including models trained on UNI 2 outputs and datasets created from UNI 2) is prohibited; by downloading you agree not to distribute, publish or reproduce a copy of the model (License).
- <!-- ZH --> 我们的理解:没有 UNI2-h 自己的论文或技术报告(GitHub README 只有基准表和简短协议),训练数据组成、预处理、倍率都不透明;切片数在卡内前后不一致(30 万+ vs 35 万+)。 <!-- EN --> Our reading: there is no UNI2-h paper or technical report (the GitHub README has only benchmark tables and a short protocol), so data composition, preprocessing and magnification are opaque; the slide count is inconsistent within the card (300k+ vs 350k+).
- <!-- ZH --> 我们的理解:单一机构(MGB)数据,扫描仪/染色域偏移需要在我们的数据上检查;PathBench 中 UNI2 在非 TCGA 任务的排名下降,提示存在一定的域依赖。 <!-- EN --> Our reading: single-institution (MGB) data, so scanner/stain shift must be checked on our data; its drop in PathBench's non-TCGA ranking suggests some domain dependence.
- <!-- ZH --> 我们的理解:tile 级形态特征,不涉及转录组或空间组学;非专为异常检测设计。 <!-- EN --> Our reading: tile-level morphology only, no transcriptomics or spatial omics; not designed for anomaly detection.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 我们的理解:UNI2-h 是 **detect** 环节 H&E 模态的候选冻结 encoder。具体用法:把肾活检 WSI 切成 224 px tile → 提 1,536 维 CLS 特征 → 在健康参考组织 tile 上建 kNN / 密度 / 单类模型 → 用到最近健康特征的距离作为 tile 级异常分数,再聚合到区域或活检级。它也可以作为 H&E 侧的嵌入,与 Xenium / snRNA 特征做跨模态对齐(H&E 与分子模态是否一致)。PathBench 显示在 TCGA 任务上它与 Virchow2 等无显著差异(非 TCGA patch 级任务上 Virchow2 显著更高),所以选型时可同时提 UNI2-h 和 Virchow2 两套特征作对照。许可明确禁止由 UNI 2 构建的数据集的商业使用,并禁止分发模型副本;非商业地公开由其提取的特征是否允许,卡上没有写明——发布 benchmark 前应向授权方确认。
<!-- EN --> Our reading: UNI2-h is a candidate frozen encoder for the H&E modality in the **detect** stage. Concretely: tile kidney-biopsy WSIs at 224 px → extract 1,536-dim CLS features → fit kNN / density / one-class models on healthy reference tiles → use the distance to the nearest healthy features as a tile-level anomaly score, aggregated to region or biopsy level. It can also be the H&E-side embedding for cross-modal alignment with Xenium / snRNA features (does H&E agree with the molecular modality?). PathBench finds no significant difference from Virchow2 and others on TCGA tasks (Virchow2 is significantly higher on non-TCGA patch-level tasks), so extracting both feature sets for comparison is sensible. The licence explicitly bans commercial use of datasets created from UNI 2 and distribution of a copy of the model; whether a non-commercial release of extracted features is allowed is not stated on the card — check with the licensor before publishing a benchmark.

## 可复用资产 / Reusable assets
- <!-- ZH --> 权重(gated,需机构邮箱):`hf-hub:MahmoodLab/UNI2-h`;加载代码与 timm_kwargs 见 `ai-ready.md`。 <!-- EN --> Weights (gated, institutional e-mail): `hf-hub:MahmoodLab/UNI2-h`; loading code and timm_kwargs in `ai-ready.md`.
<!-- ZH/EN --> <https://huggingface.co/MahmoodLab/UNI2-h>
- <!-- ZH --> 预提取特征(TCGA、CPTAC、PANDA): <!-- EN --> Pre-extracted features (TCGA, CPTAC, PANDA):
<!-- ZH/EN --> <https://huggingface.co/datasets/MahmoodLab/UNI2-h-features>
- <!-- ZH --> 代码仓库(卡上 Repository 链接): <!-- EN --> Code repository (the card's Repository link):
<!-- ZH/EN --> <https://github.com/mahmoodlab/UNI>
- <!-- ZH --> 配套工具(卡上列出):CLAM(slide 分类)、LGSSL(linear probe 与 few-shot 评测)、ViT-Adapter / Mask2Former(分割)。 <!-- EN --> Companion tools listed on the card: CLAM (slide classification), LGSSL (linear-probe and few-shot evaluation), ViT-Adapter / Mask2Former (segmentation).

## 待读 / Follow-ups
- <!-- ZH --> UNI 论文 Chen et al., Nature Medicine 2024(doi:10.1038/s41591-024-02857-3)——前代 UNI 的方法与基准(卡要求引用它);本笔记只从中核对了 Mass-100K 的规模。 <!-- EN --> The UNI paper, Chen et al., Nature Medicine 2024 (doi:10.1038/s41591-024-02857-3) — method and benchmarks of the earlier UNI (the card asks to cite it); this note checked only the Mass-100K scale from it.
- <!-- ZH --> PathBench 的 Supplementary Tables 3–8:各模型预训练数据的组织组成(UNI2 未公开)。 <!-- EN --> PathBench Supplementary Tables 3–8: tissue composition of each model's pretraining data (not disclosed for UNI2).
- <!-- ZH --> 试验:在肾活检 tile 上对比 UNI2-h 与 Virchow2 特征的 kNN 异常评分。 <!-- EN --> Experiment: compare kNN anomaly scores from UNI2-h vs Virchow2 features on kidney-biopsy tiles.

## 图表 / Figures & tables
<!-- ZH --> 这是一个 **Hugging Face 模型卡片**,内容以说明文字与代码为主,**没有方法图/结果图,也没有定量基准表**(基准表在 GitHub README,见上)。页面上唯一的图片是申请访问的操作截图(`requesting_access.png`),不属于可复用的方法/结果图,故不收录。加载与使用见 `ai-ready.md` 中的 `timm.create_model(...)` 代码片段;定量基准请见 GitHub README §"Benchmarking UNI 2"(实验室自报)与本库的 PathBench 条目(独立评测);UNI 原论文(Chen et al., Nature Medicine 2024, doi:10.1038/s41591-024-02857-3)只含前代 UNI。原始模型卡片:<https://huggingface.co/MahmoodLab/UNI2-h>。
<!-- EN --> This is a **Hugging Face model card**, dominated by descriptive text and code, with **no method/result figures and no quantitative benchmark table** (the benchmark tables are in the GitHub README, see above). The only image on the page is an access-request screenshot (`requesting_access.png`), which is not a reusable method/result figure and is therefore omitted. For loading/usage see the `timm.create_model(...)` snippet in `ai-ready.md`; for quantitative benchmarks see the GitHub README section "Benchmarking UNI 2" (lab-reported) and this library's PathBench entry (independent); the UNI paper (Chen et al., Nature Medicine 2024, doi:10.1038/s41591-024-02857-3) covers only the earlier UNI. Model card: <https://huggingface.co/MahmoodLab/UNI2-h>.

## 引用 / Cite
```bibtex
@misc{MahmoodLab_UNI2h,
  title = {{MahmoodLab/UNI2-h}},
  author = {{Mahmood Lab}},
  howpublished = {Hugging Face model card},
  year = {2025},
  note = {ViT-H/14 pathology foundation model (released 01/2025). The card asks users to cite Chen et al., "Towards a general-purpose foundation model for computational pathology", Nature Medicine 2024, doi:10.1038/s41591-024-02857-3},
  url = {https://huggingface.co/MahmoodLab/UNI2-h}
}
```
