# MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics

> **Bibkey** `Xu_2025` · **Venue** AAAI 2025 (Proceedings of the AAAI Conference on Artificial Intelligence 39(12)) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1609/aaai.v39i12.33409> · arXiv extended version: <https://arxiv.org/abs/2412.10659>
> `status: complete` — 基于 AAAI 开放 PDF 正文精读;补充材料(含 PSC 结果、理论证明)未读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> MEATRD 是 STANDS 同组(Xu、Sun 等)的后续工作:**只用正常组织训练**,把每个 Visium spot 作为图节点,同时重建其 H&E 图块与基因表达(核心是带目标节点 masking 的图双注意力 Transformer,MGDAT),再在**潜在多模态重建误差**上训练 Deep-SVDD 式的单类分类器做异常打分;在 8 个人乳腺癌 ST 数据上平均 AUC 0.723 / F1 0.741,超过 9 个图像、ST 与多模态基线,并能抓住肉眼难辨的肿瘤边缘。
<!-- EN --> MEATRD is a follow-up from the STANDS group (Xu, Sun et al.): **trained only on normal tissue**, it treats each Visium spot as a graph node, reconstructs both its H&E patch and its gene expression (core: a masked graph dual-attention transformer, MGDAT, with target-node masking), then trains a Deep-SVDD-style one-class classifier on **latent multimodal reconstruction errors** for anomaly scoring. On 8 human breast-cancer ST datasets it reaches mean AUC 0.723 / F1 0.741, beating 9 image, ST and multimodal baselines, and catches visually subtle tumour edges.

## 研究问题 / Problem
<!-- ZH --> 异常组织区域(ATR)检测传统上只靠 H&E 图像,但组织学图像复杂、ATR 与正常组织视觉差异细微、染色质量不一,纯图像方法在「看起来正常」的区域(如肿瘤边缘)会失败。ST 提供分子视角,却噪声大、缺失多;唯一的 ST-only 方法 Spatial-ID 基于分类不确定性,容易把正常组织间的相似性误判为异常。缺少能融合图像与 ST、且对重建式方法常见的**过度泛化**(异常也被重建得很好)和单类方法常见的**参照-目标域偏移**都稳健的方法。
<!-- EN --> Anomalous tissue region (ATR) detection traditionally uses H&E alone, but histology is complex, ATRs can look nearly normal, and staining varies — image-only methods fail on visually normal-looking regions such as tumour edges. ST offers a molecular view but is noisy with many dropouts; the only ST-only method, Spatial-ID, relies on classification uncertainty and confuses similarity among normal tissues with anomaly. What is missing is a method that fuses image and ST and is robust both to **over-generalization** in reconstruction methods (anomalies reconstructed too well) and to **reference–target domain shift** in one-class methods.

## 方法 / Method
<!-- ZH --> 问题设定:在正常参照 ST + 图像上训练,在目标切片上找异常 spot。三阶段:**Stage I**——以每个 spot 为中心切 32×32 图块,用 Mobile-UNet(SSIM 感知损失 + L1)预训练图像编码器得到图像嵌入;基因数据不做预训练,用两层 MLP 投影。**Stage II**——spot 作为 kNN 图(k=6,对应六边形排列)节点,取目标节点 3 跳子图;**目标节点的图像与基因特征都替换成可学习 mask token**,防止自身信息泄漏(缓解过度泛化);每个 MGDAT block 先用 Transformer 把两模态拼接生成低维**融合瓶颈嵌入**(跨模态),再与各模态嵌入拼接做图注意力聚合(跨节点);用 ResNet 反卷积解码器重建图块、单层 GNN 解码器重建表达,损失 = α·(SSIM+L1) + (1−α)·缩放余弦误差(SCE)。**Stage III**——用轻量 ResNet / MLP 把原始与重建结果映射到潜空间,β 加权融合后取差值作为**潜在多模态重建误差**,再把正常 spot 的误差压到超球中心 c(Deep SVDD 式);anomaly score = 到 c 的距离,阈值由 MAP-EM 混合模型自动确定。补充材料给出瓶颈嵌入信息性质的理论分析。
<!-- EN --> Setting: train on normal reference ST + images, find anomalous spots in a target slice. Three stages: **Stage I** — cut a 32×32 patch around each spot and pretrain a Mobile-UNet image encoder (SSIM perceptual + L1 loss); genes get no pretext stage, just a two-layer MLP projection. **Stage II** — spots are nodes of a kNN graph (k=6, hexagonal layout), with a 3-hop subgraph per target node; **the target node's image and gene features are both replaced by learnable mask tokens** to prevent self-information leakage (curbing over-generalization); each MGDAT block first uses a Transformer over the concatenated modalities to produce a low-dimensional **fused bottleneck embedding** (cross-modal), then concatenates it with each modality's embedding for graph-attention aggregation (cross-node); a ResNet deconvolutional decoder rebuilds the patch and a single-layer GNN decoder rebuilds expression, with loss α·(SSIM+L1) + (1−α)·scaled cosine error (SCE). **Stage III** — light ResNet / MLP encoders map originals and reconstructions to a latent space; the β-weighted fused difference is the **latent multimodal reconstruction error**, and normal spots' errors are collapsed to a hypersphere centre c (Deep SVDD style); the anomaly score is the distance to c, thresholded automatically with a MAP-EM mixture model. The supplement gives a theoretical analysis of the bottleneck embedding's information properties.

