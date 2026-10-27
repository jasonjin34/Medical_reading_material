# Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics

> **文献键** `Bilous_2026` · **来源** Nature Methods(2026) · **类别** spatial · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41592-026-03089-8> · `status: complete`

---

## 一句话
作者用 27 位供者、41 张乳腺癌与非小细胞肺癌切片(靶向 Breast/Lung/Custom IO 面板 + 5K PRIME 面板,配匹配 snRNA-seq 与 IHC)系统刻画 Xenium 的灵敏度、特异性和**转录本溢出(spillover)污染**,并提出 SPLIT:用 RCTD doublet 模式的细胞类型权重,把每个被污染细胞的计数按参照谱拆成「主」「次」两部分,只保留主细胞类型的纯化表达。

## 研究问题
Xenium 被广泛使用,但其数据特性缺乏大规模刻画:已有比较研究只有少数患者或组织芯片,没人直接比较过靶向面板与 5K 面板的灵敏度/特异性。更关键的是,分割误差和转录本**在 x–y 平面内**溢出到邻近细胞,会制造「人工转录组双细胞」—— 这些并非单细胞测序意义上的物理双细胞,而是信号层面的混合;z 轴重叠只能解释一部分。现有校正方法(加权 NMF+CRF、resolVI、FastReseg、ProSeg 等)要么依赖启发式,要么不可解释,且只在少量样本上验证过。

## 方法
**注释**:用 RCTD(doublet 模式)以匹配 snRNA-seq(或外部 scRNA-seq)为参照,为每个 Xenium 细胞估计主/次细胞类型及权重 w1、w2;作者强调 Xenium 中的 RCTD「doublet」几乎都不是真双细胞,因此称有次信号的细胞为「contaminated」,无次信号的为「pure」。**溢出量化**:比较细胞的污染程度 w2 与其二维邻域中同一(次)细胞类型的局部丰度,二者余弦相似度高 → 污染来自邻居溢出;对每对细胞类型求平均得到 **spillover index**,衡量某类细胞「向外污染」的倾向。**SPLIT**:按 RCTD 权重与参照谱,把每个被污染细胞的转录本按比例分配给主/次来源,默认保留主谱;可选**空间门控** —— 只有当邻域中确实有大量次细胞类型时才分解,避免把参照中缺失的真实表型(如增殖期肿瘤细胞)错误拆掉;**SPLIT-shift** 可依据邻域同质性把主表型改判为次表型。**正交验证**:Xenium 后做多重 IHC(CD8、肿瘤标志)。**比较**:SPLIT vs resolVI vs ovrlpy,并与默认 5 µm 扩张、纯核(0 µm)、多模态、Baysor、ProSeg、Segger 分割全组合比较,指标为 scib 生物保守/批次、保留细胞与基因数、恶性→T 细胞污染强度(邻域逻辑回归)、与 Chromium T 细胞伪 bulk 的余弦相似度。

## 数据
自产数据:19 张乳腺癌 FFPE 切片(17 位供者)+ 22 张 NSCLC FFPE 切片(10 位供者),共 41 张;乳腺用 Breast 靶向面板,NSCLC 用 Lung 靶向面板、自定义免疫肿瘤面板(Custom IO)与 5K PRIME 面板;部分样本有技术重复(相邻切片)、匹配 snRNA-seq(Chromium)和多重 IHC。外部参照:扩展肺癌 scRNA 图谱(318 位患者、>100 万细胞)与 Wu 等乳腺癌 scRNA。另用公开 Xenium 数据验证溢出普遍性。Xenium 数据 GEO GSE311609;snRNA 参照在 cellxgene。

## 主要结果
- **可重复性高**:技术重复(相邻切片)几乎完全一致;仅做 Seurat log 归一化、不做批次整合,非恶性细胞即可跨患者对齐(恶性细胞按患者成簇,符合预期)。
- **靶向面板比 5K 灵敏**:限定 194 个共有基因时,5K 与 Lung 面板的细胞类型分离相当,但 **5K 约 60% 细胞因转录本过少未通过 QC**,同基因下检测到的转录本明显更少,灵敏度接近 Chromium;两种面板的细胞类型组成仍高度一致;两个靶向面板(仅共享 87 个基因)之间一致性最高。
- **溢出普遍存在**:w2 与邻域中同类细胞丰度高度余弦相似,在公开多组织 Xenium 和不同分割下都可复现;越丰富的细胞类型 spillover index 越高,**恶性细胞最高**;IHC 显示肿瘤特异转录本延伸进相邻 CD8+ T 细胞,有时强到让 RCTD 把主次类型颠倒;低 RNA 含量细胞(如 T 细胞)受害最重。
- **纯核分割(0 µm)也有污染**,校正后改善;5K 在多模态分割下污染显著更低,但作者提醒这可能只是每基因转录本少导致统计功效下降。
- **方法比较**:所有校正方法都改善细胞类型分离并降低污染;**SPLIT 的细胞类型分离最好、与 Chromium 谱余弦相似度最高**(作者承认这部分源于 SPLIT 本身用了 Chromium 参照);**ovrlpy 与 resolVI 显著减少表达基因数、留下大量近空细胞**;resolVI 有时 iLISI 略差。分割上 ProSeg 优于 Baysor、多模态与 Segger,**ProSeg + SPLIT 整体最佳**。乳腺癌样本结论一致。
- **生物学**:未校正时,肿瘤邻近 T 细胞富集虚假的恶性/上皮基因签名;SPLIT 校正后,邻近肿瘤的 T 细胞显示更强的耗竭签名(HAVCR2/TIM-3、CTLA4、PDCD1、LAG3、CXCL13);resolVI、ovrlpy 的效果不稳定,resolVI 偶尔同时压掉污染与 T 细胞程序。

