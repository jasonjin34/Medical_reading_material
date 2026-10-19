# A benchmark study of vision and pathology foundation models for computational pathology

> **文献键** `Bareja_2026` · **来源** Nature Communications(2026) · **类别** foundation · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41467-026-76004-6> · `status: complete`

---

## 一句话
PathBench 把 32 个基础模型(通用视觉 VM、通用视觉-语言 VLM、病理专用视觉 Path-VM、病理专用视觉-语言 Path-VLM)放进同一套「冻结特征 + linear probing」协议,在 41 个任务、53 个数据集、17,500+ 张全切片上统一评测,结论是:Path-VM 最强、Path-VLM 反而落后、**模型规模与预训练数据量都不能稳定预测下游表现**,而后期决策级集成能进一步提升跨数据集稳健性。

## 研究问题
病理基础模型两年内爆发式增长(CTransPath、Phikon、UNI/UNI2、Virchow、Prov-GigaPath、H-optimus、CONCH、PLIP…),但各家用各自的数据、任务与协议自评,**彼此不可比**,也无法回答两个关键问题:(1) 病理专用预训练相对通用视觉模型到底赢在哪、赢多少?(2) 这些模型在训练分布之外(不同机构、染色、扫描仪)还成立吗?此前的 benchmark 要么只比病理编码器、要么只覆盖少数癌种与弱监督分类任务。

## 方法
统一协议是全文的骨架:所有模型一律**冻结**做特征抽取,下游只训一个 **linear probe**(线性探针),slide 级用简单 mean pooling 聚合 tile 特征 —— 目的是把比较对象锁定在「表示质量」本身,而不是各家的微调技巧。模型分四类(VM / VLM / Path-VM / Path-VLM),覆盖 ViT-small/base/large 三档架构与 small(<0.1M 切片)/medium(0.1–1M)/large(≥1M)三档预训练规模。统计上做得很硬:两两比较用 Welch t 检验 + FDR 校正报 ΔAUROC 与 95% CI;模型排名用 bootstrap 方差的 Wald 检验做 task-wise 两两胜负,再算 performance score =(wins−losses)/(wins+losses) 画热图。最后额外评一个 **fusion 模型**:对 top 模型做多数投票的后期决策级集成。

## 数据
41 个下游任务 / 53 个数据集 / >17,500 张 WSI,任务类型涵盖诊断分型、生物标志物状态、**转录组亚型**与**通路活性**预测,既有器官特异也有 pan-cancer 形式,组织覆盖脑、膀胱、前列腺、**肾**、乳腺、肺等。评测被刻意切成 in-domain 与 out-of-domain 两半:**TCGA**(in-domain,19 个任务)vs **CPTAC + 外部 patch 级 benchmark + 院内 out-of-domain 队列**(22 个任务)。肾脏只以肿瘤形式出现 —— TCGA 肾癌四分类(ccRCC / ChRCC / PRCC1 / PRCC2,训练 N=194、测试 N=80)。

## 主要结果
① **TCGA 上 Path-VM 稳居第一梯队**:Virchow2、Prov-GigaPath、H-optimus-0、UNI、UNI2 长期占据前列,且各有组织偏好 —— Virchow2 强在结肠/肺/前列腺,Prov-GigaPath 强在乳腺/膀胱,H-optimus-0 强在 pan-cancer,UNI 强在脑/膀胱/乳腺。② **出了 TCGA,排名会漂**:CPTAC 与 out-of-domain 上名次出现「幅度不大但一致」的位移,说明 in-domain 强 ≠ 泛化强;作者明确指出 TCGA 极可能已进入多个模型的预训练数据,故 TCGA 成绩主要反映 in-domain 表现。③ **顶尖模型之间的差距往往很小且任务依赖**,两两统计检验后多数不显著。④ **Path-VM > Path-VLM**,且 Path-VM 与通用 VM 相比仍具竞争力 —— 图文对齐监督未能转化为分类优势。⑤ **规模不是答案**:参数量与预训练切片数都不能稳定预测下游 AUROC。⑥ **集成有效**:多数投票的 fusion 模型在 TCGA 任务累计 balanced accuracy 排名**第 1**、非 TCGA 任务排名**第 2**,说明不同基础模型的强项互补。