## 数据 / Data
<!-- ZH --> 训练:8 个人正常乳腺 10x Visium 数据(10x-hNB-v03 至 v10);测试:8 个人乳腺癌 10x Visium 数据(10x-hBC-A1 至 H1),外加 10x-hBC-I1(含视觉上与正常组织相近的肿瘤边缘)做案例分析;另有 4 个原发性硬化性胆管炎(PSC)数据,结果在补充材料。
<!-- EN --> Training: 8 human normal-breast 10x Visium datasets (10x-hNB-v03 to v10); testing: 8 human breast-cancer 10x Visium datasets (10x-hBC-A1 to H1), plus 10x-hBC-I1 (with a tumour edge visually similar to normal tissue) for a case study; 4 primary sclerosing cholangitis (PSC) datasets are reported in the supplement.

## 主要结果 / Key results
- <!-- ZH --> **8 个乳腺癌数据**:MEATRD 在全部数据集 AUC 第一,6/8 数据集 F1 第一;平均 AUC 0.723、F1 0.741。作者称相对第二名平均提升 AUC 17.45%、F1 10.31%。基线包括图像类(Patch SVDD、SimpleNet、f-AnoGAN)、ST 类(scmap、CAMLU、PREM、DOMINANT、Spatial-ID)和多模态 M3DM;从 PDF 表格读到图卷积方法 DOMINANT 是平均 AUC 最好的基线(约 0.55)。 <!-- EN --> **8 breast-cancer datasets**: MEATRD ranks first in AUC on every dataset and first in F1 on 6/8; mean AUC 0.723, F1 0.741. The authors report average gains over the runner-up of 17.45% AUC and 10.31% F1. Baselines are image-based (Patch SVDD, SimpleNet, f-AnoGAN), ST-based (scmap, CAMLU, PREM, DOMINANT, Spatial-ID) and multimodal M3DM; the PDF table shows the graph method DOMINANT as the best baseline by mean AUC (~0.55).
- <!-- ZH --> **总体规律**:用 ST 的方法普遍优于只用图像的方法;忽略 spot 空间关系的多模态 M3DM 不如 MEATRD——说明空间上下文很重要。 <!-- EN --> **General pattern**: methods using ST generally beat image-only ones; the multimodal M3DM, which ignores spatial relations between spots, trails MEATRD — spatial context matters.
- <!-- ZH --> **视觉相近的肿瘤边缘(10x-hBC-I1)**:降低图像权重的 MEATRD-β(β 0.5→0.1)precision 0.693 / recall 0.895,标准 MEATRD 0.672 / 0.666,DOMINANT 0.648 / 0.780,SimpleNet 0.632 / 0.410,f-AnoGAN 0 / 0。即在这种场景下图像几乎不提供额外信息,要更依赖 ST。 <!-- EN --> **Visually subtle tumour edge (10x-hBC-I1)**: MEATRD-β (image weight β 0.5→0.1) gets precision 0.693 / recall 0.895, standard MEATRD 0.672 / 0.666, DOMINANT 0.648 / 0.780, SimpleNet 0.632 / 0.410, f-AnoGAN 0 / 0 — here the image adds little and ST should be weighted more.
- <!-- ZH --> **消融(平均 AUC / F1)**:完整 0.723 / 0.741;仅 ST 0.631 / 0.667;仅图像 0.497 / 0.544;去 MGDAT 0.639 / 0.689;去目标节点 masking 0.655 / 0.699;去重建误差输入(改用嵌入)0.642 / 0.685;去单类阶段 0.584 / 0.631。MGDAT 层数 4 时明显崩(0.533 / 0.565)。 <!-- EN --> **Ablation (mean AUC / F1)**: full 0.723 / 0.741; ST only 0.631 / 0.667; image only 0.497 / 0.544; w/o MGDAT 0.639 / 0.689; w/o target-node masking 0.655 / 0.699; w/o reconstruction-error input (embeddings instead) 0.642 / 0.685; w/o one-class stage 0.584 / 0.631. Four MGDAT layers collapse performance (0.533 / 0.565).

