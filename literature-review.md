# 文献综述 / Literature Review
### Anomaly-detection-based virtual tissue modelling

<!-- ZH --> 研究方向:检测因疾病或药物扰动而改变的生物医学影像 / 空间组学区域(**异常检测**),把组织建成可操作的**虚拟组织**,再预测能**逆转**该异常的关键基因/扰动(湿实验验证)。
<!-- EN --> Direction: detect image / spatial-omics regions changed by disease or drug perturbation (**anomaly detection**) → model tissue as a manipulable **virtual tissue** → predict the key genes / perturbations that **revert** the anomaly (validated in the wet lab).

<!-- ZH --> 本综述把 18 篇/项资料组织成一条流水线的三个阶段,外加贯穿全程的**基础模型**与**数据**底座,末尾给出空白与建议。每条都链接到对应精读。
<!-- EN --> This review organises the 18 items along a three-stage pipeline plus the cross-cutting **foundation-model** and **data** substrate, ending with gaps and recommendations. Each item links to its close-reading.

---

## 阶段一 · 异常检测 / Stage 1 — Anomaly detection

<!-- ZH --> **核心思路.** 只学"正常"组织的分布,把偏离正常的区域打成异常分数;这是"定位变化"的第一步。
<!-- EN --> **Core idea.** Learn the distribution of *normal* tissue and score departures from it — the *learn normal, flag deviation* recipe. This is the first step of localizing change.

- <!-- ZH --> [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/deep-read.md) — **STANDS**(Nat. Commun. 2024)在**空间转录组**上做多样本异常域的检测→对齐→分型,GAN 重构误差即异常分数。与本方向**模态最契合**的方法参照。代码 `Catchxu/STANDS`(GPL-3.0)。 <!-- EN --> [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/deep-read.md) — **STANDS** (Nat. Commun. 2024): multi-sample detect→align→subtype of anomalous domains in **spatial transcriptomics**; GAN reconstruction error is the anomaly score. The closest on-modality reference. Code `Catchxu/STANDS` (GPL-3.0).
- <!-- ZH --> [`histo-nejmai-2024`](papers/histo-nejmai-2024/deep-read.md) — **NEJM AI 2024**,临床级组织病理异常检测。Outlier-Exposure + ResNet-18 最优,胃 slide-AUROC 95.0%、结肠 91.0%,外部验证仍稳;100% 敏感度下可自动放行 36% 正常切片。 <!-- EN --> [`histo-nejmai-2024`](papers/histo-nejmai-2024/deep-read.md) — **NEJM AI 2024**, clinical-grade histopathology anomaly detection. Outlier-Exposure + ResNet-18 best; stomach slide-AUROC 95.0%, colon 91.0%, robust external validation; auto-clears 36% of normal slides at 100% sensitivity.
- <!-- ZH --> [`histo-miccai-2025`](papers/histo-miccai-2025/deep-read.md) — **AnoPILaD**(MICCAI 2025),潜在扩散"重构回正常",输入-重构差异即异常;patch-AUC 0.959。**"reconstruct-to-normal"** 是图像域"虚拟组织逆转"的雏形,连接阶段一与二。代码 `QuIIL/AnoPILaD`(MIT)。 <!-- EN --> [`histo-miccai-2025`](papers/histo-miccai-2025/deep-read.md) — **AnoPILaD** (MICCAI 2025): a latent diffusion model that reconstructs *back to normal*; input-vs-reconstruction discrepancy = anomaly; patch-AUC 0.959. This **reconstruct-to-normal** idea is an image-domain prototype of virtual-tissue reversion, bridging stages 1↔2. Code `QuIIL/AnoPILaD` (MIT).
- <!-- ZH --> [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/deep-read.md) — **PathPrism**(Cancer Cell 2026,开放获取)。可解释语义学习 + **结构保持的反事实**(VirtualWSI)在 628 维空间生物标志物图谱上做扰动,横跨阶段一(风险打分/显著性)与二(语义级虚拟组织)。代码 `KatherLab/PathPrism`。PI 标"重要"。 <!-- EN --> [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/deep-read.md) — **PathPrism** (Cancer Cell 2026, open access). Interpretable semantic learning + **structure-preserving counterfactuals** (VirtualWSI) over a 628-dim spatial-biomarker atlas — spanning stage 1 (risk/saliency) and stage 2 (semantic virtual tissue). Code `KatherLab/PathPrism`. Flagged "important".
- <!-- ZH --> [`histo-anomaly-bi-repo`](papers/histo-anomaly-bi-repo/deep-read.md) — Boehringer 工程化基线:仅学健康组织深特征 + one-class SVM,H&E 平衡准确率 94%。可直接复用为**组织病理异常检测基线**与工程模板(MIT)。 <!-- EN --> [`histo-anomaly-bi-repo`](papers/histo-anomaly-bi-repo/deep-read.md) — Boehringer engineering baseline: deep features of healthy tissue + one-class SVM, 94% balanced accuracy on H&E. A reusable **histopath anomaly-detection baseline** and template (MIT).
- <!-- ZH --> [`imaging-nature-2026`](papers/imaging-nature-2026/deep-read.md) ★ 与 [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/deep-read.md) — **跨模态方法学类比**:ECG 深度学习发现猝死生物标志物(Nature 2026)、非增强胸部 CT 检测异常射血分数(CT–LVEF,AUROC 0.79)。模态是心脏影像/信号,但"从常规检查机会性发现异常"的范式可迁移。 <!-- EN --> [`imaging-nature-2026`](papers/imaging-nature-2026/deep-read.md) ★ and [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/deep-read.md) — **cross-modal methodological analogues**: an ECG deep-learning biomarker for sudden cardiac death (Nature 2026) and abnormal ejection fraction from non-contrast chest CT (CT–LVEF, AUROC 0.79). Cardiac modality, but the "opportunistically detect anomalies from routine exams" paradigm transfers.

