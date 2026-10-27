# Precise identification of cell states altered in disease using healthy single-cell references

> **文献键** `Dann_2023` · **来源** Nature Genetics(2023) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41588-023-01523-7> · `status: complete`

---

## 一句话
用「健康参照」找疾病改变的细胞状态时,参照该怎么选?作者给出系统答案:**用大规模健康 atlas 学 latent space(scVI + scArches 映射),再只拿匹配的 control 样本做差异丰度检验(Milo)**——即 ACR(atlas-to-control reference)设计;它比只用 atlas(假阳性暴涨)或只用 control(漏掉多种异常状态)都更准,且有 atlas 时可以少采 control 而不增加 FDR。

## 研究问题
标准流程是:把疾病与健康数据整合进同一 latent space,再在匹配的细胞状态上做差异分析。参照数据的选择很关键但缺乏证据:Human Cell Atlas 级别的 atlas 覆盖面广、细胞状态全,但人群与实验协议与疾病队列不匹配,可能引入混杂造成假阳性;而匹配的 control 样本难采、量少,用于整合时会漏掉稀有状态、过度解读样本噪音。问题是:atlas 能否替代 control?两者如何组合?

## 方法
三步流程:(1) 在「embedding 参照」上训练降维模型(scVI,5,000 HVG,n_latent=30);(2) 用 scArches 把 query(含疾病样本)迁移映射到同一 latent space;(3) 用 Milo 在 kNN 邻域层面做差异丰度(DA)检验(10% spatial FDR)。对比三种参照设计:**AR**(atlas 既做 embedding 又做 DA 参照)、**CR**(control 两步都做;又分 query mapping 的 CR scArches 与 control+disease 拼接联合训练的 CR scVI)、**ACR**(atlas 做 embedding、control 做 DA)。用 **out-of-reference (OOR)** 模拟构建 ground truth:从 13 个研究、1,248 个供者的健康 PBMC 中取一个研究随机拆成伪疾病(16 供者)与 control(13 供者),其余 12 个研究(1,219 供者,513,565 细胞)作为 atlas;把某一细胞类型从 control 与 atlas 中删除,使其成为疾病特有的 OOR 状态。还模拟了「多个 OOR 状态」(固定删除经典单核细胞 + 一个按 PCA 拆半的 shifted OOR 状态)。另外比较了 latent 距离、label-transfer 不确定性等替代判据(Supplementary Note 2.1)。

## 数据
模拟:CELLxGENE 上 13 个健康 PBMC 10x 研究,下采样到每样本 500 细胞,共约 59.7 万高质量细胞、16 种细胞类型(atlas 513,565 / control 5,671 / 伪疾病 7,505 细胞),测试 15 种 OOR 状态。真实数据一:COVID-19 PBMC 队列(90 名患者、23 名健康志愿者;疾病 48,083、control 14,426 细胞)+ 12 研究 1,219 人的 PBMC atlas。真实数据二:特发性肺纤维化(IPF)肺实质 scRNA-seq(32 名 IPF、28 名 control、18 名 COPD;IPF 144,404、control 95,303 细胞)+ 核心 Human Lung Cell Atlas(HLCA,584,844 细胞)。

## 主要结果
- **单一 OOR 状态**:ACR 灵敏检测高 OOR 比例邻域;AR 假阳性大量膨胀(OOR 比例为 0 的邻域也被判显著);CR scArches 的 FDR 高于 ACR;CR scVI 与 ACR 相当。各设计的整合质量差异很小;改用其他 DA 方法结论一致;任何方法都需要每种细胞类型约 ≥250 个细胞才能检出 OOR。
- **CR scVI 的好表现来自特征选择**:在 control+disease 上选 HVG 会把 OOR 标记基因选进来;控制 HVG 来源后只有 CR scVI 明显掉点(control+disease 的 HVG 与仅 control 的平均重叠 81%,与仅 atlas 的重叠 68%)。在**多个 OOR 状态**的模拟里 ACR 最好。
- **稳健性**:control 队列变小时 ACR 始终优于 CR(AUPRC 分布 t 检验 P < 0.01);atlas 至少约 10,000 个细胞时 ACR 灵敏度稳定;无 control 时性能更依赖 atlas 规模(AUPRC 与规模相关 R² = 0.69 对 AR,0.4 对 ACR),且 atlas 变小时 AR 的 FPR 上升。
- **COVID-19**:DA logFC 与 IFN 签名均值的相关性 ACR 更强(Pearson R 0.63 对 CR 0.52,Fisher z P < 2.2×10⁻¹⁶);区分出 CD14⁺ 单核细胞的 IFNhi 与 IFNlo 两种 COVID 相关状态:IFNhi 在轻症/无症状最突出(相比健康 Wilcoxon P = 1.19×10⁻⁷),IFNlo(HLA-DRlo S100Ahi 功能失调单核细胞)在中重症占优;CR 设计无法区分正常 IFNlo 与重症 IFNlo。
- **IPF**:ACR 在检出促纤维化 SPP1⁺ 巨噬细胞和诊断签名阳性的基质/上皮状态上均优于 AR/CR;CR 错误地优先选出样本数显著更少的邻域(残留 batch effect)。ACR 在肺实质中区分出 KRT5⁺KRT17hi 异常 basal 细胞与 KRT5⁻KRT17⁺ basaloid 细胞两种不同异常状态,鉴定 981 个差异基因(FDR 5%),部分是在研药物靶点(如 CSF2、CCL2)。

