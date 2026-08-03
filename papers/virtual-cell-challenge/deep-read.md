# Virtual Cell Challenge

> **Bibkey** `virtual-cell-challenge` · **Venue** Arc Institute (competition; companion paper in *Cell*, 2025) · **Category** competition · **Relevance** medium · **Access** open
> **Link** <https://virtualcellchallenge.org/>
> `status: complete` — 资源卡(competition),基于官网、Arc 公告、Cell 论文与 2025 复盘整理。

---

## 一句话 / One-liner
<!-- ZH --> Arc Institute 主办的年度公开竞赛,要求参赛模型预测单基因 CRISPR 扰动在一个"留出细胞类型"(H1 人胚胎干细胞)中引起的单细胞基因表达变化,并用统一的三指标标准化评测——本质是"virtual cell 的图灵测试"。
<!-- EN --> Arc Institute's annual public competition asking models to predict single-cell gene-expression shifts caused by single-gene CRISPR perturbations in a held-out cell type (H1 hESC), scored on a standardized 3-metric protocol — framed as "a Turing test for the virtual cell."

## 研究问题 / Problem
<!-- 这篇论文要解决什么问题?为什么重要? / What problem, and why it matters. -->
<!-- ZH --> 扰动响应预测(perturbation response prediction)领域缺乏严格、公开、可比的评测标准,导致"AI virtual cell"模型的真实进展难以判断。挑战聚焦最难的现实任务——**context generalization**:能否把在其它细胞/扰动上学到的规律,泛化到一个全新的细胞语境和未见过的扰动基因上。核心科学动机是:若能准确模拟扰动→表达的映射,就能 in silico 筛选把病态细胞状态"revert"回正常的基因靶点。
<!-- EN --> The perturbation-response field lacked rigorous, public, comparable benchmarks, making real progress in "AI virtual cell" models hard to judge. The challenge targets the hardest realistic task — **context generalization**: transferring learned perturbation rules to a new cell context and to unseen perturbation genes. The scientific payoff: an accurate perturbation→expression map enables in-silico screening for genes that revert a diseased cell state.

## 方法 / Method
<!-- 核心方法、模型、数据流。关键公式/架构。 / Core method, model, data pipeline, key architecture. -->
<!-- ZH --> 竞赛设定:给定 H1 hESC 未扰动细胞的转录组参考 + 训练集(150 个基因扰动的单细胞谱),参赛者构建模型,对留出的扰动基因预测扰动后的单细胞表达谱。评测用 **三指标复合分**:(1) Differential Expression Score / DES——预测差异表达基因的准确度;(2) Perturbation Discrimination Score / PDS——区分不同扰动效应的能力;(3) Mean Absolute Error / MAE——全基因预测表达与真值的绝对误差。官方基线是 Arc 的 **STATE** 模型(State Transition 双向 transformer + State Embedding),并对比 cell-mean、linear、GEARS 等朴素/已有基线。
<!-- EN --> Setup: given an unperturbed H1 hESC transcriptomic reference plus a training set of single-cell profiles for 150 gene perturbations, entrants build a model that predicts post-perturbation single-cell expression for held-out perturbation genes. Scoring uses a **composite of three metrics**: DES (accuracy on differentially expressed genes), PDS (ability to discriminate distinct perturbation effects), and MAE (global absolute error over all genes). The official baseline is Arc's **STATE** model (State Transition bidirectional transformer + State Embedding), benchmarked against cell-mean, linear, and GEARS baselines.