<!-- ZH --> **小结.** 组织学与空间组学已有成熟的"学正常-判异常"方法(STANDS、AnoPILaD、NEJM-AI);扩散/反事实类(AnoPILaD、PathPrism)天然指向"如何把异常改回正常",是通往阶段二、三的桥。
<!-- EN --> **Takeaway.** Mature *learn-normal, flag-anomaly* methods already exist for histology and spatial-omics (STANDS, AnoPILaD, NEJM-AI); the diffusion/counterfactual ones (AnoPILaD, PathPrism) naturally point at "how to turn the anomaly back to normal" — the bridge to stages 2 and 3.

---

## 阶段二 · 虚拟组织建模 / Stage 2 — Virtual-tissue modelling

<!-- ZH --> **核心思路.** 把组织表示成可查询、可干预的生成模型,支持 *in silico* 扰动。
<!-- EN --> **Core idea.** Represent tissue as a queryable, interventionable generative model that supports *in silico* perturbation.

- <!-- ZH --> [`virtual-tissue-2501`](papers/virtual-tissue-2501/deep-read.md) ★ — **VirTues**(arXiv 2501)。多尺度、marker-aware 的"虚拟组织" Transformer,15 个 IMC 数据集/147 marker/3,102 患者;重构 r=0.723,细胞分型 +6.3% over KRONOS,TNBC AUROC 0.817。**本方向"虚拟组织"概念的核心论文**;MAE 重构误差可直接当异常分数(连接阶段一)。代码 `bunnelab/virtues`(MIT)+ HF checkpoints。 <!-- EN --> [`virtual-tissue-2501`](papers/virtual-tissue-2501/deep-read.md) ★ — **VirTues** (arXiv 2501). A multi-scale, marker-aware "virtual tissue" Transformer; 15 IMC datasets / 147 markers / 3,102 patients; reconstruction r=0.723, cell-typing +6.3% over KRONOS, TNBC AUROC 0.817. **The core "virtual tissue" paper** here; its MAE reconstruction error doubles as an anomaly score (links to stage 1). Code `bunnelab/virtues` (MIT) + HF checkpoints.
- <!-- ZH --> [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/deep-read.md) ★ — **MintFlow**(bioRxiv 2025)。流匹配生成模型,把空间表达**解耦**为内在 + 微环境诱导两部分(X = X_int + X_mic),支持 *in silico* 组织扰动:删除 TLS 巨噬细胞可"去耗竭"T 细胞,并把 TCGA 生存信号从 p=0.0073(更差)翻转为 p=0.0034(获益)。**同时打通阶段二与三**。代码 `Lotfollahi-lab/mintflow`。 <!-- EN --> [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/deep-read.md) ★ — **MintFlow** (bioRxiv 2025). A flow-matching model that **disentangles** spatial expression into intrinsic + microenvironment-induced parts (X = X_int + X_mic) and supports *in silico* tissue perturbation: deleting TLS macrophages "de-exhausts" T cells and flips a TCGA survival signal from p=0.0073 (worse) to p=0.0034 (benefit). **Bridges stages 2 and 3.** Code `Lotfollahi-lab/mintflow`.

