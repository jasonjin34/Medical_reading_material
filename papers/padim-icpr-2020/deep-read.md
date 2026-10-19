# PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization

> **Bibkey** `Defard2020_201108785` · **Venue** ICPR 2020 International Workshops and Challenges, LNCS 12664 (2021) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2011.08785> · DOI <https://doi.org/10.1007/978-3-030-68799-1_35>
> `status: complete` — 基于 arXiv v1 全文精读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> PaDiM 不训练任何网络:用 ImageNet 预训练 CNN 的多层特征给每个 patch 位置做 embedding,在每个位置上对正常训练图像拟合一个多元高斯 N(μ_ij, Σ_ij),测试时用 **Mahalanobis 距离**作为 patch 级异常分数,得到异常图;在 MVTec AD 上做到 97.5% 像素级 AUROC / 92.1% PRO,且推理成本与训练集大小无关。
<!-- EN --> PaDiM trains no network at all: it embeds every patch position with multi-layer features from an ImageNet-pretrained CNN, fits one multivariate Gaussian N(μ_ij, Σ_ij) per position over the normal training images, and at test time scores each patch by its **Mahalanobis distance** to produce an anomaly map — reaching 97.5% pixel AUROC / 92.1% PRO on MVTec AD with inference cost independent of training-set size.

## 研究问题 / Problem
<!-- ZH --> 在 one-class 设定(训练集只有正常样本)下同时做**异常检测(图像级)与定位(像素/patch 级)**。当时两条路线各有短板:重建类(AE/VAE/GAN)直观但 AE 常把异常也重建得很好;embedding 相似度类(SPADE、Patch SVDD)效果最好,但 SPADE 在测试时对整个训练 embedding 集跑 K-NN,时间和内存随训练集线性增长,不利于工业部署。PaDiM 要的是"SPADE 级别的精度 + 与训练集规模无关的推理复杂度"。
<!-- EN --> Joint **anomaly detection (image level) and localization (pixel/patch level)** in the one-class setting (normal-only training data). Both existing routes had drawbacks: reconstruction methods (AE/VAE/GAN) are intuitive but AEs often reconstruct anomalies well too; embedding-similarity methods (SPADE, Patch SVDD) were best, but SPADE runs K-NN over the whole training embedding set at test time, so time and memory grow linearly with training size — a deployment problem. PaDiM targets "SPADE-level accuracy with inference complexity independent of training-set size."

## 方法 / Method
<!-- ZH --> **(1) Patch embedding**:与 SPADE 相同,把预训练 CNN(ResNet18、Wide-ResNet-50-2 或 EfficientNet-B5,均为 ImageNet 预训练)前三层的激活图按空间位置对齐并**拼接**,使每个位置 (i,j) 的向量同时携带细粒度与语义信息;网格大小 = 所用最大激活图的分辨率。**随机降维**:从拼接后的维度(R18 为 448 维)中随机挑 100 或 550 维,作者发现这比 PCA 更好。**(2) 学习正常性**:对 N 张正常训练图在位置 (i,j) 的 embedding 集合 X_ij,假设其服从多元高斯,估计样本均值 μ_ij 与协方差 Σ_ij = 1/(N−1) Σ(x−μ)(x−μ)ᵀ + εI(ε=0.01,保证可逆);因为 embedding 来自多个层,Σ_ij 天然编码了**跨语义层的相关性**。**(3) 推理**:受 Rippel 等(MahalanobisAD)与 Lee 等(OOD 检测中的 Mahalanobis 置信分)启发,对测试 patch 计算 M(x_ij) = sqrt((x−μ_ij)ᵀ Σ_ij⁻¹ (x−μ_ij)),得到异常图;图像级分数 = 异常图最大值。预处理沿用 SPADE:缩放到 256×256、中心裁剪 224×224,异常图用 σ=4 高斯平滑。整个"训练"只是一次前向 + 协方差估计,无梯度优化。
<!-- EN --> **(1) Patch embedding**: as in SPADE, activation maps from the first three layers of a pretrained CNN (ResNet18, Wide-ResNet-50-2 or EfficientNet-B5, all ImageNet-pretrained) are spatially aligned and **concatenated**, so the vector at each position (i,j) carries both fine-grained and semantic information; the grid equals the resolution of the largest activation map used. **Random dimensionality reduction**: randomly keep 100 or 550 of the concatenated dimensions (448 for R18) — which the authors find beats PCA. **(2) Learning normality**: for the N normal training images' embeddings X_ij at position (i,j), assume a multivariate Gaussian and estimate the sample mean μ_ij and covariance Σ_ij = 1/(N−1) Σ(x−μ)(x−μ)ᵀ + εI (ε = 0.01 to keep it invertible); since embeddings span several layers, Σ_ij naturally encodes **inter-layer correlations**. **(3) Inference**: inspired by Rippel et al. (MahalanobisAD) and Lee et al. (Mahalanobis confidence scores for OOD detection), each test patch is scored by M(x_ij) = sqrt((x−μ_ij)ᵀ Σ_ij⁻¹ (x−μ_ij)), forming the anomaly map; image score = map maximum. Preprocessing follows SPADE (resize 256×256, centre-crop 224×224; σ = 4 Gaussian smoothing of the map). "Training" is a single forward pass plus covariance estimation — no gradient optimization.