## 创新点 / Contributions
- <!-- ZH --> 把「重建式」与「单类分类」两种异常检测范式串联:在重建误差(而非实例嵌入)上做单类分类,同时缓解过度泛化与域偏移。 <!-- EN --> Chains the reconstruction and one-class paradigms: one-class classification on reconstruction errors (not instance embeddings) addresses both over-generalization and domain shift.
- <!-- ZH --> MGDAT:融合瓶颈嵌入做跨模态共享 + 图注意力做跨 spot 共享 + 目标节点 masking 防泄漏。 <!-- EN --> MGDAT: fused bottleneck for cross-modal sharing + graph attention for cross-spot sharing + target-node masking against leakage.
- <!-- ZH --> 理论分析多模态瓶颈嵌入收集并压缩模态特异、任务相关信息(补充材料 D)。 <!-- EN --> Theoretical analysis that the multimodal bottleneck collects and condenses modality-specific, task-relevant information (Supplement D).
- <!-- ZH --> 证明 ST 能检出视觉上不明显的 ATR,并提供可调的模态权重 β。 <!-- EN --> Shows ST can detect visually inconspicuous ATRs, with a tunable modality weight β.

## 局限 / Limitations
- <!-- ZH --> 评估几乎只在乳腺癌 Visium 上(PSC 仅在补充材料);ATR 标签是区域级病理注释,肿瘤是相对「容易」的异常。 <!-- EN --> Evaluation is almost entirely breast-cancer Visium (PSC only in the supplement); ATR labels are region-level pathology annotations, and tumour is a relatively "easy" anomaly.
- <!-- ZH --> 自称「首个整合组织学与 ST 的 ATR 方法」,但同组此前的 STANDS(也用图像 + ST)不在正文基线中——比较不完整。 <!-- EN --> Claims to be the "first" method integrating histology and ST for ATR detection, yet the group's earlier STANDS (also image + ST) is not among the main-text baselines — an incomplete comparison.
- <!-- ZH --> 最佳模态权重 β 依场景而变(肿瘤边缘需 β=0.1),但在无标签的实际使用中如何选 β 没有答案。 <!-- EN --> The best modality weight β depends on the scenario (β=0.1 for tumour edges), with no answer for choosing β without labels.
- <!-- ZH --> 阈值依赖 MAP-EM 混合模型,假设正常/异常分数之间有间隙;F1 评估用了「真实异常比例」作阈值,实际部署时不可得。 <!-- EN --> Thresholding relies on a MAP-EM mixture that assumes a gap between normal and anomalous scores; F1 is evaluated at the true anomaly proportion, which is unknown in deployment.
- <!-- ZH --> 32×32 图块、spot 级(55 µm)分辨率;未涉及单细胞分辨率平台。 <!-- EN --> 32×32 patches at spot (55 µm) resolution; single-cell-resolution platforms are not addressed.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> MEATRD 是 detect 阶段**多模态(H&E + ST)正常-only 训练**的代表方法,与 STANDS(`spatial-natcommun-2024`)同源、与 Sardine(`sardine-bioinformatics-2025`)的统计路线互补。对 **伪影注入课题** 最直接的启示是**跨模态一致性**:本文的 10x-hBC-I1 案例恰好说明「图像正常 + 表达异常」是真实存在的疾病信号(肿瘤边缘),而不是 artifact——所以伪影注入课题不能简单地把「模态间不一致」都当 artifact;需要区分「图像看不出但多个分子模态一致异常」(疾病)与「只有一个分子模态异常、且与 QC 指标相关」(artifact)。配对的 Xenium + H&E 正好是 MEATRD 的输入形态,可作为 KidneyAnomalyBench 的多模态深度基线(需把 spot 换成细胞或 bin,并用 KPMP / HuBMAP 正常肾作为参照)。另外,β 无法无监督选择、阈值依赖真实异常比例,这两个问题正是专家验证 benchmark 能帮忙校准的地方。对 **Agent 可信度课题**:「首个」类表述与基线遗漏(STANDS)是 claim-to-evidence 核查的典型对象——verifier 应能检出「novelty 声明 vs 相关工作覆盖」的不一致。
<!-- EN --> MEATRD is the representative **multimodal (H&E + ST), normal-only-trained** method for the detect stage, sibling to STANDS (`spatial-natcommun-2024`) and complementary to the statistical route of Sardine (`sardine-bioinformatics-2025`). The most direct lesson for **the artifact-injection topic** concerns **cross-modal agreement**: the 10x-hBC-I1 case shows that "normal-looking image + abnormal expression" is a real disease signal (tumour edge), not an artifact — so the artifact-injection topic cannot treat every cross-modal disagreement as artifact; it must separate "invisible in image but consistently abnormal across molecular modalities" (disease) from "abnormal in only one molecular modality and correlated with QC metrics" (artifact). Paired Xenium + H&E matches MEATRD's input form, making it a multimodal deep baseline for KidneyAnomalyBench (with spots replaced by cells or bins and KPMP / HuBMAP normal kidney as the reference). The unsupervised choice of β and the threshold's dependence on the true anomaly fraction are exactly what an expert-validated benchmark can help calibrate. For **the agent-trustworthiness topic**: "first-ever" claims alongside a missing baseline (STANDS) are textbook targets for claim-to-evidence checking — a verifier should flag inconsistency between novelty claims and related-work coverage.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码**: <!-- EN --> **Code**:
<!-- ZH/EN --> <https://github.com/wqlzuel/MEATRD>
- <!-- ZH --> **扩展版(含补充材料)**: <!-- EN --> **Extended version (with supplement)**:
<!-- ZH/EN --> <https://arxiv.org/abs/2412.10659>
- <!-- ZH --> **基准设定**:正常乳腺 10x-hNB-v03–v10 训练 → 乳腺癌 10x-hBC-A1–H1 测试,AUC + F1(阈值 = 真实异常比例),5 次运行均值±标准差;9 个基线的清单可直接复用。 <!-- EN --> **Benchmark setup**: train on normal breast 10x-hNB-v03–v10 → test on breast cancer 10x-hBC-A1–H1, AUC + F1 (threshold = true anomaly proportion), mean ± s.d. over 5 runs; the 9-baseline list is reusable.

