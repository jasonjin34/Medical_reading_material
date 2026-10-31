# Energy-based Out-of-distribution Detection

> **文献键** `Liu2020_201003759` · **来源** Advances in Neural Information Processing Systems 33 (NeurIPS 2020)(2020) · **类别** anomaly · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2010.03759> · `status: complete`

---

## 一句话
把分类器的 logit 解释为能量模型:free energy E(x) = −T·logsumexp(f(x)/T) 与输入密度对齐,而 log MSP 只是「logit 减去最大 logit」后的 energy,是一个有偏分数;因此**直接用 energy 替代 softmax 置信度**——不需训练、无超参——就能在 CIFAR-10 上把平均 FPR95 降低 18.03%;若有辅助离群数据,再用两条 squared hinge 损失做 **energy-bounded 微调**,拉开 ID 与 OOD 的能量差,超过 Outlier Exposure。

## 研究问题
依赖 softmax 置信度的 OOD 检测会被「对远离训练数据的输入给出任意高置信度」所害(softmax 后验有 label-overfitted 的输出空间)。显式密度估计又靠不住:深度生成模型可能给 OOD 数据更高似然(Nalisnick 等),而 JEM 这类从生成视角估计 log p(x) 的方法需要归一化密度,优化不稳定。作者问:能否从纯判别式分类器得到一个与密度对齐、又易用的 OOD 分数?

## 方法
**能量函数**:对 K 类 logit f(x),定义 E(x, y) = −f_y(x),free energy E(x; f) = −T·log Σᵢ e^{fᵢ(x)/T}(即 softmax 分母的对数)。由 Gibbs 分布,p(x) ∝ e^{−E(x)/T},所以能量越低 → 密度越高。用 NLL 训练的分类器会把 ID 数据的能量往下压(梯度推导:真实类能量被压低,其他类被拉高)。**推理时分数**:用 −E(x; f) 设阈值 τ(阈值用 ID 数据选,使大部分 ID 被判对),高能量判为 OOD;logsumexp 一行实现,T=1 即可,无需调参。**与 softmax 的关系**:log max_y p(y|x) = E(x; f) + f_max(x)——对 ID 数据 E 偏低而 f_max 偏高,二者相加互相抵消,所以 MSP 是被「最大 logit 平移」过的有偏 energy。**Energy-bounded 训练**:目标 = 交叉熵 + λ·L_energy,其中 L_energy = E_ID[max(0, E(x_in) − m_in)²] + E_OOD[max(0, m_out − E(x_out))²],两个独立 margin(m_in ∈ {−3, −5, −7},m_out ∈ {−15, −19, −23, −27},按验证集 FPR95 选);λ=0.1,10 个 epoch,学习率 0.001 余弦衰减;辅助离群数据为 80 Million Tiny Images(去掉与 CIFAR 重复的样本)。作者也试过单 margin 的 hinge,训练不如双 margin 稳定。

## 方法谱系
**范式:基于分类器的 OOD(classifier-based OOD)**,训练版本属于借助辅助离群数据的 Outlier Exposure 一支。直接建立在 MSP 基线(`msp-ood-iclr-2017`,文中 [13])、ODIN(温度缩放;本文发现对 energy 来说 T 越大反而越差)和 Outlier Exposure(把 OOD 的 softmax 推向均匀)之上,并与 JEM(联合能量模型)对比。Mahalanobis(`mahalanobis-ood-neurips-2018`)作为基线出现在 Table 2。**后续**:综述(`generalized-ood-survey-ijcv-2024`)把它列为 post-hoc 输出类方法的代表,后续有 JointEnergy(多标签)、ReAct(截断激活后再算 energy 等分数)等;在 OpenOOD 基准中以 EBO 名义出现。

## 数据
ID:CIFAR-10、CIFAR-100、SVHN(标准划分),WideResNet。OOD 测试集六个:Textures、SVHN、Places365、LSUN-Crop、LSUN-Resize、iSUN。辅助离群训练数据:80 Million Tiny Images。生成模型对比另用 CelebA。