## 方法谱系 / Method lineage
<!-- ZH --> **范式:feature-embedding & memory bank**(具体是其中的"参数化密度"分支 —— 每个位置一个高斯,本质上也是 density / one-class 思想)。**承接**:Lee 等 2018 在分类器特征上用类条件高斯 + Mahalanobis 做 OOD 检测;Rippel 等 2020(MahalanobisAD)把它搬到图像级异常检测;SPADE 提出用预训练多层特征做 patch 级 K-NN 定位。PaDiM 的贡献是把"全局高斯"变成"**每个 patch 位置一个高斯**",并保留跨层协方差。**影响**:PatchCore 明确把 PaDiM 作为最相关的前作并指出其局限(依赖图像对齐、每个 patch 只和同位置统计比较);CFLOW-AD 证明在 MVG 先验下 normalizing flow 的目标退化为 Mahalanobis 距离,并把 PaDiM 的多尺度 pooling 设置原样沿用。PaDiM 现在是 anomalib 等库里的标准基线。
<!-- EN --> **Paradigm: feature-embedding & memory bank** (specifically its parametric-density branch — one Gaussian per position, so also density / one-class in spirit). **Builds on**: Lee et al. 2018 (class-conditional Gaussians + Mahalanobis on classifier features for OOD detection); Rippel et al. 2020 (MahalanobisAD) moving that to image-level AD; SPADE's pretrained multi-layer features with patch-level K-NN localization. PaDiM's step is from one global Gaussian to **one Gaussian per patch position**, keeping inter-layer covariance. **Led to**: PatchCore names PaDiM as its closest predecessor and targets its limits (alignment dependence; each patch compared only to same-position statistics); CFLOW-AD shows that under an MVG prior the normalizing-flow objective reduces to the Mahalanobis distance and reuses PaDiM's pyramid-pooling setup verbatim. PaDiM is now a standard baseline in libraries such as anomalib.

## 数据 / Data
<!-- ZH --> **MVTec AD**:15 类(10 物体 + 5 纹理),每类约 240 张,原分辨率 700²–1024²,物体类都居中对齐。**Rd-MVTec AD**(作者新建):对训练和测试集都施加随机旋转(−10°,+10°)和随机裁剪(256→224),模拟非对齐场景,随机 5 次取平均。**ShanghaiTech Campus (STC)**:静态摄像头监控视频,274,515 训练帧 / 42,883 测试帧,13 个场景,856×480。
<!-- EN --> **MVTec AD**: 15 classes (10 objects + 5 textures), ~240 images each, native 700²–1024², objects centred and aligned. **Rd-MVTec AD** (new): random rotation (−10°, +10°) and random crop (256→224) applied to both train and test sets to simulate misalignment, averaged over 5 random versions. **ShanghaiTech Campus (STC)**: static-camera surveillance video, 274,515 train / 42,883 test frames across 13 scenes at 856×480.

