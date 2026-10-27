# Anomaly detection in spatial transcriptomics via spatially localized density comparison

> **文献键** `Hu_2025` · **来源** Bioinformatics(2025) · **类别** spatial · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1093/bioinformatics/btaf242> · `status: complete`

---

## 一句话
Sardine 把空间转录组的「条件间异常区域检测」形式化为**空间局部化差异丰度问题(SDARP)**:在对齐到同一坐标系的多条件切片上,对每个 spot 取空间邻域、在表达流形 kNN 图上用 MELD 式图平滑做密度估计,比较两条件的局部密度,得到 0.5 = 无变化、→1 = 异常的可解释 anomaly score;在模拟和两个小鼠 Visium 数据上比 MELD、Vespucci、STANDS 更准、更空间连贯。

## 研究问题
疾病、炎症、药物处理会改变组织中细胞类型/状态的组成,且这些改变往往在空间上局部化。单细胞差异丰度方法(Milo、MELD、CNA)没有空间信息;已有的空间方法——STANDS(GAN,需要组织学图像)和 Vespucci(局部窗口随机森林分类器)——依赖启发式打分。经典空间扫描统计(Kulldorff)又只适用于点过程,不适配高维稀疏的 ST 数据。

## 方法
**问题形式化**:每个 spot 的 (表达 x, 位置 s) 来自各条件的联合密度;假设两条件**空间配准**(空间边缘分布相同),则后验 P(Z=1|x,s) 只依赖条件化的表达密度 f₀(x|s)、f₁(x|s)。由于每个位置只有一两个点,改为在空间区域 R 上条件化:f_k(x|R)。**两个组件**:(i) **spatial anomaly family**——对每个 spot i 取两条件各自最近的 r 个 spot 组成 Rᵢ(两条件样本数相等);(ii) **plug-in 密度估计**——在全部条件表达数据的 kNN 图上,把均匀概率质量放在 Rᵢ 内该条件的点上,用 Laplacian 正则化平滑(沿用 MELD,参数 α、β)得到 f̃₀(x|Rᵢ)、f̃₁(x|Rᵢ)。归一化得相对似然 Q̃,**anomaly score = Rᵢ 内扰动条件 spot 的 Q̃ 平均值**;两条件密度相近时为 0.5。可自然扩展到 >2 个条件(跨所有条件归一化)。需要先用 STalign 等把切片对齐。

## 数据
**模拟**:33×33 网格,两种空间模式(棋盘格、螺旋)× 多种表达分布(d=100 多元正态、S 曲线流形、螺旋流形);异常区内两条件采样分布不同。**真实数据**:(1) 小鼠大脑皮层刺伤前后 Visium(Koupourtidou et al. 2024,GSE226211),每条件 2 个重复,STalign 对齐;(2) 小鼠腰段脊髓损伤 + 硬膜外电刺激(EES)康复 Visium(Kathe et al. 2022,GSE184369),4 个条件、6 组两两比较,仅分析灰质。

## 主要结果
- **模拟**(超参 β=10、knn=8、窗口 r=30):Sardine 在全部 4 个设定上 MSE 最低(如 S 曲线棋盘格 0.039 对 MELD/Vespucci 0.138),ROC AUC 在 3/4 设定最高(S 曲线棋盘格 0.984 对 MELD 0.485、Vespucci 0.456;螺旋流形棋盘格 0.985 对 0.672 / 0.819);唯一例外是多元正态 + 螺旋形异常(0.810 对 MELD 0.817)。
- **运行时间**:每个模拟约 30 秒,MELD 约 1 秒,Vespucci >20 分钟。
- **小鼠皮层刺伤**:Sardine 找到的异常区沿皮层层状结构延伸并覆盖伤口;STANDS 完全漏掉伤口,反而突出海马。空间连贯性 Moran's I:Sardine 0.883、Vespucci 0.825、MELD 0.259、STANDS 0.147。与反应性星形胶质细胞、小胶质细胞标记的相关性 Sardine 最高。GSEA 显著基因集数:Sardine 650、Vespucci 26、MELD 0、STANDS 1,包括急性炎症异常(FDR 2.1×10⁻⁴)、先天免疫异常(FDR 4.2×10⁻⁵)。
- **脊髓损伤**:6 组比较中 Sardine 的 Moran's I 均最高(0.715–0.913;Vespucci 0.544–0.884;MELD ≤0.101);EESREHAB vs EESREHAB-walking 的 GSEA 显著基因集 Sardine 88、Vespucci 4、MELD 0(如突触可塑性受损 FDR 0.007)。多条件联合似然的 Moran's I 0.841–0.910。

