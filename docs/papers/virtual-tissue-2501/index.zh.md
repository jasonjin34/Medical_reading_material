# AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery

> **文献键** `Wenckstern2025_250106039` · **来源** arXiv preprint(2025) · **类别** virtual-tissue · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2501.06039> · `status: complete`

---

## 一句话

VirTues 是首个面向空间蛋白质组学(spatial proteomics / multiplex imaging)的通用基础模型:用蛋白质语言模型(ESM-2)嵌入把「marker 身份」编码进 token,再用「空间注意力 / marker 注意力」分解式 Transformer,从单一预训练 backbone 同时支持 marker 重建、cell typing、niche 注释、生物标志物发现与病人分层,并能跨异质 panel 做 zero-shot。

## 研究问题

Multiplex imaging(IMC、mIF 等)一次可测数十到上百个蛋白通道,但每个研究用不同的 antibody panel、协议与平台,导致 marker 数量/身份/动态范围各异;现有方法基本为单一 cohort/panel 定制,无法跨 cohort、cancer type、平台迁移知识,难以做稳健的 biomarker discovery。核心问题:如何构建一个能吃「任意 marker 组合」、跨尺度(蛋白→细胞→niche→组织)统一表征、并具临床价值的基础模型。

## 方法

三项核心设计:(1) **Marker-aware tokenization** — 图像按 crop 切成「每个 marker × 每个位置」的 image token,与 ESM-2 蛋白语言模型嵌入通过线性投影相加融合,从而处理可变 marker 集合并注入生物先验;可学习的 patch summary token 聚合成 cell / niche / tissue summary token(细胞级通过与分割 mask 卷积聚合)。(2) **分解式注意力** — 把 Transformer 注意力拆成 *marker attention*(仅在通道间交互,学习蛋白间关系)与 *spatial attention*(仅在位置间交互,学习组织结构),避免标准 ViT 对空间×通道的二次方复杂度。(3) **Masked autoencoder 预训练** — 三种 mask 策略:independent masking(每 marker 独立随机 mask 60–100%)、marker masking(整通道 mask,测跨 marker 关系)、niche masking(整块区域所有 marker 全 mask,测全局结构);decoder 逐通道重建。推理阶段用 niche summary token + optimal transport(Wasserstein 距离)做相似病例检索。下游任务用 linear probing(细胞级)与 ABMIL(组织级)。

## 数据

在 **15 个 imaging mass cytometry (IMC) 数据集**、覆盖 8 个器官部位上训练/评测,共测 147 个不同 marker(蛋白、蛋白修饰、mRNA)。规模:**3,102 病人、8,887 组织样本、>259,000 个 256×256 image crop、>1450 万个分割细胞**(9 个带分割 mask 的数据集)。关键 cohort:Cords et al.(肺癌,细粒度细胞类型+临床元数据)、Wang et al. **NeoTRIP TNBC**(138 三阴乳腺癌病人接受 atezolizumab+carboplatin+nab-paclitaxel,67 例达完全病理缓解;pre/on/post 治疗时间点)、Danenberg et al. **METABRIC** 乳腺癌(ER+ n=541,21 年随访)、Rigamonti et al. 肺癌(含训练外新 marker,用于 zero-shot)、Hoch/Jackson/Meyer 等乳腺与黑色素瘤数据集。训练语料在开源仓库中打包为 **spora**(31+ 空间蛋白质组学数据集的整理集合)。

## 主要结果

- **Marker 重建**:三种 mask 平均 Pearson r=0.723±0.157;zero-shot 到未见数据集已知 marker r=0.667(in-domain 0.797),independent/niche masking 几乎不掉(Δr=0.016 / −0.002),说明 PLM 先验支撑「虚拟 marker 增补」。
- **细胞分型**:平均 macro-F1 比 KRONOS 高 +6.31%、比 CA-MAE 高 +65.79%;全语料训练相较单数据集训练,稀有免疫群大涨(NK +95.6%、myeloid +35.2%、T +30.4%、B +27.9%);zero-shot cell typing 与 in-domain 差 ≤0.03 F1。
- **组织/临床预测(ABMIL)**:肺癌亚型 0.856 F1、乳腺 ER 状态 0.806、TNBC on-treatment 应答 0.714(全部显著优于 KRONOS)。
- **生存分层**:METABRIC ER+(n=541)按表型组成指纹聚类分高/低危,log-rank P<0.001。
- **TNBC anti-PD-L1(核心)**:从 pre-treatment 细胞经多分辨率 Leiden 聚类筛出 4 个签名(RS1/RS2/NRS1/NRS2);多变量组合 **cross-val AUROC 0.817**,优于 Wang et al. 空间预测器 +4.53%(P<0.001)、优于 immune-ratio 基线 23–30%。迁移到独立 Meyer et al. cohort 做无病生存分层:低危(n=33)3 事件 vs 高危(n=45)21 事件,log-rank P<0.005;**concordance index 0.628**,优于 Meyer 分层(0.606)与各 tumor/免疫比值基线。

## 创新点

