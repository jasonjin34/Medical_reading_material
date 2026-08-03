# HEST-1k: A Dataset for Spatial Transcriptomics and Histology Image Analysis

> **Bibkey** `Jaume2024_240616192` · **Venue** arXiv preprint (2024) · **Category** foundation · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2406.16192>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
HEST-1k is a large, multi-organ, cross-species dataset that aligns 1,229 spatial-transcriptomics (ST) profiles with paired H&E whole-slide images (WSIs) and rich metadata, shipped with the HEST-Library toolkit and HEST-Benchmark for training/evaluating pathology foundation models on morphology-to-expression prediction.

## 研究问题 / Problem
Spatial transcriptomics reads molecular tissue composition at growing resolution, but cost, fast-evolving technology, and missing standards have confined ST computational methods to small cohorts and narrow tasks. Meanwhile the morphology encoded in H&E WSIs — strongly linked to expression — is routinely overlooked. There was no unified, standardized, large-scale paired morphology–expression resource to benchmark pathology foundation models beyond diagnosis.

## 方法 / Method
(1) Unification pipeline: HEST-Library (on Scanpy/AnnData) converts heterogeneous image formats into OpenSlide-compatible pyramidal TIFF; YOLOv8 detects Visium fiducials for auto-alignment; pixel resolution is inferred from inter-spot spacing; expression matrices (CSV/MEX/TXT/h5) are unified to AnnData; a fine-tuned DeepLabV3 (ResNet50) segments tissue; 224×224 patches at 20× are cropped around each spot. (2) Benchmark protocol: from each 112×112 μm H&E patch, a frozen foundation model extracts features fed to Random Forest (70 trees) / Ridge regression predicting the top-50 highly variable genes, under patient-stratified k-fold CV, scored by Pearson correlation. (3) Multimodal alignment: CONCH's last 3 ViT layers are fine-tuned with an InfoNCE contrastive loss.

## 数据 / Data
HEST-1k (latest version) contains 1,229 ST profiles, each paired with one WSI and metadata; assembled from 153 public+internal cohorts spanning 26 organs, two species (human, mouse), 367 cancer samples across 25 cancer types; yielding ~2.1M expression–morphology pairs and >76M nuclei. ST technologies include Visium/Visium HD, Xenium (subcellular), and original Spatial Transcriptomics; both frozen and FFPE tissue at 10×/20×/40×. Sources include 10x Genomics, NCBI, Mendeley, Spatial-Research, Zenodo, and internal cohorts. (Note: the fetched v1 HTML reports earlier figures — 1,108 samples / 131 cohorts / 25 organs / 320 cancer samples / 1.5M pairs / ~60M nuclei / 825 GB; the experimental details below are quoted from v1.)

## 主要结果 / Key results
**HEST-Benchmark** (10 gene-expression prediction tasks over 9 human cancer types / 10 organs, 10 foundation models): top mean Pearson correlation is UNI 0.319, then GigaPath 0.316, CONCH 0.315, Remedis 0.315, CTransPath 0.295. Per-task range spans HCC 0.034 to SKCM (UNI) 0.613. Findings: student-teacher self-supervised pretraining beats supervised; CONCH (ViT-Base, 86M) gains ~5% absolute over second-best under Ridge and matches ViT-Giant GigaPath (1.13B) at ~13× fewer parameters. **Biomarker exploration**: on IDC Xenium, neoplastic nuclear area correlates with GATA3 at R=0.47 (FLNB R=0.49, TPD52 R=0.49, FOXA1 R=0.47); size features correlate most, shape/topology weakly (R<0.2). **Multimodal learning**: fine-tuning CONCH on 5 Xenium IDC cases (47,051 pairs, 238 genes), then predicting ER/PR/HER2 on BCNB (n=1,058 WSIs): ER AUC 0.881→0.884, PR AUC 0.810→0.818, HER2 AUC 0.715→0.724 — most metrics improve.