<!-- ZH --> **小结.** VirTues 提供"把组织建成模型"的骨架,MintFlow 提供"在模型上做因果干预并逆转表型"的机制——两者相加几乎就是本方向阶段二→三的原型。
<!-- EN --> **Takeaway.** VirTues gives the skeleton for turning tissue into a model; MintFlow gives the mechanism for causal intervention that reverts phenotype — together they are almost a stage-2→3 prototype for this direction.

---

## 阶段三 · 逆转:基因/扰动预测 / Stage 3 — Revert via gene & perturbation prediction

<!-- ZH --> **核心思路.** 求解反问题:施加什么扰动能把异常态推回正常态。
<!-- EN --> **Core idea.** Solve the inverse problem: which perturbation pushes an anomalous state back to normal.

- <!-- ZH --> [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/deep-read.md) — **Conditional Monge Gap**(Nat. Mach. Intell. 2026)。用最优传输学习可泛化的单细胞扰动映射,预测"扰动后细胞状态如何变"——正是"逆转异常"所需的建模工具。开源 `AI4SCR/conditional-monge-gap`。 <!-- EN --> [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/deep-read.md) — **Conditional Monge Gap** (Nat. Mach. Intell. 2026). Optimal-transport learning of generalizable single-cell perturbation maps — predicting how a cell state moves under perturbation, exactly the tool needed to revert anomalies. Open-source `AI4SCR/conditional-monge-gap`.
- <!-- ZH --> [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/deep-read.md) — MintFlow 的重编程能力在**空间尺度**上呼应同一目标(见阶段二)。 <!-- EN --> [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/deep-read.md) — MintFlow's reprogramming echoes the same goal at **spatial scale** (see stage 2).
- <!-- ZH --> [`virtual-cell-challenge`](papers/virtual-cell-challenge/deep-read.md) — **Arc Institute 虚拟细胞挑战赛**(2025)。任务是 context 泛化——预测 held-out H1 hESC 的单基因 CRISPR 扰动效应;STATE 基线、DES/PDS/MAE 三指标。可作我们扰动预测模型的**公开评测基准**(注意:止于单细胞尺度)。 <!-- EN --> [`virtual-cell-challenge`](papers/virtual-cell-challenge/deep-read.md) — the **Arc Institute Virtual Cell Challenge** (2025). Task: context generalization — predict single-gene CRISPR effects in held-out H1 hESCs; STATE baseline, DES/PDS/MAE metrics. A **public benchmark** for our perturbation models (caveat: single-cell scale only).

<!-- ZH --> **小结.** 扰动预测在单细胞尺度已有工具(Monge-Gap)与基准(VCC),空间尺度有 MintFlow 起步;把"异常检测的残差"接到"扰动预测的输入"是本方向最有原创性的一环。
<!-- EN --> **Takeaway.** Perturbation prediction has tools (Monge-Gap) and a benchmark (VCC) at single-cell scale, and a spatial-scale start (MintFlow); wiring the *anomaly-detection residual* into the *perturbation-prediction input* is the most original piece of this direction.

