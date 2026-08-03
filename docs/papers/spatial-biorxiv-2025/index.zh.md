# Mapping and reprogramming human tissue microenvironments with MintFlow

> **Bibkey** `Akbarnejad_2025` · **Venue**  (2025) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1101/2025.06.24.661094>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
MintFlow 是一个基于 flow matching 的生成式 AI 模型,能在空间转录组中把每个细胞的表达解耦为「内在(intrinsic)」和「微环境诱导(microenvironment-induced)」两部分,并支持对组织微环境做 in silico 扰动(删除/替换某类细胞),预测由此引发的基因表达变化。

## 研究问题 / Problem
现有空间转录组计算方法大多是描述性的:无法把「细胞本征身份」与「微环境诱导的状态改变」分开,缺乏机制可解释性(需事后解读 embedding),依赖线性假设或先验的 ligand-receptor / 基因互作知识,扩展性差,更无法做 in silico 扰动来生成/检验假设。作者要解决的是:如何在不依赖先验知识、预定义 domain 或配体-受体对的前提下,学习微环境如何 reprogram 细胞状态,并模拟对组织的干预以预测能否 revert 疾病态。

## 方法 / Method
用 kNN 图(k=5)由空间坐标定义每个细胞的微环境,计算微环境细胞类型组成(MCC)。每个细胞推断三个 latent:内在信号 z_n(以细胞类型 CT 为条件先验)、传出信号 s_out(以 CT 为条件)、以及邻居 s_out 邻域平均得到的传入信号 s_in(间接以 MCC 为条件)。在 latent 空间用 flow matching + neural ODE 解码器得到内在与微环境诱导 embedding,再解码为 X_int 与 X_mic,满足 X = X_int + X_mic(直接给出可解释的表达分解,省去 archetype/linear-probe)。可识别性(identifiability):借鉴 iVAE,把 latent 以 CT/MCC 为条件使 [z, s_in] 在置换意义下可识别;为使分解唯一,施加最优传输(optimal transport)约束(Proposition 1);另用 Wasserstein 判别器强制内在 embedding 无法预测邻居类型。扩展性靠 inductive graph learning(子图采样,PyG neighbor loader),可训练数百万细胞。下游:聚类微环境诱导 embedding 得 MCS、算 microenvironment score 找信号热点、导出 MGP、做 in silico 扰动。

## 数据 / Data
三类人体疾病 + 多个验证数据集。(1) 特应性皮炎(atopic dermatitis):10 张皮肤切片 / 8 人,Xenium 5k(8 张为新生成),含 lesional 与 non-lesional,QC 后 197,487 细胞;外部验证含 scRNA-seq(4 患者)、23 疾病 / 6 组织跨疾病 atlas、10 名 dupilumab 治疗后患者。(2) 皮肤黑色素瘤:公开 5000-plex Xenium 数据,QC 后 98,749 细胞;跨 23 种皮肤病 fibroblast scRNA-seq 评分。(3) ccRCC 肾癌:1 患者 3 个肿瘤核心 + 肿瘤-正常界面,5000-plex Xenium,整合后 337,116 细胞 / 24 种细胞类型;再分析 ccRCC scRNA-seq(147,917 细胞 / 10 患者)、Kaede 转基因小鼠抗 PD-L1 模型、TCGA 606 例 ccRCC bulk RNA-seq。模拟数据用于 benchmark(有 ground-truth 微环境效应)。

## 主要结果 / Key results
基准:在模拟数据上按三项指标(MAE/EMD/MSE)显著优于同类方法与随机基线;真实数据上把已知 signaling 基因更多地归为微环境诱导成分,且唯一能扩展到全部 10 张皮肤切片。生物发现:(1) 特应性皮炎发现新的、空间印记的 type 2 表皮 T_RM(CD8A+ ITGAE+ GZMB+,高 IL13/IL22),以及 T_DC 活化 hub(CCL19/CCR7、CCL22/CCL17-CCR4 轴);in silico 删除 Treg 加剧炎症、增补 Treg 抑制炎症,与 10 例 dupilumab 治疗(responder Treg 上升)一致。(2) 黑色素瘤识别可诱导的类瘢痕疙瘩(keloid-like)基质:CXCL12-CXCR4 与胶原交联(LOX/LOXL1/LOXL2)介导 T 细胞排除。(3) ccRCC 识别 TLS 内三种微环境诱导 T 细胞态(TLS Core1/2/Border,常规聚类无法检出),Border 态富集耗竭标记且与差生存相关(TCGA p=0.0073);TREM2+CCR1+ TLS 巨噬细胞驱动抑制;in silico 删除巨噬细胞使 T 细胞去耗竭,重编程后基因程序反而关联生存获益(p=0.0034);虚拟替换验证 12/12 中 11 个 ground-truth 巨噬基因被正确上调。

