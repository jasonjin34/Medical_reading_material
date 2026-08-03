# MahmoodLab/UNI2-h

> **文献键** `uni2-h-model` · **来源** Hugging Face() · **类别** foundation · **相关度** medium · **获取** open
> **链接** <https://huggingface.co/MahmoodLab/UNI2-h> · `status: complete`

---

## 一句话
UNI2-h 是 Mahmood Lab 发布的病理学视觉基础模型:一个用 DINOv2 自监督、在 3 亿+ H&E/IHC 图块上预训练的 ViT-H/14 backbone,把 224×224 组织学 patch 编码成 1536 维特征,可直接作为下游分类/检索/MIL 的冻结特征提取器。

## 研究问题
计算病理学缺乏通用、可迁移的组织学表征:每个任务/器官/机构常需从头训练,标注昂贵且泛化差。UNI2-h 要提供一个跨组织类型、染色和任务的通用 patch 级 encoder,让下游只需轻量 probe 或 MIL 头即可达到强性能,降低对标注的依赖。

## 方法
作为“资源”而非实验,其核心是架构+自监督配方。架构是定制 ViT-H/14:depth 24、num_heads 24、embed_dim 1536、SwiGLU FFN(mlp_ratio≈2.667×2、act=SiLU)、init_values 1e-5、8 个 register tokens、no_embed_class、dynamic_img_size,共 681M 参数。自监督用 DINOv2 配方 = DINO 自蒸馏 + iBOT 掩码图像建模 + KoLeo 正则。训练在 A100 80GB 上以 bf16 + PyTorch-FSDP 完成。输出取 CLS token 得 1536 维特征。

## 数据
预训练语料:来自 Mass General Brigham 机构的 30 万+ 张 H&E 与 IHC 玻片,采样出 2 亿+ 图块(model card 亦称 “3 亿+”表述,官方主述为 >200M tiles from >300k slides)。覆盖染色包含 H&E 和 IHC;具体倍率/器官分布未在 card 明列。相较前代 UNI(约 1 亿 tiles / 10 万 WSI),规模显著扩大且加入 IHC。

## 主要结果
Model card 未在此页给出定量基准表;定位为通用 backbone,支持 ROI 分类(logistic regression、k-NN、nearest-centroid)、ROI 最近邻检索、基于 MIL 的 slide 分类,并推荐在分割任务上微调。定量对比(TCGA/CPTAC 等下游)见 UNI 系列 Nature Medicine 论文(Chen et al. 2024)。（此页仅定性,无数字基准 / no numeric benchmarks on this page)

## 创新点
- 规模化:>200M tiles / >300k slides,较 UNI v1 显著扩大,并纳入 IHC 染色。
- 现代架构:ViT-H/14 + SwiGLU + register tokens + dynamic_img_size,遵循 DINOv2 最新配方。

## 局限
- 许可严格:CC-BY-NC-ND 4.0,禁止商用与再分发,需机构邮箱 gating 审核。
- patch 级、单张 H&E/IHC 形态学特征,不建模空间转录组/多组学,也非专为异常检测设计。
- 训练数据单一机构(MGB),可能存在扫描仪/染色域偏移;此页无外部验证数字。

## 与本研究方向的关系
处在流水线的**特征提取 / 表征**这一环,是异常检测的上游 encoder。在“anomaly detection → virtual tissue → gene-revert”链条上:把 WSI 切成 224×224 patch,用 UNI2-h 冻结提取 1536 维特征,得到组织的形态学 embedding 空间;正常组织特征分布可用于建立 normal manifold,疾病/药物扰动导致的偏离即为异常(用 kNN 密度、one-class SVM、重构/流模型或 patch 到 slide 的 MIL 聚合来打分)。这些 patch embedding 也可作为“virtual tissue”形态学坐标,与空间转录组配准做形态↔基因联合建模,为后续 gene-revert 目标预测提供图像侧条件。可复用性高、即插即用,但需注意 NC-ND 许可仅限学术。

## 可复用资产
权重:`hf-hub:MahmoodLab/UNI2-h`(gated,需登录 + 机构邮箱审核)。加载:`timm.create_model(..., **timm_kwargs)`(见 ai-ready.md 完整 kwargs);预处理用 `timm.data.resolve_data_config` + `create_transform`,ImageNet 归一化(mean .485/.456/.406, std .229/.224/.225),输入 224×224,输出 1536-d CLS。下游示例:logistic regression / k-NN / nearest-centroid ROI 分类、NN 检索、MIL slide 分类;配套生态见 Mahmood Lab 的 UNI / CLAM / Trident 仓库。引用:Chen et al., Nature Medicine 2024, doi:10.1038/s41591-024-02857-3。

## 待读
- UNI 原论文 Chen et al., Nature Medicine 2024(doi:10.1038/s41591-024-02857-3)——定量基准与外部验证。
- Mahmood Lab Trident/CLAM 工具链——WSI 分块、特征缓存、MIL 训练的工程范式。
- 与其他病理 FM(Virchow2、GigaPath、CONCH)在异常检测任务上的对比。

## 引用
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
