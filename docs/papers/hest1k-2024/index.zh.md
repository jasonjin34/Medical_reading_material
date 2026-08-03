# HEST-1k: A Dataset for Spatial Transcriptomics and Histology Image Analysis

> **文献键** `Jaume2024_240616192` · **来源** arXiv preprint(2024) · **类别** foundation · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2406.16192> · `status: complete`

---

## 一句话
HEST-1k 是一个大规模、多器官、跨物种的数据集,把 1,229 个空间转录组(ST)profile 与配对的 H&E 全切片图像(WSI)及丰富元数据对齐,并配套 HEST-Library 工具包与 HEST-Benchmark,用于训练/评测"从形态学预测基因表达"的病理基础模型。

## 研究问题
空间转录组学能以越来越高的分辨率读出组织的分子组成,但高成本、技术快速迭代、缺乏标准,使 ST 的计算方法长期局限于小队列、窄任务。同时,H&E WSI 中蕴含的组织形态信息(与基因表达高度相关)在 ST 研究中常被忽视。缺乏统一、标准化、配对形态-表达的大规模资源,阻碍了病理基础模型在诊断以外任务上的评测。

## 方法
(1) 数据统一管线:HEST-Library(基于 Scanpy/AnnData)把异构图像格式(JPG/TIFF/OME.TIF/BigTIFF)统一为兼容 OpenSlide 的金字塔 TIFF;用 YOLOv8 检测 Visium fiducial 做自动配准,用 spot 间距推断像素分辨率,把 CSV/MEX/TXT/h5 等表达格式统一为 AnnData;用微调的 DeepLabV3(ResNet50 backbone)做组织分割;围绕每个 spot 抽取 20× 下 224×224 patch。(2) 评测协议:对每个 spot 的 112×112 μm H&E patch,用基础模型提取特征,再用 Random Forest(70 树)/Ridge 回归预测 top-50 高变基因表达,做 patient-stratified k-fold 交叉验证防泄漏,以 Pearson 相关为指标。(3) 多模态对齐:用 InfoNCE 对比损失微调 CONCH 的最后 3 层 ViT。

## 数据
HEST-1k(最新版本)含 1,229 个 ST profile,每个配一张 WSI 与元数据;来自 153 个公开+内部队列,覆盖 26 个器官、两个物种(人 Homo sapiens、小鼠 Mus musculus),含 367 个癌样本、25 种癌型;识别出约 210 万对 expression–morphology 对与超 7,600 万个细胞核。ST 技术涵盖 Visium/Visium HD、Xenium(亚细胞级)与原始 Spatial Transcriptomics;组织含冷冻与 FFPE,放大倍率 10×/20×/40×。数据源包括 10x Genomics、NCBI、Mendeley、Spatial-Research、Zenodo 及内部队列。(注:被读取的 v1 HTML 报告的是较早版本数字——1,108 样本 / 131 队列 / 25 器官 / 320 癌样本 / 150 万对 / 约 6,000 万核 / 825 GB;正文实验细节引自 v1。)

## 主要结果
**HEST-Benchmark**(10 个基因表达预测任务,覆盖 9 种人类癌型/10 器官,评测 10 个基础模型):平均 Pearson 相关最高为 UNI 0.319,其次 GigaPath 0.316、CONCH 0.315、Remedis 0.315、CTransPath 0.295。单任务从 HCC 的 0.034 到 SKCM(UNI)的 0.613。结论:student-teacher 自监督预训练优于监督式;CONCH(ViT-Base, 86M)在 Ridge 回归下比次优再高约 5% 绝对值,且与 ViT-Giant 的 GigaPath(1.13B)相当,但参数量少约 13×。**生物标志物探索**:IDC Xenium 上,neoplastic 核面积与 GATA3 表达相关 R=0.47(FLNB R=0.49、TPD52 R=0.49、FOXA1 R=0.47);尺寸相关核特征关联最强,形态/拓扑特征弱(R<0.2)。**多模态表征学习**:在 5 例 Xenium IDC(47,051 对、238 基因)微调 CONCH 后,在 BCNB(n=1,058 WSI)上预测 ER/PR/HER2:ER AUC 0.881→0.884、PR AUC 0.810→0.818、HER2 AUC 0.715→0.724,多数指标提升。

## 创新点
- 迄今最大、最多样(26 器官/2 物种/25 癌型)的配对 ST+H&E WSI 数据集 HEST-1k,含 ~210 万形态-表达对与 >7,600 万核。
- HEST-Library:端到端把异构 ST 原始数据统一为 AnnData + 金字塔 TIFF + spot 对齐 patch 的开源工具包。
- HEST-Benchmark:首个系统评测病理基础模型"从形态预测基因表达"能力的多任务基准。

## 局限
- ST 数据本身含噪(染色/压缩伪影),影响标签质量。
- 未量化跨样本/数据集/技术的 batch effects。
- 部分任务样本量很小(HCC 2 例、PAAD 3 例),某些癌型形态-表达相关性极低(HCC 0.034)。
- HEST-Library 无法覆盖所有 legacy 格式;数据仅限研究用途(禁止诊断)。

## 与本研究方向的关系
这篇是我们 pipeline 的**基础数据底座与"virtual tissue"建模的直接原料**。对"virtual tissue"阶段:HEST-1k 提供了空间对齐的 (H&E patch ↔ 基因表达) 配对,正是把组织建模为可预测分子状态的空间图谱的训练数据;HEST-Benchmark 定义的"从形态预测表达"任务与我们"从图像推断分子状态"的建模目标同构,其评测协议可直接复用。对 **anomaly detection** 阶段:因数据带 spot 级表达真值,可在正常/肿瘤区域间对比形态-表达偏差,构造"表达异常"的空间标签。对 **gene-revert** 阶段:提供了大量组织类型下形态与基因的定量关联(如核面积↔GATA3/FOXA1),可作为"哪些基因驱动形态状态"的先验与验证集,但本文不涉及扰动/回复干预,需外接扰动数据(如 Perturb-seq)。总体处于数据/表征基础环,而非算法环。

## 可复用资产
- **数据集:** HEST-1k on HuggingFace Datasets (`MahmoodLab/hest`);1,229 个 ST+WSI profile,直接下载或按癌型/器官/技术过滤子集。
- **代码:** HEST-Library — <https://github.com/mahmoodlab/hest>(基于 Scanpy/AnnData;格式统一、YOLOv8 fiducial 对齐、DeepLabV3 组织分割、spot 对齐 224×224 @20× patch、批量下载)。
- **评测协议:** HEST-Benchmark — 10 个任务,从 112×112 μm patch 预测 top-50 HVG 表达,patient-stratified k-fold 交叉验证,Pearson 相关,RF(70 树)/Ridge readout。
- **可比较的基础模型:** UNI、CONCH、GigaPath、Phikon、PLIP、CTransPath、Remedis、Ciga、KimiaNet、ResNet50-IN — 现成 baseline 与相对强弱。
- **许可:** CC BY-NC-SA 4.0(非商业,仅限研究)。

## 待读
- UNI 与 CONCH 原论文(pathology foundation models,基准中的最强项)。
- 后续 HEST-1k 版本 / arXiv v2+,以确认 1,229 vs 1,108 等最终数字与新增任务。
- 结合扰动数据(Perturb-seq / drug-perturbation ST)以支撑 gene-revert 阶段。
- CellViT 核分割 + BCNB ER/PR/HER2 下游评测的复现细节。

## 引用
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

📄 **[AI-ready 全文提取 →](ai-ready.md)**