## 创新点 / Contributions
- 首个把空间转录组表达 identifiable 地分解为 intrinsic (X_int) 与 microenvironment-induced (X_mic) 两个可解释计数矩阵的生成式模型,无需先验知识/预定义 domain/配体-受体对。
- 提出「in silico 组织扰动」:删除/替换任意细胞类型并预测邻居基因表达变化,支持大规模假设生成与检验。
- 理论保证:借 iVAE 条件化 + 最优传输约束证明分解的可识别性与唯一性(Proposition 1)。
- 通过 inductive graph learning 实现可扩展到百万级细胞的空间图训练。
- 把预测的重编程基因程序连到临床结局(TCGA 生存),完成从机制到 patient stratification 的闭环。

## 局限 / Limitations
- 对低 read counts 敏感;需要跨切片一致的基因 panel。
- flow matching 训练计算量大;虽有 neighbor sampling,但训练仍需针对数据集调超参、上手困难。
- 受当前分割(segmentation)误差影响。
- 目前限于多切片,尚未支持 multi-tissue atlas / 迁移学习;in silico 扰动的因果性仍是模型预测,需湿实验验证。

## 与本研究方向的关系 / Relation to our direction
高度契合,几乎覆盖我们三段式流程的全部环节,尤其是「virtual tissue」和「gene-revert」两段。(1) Virtual tissue modelling:MintFlow 本身就是把组织建成可扰动的生成式虚拟组织,X = X_int + X_mic 的解耦正是我们想要的「本征 vs 微环境诱导(=疾病/扰动改变)」分离。(2) Gene-revert:其 in silico 扰动(删除 TLS 巨噬细胞 → T 细胞去耗竭;增补 Treg → 抑制炎症)直接演示了「预测哪些细胞/基因被调控可 revert 异常态」,并用 TCGA 生存把 revert 后程序与获益挂钩——这正是我们要预测「modulate 后能否 revert anomaly」的范式,可直接借用其扰动-评估协议。(3) Anomaly detection:较间接,但 microenvironment score(信号热点)+ 微环境诱导 MCS 提供了一种「无监督定位微环境异常/病变热点」的信号,可作为我们 anomaly 定位后再做 revert 的前置模块。可复用点:表达解耦框架、in silico 扰动 API、扰动效应 → 生存的验证闭环。

## 可复用资产 / Reusable assets

- 代码(Python 包):<https://github.com/Lotfollahi-lab/mintflow> — MintFlow 核心库,含 in silico 扰动接口。
- 复现代码 + 模拟数据:<https://github.com/Lotfollahi-lab/mintflow-reproducibility> — benchmark、分析、带 ground-truth 的模拟数据(可作我们解耦/扰动方法的评测基准)。
- 文档/教程/user guide:<https://mintflow.readthedocs.io/>。
- 评测协议:模拟微环境效应的 ground-truth benchmark(MAE/EMD/MSE)、signaling-gene 计数归属评估、扰动敏感性分析(扰动细胞比例 vs 效应量)、in silico 扰动的生物学有效性检验(虚拟替换 → 巨噬基因上调,11/12 命中)、扰动后程序 → TCGA 生存(Kaplan-Meier)。
- 数据:Xenium 5k/5000-plex 的 AD/黑色素瘤/ccRCC 空间数据(部分公开,其余「即将开放」);可复用的 MGP 基因签名(T_DC MGP、Stroma MGP、TLS T/Border 程序)。

## 待读 / Follow-ups
- Supplementary Note 2–5:identifiability 证明、encoder/decoder 架构、ELBO 推导——若要复用/改造模型必读。
- 对比 iVAE / flow matching / neural ODE 原始文献,理解可识别性假设在细胞非独立(空间图)下的松弛。
- 跑通 mintflow-reproducibility 的模拟 benchmark,评估能否作我们 anomaly/revert 方法的对照。
- 关注后续「即将开放」的 AD/ccRCC 原始 Xenium 数据发布。

## 引用 / Cite
```bibtex
@article{Akbarnejad_2025, title={Mapping and reprogramming human tissue microenvironments with MintFlow}, url={http://dx.doi.org/10.1101/2025.06.24.661094}, DOI={10.1101/2025.06.24.661094}, publisher={openRxiv}, author={Akbarnejad, Amir and Steele, Lloyd and Jafree, Daniyal J. and Birk, Sebastian and Sallese, Marta Rosa and Rademaker, Koen and Boxall, Adam and Rumney, Benjamin and Tudor, Catherine and Patel, Minal and Prete, Martin and Makarchuk, Stanislaw and Lee, Colin Y.C. and Maaskola, Jonas and Li, Tong and Stanley, Heather and Foster, April Rose and Roberts, Kenny and Trinh, Andrew L. and Villa, Carlo Emanuele and Testa, Giuseppe and Mahil, Satveer and Mehrjou, Arash and Smith, Catherine and Vakili, Sattar and Clatworthy, Menna R. and Bayraktar, Omer Ali and Mitchell, Thomas and Haniffa, Muzlifah and Lotfollahi, Mohammad}, year={2025}, month=June }
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