## 主要结果 / Key results
- <!-- ZH --> **定位(MVTec AD)**:PaDiM-WR50-Rd550 全类平均 (AUROC 97.5%, PRO 92.1%),超过 SPADE (96.5, 91.7) 和 Patch SVDD (95.7, –);纹理类上领先最多:比 SPADE 高 4.0 个百分点 AUROC、4.8 个百分点 PRO。轻量的 PaDiM-R18-Rd100 也有 (96.7, 90.1)。 <!-- EN --> **Localization (MVTec AD)**: PaDiM-WR50-Rd550 averages (AUROC 97.5%, PRO 92.1%) over all classes, above SPADE (96.5, 91.7) and Patch SVDD (95.7, –); the gap is largest on textures — +4.0 pp AUROC and +4.8 pp PRO over SPADE. The light PaDiM-R18-Rd100 reaches (96.7, 90.1).
- <!-- ZH --> **检测(图像级 AUROC)**:PaDiM-WR50-Rd550 95.3%,略低于 MahalanobisAD(EfficientNet-B4)的 95.8%;PaDiM-EfficientNet-B5 达到 **97.9%**,比所有方法至少高 2.6 个百分点。 <!-- EN --> **Detection (image AUROC)**: PaDiM-WR50-Rd550 95.3%, slightly below MahalanobisAD (EfficientNet-B4) at 95.8%; PaDiM-EfficientNet-B5 reaches **97.9%**, at least 2.6 pp above every method.
- <!-- ZH --> **跨层相关性消融(R18)**:单层最好 96.0/89.0 的"三层分数相加"对比建模跨层协方差的 PaDiM-R18 为 97.1/90.8(+1.1 AUROC、+1.8 PRO)。**降维**:随机 100 维 (96.7, 90.5) 明显优于 PCA 100 维 (93.5, 85.7),与全 448 维 (97.1, 90.8) 几乎持平。 <!-- EN --> **Inter-layer ablation (R18)**: summing three per-layer models gives 96.0/89.0 vs 97.1/90.8 for PaDiM-R18 with cross-layer covariance (+1.1 AUROC, +1.8 PRO). **Dim. reduction**: random 100-d (96.7, 90.5) clearly beats PCA 100-d (93.5, 85.7) and nearly matches full 448-d (97.1, 90.8).
- <!-- ZH --> **非对齐鲁棒性(Rd-MVTec AD)**:PaDiM-WR50-Rd550 (92.2, 73.1) vs SPADE (87.2, 69.0) vs VAE (62.1, 27.8);相对原始 MVTec,PaDiM 的 AUROC 降 5.3 个百分点,VAE 和 SPADE 分别降 12.2 和 8.8。 <!-- EN --> **Misalignment robustness (Rd-MVTec AD)**: PaDiM-WR50-Rd550 (92.2, 73.1) vs SPADE (87.2, 69.0) vs VAE (62.1, 27.8); relative to standard MVTec, PaDiM's AUROC drops 5.3 pp vs 12.2 (VAE) and 8.8 (SPADE).
- <!-- ZH --> **STC 定位**:PaDiM-R18-Rd100 91.2% AUROC,SPADE 89.9%,CAVGA-RU 85%。 <!-- EN --> **STC localization**: PaDiM-R18-Rd100 91.2% AUROC vs SPADE 89.9% and CAVGA-RU 85%.
- <!-- ZH --> **复杂度**:CPU 推理 SPADE 7.10 s/图,PaDiM-WR50-Rd550 0.95 s,PaDiM-R18-Rd100 0.23 s;内存 SPADE 在 STC 上要 37 GB,PaDiM-WR50-Rd550 5.2 GB。训练(CPU 串行)每个 MVTec 类约 150 s。 <!-- EN --> **Cost**: CPU inference 7.10 s/image for SPADE vs 0.95 s (PaDiM-WR50-Rd550) and 0.23 s (PaDiM-R18-Rd100); memory on STC 37 GB for SPADE vs 5.2 GB for PaDiM-WR50-Rd550. Training (serial CPU) takes ~150 s per MVTec class.

## 创新点 / Contributions
- <!-- ZH --> 把"高斯 + Mahalanobis"从图像级推进到**逐 patch 位置**,第一次让参数化密度模型在定位任务上达到 SOTA。 <!-- EN --> Pushes "Gaussian + Mahalanobis" from image level to **per patch position**, making a parametric density model state-of-the-art for localization for the first time.
- <!-- ZH --> 多层 embedding 拼接后用完整协方差建模**跨语义层相关性**,并用消融证明其价值。 <!-- EN --> Models **inter-semantic-level correlations** via full covariance over concatenated multi-layer embeddings, with ablations showing the gain.
- <!-- ZH --> 发现随机降维优于 PCA(高方差方向未必是区分正常/异常的方向)。 <!-- EN --> Finds random dimensionality reduction beats PCA (high-variance directions are not necessarily the discriminative ones).
- <!-- ZH --> 提出非对齐评测(Rd-MVTec AD),推理时间与内存与训练集规模无关。 <!-- EN --> Introduces a misaligned evaluation (Rd-MVTec AD); inference time and memory independent of training-set size.