## 数据 / Data
<!-- 数据集、模态、规模、来源。 / Datasets, modalities, scale, source. -->
<!-- ZH --> 首届自建单细胞转录组(Perturb-seq)数据集:约 **300,000 个 H1 hESC 细胞 × 300 个基因扰动**,扰动选择覆盖广谱表型响应。划分为:未扰动参考集;训练集 150 个扰动基因(~150,000 细胞);验证集 50 个扰动基因(驱动实时排行榜);最终测试集 100 个留出扰动。允许外部数据:Arc Virtual Cell Atlas(>5 亿细胞)、scBaseCount、Tahoe-100M、X-Atlas/Orion(目前最大公开 Perturb-seq)。
<!-- EN --> A purpose-built single-cell transcriptomic (Perturb-seq) dataset: ~**300,000 H1 hESCs × 300 gene perturbations** spanning a broad phenotypic range. Splits: an unperturbed reference; a 150-gene training set (~150,000 cells); a 50-gene validation set driving a live leaderboard; and a 100-perturbation held-out test set. External data allowed: Arc Virtual Cell Atlas (>500M cells), scBaseCount, Tahoe-100M, and X-Atlas/Orion (largest public Perturb-seq).

## 主要结果 / Key results
<!-- 关键指标与结论,尽量带数字。 / Headline metrics and conclusions, with numbers where possible. -->
<!-- ZH --> 参与规模:114 国 5,000+ 注册,1,200+ 队提交,300+ 队最终提交。基线水平:在未见单基因扰动上,STATE 相对 cell-mean 基线提升 **26%**,优于 linear(19%)与 GEARS(22%)。关键结论:**纯 AI 方法并未稳定超过统计基线**;几乎所有模型在 MAE 上都不如朴素基线;结合深度学习与统计特征的混合模型胜出,蛋白质 embedding 等多模态特征有增益。获奖:1st BM_xTVC(BioMap,xTrimoSCPerturb,scFoundation+蛋白嵌入);2nd XLearning Lab(度量驱动条件生成 + ESM-2);3rd Outlier(TransPert,跨参考细胞系相似度聚合);Generalist Prize 归 Altos Labs(go-with-the-flow,flow-matching 生成)。
<!-- EN --> Participation: 5,000+ registrants across 114 countries, 1,200+ teams submitting, 300+ final submissions. Baseline: on unseen single-gene perturbations STATE beat the cell-mean baseline by **26%** vs 19% (linear) and 22% (GEARS). Key takeaways: **pure AI did not consistently beat statistical baselines**; almost all models were worse than the naive baseline on MAE; hybrid deep-learning + statistics models won, and protein embeddings added value. Winners: 1st BM_xTVC (BioMap, xTrimoSCPerturb); 2nd XLearning Lab (metric-driven conditional generation + ESM-2); 3rd Outlier (TransPert); Generalist Prize to Altos Labs (go-with-the-flow flow matching).

## 创新点 / Contributions
- <!-- ZH --> 为单细胞扰动预测确立**公开、标准化的三指标评测协议**(DES/PDS/MAE)与留出细胞语境的泛化任务框架。 <!-- EN --> Establishes a public, standardized 3-metric protocol (DES/PDS/MAE) and a held-out-context generalization task for single-cell perturbation prediction.
- <!-- ZH --> 发布高质量的新数据资产:300K H1 hESC × 300 扰动的 Perturb-seq 数据集 + STATE 官方基线。 <!-- EN --> Releases a high-quality new dataset (300K H1 hESC × 300 perturbations) plus the STATE reference baseline.
- <!-- ZH --> 通过大规模社区参与,产出"当前 SOTA 到底在哪"的实证结论(混合模型 > 纯神经网络)。 <!-- EN --> Large-scale participation yields empirical evidence on the real state of the art (hybrids > pure neural nets).

## 局限 / Limitations
- <!-- ZH --> 单一细胞类型(H1 hESC)、单基因扰动、纯转录组模态——尚不覆盖组合扰动、空间/多模态或组织尺度。 <!-- EN --> Single cell type (H1 hESC), single-gene perturbations, transcriptome-only — no combinatorial perturbations, spatial/multimodal, or tissue scale yet.
- <!-- ZH --> MAE 上模型普遍不敌朴素基线,说明"绝对表达量"预测仍未真正解决;指标本身仍在演化。 <!-- EN --> Models generally lose to naive baselines on MAE, so absolute-expression prediction is not solved; the metrics themselves are still evolving.
- <!-- ZH --> 竞赛结论是"预测扰动效应",不直接回答"哪些基因能 revert 病态"这一逆问题。 <!-- EN --> The task predicts perturbation effects; it does not directly solve the inverse "which genes revert a diseased state" problem.