---

## 横切 · 基础模型 / Cross-cutting — Foundation backbones

<!-- ZH --> 组织病理基础模型为阶段一的特征提取与阶段二的表征骨干反复复用。
<!-- EN --> Pathology foundation models recur as feature extractors (Stage 1) and representation backbones (Stage 2).

- <!-- ZH --> [`virchow-2024`](papers/virchow-2024/deep-read.md) — **Virchow**(Nat. Med. 2024),ViT-H/14、632M 参数、~1.5M H&E WSI DINOv2 预训练;9 常见 + 7 罕见癌 specimen-AUC 0.95。可作冻结特征骨干(权重 gated,商用前核实许可)。 <!-- EN --> [`virchow-2024`](papers/virchow-2024/deep-read.md) — **Virchow** (Nat. Med. 2024): ViT-H/14, 632M params, DINOv2 pretraining on ~1.5M H&E WSIs; specimen-AUC 0.95 across 9 common + 7 rare cancers. A frozen feature backbone (weights are gated; verify the license before commercial use).
- <!-- ZH --> [`uni2-h-model`](papers/uni2-h-model/deep-read.md) — **UNI2-h**(MahmoodLab, HF),病理基础模型,`timm` 一行加载,即插即用的 patch embedding。 <!-- EN --> [`uni2-h-model`](papers/uni2-h-model/deep-read.md) — **UNI2-h** (MahmoodLab, HF): a pathology foundation model, one-line `timm` load, drop-in patch embeddings.
- <!-- ZH --> [`fm-arxiv-2604`](papers/fm-arxiv-2604/deep-read.md) — **生成式多模态组织病理基础模型**(arXiv 2604),把生成能力引入病理 FM,与阶段二的生成式虚拟组织理念相通。 <!-- EN --> [`fm-arxiv-2604`](papers/fm-arxiv-2604/deep-read.md) — a **generative multimodal histopathology foundation model** (arXiv 2604) that brings generation into pathology FMs, resonating with stage-2 generative virtual tissue.

---

## 横切 · 数据与应用 / Cross-cutting — Data & applications

- <!-- ZH --> [`hest1k-2024`](papers/hest1k-2024/deep-read.md) — **HEST-1k**,大规模配对**组织学图像↔空间转录组**数据集(>1,200 profiles / 26 organs)+ HEST-Benchmark。把 H&E 形态与分子表达对齐,是阶段一(异常标注)与二(图像→分子)的**共同数据底座**;缺扰动/逆转数据(需与 Perturb-seq 配对)。CC BY-NC-SA 4.0。 <!-- EN --> [`hest1k-2024`](papers/hest1k-2024/deep-read.md) — **HEST-1k**, a large paired **histology↔spatial-transcriptomics** dataset (>1,200 profiles / 26 organs) + HEST-Benchmark. It aligns H&E morphology with molecular expression — the **shared data substrate** for stage 1 (anomaly labeling) and stage 2 (image→molecule); lacks perturbation/revert data (pair with Perturb-seq). CC BY-NC-SA 4.0.
- <!-- ZH --> [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/deep-read.md)、[`pathomics-blood-2023`](papers/pathomics-blood-2023/deep-read.md)、[`pathomics-repo`](papers/pathomics-repo/deep-read.md) — **Pathomics 应用**:胃癌预后/疗效签名(3,138 例,MS-GMIL)、骨髓微环境细胞量化(ASH 2023 摘要)、多模态病理+组学生存预测(PathOmics, MICCAI 2023)。示范"图像→分子→临床"的落地链路。 <!-- EN --> [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/deep-read.md), [`pathomics-blood-2023`](papers/pathomics-blood-2023/deep-read.md), [`pathomics-repo`](papers/pathomics-repo/deep-read.md) — **Pathomics applications**: a gastric-cancer prognosis/response signature (3,138 patients, MS-GMIL), bone-marrow microenvironment cell quantification (ASH 2023 abstract), and multimodal pathology+omics survival prediction (PathOmics, MICCAI 2023). They exemplify the image→molecule→clinic chain.

