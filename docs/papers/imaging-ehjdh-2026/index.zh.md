# An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study

> **文献键** `Raikhelkar_2026` · **来源** European Heart Journal - Digital Health(2026) · **类别** imaging · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1093/ehjdh/ztag088> · `status: complete`

---

## 一句话
用 GenerateCT 的 CT-ViT 编码器(3D vision transformer)从为其他原因拍的常规、非门控、非增强胸部 CT 判断左室射血分数(LVEF)是否 <50%;在开发医院(Columbia)AUROC 0.786、外部医院(Weill Cornell)0.762,作为心衰的机会性筛查(Abstract)。

## 要点
- 标签来自 CT 前后 6 个月内的超声心动图报告里的 EF 值,按 50% 二值化;不需要额外检查(Methods §Data curation, §LVEF-based classification)。
- 只用人口学 + CT 报告里 260 个 ICD-9 诊断码的 XGBoost 基线 AUROC 只有 0.607 / 0.592,说明信号主要来自图像本身(Table 6)。
- CT 与超声间隔越近,AUROC 越高:Columbia ≤1 天子集 0.800 vs 全体 0.786(Holm 校正 P=0.004)(Table 5, Results)。
- 在 90 / 100 张抽样 CT 上,模型加权 F1 0.808 / 0.797,两位胸部放射科医生 0.646、0.802 / 0.623(Table 7)。
- 在时间上更晚的"独立连续测试集"上 AUROC 降到 0.742(Columbia)/ 0.735(Weill Cornell),balanced accuracy 只有约 0.57(Results)。

## 研究问题
心衰全球超过 6,400 万患者;很多早期收缩功能障碍(HFrEF / HFmrEF)患者没有症状、未被诊断,错过了能减缓进展的指南导向药物治疗(GDMT)(Introduction)。EF 通常要靠超声心动图、心脏 MRI 等专门检查测量(Discussion);美国每年做超过 8,000 万次 CT,胸部 CT 很常见(Introduction)。已有 AI 研究用 CT 预测心血管不良事件风险(如量化冠脉钙化、左房容积、左室质量指数;Introduction, Discussion),但作者称从非门控、非增强胸部 CT 计算 EF 此前没有人做过(Discussion)。问题:能否从这些"顺带"拍的非门控(不与心跳同步)、非增强胸部 CT 中直接筛出 EF 降低的患者?

## 方法
1. **配对数据**:找出 2005-07 至 2023-08 在 Columbia(CU)或 Weill Cornell(WCM)做过非增强胸部 CT、且 CT 前后 6 个月内有超声心动图的成人;经筛选和链接得到 19,410 名患者的 34,058 对 CT–超声(Methods §Data curation)。
2. **标签**:超声报告里的 LVEF(2D 超声,按瀑布逻辑取值),<50% 为阳性(EF 降低),≥50% 为正常(Methods §LVEF-based classification)。
3. **划分**:CU 用于开发,按病人随机分训练/验证/保留测试集(测试集 n=5,174,20%);WCM 全部用作外部验证;另外各建一个时间上更晚的独立连续测试集(CU 2023-08 至 12,WCM 2023-08 至 2024-07)(Methods, Results)。
4. **CT 预处理**:DICOM 换算成 Hounsfield 单位,窗宽 [−1000, 1000] HU 去掉空气和骨;OTSU 阈值聚焦人体区域;样条插值重采样到 2×2×2 mm³;裁剪/补零到 164×164×164(Methods §3D preprocessing)。
5. **模型**:GenerateCT 的 CT-ViT 编码器作骨干(先 4 个在轴位平面上做空间注意力的 block,再 4 个沿 z 轴切片做注意力的 block),输出 512 维向量,接全连接分类头输出"低 EF"概率;训练时随机裁到 164×144×144 并水平翻转,测试时中心裁剪(Methods §AI model, §Grad-CAM)。
6. **训练**:二元交叉熵,AdamW,学习率 1×10⁻⁵,权重衰减 1×10⁻⁴,batch 8,20 个 epoch,第 15 个 epoch 学习率减半;用 5 个随机种子重复训练,报告均值 ± 标准差;单张 A100(Methods §AI model)。
7. **评估**:AUROC、F1、balanced accuracy;Brier 分数与校准曲线;按性别、年龄、种族和 CT–超声间隔分组;决策曲线分析;与两位胸部放射科医生在抽样 CT 上比较,并用 McNemar 检验;Grad-CAM 显著性图做可解释性(Methods §Evaluation, §Comparison with radiologist)。
8. **机会性筛查演示**:对 633 个没有配对超声的常规胸部 CT 运行模型,再查阅被标记患者的病历(Results §Opportunistic screening)。