## 与本研究方向的关系 / Relation to our direction
<!-- anomaly detection → virtual tissue → revert via gene prediction 这条线上,这篇处在哪一环?能复用什么? -->
<!-- ZH --> 直接对应我们 pipeline 的**第二/第三环**:"virtual tissue 建模"与"预测可 revert anomaly 的基因扰动"。挑战给出的正是**扰动→单细胞表达的正向模拟器**——这正是 revert 逆问题的核心引擎:一旦有可靠的 perturbation 模型,就能对"病态 vs 正常"的目标状态做 in-silico 基因扫描,挑出把细胞推回正常的靶点。可复用的还有:(1) STATE 作为预训练 virtual cell 基线;(2) DES/PDS/MAE 作为我们自建 revert 评测的现成协议;(3) "纯 AI 未超统计基线、混合模型更强"的经验教训,提示我们在方法设计上保留统计/生物先验。局限是它停在单细胞、非组织/空间尺度,与我们的 virtual **tissue** 目标间还需空间转录组学的桥接。
<!-- EN --> Maps directly onto **stage 2/3** of our pipeline — virtual-tissue modeling and predicting gene perturbations that revert an anomaly. The challenge delivers exactly a **forward perturbation→expression simulator**, the core engine of the revert inverse problem: with a reliable perturbation model, one can run in-silico gene scans toward a "normal" target state and rank revert targets. Reusable: (1) STATE as a pretrained virtual-cell baseline; (2) DES/PDS/MAE as a ready-made scoring protocol for our own revert evaluation; (3) the empirical lesson that pure AI didn't beat statistics — argues for keeping statistical/biological priors. Caveat: it stops at single cells, not tissue/spatial scale, so bridging to our virtual-*tissue* goal still needs spatial transcriptomics.

## 可复用资产 / Reusable assets
<!-- 代码、预训练模型、数据集、评测协议。 / Code, checkpoints, datasets, eval protocols. -->
- <!-- ZH --> **STATE 模型**(Arc 的 virtual cell 模型,State Transition + State Embedding)——预训练基线,可作我们扰动模拟的起点。<https://arcinstitute.org/news/virtual-cell-model-state> <!-- EN --> **STATE model** (Arc's virtual cell model, State Transition + State Embedding) — pretrained baseline, usable as a starting point for our perturbation simulation. <https://arcinstitute.org/news/virtual-cell-model-state>
- <!-- ZH --> **挑战数据集**:300K H1 hESC × 300 扰动 Perturb-seq + 官方 splits/leaderboard,<https://virtualcellchallenge.org/>(evaluation page:`/evaluation`)。 <!-- EN --> **Challenge dataset**: 300K H1 hESC × 300-perturbation Perturb-seq plus official splits/leaderboard, <https://virtualcellchallenge.org/> (evaluation page: `/evaluation`).
- <!-- ZH --> **评测协议**:DES / PDS / MAE 复合评分——可直接移植为 revert 任务评测。 <!-- EN --> **Eval protocol**: DES / PDS / MAE composite scoring — directly portable as an evaluation for our revert task.
- <!-- ZH --> **外部语料**:Arc Virtual Cell Atlas(>5 亿细胞)、scBaseCount、Tahoe-100M、X-Atlas/Orion Perturb-seq。 <!-- EN --> **External corpora**: Arc Virtual Cell Atlas (>500M cells), scBaseCount, Tahoe-100M, X-Atlas/Orion Perturb-seq.
- <!-- ZH --> **配套论文**:"Virtual Cell Challenge: Toward a Turing test for the virtual cell," *Cell*, 2025——任务/指标的权威描述。 <!-- EN --> **Companion paper**: "Virtual Cell Challenge: Toward a Turing test for the virtual cell," *Cell*, 2025 — the authoritative description of the task and metrics.

