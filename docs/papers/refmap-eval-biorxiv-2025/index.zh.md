# Automated evaluation of single-cell reference atlas mappings enables the identification of disease-associated cell states

> **文献键** `Sikkema_2025` · **来源** bioRxiv(2025) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1101/2025.05.23.655749> · `status: complete`

---

## 一句话
MapQC(Theis 组)用健康参照 atlas 自身的**样本间差异作为零分布**,来判断一次 query→reference 映射是否成功:query 的 control 样本应与参照「正常地远」(mapQC 分数 < 2),case 样本应在部分细胞中「异常地远」(> 2)。它能检出 UMAP 看不出来的残留 batch effect,防止把 artifact 报告成疾病状态,而且比重新拿来用的整合指标(LISI、kBET 等)更可解释。

## 研究问题
把疾病/扰动的 query 数据映射到健康参照 atlas(scArches、Symphony、Azimuth 等)已是标准做法,但映射成败事先无法预测(受解离协议、测序平台、映射参数影响)。失败有两种:**欠整合**(残留 batch effect,artifact 被当成疾病状态)与**过整合**(疾病信号被抹掉)。现有指标要么只看 query 结构是否被保留(恰恰与映射目的冲突),要么是 LISI、kBET 之类的整合指标,没有绝对阈值,而且都忽略了**健康人群本身就有样本间差异**这一事实。

## 方法
两条假设:(A1) 健康参照 atlas 覆盖健康人群的大部分变异;(A2) 疾病至少在部分细胞类型上与健康不同。推出两条可检验的假设:(H1) query control 与参照样本的相似度应等同于参照样本彼此的相似度;(H2) case 样本在某些细胞类型上应比这更不相似。**计算**:在整合后的 embedding 中随机选中心细胞、取大邻域;在每个邻域内,用 **energy distance(E-distance)** 计算样本间距离;样本到参照的距离 = 到所有参照样本距离的均值(参照样本自身计算时排除同一数据集的样本,避免组内偏小);以该邻域内参照样本自身的距离分布为零分布做 **Z-score**(剔除 3.5×IQR 外的离群值);细胞的 mapQC 分数 = 其样本在该细胞所属全部邻域的归一化距离均值。**判读**:> 2 视为远离参照(残留 batch 或参照外的生物状态)。成功映射 = control 大多 < 2 且 case 有部分细胞 > 2;control 也 > 2 → 欠整合;case 与 control 一样近 → 过整合。作者试过 Wasserstein 距离(单次映射 >48 小时,不可行)和平均成对距离(受方差影响),最后选 E-distance。

## 数据
(1) IPF 数据集(5 名 IPF 患者、6 名 control)映射到 Human Lung Cell Atlas(HLCA);(2) Asherman 综合征(AS)子宫内膜数据(6 名健康、9 名 AS 供者)映射到 Human Endometrial Cell Atlas(HECA)。映射工具为 scArches。

## 主要结果
- **IPF → HLCA(默认映射)**:很多 query control 细胞 mapQC > 2,说明残留 batch effect,而 UMAP 上(如血管内皮)看不出来。对内皮细胞做常规聚类会得到一个「疾病特异」簇,但其差异基因主要是实验 artifact:环境 RNA(B 细胞来源的 IGKC、IGHA1)、解离应激(FOSB)、核糖体蛋白(RPS4Y1)。
- **AS → HECA**:93.9% 的 query control 细胞 < 2;但两个以 query 为主的簇(94% 与 97% 来自 query)持续 > 2,其中簇 21 含原论文 74% 的「AS 上皮」细胞。进一步分析显示这些是低质量细胞(总 counts 低、无特异标记、簇 25 MALAT1 低、疾病细胞呈基质 + 上皮双系表达像 doublet)——即**原论文报告的疾病特异状态很可能是低质量细胞/doublet artifact**。
- **改进映射**:query control 中 mapQC > 2 的比例:原始映射 28.4%;max KL weight 改为 2 → 100%、改为 0.1 → 49.1%(都更差);batch 协变量从 dataset 改成 sample → 17.1%;再找回 69 个因基因注释统一而丢失的输入基因 → 9.3%。此时 IPF 细胞 > 2 的比例为 23.7%(对 control 9.3%)。
- **成功映射下的疾病状态**:平滑肌细胞 IPF 26% 对 control 2% 高分,特异基因(IGFBP2、FAM162B、CCL21 等)在其他 IPF 数据集中复现;SPP1hi 肺泡巨噬细胞被正确识别为疾病特异(UMAP 上看不出);原论文报告的 CTHRC1hi 成纤维细胞则接近参照——7 名参照健康供者的 CTHRC1 均值 ≥ IPF 供者,说明更大的健康对照群体能纠正误报。
- **对比现有指标**:cluster preservation、wiq-kNN-corr、donor LISI 在最好和最差映射上几乎无差别(最差映射中 query control 在 UMAP 上已完全分离,mapQC 判 100% 远离);kBET 两种映射下几乎都是最低分(过敏感);batch LISI 对 query 下采样(1%、10%)极其敏感,mapQC 基本稳定。

