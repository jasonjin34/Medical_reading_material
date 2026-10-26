# 6 · 伪影，以及长得像伪影的生物状态

> ⏱ 约 45 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - doublet、ambient、低质量细胞、解离应激分别是怎么来的？
    - 它们在数据里长什么样，为什么会被当成病？
    - 哪些真实的生物状态反过来会被当成伪影？

## 正文

!!! note "正在编写"
    这一模块的正文还在写。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [双细胞假象(doublet)](glossary.md#doublet) | Doublet | 两个细胞或细胞核被同一条形码捕获、当作一个细胞分析的技术假象,产生嵌合表达谱,可能被误认为一种新的细胞状态。 |
| [游离 RNA 污染(ambient RNA)](glossary.md#ambient-rna) | Ambient RNA | 破裂细胞释放的游离转录本被计入其他液滴,形成背景信号,使本不相关的细胞看起来彼此相似。 |
| [空液滴](glossary.md#empty-droplet) | Empty droplet | 没装细胞的油滴；里面只有漂在液体里的 RNA，所以正好是 ambient 的样本。raw 矩阵里有，filtered 矩阵里被去掉。 |
| [低质量细胞](glossary.md#low-quality-cell) | Low-quality cell | 快死或破损的细胞：RNA 分子和基因数少、线粒体比例高；通常按 QC 阈值过滤掉，但受损细胞也可能长得很像。 |
| [线粒体比例](glossary.md#mitochondrial-fraction) | Mitochondrial fraction (percent.mt) | 一个细胞的 RNA 里来自线粒体基因的比例；标准 QC 指标（高 = 细胞应激或快死了）。完整细胞本来就比细胞核高。 |
| [解离应激](glossary.md#dissociation-stress) | Dissociation stress | 组织在 37 °C 消化时细胞启动的应激基因（FOS、JUN、热休克蛋白等）；让细胞看起来受了伤，其实伤是在实验室里造成的。 |
| [技术性丢失(假零)](glossary.md#technical-dropout) | Technical dropout (false zero) | 计数矩阵中因捕获失败而非真的不表达所产生的零;由于真零与假零无法区分,稀疏性同时既是生物学也是噪声。 |
| [批次效应](glossary.md#batch-effect) | Batch effect | 不同机构、时间或平台采集的数据集之间的系统性非生物学差异,若不校正会混淆分析。 |
| [多倍体 / 多核](glossary.md#polyploidy) | Polyploidy / multinucleation | DNA 拷贝多出来或有不止一个核的细胞；损伤后一些小管细胞会变成多倍体，一些足细胞会变成双核。在单细胞数据里，这类细胞可能看起来像 doublet。 |