## 方法图
```mermaid
flowchart LR
  A["Non-contrast chest CT<br/>non-gated"] --> B["Preprocess<br/>HU window, 2 mm, 164 cube"]
  C["Echo report within 6 months<br/>LVEF below 50 = positive"] --> D
  B --> D["CT-ViT encoder<br/>spatial + slice attention"]
  D --> E["512-d feature<br/>FC head, BCE"]
  E --> F["P of low EF"]
  F --> G["Evaluate<br/>CU test, WCM external, later cohorts"]
  F --> H["Grad-CAM<br/>saliency maps"]
```

## 数据
共 34,058 对 CT–超声、19,410 名患者:CU 14,083 名患者 / 25,948 对(正常 21,787,EF 降低 4,161,即 16.04%),WCM 5,327 名患者 / 8,110 对(正常 6,695,EF 降低 1,415,17.29%)(Methods, Table 1)。CT–超声间隔中位数 12.7–24.2 天(回顾队列),≤1 天的占 11.8–20.7%(Table 4)。独立连续测试集:CU 1,251 名患者 / 1,411 对,WCM 755 名患者 / 817 对(Results)。机会性筛查:633 个 CT / 627 名患者(Results)。数据因机构政策与伦理审批不公开,可向通讯作者合理申请(Data availability)。

## 主要结果

- **CU 保留测试集**:AUROC 0.786 ± 0.005(95% CI 0.780–0.792),F1 0.822 ± 0.005(n=5,174)(Results §AI model evaluation, Fig. 4)。
- **WCM 外部验证**:AUROC 0.762 ± 0.007(0.753–0.771),F1 0.812 ± 0.005(Results §External validation)。
- **校准**:Brier 分数 CU 0.1120 ± 0.0025(5 个种子),WCM 0.1199 ± 0.0022(Results, Fig. 7)。
- **基线**:人口学 + 260 个 ICD-9 码的随机森林 AUROC 0.538 / 0.550,XGBoost 0.607 / 0.592(CU / WCM)(Table 6)。
- **CT–超声间隔**:CU ≤1 天 0.800 vs 全体 0.786(Holm P=0.004);WCM ≤1 月 0.788 vs 0.762(Holm P=0.002)(Table 5, Results)。
- **亚组**:18–39 岁最差(CU 0.696),性别和年龄间差异显著(CU 置换 ANOVA P=0.0018、0.0008),种族间不显著(P=0.4463)(Table 5, Results)。
- **与放射科医生**:CU 90 张 CT 加权 F1:模型 0.808,RAD1 0.646,RAD2 0.802;WCM 100 张:模型 0.797,RAD2 0.623(Table 7)。错误数 CU:模型 13、RAD1 37、RAD2 18;WCM:模型 15、RAD2 43(Results)。速度:模型约 1 分钟处理完全部 90(或 100)张,放射科医生约 2–2.2 分钟/张(Results)。作者注明这一比较用的是单个选定模型,可能略偏乐观(Results)。
- **时间上更晚的测试集**:CU AUROC 0.742(0.729–0.755)、balanced accuracy 0.571;WCM AUROC 0.735(0.701–0.770)、balanced accuracy 0.563(Results)。
- **Grad-CAM**:在 51 例 EF 降低患者上由医学物理师检查,高亮区域包括心脏增大、升主动脉(尤其钙化时)、上腔静脉扩张、起搏器及导线、肺水肿浸润,以及背部皮下组织密度增高、胸骨钢丝、颈部中心静脉置管瘢痕(Results §Model interpretability)。
- **机会性筛查**:633 个 CT 中模型标记 23 名(3.7%),病历核查 18/23(78%)确为 EF 降低并有心衰诊断(Results §Opportunistic screening)。

