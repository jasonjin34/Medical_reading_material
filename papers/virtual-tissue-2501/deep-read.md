# AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery

> **Bibkey** `Wenckstern2025_250106039` · **Venue** arXiv preprint (2025) · **Category** virtual-tissue · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2501.06039>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH -->
VirTues 是首个面向空间蛋白质组学(spatial proteomics / multiplex imaging)的通用基础模型:用蛋白质语言模型(ESM-2)嵌入把「marker 身份」编码进 token,再用「空间注意力 / marker 注意力」分解式 Transformer,从单一预训练 backbone 同时支持 marker 重建、cell typing、niche 注释、生物标志物发现与病人分层,并能跨异质 panel 做 zero-shot。
<!-- EN -->
VirTues (Virtual Tissues) is a marker-aware, multi-scale foundation model for spatial proteomics that injects protein-language-model (ESM-2) marker embeddings into image tokens and uses factorized spatial-vs-marker attention; one pretrained backbone drives marker reconstruction, cell typing, niche annotation, biomarker discovery, and patient stratification, with zero-shot transfer across heterogeneous antibody panels.

## 研究问题 / Problem
<!-- ZH -->
Multiplex imaging(IMC、mIF 等)一次可测数十到上百个蛋白通道,但每个研究用不同的 antibody panel、协议与平台,导致 marker 数量/身份/动态范围各异;现有方法基本为单一 cohort/panel 定制,无法跨 cohort、cancer type、平台迁移知识,难以做稳健的 biomarker discovery。核心问题:如何构建一个能吃「任意 marker 组合」、跨尺度(蛋白→细胞→niche→组织)统一表征、并具临床价值的基础模型。
<!-- EN -->
Multiplexed imaging measures dozens–hundreds of protein channels per section, but every study uses a different panel/protocol/platform, so marker count, identity, dynamic range and noise all differ. Existing pipelines are single-cohort/single-panel and cannot transfer knowledge across cohorts, cancer types or platforms, blocking robust biomarker discovery. The goal: a foundation model that ingests arbitrary marker combinations, unifies representations across scales (protein → cell → niche → tissue), and delivers clinical utility.

## 方法 / Method
<!-- ZH -->
三项核心设计:(1) **Marker-aware tokenization** — 图像按 crop 切成「每个 marker × 每个位置」的 image token,与 ESM-2 蛋白语言模型嵌入通过线性投影相加融合,从而处理可变 marker 集合并注入生物先验;可学习的 patch summary token 聚合成 cell / niche / tissue summary token(细胞级通过与分割 mask 卷积聚合)。(2) **分解式注意力** — 把 Transformer 注意力拆成 *marker attention*(仅在通道间交互,学习蛋白间关系)与 *spatial attention*(仅在位置间交互,学习组织结构),避免标准 ViT 对空间×通道的二次方复杂度。(3) **Masked autoencoder 预训练** — 三种 mask 策略:independent masking(每 marker 独立随机 mask 60–100%)、marker masking(整通道 mask,测跨 marker 关系)、niche masking(整块区域所有 marker 全 mask,测全局结构);decoder 逐通道重建。推理阶段用 niche summary token + optimal transport(Wasserstein 距离)做相似病例检索。下游任务用 linear probing(细胞级)与 ABMIL(组织级)。
<!-- EN -->
Three innovations: (1) **Marker-aware tokenization** — images are cropped into a 3-D grid of image tokens (each marker at each position) fused via linear projection + addition with ESM-2 protein-LM marker embeddings; learnable patch-summary tokens aggregate (via convolution with segmentation masks) into cell/niche/tissue summary tokens. (2) **Factorized attention** — disentangled *marker attention* (channel-only, learns inter-protein dependencies) and *spatial attention* (position-only, learns tissue architecture), escaping the quadratic spatial×channel cost of standard ViTs; accuracy keeps improving with marker depth (esp. first ~20 markers) where modality-agnostic designs plateau. (3) **Masked-autoencoder pretraining** with independent (60–100% per-channel), marker (whole-channel), and niche (whole-region) masking; the decoder reconstructs channel-wise. At inference, niche summary tokens + optimal-transport (Wasserstein) power a patient-retrieval "Virtual Tissues Database". Downstream: linear probing (cell) and ABMIL (tissue).

