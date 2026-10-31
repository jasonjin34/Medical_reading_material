# A Unifying Review of Deep and Shallow Anomaly Detection

> **文献键** `Ruff2020_200911732` · **来源** Proceedings of the IEEE(2021) · **类别** anomaly · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1109/JPROC.2021.3052449> · `status: complete`

---

## 一句话
这篇综述(TU Berlin / Kloft / Dietterich / Müller 组)把异常检测统一到一个**概率定义**(异常 = 正常分布 P⁺ 低密度区的点,问题即密度水平集估计)和一个**五维建模框架**(损失、模型、特征映射、正则、推断方式)之下,把经典"浅层"方法与深度方法按三大族——**概率/密度、单类分类、重建**——一一对应;再用 MNIST-C 与 MVTec-AD 的统一实验与 XAI 解释表明:没有银弹,而且高 AUC 可能是 **Clever Hans**(靠虚假相关取得)。

## 研究问题
深度学习让图像、文本等复杂数据上的异常检测性能大幅提升,随之涌现大量基于生成模型、单类分类与重建的新方法。但这些方法各自隐含的假设(异常是什么类型、异常分布的先验、训练数据是否干净)很少被说明,彼此之间以及与经典核方法之间的联系也不清楚,评测习惯(把分类数据集的某些类当异常)也受到质疑。作者要给出:统一的形式化定义、可以系统比较方法的框架、带解释的经验评估与实操建议,以及开放问题清单。

## 方法
**(1) 定义**:正常概念 = 真实分布 P⁺(密度 p⁺);异常集 A = {x | p⁺(x) ≤ τ}。核心是**集中性假设**(正常数据集中在高密度区,异常不集中),因此异常检测 ≈ 在水平 α 下估计密度水平集;异常分数提供连续排序,阈值决定误报率。**异常类型**:点异常、条件/上下文异常(依赖时间、空间或图结构的条件分布 p⁺(x|t))、群体/集体异常(单点都正常、整体联合分布异常),以及作者新增的**低层感官异常 vs 高层语义异常**(纹理划痕 vs "猫群里的狗")。**数据设定**:无监督(默认训练数据"干净",但现实中是 P = (1−η)P⁺ + ηP⁻ 的**污染**混合,外加噪声 ε)、半监督(少量带标签正常/异常)、监督;并指出 KDE、OC-SVM 等隐式假设异常分布 P⁻ 是均匀分布。**(2) 三大族**:**概率模型**(Gaussian/Mahalanobis、GMM、KDE、能量模型、VAE/GAN、normalizing flow)——作者引 Vapnik 原则指出完整密度估计"多解了问题";**单类分类**(OC-SVM、SVDD、Deep SVDD 等,只估计一个水平集边界;负样本按信息量分为人工、辅助(如 Outlier Exposure)与真实异常三种);**重建模型**(PCA/核 PCA、自编码器、原型聚类如 k-means/VQ)。另有不学目标函数的**距离类**方法(kNN、LOF、Isolation Forest)。**(3) 统一视角**:五个建模维度 D1 损失 ℓ(s,y)、D2 模型 f_θ(x)、D3 特征映射 φ(x)(原始输入 / 核 / 神经网络)、D4 正则 R(f,φ,θ)、D5 推断方式(频率派或贝叶斯);统一目标 min (1/n)Σℓ(f_θ(xᵢ),yᵢ) + R(f,φ,θ),表 II 把数十种方法填进这张表。**(4) 评测与解释**:讨论基准构造与 AUC/AP 的利弊;在 MNIST-C(15 种腐蚀)与 MVTec-AD(15 类工业缺陷)上统一比较 9 种模型(Gaussian、MVE、PCA、KDE、SVDD、kPCA、AGAN、DOCC、AE);用 LRP / "neuralization" 解释异常预测。**(5) 两个实操示例**:Thyroid(OC-SVM)与 MVTec 'wood'(KDE 的 Clever Hans)。

## 方法谱系
这是综述,覆盖七大范式里的前三类主干:**重建/生成式**、**密度/单类**(以及作为单类负样本的**合成异常/辅助异常**,如 Outlier Exposure);并在"连接鲁棒性研究"一节把**基于分类器的 OOD 检测**、校准、拒识与不确定性估计明确归为同一问题(OOD 检测在形式上就是"x 是否落在 P⁺ 高密度区之外")。它不涉及 conformal 与跨模态一致性。它的作用是**谱系地图本身**:例如表 II 指出核 SVDD 与 Deep SVDD 共享超球模型,因此半监督、多超球等扩展可以在浅层与深度之间迁移;深度自编码器在输入空间算重建误差,而核 PCA 在特征空间算 —— 由此提示"在神经特征空间里算重建误差"(后来的 feature-reconstruction 方法)。AnoGAN 被归为"把 GAN 生成器当随机解码器、latent 搜索当隐式编码"的重建方法,f-AnoGAN 等加了显式编码器。同组后续把这套框架带到病理:histo-nejmai-2024(Ruff、Müller 等)系统比较了基础模型特征 + kNN、one-class 微调与 Outlier Exposure。