## 创新点
- 作者称是首个从常规非门控、非增强胸部 CT 识别 EF 降低的研究(Discussion)。
- 双中心、大规模配对数据,外加时间上更晚的独立测试集、校准与决策曲线分析(Results)。
- 与放射科医生的盲法对照和误差重叠分析(Table 7, Fig. 6)。

## 局限
- 作者:回顾性研究,计划做前瞻性研究(Discussion)。
- 作者:2D 超声测 EF 的观察者内/间差异分别为 8–21% 和 6–13%;报告中未统一记录测量方法(Simpson 双平面、单平面或目测);CT 与超声之间 EF 可能因治疗而变化,标签有噪声(Discussion)。
- 作者:只用了非增强 CT;Grad-CAM 只能做个例的定性解释,缺少群体层面的可解释性(因为不同 CT 之间没有体素级配准);没有系统研究伪影/低质量扫描的影响(Discussion)。
- 我们的理解:Grad-CAM 高亮的起搏器、胸骨钢丝、颈部置管瘢痕都是"既往治疗的痕迹",模型可能部分在识别"已经被诊断和治疗过的病人",这对筛查"未诊断"人群的价值打了折扣。
- 我们的理解:时间上更晚的两个独立连续测试集上 balanced accuracy 只有 0.571 / 0.563(F1 却为 0.809 / 0.825),说明在默认阈值下对阳性类的召回偏低,F1 很可能主要由占多数(约 83%)的正常类撑起(与放射科医生比较时文中明确用的是加权 F1;主结果的 F1 类型未写明);保留测试集的 balanced accuracy 只在 Fig. 4C 中给出。作者在 Discussion 中另选了一个优先特异度的阈值:CU 特异度 80% 时灵敏度 64%。

## 与本研究方向的关系
我们的理解:这是有监督分类,不是无监督异常检测;它在 detect → model → revert 里只和 **detect** 有间接关系。对课题 1 的启发有三点。(1) **机会性利用已有数据**:用为其他目的采集的影像去发现未标注的疾病信号,和我们想从常规 H&E / 空间组学中检出疾病区域的思路相近。(2) **"捷径特征"的警示**:Grad-CAM 显示模型会用起搏器、手术钢丝、置管瘢痕等治疗痕迹做判断——在肾脏数据里,类似的捷径可能是活检针道、制片伪影或特定医院的染色风格,这正是课题 1 想用跨模态一致性排除的东西。(3) **评估设计可借鉴**:按时间先后的独立测试集、按采集条件(此处是 CT–超声间隔)分层、与朴素临床特征基线(ICD 码)比较、与专家做盲法对照,这些都适合写进 KidneyAnomalyBench 的评测协议。不涉及 virtual tissue 或 revert。

## 可复用资产
- **代码与权重**:文中称上线发表后在 GitHub 公开预处理、训练、评估代码和训练好的权重(Code and model weight availability);仓库已存在;截至 2026-10-27,仓库中只有代码(main.py、archs.py、transformer.py、预处理脚本与 notebook、README.txt),没有训练好的权重文件。
<https://github.com/ZB-WCM/AI_CT_LVEF>
- **骨干**:GenerateCT 的 CT-ViT 编码器(3D CT 的空间 + 切片注意力结构)(Methods)。
- **预处理规范**:HU 窗 [−1000, 1000]、2 mm 各向同性、164³ 体积(Methods)。
- **数据**:不公开,可向通讯作者申请(Data availability)。

