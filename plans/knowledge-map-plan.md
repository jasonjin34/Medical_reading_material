# 知识图谱与流程图 实施计划 / Knowledge map plan

> 状态:已实施(M0–M3 ✓)· 2026-10-19
> 目标:把 99 篇论文、核心概念和两个硕士论文 plan 整合成**可读**的图谱和流程图,
> 网页(Cytoscape.js)和 Obsidian 两端同时可用,由同一份数据生成。

---

## 1. 已定的结构

- **一份数据,多张独立的图。** 每个视图有自己的网页和自己的 Obsidian MOC/Canvas,
  只加载属于它的节点;底层只维护一份 metadata。
- **同时属于 A 和 B 的论文**在两张图里各出现一次,带"也在 Plan B / A"标签,并单独组成一张"桥"图。
- **全图只做总览**,不用来细读。
- **默认先显示折叠的骨架**,需要时再展开。

| 视图 | 选取规则 | 主轴(左 → 右) | 展开后节点数 | 默认可见 |
|---|---|---|---|---|
| Plan A | `plans` 含 `A` | A1 图谱 → A2 QC/伪影 → A3 anomaly/OOD → A4 跨模态 → A5 基础模型/基线 → A6 评测 | ≈ 45 | 6 个组框 + 概念 ≈ 20 |
| Plan B | `plans` 含 `B` | B1 科研 agent → B2 omics agent → B3 benchmark → B4 claim 核查 → B5 幻觉/judge → B6 假设评测 → B7 可靠性/安全 | ≈ 55 | 7 个组框 + 概念 ≈ 22 |
| 桥 A∩B | 同时含 `A` 和 `B` | 无主轴,两侧分别是 A、B 的概念 | ≈ 10–15 | 全部 |
| Sikander's picks | `recommended_by: sikander` | detect → model → revert | ≈ 30 | 全部 |
| EHR | `plans` 含 `EHR` | 无 | 5 | 全部 |
| 全图 | 全部 | 按分类聚类 | ≈ 250 | 只看轮廓 |

可读性标准:默认视图 ≤ 25 个可见节点;展开后 ≤ 60;Canvas ≤ 20 张卡片。

---

## 2. 数据层(两端共用)

### 2.1 每篇论文的 `metadata.yaml` 新增字段

```yaml
plans: ["A"]             # 可多选:A / B / EHR
track: "A3"              # 在 reading list 中的分组;A 与 B 都有时写主分组
recommended_by: ""       # "sikander" 或留空
```

- 99 篇由脚本按 thesis doc 的 reading list 分组自动填写,你抽查。
- Sikander 7 月清单里的 18 项:`recommended_by: sikander`,并按内容归入 Plan A 的分组(或只进 Sikander 视图)。
- `track` 也作为网页和 Canvas 上的列。

### 2.2 视图配置 `maps/views.yaml`(手写的源文件)

```yaml
plan-a:
  title: {en: "Plan A — kidney omics anomaly detection", zh: "Plan A:肾脏组学异常检测"}
  select: {plans: A}
  tracks:
    A1: {en: "Atlases & disease states", zh: "图谱与疾病状态"}
    # … A2–A6
  concepts: [healthy-reference, cross-modal-agreement, segmentation-artifact, …]   # 15–20 个
```

### 2.3 概念节点

- 来自 glossary(已有 110 个术语,每个都有 `seen_in: [slug…]`,可直接作为概念 → 论文的连线)。
- 每个视图只放 `views.yaml` 里列出的 15–20 个核心概念;glossary 缺的概念补进 glossary(源文件)。
- 我先起草两个 plan 的核心概念清单,你来增删。

---

## 3. 生成产物(新脚本 `scripts/build_maps.py`)

### 3.1 网页(Cytoscape.js)

- `docs/maps/<view>.html` + `docs/maps/<view>.json`:独立的 HTML 页面,和现在的 slides 一样直接复制进站点。
  Cytoscape.js 从 cdnjs 加载,不新增 Python 依赖。
- `docs/knowledge-map.md`(及 `.zh.md`):总入口页,列出各视图的卡片,导航栏新增 "Knowledge map"。
- **布局:** 位置由 Python 预先算好(列 = track,列内按年份排序),结果确定,每次 build 一致,不依赖力导向布局。
- **交互:**
  - 组框默认折叠,点开后展开。
  - 单击节点进入聚焦模式:只亮出邻居,其余变灰。
  - 双击节点跳到对应论文的精读页。
  - 顶部有筛选:relevance(must/should)、年份、节点类型。
  - 节点颜色表示类型(论文 / 概念 / 数据集),大小表示 relevance;桥节点加描边。