## 局限 / Limitations
- <!-- ZH --> **位置绑定**:每个 (i,j) 一个高斯,隐含"同一位置在所有图像里语义一致"的假设,需要对齐;训练和测试图像必须同尺寸(PatchCore 正是针对这一点)。 <!-- EN --> **Position-bound**: one Gaussian per (i,j) assumes the same position means the same thing across images — it needs alignment, and train/test images must share a shape (exactly what PatchCore targets).
- <!-- ZH --> **单峰高斯假设**:每个位置一个高斯,无法表达多模态正常分布。 <!-- EN --> **Unimodal Gaussian**: one Gaussian per position cannot represent multimodal normality.
- <!-- ZH --> 内存随图像分辨率增长(要存 H×W 个 D×D 协方差逆矩阵);完全依赖 ImageNet 特征的可迁移性,无域适应。 <!-- EN --> Memory grows with image resolution (H×W inverse D×D covariances stored); fully reliant on ImageNet feature transferability with no domain adaptation.
- <!-- ZH --> 只在工业与监控数据上验证;图像级阈值未讨论。 <!-- EN --> Validated only on industrial and surveillance data; no discussion of how to set an operating threshold.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> PaDiM 是 detect 阶段**最简单、可解释的"健康参考 → 距离"基线**,值得作为 Plan A 的第一个下限。**映射到肾脏组学**:样本 = 细胞或 Xenium/Visium spot;"正常训练集" = 健康肾参考(Lake 图谱、KPMP/HuBMAP 正常供体、95 例活检中的正常对照);特征空间 = scVI / scArches 潜空间或单细胞基础模型 embedding;H&E 端则是 UNI2-h / Virchow 的 patch embedding。PaDiM 的"每个位置一个高斯"在组学里最自然的对应是**"每个细胞类型(或每个解剖小区:肾小球 / 近端小管 / 间质)一个高斯"**——用 Mahalanobis 距离衡量一个细胞偏离其所属类型的健康分布多远,这就是 PaDiM 的条件化版本。**哪些假设会破**:(1) PaDiM 依赖"位置对齐",组学里对应的是"细胞类型注释正确" —— 注释错了,细胞会被拿去和错误的高斯比较,假阳性爆发;(2) 单峰高斯在连续状态(近端小管 healthy → injured → failed-repair 的连续轴)上不成立;(3) batch effect、ambient RNA、doublet 都会让细胞在 embedding 里"远离"均值,Mahalanobis 无法区分技术伪影与疾病 —— 这正是 Plan A 用**跨模态一致性**(snRNA ↔ snATAC ↔ Xenium ↔ H&E)去分辨的问题;(4) 组学里没有像素级 mask,PRO / 像素 AUROC 无从计算,需要 KidneyAnomalyBench 用专家标注或合成扰动来代替。**仓库里已有的同类思想**:healthy-ref-natgenet-2023 在 scVI 健康图谱潜空间上找疾病态(但用 Milo 差异丰度而非距离分数);pathology-ad-bench-mlhealth-2025 把 PaDiM 放在"feature distribution"家族里直接在 Camelyon16、Crohn 结肠和小鼠肾小球上评测,结论是该家族整体最好但真实病理远难于工业数据;histo-nejmai-2024 用病理基础模型特征 + kNN 距离打分,是同一"预训练特征 + 距离"范式。PaDiM 的"随机降维优于 PCA"也提醒我们:在 scVI/PCA 潜空间里,高方差主成分往往是批次或细胞类型,而非病变方向。
<!-- EN --> PaDiM is the **simplest, interpretable "healthy reference → distance" baseline** for the detect stage and a natural floor for Plan A. **Mapping to kidney omics**: samples = cells or Xenium/Visium spots; "normal training set" = a healthy kidney reference (Lake atlas, KPMP/HuBMAP healthy donors, normal controls among the 95 biopsies); feature space = scVI / scArches latent space or single-cell foundation-model embeddings, and UNI2-h / Virchow patch embeddings on the H&E side. PaDiM's "one Gaussian per position" maps most naturally to **"one Gaussian per cell type (or per anatomical unit: glomerulus / proximal tubule / interstitium)"** — the Mahalanobis distance of a cell from its own type's healthy distribution is the conditional version of PaDiM. **What breaks**: (1) PaDiM relies on positional alignment; the omics analogue is correct cell-type annotation — mis-annotated cells get compared with the wrong Gaussian and false positives explode; (2) a unimodal Gaussian fails on continuous states (the proximal-tubule healthy → injured → failed-repair axis); (3) batch effects, ambient RNA and doublets all push cells away from the mean, and Mahalanobis cannot tell technical artifacts from disease — exactly what Plan A resolves with **cross-modal agreement** (snRNA ↔ snATAC ↔ Xenium ↔ H&E); (4) omics has no pixel masks, so PRO / pixel AUROC cannot be computed and KidneyAnomalyBench must substitute expert labels or synthetic perturbations. **Existing repo papers with the same idea**: healthy-ref-natgenet-2023 finds disease states in an scVI healthy-atlas latent space (via Milo differential abundance rather than a distance score); pathology-ad-bench-mlhealth-2025 benchmarks PaDiM within its "feature distribution" family on Camelyon16, Crohn's colon and mouse glomeruli, finding that family best overall but real pathology far harder than industrial data; histo-nejmai-2024 scores pathology-foundation-model features with kNN distance — the same "pretrained features + distance" paradigm. PaDiM's "random beats PCA" finding is also a warning for us: in scVI/PCA latent spaces the high-variance components are often batch or cell type, not the lesion direction.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** 论文未发布官方代码;常用实现在 anomalib 中(pathology-ad-bench-mlhealth-2025 即用此实现)。 <!-- EN --> **Code:** no official code release in the paper; the commonly used implementation is in anomalib (used by pathology-ad-bench-mlhealth-2025).
<!-- ZH/EN --> <https://github.com/open-edge-platform/anomalib>
- <!-- ZH --> **评测协议:** Rd-MVTec AD 非对齐评测(随机旋转 + 随机裁剪,5 次平均)—— 可类比为组学中"扰动细胞类型注释 / 空间配准"的鲁棒性测试。 <!-- EN --> **Eval protocol:** the Rd-MVTec AD misalignment test (random rotation + crop, averaged over 5) — analogous to robustness tests that perturb cell-type annotation or spatial registration in omics.
- <!-- ZH --> **配方:** 多层特征拼接 + 随机降维 + 每组一个高斯 + ε=0.01 正则化,可直接套在 scVI / 基础模型 embedding 上做按细胞类型的基线。 <!-- EN --> **Recipe:** multi-layer concatenation + random dim. reduction + one Gaussian per group + ε = 0.01 regularization, directly applicable to scVI / foundation-model embeddings as a per-cell-type baseline.

