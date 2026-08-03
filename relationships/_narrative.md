## 叙述 / How these papers relate

<!-- ZH --> 我们把整个研究方向拆成一条流水线,每一篇/每个资源落在其中一环:**异常检测 (anomaly detection) → 虚拟组织建模 (virtual tissue) → 基因/扰动预测以"逆转"异常 (revert)**。下面按流水线阶段说明它们的关系,以及跨阶段的复用关系。
<!-- EN --> We frame the direction as a pipeline — **anomaly detection → virtual-tissue modelling → gene/perturbation prediction to *revert* the anomaly** — and place each item in a stage, then note the cross-stage reuse.

### ① 异常检测 / Anomaly detection
<!-- ZH --> 定位"变了"的区域。`spatial-natcommun-2024`(STANDS)在空间转录组上直接做异常解剖区域检测,是本方向最核心的方法参照;`histo-nejmai-2024` 与 `histo-anomaly-bi-repo` 把异常检测搬到临床级组织病理图像(前者方法+临床验证,后者可直接复用代码);`histo-sciencedirect-2026`(PathPrism)、`histo-miccai-2025`(AnoPILaD)补充最新的组织病理方法;`imaging-ehjdh-2026`(CT 异常射血分数)与 `imaging-nature-2026`(ECG 深度学习生物标志物)提供*跨模态*的异常/生物标志物发现范式——方法可迁移,模态是心脏影像/信号。
<!-- EN --> Flag the changed regions. `spatial-natcommun-2024` (STANDS) detects anomalous anatomic regions directly in spatial transcriptomics — the closest method reference; `histo-nejmai-2024` and `histo-anomaly-bi-repo` bring anomaly detection to clinical-grade histopathology (method+validation, and reusable code respectively); `histo-sciencedirect-2026` (PathPrism) and `histo-miccai-2025` (AnoPILaD) add the newest histology methods; `imaging-ehjdh-2026` (abnormal ejection fraction from CT) and `imaging-nature-2026` (ECG deep-learning biomarker) offer *cross-modal* anomaly/biomarker-discovery paradigms — transferable methods, cardiac modality.

### ② 虚拟组织建模 / Virtual-tissue modelling
<!-- ZH --> 把组织建成可干预的生成模型。`virtual-tissue-2501`(VirTues)是"虚拟组织"概念的核心论文;`spatial-biorxiv-2025`(MintFlow)不仅建模,还能*重编程*组织微环境,直接连向第③环;`hest1k-2024` 提供把组织学图像与空间转录组配对的大规模数据集,是①②两环共同的数据底座。
<!-- EN --> Model tissue as an interventionable generative model. `virtual-tissue-2501` (VirTues) is the core "virtual tissue" paper; `spatial-biorxiv-2025` (MintFlow) not only models but *reprograms* the tissue microenvironment, linking straight to stage ③; `hest1k-2024` provides a large paired histology↔spatial-transcriptomics dataset — the shared data substrate for stages ① and ②.

### ③ 逆转:基因/扰动预测 / Revert via gene & perturbation prediction
<!-- ZH --> 求解反问题:施加什么扰动能把异常态推回正常。`scrna-natmachintell-2026`(Conditional Monge Gap)做可泛化的单细胞扰动建模,正是"逆转异常"所需的反问题工具;`spatial-biorxiv-2025` 的重编程能力在空间尺度上呼应同一目标;`virtual-cell-challenge` 是这一环的公开基准/竞赛,可评测我们的扰动预测模型。
<!-- EN --> Solve the inverse problem: which perturbation pushes an anomalous state back to normal. `scrna-natmachintell-2026` (Conditional Monge Gap) does generalizable single-cell perturbation modelling — exactly the inverse-problem tool for reverting anomalies; `spatial-biorxiv-2025`'s reprogramming echoes the goal at spatial scale; `virtual-cell-challenge` is the public benchmark for such perturbation-prediction models.

### ④ 基础模型与病理应用 / Foundation backbones & pathology applications
<!-- ZH --> 横跨全流程。`virchow-2024`、`uni2-h-model`、`fm-arxiv-2604` 是组织病理基础模型,作为①的特征提取器与②的表征骨干被反复复用;`pathomics-npjpo-2026`、`pathomics-blood-2023`、`pathomics-repo` 展示 pathomics(影像+组学)在预后/疗效预测上的落地,示范"图像→分子→临床"的多模态链路。
<!-- EN --> Cross-cutting. `virchow-2024`, `uni2-h-model`, `fm-arxiv-2604` are pathology foundation models reused as feature extractors (stage ①) and representation backbones (stage ②); `pathomics-npjpo-2026`, `pathomics-blood-2023`, `pathomics-repo` show pathomics (image+omics) applied to prognosis/treatment-response, exemplifying the image→molecule→clinic chain.

<!-- ZH --> **关键跨链接:** 基础模型(④)为异常检测(①)与虚拟组织(②)提供 embedding;HEST-1k(②数据)桥接组织学与空间转录组;MintFlow(②)与 Monge-Gap(③)在"逆转/重编程"目标上汇合;竞赛(③)提供统一评测。
<!-- EN --> **Key cross-links:** foundation models (④) supply embeddings to anomaly detection (①) and virtual tissues (②); HEST-1k (② data) bridges histology and spatial transcriptomics; MintFlow (②) and Monge-Gap (③) converge on the revert/reprogram goal; the challenge (③) provides a common benchmark.