- **Marker-aware tokenization**:把 ESM-2 蛋白语言模型嵌入注入 image token,使模型能吃任意 marker 组合并对全新 marker 做 zero-shot(无需重训)。
- **分解式空间/marker 注意力**:突破标准 ViT 的空间×通道二次方复杂度,可扩展到高维 multiplex 数据,且注意力本身可解释。
- **多尺度层级表征**:patch→cell→niche→tissue summary token,单一 backbone 覆盖分子到临床全尺度任务。
- **可复用计算层**:同一预训练模型完成重建、cell typing、niche 注释、OT 病例检索与跨 cohort 可迁移的 biomarker 发现,建立「空间蛋白质组学基础模型」范式。

## 局限

- 对与训练集生化关系弱的全新 marker,重建/预测会退化;「虚拟 marker 增补」需带校准与不确定度。
- 稀有细胞状态与罕见组织结构仍难,主要受数据稀缺限制。
- 生存分析多为未校正模型;需协变量校正、比例风险检验与前瞻验证才能临床采用。
- 注意力图仅是部分解释,缺因果/扰动分析。
- 仅在 15 个 IMC cohort、8 器官上训练;跨更多疾病、组织处理协议与成像平台的普适性待验证。当前限于蛋白/RNA marker,H&E、空间转录组、代谢组等多模态融合是下一步。

## 与本研究方向的关系

这篇是我们「virtual tissues」概念的**奠基性核心参考**,直接落在流水线中间的「virtual tissue 建模」一环,并对首尾两环都有可复用件:

- **Virtual tissue 建模(主命中)**:VirTues 正是把组织显式建模为「virtual tissue」——多尺度、marker-aware、跨 panel 统一的组织表征(patch/cell/niche/tissue summary token)。它示范了如何从异质 spatial-proteomics 学一个通用 backbone,可作为我们组织表征层的直接骨架或对照基线。其 spora 语料 + Hugging Face checkpoint 可直接拿来当预训练表征。
- **Anomaly detection(前环,可改造)**:MAE 预训练目标天然是一个「重建正常组织」的自监督框架——重建误差(或 marker/niche masking 下的偏差)可直接改造为**anomaly score**,用于检出因疾病/药物扰动而改变的区域。论文本身已展示「responder 的 cell-state 分布位移大于 non-responder」,即扰动引起的分布偏移可被 VirTues 表征捕捉,这与我们的「检测因扰动改变的区域」目标高度一致。
- **Gene/target revert(后环,间接)**:虽然 VirTues 不做基因扰动预测,但其 biomarker discovery 流程(cell 嵌入 → 多分辨率 Leiden 聚类 → 病人级 cross-val 评分 → 可迁移签名 RS/NRS)给出了「从 virtual tissue 表征反推与治疗应答/逆转相关的分子程序」的可复用范式;RS1/RS2 富集的 PD-L1+GZMB+、CD4+ T 等群体正是候选调控靶点方向。其 marker attention 还能指出每个 niche 的关键蛋白,可作为「哪些分子若被调控会改变该 niche」的假设生成器。
- **对照/评测**:其 zero-shot 跨 panel 协议、OT 病例检索、cross-cohort 签名迁移都可作为我们评测方案的模板。

## 可复用资产

- **代码**:官方仓库 `github.com/bunnelab/virtues`(MIT license)。conda 脚本建 Python 3.12 环境;`configs/base_config` 配数据/marker 嵌入路径;3 个 Jupyter notebook 演示 reconstruction / cell phenotyping / segmentation;附 `spora-bench` 基准库。
- **预训练 checkpoint(Hugging Face Hub)**:`virtues-sp32`(32 数据集,CC BY-NC 4.0)、`virtues-sp31`(31 数据集,MIT)、`virtues-imc14`(14 个 IMC 数据集,CC BY-NC 4.0)。
- **数据集**:`spora`——31+ 空间蛋白质组学数据集整理集合,含自定义数据转 spora 格式的指南与示例数据。
- **Marker 嵌入**:ESM-2 蛋白语言模型嵌入(可为新 antibody 生成 marker token)。
- **评测协议**:linear-probing 细胞分型、ABMIL 组织级预测、OT/Wasserstein 病例检索、Leiden→cross-val AUROC 的 biomarker 发现与 cross-cohort 迁移(concordance-index / log-rank 生存评估)。

## 待读

- 核对 v1 与 v2 差异:v1 报 4 数据集/96 marker/2062 病人,v2 扩到 15 数据集/147 marker/3102 病人并加入 NeoTRIP TNBC 主线——确认引用哪个版本。
- 精读 KRONOS(主要对照基线)与 CA-MAE 的差异,评估作为我们 baseline 的合适度。
- 复现 `virtues-sp31`(MIT,可商用友好)在自有 IMC/mIF 数据上的 zero-shot cell typing。
- 验证「reconstruction error 作 anomaly score」的可行性:在药物扰动配对样本上测 masking-deviation 是否与已知变化区域对齐。
- 追 ESM-2 marker 嵌入对 antibody 命名/克隆差异的鲁棒性(marker isolation 退化问题)。

## 引用
```bibtex
@misc{Wenckstern2025_250106039,
  title = {AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery},
  author = {Johann Wenckstern and Eeshaan Jain and Yexiang Cheng and Benedikt von Querfurth and Kiril Vasilev and Matteo Pariset and Phil F. Cheng and Petros Liakopoulos and Olivier Michielin and Andreas Wicki and Gabriele Gut and Charlotte Bunne},
  year = {2025},
  eprint = {2501.06039},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2501.06039}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
