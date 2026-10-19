# Conformal inference for reliable single cell RNA-seq annotation

> **文献键** `L_pez_De_Castro_2025` · **来源** Bioinformatics(2025) · **类别** single-cell · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1093/bioinformatics/btaf521> · `status: complete`

---

## 一句话
用 conformal prediction 给 scRNA-seq 自动注释加上分布无关的统计保证:先用**自编码器 + conformal p 值**检测参照中不存在的细胞类型(OOD),控制假阳性率 ≤ α₀;再对剩下的细胞输出**带覆盖保证的预测集合**(标准 / classwise / cluster 三种 Mondrian 分类方式,APS / RAPS / THR 三种非一致性分数),集合大小即不确定性;conformal p 值分布偏离均匀还可以用来诊断参照与 query 之间的可交换性是否被破坏。

## 研究问题
监督式细胞注释器(scmap、CellTypist 等)通常缺乏可靠的不确定性估计;已有的「拒识」机制靠 softmax 分数阈值,而神经网络的分数常常校准不良,也没有统计保证。conformal prediction 在 i.i.d./可交换假设下能给出覆盖保证,但 query 中出现参照外的新细胞类型时假设被破坏,保证失效。此前只有一项工作把 conformal 用于单细胞注释,而且只做了标准分类方式,没处理新细胞类型。

## 方法
**归纳式 conformal**:参照集拆为训练集与校准集(校准集占可用训练样本的 40%;另留 10% 作内部测试、15% 作验证)。**模块 1:OOD 检测器**——在训练集(无离群)上训练全连接自编码器,重建误差作非一致性分数;对新细胞计算 conformal p 值(校准分数中不小于其分数的比例),在可交换时边际有效,**直接控制边际 FPR ≤ α₀**;可选用 calibration-conditional p 值(Bates et al. 2023)以概率 1−δ 保证本次校准集下 FPR ≤ α₀(功效降低);α₀ 有自动选择方法(补充 S3.1)。**模块 2:conformal 注释器**——底层分类器为 scmap、CellTypist 或前馈网络「TorchNet」,要求输出 softmax;非一致性分数用 THR、APS、RAPS(κ=1,η=0.01);对每个类别算 p 值,预测集合 = p > α 的类别;标准方式保证边际覆盖,**classwise**(Mondrian)保证每个细胞类型的条件覆盖(稀有类会不稳定),**cluster** 方式(k-means 聚合类别,Ding et al. 2023)折中。预处理:CPM + log2;TorchNet 用 Seurat 2,000 HVG + Harmony 整合。

## 数据
共 10 个批次化实验:**肺**——参照为跨组织免疫细胞 atlas(Domínguez Conde et al. 2022),query 为健康肺(GSE178360)和肺癌患者(GSE127465);**胰腺**——GSE84133 四名受试者轮流留一人作 query(4 个实验);**乳腺**——GSE180878,12 例预防性乳房切除作参照、4 例缩乳术作 query;**小鼠原肠胚**——Pijuan-Sala et al. 2019,按两个测序批次分参照/query。质控:排除 <60 个细胞的类型,过滤线粒体 >10%、核糖体 >60%、血红蛋白 >60% 的细胞。评估:leave-one-cell-type-out(从参照删除一类,保留在 query),α ∈ {0.01, 0.05, 0.1},每种配置 20 个随机种子。

## 主要结果
- **OOD 检测**:以 Naive B 细胞为 OOD(在健康肺 query 中占 1.54%、肺癌 query 中占 1.27%),在低显著性阈值下就达到高检出功效;健康 query 中满足 FPR 保证,**肺癌 query 中不满足**——因为疾病破坏了可交换性。其他细胞类型和组织趋势相似(补充图 S3–S7)。
- **FDR 偏高**:OOD 细胞越稀有,FDR 越大——可交换的 ID 细胞的 p 值服从均匀分布,必然有一部分很低,在 OOD 很少时淹没真阳性。
- **可交换性诊断**:p 值分布呈三种形态——含 OOD 时低 p 值尖峰;无 OOD 的健康 query 有小的低 p 值峰(轻微 batch / 生物差异);肺癌 query 明显偏离均匀(疾病造成的强协变量偏移)。
- **注释覆盖**:乳腺数据上 TorchNet 在三种分类方式下都接近理论覆盖;scmap 在 classwise/cluster 下好、标准方式下失败;CellTypist 达不到覆盖保证(作者推测是预处理未处理技术差异)。其他组织覆盖基本满足;健康肺(参照与 query 完全独立)略有偏差;肺癌 query 偏差最大。
- **取舍**:标准方式集合最小;classwise 保证每类覆盖但集合更大、极稀有类 CovGap 更高;cluster 折中,但在极严格覆盖要求下会给出完全无信息的集合;THR 高效但可能出现空集(= 拒识),APS/RAPS 更自适应。
- **局限案例(胰腺)**:α₀ 很低时检测器几乎不报 OOD,经验覆盖与理论差距明显;α₀ 增大后差距收窄。实验 2 中即使 OOD 检出率高,覆盖仍偏低,直到更大 α₀ 剔除了一批**违反可交换性的 ID 细胞**后才突然闭合。