## 待读
- GenerateCT / CT-ViT 原论文:编码器的预训练数据与方式。
- 补充材料 Table S5–S6:3/4 分类和 40%、35% 阈值下的表现。
- 同类工作(ECG 或胸片预测 EF),比较机会性筛查的不同模态。

## 图表

本文为开放获取(CC BY),全文与图表见 PMC 与 OUP 文章页;本卡未下载图片,只按原文编号列出。
<https://pmc.ncbi.nlm.nih.gov/articles/PMC13322390/> · <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677>

**图1**:数据整理与预处理流程——Columbia 与 Weill Cornell 的超声报告与胸部 CT 的筛选、排除与预处理。见 <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F1>

**图2**(方法总览):分析 3D 胸部 CT 并预测左室收缩功能障碍的 vision transformer 结构示意。见 <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F2>

**图4**(主结果):两个中心的 ROC 曲线与 AUROC、按人口学亚组的指标、混淆矩阵。见 <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F4>

**图5**(可解释性):叠加在轴位 CT 上的 Grad-CAM 显著性图,4 例 EF 降低患者。见 <https://academic.oup.com/ehjdh/article/7/6/ztag088/8705677#F5>

_其余:图3 研究设计 · 图6 模型与放射科医生的误差 Venn 图 · 图7 校准曲线 · 图8 决策曲线;表1 人群 · 表2 采集参数 · 表3 诊断码 · 表4 CT–超声间隔 · 表5 亚组 AUROC · 表6 RF/XGBoost 基线 · 表7 与放射科医生的 F1 · 表8 超声操作者与数据来源。(注:正文的图号与图注不一致:Grad-CAM 示例被引作"Figure 6A–D"(图注为图5),校准曲线被引作"Figure 5"(图注为图7),Venn 图被引作"Figure 7"(图注为图6);本卡按图注编号。)_

### 结果表

**表1.** 主要数字(PMC 全文;均值 ± 标准差为 5 个随机种子)。

| Cohort | n pairs | AUROC | F1 | Source |
|---|---|---|---|---|
| CU hold-out test | 5,174 | 0.786 ± 0.005 | 0.822 ± 0.005 | AUROC Table 5; F1 Results |
| WCM external validation | 8,110 | 0.762 ± 0.007 | 0.812 ± 0.005 | AUROC Table 5; F1 Results |
| CU independent consecutive | 1,411 | 0.742 | 0.809 | Results |
| WCM independent consecutive | 817 | 0.735 | 0.825 | Results |
| XGBoost baseline (CU / WCM) | — | 0.607 / 0.592 | 0.309 / 0.312 | Table 6 |

## 引用
```bibtex
@article{Raikhelkar_2026, title={An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study}, volume={7}, ISSN={2634-3916}, url={http://dx.doi.org/10.1093/ehjdh/ztag088}, DOI={10.1093/ehjdh/ztag088}, number={6}, journal={European Heart Journal - Digital Health}, publisher={Oxford University Press (OUP)}, author={Raikhelkar, Jayant and Bai, Zilong and Beecy, Ashley N and Richter, Ilan and Liu, Fengbei and Nizam, Nusrat Binta and Kishore, Varsha and Kelsey, Chris and vanMaanen, David and Ruhl, Jeffrey and Tesfuzigta, Naomi and Lancet, Erica and Leb, Jay and Legasto, Alan and Elias, Pierre and Poterucha, Timothy and Kumaraiah, Deepa and Prince, Martin and Wang, Fei and Sayer, Gabriel and Estrin, Deborah and Sabuncu, Mert and Uriel, Nir}, year={2026}, month=jun }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