## 数据
综述自身的实验:**MNIST-C**(在标准 MNIST 训练集上训练,对 15 种腐蚀分别测试,AUC 区分腐蚀/未腐蚀测试集)、**MVTec-AD**(15 类,每类单独训练)、**Thyroid**(ODDS 库,n=3,772,D=6 个实值特征,93 个异常约 2.5%,60:10:30 划分并保持异常比例)。训练细节见附录 B:例如 DOCC 在 VGG16(MVTec-AD)或 EMNIST 字母分类 CNN(MNIST-C)第一个全连接层表示上做白化;AGAN 复用 AE 的编码器/解码器作为判别器/生成器。附录 D 列有开源软件、教程与 demo。

## 主要结果
**(1) 异质性**:不同方法在不同腐蚀和缺陷类别上表现差异巨大。例如 AGAN 在 MNIST-C 上普遍不错,却在 MVTec-AD 上被 DOCC 系统性超过;更强的非线性模型并非每类都更好,简单浅层模型偶尔胜出。MVTec-AD 表 V 中的极端例子:'screw' 类 SVDD 仅 **8.6**、AGAN **99.6**、DOCC 86.9;'carpet' 类 DOCC 90.6、KDE 34.8;'wood' 类 KDE **94.7**(9 种模型中最高)。**(2) Clever Hans**:对 'wood' 上 KDE 的 LRP 解释显示,它的高相关性落在**木纹竖条**而不是真实缺陷(液体污渍)上 —— 高 AUC 来自测试集里条纹与异常的虚假相关。把高斯核换成相当于水平方向模糊的 **Mahalanobis 核**后,解释与真实缺陷的平均余弦相似度从 **0.34 升到 0.38**,AUC 则**降到 87%**,作者认为后者才是更真实的泛化估计。改进策略:数据扩充(补齐打破虚假相关的样本)、模型扩展(更灵活的模型或加结构/正则)、集成。**(3) Thyroid 示例**:先根据风险设 ν=0.15(倾向零漏报,并对约 2.5% 的训练污染更稳健);未做特征缩放时验证 AUC 仅 **83.9%**,改用基于中位数与四分位距的**稳健缩放**(只用训练集统计量)后验证 AUC **98.6%**,测试 AUC **99.2%**、误报率 **14.8%**(接近预设 ν)、漏报率 **0**。**(4) 比较性结论**:概率与重建方法给出连续排序、还能给正常样本排序;单类方法通常不给正常样本排序,但**样本效率更高、对正常数据的非代表性采样更稳健**。**(5) 开放问题**:未探索的建模维度组合;把 OOD 检测、校准、不确定性、对抗鲁棒性与异常检测打通;可解释与可信;**需要更多困难、开放的数据集**(作者点名 MVTec-AD 与 Medical Out-of-Distribution Analysis Challenge 是好例子,并批评主流基准只是重用分类数据集、偏向展示新方法的优点而忽略失败模式);弱监督与自监督;理论基础。

## 创新点
- 给出异常检测的概率形式化定义,区分 anomaly / outlier / novelty,并把"集中性假设"、污染率 η 与异常分布先验 P⁻ 这些常被隐含的假设显式化。
- 五维统一框架(损失、模型、特征映射、正则、推断)+ 表 II,把浅层与深度方法放在同一张表里,并据此提出可迁移的改进方向。
- 新增"低层感官 vs 高层语义"异常类型,解释为什么深度特征并不总是更好。
- 把 XAI(LRP / neuralization)引入异常检测评估,用 Clever Hans 示例说明"高 AUC ≠ 正确的决策依据"。
- 带实操建议的完整示例(风险评估 → ν 设定 → 稳健缩放 → 解释 → 修正)。

## 局限
- 作者自承包含了不少自己组的工作(Deep SVDD、Deep SAD 等),视角可能偏向单类与核方法。
- 写于 2020 年:不覆盖之后在工业异常检测里占主导的**预训练特征 + memory bank**(PaDiM、PatchCore)、流模型 CFLOW、合成异常 DRAEM、扩散异常检测与 conformal 校准等。
- 统一实验规模有限(9 个模型、MNIST-C 与 MVTec-AD),没有生物医学组学数据;医学只作为动机与 Thyroid 小例子出现。
- 统一框架聚焦带损失函数的方法,距离类方法只简要归组。