## 数据 / Data
<!-- ZH -->
在 **15 个 imaging mass cytometry (IMC) 数据集**、覆盖 8 个器官部位上训练/评测,共测 147 个不同 marker(蛋白、蛋白修饰、mRNA)。规模:**3,102 病人、8,887 组织样本、>259,000 个 256×256 image crop、>1450 万个分割细胞**(9 个带分割 mask 的数据集)。关键 cohort:Cords et al.(肺癌,细粒度细胞类型+临床元数据)、Wang et al. **NeoTRIP TNBC**(138 三阴乳腺癌病人接受 atezolizumab+carboplatin+nab-paclitaxel,67 例达完全病理缓解;pre/on/post 治疗时间点)、Danenberg et al. **METABRIC** 乳腺癌(ER+ n=541,21 年随访)、Rigamonti et al. 肺癌(含训练外新 marker,用于 zero-shot)、Hoch/Jackson/Meyer 等乳腺与黑色素瘤数据集。训练语料在开源仓库中打包为 **spora**(31+ 空间蛋白质组学数据集的整理集合)。
<!-- EN -->
Trained/evaluated on **15 IMC datasets across 8 organ sites**, 147 distinct markers (proteins, PTMs, mRNAs). Scale: **3,102 patients, 8,887 tissue samples, >259k 256×256 crops, >14.5M segmented cells** (9 datasets with masks). Key cohorts: Cords et al. (lung), Wang et al. **NeoTRIP TNBC** (138 patients on atezolizumab + carboplatin + nab-paclitaxel, 67 pCR, pre/on/post timepoints), Danenberg et al. **METABRIC** breast (ER+, n=541, 21-yr follow-up), Rigamonti et al. lung (novel unseen markers for zero-shot), plus Hoch/Jackson/Meyer breast & melanoma sets. The training corpus is released as **spora**, a curated collection of 31+ spatial-proteomics datasets.

## 主要结果 / Key results
<!-- ZH -->
- **Marker 重建**:三种 mask 平均 Pearson r=0.723±0.157;zero-shot 到未见数据集已知 marker r=0.667(in-domain 0.797),independent/niche masking 几乎不掉(Δr=0.016 / −0.002),说明 PLM 先验支撑「虚拟 marker 增补」。
- **细胞分型**:平均 macro-F1 比 KRONOS 高 +6.31%、比 CA-MAE 高 +65.79%;全语料训练相较单数据集训练,稀有免疫群大涨(NK +95.6%、myeloid +35.2%、T +30.4%、B +27.9%);zero-shot cell typing 与 in-domain 差 ≤0.03 F1。
- **组织/临床预测(ABMIL)**:肺癌亚型 0.856 F1、乳腺 ER 状态 0.806、TNBC on-treatment 应答 0.714(全部显著优于 KRONOS)。
- **生存分层**:METABRIC ER+(n=541)按表型组成指纹聚类分高/低危,log-rank P<0.001。
- **TNBC anti-PD-L1(核心)**:从 pre-treatment 细胞经多分辨率 Leiden 聚类筛出 4 个签名(RS1/RS2/NRS1/NRS2);多变量组合 **cross-val AUROC 0.817**,优于 Wang et al. 空间预测器 +4.53%(P<0.001)、优于 immune-ratio 基线 23–30%。迁移到独立 Meyer et al. cohort 做无病生存分层:低危(n=33)3 事件 vs 高危(n=45)21 事件,log-rank P<0.005;**concordance index 0.628**,优于 Meyer 分层(0.606)与各 tumor/免疫比值基线。
<!-- EN -->
- **Reconstruction**: mean Pearson r=0.723±0.157; zero-shot known-marker r=0.667 (vs 0.797 in-domain); independent/niche masking barely degrade (Δr=0.016 / −0.002).
- **Cell typing**: +6.31% macro-F1 over KRONOS, +65.79% over CA-MAE; full-corpus vs single-dataset boosts rare immune cells (NK +95.6%, myeloid +35.2%, T +30.4%, B +27.9%); zero-shot within ≤0.03 F1 of in-domain.
- **Tissue/clinical (ABMIL)**: lung subtype 0.856, breast ER 0.806, TNBC on-treatment response 0.714 F1 (all sig. > KRONOS).
- **Survival**: METABRIC ER+ (n=541) high/low-risk split, log-rank P<0.001.
- **TNBC anti-PD-L1 (headline)**: Leiden clustering of pre-treatment cells yields 4 signatures (RS1/RS2/NRS1/NRS2); combined model **cross-val AUROC 0.817**, +4.53% over Wang et al. (P<0.001), +23–30% over immune-ratio baselines. Transferred to independent Meyer et al. TNBC cohort for disease-free survival: low-risk (n=33) 3 events vs high-risk (n=45) 21 events, log-rank P<0.005; **c-index 0.628 > Meyer (0.606)** and all tumor/immune-ratio baselines.

