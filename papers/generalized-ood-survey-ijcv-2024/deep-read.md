# Generalized Out-of-Distribution Detection: A Survey

> **Bibkey** `Yang2021_211011334` · **Venue** International Journal of Computer Vision 132 (2024) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1007/s11263-024-02117-4> · arXiv <https://arxiv.org/abs/2110.11334>
> `status: complete` — 基于 arXiv 全文(v3,2024 年 1 月版)精读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 把异常检测(AD)、新颖性检测(ND)、开集识别(OSR)、OOD 检测和离群检测(OD)五个各自发展的子领域统一进一个「**广义 OOD 检测**」框架,用四个二分维度(检测协变量偏移还是语义偏移、ID 是单类还是多类、是否需要 ID 分类、归纳还是直推)厘清它们的区别;系统综述 OOD 检测方法(分类器输出、Outlier Exposure、梯度、贝叶斯、基础模型、密度、距离、重构),在 OpenOOD 上做统一公平对比,并列出挑战与未来方向。
<!-- EN --> Unifies five separately developed sub-fields — anomaly detection (AD), novelty detection (ND), open-set recognition (OSR), OOD detection and outlier detection (OD) — into one "**generalized OOD detection**" framework, distinguishing them along four dichotomies (covariate vs semantic shift, single- vs multi-class ID, whether ID classification is required, inductive vs transductive); systematically reviews OOD methods (classifier outputs, Outlier Exposure, gradients, Bayesian, foundation models, density, distance, reconstruction), runs a unified fair comparison on OpenOOD, and lays out challenges and future directions.

## 研究问题 / Problem
<!-- ZH --> OOD 检测这一术语自 2017 年(MSP 基线)出现后方法激增,而 AD、ND、OSR、OD 有相近的动机和方法,却**各自孤立发展**,定义与设定上的细微差别让读者和从业者困惑——同一个方法被放进不同基准、不同指标,难以互相比较、互相借鉴。已有 AD/ND/OSR/OD 的综述,但缺少对最新 OOD 检测方法的系统总结,也缺少跨子领域的公平对比。
<!-- EN --> Since the term OOD detection emerged in 2017 (the MSP baseline) methods have proliferated, while AD, ND, OSR and OD share motivation and methods yet **develop in isolation**; subtle differences in definitions and settings confuse readers and practitioners, and methods land in different benchmarks and metrics, hard to compare or cross-pollinate. Surveys exist for AD/ND/OSR/OD, but recent OOD methods lacked a systematic summary and a fair cross-sub-field comparison.

