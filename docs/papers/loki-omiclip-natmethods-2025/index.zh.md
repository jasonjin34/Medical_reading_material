# A visual–omics foundation model to bridge histopathology with spatial transcriptomics

> **文献键** `Chen_2025_Loki` · **来源** Nature Methods(2025) · **类别** spatial · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41592-025-02707-1> · `status: complete`

---

## 一句话
OmiCLIP 把每个 Visium spot 的转录组写成「按表达量排序的基因符号句子」,与对应 H&E patch 做 CLIP/CoCa 式对比学习(ST-bank:2.2M 对、1,007 个样本、32 个器官);在此之上的 Loki 平台提供五个模块 —— 组织对齐、组织注释、细胞类型分解、图像↔转录组检索、从 H&E 预测 ST 表达。

## 研究问题
病理视觉–语言基础模型(PLIP、CONCH)用的是文字描述,缺少分子信息;而把组织学与组学结合的方法大多是任务专用的,没有一个统一的多模态模型与基础设施能同时处理测序数据与病理图像。

## 方法
**数据**:ST-bank —— 113 项研究、1,007 个 10x Visium 样本、约 2.2M 组织 patch 与配对转录组,覆盖 32 个器官,包含健康、癌症、心衰、阿尔茨海默病等状态;QC 保留高分辨率 H&E。**表示**:Ensembl ID 转基因符号、去除 housekeeping 基因,按表达从高到低排序成文本句子(借鉴 GenePT / Cell2Sentence;rank-based 思路借鉴 Geneformer / scFoundation,用以减轻批次效应)。**模型**:基于 CoCa(图像编码器 + 文本编码器 + 多模态融合解码器)微调,对比损失对齐配对的图像/转录组嵌入(768 维)。**Loki 模块**:Align(OmiCLIP 嵌入 + 改进的 coherent point drift,支持 ST↔ST、H&E↔ST);Annotate(H&E patch 与组织特异 bulk RNA-seq 或 marker 基因句子的余弦相似度;可与 PLIP 的文本相似度平均);Decompose(把 Tangram 的优化目标作用在 OmiCLIP 嵌入而非原始表达上,以 scRNA-seq 为参考,支持 ST 模式与纯图像模式,另加 NMS 风格后处理);Retrieve(用图像嵌入在 ST-bank 中检索最相似的转录组);PredEx(以查询图像与参考 ST spots 的相似度为权重,对参考表达做加权和)。多数任务默认在目标切片上微调。

## 数据
训练:ST-bank(见上)。评测:与 22 个 SOTA 方法比较,覆盖 5 个模拟数据集、19 个公开实验数据集、4 个自有数据集,包括 8 张相邻小肠切片、2 张相邻卵巢癌肉瘤切片、乳腺癌 Visium + Xenium、自有 TNBC Xenium、结直肠癌 Visium-HD、小鼠脑皮层、CRC7K / WSSS4LUAD / PatchCamelyon / LC25000、39 例正常心脏 ST 等。

## 主要结果
- **表示质量**:在 95 个有专家注释的 ST-bank 样本上,对比学习后的 Calinski–Harabasz 分数显著提升(P < 0.001);图像嵌入的聚类优于 UNI 与 GigaPath。对加噪图像与降采样测序深度(11,792 → 4,512 → 615 UMI)稳健。
- **Align**:小肠 8 切片中位 PCC 0.67–0.80(image→ST)/0.62–0.83(ST→ST),PASTE −0.25–0.39、GPSA 0.27–0.56;卵巢癌肉瘤中位 PCC 0.88/0.86,PASTE 0.26、GPSA 0.43、CAST 0.71;Xenium↔Visium 平均对齐误差 0.08 mm。从头训练只有 PCC 0.53。图像+转录组平均嵌入并不优于单模态。
- **Annotate(marker 基因零样本)**:四个病理基准上 F1 0.59–0.96,OpenAI CLIP 0.03–0.34,PLIP 0.5–0.93;Loki+PLIP 平均相似度在四个数据集上都最好(CRC7K 召回率 93%)。
- **Decompose**:TNBC Xenium 基准上 ST 模式与图像模式综合分 1.32/1.11 排前二,Tangram、CARD、Cell2location、RCTD 等 0.87 至 −1.82;把嵌入换成 scGPT / scFoundation / Geneformer 分别排第 6/8/9。
- **Retrieve**:肾验证样本 Recall@5% 0.173、Recall@10% 0.297(约为 CLIP/PLIP 的 3.2 倍);独立测试集 Recall@5% 0.117、@10% 0.208。
- **PredEx**:39 例正常心脏中,MSE 最优 28/39、PCC 最优 16/39(对比 Hist2ST、HisToGene、BLEEP、mclSTExp),且不需要重训。