## 创新点 / Contributions
<!-- ZH -->
- **Marker-aware tokenization**:把 ESM-2 蛋白语言模型嵌入注入 image token,使模型能吃任意 marker 组合并对全新 marker 做 zero-shot(无需重训)。
- **分解式空间/marker 注意力**:突破标准 ViT 的空间×通道二次方复杂度,可扩展到高维 multiplex 数据,且注意力本身可解释。
- **多尺度层级表征**:patch→cell→niche→tissue summary token,单一 backbone 覆盖分子到临床全尺度任务。
- **可复用计算层**:同一预训练模型完成重建、cell typing、niche 注释、OT 病例检索与跨 cohort 可迁移的 biomarker 发现,建立「空间蛋白质组学基础模型」范式。
<!-- EN -->
- **Marker-aware tokenization**: injects ESM-2 protein-language-model embeddings into image tokens, letting the model ingest arbitrary marker combinations and perform zero-shot on entirely new markers (no retraining).
- **Factorized spatial/marker attention**: breaks the spatial×channel quadratic complexity of standard ViTs, scales to high-dimensional multiplex data, and the attention itself is interpretable.
- **Multi-scale hierarchical representation**: patch→cell→niche→tissue summary tokens; a single backbone covers the full molecular-to-clinical range of tasks.
- **Reusable computational layer**: the same pretrained model performs reconstruction, cell typing, niche annotation, OT patient retrieval, and cross-cohort-transferable biomarker discovery, establishing a "spatial-proteomics foundation model" paradigm.

## 局限 / Limitations
<!-- ZH -->
- 对与训练集生化关系弱的全新 marker,重建/预测会退化;「虚拟 marker 增补」需带校准与不确定度。
- 稀有细胞状态与罕见组织结构仍难,主要受数据稀缺限制。
- 生存分析多为未校正模型;需协变量校正、比例风险检验与前瞻验证才能临床采用。
- 注意力图仅是部分解释,缺因果/扰动分析。
- 仅在 15 个 IMC cohort、8 器官上训练;跨更多疾病、组织处理协议与成像平台的普适性待验证。当前限于蛋白/RNA marker,H&E、空间转录组、代谢组等多模态融合是下一步。
<!-- EN -->
- For entirely new markers with weak biochemical relationship to the training set, reconstruction/prediction degrades; "virtual marker imputation" needs calibration and uncertainty.
- Rare cell states and rare tissue structures remain hard, mainly limited by data scarcity.
- Survival analyses are mostly uncorrected models; covariate adjustment, proportional-hazards testing, and prospective validation are needed before clinical adoption.
- Attention maps are only a partial explanation, lacking causal/perturbation analysis.
- Trained on only 15 IMC cohorts and 8 organ sites; generalizability across more diseases, tissue-processing protocols, and imaging platforms remains to be verified. Currently limited to protein/RNA markers; multimodal fusion with H&E, spatial transcriptomics, metabolomics, etc. is the next step.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH -->
这篇是我们「virtual tissues」概念的**奠基性核心参考**,直接落在流水线中间的「virtual tissue 建模」一环,并对首尾两环都有可复用件:

- **Virtual tissue 建模(主命中)**:VirTues 正是把组织显式建模为「virtual tissue」——多尺度、marker-aware、跨 panel 统一的组织表征(patch/cell/niche/tissue summary token)。它示范了如何从异质 spatial-proteomics 学一个通用 backbone,可作为我们组织表征层的直接骨架或对照基线。其 spora 语料 + Hugging Face checkpoint 可直接拿来当预训练表征。
- **Anomaly detection(前环,可改造)**:MAE 预训练目标天然是一个「重建正常组织」的自监督框架——重建误差(或 marker/niche masking 下的偏差)可直接改造为**anomaly score**,用于检出因疾病/药物扰动而改变的区域。论文本身已展示「responder 的 cell-state 分布位移大于 non-responder」,即扰动引起的分布偏移可被 VirTues 表征捕捉,这与我们的「检测因扰动改变的区域」目标高度一致。
- **Gene/target revert(后环,间接)**:虽然 VirTues 不做基因扰动预测,但其 biomarker discovery 流程(cell 嵌入 → 多分辨率 Leiden 聚类 → 病人级 cross-val 评分 → 可迁移签名 RS/NRS)给出了「从 virtual tissue 表征反推与治疗应答/逆转相关的分子程序」的可复用范式;RS1/RS2 富集的 PD-L1+GZMB+、CD4+ T 等群体正是候选调控靶点方向。其 marker attention 还能指出每个 niche 的关键蛋白,可作为「哪些分子若被调控会改变该 niche」的假设生成器。
- **对照/评测**:其 zero-shot 跨 panel 协议、OT 病例检索、cross-cohort 签名迁移都可作为我们评测方案的模板。
<!-- EN -->
This is the **foundational core reference** for our "virtual tissues" concept and sits squarely at the middle *virtual-tissue-modelling* stage, with reusable pieces for the other two stages:

- **Virtual tissue modelling (primary hit)**: VirTues literally models tissue as a multi-scale, marker-aware, cross-panel "virtual tissue" (patch/cell/niche/tissue summary tokens). It is a direct backbone/baseline candidate for our tissue-representation layer; the spora corpus + HF checkpoints give ready-made pretrained representations.
- **Anomaly detection (upstream, adaptable)**: the MAE objective is a self-supervised "reconstruct-normal-tissue" framework — reconstruction error (or deviation under marker/niche masking) can be repurposed as an **anomaly score** for regions altered by disease/drug perturbation. The paper already shows responders exhibit larger cell-state distribution shifts than non-responders, i.e. perturbation-induced shifts are captured in VirTues space — exactly our "detect changed regions" goal.
- **Gene/target revert (downstream, indirect)**: VirTues does not predict gene perturbations, but its biomarker pipeline (cell embeddings → multi-resolution Leiden → patient-level cross-val scoring → transferable RS/NRS signatures) is a reusable template for reading off molecular programs tied to response/reversion; the PD-L1+GZMB+ / CD4+ T populations enriched in RS1/RS2 are candidate modulation targets, and marker-attention names the key proteins per niche as hypothesis generators.
- **Eval templates**: its zero-shot cross-panel protocol, OT patient retrieval, and cross-cohort signature transfer are all reusable evaluation designs for us.

## 可复用资产 / Reusable assets
<!-- ZH -->
- **代码**:官方仓库 `github.com/bunnelab/virtues`(MIT license)。conda 脚本建 Python 3.12 环境;`configs/base_config` 配数据/marker 嵌入路径;3 个 Jupyter notebook 演示 reconstruction / cell phenotyping / segmentation;附 `spora-bench` 基准库。
- **预训练 checkpoint(Hugging Face Hub)**:`virtues-sp32`(32 数据集,CC BY-NC 4.0)、`virtues-sp31`(31 数据集,MIT)、`virtues-imc14`(14 个 IMC 数据集,CC BY-NC 4.0)。
- **数据集**:`spora`——31+ 空间蛋白质组学数据集整理集合,含自定义数据转 spora 格式的指南与示例数据。
- **Marker 嵌入**:ESM-2 蛋白语言模型嵌入(可为新 antibody 生成 marker token)。
- **评测协议**:linear-probing 细胞分型、ABMIL 组织级预测、OT/Wasserstein 病例检索、Leiden→cross-val AUROC 的 biomarker 发现与 cross-cohort 迁移(concordance-index / log-rank 生存评估)。
<!-- EN -->
- **Code**: official repo `github.com/bunnelab/virtues` (MIT license). Conda script builds a Python 3.12 environment; `configs/base_config` sets data/marker-embedding paths; 3 Jupyter notebooks demo reconstruction / cell phenotyping / segmentation; ships with the `spora-bench` benchmark library.
- **Pretrained checkpoints (Hugging Face Hub)**: `virtues-sp32` (32 datasets, CC BY-NC 4.0), `virtues-sp31` (31 datasets, MIT), `virtues-imc14` (14 IMC datasets, CC BY-NC 4.0).
- **Dataset**: `spora` — a curated collection of 31+ spatial-proteomics datasets, with a guide for converting custom data to the spora format plus example data.
- **Marker embeddings**: ESM-2 protein-language-model embeddings (can generate marker tokens for new antibodies).
- **Evaluation protocols**: linear-probing cell typing, ABMIL tissue-level prediction, OT/Wasserstein patient retrieval, Leiden→cross-val AUROC biomarker discovery and cross-cohort transfer (concordance-index / log-rank survival evaluation).

