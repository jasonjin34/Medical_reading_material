# Pathology-Informed Latent Diffusion Model for Anomaly Detection in Lymph Node Metastasis

> **Bibkey** `histo-miccai-2025` · **Venue** MICCAI 2025 (2025) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://papers.miccai.org/miccai-2025/0675-Paper2270.html>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
AnoPILaD:用病理关键词提示(CONCH 视觉-语言模型选词)引导潜空间扩散模型(Stable Diffusion v1.5 + LoRA)重建"正常样"淋巴结组织,再以重建差异作为异常分数,实现无监督的转移灶检测。

## 研究问题 / Problem
数字病理中监督式转移灶检测依赖大量标注,而标注稀缺且昂贵。无监督异常检测只用正常(in-distribution)样本训练即可发现偏离正常分布的转移灶,但现有基于 DDPM 的方法(如 AnoDDPM)重建能力不足,对正常/异常分布区分度低,产生大量假阳性。本文要提升无监督重建式异常检测在淋巴结病理上的判别力与跨器官鲁棒性。

## 方法 / Method
核心是"病理知识提示 + 潜空间扩散重建"。(1) 骨干为 Stable Diffusion v1.5 的 LDM,用 LoRA(秩=4,lr=1e-5,batch=64)仅在正常 patch 上微调,学习正常组织的潜空间表示;训练目标为条件去噪损失 `L = E‖ε − ε_θ(z_t, t, c)‖²`,c 为文本条件。(2) 权重提示生成:从文献收集 74 个描述正常淋巴结细胞/微环境的病理关键词(经病理医师审核);推理时用 CONCH(在 117 万病理图文对上预训练的 VLM)的图像/文本编码器算余弦相似度,取 top-5 关键词,相似度除以中位数归一化得权重,经 Compel 库转成加权文本嵌入送入 LDM。(3) 异常评分沿用 AnoDDPM:对输入部分加噪到时间步 t(选定 t=674),在文本条件引导下反向去噪重建 ẑ₀ ∼ p_θ(z₀|z_{1:t}, c),输入与重建的差异即异常分数——正常样本差异小、转移样本差异大。推理用 PLMS 采样、100 步。

## 数据 / Data
两套淋巴结全切片(WSI,20× 放大,256×256 patch)。(1) 本地医院 (LH) 胃淋巴结:808 张 WSI(751 正常 / 57 转移,部分标注),训练 643 正常 WSI(1,373,475 patch),验证 50,in-distribution 测试 58,OOD 测试 57(转移);patch 级 base prevalence ≈0.40(patch)/0.50(WSI)。(2) 公开 Camelyon16 (C16) 乳腺淋巴结用于跨域独立测试:32 正常验证 / 80 正常 in-dist 测试 / 49 转移 OOD(其中 22 张肿瘤簇 >2mm,记为 C16 Macro);patch 级 OOD 55,659,prevalence ≈0.19。LH 所有肿瘤区 >2mm。

## 主要结果 / Key results
Patch 级异常检测(Table 2):AnoPILaD 全面领先。LH 上 AUC 0.9587 / AUPR 0.9499(次优 MemAE 0.9290/0.8886,AnoDDPM 仅 0.8555/0.7841);跨域 C16 上 AUC 0.8884 / AUPR 0.6987,比 AE/MemAE(约 0.66 AUC)高出约 0.22 AUC,显示强跨器官鲁棒性。WSI 级(Table 3):分类 AnoPILaD 在 LH 达 AUC 0.9943 / AUPR 0.9948(Z99),C16 0.6745(Zmax),C16 Macro AUC 0.8062——其余模型 Macro 上仅约 0.5–0.6。分割上 AnoPILaD 在所有场景 DICE/IoU/TNR 最高(C16 Macro DICE 0.5420 vs AnoDDPM 0.3131),而 AE/MemAE 分类尚可但分割极差(热图对全片打分近似均匀,定位能力弱)。定性上文本引导让 OOD 重建出更均匀的淋巴细胞排列、抑制多形核与纤维化,拉大正常/异常边界。