## 创新点
- 把「转录组即文本」的思路接入 CLIP 式病理基础模型,首次用公开 ST 规模化预训练视觉–组学对齐。
- 一个共享嵌入空间支撑五类下游任务,允许用 bulk RNA-seq、scRNA-seq 乃至 marker 基因列表去解读 H&E。
- 公开 ST-bank、模型权重与代码。

## 局限
- 预训练规模(百万级)远小于通用 CLIP;罕见病况在 ST-bank 中代表性不足,对齐/分解默认需要在目标切片上微调。
- 对比式、非生成式:PredEx 本质是对参考 spots 的检索加权,无法生成真正新的表达谱。
- 只用 top-ranked 基因名,丢失绝对表达量;仅基于 Visium(spot 级,~55 μm),非单细胞分辨率。
- 部分评测(如 Retrieve)缺乏真正的转录组 ground truth,以图像相似度代理;双模态融合时一个模态主导会抵消收益。

## 与本研究方向的关系
对 detect → model → revert,OmiCLIP 提供的是**H&E 与表达共享的嵌入空间**,这对课题 1 的「跨模态一致性」最关键:同一块组织的 H&E 嵌入与转录组嵌入若在共享空间中相互「检索不到」,就是一个天然的跨模态不一致信号;反之二者都偏离健康参考才更可能是真实病变。若有配对的 H&E 与单细胞分辨率空间组学数据,可以用 Loki Align(Xenium→pseudo-Visium 的流程本文已示范)对齐,再用图像/表达嵌入各自的健康分布距离做异常打分,比较两者是否一致。Loki Annotate 的「marker 基因句子零样本标注」可直接拿肾损伤 marker(如 HAVCR1、LCN2、VCAM1)作为文本 prompt 生成弱标签,辅助 KidneyAnomalyBench 的专家标注。需要注意它在肾上只有少量验证样本(Retrieve 的 kidney Recall@10% 0.297),也不是单细胞分辨率。对课题 2,Retrieve 用「图像相似度代替转录组 ground truth」的评测方式,正是 agent 报告中易被当作证据的弱代理,是 claim-to-evidence 校验应当标记的类型。

## 可复用资产
- **代码:**
<https://github.com/GuangyuWangLab2021/Loki>
- **模型权重与 ST-bank:**
<https://huggingface.co/WangGuangyuLab/Loki>
- **评测基线**:PASTE、GPSA、CAST(对齐);Tangram、CARD、Cell2location、RCTD 等(分解);Hist2ST、HisToGene、BLEEP、mclSTExp(表达预测)。

## 待读
- HEST-1k(`hest1k-2024`)与 H&E→表达 benchmark(`he2expr-bench-natcommun-2025`),对照 PredEx 的评测口径。
- CONCH、PLIP、UNI(`uni2-h-model`)作为病理图像编码器的替代。
- GenePT / Cell2Sentence:「表达即文本」思路的来源。

## 引用
```bibtex
@article{Chen_2025_Loki, title={A visual–omics foundation model to bridge histopathology with spatial transcriptomics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02707-1}, DOI={10.1038/s41592-025-02707-1}, number={7}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Chen, Weiqing and Zhang, Pengzhi and Tran, Tu N and Xiao, Yiwei and Li, Shengyu and Shah, Vrutant V. and Cheng, Hao and Brannan, Kristopher W. and Youker, Keith and Lai, Li and Fang, Longhou and Yang, Yu and Le, Nhat-Tu and Abe, Jun-ichi and Chen, Shu-Hsia and Ma, Qin and Chen, Ken and Song, Qianqian and Cooke, John P. and Wang, Guangyu}, year={2025}, month=May, pages={1568–1582} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
