# Virtual Cell Challenge

> **Bibkey** `virtual-cell-challenge` · **Venue** Arc Institute (competition; companion paper in *Cell*, 2025) · **Category** competition · **Relevance** medium · **Access** open
> **Link** <https://virtualcellchallenge.org/>
> `status: abstract-only` — 资源卡(competition)。*Cell* 评论文章(Roohani et al., *Cell* 188:3370–3374, 2025;2025-10-23 起 CC BY-NC-ND)的全文本次未能获取(cell.com 与 ScienceDirect 返回 403),只读了摘要(Europe PMC)。其余内容来自 2026-10-27 读取的 Arc Institute 官方网页:发布公告(2025-06-26)、数据说明 "Behind the data"(2025-08-22)、赛后总结 "wrap-up"(2025-12-06)、2026 届公告,以及 State 模型新闻页。virtualcellchallenge.org 是 JavaScript 页面,抓取不到正文。/ Competition resource card. The full text of the *Cell* commentary could not be retrieved (403 from cell.com and ScienceDirect); only its abstract (Europe PMC) was read. Everything else comes from Arc Institute pages read on 2026-10-27: launch announcement (26 Jun 2025), "Behind the data" (22 Aug 2025), the 2025 wrap-up (6 Dec 2025), the 2026 announcement, and the State model news page. virtualcellchallenge.org is a JavaScript app and returned no text.

---

## 一句话 / One-liner
<!-- ZH --> Arc Institute 每年举办的公开竞赛:给定一个新细胞类型(2025 届是 H1 人胚胎干细胞)里部分基因被 CRISPRi 敲低后的单细胞表达,预测其余未见过的敲低会让单细胞表达怎样变化;官方把它定位为"virtual cell 的图灵测试"(*Cell* 标题, Arc 发布公告)。
<!-- EN --> An annual open competition by the Arc Institute: given single-cell expression after CRISPRi knockdown of some genes in a new cell type (H1 human embryonic stem cells in 2025), predict how unseen knockdowns change single-cell expression; framed as "a Turing test for the virtual cell" (*Cell* title, Arc launch page).

## 要点 / Takeaways
- <!-- ZH --> 任务本质是**正向模拟器**:输入"敲低哪个基因",输出"细胞表达会变成什么样"。这是 revert 问题(反过来找该敲哪个基因)所需的前向模型(Arc 发布公告)。 <!-- EN --> The task is a **forward simulator**: input "which gene is knocked down", output "what the cells' expression becomes" — the forward model a reversion search (which gene to perturb) would need (Arc launch page).
- <!-- ZH --> 2025 数据:约 30 万个 H1 细胞、300 个靶基因(150 训练 / 50 验证 / 100 测试),每个扰动约 1,000 个细胞,每个细胞中位数 >50,000 UMI("Behind the data")。 <!-- EN --> 2025 data: ~300,000 H1 cells, 300 target genes (150 train / 50 validation / 100 test), ~1,000 cells per perturbation, median >50,000 UMIs per cell ("Behind the data").
- <!-- ZH --> 评分 = DES、PDS、MAE 三个指标相对"扰动均值基线"归一化后取平均("Behind the data")。几乎所有模型在 MAE 上都**不如**基线,前几名主要靠 PDS 和 DES 拿分(wrap-up)。 <!-- EN --> Score = DES, PDS and MAE, each normalised against a perturbation-mean baseline and averaged ("Behind the data"). Almost all models were **worse** than the baseline on MAE; top teams scored mainly via PDS and DES (wrap-up).
- <!-- ZH --> 主办方的结论:模型没有在所有指标上稳定胜过朴素基线;混合"深度学习 + 统计特征"的方案好于纯神经网络;损失函数设计和架构同样重要;优化一个指标常以牺牲其他指标为代价(wrap-up)。 <!-- EN --> Organisers' conclusions: models did not consistently beat naive baselines across all metrics; hybrids of deep learning and statistical features beat purely neural models; loss design mattered as much as architecture; optimising one metric often hurt others (wrap-up).
- <!-- ZH --> 规模:5,000+ 人注册、来自 114 国;1,200+ 队提交结果,300+ 队最终提交(wrap-up)。 <!-- EN --> Scale: 5,000+ registrants from 114 countries; 1,200+ teams submitted results, 300+ made final submissions (wrap-up).
- <!-- ZH --> 2026 届改为**零样本**:六个细胞系(3 个验证、3 个最终测试),不发专门训练集,终评用六个指标的综合分(2026 公告)。 <!-- EN --> The 2026 edition is **zero-shot**: six cell lines (3 for validation, 3 for final testing), no challenge-specific training set, final ranking on an aggregate of six metrics (2026 announcement).