- **主题:** 跟随站点的明暗模式,手机宽度可用。

### 3.2 Obsidian

repo 根目录直接当 vault 打开。生成的内容全部放在 `_maps/` 文件夹里,你自己的笔记放在别处,互不覆盖。

- `_maps/papers/<slug>.md`:每篇论文一张 hub note。
  - frontmatter:`plans`、`track`、`year`、`relevance`、`tags`,用于 Graph view 着色和 Dataview 查询。
  - 正文:`![[papers/<slug>/deep-read.md]]` 嵌入精读,原文不复制也不改动。
  - 链接区:related 和概念边转成 `[[wikilink]]`,并写上边的标签。
- `_maps/concepts/<id>.md`:每个核心概念一张,链回 `seen_in` 里的论文。
- `_maps/Plan A.md`、`_maps/Plan B.md`……:每个视图一张 MOC,按 track 分节列出论文。
- `_maps/Plan A.canvas`、`_maps/Plan B.canvas`:JSON Canvas 格式的流程图,每列一个 track,只放 must-read(≤ 20 张卡片),卡片链到 hub note。
- Graph view 的颜色分组(按 `plans`)写在说明里,由你在 Obsidian 里一次性设置;不改 `.obsidian/` 配置。

### 3.3 build 流程

```bash
python scripts/build_bib.py
python scripts/build_relationships.py
python scripts/build_maps.py      # 新增:生成 docs/maps/ 和 _maps/
python scripts/build_site.py      # 把 Knowledge map 加入导航
```

`_maps/`、`docs/maps/` 属于 generated 文件,写入 CLAUDE.md 的"不可手改"清单。

---

## 4. 实施步骤

| 步骤 | 内容 | 产出 | 你需要做的 |
|---|---|---|---|
| M0 数据层 ✓ | 给 99 篇论文填 `plans` / `track` / `recommended_by`;写 `views.yaml`;起草概念清单 | metadata 更新、`maps/views.yaml` | 抽查分组,增删概念 |
| M1 Plan A 小样 ✓ | 网页视图 + Obsidian hub notes、MOC、Canvas,只做 Plan A | `docs/maps/plan-a.html`、`_maps/` | 在浏览器和 Obsidian 里看可读性,提意见 |
| M2 铺开 ✓ | Plan B(组框折叠)、桥、Sikander's picks、EHR、全图总览 | 其余视图 | 再看一遍 |
| M3 收尾 ✓ | 接入 build、更新 CLAUDE.md 和 README、`mkdocs build --strict`、截图检查 | commit + 部署 | 确认后 push |

每一步完成都会截图检查网页图,确认真的看得清再进入下一步。

---

### 实施时的补充(M2)

- **流程图：** `views.yaml` 里每个 plan 有一个 `flow:` 段。生成三处：
  - 站点 Knowledge map 页的 Mermaid 纵向流程图，图下附上每一步在图谱里的链接;
  - MOC 顶部同一张 Mermaid 图;
  - Obsidian 的 `<视图> — flow.canvas`。
- **筛选：** viewer 加了年份和类型筛选，URL 参数是 `year=`、`type=`、`must=1`。类型用形状区分：代码 / 模型是切角，竞赛是桶形。
- **概念：** Plan B 去掉了 knowledge-graph 概念(默认可见节点从 26 降到 25)。Sikander 视图有 8 个概念，由 `concepts_pick` 从 Plan A 选取，再加上自己的概念。
- **总览：** 全部折叠时，组框按每行 4 个排列(`wrap: 4`)。

## 5. 验收标准

- 每个视图默认 ≤ 25 个可见节点,展开后 ≤ 60;文字不重叠,不出现穿过节点的连线。
- 任意论文节点双击都能打开精读页;Obsidian 里任意 hub note 都能看到嵌入的精读和链接。
- 同时属于 A 和 B 的论文在两张图里都有,并标出。
- 加一篇新论文时,只需填 `plans` / `track`,重新 build,图会自动更新。
- `mkdocs build --strict` 通过,手机宽度不出现横向滚动。

## 6. 不做的事

- 不把 glossary 的 110 个术语全部放进图。
- 不改动精读源文件,也不复制它们的内容。
- 不使用外部服务(Connected Papers 等)的数据;它们只用来发现新文章。
- 第一版不做力导向的全局大图细读。

## 7. 待确认

1. 核心概念的数量:每个 plan 15–20 个,可以吗?
2. Obsidian 用"repo 直接当 vault 打开 + `_maps/` 由生成脚本覆盖"的方式,可以吗?
3. Sikander 7 月清单里不属于任何 plan 的项目(比如心脏影像、pathomics),只放在 Sikander 视图里,可以吗?
