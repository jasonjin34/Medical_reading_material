# Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup

> **文献键** `Dumoulin_2026` · **来源** Nature(2026) · **类别** spatial · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41586-026-10363-4> · `status: complete`

---

## 一句话
用 CosMx(1k 基因)与 **Xenium(5k 基因)** 单细胞空间转录组对 58 名患者的 64 个 FFPE 肾样本建图,并与 150 例 snRNA-seq 参照用 scVI/scANVI 整合成 > 500 万细胞的跨平台 DKD 空间图谱;定义 11 个可复现的组织 niche 与以细胞为中心的"microenvironment",发现随病情扩张、与 eGFR 负相关的**促纤维化损伤小管微环境**,以及其中嵌入的、**B 细胞为主的 TLS 样免疫微环境**——它标志一个进展更快的 DKD 亚群(B+ DKD,约 8.4%),并据此得到组织基因签名与 14 蛋白血浆 panel(UK Biobank 外部验证 AUC 0.70 vs KFRE 0.63)。

## 研究问题
DKD 是肾衰竭的首要病因,约 40% 糖尿病患者会发生,但临床与分子异质性极大(从快速下降到长期稳定),使治疗开发与患者选择都很难。年龄、性别、eGFR、白蛋白尿能预测结局却不揭示生物学;遗传风险分数价值有限;循环 TNFR1/2 与肾功能下降强相关,但肾内炎症的细胞与空间语境不明。作者认为,真正细胞分辨率、近全基因组的空间转录组可以把组织结构变成"可计算的"对象,直接从临床活检中揭示病理亚型。

## 方法
**数据整合**:CosMx 1k(n = 48,含 50 个自定义探针)与 Xenium 5k(n = 16,含 100 个自定义探针),两者重叠 656 个转录本;分别与 snRNA-seq 参照(150 例)用 scVI(NB 似然、4 隐层、30 维潜空间)+ scANVI 整合(scIB 基准显示 scANVI 最佳);**在潜空间里计算每个空间细胞到 10 个 snRNA 近邻的平均距离,距离过大的细胞被丢弃后重新整合**;最终 CosMx 3,386,822 + Xenium 951,041 个细胞,用 scANVI 潜空间插补 3,000 个高变基因。Leiden 聚类 + marker 注释得 20 种细胞类型,按损伤签名区分 iPT/PT、iTAL/TAL。**Niche**:在 20–80 µm 多尺度半径聚合邻域组成,机器学习得 11 个跨平台一致的 niche;用 COVET(局部基因协方差 + 近似最优传输)与 NicheCompass 做正交验证;Hotspot 做空间基因–基因相关与差异相关。**Microenvironment**:以某一细胞类型(损伤小管 iTEC、免疫细胞)为中心,按其邻域组成聚类。**下游**:CellPhoneDB v5 配体–受体并与 eGFR/HAVCR1/COL1A1 相关;843 例肾小管间质 bulk RNA-seq 验证;IMC 蛋白层面验证;与单细胞 B 细胞图谱整合;IgA 免疫沉淀质谱;TRIDENT 队列用 10 基因 B 细胞签名做 Ward 聚类分 B+/B−,Kaplan–Meier;血浆蛋白组上用 elastic-net logistic(SMOTE、5 折 CV)选蛋白,再入 Cox 模型并在 UK Biobank 外部验证。

## 数据
空间:64 个 FFPE 样本 / 58 名患者(26% 女性,平均 57.3 岁,覆盖全 GFR 范围;含健康儿童肾);CosMx 配 PAS 染色、Xenium 配 H&E 染色。snRNA-seq 参照:150 份样本、720,924 个细胞。整合后 > 500 万细胞、> 200 名患者。验证:Susztaklab Biobank 843 例 bulk RNA-seq(含病理纤维化评分)、TRIDENT 队列(n = 248,B+ 17 / B− 231;血浆蛋白组 B+ 13 / B− 182)、UK Biobank 3,309 名糖尿病参与者。