## 创新点
- 迄今最大的 Xenium 系统评估之一,并首次直接比较靶向面板与 5K 面板的灵敏度–覆盖度权衡。
- 把 RCTD 的 doublet 权重重新解释为**污染度量**,并提出 cell-type 级的 **spillover index**。
- SPLIT:简单、可解释、基于参照的信号分解,可与任何分割组合,并用空间门控防止过度校正。
- 用 IHC 蛋白信号做正交验证(蛋白染色不易溢出)。

## 局限
- **依赖参照**:参照中没有的细胞状态可能被错拆;作者计划做无参照版本。
- 主分析只覆盖两种癌症;每个细胞只建模主+次两种来源。
- 「SPLIT 与 Chromium 最像」的指标对 SPLIT 有利(作者已说明);与 resolVI 的比较结论和 resolVI 论文本身的结论相反 —— 两组都在自己设计的指标上胜出。
- 5K 污染较低可能只是统计功效问题,未能区分。

## 与本研究方向的关系
对 **课题 1** 这几乎是一份操作手册:snRNA + snATAC + Xenium + H&E 这类多模态设计**同时有 snRNA/snATAC 与 Xenium**,正好满足 SPLIT「匹配 snRNA 参照 + RCTD」的前提。三点直接可用:**(1) 「contaminated vs pure」+ spillover index 作为伪影标签** —— 肾脏中近端小管细胞数量最多,很可能扮演本文「恶性细胞」的角色,向体积小、RNA 少的免疫细胞溢出;在 KidneyAnomalyBench 里,一个「免疫细胞表达 PT 标志物」的异常若与邻域 PT 丰度一致,应优先判为溢出伪影。**(2) 跨模态一致性**:本文用 IHC 这种不易溢出的模态验证转录组信号,与课题 1「用跨模态一致性区分伪影与疾病」完全同构 —— 可对应到 H&E 形态和 snATAC。**(3) 面板选择**:5K 面板灵敏度低、约 60% 细胞未过 QC,做异常检测时低计数细胞本身就是「异常」来源,需要单独分层。**关键张力**:SPLIT 是参照驱动的,参照中没有的状态会被拆回已知类型 —— 而异常检测要找的恰恰是参照中没有的东西。若用健康参照做 SPLIT,可能把疾病特异状态(如 `inflammatory-pt-natcommun-2025` 的炎症性 PT)「纯化」成普通 PT。所以应使用疾病参照或空间门控模式,并把「校正前后异常是否稳定」作为基准的一部分。对 **课题 2**:本文与 resolVI 论文对同一组方法得出相反排名,是「评测指标由作者选择 → 自评偏差」的典型案例,适合作为 claim-to-evidence 校验中「比较性结论需要独立证据」一类的样例;作者对 5K 低污染的谨慎解读(可能是功效不足)也是 agent 应学会的推理。

## 可复用资产
- **代码:** SPLIT R 包、完整 Xenium 分析流程、复现代码。
<https://github.com/bdsc-tds/SPLIT>
<https://github.com/bdsc-tds/xenium_analysis_pipeline>
<https://github.com/bdsc-tds/Bilous2026>
- **数据:** 41 张 Xenium 切片(GEO GSE311609)与匹配 snRNA 参照(cellxgene)。
<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311609>
<https://cellxgene.cziscience.com/collections/bd552f76-1f1b-43a3-b9ee-0aace57e90d6>
- **评测协议:** 「分割 × 校正」全组合比较框架;邻域逻辑回归测污染强度;spillover index。

## 待读
- Marco Salas 等的 Xenium 质量评估;Mitchel 等关于错配导致虚假细胞通讯;ProSeg(Jones 等)。
- 在肾脏 Xenium 上复现 resolVI / SPLIT / ovrlpy 三方比较,看结论是否依赖组织与指标。

## 引用
```bibtex
@article{Bilous_2026, title={Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics}, volume={23}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-026-03089-8}, DOI={10.1038/s41592-026-03089-8}, number={6}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Bilous, Mariia and Buszta, Daria and Bac, Jonathan and Kang, Senbai and Dong, Yixing and Tissot, Stephanie and Andre, Sylvie and Alexandre Gaveta, Marina and Voize, Christel and Peters, Solange and Homicsko, Krisztian and Gottardo, Raphael}, year={2026}, month=Apr, pages={1152–1162} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
