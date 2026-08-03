# MahmoodLab/UNI2-h

> **Bibkey** `uni2-h-model` · **Venue** Hugging Face () · **Category** foundation · **Relevance** medium · **Access** open
> **Link** <https://huggingface.co/MahmoodLab/UNI2-h>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> UNI2-h 是 Mahmood Lab 发布的病理学视觉基础模型:一个用 DINOv2 自监督、在 3 亿+ H&E/IHC 图块上预训练的 ViT-H/14 backbone,把 224×224 组织学 patch 编码成 1536 维特征,可直接作为下游分类/检索/MIL 的冻结特征提取器。
<!-- EN --> UNI2-h is Mahmood Lab's histopathology foundation model: a ViT-H/14 backbone self-supervised with DINOv2 on 200M+ H&E/IHC tiles, turning a 224×224 tissue patch into a 1536-dim embedding usable as a frozen feature extractor for downstream classification, retrieval and MIL.

## 研究问题 / Problem
<!-- ZH --> 计算病理学缺乏通用、可迁移的组织学表征:每个任务/器官/机构常需从头训练,标注昂贵且泛化差。UNI2-h 要提供一个跨组织类型、染色和任务的通用 patch 级 encoder,让下游只需轻量 probe 或 MIL 头即可达到强性能,降低对标注的依赖。
<!-- EN --> Computational pathology lacks a general, transferable histology representation — each task/organ/site often needs bespoke training with costly labels and poor generalization. UNI2-h aims to be a universal patch-level encoder across tissue types, stains and tasks, so downstream work needs only lightweight probes or MIL heads.

## 方法 / Method
<!-- ZH --> 作为“资源”而非实验,其核心是架构+自监督配方。架构是定制 ViT-H/14:depth 24、num_heads 24、embed_dim 1536、SwiGLU FFN(mlp_ratio≈2.667×2、act=SiLU)、init_values 1e-5、8 个 register tokens、no_embed_class、dynamic_img_size,共 681M 参数。自监督用 DINOv2 配方 = DINO 自蒸馏 + iBOT 掩码图像建模 + KoLeo 正则。训练在 A100 80GB 上以 bf16 + PyTorch-FSDP 完成。输出取 CLS token 得 1536 维特征。
<!-- EN --> As a resource, the core is architecture + SSL recipe. A custom ViT-H/14: depth 24, 24 heads, embed_dim 1536, SwiGLU FFN (mlp_ratio≈2.667×2, SiLU act), init_values 1e-5, 8 register tokens, no_embed_class, dynamic_img_size — 681M params. Pretraining uses the DINOv2 recipe = DINO self-distillation + iBOT masked-image modeling + KoLeo regularization, on A100 80GB with bf16 + PyTorch-FSDP. Inference returns the 1536-dim CLS token.

## 数据 / Data
<!-- ZH --> 预训练语料:来自 Mass General Brigham 机构的 30 万+ 张 H&E 与 IHC 玻片,采样出 2 亿+ 图块(model card 亦称 “3 亿+”表述,官方主述为 >200M tiles from >300k slides)。覆盖染色包含 H&E 和 IHC;具体倍率/器官分布未在 card 明列。相较前代 UNI(约 1 亿 tiles / 10 万 WSI),规模显著扩大且加入 IHC。
<!-- EN --> Pretraining corpus: 300k+ H&E and IHC slides from Mass General Brigham, sampled into 200M+ tiles (>200M tiles from >300k slides is the headline figure). Stains include H&E and IHC; exact magnification/organ breakdown is not enumerated on the card. Substantially larger than UNI v1 (~100M tiles / 100k WSIs) and adds IHC.

## 主要结果 / Key results
<!-- ZH --> Model card 未在此页给出定量基准表;定位为通用 backbone,支持 ROI 分类(logistic regression、k-NN、nearest-centroid)、ROI 最近邻检索、基于 MIL 的 slide 分类,并推荐在分割任务上微调。定量对比(TCGA/CPTAC 等下游)见 UNI 系列 Nature Medicine 论文(Chen et al. 2024)。（此页仅定性,无数字基准 / no numeric benchmarks on this page)
<!-- EN --> The card gives no quantitative benchmark table on this page; it is positioned as a general backbone supporting ROI classification (logistic regression, k-NN, nearest-centroid), ROI retrieval by nearest neighbors, MIL-based slide classification, and fine-tuning for segmentation. Quantitative comparisons live in the UNI-series Nature Medicine paper (Chen et al. 2024).

## 创新点 / Contributions
- <!-- ZH --> 规模化:>200M tiles / >300k slides,较 UNI v1 显著扩大,并纳入 IHC 染色。
- <!-- ZH --> 现代架构:ViT-H/14 + SwiGLU + register tokens + dynamic_img_size,遵循 DINOv2 最新配方。
- <!-- EN --> Scaled DINOv2 pretraining (>200M tiles / >300k slides) with a modern ViT-H (SwiGLU, 8 register tokens, dynamic sizing) producing a strong 1536-dim histology embedding.

