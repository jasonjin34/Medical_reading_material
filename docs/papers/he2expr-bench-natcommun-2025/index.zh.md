# Benchmarking the translational potential of spatial gene expression prediction from histology

> **文献键** `Wang_2025_HE2Expr` · **来源** Nature Communications(2025) · **类别** histopath · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s41467-025-56618-y> · `status: complete`

---

## 一句话
对 11 个「从 H&E 预测空间基因表达(SGE)」的方法做独立复现与评测:5 个 SRT 数据集 + TCGA-BRCA 外部验证,28 个指标覆盖预测精度、泛化、临床转化(生存)、可用性与计算效率;结论是没有一个方法全面最优,全基因平均相关性普遍 < 0.25,复杂架构并不更好,且在交叉验证下生存分层基本不显著。

## 研究问题
从常规 H&E 推断空间表达若可行,将大幅放大现有病理档案的分子信息。但这些方法近 3 年才出现,几乎都只由开发者自评,评测框架各不相同(有的测 TCGA、有的做消融、有的比 backbone),缺乏统一、独立的比较,也缺少对图像质量、分辨率、转化价值的批判性评估。

## 方法
**被测方法(11 个)**:ST-Net(DenseNet121)、HisToGene(ViT + super-resolution)、DeepPT(ResNet50 + AE + MLP)、Hist2ST(ConvMixer + GraphSAGE + Transformer)、DeepSpaCE(VGG16)、GeneCodeR(非深度学习)、EGNv1(ViT + exemplar)、EGNv2(exemplar + GCN)、TCGN(CNN + ViT + GNN)、THItoGene(动态卷积 + capsule + GAT + ViT)、iStar(HViT,近单细胞超分辨)。**五类评测**:(1) 同一研究内的 SGE 预测(ST 与 Visium,4 折 CV;PCC、MI、SSIM、AUC、JS 散度、NRMSE 等,并区分全基因、HVG、SVG、高稀疏基因 HSG);(2) 跨研究泛化(ST→Visium、跨乳腺癌亚型、ST 训练模型→TCGA 图像 pseudobulk 与 bulk RNA-seq 的患者级相关);(3) 临床转化(HistoQC 图像质量对性能的依赖;用预测 pseudobulk 做 Cox 生存模型,C-index 与 log-rank,3 折 CV × 100 次重复);(4) 可用性评分(8 个方面加权,满分 31);(5) 计算效率。

## 数据
HER2+ 乳腺癌 ST(Andersson et al.)、皮肤 cSCC ST(GSE144240)、10x Visium:Visium-HER2+(Block A 两切片)、Visium-Hercep-Test2+、**Visium-Kidney(10x 健康人肾 FFPE)**;外部:TCGA-BRCA(671 张图像;HER2+ 92、luminal 463、TNBC 79 例用于生存)。

## 主要结果
- **ST 数据整体最佳 EGNv2**:PCC 0.28、MI 0.06、SSIM 0.22、AUC 0.65;所有方法的全基因平均相关 < 0.25。HVG/SVG 上相关性和 SSIM 显著高于全基因,作者主张以 HVG/SVG 为主要评测口径。预测值对「>10 vs <10 counts」的区分 AUC 0.65,对「零 vs 非零」仅 0.57;基因零比例越高相关性越低。
- **架构**:只看单 spot patch 的 CNN 类(EGNv2、ST-Net、DeepPT)聚为一类且表现最好;引入邻域/全片全局信息的方法并不更优(spot 间距 ST 150–200 μm、Visium 100 μm,邻域相关不强)。
- **健康肾 Visium**:DeepPT 最好(HVG 平均相关 0.45、SVG 0.47),其次 ST-Net(0.31/0.36)、EGNv1(0.25/0.24);作者归因于低异质性组织中单 patch 信息已足够。多种方法在 Visium 上预测几乎无空间变化(与 Visium 表达更稠密有关)。
- **泛化**:跨亚型、跨分辨率迁移普遍明显变差;ST→Visium 只有 HisToGene 有效。TCGA 患者级相关:HisToGene、EGNv2 均值 0.53、DeepSpaCE 0.52 … ST-Net 0.33。DeepPT 性能与图像质量强相关(r = 0.53),HisToGene(0.05)、Hist2ST(0.19)基本不受影响。
- **生存**:C-index 与 bulk RNA-seq 接近但都很低(如 HER2+ DeepPT 0.55 vs RNA-seq 0.58;TNBC Hist2ST 0.58 vs 0.57);在训练集上 KM 分离显著,但在 CV 下基本不显著,仅 DeepSpaCE(p = 0.028)及 Hist2ST、ST-Net 边缘显著 —— 作者结论是尚未准备好临床转化。
- **可用性**:最高 Hist2ST 18.8/31,均值 15.1(不含 DeepPT,其无公开代码仅得 2);所有方法都没有单元测试。