## 研究问题 / Problem
<!-- ZH --> "virtual cell"(细胞状态模型)的一个核心目标是预测细胞对扰动的反应,但领域缺少统一的评测框架和专门生成的数据集(*Cell* 摘要)。主办方想用一个反复举办的开放基准竞赛提供评测框架、专门数据和交流场所(*Cell* 摘要),并检验模型能否泛化到一个新的细胞语境(Arc 发布公告中 Dave Burke 的说法)。Arc 在总结中把问题表述为:计算模型能否替代一次 Perturb-seq 实验(wrap-up)。
<!-- EN --> A key goal of "virtual cell" (cell-state) models is predicting cellular responses to perturbations, but the field lacks a shared evaluation framework and purpose-built datasets (*Cell* abstract). The organisers set up a recurring open benchmark competition to provide the framework, the data and a venue (*Cell* abstract), testing whether models generalise to a new cell context (Dave Burke, Arc launch page). Arc's wrap-up phrases the question as: can a computational model stand in for a Perturb-seq experiment (wrap-up)?

## 方法 / Method
<!-- ZH --> 1. **实验设计**:在 H1 人胚胎干细胞中做双 guide 的 CRISPRi 敲低(催化失活的 Cas9 融合 KRAB 抑制结构域,压低靶基因转录,而不是切断 DNA),再用单细胞 RNA 测序(10x Genomics Flex,一种固定后、基于探针的化学)读出每个细胞的表达("Behind the data")。这种"批量扰动 + 单细胞读出"的实验叫 Perturb-seq。
<!-- ZH --> 2. **选细胞类型**:选 H1 是因为它被充分表征(属于 ENCODE),且不同于现有 Perturb-seq 数据中占主导的永生化细胞系(K562、A375)("Behind the data")。
<!-- ZH --> 3. **选靶基因**:先在 H1 中做大规模 CRISPRi 预筛,按每个扰动引起的差异表达基因数分档,每档抽样以保证多样性;用 ContrastiveVI+ 在隐空间聚类扰动反应,保证覆盖不同反应模式;同时要求 guide 分配干净、靶基因本底表达足够、Flex 能测到明显抑制("Behind the data")。
<!-- ZH --> 4. **划分**:每个靶基因按差异表达基因数和高质量细胞数打分,分档后随机分到训练 150 / 验证 50 / 测试 100,使三组构成平衡("Behind the data")。报名即可拿到训练数据;比赛中段用验证集提交,结果上实时排行榜;最终测试集在截止前约一周放出;只按最终测试集排名(Arc 发布公告)。
<!-- ZH --> 5. **指标**:DES(差异表达分)= 预测与真实差异表达基因集合的重叠;PDS(扰动区分分)= 每个预测是否最接近它自己那个扰动的真实表达谱;MAE = 全转录组的平均绝对误差。三者都相对扰动均值基线归一化,再平均成排行榜总分("Behind the data")。
<!-- ZH --> 6. **Generalist Prize(赛中追加)**:因为 MAE 已不再影响排行榜,主办方追加一个奖项:对前 50 个最终提交用 7 个指标排名(DES、PDS、MAE、Pearson delta 相关、log fold change 的 Spearman 相关、AUPRC、效应量的 Spearman 相关;后四个来自 State 模型的评测),取平均名次最高者(wrap-up)。
<!-- ZH --> 7. **外部数据**:允许用 Arc Virtual Cell Atlas(超过 5 亿个细胞)和其他公开数据训练(Arc 发布公告)。
<!-- EN --> 1. **Experiment**: dual-guide CRISPRi knockdown in H1 human embryonic stem cells (catalytically dead Cas9 fused to a KRAB repressor, which silences transcription of the target gene instead of cutting DNA), read out by single-cell RNA-seq with 10x Genomics Flex (a fixation-based, probe-based chemistry) ("Behind the data"). Pooled perturbation with a single-cell readout is called Perturb-seq.
<!-- EN --> 2. **Cell type**: H1 was chosen because it is well characterised (part of ENCODE) and unlike the immortalised lines (K562, A375) that dominate existing Perturb-seq data ("Behind the data").
<!-- EN --> 3. **Target genes**: a large CRISPRi pilot screen in H1 counted differentially expressed (DE) genes per perturbation; perturbations were binned by strength and sampled per bin for diversity; ContrastiveVI+ clustered responses in latent space to cover different response modes; guides also had to assign cleanly, targets needed enough basal expression, and repression had to be visible with Flex ("Behind the data").
<!-- EN --> 4. **Splits**: each target got a stratification score from its DE-gene count and number of high-quality cells; genes were binned and randomly assigned to 150 train / 50 validation / 100 test so the splits are balanced ("Behind the data"). Training data come at sign-up; mid-competition validation submissions feed a live leaderboard; the final test set is released about a week before the deadline; ranking uses only the final test set (Arc launch page).
<!-- EN --> 5. **Metrics**: DES = overlap of predicted and true DE gene sets; PDS = whether each prediction is closest to its own perturbation's true profile; MAE = mean absolute error over all genes. Each is normalised against a perturbation-mean baseline and averaged into the leaderboard score ("Behind the data").
<!-- EN --> 6. **Generalist Prize (added mid-competition)**: since MAE no longer moved the leaderboard, the top 50 final entries were ranked on 7 metrics (DES, PDS, MAE, Pearson delta correlation, Spearman correlation of log fold change, AUPRC, Spearman correlation of effect size; the last four from the State model's evaluation) and the best average rank won (wrap-up).
<!-- EN --> 7. **External data**: training on the Arc Virtual Cell Atlas (over half a billion cells) and other public data is allowed (Arc launch page).

## 方法图 / Method diagram
```mermaid
flowchart LR
  A["Pilot CRISPRi screen<br/>in H1 hESC"] --> B["Pick 300 targets<br/>by strength and response mode"]
  B --> C["Perturb-seq<br/>dual-guide CRISPRi, 10x Flex"]
  C --> D["Split targets<br/>150 train, 50 val, 100 test"]
  D --> E["Teams predict<br/>single-cell expression"]
  E --> F["DES, PDS, MAE<br/>vs perturbation-mean baseline"]
  F --> G["Leaderboard<br/>plus 7-metric Generalist Prize"]
```

## 数据 / Data
<!-- ZH --> 约 300,000 个 H1 人胚胎干细胞,300 个 CRISPRi 靶基因(150 / 50 / 100);每个扰动的细胞数中位数/均值约 1,000;每个细胞 UMI 中位数/均值 >50,000;63% 的细胞两个 guide 都被正确检出;83% 的细胞靶基因被敲低 >80%("Behind the data", wrap-up)。按每扰动约 1,000 个细胞推算,训练集约 15 万个细胞(这是我们的推算,网页未直接给出)。2025 数据集现已可从 Arc Virtual Cell Atlas 下载(2026 公告)。
<!-- EN --> ~300,000 H1 human embryonic stem cells, 300 CRISPRi targets (150 / 50 / 100); median/mean ~1,000 cells per perturbation; median/mean >50,000 UMIs per cell; 63% of cells with both correct guides detected; 83% of cells with >80% knockdown ("Behind the data", wrap-up). At ~1,000 cells per perturbation the training set is roughly 150,000 cells (our arithmetic; not stated on the pages). The 2025 dataset can now be downloaded through the Arc Virtual Cell Atlas (2026 announcement).

## 主要结果 / Key results
<!-- ZH -->
- **参与**:5,000+ 注册(114 国),1,200+ 队提交,300+ 队最终提交(wrap-up)。
- **对基线**:模型总体没有在所有指标上稳定胜过朴素基线,但在扰动区分和差异表达基因识别上有进步;几乎所有模型 MAE 比基线差(wrap-up)。
- **指标漏洞**:一位参赛者的分析发现,基于 L1 的 PDS 会随预测幅度变大而上升,趋近于只看符号的余弦相似度(wrap-up)。主办方提到未来可能用"范数匹配"的 PDS 变体(wrap-up)。
- **第 1 名(10 万美元)**:BM_xTVC(BioMap Research),xTrimoSCPerturb:改进的 scFoundation 预训练模型 + 蛋白质 embedding + 训练集中差异表达基因频率与平均表达作特征;融合损失(PDS + DES + 小权重 MAE);在 pseudo-bulk(把同一扰动的细胞求平均)上训练(wrap-up)。
- **第 2 名(5 万美元)**:XLearning Lab(四川大学 / 天府锦城实验室):全连接网络 + pseudo-bulk + ESM-2 蛋白 embedding + 残差学习,MSE 损失;只用公开 Perturb-seq 数据训练(wrap-up)。
- **第 3 名(2.5 万美元)**:Outlier(芝加哥大学、达特茅斯、香港大学),TransPert:基于汇总数据的统计框架,把参考细胞系数据按相似度加权聚合,再做针对 PDS 调好的全局线性缩放(wrap-up)。
- **Generalist Prize(10 万美元)**:Altos Labs,go-with-the-flow:U-Net 结构的 flow matching 生成模型,先在约 700 万个单细胞上预训练再在 H1 上微调,7 个指标平均名次最高(wrap-up)。
<!-- EN -->
- **Participation**: 5,000+ registrants (114 countries), 1,200+ teams submitting, 300+ final submissions (wrap-up).
- **Versus baselines**: models did not consistently beat naive baselines on all metrics, though they improved on perturbation discrimination and DE-gene identification; almost all were worse than baseline on MAE (wrap-up).
- **Metric loophole**: a participant showed that L1-based PDS rises as prediction magnitude grows, approaching sign-based cosine similarity (wrap-up); norm-matched PDS variants are mentioned as future work (wrap-up).
- **1st ($100,000)**: BM_xTVC (BioMap Research), xTrimoSCPerturb: improved scFoundation-based pretrained model + protein embeddings + training-set DE-gene frequency and mean expression as features; fused loss (PDS + DES + small-weight MAE); trained on pseudo-bulk (cells averaged per perturbation) (wrap-up).
- **2nd ($50,000)**: XLearning Lab (Sichuan University / Tianfu Jincheng Lab): fully connected network on pseudo-bulk + ESM-2 protein embeddings + residual learning, MSE loss; trained only on public Perturb-seq data (wrap-up).
- **3rd ($25,000)**: Outlier (U Chicago, Dartmouth, HKU), TransPert: a statistical framework on summary-level data — similarity-aware aggregation of reference cell-line data, then a global linear scaling tuned for PDS (wrap-up).
- **Generalist Prize ($100,000)**: Altos Labs, go-with-the-flow: a flow-matching generative model with a U-Net, pretrained on ~7 million single cells and fine-tuned on H1; best average rank over the 7 metrics (wrap-up).

## 创新点 / Contributions
- <!-- ZH --> 专门为评测生成的高质量 Perturb-seq 数据集(H1、双 guide CRISPRi、深测序),并按反应强度和反应模式平衡地划分(“Behind the data”)。 <!-- EN --> A purpose-built, high-quality Perturb-seq dataset (H1, dual-guide CRISPRi, deep sequencing) with splits balanced by response strength and mode ("Behind the data").
- <!-- ZH --> 公开、可重复的评测框架(DES / PDS / MAE,相对基线归一化),每年迭代(*Cell* 摘要, wrap-up)。 <!-- EN --> A public, repeatable evaluation framework (DES / PDS / MAE, baseline-normalised), iterated yearly (*Cell* abstract, wrap-up).
- <!-- ZH --> 用大规模参赛得到关于"当前方法到底行不行"的经验证据,包括指标可被钻空子的教训(wrap-up)。 <!-- EN --> Large-scale participation yields empirical evidence on where methods stand, including the lesson that metrics can be gamed (wrap-up).

## 局限 / Limitations
- <!-- ZH --> 主办方:单个指标抓不住模型质量;窄的评分函数会诱导优化指标而非生物学,因此 2026 年改用六指标综合分(wrap-up, 2026 公告)。 <!-- EN --> Organisers: no single metric captures model quality; a narrow scoring function invites optimising the metric rather than the biology, hence a six-metric aggregate in 2026 (wrap-up, 2026 announcement).
- <!-- ZH --> 主办方:模型准确度、指标设计和生物学泛化仍有很大提升空间(2026 公告)。 <!-- EN --> Organisers: model accuracy, metric design and biological generalisation still need work (2026 announcement).
- <!-- ZH --> 我们的理解:2025 届只有一个细胞类型、单基因敲低、只有转录组;没有组织、空间或多细胞相互作用。 <!-- EN --> Our reading: the 2025 edition has one cell type, single-gene knockdowns and transcriptome only; no tissue, spatial or cell–cell context.
- <!-- ZH --> 我们的理解:前几名大量依赖 pseudo-bulk(细胞平均),说明当前评分主要奖励"平均反应"而非单细胞异质性。 <!-- EN --> Our reading: top teams relied heavily on pseudo-bulk (cell averages), so the scoring mainly rewards the average response rather than single-cell heterogeneity.
- <!-- ZH --> 我们的理解:本卡没有读到 *Cell* 评论全文,指标的精确公式(如 DES 的阈值、PDS 的距离)需看论文或评测代码确认。 <!-- EN --> Our reading: we did not read the full *Cell* commentary; exact metric formulas (DES thresholds, PDS distance) must be checked in the paper or evaluation code.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 我们的理解:这个竞赛对应 detect → model → revert 里的 **model → revert**:它评测的是"给定扰动,预测细胞状态"的前向模型;revert 则是反问题——给定异常状态和目标正常状态,找出能把前者推向后者的扰动。可借鉴的有三点。(1) **评测设计**:按反应强度和反应模式平衡划分、相对朴素基线归一化,这套做法可以搬到课题 1 的异常检测基准上——例如异常分也应相对"按细胞类型取均值"这类朴素基线报告。(2) **指标会被钻空子**:PDS 随预测幅度上升、MAE 被放弃,这提醒我们在 KidneyAnomalyBench 里不要只用一个指标排名,要配多个互补指标和专家复核。(3) **对 revert 的直接价值有限**:H1 干细胞与肾小管/足细胞等肾脏细胞差别很大,单细胞而非组织尺度;要做肾脏 revert,还需要肾脏细胞类型的扰动数据。2026 届的零样本、多细胞系设置更接近"在没见过扰动的细胞类型里预测"——这正是我们在肾脏里会遇到的情况。
<!-- EN --> Our reading: the challenge maps to **model → revert** in detect → model → revert: it scores the forward model "given a perturbation, predict the cell state"; reversion is the inverse — given an abnormal state and a normal target, find perturbations that move one to the other. Three lessons. (1) **Evaluation design**: splits balanced by response strength and mode and scores normalised against a naive baseline transfer directly to Topic 1's anomaly benchmark — anomaly scores should also be reported relative to a naive baseline such as per-cell-type means. (2) **Metrics get gamed**: PDS inflating with prediction magnitude and MAE being abandoned warn us not to rank KidneyAnomalyBench on a single metric; use several complementary metrics plus expert review. (3) **Limited direct value for kidney reversion**: H1 stem cells are far from tubule or podocyte cells, and the setting is single-cell, not tissue; kidney reversion would need perturbation data in kidney cell types. The 2026 zero-shot, multi-cell-line setting is closer to predicting in a cell type never perturbed — the situation we would face in kidney.

## 可复用资产 / Reusable assets
- <!-- ZH --> **竞赛网站**(JavaScript 页面,需浏览器打开): <!-- EN --> **Challenge site** (JavaScript app, open in a browser):
<!-- ZH/EN --> <https://virtualcellchallenge.org/>
- <!-- ZH --> **2025 数据集**:已可从 Arc Virtual Cell Atlas 下载(2026 公告)。 <!-- EN --> **2025 dataset**: downloadable through the Arc Virtual Cell Atlas (2026 announcement).
<!-- ZH/EN --> <https://arcinstitute.org/virtual-cell-initiative>
- <!-- ZH --> **数据说明与指标**: <!-- EN --> **Data description and metrics**:
<!-- ZH/EN --> <https://arcinstitute.org/news/behind-the-data-virtual-cell-challenge>
- <!-- ZH --> **赛后总结与获奖方案**: <!-- EN --> **Wrap-up and winning solutions**:
<!-- ZH/EN --> <https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up>
- <!-- ZH --> **State 模型**(Arc 的 virtual cell 模型,State Embedding + State Transition 两个模块;用近 1.7 亿个观测细胞和 70 个细胞系中超过 1 亿个扰动细胞训练)(State 新闻页)。 <!-- EN --> **State model** (Arc's virtual-cell model with State Embedding + State Transition modules; trained on nearly 170 million observational cells and over 100 million perturbed cells across 70 cell lines) (State news page).
<!-- ZH/EN --> <https://arcinstitute.org/news/virtual-cell-model-state>

## 待读 / Follow-ups
- <!-- ZH --> *Cell* 评论全文(DOI 10.1016/j.cell.2025.06.008),核对 DES / PDS / MAE 的精确定义。 <!-- EN --> Full *Cell* commentary (DOI 10.1016/j.cell.2025.06.008) for exact DES / PDS / MAE definitions.
- <!-- ZH --> 2026 届 *Cell* 文章 "Virtual Cell Challenge 2026: Benchmarking zero-shot generalization across cellular contexts" 与六指标方案。 <!-- EN --> The 2026 *Cell* article "Virtual Cell Challenge 2026: Benchmarking zero-shot generalization across cellular contexts" and its six metrics.
<!-- ZH/EN --> <https://arcinstitute.org/news/virtual-cell-challenge-2026>
- <!-- ZH --> Altos Labs 的 flow-matching 预印本(2026 公告提到已发布)。 <!-- EN --> Altos Labs' flow-matching preprint (mentioned as posted in the 2026 announcement).
- <!-- ZH --> State 模型论文与 cell-eval 评测工具。 <!-- EN --> The State model paper and the cell-eval evaluation tool.

## 图表 / Figures & tables

<!-- ZH --> 本条目是竞赛资源卡,不嵌入图片。下面两张表按上述 Arc 官方网页整理。 <!-- EN --> Competition resource card; no images are embedded. The two tables below are compiled from the Arc pages listed above.

### 结果表 / Results

<!-- ZH --> **表1.** 2025 数据集划分(“Behind the data”)。 <!-- EN --> **Table 1.** 2025 dataset split ("Behind the data").

| Split | Target genes | Role |
|---|---|---|
| Training | 150 | Given at sign-up |
| Validation | 50 | Live leaderboard during the competition |
| Final test | 100 | Released ~1 week before the deadline; sole basis for ranking |
| **Total** | **300** | ~300,000 H1 cells, ~1,000 cells per target |

<!-- ZH --> **表2.** 2025 获奖方案(wrap-up)。 <!-- EN --> **Table 2.** 2025 winners (wrap-up).

| Place | Team | Approach |
|---|---|---|
| 1st ($100,000) | BM_xTVC (BioMap Research) | xTrimoSCPerturb: scFoundation-based + protein embeddings + statistical features; fused PDS+DES+MAE loss; pseudo-bulk |
| 2nd ($50,000) | XLearning Lab | Fully connected net, ESM-2 embeddings, residual learning, MSE; public Perturb-seq only |
| 3rd ($25,000) | Outlier | TransPert: similarity-weighted aggregation of reference cell lines + linear scaling tuned for PDS |
| Generalist ($100,000) | Altos Labs | go-with-the-flow: U-Net flow matching, pretrained on ~7M cells |

## 引用 / Cite
```bibtex
@article{Roohani_2025, title={Virtual Cell Challenge: Toward a Turing test for the virtual cell}, volume={188}, ISSN={0092-8674}, url={http://dx.doi.org/10.1016/j.cell.2025.06.008}, DOI={10.1016/j.cell.2025.06.008}, number={13}, journal={Cell}, publisher={Elsevier BV}, author={Roohani, Yusuf H. and Hua, Tony J. and Tung, Po-Yuan and Bounds, Lexi R. and Yu, Feiqiao B. and Dobin, Alexander and Teyssier, Noam and Adduri, Abhinav and Woodrow, Alden and Plosky, Brian S. and Mehta, Reshma and Hsu, Benjamin and Sullivan, Jeremy and Ricci-Tam, Chiara and Li, Nianzhen and Kazaks, Julia and Gilbert, Luke A. and Konermann, Silvana and Hsu, Patrick D. and Goodarzi, Hani and Burke, Dave P.}, year={2025}, month=jun, pages={3370–3374} }
```