## 主要结果
- **细胞类型**:20 种,跨平台保守的损伤标记 —— iPT:SOX4、VCAM1、HAVCR1;iTAL:CLU、SLPI、ITGB6;Xenium 的更高分辨率能检出淋巴管内皮。
- **11 个 niche**:与 eGFR 的相关 —— DCT r = 0.61、PT r = 0.52(正),immune r = −0.59、iPT r = −0.55(负);DKD 中肾小球 niche 的系膜细胞与免疫细胞小幅增加(P = 0.047 / 0.029),两者相关 r = 0.32;NRG1–ERBB3 与肾功能正相关,PLAU–PLAUR、IL-6–IL-6R 在重症中富集。
- **5 种损伤小管微环境**(proximal、distal、periglomerular、perivascular、profibrotic);**促纤维化微环境**富含免疫与成纤维邻居,中心细胞为 MMP7+/HAVCR1+/HIF1A+ iPT 与 MMP7+/ANXA2+/CLU+/ITGB6+ iTAL,在 DKD 中扩张并与 eGFR 负相关(r = −0.6,P < 0.001),Sirius Red 证实胶原沉积;HBEGF–EGFR、TNFSF10–TNFRSF10B 与 HAVCR1 相关,JAG2–NOTCH2、PDGFβ–PDGFRβ 与 COL1A1 相关(843 例 bulk 验证)。
- **免疫图谱**:11 类免疫细胞;DKD 中浆细胞 3.1 倍、B 细胞 2.4 倍;健康儿童肾中多数免疫细胞位于以抗炎巨噬细胞(MRC1、CD163 等)为主的"residential"微环境,在 DKD 中比例稳定。
- **B 细胞为主的 TLS 样微环境**:嵌入促纤维化小管 niche,CXCL13–CXCR5、TNFSF13B–TNFRSF13C 共表达,CXCR5+/PDCD1+ TFH 样 CD4 T 细胞,IMC 证实 CD20+ B 与 CD4+ T、Ki-67+ 增殖 B 细胞,IgD+ 初始 B 显著富集(P = 2.38 × 10⁻¹¹),Xenium 检出 AICDA、IRF4;IgA 免疫复合物中富集颗粒酶与补体(C3、C4A、C8B)。
- **临床转化**:B 细胞签名与间质纤维化正相关;TRIDENT 中 B+ DKD(8.4%)三年内更快到达肾终点(log-rank P = 0.02);14 蛋白 B+ DKD 血浆 panel 在 Cox 模型中优于纯临床模型,UK Biobank 外部验证 AUC 0.70 vs KFRE 0.63,最高四分位风险显著更高。

## 创新点
- 迄今最大的人肾单细胞空间数据集之一,CosMx + Xenium + snRNA 跨平台、跨模态统一图谱。
- "niche"(多细胞)与 "microenvironment"(以某类细胞为中心的局部语境)两级空间抽象,并用 COVET / NicheCompass 正交验证。
- 从空间发现(B 细胞 TLS 样 niche)→ bulk 签名 → 血浆蛋白 panel → 人群生物库验证,走通一条完整的转化链,并提出 B 细胞靶向治疗 + 生物标志物分层的试验设想。

## 局限
- 空间面板非全基因组(1k / 5k),3,000 基因靠 scANVI 从 snRNA 参照**插补** —— 插补表达用于 DEG、通路与配体–受体,可能把参照的偏好带入空间结论。
- **整合时丢弃与 snRNA 参照距离过大的空间细胞** —— 这可能恰好删掉了真正的"新"或异常细胞。
- B+ DKD 组样本很小(TRIDENT 17 例,血浆 13 例),关联非因果;SMOTE 过采样 + 小阳性组容易高估;CosMx 与 Xenium 样本数不均衡(48 vs 16)。
- 完整空间数据在发表时才放出(Zenodo DOI 已预留);健康对照有限(含儿童肾),可能与成人 DKD 存在年龄混杂。

