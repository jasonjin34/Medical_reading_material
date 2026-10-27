---
hide:
  - toc
---

# 知识图谱

每个视图是一张独立的图。组默认折叠：点击组展开，点击节点只看它的邻居，双击论文打开精读。

## 方法图

行是异常检测的方法范式，列从通用数据一直到肾脏组学。箭头表示方法被迁移到哪里；虚线格是课题 1 要补的空白。 [全屏打开 ↗](maps/matrix.html?lang=zh){target=_blank}

<iframe src="../../maps/matrix.html?lang=zh&embed=1" style="width:100%;height:760px;border:1px solid var(--md-default-fg-color--lightest);border-radius:6px" loading="lazy"></iframe>

## 按阅读清单的视图

| 视图 | 论文 | 概念 |
| --- | --- | --- |
| [课题 1:肾脏单细胞组学异常检测基准 ↗](maps/viewer.html?view=plan-a&lang=zh){target=_blank} — 从健康数据学习正常肾脏，再标出它解释不了的细胞和区域；用一个模态作为另一个模态的证据。 | 61 | 20 |
| [课题 2:生物医学分析 agent 的结论核查 ↗](maps/viewer.html?view=plan-b&lang=zh){target=_blank} — 把 agent 的每条结论追溯到代码和数据；用专家标注校准核查器。 | 50 | 18 |
| [桥：多个课题共用的论文 ↗](maps/viewer.html?view=bridge&lang=zh){target=_blank} — 不止一个研究课题要用到的论文。 | 6 | 17 |
| [核心阅读清单 ↗](maps/viewer.html?view=reading-list&lang=zh){target=_blank} — 核心背景阅读，按 detect → model → revert 排列。 | 32 | 7 |
| [电子病历与患者轨迹 ↗](maps/viewer.html?view=ehr&lang=zh){target=_blank} — Mount Sinai 电子病历项目的论文。 | 5 | 0 |
| [总览：全部论文 ↗](maps/viewer.html?view=overview&lang=zh){target=_blank} — 全部论文按分类聚在一起，只用来看轮廓；细读请用上面的视图。 | 123 | 0 |

## 流程图

每个课题从左到右画成一条流程。每一步列出它的必读论文；点“在图谱中打开”可在图谱里查看这一步。

<style>
.kmflow { display: flex; align-items: stretch; overflow-x: auto; padding: 2px 0 10px; margin: 0.4em 0 1.4em; }
.kmstep { flex: 1 1 0; min-width: 6.5rem; border: 1px solid var(--md-default-fg-color--lightest);
  border-top: 3px solid var(--md-accent-fg-color); border-radius: 6px; padding: 0.55em 0.7em 0.6em;
  background: var(--md-code-bg-color); font-size: 0.7rem; line-height: 1.4; display: flex; flex-direction: column; }
.kmstep .kmnum { font-size: 0.62rem; font-weight: 700; color: var(--md-default-fg-color--light); letter-spacing: 0.04em; }
.kmstep .kmtitle { font-weight: 700; font-size: 0.76rem; margin: 0.1em 0 0.35em; }
.kmstep ul { list-style: none; margin: 0 0 0.4em !important; padding: 0 !important; }
.kmstep li { margin: 0 0 0.15em !important; }
.kmstep .kmopen { margin-top: auto; font-size: 0.64rem; }
.kmarrow { align-self: center; flex: 0 0 auto; padding: 0 0.12em; color: var(--md-default-fg-color--light); font-size: 0.9rem; }
</style>

### 课题 1:肾脏单细胞组学异常检测基准