## 创新点
- 第一个把**健康人群自然的样本间差异**显式纳入映射质量评价的指标;有绝对、可解释的阈值(Z > 2)。
- 邻域级零分布:不同细胞类型/状态的正常变异幅度不同,局部归一化。
- 用 control 检验(欠整合)和 case 检验(过整合)两个方向同时判定映射成败;与映射方法无关、细胞级分辨率。
- 具体展示了已发表的「疾病特异状态」可能是 artifact(AS 上皮、CTHRC1hi 成纤维细胞)。

## 局限
- 需要 query 中有与 case 同协议的 control 样本。
- 假设参照覆盖了 query 人群的健康变异——只对大规模 atlas 成立;若参照只覆盖部分人群(如仅欧洲血统),会把生物学差异误判为 batch。
- 参照自身若有强 batch effect,会抬高零分布,掩盖同等强度的 query batch effect。
- 假设 query 中 control 与 case 的 batch effect 程度相同;完全混杂时任何数据驱动指标都无解。
- 只有两个案例(肺、子宫内膜),Z>2 阈值依赖近似高斯假设;预印本,未经同行评审。

## 与本研究方向的关系
这篇是 **课题 1 最关键的「artifact vs 疾病」工具之一**,也是 Dann et al.(`healthy-ref-natgenet-2023`)ACR 设计的直接延续:mapQC 本质上是一个「以健康 atlas 为零分布的样本级异常分数」,> 2 就是异常——而本文最重要的贡献是指出**这个异常可能来自 batch / 环境 RNA / 解离应激 / doublet,而不一定是疾病**,并给出 control 检验来区分。课题 1 可以直接把待测肾样本的 snRNA 映射到 Lake 肾脏 atlas / KPMP 参照,用 mapQC 检查 control(如 KPMP 参照组织或其他正常肾组织)是否正常;本文 IPF 内皮簇的 artifact 基因清单(IGKC、IGHA1、FOSB、RPS4Y1)和 AS 低质量细胞特征(低 counts、低 MALAT1、双系共表达)可以直接成为 KidneyAnomalyBench 的 **artifact 类别**与负样本标签。与跨模态一致性结合:一个 snRNA 中 mapQC > 2 的群体,如果在 snATAC / Xenium 中找不到对应异常,就更可能是 artifact。对 **课题 2**:「已发表的疾病特异状态其实是 artifact」正是 claim-to-evidence 核查要抓的东西——agent 声称发现疾病状态时,verifier 应要求 mapQC 式的 control 检验证据;mapQC 的 Z 分数也是天然可校准的置信度信号,可作为 calibrated verifier 的输入特征。

## 可复用资产
- **mapQC 软件包**:
<https://github.com/theislab/mapqc>
- **复现代码**:
<https://github.com/theislab/mapqc_reproducibility/tree/v0.1.0-manuscript>
- **判读规则**:control < 2 & case 部分 > 2 = 成功;control > 2 = 欠整合;case ≈ control = 过整合。
- **artifact 标记**:环境 RNA(IGKC、IGHA1)、解离应激(FOSB)、核糖体(RPS4Y1)、低 counts / 低 MALAT1 / 双系共表达。

## 待读
- Dann et al. 2023(`healthy-ref-natgenet-2023`)——本文引用的「有限匹配 control 能显著降低假阳性」依据。
- 环境 RNA 去污染基准(`ambient-rna-bench-biorxiv-2026`):把去污染作为映射前处理再测 mapQC。
- 在肾脏参照(Lake atlas、KPMP)上跑 mapQC,看哪些细胞类型天然整合差(类似 HLCA 中 NK/T 细胞)。
- 关注正式发表版本是否扩展到 ATAC / 空间数据。

## 引用
```bibtex
@article{Sikkema_2025, title={Automated evaluation of single-cell reference atlas mappings enables the identification of disease-associated cell states}, url={http://dx.doi.org/10.1101/2025.05.23.655749}, DOI={10.1101/2025.05.23.655749}, journal={bioRxiv}, publisher={Cold Spring Harbor Laboratory}, author={Sikkema, Lisa and Lkandushi, Mariam and Scarcella, Daniele and Moinfar, Amir Ali and Engelmann, Jan and Theis, Fabian J.}, year={2025}, month=May }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