## 待读 / Follow-ups
<!-- ZH -->
- 核对 v1 与 v2 差异:v1 报 4 数据集/96 marker/2062 病人,v2 扩到 15 数据集/147 marker/3102 病人并加入 NeoTRIP TNBC 主线——确认引用哪个版本。
- 精读 KRONOS(主要对照基线)与 CA-MAE 的差异,评估作为我们 baseline 的合适度。
- 复现 `virtues-sp31`(MIT,可商用友好)在自有 IMC/mIF 数据上的 zero-shot cell typing。
- 验证「reconstruction error 作 anomaly score」的可行性:在药物扰动配对样本上测 masking-deviation 是否与已知变化区域对齐。
- 追 ESM-2 marker 嵌入对 antibody 命名/克隆差异的鲁棒性(marker isolation 退化问题)。
<!-- EN -->
- Check v1 vs v2 differences: v1 reports 4 datasets / 96 markers / 2062 patients, v2 expands to 15 datasets / 147 markers / 3102 patients and adds the NeoTRIP TNBC main line — confirm which version to cite.
- Closely read the differences between KRONOS (main comparison baseline) and CA-MAE, assessing their suitability as our baseline.
- Reproduce `virtues-sp31` (MIT, commercially friendly) zero-shot cell typing on our own IMC/mIF data.
- Validate the feasibility of "reconstruction error as anomaly score": on drug-perturbation paired samples, test whether masking-deviation aligns with known changed regions.
- Track the robustness of ESM-2 marker embeddings to antibody naming/clone differences (marker isolation degradation problem).

## 图表 / Figures & tables

![VirTues platform overview and architecture](figures/fig1.png)
<!-- ZH --> **图1.** 平台总览与架构:(a) 从 multiplex 影像学到「Virtual Tissues 表征 / 数据库」两条路径,支撑临床诊断、生物学发现与信息检索;(b) 训练语料覆盖 15 数据集、8 器官部位、147 个不同 marker;(c) 规模 3,102 病人 / 8,887 样本 / ~259k crops;(d) marker-aware tokenization + 分子/细胞/niche/组织多尺度 summary token + 分解式 spatial/marker 注意力;(e) 随 marker 数增多性能持续提升(蓝线 VirTues vs 灰线 CA-MAE full-attention)。
<!-- EN --> **Fig 1.** Platform overview and architecture: (a) two paths — Virtual Tissues Representation and Database — feeding clinical diagnostics, biological discovery and information retrieval; (b) training corpus of 15 datasets, 8 organ sites, 147 distinct markers; (c) 3,102 patients / 8,887 samples / ~259k crops; (d) marker-aware tokenization plus molecular/cell/niche/tissue summary tokens and factorized spatial/marker attention; (e) scaling laws — accuracy keeps rising with marker depth (blue VirTues vs grey full-attention CA-MAE).
<!-- ZH/EN --> _Source: https://arxiv.org/html/2501.06039v2 (x1.png)  ·  License: arXiv open (code MIT, github.com/bunnelab/virtues)_