## 方法 / Method
<!-- ZH --> **统一框架**:先定义两类分布偏移——**协变量偏移**(P(X) 变、标签空间不变,如对抗样本、域偏移、风格变化)与**语义偏移**(P(Y) 变,新类别出现,并间接改变 P(X))。然后按四个维度定位五个子任务:**AD** 把 ID 当整体、不需要区分 ID 内部类别,分为**感官 AD**(sensory,只有协变量偏移,如 MVTec-AD 工业缺陷)与**语义 AD**(新类别);**ND**(单类/多类)关注语义异常,与语义 AD 等价;**OSR** = 多类 ND + 需要 ID 分类;**OOD 检测**在分类任务中与 OSR 等价,但覆盖更广的任务和解空间,且要求不损害 ID 分类;**OD** 是直推式的——没有训练/测试划分,「ID」就是观测集中的多数。另讨论相邻主题:拒识学习、域适应/泛化(期望只有协变量偏移、要保持预测)、novelty discovery、零样本、开放世界识别(OSR + 增量学习),以及 **conformal prediction**(作为新兴交叉方向)。**方法综述**:(1) 基于分类器——post-hoc 输出类(MSP、ODIN、energy、ReAct 等)、Outlier Exposure、梯度类(GradNorm)、贝叶斯、面向基础模型(CLIP 等);(2) 密度类;(3) 距离类(Mahalanobis、非参数 KNN、余弦等);(4) 重构类;(5) 理论分析。并回顾 OSR、AD/ND(密度、重构、距离、one-class 如 DeepSVDD、自监督)、OD 的方法。**实验**:基于 OpenOOD,ResNet-18 骨干,统一超参(SGD,lr 0.1,momentum 0.9,weight decay 5e-4,100 epoch);CIFAR-10 与 CIFAR-100 作 ID,各设 **near-OOD**(只有语义偏移:CIFAR-100/CIFAR-10 与 TinyImageNet)与 **far-OOD**(MNIST、SVHN、Texture、Places365),并剔除与 ID 语义重叠的图像(如 TinyImageNet 中 1,207 张属于 CIFAR-10 类别);只报告 AUROC。
<!-- EN --> **Unified framework**: first, two kinds of distribution shift — **covariate shift** (P(X) changes, label space fixed: adversarial examples, domain shift, style) and **semantic shift** (P(Y) changes, new classes, which indirectly changes P(X)). The five sub-tasks are then placed by four dichotomies: **AD** treats ID as a whole with no need to distinguish ID classes, split into **sensory AD** (covariate shift only, e.g. MVTec-AD industrial defects) and **semantic AD** (new classes); **ND** (one-/multi-class) concerns semantic anomalies and equals semantic AD; **OSR** = multi-class ND + ID classification; **OOD detection** equals OSR for classification but spans more tasks and solutions and must not hurt ID classification; **OD** is transductive — no train/test split, "ID" is the majority of the observed set. Neighbouring topics: learning with rejection, domain adaptation/generalization (expect covariate shift only and keep predicting), novelty discovery, zero-shot learning, open-world recognition (OSR + incremental learning), and **conformal prediction** (an emerging intersection). **Method review**: (1) classification-based — post-hoc output methods (MSP, ODIN, energy, ReAct, …), Outlier Exposure, gradient-based (GradNorm), Bayesian, and foundation-model OOD (CLIP etc.); (2) density-based; (3) distance-based (Mahalanobis, non-parametric KNN, cosine, …); (4) reconstruction-based; (5) theory. Methods of OSR, AD/ND (density, reconstruction, distance, one-class such as DeepSVDD, self-supervised) and OD are reviewed too. **Experiments**: on OpenOOD, ResNet-18 backbone, unified hyperparameters (SGD, lr 0.1, momentum 0.9, weight decay 5e-4, 100 epochs); CIFAR-10 and CIFAR-100 as ID, each with **near-OOD** (semantic shift only: CIFAR-100/CIFAR-10 and TinyImageNet) and **far-OOD** (MNIST, SVHN, Texture, Places365), removing images that overlap ID semantics (e.g. 1,207 TinyImageNet images belonging to CIFAR-10 classes); AUROC only.

## 方法谱系 / Method lineage
<!-- ZH --> **综述,横跨全部范式**——分类器 OOD(MSP `msp-ood-iclr-2017`、energy `energy-ood-neurips-2020`、ODIN、OE)、特征嵌入/距离(Mahalanobis `mahalanobis-ood-neurips-2018`、KNN)、密度/one-class(DeepSVDD `deep-svdd-icml-2018`)、重构/生成、合成异常/自监督(DRAEM `draem-iccv-2021`、CutPaste)、conformal(作为相邻方向)。框架中的感官/语义异常二分取自其参考文献 [32],并经 Ruff 等的 AD 综述(`ad-unifying-review-procieee-2021`,文中 [16])强调;实验依托 OpenOOD(同一团队的基准平台,NeurIPS 2022 及 v1.5)。缺少跨模态一致性这一范式。
<!-- EN --> **A survey spanning all paradigms** — classifier-based OOD (MSP `msp-ood-iclr-2017`, energy `energy-ood-neurips-2020`, ODIN, OE), feature-embedding / distance (Mahalanobis `mahalanobis-ood-neurips-2018`, KNN), density / one-class (DeepSVDD `deep-svdd-icml-2018`), reconstruction / generative, synthetic anomalies / self-supervised (DRAEM `draem-iccv-2021`, CutPaste), and conformal (as a neighbouring topic). Its sensory/semantic anomaly dichotomy is taken from its ref [32] as highlighted in Ruff et al.'s AD review (`ad-unifying-review-procieee-2021`, ref [16]); the experiments rest on OpenOOD (the same team's benchmark, NeurIPS 2022 and v1.5). The cross-modal-consistency paradigm is absent.

