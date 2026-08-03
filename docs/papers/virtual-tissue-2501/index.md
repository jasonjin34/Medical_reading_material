# AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery

> **Bibkey** `Wenckstern2025_250106039` · **Venue** arXiv preprint (2025) · **Category** virtual-tissue · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2501.06039>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner

VirTues (Virtual Tissues) is a marker-aware, multi-scale foundation model for spatial proteomics that injects protein-language-model (ESM-2) marker embeddings into image tokens and uses factorized spatial-vs-marker attention; one pretrained backbone drives marker reconstruction, cell typing, niche annotation, biomarker discovery, and patient stratification, with zero-shot transfer across heterogeneous antibody panels.

## 研究问题 / Problem

Multiplexed imaging measures dozens–hundreds of protein channels per section, but every study uses a different panel/protocol/platform, so marker count, identity, dynamic range and noise all differ. Existing pipelines are single-cohort/single-panel and cannot transfer knowledge across cohorts, cancer types or platforms, blocking robust biomarker discovery. The goal: a foundation model that ingests arbitrary marker combinations, unifies representations across scales (protein → cell → niche → tissue), and delivers clinical utility.

## 方法 / Method

Three innovations: (1) **Marker-aware tokenization** — images are cropped into a 3-D grid of image tokens (each marker at each position) fused via linear projection + addition with ESM-2 protein-LM marker embeddings; learnable patch-summary tokens aggregate (via convolution with segmentation masks) into cell/niche/tissue summary tokens. (2) **Factorized attention** — disentangled *marker attention* (channel-only, learns inter-protein dependencies) and *spatial attention* (position-only, learns tissue architecture), escaping the quadratic spatial×channel cost of standard ViTs; accuracy keeps improving with marker depth (esp. first ~20 markers) where modality-agnostic designs plateau. (3) **Masked-autoencoder pretraining** with independent (60–100% per-channel), marker (whole-channel), and niche (whole-region) masking; the decoder reconstructs channel-wise. At inference, niche summary tokens + optimal-transport (Wasserstein) power a patient-retrieval "Virtual Tissues Database". Downstream: linear probing (cell) and ABMIL (tissue).

## 数据 / Data

Trained/evaluated on **15 IMC datasets across 8 organ sites**, 147 distinct markers (proteins, PTMs, mRNAs). Scale: **3,102 patients, 8,887 tissue samples, >259k 256×256 crops, >14.5M segmented cells** (9 datasets with masks). Key cohorts: Cords et al. (lung), Wang et al. **NeoTRIP TNBC** (138 patients on atezolizumab + carboplatin + nab-paclitaxel, 67 pCR, pre/on/post timepoints), Danenberg et al. **METABRIC** breast (ER+, n=541, 21-yr follow-up), Rigamonti et al. lung (novel unseen markers for zero-shot), plus Hoch/Jackson/Meyer breast & melanoma sets. The training corpus is released as **spora**, a curated collection of 31+ spatial-proteomics datasets.

## 主要结果 / Key results

- **Reconstruction**: mean Pearson r=0.723±0.157; zero-shot known-marker r=0.667 (vs 0.797 in-domain); independent/niche masking barely degrade (Δr=0.016 / −0.002).
- **Cell typing**: +6.31% macro-F1 over KRONOS, +65.79% over CA-MAE; full-corpus vs single-dataset boosts rare immune cells (NK +95.6%, myeloid +35.2%, T +30.4%, B +27.9%); zero-shot within ≤0.03 F1 of in-domain.
- **Tissue/clinical (ABMIL)**: lung subtype 0.856, breast ER 0.806, TNBC on-treatment response 0.714 F1 (all sig. > KRONOS).
- **Survival**: METABRIC ER+ (n=541) high/low-risk split, log-rank P<0.001.
- **TNBC anti-PD-L1 (headline)**: Leiden clustering of pre-treatment cells yields 4 signatures (RS1/RS2/NRS1/NRS2); combined model **cross-val AUROC 0.817**, +4.53% over Wang et al. (P<0.001), +23–30% over immune-ratio baselines. Transferred to independent Meyer et al. TNBC cohort for disease-free survival: low-risk (n=33) 3 events vs high-risk (n=45) 21 events, log-rank P<0.005; **c-index 0.628 > Meyer (0.606)** and all tumor/immune-ratio baselines.