## 主要结果
- **一个直观例子**:CIFAR-10 样本与 SVHN 样本的 softmax 置信度几乎相同(1.0 vs 0.99),负能量却是 11.19 vs 7.11。
- **预训练模型,不微调**(WideResNet,六个 OOD 集平均):CIFAR-10 上 FPR95 从 MSP 的 51.04 降到 33.01(−18.03),AUROC 90.90 → 91.88;ODIN 35.71、Mahalanobis 37.08(AUROC 91.09 / 93.27)。CIFAR-100 上 FPR95:MSP 80.41、energy 73.60、ODIN 74.64、Mahalanobis 54.04。SVHN 作为 ID 时 energy 比 softmax 低 8.69 个 FPR95 点。
- **微调**:CIFAR-10 上 energy 微调 FPR95 3.32(AUROC 98.92),OE 8.53(98.30),即降低 5.20;CIFAR-100 上 47.55 vs OE 58.10(降低 10.55),AUROC 88.46 vs 85.19。SVHN 例子中 FPR95:softmax 48.49 → energy 35.59(预训练);OE 4.36 → energy 微调 1.04。
- **分类准确率基本不变**:CIFAR-10 测试错误率 energy 微调 4.98%(正文;Table 2 列为 4.87)vs OE 5.32% vs 预训练 5.16%。
- **对比生成/混合模型**(CIFAR-10,AUROC):energy 分数 SVHN 0.91 / CIFAR-100 0.87 / CelebA 0.78,energy 微调 0.99 / 0.94 / 1.00;JEM-softmax 0.89 / 0.87 / 0.79,类条件 Glow 0.64 / 0.65 / 0.54。
- **温度**:T 从 1 增到 1000,预测更均匀,energy 区分度下降——T=1 即最佳。

## 创新点
(1) 给出 MSP 与 free energy 的精确关系,说明 MSP 为何有偏;(2) 一个无参数、即插即用的 post-hoc OOD 分数;(3) 一个直接优化 ID/OOD 能量差的训练目标,既能配合辅助离群数据,又不改变语义类空间;(4) 在判别式框架下获得密度解释,避开生成模型的训练难题。

## 局限
「与密度对齐」是 up to 归一化常数的论证,分类器的 logit 并没有被训练成真正的密度;微调版本依赖大规模辅助离群集(80M Tiny Images)且需仔细去重,综述把「对辅助离群数据的依赖」列为领域主要挑战之一;CIFAR-100 上 energy 预训练分数仍明显差于 Mahalanobis(73.60 vs 54.04 FPR95);只在 32×32 图像分类上验证;作者自己说下一步要走出图像分类。

## 与本研究方向的关系
**映射到肾脏组学**:任何在健康参照(KPMP、Lake 图谱)上训练的细胞类型注释器、或 H&E 组织类型分类器,都能免费算出每个细胞/spot/patch 的 energy;它比 MSP 多利用了 logit 的整体幅度,是伪影注入课题里比 MSP 更强、同样零成本的基线。**能量微调对应「Outlier Exposure 式」的肾脏版本**:需要一个辅助离群集——可选非肾脏器官的细胞(其他器官图谱)或其他组织的 H&E patch,这正是 `histo-nejmai-2024` 的做法(正常胃肠 patch vs 异质 out-of-domain 组织 patch 的 OE 二分类器,其最佳方案)。**哪些假设会断**:(1) **logit 幅度与数据质量耦合**——低 UMI、高线粒体比例、受环境 RNA 污染的细胞表达信号弱,logit 整体偏小 → 能量偏高 → 被判为 OOD;于是 energy 很可能主要在检测**低质量细胞**而非疾病状态;(2) **批次效应**同样改变 logit 尺度;(3) **辅助离群集决定了检测器学会找什么**——如果用空液滴、doublet 或其他技术噪声当离群样本,会把检测器调成 QC 工具;用其他器官细胞,则学到的是「器官身份」而非「肾脏病理」——都不等于疾病;(4) 连续疾病状态下没有清晰的 ID/OOD 能量边界,双 margin 的设定需要重新思考。因此 energy 适合作为**单模态内的分数**,再用伪影注入课题的跨模态一致性(snRNA vs snATAC、Xenium vs H&E)过滤与质量相关的报警。**对 Agent 可信度课题**:logsumexp 型的不确定性分数可以作用于 LLM 的 token logits;综述也把「用 OOD 检测缓解 LLM 幻觉」列为未来方向——但本文的「logit 幅度 ≠ 正确性」的教训同样适用:verifier 需要单独校准。

## 可复用资产
- **代码:** 官方实现(energy 分数与 energy-bounded 微调)。
<https://github.com/wetliu/energy_ood>
- **一行分数:** `-torch.logsumexp(logits, dim=1)`(T=1)——可直接加到任何肾脏注释器的输出上。
- **训练配方:** 交叉熵 + 0.1×双 margin squared hinge;margin 取预训练模型 ID/OOD 能量均值附近。

## 待读
- Outlier Exposure(Hendrycks 等,2019)原文,以及 ReAct(Sun 等,2021)——energy 的两个最常见搭档。
- 在肾脏数据上检验 energy 与 UMI 数 / 线粒体比例的相关性:若高度相关,说明它主要在测质量而非疾病。

## 引用
```bibtex
@inproceedings{Liu2020_201003759,
  title = {Energy-based Out-of-distribution Detection},
  author = {Liu, Weitang and Wang, Xiaoyun and Owens, John D. and Li, Yixuan},
  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS 2020)},
  year = {2020},
  eprint = {2010.03759},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2010.03759}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