<div class="kmflow"><div class="kmstep"><div class="kmnum">第 1 步 · 8 篇</div><div class="kmtitle">公开肾脏图谱</div><ul><li><a href="../papers/damage-scores-cellgenomics-2026/">Damage scores</a></li><li><a href="../papers/dkd-spatial-atlas-nature-2026/">DKD spatial atlas</a></li><li><a href="../papers/cellspectra-natgenet-2025/">CellSpectra</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-a&amp;lang=zh&amp;focus=group:A1" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 2 步 · 9 篇</div><div class="kmtitle">质控与去伪影</div><ul><li><a href="../papers/ovrlpy-natbiotech-2026/">ovrlpy</a></li><li><a href="../papers/resolvi-natmethods-2026/">ResolVI</a></li><li><a href="../papers/xenium-split-natmethods-2026/">Xenium contamination (SPLIT)</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-a&amp;lang=zh&amp;focus=group:A2" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 3 步 · 7 篇</div><div class="kmtitle">健康组织模型</div><ul><li><a href="../papers/pathbench-natcommun-2026/">Pathology FM benchmark</a></li><li><a href="../papers/linear-baselines-natmethods-2025/">Linear baselines win</a></li><li><a href="../papers/nephrobase-biorxiv-2025/">Nephrobase Cell+</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-a&amp;lang=zh&amp;focus=group:A5" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 4 步 · 25 篇</div><div class="kmtitle">异常 / OOD 打分</div><ul><li><a href="../papers/meatrd-aaai-2025/">MEATRD</a></li><li><a href="../papers/refmap-eval-biorxiv-2025/">Reference-mapping QC</a></li><li><a href="../papers/sardine-bioinformatics-2025/">Sardine</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-a&amp;lang=zh&amp;focus=group:A3" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 5 步 · 5 篇</div><div class="kmtitle">跨模态验证</div><ul><li><a href="../papers/kidney-multimodal-genomebiol-2026/">Kidney multiome (mBDRC)</a></li><li><a href="../papers/loki-omiclip-natmethods-2025/">Loki / OmiCLIP</a></li><li><a href="../papers/he2expr-bench-natcommun-2025/">H&amp;E→expression benchmark</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-a&amp;lang=zh&amp;focus=group:A4" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 6 步 · 7 篇</div><div class="kmtitle">对照专家评测</div><ul><li><a href="../papers/nih-kidney-ai-challenge-2026/">NIH Kidney AI Challenge</a></li><li><a href="../papers/pathology-ad-bench-mlhealth-2025/">Pathology AD benchmark</a></li><li><a href="../papers/histo-nejmai-2024/">Clinical-grade histo AD</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-a&amp;lang=zh&amp;focus=group:A6" target="_blank" rel="noopener">在图谱中打开 ↗</a></div></div>

### 课题 2:生物医学分析 agent 的结论核查

<div class="kmflow"><div class="kmstep"><div class="kmnum">第 1 步 · 16 篇</div><div class="kmtitle">agent 执行分析</div><ul><li><a href="../papers/co-scientist-nature-2026/">Co-Scientist</a></li><li><a href="../papers/deepevidence-natmachintell-2026/">DeepEvidence</a></li><li><a href="../papers/robin-nature-2026/">Robin</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-b&amp;lang=zh&amp;focus=group:B1" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 2 步 · 7 篇</div><div class="kmtitle">抽取结论，追溯到代码 / 数据 / 引用</div><ul><li><a href="../papers/citation-faithfulness-arxiv-2026/">Citation faithfulness guard</a></li><li><a href="../papers/medragchecker-arxiv-2026/">MedRAGChecker</a></li><li><a href="../papers/citation-blame-emnlp-2026/">Who is to blame? (citations)</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-b&amp;lang=zh&amp;focus=group:B4" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 3 步 · 5 篇</div><div class="kmtitle">检测幻觉与评审</div><ul><li><a href="../papers/llm-judge-healthcare-arxiv-2026/">LLM-as-judge in healthcare</a></li><li><a href="../papers/deep-research-hallucination-arxiv-2026/">PING (trajectory hallucination)</a></li><li><a href="../papers/generalization-bias-rsos-2025/">Overgeneralization bias</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-b&amp;lang=zh&amp;focus=group:B5" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 4 步 · 6 篇</div><div class="kmtitle">评估假设</div><ul><li><a href="../papers/rq-bench-arxiv-2026/">RQ-Bench</a></li><li><a href="../papers/truthhypo-ijcai-2025/">TruthHypo</a></li><li><a href="../papers/hypogen-llm-colm-2024/">LLM hypothesis generators</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-b&amp;lang=zh&amp;focus=group:B6" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 5 步 · 11 篇</div><div class="kmtitle">重跑与失败分析</div><ul><li><a href="../papers/autoresearch-failures-arxiv-2026/">AutoResearch failures</a></li><li><a href="../papers/fev-bioinformatics-agents-arxiv-2026/">FEV review</a></li><li><a href="../papers/clinical-agent-reruns-arxiv-2026/">Same patient, different order</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-b&amp;lang=zh&amp;focus=group:B7" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 6 步 · 5 篇</div><div class="kmtitle">基准 + 专家校准</div><ul><li><a href="../papers/biomnibench-biorxiv-2026/">BiomniBench</a></li><li><a href="../papers/bixbench-arxiv-2025/">BixBench</a></li><li><a href="../papers/bioml-bench-biorxiv-2025/">BioML-bench</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=plan-b&amp;lang=zh&amp;focus=group:B3" target="_blank" rel="noopener">在图谱中打开 ↗</a></div></div>

