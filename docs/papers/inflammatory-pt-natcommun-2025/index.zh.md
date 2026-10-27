# Multiomic analysis of human kidney disease identifies a tractable inflammatory and pro-fibrotic tubular cell phenotype

> **文献键** `Reck_2025` · **来源** Nature Communications(2025) · **类别** single-cell · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s41467-025-59997-4> · `status: complete`

---

## 一句话
作者把 snRNA+snATAC 多组学与 CosMx 高通量单细胞空间成像(6,000 与 1,000 探针)结合,在人类肾病中找到一类 **VCAM1+ICAM1+ 炎症性近端小管(PT)细胞**:它们是 KPMP「adaptive PT」的一个亚群,表达趋化因子、促纤维化与衰老相关基因,特异地定位在纤维化 niche;表观上由 **HNF4α 网络崩溃 + AP-1/NF-κB 激活**锁定;在小鼠中用 AP-1 抑制剂 T5224 或衰老清除剂 ABT-263 能减少这类细胞并减轻炎症和纤维化。

## 研究问题
人类肾病中已描述了表达 VCAM1 的「adaptive」PT 状态,小鼠中也有 Havcr1+Vcam1+「failed repair」PT 细胞,但(1) failed repair 表型与人类肾病的关系、(2) 它在组织中的空间位置、(3) 驱动它的转录调控程序,都不清楚 —— 因此也不知道它是不是一个可干预的靶点。

## 方法
**人类图谱**:肿瘤肾切除标本的非肿瘤极,5 例输尿管梗阻(UUO,尿路上皮癌导致)vs 7 例无梗阻的肾细胞癌对照;为减少批次,把 3–5 位患者的核混成 6 个 pool 做 10x Multiome,用 SNP 反卷积分配供者(RNA 与 ATAC 文库的供者一致率 98.68%,并用 SNP 芯片验证),跨供者 SNP 还能检出普通阈值漏掉的双细胞。**投射到 KPMP**:验证聚类、确认 inflammatory 亚群在其他病因中也存在。**轨迹与跨物种**:RNA velocity + 伪时间;与小鼠 IRI、可逆 UUO(R-UUO)时间序列比较。**衰老签名**:照射诱导衰老的 RPTEC 做 bulk RNA-seq。**空间**:CosMx 6,000-plex(UUO 5 例、对照 2 例)与 1,000-plex(微小病变 3 例、IgA 肾病 6 例、慢性肾盂肾炎 4 例);25 µm 半径共定位富集、到细胞质心距离的转录本富集、niche 划分;多重免疫荧光(PanCK、VCAM1、ICAM1、FAP、CD68)验证。**调控**:配对 RNA/ATAC 构建 TF–CRE–靶基因网络、motif footprint;TNF 刺激 RPTEC 后做 JUN 与 NF-κB1 的 CUT&RUN。**干预**:小鼠单侧 IRI 后第 3 天起每日灌胃 T5224 10 mg/kg × 2 周;R-UUO 模型中给 BCL2/w/xL 抑制剂 ABT-263。

## 数据
12 位患者(平均 71 岁)的 46,957 个高质量核(59 个簇);CosMx 6,000-plex 与 1,000-plex(后者共 246,055 个细胞);小鼠 IRI 与 R-UUO 公共单细胞数据;KPMP snRNA 图谱。全部数据在 GEO:Multiome GSE254185,CosMx 6K GSE282059,CosMx 1K GSE253439,RPTEC bulk 与 CUT&RUN GSE252584/GSE254187;cellxgene 可交互浏览;Zenodo 15124887。