## 待读 / Follow-ups
- <!-- ZH --> arXiv 扩展版的补充材料:PSC 结果、MAP-EM 阈值、瓶颈嵌入理论、复杂度分析。 <!-- EN --> The arXiv supplement: PSC results, MAP-EM thresholding, bottleneck theory, complexity analysis.
- <!-- ZH --> 与 STANDS 在同一数据上的直接对比(本文未做)。 <!-- EN --> A head-to-head with STANDS on the same data (not done here).
- <!-- ZH --> Spatial-ID、CAMLU、DOMINANT 原文——ST / 图异常检测基线。 <!-- EN --> Spatial-ID, CAMLU, DOMINANT papers — ST / graph anomaly baselines.
- <!-- ZH --> 把 Mobile-UNet 图像编码器换成病理基础模型(UNI2-h、Virchow)是否提升。 <!-- EN --> Whether swapping the Mobile-UNet encoder for a pathology foundation model (UNI2-h, Virchow) helps.

## 引用 / Cite
```bibtex
@article{Xu_2025, title={MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics}, volume={39}, ISSN={2159-5399}, url={http://dx.doi.org/10.1609/aaai.v39i12.33409}, DOI={10.1609/aaai.v39i12.33409}, number={12}, journal={Proceedings of the AAAI Conference on Artificial Intelligence}, publisher={Association for the Advancement of Artificial Intelligence (AAAI)}, author={Xu, Kaichen and Wu, Qilong and Lu, Yan and Zheng, Yinan and Li, Wenlin and Tang, Xingjie and Wang, Jun and Sun, Xiaobo}, year={2025}, month=Apr, pages={12918–12926} }
```