## 与本研究方向的关系
这篇与 **Plan A** 的数据形态几乎同构:Xenium 5k + H&E + snRNA 参照,正是我们 95 例活检(snRNA/snATAC/Xenium + H&E)的模态组合,因此它的流程(scVI/scANVI 整合、20–80 µm 多尺度邻域、niche/microenvironment 两级抽象、COVET/NicheCompass 正交验证)可以直接作为我们空间分析的基线。但从 **detect** 的角度,它暴露了两个关键问题,正好是 Plan A 的切入点:(1) **它把"离参照太远"的空间细胞当作整合质量问题丢弃** —— 而对异常检测而言,这些细胞正是候选异常;Plan A 应把"到参照的潜空间距离"作为显式的异常分数,并用跨模态一致性(同一位置的 H&E 形态、snATAC 可及性是否也异常)判断它是分割/探针伪影还是疾病信号,而不是直接丢掉;(2) 它依赖**插补表达**做下游结论,KidneyAnomalyBench 应包含"插补 vs 实测"不一致的检测项。它的 B 细胞 TLS 样 niche 是一个很好的**"已知稀有异常"金标准**:仅约 8.4% 患者出现、空间上聚集、有 IMC 蛋白层面证据 —— 可作为 seeded/expert-validated finding,检验我们的无监督检测器能否在不知道标签的情况下把它排进 top-k(与 NIH Kidney AI 挑战的评审指标一致)。对 **model → revert**:促纤维化微环境的配体–受体轴(HBEGF–EGFR、JAG2–NOTCH2、PDGFβ–PDGFRβ)与 B 细胞靶向是候选"回退"扰动,virtual tissue 可以模拟阻断这些轴后微环境组成是否回到 proximal/distal 等较健康的状态。对 **Plan B**,本文的结论链(空间 → bulk → 血浆 → 生物库)是构造多跳 claim-to-evidence 测试的好素材:agent 若声称"B+ DKD 进展更快",verifier 需追溯到 TRIDENT n = 17 的小样本与 log-rank P = 0.02 这一证据强度。

## 可复用资产
- **代码:** 全部分析代码。
<https://github.com/Woopsydaisy/Spatial-Human-Kidney-Map>
- **数据:** snRNA-seq 参照(Zenodo 15007208)、B 细胞单细胞图谱(Zenodo 11468564)、bulk(GSE115098)、完整空间数据(Zenodo 18674907,发表时公开)、Susztak lab 浏览器。
<https://zenodo.org/records/15007208> · <https://zenodo.org/records/11468564> · <https://doi.org/10.5281/zenodo.18674907> · <http://www.susztaklab.com>
- **探针设计:** CosMx 50 个与 Xenium 100 个肾脏自定义探针列表(Methods),可参考用于我们的 Xenium 面板。
- **方法基线:** scVI/scANVI 跨平台整合、COVET、NicheCompass、Hotspot、CellPhoneDB v5。

## 待读
- CellSpectra(Klötzer 2025,同一实验室)—— 个体患者层面的通路协调异常,可与本文的 niche 分析互补。
- NicheCompass 与 COVET 原文,评估它们能否直接产出 niche 级异常分数。
- Xenium 分割/探针伪影相关工作(本轮的 xenium-split、ovrlpy、resolVI),用于解释"离参照远"的细胞。

## 引用
```bibtex
@article{Dumoulin_2026, title={Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup}, volume={653}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10363-4}, DOI={10.1038/s41586-026-10363-4}, number={8116}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Dumoulin, Bernhard and Levinsohn, Jonathan and Klötzer, Konstantin A. and Li, Chenyu and Mao, Liran and Ha, Eunji and Mohandes, Samer and Nguyen, Thao and Paruzzo, Luca and Hirohama, Daigoro and Fang, Victoria and Bhoj, Vijay G. and Parhiz, Hamideh and Andrade-Silva, Magaiver and Abedini, Amin and Bergeson, Andi and Traum, Daniel and May, Michael J. and Kaestner, Klaus H. and Ruella, Marco and McAllister, Fiona Elizabeth and Hakimi, A. Ari and Li, Mingyao and Palmer, Matthew and Wherry, E. John and Hunter, Christopher A. and Cancro, Michael Paul and Townsend, Raymond and Coppock, Gaia and Singh, Manisha and Ross, Michael and Tumlin, James and Campbell, Kirk and Mottl, Amy and Argyropoulos, Christos and Isakova, Tamara and Almaani, Salem and Avasare, Rupali and Lafayette, Richard and Scialla, Julia and Luciano, Randy and Bansal, Shweta and Brosius, Frank and Mehta, Ankit and Lenz, Oliver and Kopyt, Nelson and Canetta, Piettro and Kretzler, Matthias and Schelling, Jeffrey and Hofherr, Alexis and Pullen, Steven S. and Thorley, Andrew and Shang, Ching and Hu, Erding and Karihaloo, Anil and Devalaraja-Narashimha, Kishor and Susztak, Katalin}, year={2026}, month=Apr, pages={1158–1169} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
