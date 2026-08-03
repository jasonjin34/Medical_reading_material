# Conditional Monge Gap enables generalizable single-cell perturbation modelling

> **Bibkey** `Driessen_2026` · **Venue** Nature Machine Intelligence (2026) · **Category** single-cell · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s42256-026-01242-8>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> 提出 Conditional Monge Gap (CMonge):一种可在任意协变量(药物、剂量、细胞类型、组合)上条件化的神经最优传输(neural OT)方法,把"对照细胞分布→扰动后细胞分布"的映射统一到单一模型,并能仅凭化合物结构泛化到未见过的药物。
<!-- EN --> CMonge is a conditional neural optimal-transport method that learns a single map from control to perturbed single-cell distributions conditioned on arbitrary covariates (drug, dose, cell type, combinations), and generalizes to unseen drugs from compound structure alone.

## 研究问题 / Problem
<!-- ZH --> 单细胞扰动预测的核心难点是数据非配对(测序/成像会破坏细胞,无法观测同一细胞的"前后"状态),因此需要在分布层面建模。既有 neural OT 方法(如 CellOT)每个条件都要单独训一个模型,无法条件化于处理上下文,也几乎无法泛化到未见药物/剂量。作者要用一个统一、参数高效的模型同时解决"条件化"与"对未见处理的泛化"。
<!-- EN --> Single-cell perturbation data are unpaired (cells are destroyed on measurement), forcing distribution-level modelling. Prior neural OT (e.g. CellOT) trains one model per condition, cannot condition on treatment context, and fails to generalize to unseen drugs/doses. The goal: one parameter-efficient model that both conditions on covariates and generalizes to unseen perturbations.

## 方法 / Method
<!-- ZH --> 在 Monge Gap(一种无需 ICNN、直接以正则项逼近 OT 映射的框架)基础上引入条件化。网络是 encoder–decoder,以对照细胞表征为输入、以条件向量(药物/剂量/组合的嵌入)注入映射;训练目标 = Sinkhorn divergence 拟合项 + Monge gap 正则项(逼近最优传输的位移最小性)。条件化通过药物嵌入实现,论文对比两类嵌入:(1) RDKit 分子指纹(194 维,来自 SMILES,基于结构);(2) Mode-of-Action (MoA) 嵌入(10 维,数据驱动,用各药物靶细胞群两两 Wasserstein 距离经 MDS 得到,基于效应)。通过在数百个条件上聚合训练实现 cross-task learning,从而对未见药物做 OOD 预测。先训一个 autoencoder 降维,再在潜空间训条件 Monge 模型。
<!-- EN --> Builds on the Monge Gap (an ICNN-free OT-map regularizer). An encoder–decoder maps control-cell representations to perturbed ones, injecting a condition vector (drug/dose/combination embedding). Objective = Sinkhorn-divergence fitting term + Monge-gap regularizer. Two drug-embedding families are compared: RDKit fingerprints (194-d, structure-based, from SMILES) and Mode-of-Action embeddings (10-d, effect-based, MDS over pairwise Wasserstein distances between treated populations). Aggregating hundreds of conditions enables cross-task learning and OOD prediction. An autoencoder is trained first for dimensionality reduction, then the conditional Monge model in latent space.

## 数据 / Data
<!-- ZH --> 两个数据集:(1) **SciPlex3**(scRNA-seq):762,039 个细胞,3 个癌系(A549/K562/MCF7),187–188 种化合物 × 4 个剂量(10/100/1000/10000 nM)+ 对照,共 748 个药物-剂量条件;实验既做 9 药子集,也做全量数百条件。(2) **4i**(multiplexed protein imaging,iterative indirect immunofluorescence):97,748 个细胞(10,995 对照),黑色素瘤肿瘤系,35 种癌症疗法(约 2,500 细胞/处理),48 维标志物与形态学特征,含组合疗法。预处理版数据在 ETH research collection 公开。
<!-- EN --> (1) **SciPlex3** scRNA-seq: 762,039 cells, three cancer lines (A549/K562/MCF7), 187–188 compounds × 4 doses + control, 748 drug-dose conditions. (2) **4i** multiplexed protein imaging: 97,748 cells (10,995 controls), melanoma lines, 35 therapies (~2,500 cells each), 48 marker/morphology features, including combination therapies.

## 主要结果 / Key results
<!-- ZH --> **In-distribution (SciPlex, 9 药):** 无条件 Monge(上界)R²≈0.950–0.978;CMonge-Dose-ID R²=0.882–0.974,用少 4× 的模型几乎追平逐条件模型;CMonge-DrugDose-MoA-ID 与 36 个逐条件模型相当。**OOD(未见药物,SciPlex):** CMonge-MoA-OOD 大幅超过 SOTA 条件方法 chemCPA(最高剂量下 R²≈0.90 vs ≈0.76);规模化到 712 训练条件时 CMonge-MoA-OOD R²=0.900±0.059 而 chemCPA=0.760±0.211;RDKit 嵌入在扩到 187 药后由弱变强。**4i:** 组合疗法上 CMonge-MoA 在 MMD 指标优于 identity 基线;单药因效应量小提升有限。作者强调 CMonge 相对单细胞基础模型参数高效,且能只凭化合物结构预测未见药物。
<!-- EN --> In-distribution (SciPlex, 9 drugs): unconditional Monge upper bound R²≈0.950–0.978; CMonge-Dose-ID R²=0.882–0.974 with 4× fewer models; DrugDose-MoA-ID on par with 36 per-condition models. OOD unseen drugs: CMonge-MoA-OOD R²≈0.90 vs chemCPA ≈0.76 at highest dose; at 712 conditions 0.900±0.059 vs 0.760±0.211. On 4i, CMonge-MoA beats identity on MMD for combination therapies. Parameter-efficient vs single-cell foundation models; predicts unseen drugs from structure alone.