## 创新点 / Contributions
- 首次将病理专用 VLM(CONCH)与潜空间扩散重建结合用于病理异常检测,用**正常组织关键词**作为文本条件引导重建方向。
- 提出"加权提示生成":74 个病理医师审核的正常关键词 + CONCH 相似度 top-5 + 中位数归一化权重 + Compel 加权嵌入。
- 系统评测跨器官域偏移(胃→乳腺),证明文本引导显著提升鲁棒性;并强调分割(定位)而非仅分类才是异常检测的关键评价。

## 局限 / Limitations
- 跨域性能仍大幅下降(C16 WSI AUC 从 LH 的 ~0.99 掉到 ~0.67),绝对分割 DICE 偏低(C16 Macro 0.54),离临床可用尚有距离。
- 关键词池靠人工从文献收集且面向淋巴结,迁移到其他器官需重建词表;未做提示词数量/来源的消融。
- 仅两器官、单一(部分为本地私有)数据集验证;重建时间步 t=674 依赖 LH 验证集调参,可能过拟合该分布。

## 与本研究方向的关系 / Relation to our direction
直接落在我们 pipeline 的**第一环:anomaly detection**,而且几乎是理想模板——用生成式模型只在"正常"组织上建模,把疾病(转移)区域当作偏离正常分布的 OOD 来检测并**定位**(z-score 热图 + 分割),这正是"检测因疾病/扰动而改变的区域"。其"重建成正常样 + 差异即异常"的思路,可视为**virtual tissue(虚拟正常组织)**在像素/潜空间层面的雏形:模型把异常样本"revert"回正常形态,差异图直接给出扰动位置——与我们"把异常 revert 回正常"的目标同构,只是发生在图像域而非基因域。可迁移的机制:(1) 用病理/组学 foundation model 的文本或先验条件去引导生成,把"正常态"知识注入重建;(2) CONCH 关键词加权提示的做法可类比到 spatial-omics 上——用 marker/pathway 词表条件化虚拟组织生成。它不涉及基因层的 revert 预测(第三环),但为"如何客观定义并定位异常"提供了可复用的评测范式(patch/WSI 级 AUC/AUPR + DICE/IoU/TNR)。

## 可复用资产 / Reusable assets

- **代码**:<https://github.com/QuIIL/AnoPILaD>(MIT 许可)。含 `image_caption.py`(CONCH 生成/选词)、`train_text_to_image_lora.py`(LoRA 微调 SD v1.5)、`rec_generate.py`(重建+异常评分)。依赖 HuggingFace `diffusers`、CONCH、`compel`、CFG++ solver;`conda python=3.11`。
- **无发布 checkpoint**:README 未提供预训练权重下载,需自行在正常数据上微调。
- **数据**:Camelyon16 (C16) 公开可复现跨域实验;LH 胃淋巴结为本地私有,不公开。
- **评测协议(可直接借用)**:patch 级 z-score → AUC/AUPR;WSI 级用 Zmax 与 Z99(99 分位)两种打分 + 形态学腐蚀(2×2);分割用 DICE/IoU(OOD)与 TNR(in-dist),阈值 0;FID 选扩散模型 checkpoint。
- **关键词资产**:74 个正常淋巴结病理关键词表 + top-5/median 归一化加权提示流程。

## 待读 / Follow-ups
- AnoDDPM(Wyatt 2022)与 Linmans 2024《Diffusion models for OOD detection in digital pathology》(Med Image Anal 93:103088)——本文直接基线与病理 DDPM 前身。
- CONCH(Lu 2023, arXiv:2307.12914)——病理 VLM 基础,评估其嵌入能否用于 spatial-omics 条件化。
- Compel 加权提示嵌入实现细节;能否把关键词权重换成基因/marker 表达权重。

## 引用 / Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