## 局限 / Limitations
- <!-- ZH --> 许可严格:CC-BY-NC-ND 4.0,禁止商用与再分发,需机构邮箱 gating 审核。
- <!-- ZH --> patch 级、单张 H&E/IHC 形态学特征,不建模空间转录组/多组学,也非专为异常检测设计。
- <!-- ZH --> 训练数据单一机构(MGB),可能存在扫描仪/染色域偏移;此页无外部验证数字。
- <!-- EN --> Restrictive CC-BY-NC-ND 4.0 (no commercial use, no redistribution, gated); single-institution (MGB) data risks domain shift; patch-level morphology only, no spatial-omics and not tailored to anomaly detection.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 处在流水线的**特征提取 / 表征**这一环,是异常检测的上游 encoder。在“anomaly detection → virtual tissue → gene-revert”链条上:把 WSI 切成 224×224 patch,用 UNI2-h 冻结提取 1536 维特征,得到组织的形态学 embedding 空间;正常组织特征分布可用于建立 normal manifold,疾病/药物扰动导致的偏离即为异常(用 kNN 密度、one-class SVM、重构/流模型或 patch 到 slide 的 MIL 聚合来打分)。这些 patch embedding 也可作为“virtual tissue”形态学坐标,与空间转录组配准做形态↔基因联合建模,为后续 gene-revert 目标预测提供图像侧条件。可复用性高、即插即用,但需注意 NC-ND 许可仅限学术。
<!-- EN --> It sits at the **feature-extraction / representation** stage — the upstream encoder for anomaly detection. In our chain: tile a WSI into 224×224 patches, extract frozen 1536-dim UNI2-h features to get a morphology embedding space; fit a normal-tissue manifold and score disease/drug-perturbed deviations as anomalies (kNN density, one-class SVM, reconstruction/flow scoring, or MIL aggregation to slide level). The same patch embeddings serve as morphological coordinates for "virtual tissue," registrable to spatial transcriptomics for morphology↔gene joint modeling that conditions downstream gene-revert targets. Plug-and-play and reusable, but academic-only under NC-ND.

## 可复用资产 / Reusable assets
<!-- ZH --> 权重:`hf-hub:MahmoodLab/UNI2-h`(gated,需登录 + 机构邮箱审核)。加载:`timm.create_model(..., **timm_kwargs)`(见 ai-ready.md 完整 kwargs);预处理用 `timm.data.resolve_data_config` + `create_transform`,ImageNet 归一化(mean .485/.456/.406, std .229/.224/.225),输入 224×224,输出 1536-d CLS。下游示例:logistic regression / k-NN / nearest-centroid ROI 分类、NN 检索、MIL slide 分类;配套生态见 Mahmood Lab 的 UNI / CLAM / Trident 仓库。引用:Chen et al., Nature Medicine 2024, doi:10.1038/s41591-024-02857-3。
<!-- EN --> Weights `hf-hub:MahmoodLab/UNI2-h` (gated); load via `timm.create_model(..., **timm_kwargs)` with `resolve_data_config`+`create_transform`, ImageNet norm, 224×224 in → 1536-d CLS out. Downstream recipes (LR/k-NN/nearest-centroid, NN retrieval, MIL) and the UNI/CLAM/Trident ecosystem from Mahmood Lab. Cite Chen et al., Nature Medicine 2024.

## 待读 / Follow-ups
- <!-- ZH --> UNI 原论文 Chen et al., Nature Medicine 2024(doi:10.1038/s41591-024-02857-3)——定量基准与外部验证。
- <!-- ZH --> Mahmood Lab Trident/CLAM 工具链——WSI 分块、特征缓存、MIL 训练的工程范式。
- <!-- ZH --> 与其他病理 FM(Virchow2、GigaPath、CONCH)在异常检测任务上的对比。

## 图表 / Figures & tables

<!-- ZH --> 这是一个 **Hugging Face 模型卡片**,内容以说明文字与代码为主,**没有方法图/结果图,也没有定量基准表**。页面上唯一的图片是申请访问的操作截图(`requesting_access.png`),不属于可复用的方法/结果图,故不收录。加载与使用见 `ai-ready.md` 中的 `timm.create_model(...)` 代码片段;定量基准与外部验证请见 UNI 原论文(Chen et al., Nature Medicine 2024, doi:10.1038/s41591-024-02857-3)。原始模型卡片:<https://huggingface.co/MahmoodLab/UNI2-h>。
<!-- EN --> This is a **Hugging Face model card**, dominated by descriptive text and code, with **no method/result figures and no quantitative benchmark table**. The only image on the page is an access-request screenshot (`requesting_access.png`), which is not a reusable method/result figure and is therefore omitted. For loading/usage see the `timm.create_model(...)` snippet in `ai-ready.md`; quantitative benchmarks and external validation live in the UNI paper (Chen et al., Nature Medicine 2024, doi:10.1038/s41591-024-02857-3). Model card: <https://huggingface.co/MahmoodLab/UNI2-h>.

## 引用 / Cite
```bibtex
% no BibTeX fetched
```