## 主要结果
- **状态谱系**:PT 细胞分为健康(S1–S3)、损伤(HAVCR1+VCAM1+,对应 KPMP adaptive PT)与炎症(额外表达 CCL2、CXCL1、TGM2、ICAM1 等)三态;炎症态几乎只见于梗阻肾,在 KPMP 的 adaptive PT 中也能找到 ICAM1+ 亚群。KPMP CKD 患者中,**炎症 PT 比例与活化巨噬细胞/肌成纤维细胞比例紧密相关,而总 adaptive 比例则不显著相关**。
- **「不可回头点」**:RNA velocity 提示早期损伤细胞仍可能回到健康态,而更晚期的细胞只流向炎症态;小鼠 IRI 与 R-UUO 中损伤 PT 在恢复期逐渐减少,而炎症 PT 持续存在更久;炎症 PT 的照射衰老签名评分明显更高。
- **空间定位**:CosMx 与多重 IF 均显示只有炎症 PT(VCAM1+ICAM1+)与单核细胞、单核–巨噬过渡细胞、树突细胞和肌成纤维细胞共定位于纤维化 niche,损伤 PT 则分散分布;同一小管内细胞状态很少混杂;ICAM1 位于炎症 PT 的管腔膜,可拴住尿腔中的髓系细胞。在 IgA 肾病等活检中,炎症 PT 比例与肌成纤维细胞、单核细胞、cDC 比例及纤维化严重度正相关,与 eGFR 负相关。
- **信号**:炎症 PT 是纤维化 niche 中趋化因子转录本的主要来源(如 CCL2–CCR2),并表达 PDGF、TGF、FGF 受体的多种配体;同时上调 FAS、TWEAK、TNF/TRAIL 受体,提示双向和自分泌的前馈回路。
- **调控**:下调的 PT 功能基因(CUBN、SLC34A1 等)由 HNF1α/HNF4α 主导的 TF 模块 A 控制,HNF4α 疑为主调控因子并自我调控其位点 —— 持续损伤打断这一自调控环,导致 PT 身份不可逆丢失;小鼠 IRI 中 HNF4α 靶基因 4 小时内下调,恢复的细胞 48 小时内回升,而炎症 PT 直到 6 周仍维持低水平。炎症程序由 AP-1(约 20% 可及 CRE 含其 motif)与 NF-κB1(晚期 CRE 更富集)驱动,CUT&RUN 证实 JUN 结合 CDKN1A、HDAC9、HAVCR1、VCAM1、ICAM1、PDGFA 附近的 CRE。
- **逆转**:T5224 减轻 IRI 后的肾重量下降、炎症(IBA1)与纤维化(PSR),降低 KIM1+VCAM1+ 炎症 PT 比例及 Icam1、Vcam1、Pdgfa 表达;ABT-263 在 R-UUO 中显著降低炎症 PT 基因表达,并(经 bulk 反卷积)降低炎症 PT 比例。

## 创新点
- 把小鼠「failed repair」概念落到人类肾病上,并用 ICAM1 把它从更宽泛的 adaptive/injured PT 中区分出来(人类中 VCAM1 两态共有,ICAM1 特异)。
- 在单细胞分辨率空间数据中把这一状态定位到纤维化 niche,并给出可在活检中使用的抗体面板(VCAM1/ICAM1)。
- 从「状态 → TF 程序 → 药理干预」完整走通:HNF4α 崩溃 + AP-1/NF-κB,AP-1 抑制与衰老清除在小鼠中有效。
- 混池 + SNP 反卷积的 Multiome 设计,同时降低批次并检出跨供者双细胞。

## 局限
- 人类样本来自肿瘤肾切除的非肿瘤部分,UUO 作为损伤范式;样本量小(5 vs 7),对照有轻度肾小球硬化(队列平均 71 岁)。
- 「不可回头点」主要来自 RNA velocity 与小鼠时间序列的推断,人类中无纵向证据;作者也指出需要早期活检来判断炎症态是起因还是继发于浸润白细胞。
- 干预只在小鼠中,T5224 与 ABT-263 均为全身给药,非细胞特异;ABT-263 对炎症 PT 比例的影响来自 bulk 反卷积。小鼠中 VCAM1 的特异性与人类不同。
- snRNA-seq 的细胞比例受解离偏差影响(作者自陈),CosMx 用于部分弥补。