## 创新点
- 第一次把空间 ST 异常检测严格写成「局部双样本 / 密度比较」问题(SDARP),连接了单细胞 DA 理论与空间扫描统计。
- anomaly score 有概率含义(0.5 = 无差异),跨方法、跨条件可解释,不依赖二分类器。
- 框架模块化:spatial anomaly family 与密度估计器都可替换;原生支持多条件。
- 不需要组织学图像,只需表达 + 配准坐标。

## 局限
- **必须先把不同条件的切片配准到同一坐标系**;而很多对齐方法假设表达对应关系,这在跨条件(恰恰有异常)时可能过强——作者也承认联合做对齐与异常检测可能更好。
- 真实数据没有 spot 级 ground truth,评估靠 Moran's I、标记基因相关和 GSEA 命中数等间接代理;空间连贯不等于正确。
- 只在 Visium(55 µm spot)的小鼠组织上验证;单细胞分辨率(Xenium 等)需重新调参或设计新的 anomaly family。
- 需要有「对照条件」的切片——是 case-vs-control 比较,而非对单一患者切片的无参照检测。

## 与本研究方向的关系
Sardine 是 detect 阶段**空间版的统计基线**:它与 Dann et al.(`healthy-ref-natgenet-2023`)的 Milo-DA 思路一脉相承,只是把邻域从表达空间搬到物理空间,并与 STANDS(`spatial-natcommun-2024`)、MEATRD(`meatrd-aaai-2025`)这类深度重建/判别式方法形成对照——后者需要组织学图像,Sardine 不需要。对 **课题 1**:肾脏 Xenium 数据(加上 KPMP 的空间数据)可以用 Sardine 作为 KidneyAnomalyBench 的「无图像、有概率含义」基线;它的 0.5 中性点很适合与 snRNA / snATAC 的异常分数做**跨模态一致性**比较(同一区域在多个模态都显著偏离 0.5 才算疾病,只在一个模态偏离更可能是 artifact)。但要注意肾活检的现实:不同患者活检的空间配准远比小鼠脑切片难(取材部位、皮髓质比例不同),配准误差会直接被当成异常——这是课题 1 需要专门测试的 failure mode。对 **课题 2**:本文的评估方式本身就是个警示案例——「Moran's I 高 + GSEA 命中多 = 更合理」只是间接证据,agent 若以此类代理指标声称「发现异常区域」,calibrated verifier 应当降低置信度并要求有 ground truth 的验证。

## 可复用资产
- **代码**(Python 3):
<https://github.com/raphael-group/spatial_anomaly_detection>
- **数据**:小鼠皮层刺伤 GSE226211;脊髓损伤 GSE184369。
- **评估协议**:合成流形 ST 模拟(棋盘格/螺旋 × 正态/S 曲线/螺旋流形),AUROC + 以 0.5/1 为目标的 MSE,真实数据用 Moran's I 与 GSEA。

## 待读
- Vespucci(Teo et al. 2024)与 MELD(Burkhardt et al. 2021)原文。
- Landa et al. 2020 的局部双样本检验框架(本文的统计基础,补充 S4)。
- STalign 等跨条件切片对齐方法,以及「对齐 + 异常检测联合」的后续工作。
- 在 Xenium 单细胞分辨率肾组织上测试 Sardine。

## 引用
```bibtex
@article{Hu_2025, title={Anomaly detection in spatial transcriptomics via spatially localized density comparison}, volume={41}, ISSN={1367-4811}, url={http://dx.doi.org/10.1093/bioinformatics/btaf242}, DOI={10.1093/bioinformatics/btaf242}, number={Supplement_1}, journal={Bioinformatics}, publisher={Oxford University Press (OUP)}, author={Hu, Gary and Gold, Julian and Chitra, Uthsav and Joshi, Sunay and Raphael, Benjamin J}, year={2025}, month=July, pages={i493–i501} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