## 待读 / Follow-ups
- <!-- ZH --> STATE 模型论文与代码(State Transition / State Embedding 架构细节)。 <!-- EN --> The STATE model paper and code (State Transition / State Embedding architecture details).
- <!-- ZH --> 获奖方案:xTrimoSCPerturb(BioMap)、TransPert、Altos "go-with-the-flow" flow-matching——混合与生成式思路。 <!-- EN --> Winning solutions: xTrimoSCPerturb (BioMap), TransPert, Altos "go-with-the-flow" flow-matching — hybrid and generative approaches.
- <!-- ZH --> 独立基准论文 "Benchmarking virtual cell models for in-the-wild perturbation response" 与 "The Baseline Gap" (Research Square),审视指标可靠性。 <!-- EN --> Independent benchmark papers "Benchmarking virtual cell models for in-the-wild perturbation response" and "The Baseline Gap" (Research Square), scrutinizing metric reliability.
- <!-- ZH --> X-Atlas/Orion Perturb-seq 数据说明,评估作为额外训练/迁移语料的价值。 <!-- EN --> The X-Atlas/Orion Perturb-seq data documentation, assessing its value as an extra training/transfer corpus.

## 图表 / Figures & tables

<!-- ZH --> 本条目是**竞赛资源卡**:官网(virtualcellchallenge.org)为竞赛站点,配套论文发表于 *Cell*(付费墙,DOI 10.1016/j.cell.2025.06.008),两者的示意图/图表均非开放许可,故不下载或嵌入图片。原始示意图见官网与 Cell 论文;下方以两张小表复述**数据集划分**与**三指标评分协议**(数字均来自官方公开描述,未作推断)。
<!-- EN --> This entry is a **competition resource card**: the site (virtualcellchallenge.org) is a competition page and the companion paper is in *Cell* (paywalled, DOI 10.1016/j.cell.2025.06.008); neither's schematics carry an open license, so no images are downloaded or embedded. See the original diagrams on the site and in the Cell paper. The two small tables below restate the **dataset split** and the **3-metric scoring protocol** (figures are from the official public description; nothing is inferred).

<!-- ZH/EN --> _Source: https://virtualcellchallenge.org/ (site, competition) · companion paper *Cell* 2025, DOI 10.1016/j.cell.2025.06.008 (paywalled) — figures linked, not reproduced._

### 结果表 / Results

<!-- ZH --> **表1.** 数据集划分:约 300,000 个 H1 hESC 细胞 × 300 个单基因扰动(Perturb-seq)。 <!-- EN --> **Table 1.** Dataset split: ~300,000 H1 hESCs × 300 single-gene perturbations (Perturb-seq).

| Split | Perturbations | Cells (approx.) | Role |
|---|---|---|---|
| Unperturbed reference | — | (H1 hESC baseline) | Transcriptomic reference for the held-out context |
| Training | 150 genes | ~150,000 | Model training |
| Validation | 50 genes | — | Drives the live leaderboard |
| Final test | 100 genes | — | Held-out scoring |
| **Total** | **300** | **~300,000** | — |

<!-- ZH --> **表2.** 评分协议:三指标复合分(context generalization,留出 H1 hESC 语境)。 <!-- EN --> **Table 2.** Scoring: composite of three metrics (context generalization on the held-out H1 hESC context).

| Metric | Full name | Measures | Direction |
|---|---|---|---|
| DES | Differential Expression Score | Accuracy on differentially expressed genes after perturbation | higher = better |
| PDS | Perturbation Discrimination Score | Ability to distinguish the effects of different perturbations vs ground truth | higher = better |
| MAE | Mean Absolute Error | Global absolute error vs true post-perturbation expression across all genes | lower = better |

<!-- ZH --> 官方基线 **STATE**(State Transition + State Embedding):在未见单基因扰动上相对 cell-mean 基线提升约 26%(linear 19%、GEARS 22%);但几乎所有参赛模型在 MAE 上都不敌朴素基线。 <!-- EN --> Official baseline **STATE** (State Transition + State Embedding): on unseen single-gene perturbations it beat the cell-mean baseline by ~26% (linear 19%, GEARS 22%); yet almost all submissions were worse than the naive baseline on MAE.

## 引用 / Cite
```bibtex
% no BibTeX fetched
```