### 核心阅读清单

<div class="kmflow"><div class="kmstep"><div class="kmnum">第 1 步 · 5 篇</div><div class="kmtitle">基础模型与数据</div><ul><li><a href="../papers/fm-arxiv-2604/">Generative histopathology FM</a></li><li><a href="../papers/pathbench-natcommun-2026/">Pathology FM benchmark</a></li><li><a href="../papers/uni2-h-model/">UNI2-h</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=reading-list&amp;lang=zh&amp;focus=group:foundations" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 2 步 · 12 篇</div><div class="kmtitle">检测</div><ul><li><a href="../papers/imaging-nature-2026/">ECG sudden-death biomarker</a></li><li><a href="../papers/histo-sciencedirect-2026/">Spatial biomarker discovery</a></li><li><a href="../papers/imaging-ehjdh-2026/">AI ejection fraction</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=reading-list&amp;lang=zh&amp;focus=group:detect" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 3 步 · 2 篇</div><div class="kmtitle">建模</div><ul><li><a href="../papers/virtual-tissue-2501/">Virtual tissues (spatial proteomics)</a></li><li><a href="../papers/virtual-cell-challenge/">Virtual Cell Challenge</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=reading-list&amp;lang=zh&amp;focus=group:model" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 4 步 · 3 篇</div><div class="kmtitle">逆转</div><ul><li><a href="../papers/spatial-biorxiv-2025/">MintFlow</a></li><li><a href="../papers/scrna-natmachintell-2026/">Conditional Monge Gap</a></li><li><a href="../papers/counterfactual-diffusion-cancerres-2026/">Counterfactual diffusion</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=reading-list&amp;lang=zh&amp;focus=group:revert" target="_blank" rel="noopener">在图谱中打开 ↗</a></div><div class="kmarrow">→</div><div class="kmstep"><div class="kmnum">第 5 步 · 5 篇</div><div class="kmtitle">agent 与证据</div><ul><li><a href="../papers/deepevidence-natmachintell-2026/">DeepEvidence</a></li><li><a href="../papers/biomni-biorxiv-2025/">Biomni</a></li><li><a href="../papers/hypogen-llm-colm-2024/">LLM hypothesis generators</a></li></ul><a class="kmopen" href="../../maps/viewer.html?view=reading-list&amp;lang=zh&amp;focus=group:agents" target="_blank" rel="noopener">在图谱中打开 ↗</a></div></div>


## 课题 1:肾脏单细胞组学异常检测基准

<iframe src="../../maps/viewer.html?view=plan-a&lang=zh&embed=1" style="width:100%;height:640px;border:1px solid var(--md-default-fg-color--lightest);border-radius:6px" loading="lazy"></iframe>