## 创新点
- 迄今覆盖最广的病理基础模型横评:32 模型 × 4 类别 × 41 任务 × 53 数据集,统一协议下可比。
- 显式切分 in-domain(TCGA)与 non-TCGA 评测,把「泄漏可能性」作为设计前提而非事后说明。
- 任务类型突破弱监督分类,纳入通路活性与转录组亚型这类**分子层**预测。
- 严谨的统计比较框架(Welch + FDR、bootstrap Wald、胜负热图、95% CI),而非只报一列均值。
- 给出可操作结论:与其追更大的单模型,不如做后期决策级集成。

## 局限
- 只做 linear probing,反映表示质量而非任务特定微调后的上限。
- 公开数据(TCGA/CPTAC)与预训练数据的重叠无法完全排除,可能抬高 in-domain 成绩。
- 规模分析用参数量与切片数这类粗代理,没刻画数据组成与质量。
- slide 级用 mean pooling 聚合,会稀释局部判别信号。
- **全部任务都是肿瘤**;非肿瘤疾病(纤维化、慢性器官病变)与**异常检测**类任务完全不在评测范围内。

## 与本研究方向的关系
这篇不在 detect → model → revert 这条主链的任何一环上,它坐在**横切的评测层**:回答「用哪个 backbone、怎么公平比」。价值有三点。**其一,它是骨干选型的现成依据**:我们做组织异常检测要挑 WSI 编码器,PathBench 给出了带统计检验的排名与组织特异性偏好(如果做肾,注意它的肾任务只有 RCC 分型),并且提示 UNI2/Virchow2/Prov-GigaPath/H-optimus-0 属同一梯队、差距常不显著 —— 因此**不必纠结选哪个,更应该做集成**。**其二,它是我们要做 benchmark 时的协议模板**:冻结特征 + linear probe 作为诚实基线、in-domain 与 out-of-domain 显式切分、两两统计检验而非只报均值 —— 这套东西可以直接搬到异常检测/跨模态预测任务上。**其三,也是最重要的,它的结论支持「瓶颈不在模型容量」**:规模不预测性能、专用图文模型反而落后、集成比单模型更稳 —— 这与本仓库方向的判断一致,也说明下一步该投在数据质量与评测协议上,而不是训更大的模型。**空白就是机会**:41 个任务全是肿瘤,非肿瘤疾病与异常检测任务在这个体系里是缺席的,这正是本方向可以填的位置。

## 可复用资产
- **代码:** MIT 许可,含处理后的评测结果与图源数据;部分改编自 facebookresearch/dino(Apache-2.0)。
<https://github.com/gevaertlab/benchmarking-path-models>
- **在线 benchmark:** PathBench 排行榜。
<https://pathbench.stanford.edu/>
- **数据:** TCGA(GDC portal)、CPTAC(CPTAC Data Portal)、NLST(The Cancer Imaging Archive)等外部与 out-of-domain 队列。
- **评测协议:** 冻结特征 + linear probe、mean-pooling slide 聚合、Welch t + FDR、bootstrap Wald 两两胜负与 performance score、多数投票 fusion。

## 待读
- 补读它对比的两篇既有 benchmark(参考文献 50/51)与那篇跨五癌种的近期 benchmark(60),看任务设计差异。
- 查 Virchow2 / Prov-GigaPath / H-optimus-0 的原始论文,补齐本仓库缺的这几个 Path-VM 条目(已有 virchow-2024、uni2-h-model)。
- 试跑其 repo,看 linear-probe 流水线能否直接接非肿瘤任务与异常检测评分。

## 引用
```bibtex
@article{Bareja_2026, title={A benchmark study of vision and pathology foundation models for computational pathology}, volume={17}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-026-76004-6}, DOI={10.1038/s41467-026-76004-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Bareja, Rohan and Carrillo-Perez, Francisco and Zheng, Yuanning and Pizurica, Marija and Nandi, Tarak Nath and Tian, Lu and Shen, Jeanne and Madduri, Ravi and Gevaert, Olivier}, year={2026}, month=July }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