## 创新点
- 用同一个 conformal 框架同时处理「新细胞类型检测」(带 FPR 保证的假设检验)和「不确定性注释」(带覆盖保证的预测集合)。
- 系统比较三种 Mondrian 分类方式 × 三种非一致性分数 × 三种底层分类器在 10 个实验上的表现。
- 把 conformal p 值的均匀性当作**可交换性 / 协变量偏移的诊断工具**。
- 预测集合支持 human-in-the-loop:单元素集合自动注释,多元素集合交给专家缩小范围。

## 局限
- 保证只在可交换性成立时有效;疾病 query(恰恰是我们最关心的)会打破它。
- OOD 稀有时 FDR 高;检出功效不足会连带破坏注释覆盖。
- 只保证边际(或按类)覆盖,不保证单个细胞;classwise 对极稀有类不稳定。
- OOD 检测器只是一个简单自编码器;α₀ 自动选择可能在找全 OOD 之前就停止。
- 只评估 scRNA-seq,底层模型种类有限;正文定量结果多在图中。

## 与本研究方向的关系
这篇给 detect 阶段带来**统计保证**这一维度。本方向里的「异常」大多是一个连续分数(重建误差、mapQC Z 值、Sardine 似然),而本文展示了如何用 conformal p 值把任意异常分数变成**有 FPR 保证的检验**——可以直接套在 MEATRD/STANDS 类重建误差、或 Plan A 自己的 snRNA/snATAC/Xenium 异常分数上,让 KidneyAnomalyBench 报告「在 α₀ = 0.05 下的 FPR/功效/FDR」,而不只是 AUROC。更重要的是本文的**负面结果**:疾病样本会破坏可交换性,p 值整体偏离均匀——这说明「异常」可能来自真正的疾病细胞,也可能来自整体协变量偏移(batch、协议),和 mapQC(`refmap-eval-biorxiv-2025`)指出的问题相同;Plan A 的跨模态一致性正好可以作为 p 值之外的第二道判据。对 **Plan B**,本文几乎就是「calibrated verifier」的单细胞原型:预测集合大小 = 不确定性,空集 = 拒识,p 值均匀性 = 分布偏移警报;verifier 核查 agent 的细胞注释声明时,可以要求以 conformal 集合而非单一标签作为证据,并在 p 值分布异常时自动降低置信度。

## 可复用资产
- **代码**(conformalized single-cell annotator):
<https://github.com/digital-medicine-research-group-UNAV/conformalized_single_cell_annotator>
- **存档**:
<https://doi.org/10.5281/zenodo.15870599>
- **评估协议**:leave-one-cell-type-out;指标 Power/FPR/FDR(检测)、覆盖率、CovGap、平均集合大小(注释);依赖 TorchCP 实现 cluster 分类方式。

## 待读
- Bates et al. 2023(conformal 离群检测与 calibration-conditional p 值)。
- Khatri & Bonn 2022(首个单细胞 conformal 注释);Sun et al. 2024(空间转录组 conformal)。
- 加权 / 协变量偏移下的 conformal 方法,用于疾病 query。
- CARA(`scatac-novel-genomeres-2026`):scATAC 侧的新细胞类型检测,可对比不确定性机制。

## 引用
```bibtex
@article{L_pez_De_Castro_2025, title={Conformal inference for reliable single cell RNA-seq annotation}, volume={41}, ISSN={1367-4811}, url={http://dx.doi.org/10.1093/bioinformatics/btaf521}, DOI={10.1093/bioinformatics/btaf521}, number={10}, journal={Bioinformatics}, publisher={Oxford University Press (OUP)}, author={López-De-Castro, Marcos and García-Galindo, Alberto and González-Gomariz, José and Armañanzas, Rubén}, editor={Mathelier, Anthony}, year={2025}, month=Sept }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