## 创新点 / Contributions
- The largest, most diverse paired ST+H&E WSI dataset to date (26 organs / 2 species / 25 cancer types) with ~2.1M morphology–expression pairs and >76M nuclei.
- HEST-Library: an open-source toolkit that unifies heterogeneous raw ST data into AnnData + pyramidal TIFF + spot-aligned patches end-to-end.
- HEST-Benchmark: the first multi-task benchmark systematically evaluating pathology foundation models on morphology-to-expression prediction.

## 局限 / Limitations
- ST data is inherently noisy (staining/compression artifacts), affecting label quality.
- Batch effects across samples/datasets/technologies are not quantified.
- Some tasks have tiny cohorts (HCC 2 patients, PAAD 3), and some cancers show very low morphology–expression correlation (HCC 0.034).
- HEST-Library cannot cover all legacy formats; data is research-only (diagnostic use prohibited).

## 与本研究方向的关系 / Relation to our direction
This is a **foundational data substrate and direct raw material for the "virtual tissue" stage** of our pipeline. For virtual-tissue modelling: HEST-1k supplies spatially aligned (H&E patch ↔ gene expression) pairs — exactly the training data to model tissue as a spatial map of predictable molecular state; HEST-Benchmark's morphology-to-expression task is isomorphic to our "infer molecular state from image" goal, and its eval protocol is directly reusable. For anomaly detection: because spot-level expression ground truth exists, one can contrast morphology–expression deviations between normal and tumor regions to construct spatial "expression-anomaly" labels. For gene-revert: it provides quantitative morphology–gene links across many tissue types (e.g. nuclear area ↔ GATA3/FOXA1) as a prior and validation set for "which genes drive a morphological state," though it contains no perturbation/reversion interventions and must be paired with perturbation data (e.g. Perturb-seq). Overall it sits at the data/representation layer, not the algorithm layer.

## 可复用资产 / Reusable assets
- **数据集 / Dataset:** HEST-1k on HuggingFace Datasets (`MahmoodLab/hest`); 1,229 ST+WSI profiles, 直接下载或按癌型/器官/技术过滤子集 filter subsets by cancer type/organ/technology.
- **代码 / Code:** HEST-Library — <https://github.com/mahmoodlab/hest> (Scanpy/AnnData-based; format unification, YOLOv8 fiducial alignment, DeepLabV3 tissue segmentation, spot-aligned 224×224 @20× patching, batch download).
- **评测协议 / Eval protocol:** HEST-Benchmark — 10 tasks, top-50 HVG expression prediction from 112×112 μm patches, patient-stratified k-fold CV, Pearson correlation, RF(70 trees)/Ridge readouts.
- **可比较的基础模型 / Foundation models scored:** UNI, CONCH, GigaPath, Phikon, PLIP, CTransPath, Remedis, Ciga, KimiaNet, ResNet50-IN — 现成 baselines 与相对强弱。
- **License:** CC BY-NC-SA 4.0 (non-commercial, research-only).

## 待读 / Follow-ups
- UNI 与 CONCH 原论文(pathology foundation models,基准中的最强项)。 UNI and CONCH source papers (strongest models in the benchmark).
- 后续 HEST-1k 版本 / arXiv v2+ 以确认 1,229 vs 1,108 等最终数字与新增任务。 Later HEST-1k / arXiv versions to confirm final figures (1,229 vs 1,108) and any added tasks.
- 结合扰动数据(Perturb-seq / drug-perturbation ST)以支撑 gene-revert 阶段。 Pair with perturbation data (Perturb-seq / drug-perturbation ST) for the gene-revert stage.
- CellViT 核分割 + BCNB ER/PR/HER2 下游评测的复现细节。 Reproduction details of CellViT nuclear segmentation and BCNB ER/PR/HER2 downstream eval.

## 引用 / Cite
```bibtex
@misc{Jaume2024_240616192,
  title = {HEST-1k: A Dataset for Spatial Transcriptomics and Histology Image Analysis},
  author = {Guillaume Jaume and Paul Doucet and Andrew H. Song and Ming Y. Lu and Cristina Almagro-Pérez and Sophia J. Wagner and Anurag J. Vaidya and Richard J. Chen and Drew F. K. Williamson and Ahrong Kim and Faisal Mahmood},
  year = {2024},
  eprint = {2406.16192},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2406.16192}
}
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