## 创新点
- 第一个独立、统一复现 11 个 H&E→SGE 方法的基准,28 个指标、五个维度。
- 提出「全基因平均相关」是误导性指标,应聚焦 HVG/SVG。
- 把图像质量依赖、跨分辨率泛化、CV 下生存分层纳入评测,揭示「训练集上显著」的转化结论在 CV 下消失。
- 开源 benchmark 流水线。

## 局限
- 数据以乳腺癌为主,肾只有一张健康 Visium;未涵盖 Xenium 等亚细胞分辨率平台。
- 未纳入基于病理基础模型(UNI、CONCH、OmiCLIP 等)的新一代方法;方法版本截至评测时。
- 生存分析只用 pseudobulk,不利用空间信息;可用性评分有一定主观性。

## 与本研究方向的关系
对伪影注入课题,这篇是「H&E 能在多大程度上代替/校验分子模态」的冷静基线:若想用 H&E 预测表达,再与 Xenium/snRNA 实测比较来做跨模态一致性检验,就必须先知道「预测本身有多不靠谱」—— 全基因相关 < 0.25,只有 HVG/SVG 上才有意义的信号,且对零膨胀基因几乎无能为力。这意味着 **H&E↔表达不一致的阈值必须按基因可预测性分层**,否则大量不一致只是预测噪声而非伪影或病变。好消息是:健康肾 Visium 上 DeepPT 对 HVG/SVG 的相关达 0.45–0.47,说明肾这种低异质性组织里单 patch 信息较充分,适合做「健康外观 vs 表达」的正常模型。图像质量依赖(DeepPT r = 0.53)提醒我们:H&E 质量本身就是一个需要单独建模的伪影源。对 Agent 可信度课题,「训练集上显著、CV 下不显著」的生存结论是 agent 最容易复述的过度结论,是 claim-to-evidence 校验与 rerun 稳定性测试的现成范例;「用 HVG/SVG 而非全基因评价」也可写入组学特异的评测规范。

## 可复用资产
- **Benchmark 代码**(Apache-2.0):
<https://github.com/SydneyBioX/HEtoSGEBench> · Zenodo 10.5281/zenodo.14602489
- **健康人肾 Visium FFPE**(10x 公共数据集),可作为伪影注入课题的 H&E↔表达正常参考:
<https://www.10xgenomics.com/datasets/human-kidney-11-mm-capture-area-ffpe-2-standard>
- **评测规范**:HVG/SVG/HSG 分层、HistoQC 质量依赖、CV×100 生存评估、可用性评分表。

## 待读
- HEST-1k(`hest1k-2024`)与 OmiCLIP/Loki(`loki-omiclip-natmethods-2025`):基础模型时代的 H&E→表达,看是否突破本文的 0.25 天花板。
- iStar 与 Xenium 级别的预测方法。

## 引用
```bibtex
@article{Wang_2025_HE2Expr, title={Benchmarking the translational potential of spatial gene expression prediction from histology}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-56618-y}, DOI={10.1038/s41467-025-56618-y}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Wang, Chuhan and Chan, Adam S. and Fu, Xiaohang and Ghazanfar, Shila and Kim, Jinman and Patrick, Ellis and Yang, Jean Y. H.}, year={2025}, month=Feb }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
