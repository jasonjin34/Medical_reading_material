# Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology

> **文献键** `Li_2025_Nephrobase` · **来源** bioRxiv(2025) · **类别** foundation · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1101/2025.09.30.679471> · `status: complete`

---

## 一句话
Susztak 组从零预训练了首个肾脏专用单细胞基础模型 Nephrobase Cell+(1B 与 500M 两个版本):约 39.5M 个细胞/核、4,319 个样本、四个物种(人、小鼠、大鼠、猪)、scRNA / snRNA / snATAC / CosMx / Xenium 多模态,约 1000 亿 token;encoder-decoder Transformer + MoE + 对抗去批次;在留出的人(KPMP 2025 Q2)与小鼠肾数据上,聚类、批次整合、跨物种对齐与「零样本」注释均优于 Geneformer、scGPT、UCE、PCA 与 autoencoder。

## 研究问题
通用单细胞基础模型大量涌现,但没有肾脏专用模型,也不清楚「器官专用」能否胜过「通用」。肾的细胞结构复杂、微环境动态,大规模单细胞 + 空间数据整合时批次效应、跨模态差异与跨物种泛化都是难点(KPMP 等图谱项目的老问题)。

## 方法
**输入/编码**:细胞×基因矩阵;每个基因由身份、归一化表达值(sum-log 归一化)及可选元数据/扰动信息组成 token,通过 cross-attention 嵌入;固定的 32,768 个直系同源基因特征空间。**架构**:encoder 自注意力、decoder 交叉注意力;RMSNorm;稀疏 top-k 路由的 Mixture-of-Experts(含 shared expert 与负载均衡损失)。**目标**:掩码生成式预训练,重建头用 ZINB 似然;分类头用 focal loss(按有效样本数做类别加权,缺失标签样本跳过);Elastic Cell Similarity 正则(防止嵌入坍缩,目标余弦相似度阈值如 0.5);监督对比损失(同标签拉近);带梯度反转层的 domain / assay 对抗判别器(assay 对抗权重随 epoch 递增)。**注意**:模型训练使用了细胞类型标签(监督对比 + 分类头),因此文中的「零样本注释」是指在留出数据上不再微调、直接用已训练的分类头,而非无监督意义上的零样本。**扰动**:随机抽 5,000 个细胞,将目标基因表达加倍,看预测的差异表达并做 GSEA。

## 数据
预训练语料:4,319 个样本、约 39.5M 个谱 —— 人 25.2M、小鼠 12.5M、大鼠 1.4M、猪 0.293M;约 30M 来自肾组织,约 10M 来自免疫/外周(含健康与 CKD 患者 PBMC);也包括胎肾与类器官。Assay 构成:scRNA ~48.7%、snRNA ~25.4%、CosMx ~7.7%、snATAC ~6.2%、Xenium ~5.5%。细胞类型以 PT(27.4%)、T 细胞(19.1%)、内皮(8.8%)为主。来源:GEO、SRA、HCA、CELLxGENE、KPMP 及大量自产数据(CosMx ~3M、Xenium ~2M、sn/sc/snATAC ~3M)。评测:留出的 KPMP 2025 Q2 人肾数据、一个小鼠发育模型数据、一个人鼠混合肾数据集。自产数据 GEO 号在 v1 中尚为占位符(***)。

## 主要结果
- **人肾(KPMP 留出)**:KMeans ARI 1B 模型 0.82(scGPT 0.40、autoencoder 0.55、Geneformer 0.22),NMI 0.78(scGPT 0.48),silhouette ~0.68;cLISI 1.00,iLISI ~0.17–0.18,kBET 0.25–0.28(scGPT 0.09);总整合分 0.71(1B)/0.70(500M),所有方法中最高。
- **小鼠**:ARI ~0.70,cLISI 1.0,总分 0.69–0.68,优于 UCE、PCA、scGPT。
- **跨物种**:500M 模型 NMI 0.75 / ARI 0.72(Geneformer 0.44/0.22,scGPT 0.62/0.43);1B 模型 NMI 0.73 / ARI 0.57;iLISI 0.01,graph connectivity 与 PCR ~0.94;总分 0.63(500M)/0.61(1B),Geneformer 0.50、UCE 0.51。即较小的 500M 模型在跨物种上略好。
- **注释**:人与小鼠主要谱系 >90% 正确(如 PT),误差主要在相近亚型(远曲小管 vs 连接小管)之间;与「更简单方法」的比较「未展示」。
- **in silico 扰动**:CCL2、VCAM1 加倍富集免疫黏附/趋化通路;GDF15 富集生长调控与 MAPK;SOX4 富集肾形态发生与氧化磷酸化 —— 仅为定性 GO 结果,无实验或基线验证。