## 数据 / Data
<!-- ZH --> 综述本身不收集新数据。实验:CIFAR-10 / CIFAR-100(各 50k 训练、10k 测试)为 ID;near-OOD = CIFAR-100(或 CIFAR-10)+ TinyImageNet(分别去除 1,207 / 2,502 张语义重叠图);far-OOD = MNIST、SVHN、Texture、Places365(去除 1,305 张)。文中提到的 AD 基准:MVTec-AD;更大规模的 ImageNet OOD 基准与修正后的 NINCO 数据集。
<!-- EN --> No new data collected. Experiments: CIFAR-10 / CIFAR-100 (50k train, 10k test each) as ID; near-OOD = CIFAR-100 (or CIFAR-10) + TinyImageNet (removing 1,207 / 2,502 semantically overlapping images); far-OOD = MNIST, SVHN, Texture, Places365 (1,305 removed). AD benchmark referenced: MVTec-AD; larger ImageNet OOD benchmarks and the corrected NINCO dataset are discussed.

## 主要结果 / Key results
<!-- ZH --> OpenOOD 公平对比(Fig. 5,近/远 OOD 的 AUROC)的发现:
- **数据增强类最有效**:PixMix、CutMix 等,PixMix 在 CIFAR-10 near-OOD 上 93.1%,全场最佳;Ensemble、Mixup 也很好。
- **额外数据似乎不必要**:最佳用额外数据的 UDG 只在 CIFAR-10 near-OOD 上优于最佳无额外数据的 KNN,而它需要大量真实离群数据(这里用整个 TinyImageNet 训练集)。
- **post-hoc 方法总体优于需要训练的方法**,且 2021 年后的 post-hoc 方法在持续进步;经典 MDS(Mahalanobis)在 MNIST 上好、在 CIFAR-10/100 上差,而 KNN 在 MNIST、CIFAR、ImageNet 上都保持良好。
- **部分 AD 方法擅长 far-OOD**:为 MVTec-AD 像素级外观差异设计的 DRAEM、CutPaste 在 far-OOD 上表现很高(尤其 CIFAR-100 作 ID 时)。
- **协变量偏移**:引用的实验表明,多数现有 OOD 检测器对协变量偏移比对语义偏移更敏感(→「full-spectrum OOD」)。
<!-- EN --> Findings of the OpenOOD fair comparison (Fig. 5, near/far-OOD AUROC):
- **Data augmentation is most effective**: PixMix, CutMix, etc.; PixMix reaches 93.1% on CIFAR-10 near-OOD, the best overall; Ensemble and Mixup also do well.
- **Extra data seems unnecessary**: the best extra-data method (UDG) beats the best extra-data-free method (KNN) only on CIFAR-10 near-OOD, while requiring lots of real outliers (the whole TinyImageNet training set here).
- **Post-hoc methods generally beat training-based ones**, and post-hoc methods since 2021 keep improving; classic MDS (Mahalanobis) does well on MNIST but poorly on CIFAR-10/100, whereas KNN stays strong on MNIST, CIFAR and ImageNet.
- **Some AD methods excel at far-OOD**: DRAEM and CutPaste, designed for MVTec-AD pixel-level appearance differences, score highly on far-OOD (especially with CIFAR-100 as ID).
- **Covariate shift**: cited experiments show most current OOD detectors are more sensitive to covariate than to semantic shift (→ "full-spectrum OOD").

## 创新点 / Contributions
<!-- ZH --> (1) 第一个把 AD、ND、OSR、OOD、OD 统一起来的框架和清晰的任务分类图(Fig. 1–2);(2) 对 OOD 检测方法的全面综述(含基础模型时代);(3) 依托 OpenOOD 的跨子领域公平对比;(4) 挑战:合理的评估与基准(明确 OOD 类型;去除与 ID 重叠的样本)、无离群训练、分类与检测的权衡、真实大规模基准;未来方向:跨子任务方法迁移、OOD 检测与泛化结合、开集噪声标签、更广的学习任务(分割、时间序列、LLM 幻觉)、借助世界模型 / 基础模型。
<!-- EN --> (1) The first framework unifying AD, ND, OSR, OOD and OD, with a clear task taxonomy (Figs. 1–2); (2) a comprehensive review of OOD methods, including the foundation-model era; (3) a cross-sub-field fair comparison via OpenOOD; (4) challenges — proper evaluation and benchmarking (specify the OOD type; remove ID-overlapping samples), outlier-free training, the classification–detection trade-off, real large-scale benchmarks — and future directions: cross-sub-task method transfer, combining OOD detection with generalization, open-set noisy labels, broader tasks (segmentation, time series, LLM hallucination), and world / foundation models.