## 创新点 / Contributions
- <!-- ZH --> 将 Monge Gap 条件化为 **Conditional Monge Gap**,可在任意协变量(药物/剂量/细胞类型/组合)上共享一个 OT 映射 —— 首个统一条件化 + 参数高效的 neural OT 扰动模型。 <!-- EN --> Conditionalizes the Monge Gap into a **Conditional Monge Gap** that shares a single OT map across arbitrary covariates (drug/dose/cell type/combination) — the first neural OT perturbation model to unify conditioning with parameter efficiency.
- <!-- ZH --> 通过在数百条件上 cross-task 训练,实现对**未见药物/剂量的 OOD 泛化**,且仅需化合物结构(SMILES→RDKit)或 MoA 嵌入。 <!-- EN --> Cross-task training over hundreds of conditions achieves **OOD generalization to unseen drugs/doses**, needing only compound structure (SMILES→RDKit) or MoA embeddings.
- <!-- ZH --> 系统对比结构型(RDKit)与效应型(MoA)药物嵌入,并同时在 scRNA-seq 与蛋白成像两种模态上验证。 <!-- EN --> Systematically compares structure-based (RDKit) and effect-based (MoA) drug embeddings, validating on both scRNA-seq and protein-imaging modalities.
- <!-- ZH --> 上游合并进 `ott-jax`(OTT 库 PR #605),方法可复用。 <!-- EN --> Merged upstream into `ott-jax` (OTT library PR #605), making the method reusable.

## 局限 / Limitations
- <!-- ZH --> RDKit 分子指纹需要显著更多训练条件才能追平 MoA,少条件下结构表征引入噪声。 <!-- EN --> RDKit fingerprints need substantially more training conditions to match MoA; with few conditions the structural representation introduces noise.
- <!-- ZH --> 最高剂量条件最难学(扰动最强)。 <!-- EN --> The highest-dose conditions are the hardest to learn (strongest perturbation).
- <!-- ZH --> MoA 嵌入依赖已测得的单药群体;缺单药测量的组合处理无法评估。 <!-- EN --> MoA embeddings depend on measured single-drug populations; combination treatments lacking single-drug measurements cannot be evaluated.
- <!-- ZH --> 个别机制迥异的药(如 trametinib)预测明显更差。 <!-- EN --> A few drugs with markedly different mechanisms (e.g. trametinib) are predicted noticeably worse.
- <!-- ZH --> 4i 数据 identity 基线 R² 已 >0.6(效应量小),条件信息带来的增益受限;DrugDose-MoA-ID 在捕获特征均值 R² 上不及 36 个逐条件模型(尽管 Wasserstein 更好)。 <!-- EN --> On 4i data the identity baseline already has R² >0.6 (small effect size), limiting the gain from conditioning; DrugDose-MoA-ID trails the 36 per-condition models on feature-mean R² (though it is better on Wasserstein).

## 与本研究方向的关系 / Relation to our direction
<!-- anomaly detection → virtual tissue → revert via gene prediction 这条线上,这篇处在哪一环?能复用什么? -->
<!-- ZH --> 直接落在 **virtual tissue / 扰动响应建模 → gene/药物 revert 预测** 环节,而非 anomaly detection。CMonge 把"对照→扰动"建成条件 OT 映射;对我们的"预测能把异常态 revert 回正常态的干预"目标,这等价于给定目标分布(正常/对照)反解所需的条件(药物/剂量),即可用其条件化能力做 in-silico 干预筛选与药物重定位。其 OOD 泛化(仅凭 SMILES 就能预测未见药物)对"提出候选干预→湿实验验证"闭环特别有用。值得注意的是它建模的是分布位移(distribution shift),与我们把疾病/药物导致的组织改变当作 anomaly 的框架天然契合 —— 可把 Monge/Sinkhorn 位移量当作 anomaly 严重度或 revert 距离的度量。模态上同时覆盖 scRNA-seq 与多重蛋白成像,契合我们跨 single-cell/spatial/成像的需求。局限是它工作在细胞群体分布层面、未做空间坐标建模,也非专门的异常检测器。
<!-- EN --> Sits in the virtual-tissue / perturbation-response → gene-and-drug-revert stage, not anomaly detection. CMonge models control→perturbed as a conditional OT map; for our goal of predicting interventions that revert an anomalous state, its conditioning lets us search which drug/dose maps a population toward a target (normal) distribution — an in-silico intervention/repurposing screen. Its OOD generalization (unseen drugs from SMILES) fits the propose-candidate → wet-lab-validate loop. It explicitly models distribution shift, aligning with treating disease/drug-induced tissue change as an anomaly, and the Monge/Sinkhorn displacement can serve as a revert-distance metric. Caveats: population-distribution level, no spatial coordinates, and not itself an anomaly detector.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码**:`AI4SCR/conditional-monge-gap`(MIT 许可,`pip install cmonge`;Python 3.10/3.11,JAX/OTT 后端)。<https://github.com/AI4SCR/conditional-monge-gap> <!-- EN --> **Code:** `AI4SCR/conditional-monge-gap` (MIT license, `pip install cmonge`; Python 3.10/3.11, JAX/OTT backend). <https://github.com/AI4SCR/conditional-monge-gap>
- <!-- ZH --> **CAR-T 扩展**:`AI4SCR/car-conditional-monge`(把 CMonge 扩到 CAR-T scRNA-seq,含 CAR 专用 dataloader/embedding/trainer)。<https://github.com/AI4SCR/car-conditional-monge> <!-- EN --> **CAR-T extension:** `AI4SCR/car-conditional-monge` (extends CMonge to CAR-T scRNA-seq, with CAR-specific dataloader/embedding/trainer). <https://github.com/AI4SCR/car-conditional-monge>
- <!-- ZH --> **上游集成**:OTT (`ott-jax`) PR #605 —— conditional Monge gap 已并入 OTT。 <!-- EN --> **Upstream integration:** OTT (`ott-jax`) PR #605 — conditional Monge gap merged into OTT.
- <!-- ZH --> **数据**:预处理好的 SciPlex3 与 4i 数据(ETH research collection)<https://www.research-collection.ethz.ch/handle/20.500.11850/609681>。 <!-- EN --> **Data:** preprocessed SciPlex3 and 4i data (ETH research collection). <https://www.research-collection.ethz.ch/handle/20.500.11850/609681>
- <!-- ZH --> **预训练模型**:仓库 `models/` 目录含 checkpoints(旧版需 `cmonge_checkpoint_loading` git tag)。 <!-- EN --> **Pretrained models:** the repo `models/` directory contains checkpoints (older versions need the `cmonge_checkpoint_loading` git tag).
- <!-- ZH --> **评测协议**:R²(特征均值)、MMD、(entropic) Wasserstein / Sinkhorn divergence;identity、逐条件 Monge、CellOT(ICNN)、chemCPA 等基线可直接复用。 <!-- EN --> **Evaluation protocol:** R² (feature mean), MMD, (entropic) Wasserstein / Sinkhorn divergence; baselines such as identity, per-condition Monge, CellOT (ICNN), and chemCPA are directly reusable.
- <!-- ZH --> **预印本**:arXiv:2504.08328(全文,含全部指标/图表)。 <!-- EN --> **Preprint:** arXiv:2504.08328 (full text, with all metrics/figures).

## 待读 / Follow-ups
- <!-- ZH --> 精读 arXiv:2504.08328 方法节:Monge gap 正则的确切形式、autoencoder 潜空间维度、条件注入位置。 <!-- EN --> Close-read the arXiv:2504.08328 methods section: the exact form of the Monge-gap regularizer, autoencoder latent-space dimensionality, and where the condition is injected.
- <!-- ZH --> chemCPA 原文(对比基线,SOTA 条件扰动模型)。 <!-- EN --> The chemCPA paper (comparison baseline, SOTA conditional perturbation model).
- <!-- ZH --> CellOT / Monge Gap(Uscidda & Cuturi)原始方法,理解无 ICNN OT 的收敛性。 <!-- EN --> The CellOT / Monge Gap (Uscidda & Cuturi) original methods, to understand the convergence of ICNN-free OT.
- <!-- ZH --> 复现 SciPlex3 OOD 设置,把"revert 到对照分布"的方向设为目标分布做一次 in-silico 干预筛选。 <!-- EN --> Reproduce the SciPlex3 OOD setup, set "revert to the control distribution" as the target direction, and run one in-silico intervention screen.
- <!-- ZH --> 评估能否把 CMonge 迁到 spatial transcriptomics(加入空间坐标/邻域条件)。 <!-- EN --> Evaluate whether CMonge can transfer to spatial transcriptomics (adding spatial-coordinate / neighborhood conditions).

## 引用 / Cite
```bibtex
@article{Driessen_2026, title={Conditional Monge Gap enables generalizable single-cell perturbation modelling}, volume={8}, ISSN={2522-5839}, url={http://dx.doi.org/10.1038/s42256-026-01242-8}, DOI={10.1038/s42256-026-01242-8}, number={6}, journal={Nature Machine Intelligence}, publisher={Springer Science and Business Media LLC}, author={Driessen, Alice and Rajwade, Dhruva Abhijit and Harsanyi, Benedek and Rapsomaniki, Marianna and Born, Jannis}, year={2026}, month=June, pages={984–996} }
```