![Cell-level representation evaluation](figures/fig3.png)
<!-- ZH --> **图3.** 细胞级表征评测:(b) 跨数据集 linear-probing cell typing 的 F1,VirTues(蓝)优于 KRONOS 与 CA-MAE;(c) 全语料训练 vs 单数据集训练在稀有免疫群上的增益;(d) zero-shot(浅色)接近 in-domain(蓝);(e–g) 细胞注释向未见 cohort(Rigamonti 肺癌)的 Random-Forest 迁移。
<!-- EN --> **Fig 3.** Cell-level representation evaluation: (b) linear-probing cell-typing F1 across datasets, VirTues (blue) beating KRONOS and CA-MAE; (c) full-corpus vs single-dataset training gains on rare immune populations; (d) zero-shot (light) close to in-domain (blue); (e–g) Random-Forest transfer of cell annotations to an unseen cohort (Rigamonti lung).
<!-- ZH/EN --> _Source: https://arxiv.org/html/2501.06039v2 (x3.png)  ·  License: arXiv open_

![FM-based signatures for treatment response and survival](figures/fig5.png)
<!-- ZH --> **图5.** 治疗应答与生存的 FM 签名(核心结果):(a) NeoTRIP TNBC 队列的 pre/on/post 治疗时间线;(b) responder 在 Virtual Tissues 空间中的治疗诱导位移大于 non-responder;(c–e) Leiden 聚类得 4 个签名(RS1/RS2/NRS1/NRS2),pre-treatment 组合模型 AUROC 0.817,优于 Wang et al. 空间预测器与免疫比值基线;(h–k) 迁移到独立 Meyer et al. 队列做无病生存分层(log-rank P=3.66e-03,concordance index 0.628)。
<!-- EN --> **Fig 5.** FM-based signatures for treatment response and survival (headline): (a) pre/on/post timeline of the NeoTRIP TNBC cohort; (b) responders shift more in Virtual Tissues space than non-responders under treatment; (c–e) Leiden clustering yields 4 signatures (RS1/RS2/NRS1/NRS2), pre-treatment combined model AUROC 0.817, beating the Wang et al. spatial predictor and immune-ratio baselines; (h–k) transfer to an independent Meyer et al. cohort for disease-free-survival stratification (log-rank P=3.66e-03, concordance index 0.628).
<!-- ZH/EN --> _Source: https://arxiv.org/html/2501.06039v2 (x5.png)  ·  License: arXiv open_

### 结果表 / Results

<!-- ZH --> **表1.** 组织级 ABMIL 临床预测(macro-F1)与生物标志物 / 生存结果,VirTues vs 主要基线。
<!-- EN --> **Table 1.** Tissue-level ABMIL clinical prediction (macro-F1) and biomarker / survival results, VirTues vs main baselines.

| Task / Metric | VirTues | Baseline (KRONOS / other) | Δ |
|---|---|---|---|
| Lung cancer subtyping (macro-F1) | 0.856 | KRONOS | +8.9% |
| Breast cancer ER status (macro-F1) | 0.806 | KRONOS | +14.2% |
| TNBC treatment response (macro-F1) | 0.714 (on-treatment) / 0.676 (pre-treatment) | > KRONOS | — |
| Cell typing (macro-F1, avg rel.) | best | KRONOS / CA-MAE | +6.31% / +65.79% |
| TNBC response prediction (cross-val AUROC) | 0.817 | Wang et al. 2023 spatial predictor | +4.53% (P<0.001); +23–30% vs immune-ratio |
| Disease-free survival (concordance index) | 0.628 | Meyer et al. 2025 | +0.022 (0.606) |

<!-- ZH --> **表2.** Marker 重建 Pearson 相关(masked-autoencoder 预训练目标)。
<!-- EN --> **Table 2.** Marker-reconstruction Pearson correlation (masked-autoencoder pretraining objective).

| Setting | Pearson r |
|---|---|
| Mean over 3 masking strategies | 0.723 ± 0.157 |
| In-domain (known markers) | 0.797 |
| Zero-shot (unseen dataset, known markers) | 0.667 |
| Δr under independent masking | +0.016 |
| Δr under niche masking | −0.002 |

## 引用 / Cite
```bibtex
@misc{Wenckstern2025_250106039,
  title = {AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery},
  author = {Johann Wenckstern and Eeshaan Jain and Yexiang Cheng and Benedikt von Querfurth and Kiril Vasilev and Matteo Pariset and Phil F. Cheng and Petros Liakopoulos and Olivier Michielin and Andreas Wicki and Gabriele Gut and Charlotte Bunne},
  year = {2025},
  eprint = {2501.06039},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2501.06039}
}
```
