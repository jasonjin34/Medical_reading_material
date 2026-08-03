# Virtual Cell Challenge

> **Bibkey** `virtual-cell-challenge` · **Venue** Arc Institute (competition; companion paper in *Cell*, 2025) · **Category** competition · **Relevance** medium · **Access** open
> **Link** <https://virtualcellchallenge.org/>
> `status: complete` — 资源卡(competition),基于官网、Arc 公告、Cell 论文与 2025 复盘整理。

---

## 一句话 / One-liner
Arc Institute's annual public competition asking models to predict single-cell gene-expression shifts caused by single-gene CRISPR perturbations in a held-out cell type (H1 hESC), scored on a standardized 3-metric protocol — framed as "a Turing test for the virtual cell."

## 研究问题 / Problem
The perturbation-response field lacked rigorous, public, comparable benchmarks, making real progress in "AI virtual cell" models hard to judge. The challenge targets the hardest realistic task — **context generalization**: transferring learned perturbation rules to a new cell context and to unseen perturbation genes. The scientific payoff: an accurate perturbation→expression map enables in-silico screening for genes that revert a diseased cell state.

## 方法 / Method
Setup: given an unperturbed H1 hESC transcriptomic reference plus a training set of single-cell profiles for 150 gene perturbations, entrants build a model that predicts post-perturbation single-cell expression for held-out perturbation genes. Scoring uses a **composite of three metrics**: DES (accuracy on differentially expressed genes), PDS (ability to discriminate distinct perturbation effects), and MAE (global absolute error over all genes). The official baseline is Arc's **STATE** model (State Transition bidirectional transformer + State Embedding), benchmarked against cell-mean, linear, and GEARS baselines.

## 数据 / Data
A purpose-built single-cell transcriptomic (Perturb-seq) dataset: ~**300,000 H1 hESCs × 300 gene perturbations** spanning a broad phenotypic range. Splits: an unperturbed reference; a 150-gene training set (~150,000 cells); a 50-gene validation set driving a live leaderboard; and a 100-perturbation held-out test set. External data allowed: Arc Virtual Cell Atlas (>500M cells), scBaseCount, Tahoe-100M, and X-Atlas/Orion (largest public Perturb-seq).

## 主要结果 / Key results
Participation: 5,000+ registrants across 114 countries, 1,200+ teams submitting, 300+ final submissions. Baseline: on unseen single-gene perturbations STATE beat the cell-mean baseline by **26%** vs 19% (linear) and 22% (GEARS). Key takeaways: **pure AI did not consistently beat statistical baselines**; almost all models were worse than the naive baseline on MAE; hybrid deep-learning + statistics models won, and protein embeddings added value. Winners: 1st BM_xTVC (BioMap, xTrimoSCPerturb); 2nd XLearning Lab (metric-driven conditional generation + ESM-2); 3rd Outlier (TransPert); Generalist Prize to Altos Labs (go-with-the-flow flow matching).

## 创新点 / Contributions
- Establishes a public, standardized 3-metric protocol (DES/PDS/MAE) and a held-out-context generalization task for single-cell perturbation prediction.
- Releases a high-quality new dataset (300K H1 hESC × 300 perturbations) plus the STATE reference baseline.
- Large-scale participation yields empirical evidence on the real state of the art (hybrids > pure neural nets).

## 局限 / Limitations
- Single cell type (H1 hESC), single-gene perturbations, transcriptome-only — no combinatorial perturbations, spatial/multimodal, or tissue scale yet.
- Models generally lose to naive baselines on MAE, so absolute-expression prediction is not solved; the metrics themselves are still evolving.
- The task predicts perturbation effects; it does not directly solve the inverse "which genes revert a diseased state" problem.

## 与本研究方向的关系 / Relation to our direction
Maps directly onto **stage 2/3** of our pipeline — virtual-tissue modeling and predicting gene perturbations that revert an anomaly. The challenge delivers exactly a **forward perturbation→expression simulator**, the core engine of the revert inverse problem: with a reliable perturbation model, one can run in-silico gene scans toward a "normal" target state and rank revert targets. Reusable: (1) STATE as a pretrained virtual-cell baseline; (2) DES/PDS/MAE as a ready-made scoring protocol for our own revert evaluation; (3) the empirical lesson that pure AI didn't beat statistics — argues for keeping statistical/biological priors. Caveat: it stops at single cells, not tissue/spatial scale, so bridging to our virtual-*tissue* goal still needs spatial transcriptomics.

## 可复用资产 / Reusable assets
- **STATE model** (Arc's virtual cell model, State Transition + State Embedding) — 预训练基线,可作我们扰动模拟的起点。<https://arcinstitute.org/news/virtual-cell-model-state>
- **Challenge dataset**: 300K H1 hESC × 300-perturbation Perturb-seq + 官方 splits/leaderboard,<https://virtualcellchallenge.org/> (evaluation page: `/evaluation`).
- **Eval protocol**: DES / PDS / MAE composite scoring — 可直接移植为 revert 任务评测。
- **External corpora**: Arc Virtual Cell Atlas (>500M cells)、scBaseCount、Tahoe-100M、X-Atlas/Orion Perturb-seq。
- **Companion paper**: "Virtual Cell Challenge: Toward a Turing test for the virtual cell," *Cell*, 2025 — 任务/指标的权威描述。

## 待读 / Follow-ups
- STATE 模型论文与代码(State Transition / State Embedding 架构细节)。
- 获奖方案:xTrimoSCPerturb(BioMap)、TransPert、Altos "go-with-the-flow" flow-matching——混合与生成式思路。
- 独立基准论文 "Benchmarking virtual cell models for in-the-wild perturbation response" 与 "The Baseline Gap" (Research Square),审视指标可靠性。
- X-Atlas/Orion Perturb-seq 数据说明,评估作为额外训练/迁移语料的价值。

## 引用 / Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