## 创新点
- 第一个肾专用、跨四物种、跨五种 assay 的单细胞基础模型,规模达 1B 参数。
- 把 ZINB 重建、MoE、监督对比、ECS 与对抗去批次组合在一个 encoder-decoder 中。
- 在 KPMP 留出数据上提供了与通用基础模型的直接对比,初步回答「器官专用 vs 通用」。

## 局限
- 预印本,未同行评审;未见公开代码/权重链接,自产数据 GEO 号为占位符 —— 目前不可复现。
- **评测口径存疑**:训练用了细胞类型标签与监督对比损失,所谓「零样本」注释与聚类优势部分来自监督信号,与 Geneformer/scGPT 的无监督零样本嵌入不完全可比;文中把低 iLISI 解释为「批次分离少」、把 kBET「越低越好」,与 scib 惯例不一致,需要读者自行核对。
- 缺少 HVG + scVI/Harmony 这类强传统基线(只比了 PCA 与 autoencoder);与简单方法的注释比较「未展示」。
- 扰动实验只是「表达加倍 + GSEA」的定性展示,没有对照线性/加性基线或实验验证;作者自陈只能捕获相关性。
- 固定 32,768 基因空间;蛋白/影像等模态未纳入;训练成本高,普通实验室难以重训。

## 与本研究方向的关系
这是 Plan A 最直接的「模型层」候选:同为肾、同样覆盖 snRNA + snATAC + Xenium(+ CosMx),且语料包含 KPMP 与 CKD 样本 —— 若能拿到权重,它的嵌入是构建「健康肾流形」并在上面做异常打分的现成骨干,其对抗去批次也正对准我们多中心、多协议的批次问题。但三点必须在 Plan A 中自己验证,不能直接采信:**(1) 去批次可能「过头」** —— 对抗去 assay 信号会同时抹掉 assay 特异可见的真实状态(`kidney-multimodal-genomebiol-2026` 显示 WFDC2⁺ aTAL、Norn 只在部分协议中可见),对异常检测而言这正是要保留的信号;**(2) 监督训练会把嵌入拉向已知细胞类型**,新的/中间的疾病状态可能被吸附到最近的已知类别,从而降低异常可检出性 —— 需要用 KidneyAnomalyBench 的已知阳性状态检验;**(3) 必须补上 HVG/scVI 基线与零样本口径**(参见 `scfm-zeroshot-genomebiol-2025`)。对 revert 阶段,它的「表达加倍 + GSEA」扰动正是 `linear-baselines-natmethods-2025` 所批评的、缺乏基线的扰动 claim。对 Plan B,这篇是一个现成的 claim-to-evidence 练习对象:「远超所有现有模型」「>90% 零样本准确率」等 claim 与其证据(监督训练、缺失基线、指标解读)之间存在可被 verifier 系统性标注的落差。

## 可复用资产
- **代码/权重**:v1 全文中未找到公开链接(需关注后续版本或联系 Susztak 组)。
- **已公开的肾数据 GEO 号**(文中列出):GSE107585、GSE182256、GSE183842、GSE173343、GSE211785、GSE209821、GSE183839、GSE291551 —— 可作为 Plan A 外部数据源。
- **方法组件**:ECS 防坍缩正则、assay 对抗 + 梯度反转、ZINB 重建 —— 可单独借用。

## 待读
- 后续版本 / 正式发表版是否补充了代码、HVG/scVI 基线与真正的零样本评测。
- Susztak 组的肾空间微环境工作(文中提到的 glomerular/immune/tubular/fibrotic 四类微环境,对应本仓库 `dkd-spatial-atlas-nature-2026` 或相关条目)。
- KPMP 2025 Q2 数据发布,作为 KidneyAnomalyBench 的外部测试集候选。

## 引用
```bibtex
@article{Li_2025_Nephrobase, title={Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology}, url={http://dx.doi.org/10.1101/2025.09.30.679471}, DOI={10.1101/2025.09.30.679471}, publisher={openRxiv}, author={Li, Chenyu and Ziyadeh, Elias and Sharma, Yash and Dumoulin, Bernhard and Levinsohn, Jonathan and Ha, Eunji and Pan, Siyu and Rao, Vishwanatha and Subramaniyam, Madhav and Szegedy, Mario and Zhang, Nancy and Susztak, Katalin}, year={2025}, month=Oct }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