## 创新点
- 把「健康参照怎么用」拆成 embedding 参照与 DA 参照两个独立选择,并给出明确的 ACR 推荐。
- 基于真实数据切分的 OOR 模拟框架,保留真实供者/文库效应,可作为「疾病状态检测」的 ground-truth 基准。
- 量化 atlas 规模、control 数量、HVG 选择对假阳性的影响,给出队列设计指南(有 atlas 时可减少 control)。
- 倡导 atlas 构建者共享训练好的 embedding 模型以便 scArches 映射。

## 局限
- 依赖两条假设:control 中的所有状态在 atlas 中都存在;疾病只改变部分细胞类型。
- 模拟的 OOR 是「删除细胞类型」或「拆半」,比真实的连续性疾病漂移更离散;检出需约 ≥250 细胞,稀有状态受限。
- 仅 scRNA-seq、仅 PBMC 与肺;不涉及空间、多模态或 ATAC。
- 仍需匹配 control;完全没有 control 时的替代方案只在补充材料中讨论。

## 与本研究方向的关系
这是 detect 阶段的**方法学基石**:我们把「疾病改变的细胞状态」当作异常,而本文告诉我们异常检测的「正常」该如何定义——**atlas 定义坐标系,匹配 control 定义统计零假设**。对 **课题 1**(肾脏组学异常检测)直接可用:用 KPMP / Lake 肾脏 atlas / HuBMAP 做 embedding 参照,把待测肾样本的 snRNA 映射进去,再用 KPMP 等来源的匹配健康样本(如肿瘤肾切除旁正常组织)做 DA 对照;本文的 OOR 模拟(从健康数据里删掉一类细胞)也可以直接改造成 **KidneyAnomalyBench** 的合成 ground-truth 部分,与专家标注互补。本文也解释了一种重要失败模式——「AR 设计下批次/协议差异被误判为疾病」——这正是课题 1 需要用**跨模态一致性**(snRNA vs snATAC vs Xenium)去区分 artifact 与疾病的原因:单模态的 DA 显著性不足以定罪。对 **课题 2**(可信生物医学 agent),本文给出了一个可执行的「声明→证据」核查规则:当 agent 声称「发现某疾病特异细胞状态」时,verifier 应检查其参照设计(是否有匹配 control?HVG 是否在疾病数据上选择?邻域样本数是否异常少?),这些都可以写进 omics-specific failure taxonomy。

## 可复用资产
- **复现代码**(OOR 设计基准):
<https://github.com/MarioniLab/oor_design_reproducibility>
- **milopy**(Python 版 Milo 差异丰度):
<https://github.com/emdann/milopy>
- **数据**:Zenodo 上的处理后 PBMC 数据;HLCA 复现仓库。
<https://zenodo.org/record/6337966> · <https://github.com/LungCellAtlas/HLCA_reproducibility>
- **协议**:scVI(5,000 HVG)+ scArches 映射 + Milo DA(10% spatial FDR)+ AUPRC/FDR/TPR 评价。

## 待读
- MapQC(本仓库 `refmap-eval-biorxiv-2025`):在 ACR 设计之上自动判断映射是否成功,是本文的直接延续。
- MrVI(`mrvi-natmethods-2025`):无需聚类的样本级 DA/DE,可与 Milo 对比。
- 补充材料 Note 2.1 / 2.3:无 control 时的替代判据(latent 距离、label-transfer 不确定性)。
- 在肾脏数据(Lake atlas + KPMP)上复现 ACR vs CR。

## 引用
```bibtex
@article{Dann_2023, title={Precise identification of cell states altered in disease using healthy single-cell references}, volume={55}, ISSN={1546-1718}, url={http://dx.doi.org/10.1038/s41588-023-01523-7}, DOI={10.1038/s41588-023-01523-7}, number={11}, journal={Nature Genetics}, publisher={Springer Science and Business Media LLC}, author={Dann, Emma and Cujba, Ana-Maria and Oliver, Amanda J. and Meyer, Kerstin B. and Teichmann, Sarah A. and Marioni, John C.}, year={2023}, month=Oct, pages={1998–2008} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