## 局限 / Limitations
<!-- ZH --> 实验只在 CIFAR 规模、只报 AUROC,且刻意不评测纯协变量偏移(作者解释是为避免过度强调协变量偏移检测);框架以分类任务为主要示例,对生物医学、连续标签或无明确类别的数据讨论很少;conformal 只作为相邻主题一笔带过;没有覆盖多模态/跨模态一致性作为检测信号;作为综述,对每种方法只做简述,结论依赖 OpenOOD 的统一超参设定。
<!-- EN --> Experiments are CIFAR-scale and AUROC-only, and deliberately exclude pure covariate-shift evaluation (to avoid over-emphasizing covariate-shift detection, the authors say); the framework is illustrated mainly with classification and says little about biomedical, continuous-label or class-free data; conformal gets only a brief neighbouring-topic mention; multi-modal / cross-modal agreement as a detection signal is not covered; as a survey, each method gets a short summary and conclusions depend on OpenOOD's unified hyperparameters.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> **这是给 KidneyAnomalyBench 定义任务类型的「词汇表」**。用它的维度给肾脏场景定位:(1) 「健康参照中不存在的细胞状态」(如失败修复的 PT、新的免疫浸润状态)= **语义偏移**;只需标出 → ND/语义 AD;同时要给已知细胞注释 → OSR/OOD 检测(参照映射 + 拒识)。(2) **批次效应、环境 RNA、doublet、Xenium 分割错误、H&E 染色差异** = **协变量偏移**——我们希望对它**稳健**,而不是把它报出来。综述引用的结论「多数 OOD 检测器对协变量偏移比语义偏移更敏感」正是 Plan A 的核心风险:不加处理的检测器会把 artifact 当成疾病。它提出的「full-spectrum OOD」(对协变量偏移泛化、对语义偏移敏感)正好是 Plan A 用**跨模态一致性**分离 artifact 与疾病的目标的形式化表述——而跨模态一致性本身不在综述的方法分类里,是我们可以补的空白。(3) 在单个数据集内部做 doublet/低质量细胞剔除 = **直推式 OD**。**评估层面可直接借用**:(a) near-OOD vs far-OOD 分层——肾脏中 near = 轻度损伤 / aPT 等邻近状态,far = 其他器官细胞或完全不同的组织;(b) 「OOD 测试集不得含 ID 类别」——疾病活检里大部分细胞其实是正常的,若把整份疾病活检当「异常」标签,评测就会像早期 OOD 基准那样被污染,所以 KidneyAnomalyBench 需要专家在细胞/区域层面验证标签;(c) 「明确说明检测哪种 OOD」的要求。**方法层面**:「post-hoc 方法优于训练方法、KNN 比 Mahalanobis 更稳」提示在 scVI / 基础模型嵌入上先跑 post-hoc 距离类基线;「额外数据不必要」也支持不依赖辅助离群集。**仓库中相关文献**:`pathology-ad-bench-mlhealth-2025` 与 `medianomaly-media-2025` 是病理/医学影像里相同「统一协议公平对比」思路的落地;`ad-unifying-review-procieee-2021` 是互补的 AD 侧综述;`conformal-scrna-bioinformatics-2025` 落实了综述只是提到的 conformal × OOD 方向。**对 Plan B**:它的任务分类法是设计组学 agent **失败分类法**的模板(先定义偏移类型再定义失败类型),而「OOD 检测用于 LLM 幻觉」被列为未来方向,与 Plan B 的 claim 验证直接相关。
<!-- EN --> **This is the vocabulary for defining KidneyAnomalyBench's task types.** Placing the kidney setting on its axes: (1) "cell states absent from the healthy reference" (failed-repair PT, a new immune-infiltrate state) = **semantic shift**; flagging only → ND / semantic AD; flagging while annotating known cells → OSR / OOD detection (reference mapping + rejection). (2) **Batch effects, ambient RNA, doublets, Xenium segmentation errors, H&E stain variation** = **covariate shift** — which we want to be **robust to**, not report. The survey's cited finding that "most OOD detectors are more sensitive to covariate than semantic shift" is exactly Plan A's core risk: an untreated detector reports artifacts as disease. Its "full-spectrum OOD" (generalize over covariate shift, detect semantic shift) is a formal statement of Plan A's goal of separating artifact from disease via **cross-modal agreement** — and cross-modal agreement itself is missing from the survey's method taxonomy, a gap we can fill. (3) Removing doublets / low-quality cells inside one dataset = **transductive OD**. **Directly reusable for evaluation**: (a) near- vs far-OOD stratification — in kidney, near = mild injury / aPT-like neighbouring states, far = other organs' cells or entirely different tissue; (b) "OOD test sets must not contain ID classes" — most cells in a disease biopsy are actually normal, so labelling an entire disease biopsy as "anomalous" contaminates evaluation the way early OOD benchmarks were, hence KidneyAnomalyBench needs expert validation at the cell/region level; (c) the demand to state which OOD type is being detected. **Methodologically**: "post-hoc beats training-based, KNN is more robust than Mahalanobis" suggests starting with post-hoc distance baselines on scVI / foundation-model embeddings; "extra data seems unnecessary" supports not depending on auxiliary outlier sets. **Related repo papers**: `pathology-ad-bench-mlhealth-2025` and `medianomaly-media-2025` apply the same "unified protocol, fair comparison" idea to pathology / medical imaging; `ad-unifying-review-procieee-2021` is the complementary AD-side review; `conformal-scrna-bioinformatics-2025` realizes the conformal × OOD direction the survey only mentions. **For Plan B**: its task taxonomy is a template for an omics-agent **failure taxonomy** (define the shift types before the failure types), and "OOD detection for LLM hallucination" is listed as a future direction directly relevant to Plan B's claim verification.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码 / 基准:** OpenOOD——统一框架与排行榜,含 MSP、ODIN、MDS、EBO、ReAct、KNN、DeepSVDD、DRAEM、CutPaste 等实现,可直接作为肾脏嵌入上的基线集合。 <!-- EN --> **Code / benchmark:** OpenOOD — a unified framework and leaderboard with implementations of MSP, ODIN, MDS, EBO, ReAct, KNN, DeepSVDD, DRAEM, CutPaste and more — a ready baseline suite for kidney embeddings.
<!-- ZH/EN --> <https://github.com/Jingkang50/OpenOOD>
- <!-- ZH --> **任务分类法:** Fig. 1(四个二分维度)与 Fig. 2(五个子任务示意),可直接用来写 KidneyAnomalyBench 的任务定义。 <!-- EN --> **Task taxonomy:** Fig. 1 (four dichotomies) and Fig. 2 (five sub-task diagrams) — directly usable for writing KidneyAnomalyBench task definitions.
- <!-- ZH --> **基准构建规则:** near/far-OOD 分层 + 去除与 ID 语义重叠的样本。 <!-- EN --> **Benchmark-building rules:** near/far-OOD stratification + removing samples that overlap ID semantics.