---

## 综合与空白 / Synthesis & gaps

<!-- ZH --> 1. **三个阶段各有成熟组件,但尚未串成闭环。** 异常检测(STANDS / AnoPILaD / NEJM-AI)、虚拟组织(VirTues)、扰动逆转(MintFlow / Monge-Gap)彼此独立;**最大机会是把它们连成 detect → model → revert 的端到端管线。**
<!-- EN --> 1. **Mature components exist per stage but are not yet a closed loop.** Anomaly detection (STANDS / AnoPILaD / NEJM-AI), virtual tissue (VirTues), and perturbation-revert (MintFlow / Monge-Gap) are independent; **the opportunity is an end-to-end detect → model → revert pipeline.**
<!-- ZH --> 2. **"重构回正常"反复出现**(AnoPILaD 扩散重构、PathPrism 反事实、MintFlow in-silico 删除、VirTues MAE 残差),天然统一"异常检测"与"逆转",值得作为方法主线。
<!-- EN --> 2. **"Reconstruct back to normal" recurs** (AnoPILaD's diffusion, PathPrism's counterfactuals, MintFlow's in-silico deletion, VirTues' MAE residual) — it unifies anomaly detection and reversion and is worth adopting as the methodological spine.
<!-- ZH --> 3. **模态桥接靠数据。** HEST-1k 提供 H&E↔ST 配对但**无扰动标签**;需与单细胞扰动数据(VCC / Perturb-seq)拼接,才能训练"空间尺度的逆转"。
<!-- EN --> 3. **Modality bridging hinges on data.** HEST-1k offers H&E↔ST pairs but **no perturbation labels**; it must be joined with single-cell perturbation data (VCC / Perturb-seq) to train spatial-scale reversion.
<!-- ZH --> 4. **基础模型是免费的起跑线。** Virchow / UNI2 / 生成式 FM 可直接做特征骨干,省去从零预训练。
<!-- EN --> 4. **Foundation models are a free head start.** Virchow / UNI2 / the generative FM serve as feature backbones, saving pretraining from scratch.
<!-- ZH --> 5. **异常检测范式偏好未定。** 临床影像多为**有监督**(CT–LVEF、ECG),组织学更倾向**无/自监督 OOD**;本方向应明确采用后者以适配"未知异常"。
<!-- EN --> 5. **The anomaly-detection paradigm is unsettled.** Clinical imaging is mostly **supervised** (CT–LVEF, ECG) while histology favours **un-/self-supervised OOD**; this direction should commit to the latter to handle *unknown* anomalies.

<!-- ZH --> **建议下一步.** (a) 以 VirTues/MintFlow 为阶段二骨架,用其重构残差驱动阶段一;(b) 在 HEST-1k + VCC 上搭"异常残差→扰动预测"原型;(c) 用 AnoPILaD/PathPrism 的反事实做图像域可视化验证;(d) 参加 Virtual Cell Challenge 获得统一评测。
<!-- EN --> **Suggested next steps.** (a) Use VirTues/MintFlow as the stage-2 skeleton and drive stage 1 from their reconstruction residuals; (b) prototype "anomaly residual → perturbation prediction" on HEST-1k + VCC; (c) use AnoPILaD/PathPrism counterfactuals for image-domain visual validation; (d) enter the Virtual Cell Challenge for a common benchmark.

---

## 引用 / Citations
<!-- ZH --> 所有条目的 BibTeX 见 [`references.bib`](references.bib);论文间关系见 [`relationships`](relationships.md)。
<!-- EN --> All BibTeX in [`references.bib`](references.bib); inter-paper links in [`relationships`](relationships.md).