## 与本研究方向的关系
这是本仓库里**肾脏方向最完整的 detect → model → revert 范例**:**detect** —— 在单细胞与空间数据中识别出一个疾病特异、偏离健康 PT 的状态(VCAM1+ICAM1+);**model** —— 用 TF–CRE 网络解释它为何被锁定(HNF4α 自调控环断裂 + AP-1/NF-κB);**revert** —— 用 AP-1 抑制剂与衰老清除剂在小鼠中把它拉回去,并减轻纤维化。对 **课题 1** 的具体价值:**(1) 专家可验证的正样本** —— VCAM1+ICAM1+ 炎症 PT 与纤维化 niche 是 KidneyAnomalyBench 理想的「真实疾病异常」类别,且有 IF 抗体面板作为与转录组正交的蛋白层验证(跨模态一致性);**(2) 异常应分级** —— 「可逆的损伤 PT」与「不可逆的炎症 PT」都偏离健康,但临床意义不同,基准应区分「偏离程度」与「是否可逆」;**(3) 伪影风险** —— 炎症 PT 恰好贴着巨噬细胞与肌成纤维细胞,在 Xenium/CosMx 上极易被转录本溢出污染(见 `xenium-split-natmethods-2026`、`resolvi-natmethods-2026`),所以它也是检验「去伪影会不会抹掉真异常」的最佳测试例;**(4) 数据** —— 6K 与 1K CosMx 数据(含 IgA 肾病活检)和 Multiome 全部公开,可作为外部验证集。对 **revert**:HNF4α/AP-1 给出了明确的、可在虚拟组织中模拟的扰动靶点。对 **课题 2**:本文的结论强度不一 —— 有 CUT&RUN 与小鼠干预支持的(AP-1)、只有相关性的(KPMP 比例相关)、只来自推断的(RNA velocity 的「不可回头点」)—— 很适合用来构建 claim-to-evidence 校验中「证据类型分级」的标注样例。

## 可复用资产
- **代码:** 复现图的脚本。
<https://github.com/mreck1/human_kidney_multiomics>
- **数据:** Multiome GSE254185;CosMx 6K GSE282059;CosMx 1K GSE253439;CUT&RUN GSE254187;RPTEC bulk GSE252584;cellxgene 浏览;Zenodo 15124887。
<https://cellxgene.cziscience.com/e/867757c1-3b1a-49d9-a0cd-17767eb160cc.cxg>
- **标志物面板:** VCAM1+ICAM1−(损伤)vs VCAM1+ICAM1+(炎症)PT,以及共同损伤签名 PROM1、DCDC2、SPP1、ITGB6、ITGB8。

## 待读
- KPMP / Lake 等人类肾图谱(`lake-kidney-atlas-nature-2023`)中 adaptive/maladaptive PT 的定义,对齐术语。
- 小鼠 failed-repair PT 原始工作(Kirita 等、Gerhardt 等),以及跨病因(DKD,`dkd-spatial-atlas-nature-2026`)是否存在同一状态。

## 引用
```bibtex
@article{Reck_2025, title={Multiomic analysis of human kidney disease identifies a tractable inflammatory and pro-fibrotic tubular cell phenotype}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-59997-4}, DOI={10.1038/s41467-025-59997-4}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Reck, Maximilian and Baird, David P. and Veizades, Stefan and Sutherland, Callum and Bell, Rachel M. B. and Hur, Heeyoun and Cairns, Carolynn and Janas, Piotr P. and Campbell, Ross and Nam, Andy and Yang, Wei and Schurman, Nathan and Williams, Claire and O’Sullivan, Eoin and Beniazza, Meryam and Corsinotti, Andrea and Bellamy, Christopher and Hughes, Jeremy and Laird, Alexander and Denby, Laura and Chandra, Tamir and Ferenbach, David A. and Conway, Bryan R.}, year={2025}, month=May }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