## 待读 / Follow-ups
- <!-- ZH --> OpenOOD v1.5 报告与 full-spectrum OOD(协变量偏移下的 ID)论文——最接近「对批次效应稳健、对疾病敏感」的设定。 <!-- EN --> The OpenOOD v1.5 report and the full-spectrum OOD paper (covariate-shifted ID) — the setting closest to "robust to batch effects, sensitive to disease".
- <!-- ZH --> 非参数 KNN OOD(Sun 等,2022)与 ReAct——综述中表现稳健的 post-hoc 方法。 <!-- EN --> Non-parametric KNN OOD (Sun et al., 2022) and ReAct — robust post-hoc methods in the survey.
- <!-- ZH --> 综述引用的 conformal × OOD 工作(其参考文献 [104–106])。 <!-- EN --> The conformal × OOD works the survey cites (its refs [104–106]).

## 引用 / Cite
```bibtex
@article{Yang2021_211011334,
  title = {Generalized Out-of-Distribution Detection: A Survey},
  author = {Yang, Jingkang and Zhou, Kaiyang and Li, Yixuan and Liu, Ziwei},
  journal = {International Journal of Computer Vision},
  volume = {132},
  pages = {5635--5662},
  year = {2024},
  doi = {10.1007/s11263-024-02117-4},
  eprint = {2110.11334},
  archivePrefix = {arXiv},
  url = {https://doi.org/10.1007/s11263-024-02117-4}
}
```