## 与本研究方向的关系
这是伪影注入课题的**理论底稿**:几乎每一个伪影注入课题要回答的问题,在这里都有对应的形式化名称。**把定义翻译到肾脏组学**:样本 = snRNA/snATAC 细胞、Xenium 细胞、Visium spot 或 H&E 图块;P⁺ = KPMP/HuBMAP 健康参考所代表的正常分布;特征映射 φ = 原始计数、scVI latent 或 H&E 基础模型嵌入(D3 维度);模型族 = 密度(Mahalanobis/flow)、单类(Deep SVDD)或重建(AE/f-AnoGAN/扩散)。**哪些假设会断,以及综述里对应的术语**:(1) **污染** P = (1−η)P⁺ + ηP⁻:"健康"参考里混着 doublet、ambient RNA 主导的细胞和 Xenium 分割/溢出错误的细胞(见 xenium-split、ovrlpy);综述的 Thyroid 示例给出了处理方式——用 ν 写入污染先验、用中位数/四分位距的稳健缩放。(2) **非代表性采样**:健康供肾的年龄、性别、中心分布与患者不同;综述指出单类方法对此更稳健,这是选择 Deep SVDD 类打分的理论依据。(3) **上下文异常**:同一表达谱在皮质是正常、在髓质是异常 —— 应建模 p⁺(x | 空间位置/细胞类型),这正是空间组学异常需要的条件分布;Sardine 的"空间局部密度比较"就是此类条件化的一个实现。(4) **群体异常**:单个细胞都正常、但一个区域的细胞组成异常(如免疫浸润的 niche)——需要 niche/区域级样本而不是细胞级。(5) **低层 vs 高层异常**:染色差异、组织折叠是"低层感官异常",肾小球硬化是"高层语义异常";不同特征映射会偏向其中一种,这直接解释了为什么伪影注入课题需要跨模态。(6) **Clever Hans**:这是伪影注入课题最需要警惕的失败模式——如果患者样本与健康样本来自不同中心或批次,任何检测器都可能靠批次签名拿到高 AUC;综述的处方(用解释检查决策依据、补齐打破虚假相关的样本、报告修正后的更低 AUC)应写进 KidneyAnomalyBench 的协议。**跨模态一致性**可以看作把"解释与真实缺陷是否一致"推广为"两个模态的异常图是否一致":H&E 与表达的异常同时出现才算疾病,单模态异常提示伪影。**与 Agent 可信度课题的关系**:综述"把 OOD、校准、拒识、不确定性视为同一问题"的论述,正是 Agent 可信度课题校准验证器与 rerun 稳定性的概念基础;"高 AUC 可能是 Clever Hans"也直接对应"agent 结论正确但证据不对"的失败类型。**仓库里已有的相关工作**:同组的 histo-nejmai-2024 把单类与 Outlier Exposure 带到临床病理;MedIAnomaly 与 pathology-ad-bench-mlhealth-2025 在医学影像和病理上做了综述呼吁的"多范式统一基准",并同样发现不同家族表现高度异质;MEATRD 在空间转录组上组合了重建(D2)与 Deep-SVDD 式单类打分 —— 正是综述所说"未探索的建模维度组合"的一个实例。

## 可复用资产
- **框架:** 表 II(五维建模表)可直接当伪影注入课题方法选型与论文"相关工作"的组织骨架。
- **评测协议:** MNIST-C / MVTec-AD 统一对比的做法(三族 × 三种特征映射)与 AUC + AP(附录 A)双指标;Clever Hans 检查流程(解释 → 与真实缺陷比对 → 修正 → 报告修正后指标)。
- **实操清单:** 先评估误报与漏报的不对称风险、用 ν 写入污染先验、只用训练集统计量做稳健特征缩放。
- **软件:** 附录 D 汇总的开源实现、教程与 demo。

## 待读
- Deep SVDD(本仓库 deep-svdd-icml-2018)与 Deep SAD(半监督扩展)。
- Outlier Exposure(Hendrycks 等)与本轮的 OOD 系列(msp-ood-iclr-2017、mahalanobis-ood-neurips-2018、energy-ood-neurips-2020、generalized-ood-survey-ijcv-2024)。
- 综述之后的工业范式:padim-icpr-2020、patchcore-cvpr-2022、draem-iccv-2021、cflow-ad-wacv-2022;以及 mvtec-ad-cvpr-2019 数据集原文。
- Medical Out-of-Distribution Analysis Challenge(综述点名的医学开放基准)。

## 引用
```bibtex
@article{Ruff2020_200911732,
  title = {A Unifying Review of Deep and Shallow Anomaly Detection},
  author = {Ruff, Lukas and Kauffmann, Jacob R. and Vandermeulen, Robert A. and Montavon, Gr{\'e}goire and Samek, Wojciech and Kloft, Marius and Dietterich, Thomas G. and M{\"u}ller, Klaus-Robert},
  journal = {Proceedings of the IEEE},
  volume = {109},
  number = {5},
  pages = {756--795},
  year = {2021},
  doi = {10.1109/JPROC.2021.3052449},
  eprint = {2009.11732},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2009.11732}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