## 创新点 / Contributions
- **Marker-aware tokenization**:把 ESM-2 蛋白语言模型嵌入注入 image token,使模型能吃任意 marker 组合并对全新 marker 做 zero-shot(无需重训)。
- **分解式空间/marker 注意力**:突破标准 ViT 的空间×通道二次方复杂度,可扩展到高维 multiplex 数据,且注意力本身可解释。
- **多尺度层级表征**:patch→cell→niche→tissue summary token,单一 backbone 覆盖分子到临床全尺度任务。
- **可复用计算层**:同一预训练模型完成重建、cell typing、niche 注释、OT 病例检索与跨 cohort 可迁移的 biomarker 发现,建立「空间蛋白质组学基础模型」范式。

## 局限 / Limitations
- 对与训练集生化关系弱的全新 marker,重建/预测会退化;「虚拟 marker 增补」需带校准与不确定度。
- 稀有细胞状态与罕见组织结构仍难,主要受数据稀缺限制。
- 生存分析多为未校正模型;需协变量校正、比例风险检验与前瞻验证才能临床采用。
- 注意力图仅是部分解释,缺因果/扰动分析。
- 仅在 15 个 IMC cohort、8 器官上训练;跨更多疾病、组织处理协议与成像平台的普适性待验证。当前限于蛋白/RNA marker,H&E、空间转录组、代谢组等多模态融合是下一步。

## 与本研究方向的关系 / Relation to our direction

This is the **foundational core reference** for our "virtual tissues" concept and sits squarely at the middle *virtual-tissue-modelling* stage, with reusable pieces for the other two stages:

- **Virtual tissue modelling (primary hit)**: VirTues literally models tissue as a multi-scale, marker-aware, cross-panel "virtual tissue" (patch/cell/niche/tissue summary tokens). It is a direct backbone/baseline candidate for our tissue-representation layer; the spora corpus + HF checkpoints give ready-made pretrained representations.
- **Anomaly detection (upstream, adaptable)**: the MAE objective is a self-supervised "reconstruct-normal-tissue" framework — reconstruction error (or deviation under marker/niche masking) can be repurposed as an **anomaly score** for regions altered by disease/drug perturbation. The paper already shows responders exhibit larger cell-state distribution shifts than non-responders, i.e. perturbation-induced shifts are captured in VirTues space — exactly our "detect changed regions" goal.
- **Gene/target revert (downstream, indirect)**: VirTues does not predict gene perturbations, but its biomarker pipeline (cell embeddings → multi-resolution Leiden → patient-level cross-val scoring → transferable RS/NRS signatures) is a reusable template for reading off molecular programs tied to response/reversion; the PD-L1+GZMB+ / CD4+ T populations enriched in RS1/RS2 are candidate modulation targets, and marker-attention names the key proteins per niche as hypothesis generators.
- **Eval templates**: its zero-shot cross-panel protocol, OT patient retrieval, and cross-cohort signature transfer are all reusable evaluation designs for us.

## 可复用资产 / Reusable assets
- **代码**:官方仓库 `github.com/bunnelab/virtues`(MIT license)。conda 脚本建 Python 3.12 环境;`configs/base_config` 配数据/marker 嵌入路径;3 个 Jupyter notebook 演示 reconstruction / cell phenotyping / segmentation;附 `spora-bench` 基准库。
- **预训练 checkpoint(Hugging Face Hub)**:`virtues-sp32`(32 数据集,CC BY-NC 4.0)、`virtues-sp31`(31 数据集,MIT)、`virtues-imc14`(14 个 IMC 数据集,CC BY-NC 4.0)。
- **数据集**:`spora`——31+ 空间蛋白质组学数据集整理集合,含自定义数据转 spora 格式的指南与示例数据。
- **Marker 嵌入**:ESM-2 蛋白语言模型嵌入(可为新 antibody 生成 marker token)。
- **评测协议**:linear-probing 细胞分型、ABMIL 组织级预测、OT/Wasserstein 病例检索、Leiden→cross-val AUROC 的 biomarker 发现与 cross-cohort 迁移(concordance-index / log-rank 生存评估)。

## 待读 / Follow-ups
- 核对 v1 与 v2 差异:v1 报 4 数据集/96 marker/2062 病人,v2 扩到 15 数据集/147 marker/3102 病人并加入 NeoTRIP TNBC 主线——确认引用哪个版本。
- 精读 KRONOS(主要对照基线)与 CA-MAE 的差异,评估作为我们 baseline 的合适度。
- 复现 `virtues-sp31`(MIT,可商用友好)在自有 IMC/mIF 数据上的 zero-shot cell typing。
- 验证「reconstruction error 作 anomaly score」的可行性:在药物扰动配对样本上测 masking-deviation 是否与已知变化区域对齐。
- 追 ESM-2 marker 嵌入对 antibody 命名/克隆差异的鲁棒性(marker isolation 退化问题)。

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


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