## 待读 / Follow-ups
- <!-- ZH --> Rippel 等 2020(MahalanobisAD)与 SPADE(Cohen & Hoshen 2020),两篇直接前作,仓库还没有条目。 <!-- EN --> Rippel et al. 2020 (MahalanobisAD) and SPADE (Cohen & Hoshen 2020), the two direct predecessors — not yet in the repo.
- <!-- ZH --> 对照 mahalanobis-ood-neurips-2018,看分类器特征上的类条件高斯如何对应"按细胞类型的高斯"。 <!-- EN --> Compare with mahalanobis-ood-neurips-2018 — how class-conditional Gaussians on classifier features map to "per-cell-type Gaussians".
- <!-- ZH --> 在 Lake 图谱 scVI 潜空间上实测按细胞类型的 PaDiM 式基线,作为 KidneyAnomalyBench 的下限。 <!-- EN --> Run a per-cell-type PaDiM-style baseline on the Lake-atlas scVI latent space as a floor for KidneyAnomalyBench.

## 引用 / Cite
```bibtex
@inproceedings{Defard2020_201108785,
  title = {{PaDiM}: A Patch Distribution Modeling Framework for Anomaly Detection and Localization},
  author = {Defard, Thomas and Setkov, Aleksandr and Loesch, Angelique and Audigier, Romaric},
  booktitle = {Pattern Recognition. ICPR International Workshops and Challenges},
  series = {Lecture Notes in Computer Science},
  volume = {12664},
  pages = {475--489},
  publisher = {Springer},
  year = {2021},
  doi = {10.1007/978-3-030-68799-1_35},
  eprint = {2011.08785},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2011.08785}
}
```
