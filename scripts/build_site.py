#!/usr/bin/env python3
"""Assemble the bilingual MkDocs site under docs/ and regenerate mkdocs.yml.

Source notes are written once, bilingually, with inline markers:
    <!-- ZH --> 中文 ...
    <!-- EN --> English ...
    <!-- ZH/EN --> shared line kept in both (code, links, datasets)
This script splits each page into an English edition (`page.md`, the default
locale) and a Chinese edition (`page.zh.md`), and the mkdocs-static-i18n plugin
renders a 🌐 language switcher in the header. Idempotent.
"""
from __future__ import annotations

import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _meta  # noqa: E402
import build_glossary  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ONBOARDING = ROOT / "onboarding"
DATASETS = ROOT / "datasets"
RESEARCH = ROOT / "research"
DIRECTION = "Anomaly-detection-based virtual tissue modelling"

CAT_ORDER = ["anomaly", "single-cell", "spatial", "virtual-tissue", "histopath",
             "foundation", "pathology", "imaging", "competition",
             "agents", "ehr", "other"]
CAT_LABEL = {
    "anomaly": "General anomaly detection", "single-cell": "Single-cell", "spatial": "Spatial transcriptomics",
    "virtual-tissue": "Virtual tissues", "histopath": "Histopathology",
    "foundation": "Foundation models", "pathology": "Pathology",
    "imaging": "Imaging", "competition": "Competitions",
    "agents": "Biomedical agents & evaluation", "ehr": "EHR & patient trajectories",
    "other": "Other",
}

# Standalone interactive HTML decks + speaker script. These are copied verbatim
# into docs/<SLIDE_ASSETS>/ (static assets, kept out of the markdown pipeline) and
# linked from a generated bilingual "Slides & talk" page.
SLIDES_SRC = ROOT / "slides" / "med-anomaly-detection"
SLIDE_ASSETS = "talk"
SLIDE_PAGES = [
    ("tree-deck.html", "Tree-deck — interactive navigator", "问题树 deck(推荐)",
     "The talk with a clickable problem-tree sidebar — ← → to navigate, F for fullscreen.",
     "带可点击问题树导航的 deck —— ← → 翻页,F 全屏。"),
    ("index.html", "Full deck", "完整 deck",
     "The linear version of the same talk.",
     "同一场 talk 的线性版 deck。"),
    ("storyline.html", "Storyline (one page)", "Storyline 一页版",
     "The question tree, fact-check, and references on one page.",
     "核心问题树、Fact-check、参考文献,一页看完。"),
    ("speaker-script.html", "Speaker script (EN / 中文)", "讲稿(中英对照)",
     "A ~35-min speaker script — English and Chinese, side by side.",
     "约 35 分钟讲稿 —— 中英三栏对照。"),
]

MARKER = re.compile(r"<!--\s*(ZH|EN|ZH/EN)\s*-->\s*")


# --------------------------------------------------------------------------- #
# Bilingual splitter
# --------------------------------------------------------------------------- #
def _strip_markers(line: str) -> str:
    return MARKER.sub("", line)


CJK = re.compile(r"[一-鿿]")


def _split_header(line: str, lang: str) -> str:
    """`## 中文 / English` -> `## English` (en) or `## 中文` (zh).
    Headers without a ' / ' whose left side is CJK are kept unchanged (both)."""
    m = re.match(r"^(\s*#{1,6}\s+)(.*)$", line)
    if not m:
        return line
    prefix, title = m.group(1), m.group(2)
    parts = title.split(" / ", 1)
    if len(parts) == 2 and CJK.search(parts[0]):
        return prefix + (parts[0].strip() if lang == "zh" else parts[1].strip())
    return line


def _split_table_row(line: str, lang: str) -> str:
    """Split bilingual `X / 中文` table cells by language; leave mono cells alone."""
    parts = line.split("|")
    out = []
    for cell in parts:
        if " / " in cell and CJK.search(cell):
            left, _, right = cell.partition(" / ")
            keep = right if lang == "zh" else left
            # preserve one padding space on each side for readability
            out.append(" " + keep.strip() + " ")
        else:
            out.append(cell)
    return "|".join(out)


def _inline_pick(line: str, lang: str) -> str:
    m = re.match(r"^(\s*(?:[-*]\s+)?)", line)
    prefix, after = m.group(1), line[m.end():]
    zh = re.search(r"<!--\s*ZH\s*-->(.*?)(?=<!--\s*EN\s*-->)", after, re.S)
    en = re.search(r"<!--\s*EN\s*-->(.*)", after, re.S)
    if zh and en:
        part = (zh.group(1) if lang == "zh" else en.group(1))
    else:
        part = _strip_markers(after)
    return (prefix + part.strip()).rstrip()


def split_bilingual(text: str, lang: str) -> str:
    """Return the `lang` ('en'|'zh') edition of marker-annotated markdown."""
    out, mode, in_code = [], "both", False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            out.append(line); mode = "both"; continue
        if in_code:
            out.append(line); continue
        # headers -> split by ' / ' when bilingual, reset language mode
        if re.match(r"^\s*#{1,6}\s", line):
            out.append(_split_header(line, lang)); mode = "both"; continue
        if line.rstrip() == "---":              # a top-level rule only; an indented
            out.append(line); mode = "both"; continue   # "---" (card divider) keeps the mode
        # blockquotes -> both, unless they carry language markers
        if s.startswith(">"):
            if MARKER.search(line):
                if "<!-- ZH/EN -->" in line:
                    out.append(_strip_markers(line))
                elif "<!-- ZH -->" in line and "<!-- EN -->" in line:
                    out.append(_inline_pick(line, lang))
                elif ("<!-- ZH -->" in line and lang == "zh") or \
                     ("<!-- EN -->" in line and lang == "en"):
                    out.append(_strip_markers(line))
            else:
                out.append(line)
            mode = "both"; continue
        # drop standalone template-hint comments (no language marker)
        if re.match(r"^\s*<!--.*-->\s*$", line) and "ZH" not in line and "EN" not in line:
            continue
        has_zh, has_en = "<!-- ZH -->" in line, "<!-- EN -->" in line
        if "<!-- ZH/EN -->" in line:
            out.append(_strip_markers(line)); mode = "both"; continue
        if has_zh and has_en:
            out.append(_inline_pick(line, lang)); mode = "both"; continue
        if has_zh:
            mode = "zh"
            if lang == "zh":
                out.append(_strip_markers(line))
            continue
        if has_en:
            mode = "en"
            if lang == "en":
                out.append(_strip_markers(line))
            continue
        if s == "":
            out.append(line); continue          # blanks in both, keep mode
        if s.startswith("|"):                    # table row: split bilingual cells
            out.append(_split_table_row(line, lang)); continue
        if mode in ("both", lang):
            out.append(line)
    # collapse 3+ blank lines
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


# --------------------------------------------------------------------------- #
# Link rewriting for the flattened docs/ layout
# --------------------------------------------------------------------------- #
def fix_links(text: str) -> str:
    text = text.replace("../papers/", "papers/")
    text = text.replace("relationships/relationships.md", "relationships.md")
    text = re.sub(r"papers/([^/()\s]+)/deep-read\.md", r"papers/\1/index.md", text)
    return text


AI_LINK_EN = "\n\n---\n\n📄 **[AI-ready full-text extract →](ai-ready.md)**\n"
AI_LINK_ZH = "\n\n---\n\n📄 **[AI-ready 全文提取 →](ai-ready.md)**\n"


def _head_body(raw: str):
    """Return (h1_title_line, body_after_first_hr)."""
    lines = raw.split("\n")
    h1 = next((ln for ln in lines if ln.startswith("# ")), "# ")
    idx = next((i for i, ln in enumerate(lines) if ln.strip() == "---"), None)
    body = "\n".join(lines[idx + 1:]) if idx is not None else raw
    return h1, body


def _meta_block(m: dict, lang: str) -> str:
    """A clean, language-neutral metadata block regenerated from metadata.yaml."""
    y = m.get("year") or ""
    if lang == "en":
        return "\n".join([
            f"> **Bibkey** `{m.get('bibkey','')}` · **Venue** {m.get('venue','')} ({y}) · "
            f"**Category** {m.get('category','')} · **Relevance** {m.get('relevance','')} · "
            f"**Access** {m.get('access','')}",
            f"> **Link** <{m.get('url','')}> · `status: {m.get('status','')}`",
        ])
    return "\n".join([
        f"> **文献键** `{m.get('bibkey','')}` · **来源** {m.get('venue','')}({y}) · "
        f"**类别** {m.get('category','')} · **相关度** {m.get('relevance','')} · "
        f"**获取** {m.get('access','')}",
        f"> **链接** <{m.get('url','')}> · `status: {m.get('status','')}`",
    ])


# --------------------------------------------------------------------------- #
# Standalone HTML decks → docs/talk/ + a linked "Slides & talk" page
# --------------------------------------------------------------------------- #
def _copy_slides() -> None:
    dst = DOCS / SLIDE_ASSETS
    if dst.exists():
        shutil.rmtree(dst)
    if not SLIDES_SRC.is_dir():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for fn, *_ in SLIDE_PAGES:              # only the curated decks, not experiments
        src = SLIDES_SRC / fn
        if src.exists():
            shutil.copyfile(src, dst / fn)
    figs = SLIDES_SRC / "figures"
    if figs.is_dir():                        # decks reference figures/ relatively
        shutil.copytree(figs, dst / "figures", dirs_exist_ok=True)


def _slides_page(lang: str) -> str:
    if lang == "en":
        out = ["# Slides & talk\n",
               "Interactive decks and the speaker script for the "
               "**Anomaly Detection in Medical Imaging** talk. Each opens in a new tab.\n"]
    else:
        out = ["# 幻灯片与讲稿\n",
               "《医学影像异常检测》这场 talk 的交互式 deck 与讲稿。点击在新标签页打开。\n"]
    for fn, en, zh, den, dzh in SLIDE_PAGES:
        if not (SLIDES_SRC / fn).exists():
            continue
        label = en if lang == "en" else zh
        desc = den if lang == "en" else dzh
        out.append(f"- **[{label} ↗]({SLIDE_ASSETS}/{fn}){{target=_blank}}** — {desc}")
    return "\n".join(out) + "\n"


def _write_slides() -> None:
    _copy_slides()
    (DOCS / "slides.md").write_text(_slides_page("en"), encoding="utf-8")
    (DOCS / "slides.zh.md").write_text(_slides_page("zh"), encoding="utf-8")


# --------------------------------------------------------------------------- #
def main() -> None:
    metas = _meta.all_meta()
    papers_out = DOCS / "papers"
    if papers_out.exists():
        shutil.rmtree(papers_out)
    papers_out.mkdir(parents=True, exist_ok=True)

    for m in metas:
        src = _meta.PAPERS / m["_dir"]
        dst = papers_out / m["_dir"]
        dst.mkdir(parents=True, exist_ok=True)
        dr, ar = src / "deep-read.md", src / "ai-ready.md"
        if dr.exists():
            raw = dr.read_text(encoding="utf-8")
            h1, body = _head_body(raw)
            has_ai = ar.exists()
            for lang, suffix, ailink in (("en", "index.md", AI_LINK_EN),
                                         ("zh", "index.zh.md", AI_LINK_ZH)):
                page = f"{h1}\n\n{_meta_block(m, lang)}\n\n---\n\n" + \
                    fix_links(split_bilingual(body, lang))
                if has_ai:
                    page += ailink
                (dst / suffix).write_text(page, encoding="utf-8")
        if ar.exists():  # single-language source extract (en default; zh falls back)
            (dst / "ai-ready.md").write_text(ar.read_text(encoding="utf-8"), encoding="utf-8")
        figdir = src / "figures"
        if figdir.is_dir():  # bring downloaded figures into the site
            shutil.copytree(figdir, dst / "figures", dirs_exist_ok=True)

    # top-level bilingual pages
    _emit_split(ROOT / "literature-review.md", "literature-review")
    _emit_split(ROOT / "relationships" / "relationships.md", "relationships")

    _write_index(metas)

    bib = ROOT / "references.bib"
    if bib.exists():
        shutil.copyfile(bib, DOCS / "references.bib")

    _write_slides()
    theme_css = ROOT / "theme" / "extra.css"            # site look (close to hayatlab.org)
    if theme_css.exists():
        (DOCS / "assets").mkdir(exist_ok=True)
        shutil.copyfile(theme_css, DOCS / "assets" / "extra.css")
    modules = _write_onboarding()
    datasets = _write_datasets()
    topics = _write_research()
    _write_mkdocs(metas, modules, datasets, topics)
    print(f"✓ site: {len(metas)} papers + {len(modules)} onboarding pages × (en+zh), "
          "mkdocs.yml (i18n) regenerated")


# --------------------------------------------------------------------------- #
# Research topics: research/topics.yaml + bilingual research/*.md → docs/research/
# --------------------------------------------------------------------------- #
def _load_yaml(path: Path):
    import yaml
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else None


def _topic_page(t: dict) -> str:
    return "index.md" if t["id"] == "overview" else t["file"]


def _write_research() -> list[dict]:
    out = DOCS / "research"
    if out.exists():
        shutil.rmtree(out)
    topics = [t for t in (_load_yaml(RESEARCH / "topics.yaml") or []) if (RESEARCH / t["file"]).exists()]
    if not topics:
        return []
    out.mkdir(parents=True)
    for t in topics:
        raw = (RESEARCH / t["file"]).read_text(encoding="utf-8")
        stem = _topic_page(t)[:-3]
        for lang, suffix in (("en", ".md"), ("zh", ".zh.md")):
            (out / f"{stem}{suffix}").write_text(split_bilingual(raw, lang), encoding="utf-8")
    return topics


# --------------------------------------------------------------------------- #
# Datasets: datasets/datasets.yaml → docs/datasets/ (overview + one page each)
# --------------------------------------------------------------------------- #
DS_TEXT = {
    "en": {"title": "Datasets", "glance": "At a glance", "scale": "Scale", "people": "People / samples",
           "labels": "Labels", "licence": "Licence", "paper": "Paper", "deep": "deep-read",
           "measured": "What was measured", "samples": "People and samples", "label_detail": "Labels",
           "issues": "Known issues", "downloads": "Download", "fmt": "Format", "what": "File",
           "size": "Size", "link": "Link", "use": "Used in our research topics", "species": "Species",
           "assays": "Assays", "access": "Access", "human": "human", "mouse": "mouse",
           "open": "open", "mixed": "processed open, raw controlled", "controlled": "controlled",
           "data": "Dataset", "topics": "Topics", "fig": "Original figure",
           "prepare": "How to prepare",
           "prepare_note": "Tested on 2026-10-26 in plain Python (anndata, scanpy, h5py, scipy, pandas, rdata); no R needed. Keep the data outside this repository."},
    "zh": {"title": "数据集", "glance": "一眼看完", "scale": "规模", "people": "人 / 样本",
           "labels": "标签", "licence": "许可", "paper": "论文", "deep": "精读",
           "measured": "测了什么", "samples": "人和样本", "label_detail": "标签",
           "issues": "已知问题", "downloads": "下载", "fmt": "格式", "what": "文件",
           "size": "大小", "link": "链接", "use": "在我们的研究课题里", "species": "物种",
           "assays": "测法", "access": "获取", "human": "人", "mouse": "小鼠",
           "open": "公开", "mixed": "处理后公开，原始数据受控", "controlled": "受控",
           "data": "数据", "topics": "课题", "fig": "原图",
           "prepare": "怎么准备",
           "prepare_note": "2026-10-26 实测，只用 Python（anndata、scanpy、h5py、scipy、pandas、rdata），不需要 R。数据不要放进这个仓库。"},
}


def _l(d, lang: str) -> str:
    if isinstance(d, dict):
        return d.get(lang) or d.get("en") or ""
    return d or ""


def _cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def _dataset_page(d: dict, cfg: dict, topics: dict, lang: str) -> str:
    T = DS_TEXT[lang]
    name = d.get("name_zh") if lang == "zh" and d.get("name_zh") else d["name"]
    assays = " · ".join(_l(cfg["assay_labels"][a], lang) for a in d.get("assays", []))
    out = [f"# {name}\n", f"> {_l(d.get('oneliner'), lang)}\n",
           f"**{T['species']}** {T.get(d.get('species'), d.get('species'))} · **{T['assays']}** {assays} · "
           f"**{T['access']}** {T.get(d.get('access'), d.get('access'))}\n",
           f"## {T['glance']}\n", "| | |", "|---|---|",
           f"| {T['scale']} | {_cell(_l(d.get('scale'), lang))} |",
           f"| {T['people']} | {_cell(_l(d.get('people'), lang))} |",
           f"| {T['labels']} | {_cell(_l(d.get('labels'), lang))} |",
           f"| {T['licence']} | {_cell(d.get('licence', ''))} |"]
    if d.get("paper"):
        out.append(f"| {T['paper']} | {_cell(d.get('cite', ''))} · [{T['deep']}](../papers/{d['paper']}/index.md) |")
    out.append("")
    fig = d.get("figure")
    if fig:
        out += [f"![{name}](img/{fig['file']})\n", f"*{T['fig']}: {_l(fig, lang)}*\n"]
    for key in ("measured", "samples", "label_detail"):
        if d.get(key):
            out += [f"## {T[key]}\n", _l(d[key], lang) + "\n"]
    if d.get("issues"):
        out.append(f"## {T['issues']}\n")
        out += [f"- {_l(i, lang)}" for i in d["issues"]]
        out.append("")
    if d.get("downloads"):
        out += [f"## {T['downloads']}\n", f"| {T['fmt']} | {T['what']} | {T['size']} | {T['link']} |",
                "|---|---|---|---|"]
        for f in d["downloads"]:
            link = f"[↗]({f['url']})" if f.get("url") else "—"
            out.append(f"| `{f['fmt']}` | {_cell(_l(f['what'], lang))} | {f.get('size', '')} | {link} |")
        out.append("")
        if d.get("download_note"):
            out.append(_l(d["download_note"], lang) + "\n")
    prep = (cfg.get("prepare") or {}).get(d["id"])
    if prep:
        out += [f"## {T['prepare']}\n", f"*{T['prepare_note']}*\n"]
        out += [f"{i}. {_l(st, lang)}" for i, st in enumerate(prep.get("steps", []), 1)]
        out.append("")
        if prep.get("code"):
            out += ["```python", prep["code"].rstrip(), "```", ""]
    if d.get("use_in"):
        out.append(f"## {T['use']}\n")
        for tid, text in d["use_in"].items():
            t = topics.get(tid)
            label = _l(t["title"], lang) if t else tid
            target = f"[{label}](../research/{_topic_page(t)})" if t else label
            out.append(f"- **{target}**: {_l(text, lang)}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _datasets_index(cfg: dict, topics: dict, lang: str) -> str:
    T = DS_TEXT[lang]
    if lang == "zh":
        out = ["# 数据集\n",
               "我们用到的公开肾脏数据，每份一页：测了什么、多少人、有什么标签、在哪下载、什么格式和许可、"
               "已知问题，以及被哪个研究课题用到。看不懂测法或术语，先读 **[入门](../onboarding/index.md)**；"
               "怎么判断一份数据能不能用，见 [入门 · 怎么读懂一份数据集](../onboarding/07-datasets.md)。\n",
               "数字都在 2026-10-26 对过 GEO、Zenodo、cellxgene、SRA 和论文原文；标“我们数的”是从下载的标签表里算出来的。\n",
               "**能不能下载：**2026-10-26 用不下载的方式（每个文件只请求开头 16 字节）检查了 8 个数据集的 33 个文件，全部可以下载、格式正确。"
               "每个数据集页面的“怎么准备”一节有实测过的读取步骤和代码。\n"]
    else:
        out = ["# Datasets\n",
               "The public kidney datasets we use, one page each: what was measured, on how many people, which "
               "labels, where to download, format and licence, known issues, and which research topic uses it. "
               "New to the assays or terms? Read **[Onboarding](../onboarding/index.md)** first; for how to judge "
               "whether a dataset is usable, see [Onboarding · How to read a dataset](../onboarding/07-datasets.md).\n",
               "Numbers were checked on 2026-10-26 against GEO, Zenodo, cellxgene, SRA and the papers; "
               "\"counted by us\" means computed from the downloaded label tables.\n",
               "**Availability:** on 2026-10-26 all 33 files of the 8 datasets were checked without downloading "
               "(one 16-byte request per file): every file is downloadable and has the expected format. Each "
               "dataset page has a tested \"How to prepare\" section with loading steps and code.\n"]
    for g, glabel in cfg["groups"].items():
        items = [d for d in cfg["datasets"] if d.get("group") == g]
        if not items:
            continue
        out += [f"## {_l(glabel, lang)}\n",
                f"| {T['data']} | {T['species']} | {T['assays']} | {T['scale']} | {T['people']} | {T['access']} | {T['topics']} |",
                "|---|---|---|---|---|---|---|"]
        for d in items:
            name = d.get("name_zh") if lang == "zh" and d.get("name_zh") else d["name"]
            assays = ", ".join(_l(cfg["assay_labels"][a], lang) for a in d.get("assays", []))
            tl = ", ".join(str(list(topics).index(t)) for t in (d.get("use_in") or {}) if t in topics)
            out.append(f"| [{_cell(name)}]({d['id']}.md) | {T.get(d.get('species'))} | {assays} | "
                       f"{_cell(_l(d.get('scale'), lang))} | {_cell(_l(d.get('people'), lang))} | "
                       f"{T.get(d.get('access'), d.get('access'))} | {tl} |")
        out.append("")
    names = [f"{i} = [{_l(t['title'], lang)}](../research/{_topic_page(t)})" for i, t in enumerate(topics.values()) if i]
    out.append(("**课题编号：**" if lang == "zh" else "**Topic numbers:** ") + " · ".join(names) + "\n")
    return "\n".join(out)


def _write_datasets() -> list[dict]:
    out = DOCS / "datasets"
    if out.exists():
        shutil.rmtree(out)
    cfg = _load_yaml(DATASETS / "datasets.yaml")
    if not cfg or not cfg.get("datasets"):
        return []
    topics = {t["id"]: t for t in (_load_yaml(RESEARCH / "topics.yaml") or [])}
    out.mkdir(parents=True)
    for lang, suffix in (("en", ".md"), ("zh", ".zh.md")):
        (out / f"index{suffix}").write_text(_datasets_index(cfg, topics, lang), encoding="utf-8")
        for d in cfg["datasets"]:
            (out / f"{d['id']}{suffix}").write_text(_dataset_page(d, cfg, topics, lang), encoding="utf-8")
    if (DATASETS / "img").is_dir():
        shutil.copytree(DATASETS / "img", out / "img")
    return cfg["datasets"]


# --------------------------------------------------------------------------- #
# Onboarding: onboarding/*.md (bilingual sources) → docs/onboarding/, plus the
# glossary, which lives in this section and is ordered by module.
# --------------------------------------------------------------------------- #
def _onboarding_meta(m: dict, lang: str) -> str:
    mins = m.get("minutes", 0)
    t = (f"{mins // 60} 小时" if mins >= 60 and mins % 60 == 0 else f"{mins} 分钟") if lang == "zh" \
        else (f"{mins // 60} h" if mins >= 60 and mins % 60 == 0 else f"{mins} min")
    day = m.get("day", 0)
    if lang == "zh":
        when = {1: "第 1 天 · 读懂", 2: "第 2 天 · 上手（可选）"}.get(day, "")
        return f"> ⏱ 约 {t}" + (f" · {when}" if when else "")
    when = {1: "Day 1 · Understand", 2: "Day 2 · Hands-on (optional)"}.get(day, "")
    return f"> ⏱ About {t}" + (f" · {when}" if when else "")


def _write_onboarding() -> list[dict]:
    """Render onboarding modules and the glossary; return the modules that have a page."""
    out = DOCS / "onboarding"
    if out.exists():
        shutil.rmtree(out)
    for stale in ("glossary.md", "glossary.zh.md"):   # the glossary moved into onboarding/
        (DOCS / stale).unlink(missing_ok=True)
    modules = [m for m in build_glossary.load_modules() if (ONBOARDING / m["file"]).exists()]
    if not modules:
        return []
    out.mkdir(parents=True)
    terms = build_glossary.load_terms()
    for m in modules:
        raw = (ONBOARDING / m["file"]).read_text(encoding="utf-8")
        stem = build_glossary.page_name(m)[:-3]
        for lang, suffix in (("en", ".md"), ("zh", ".zh.md")):
            body = split_bilingual(raw, lang)
            lines = body.split("\n")
            h1 = next((i for i, ln in enumerate(lines) if ln.startswith("# ")), None)
            if h1 is not None:
                lines.insert(h1 + 1, "\n" + _onboarding_meta(m, lang))
            page = "\n".join(lines).rstrip() + "\n"
            table = build_glossary.module_table(m, terms, lang)
            if table:
                page += "\n" + table
            (out / f"{stem}{suffix}").write_text(page, encoding="utf-8")
    if (ONBOARDING / "img").is_dir():
        shutil.copytree(ONBOARDING / "img", out / "img")
    if (ONBOARDING / "onboarding.css").exists():
        shutil.copy(ONBOARDING / "onboarding.css", out / "onboarding.css")
    if (ONBOARDING / "onboarding.js").exists():
        shutil.copy(ONBOARDING / "onboarding.js", out / "onboarding.js")
    build_glossary.write()
    return modules


def _emit_split(src: Path, stem: str) -> None:
    if not src.exists():
        return
    raw = src.read_text(encoding="utf-8")
    (DOCS / f"{stem}.md").write_text(fix_links(split_bilingual(raw, "en")), encoding="utf-8")
    (DOCS / f"{stem}.zh.md").write_text(fix_links(split_bilingual(raw, "zh")), encoding="utf-8")


def _home_text(metas, lang: str) -> str:
    """Landing page: what the site is, and two doors — onboarding and the paper library."""
    n = len(metas)
    if lang == "en":
        return f"""# Omics AI Handbook

> **Research direction:** {DIRECTION}

Detect regions of biomedical images and spatial omics changed by disease or drug perturbation,
model them as *virtual tissues*, and predict key genes that **revert** the anomaly.

<div class="grid cards" markdown>

-   :material-school-outline:{{ .lg .middle }} __New here? Onboarding__

    ---

    One to two days from zero to reading kidney single-cell data: cells and RNA, the kidney,
    assays, artifacts, classic datasets, and the problem we work on. Written for people with a
    computer-science background. Includes the glossary.

    [:octicons-arrow-right-24: Start here](onboarding/index.md)

-   :material-database-outline:{{ .lg .middle }} __Datasets__

    ---

    The public kidney datasets we use: what each measured, on how many people, which labels,
    where to download, format, licence and known issues.

    [:octicons-arrow-right-24: Browse datasets](datasets/index.md)

-   :material-flask-outline:{{ .lg .middle }} __Research topics__

    ---

    The group's research topics: what each asks, what it will produce, and where it stands.

    [:octicons-arrow-right-24: See the topics](research/index.md)

-   :material-book-open-variant:{{ .lg .middle }} __Paper library__

    ---

    {n} bilingual deep-reads, the literature review, the knowledge map and the paper
    relationship graph.

    [:octicons-arrow-right-24: Browse papers](papers/index.md)

-   :material-presentation:{{ .lg .middle }} __Talks__

    ---

    The interactive tree-deck, full deck, storyline and ~35-min speaker script.

    [:octicons-arrow-right-24: Slides & talk](slides.md)

</div>

Add a paper with `python scripts/add_paper.py <url> --category <c> --relevance <r>`.
"""
    return f"""# 组学 AI 手册

> **研究方向：**{DIRECTION}（异常检测驱动的虚拟组织建模）

检测因疾病或药物扰动而改变的生物医学影像与空间组学区域，建成*虚拟组织*，再预测能**逆转**异常的关键基因。

<div class="grid cards" markdown>

-   :material-school-outline:{{ .lg .middle }} __新人？先读入门__

    ---

    1–2 天从零读懂肾脏单细胞数据：细胞和 RNA、肾脏、测法、伪影、经典数据集，以及我们要解决的问题。
    写给计算机背景的读者，名词表也在这里。

    [:octicons-arrow-right-24: 从这里开始](onboarding/index.md)

-   :material-database-outline:{{ .lg .middle }} __数据集__

    ---

    我们用到的公开肾脏数据：每份测了什么、多少人、有什么标签、在哪下载、什么格式和许可、已知问题。

    [:octicons-arrow-right-24: 浏览数据集](datasets/index.md)

-   :material-flask-outline:{{ .lg .middle }} __研究课题__

    ---

    组里的各个研究课题：每个课题要回答什么、做出什么、现在到哪一步。

    [:octicons-arrow-right-24: 看研究课题](research/index.md)

-   :material-book-open-variant:{{ .lg .middle }} __论文库__

    ---

    {n} 篇中英双语精读、文献综述、知识图谱和论文关系图。

    [:octicons-arrow-right-24: 浏览论文](papers/index.md)

-   :material-presentation:{{ .lg .middle }} __报告__

    ---

    交互式问题树 deck、完整 deck、storyline 和约 35 分钟讲稿。

    [:octicons-arrow-right-24: 幻灯片与讲稿](slides.md)

</div>

添加论文：`python scripts/add_paper.py <url> --category <c> --relevance <r>`。
"""


def _papers_index_text(metas, lang: str) -> str:
    """The Papers tab's landing page: pointers to the synthesis pages + the reading list."""
    bycat = defaultdict(list)
    for m in metas:
        bycat[m.get("category", "other")].append(m)
    if lang == "en":
        head = [
            "# Paper library\n",
            "Background first? See **[Onboarding](../onboarding/index.md)**. "
            "Across papers: **[Literature review](../literature-review.md)** · "
            "**[Knowledge map](../knowledge-map.md)** · **[Relationships](../relationships.md)**.\n",
            "## Reading list\n",
            "| Paper | Category | Relevance | Access |",
            "|---|---|---|---|",
        ]
    else:
        head = [
            "# 论文库\n",
            "需要背景知识？先读 **[入门](../onboarding/index.md)**。"
            "跨论文的综合：**[文献综述](../literature-review.md)** · "
            "**[知识图谱](../knowledge-map.md)** · **[论文关系](../relationships.md)**。\n",
            "## 阅读清单\n",
            "| 论文 | 类别 | 相关度 | 获取 |",
            "|---|---|---|---|",
        ]
    rows = []
    for c in CAT_ORDER:
        for m in sorted(bycat.get(c, []), key=lambda x: -(x.get("relevance") == "high")):
            star = " ★" if m.get("relevance") == "high" else ""
            title = (m.get("title") or m["id"])
            rows.append(
                f"| [{title}]({m['_dir']}/index.md){star} | {CAT_LABEL.get(c, c)} "
                f"| {m.get('relevance','')} | {m.get('access','')} |"
            )
    return "\n".join(head + rows) + "\n"


def _write_index(metas) -> None:
    (DOCS / "index.md").write_text(_home_text(metas, "en"), encoding="utf-8")
    (DOCS / "index.zh.md").write_text(_home_text(metas, "zh"), encoding="utf-8")
    (DOCS / "papers" / "index.md").write_text(_papers_index_text(metas, "en"), encoding="utf-8")
    (DOCS / "papers" / "index.zh.md").write_text(_papers_index_text(metas, "zh"), encoding="utf-8")


# Chinese labels for nav sections (page titles come from each page's own H1).
NAV_ZH = {
    "Home": "首页", "Onboarding": "入门", "Day 1 · Understand": "第 1 天 · 读懂",
    "Day 2 · Hands-on (optional)": "第 2 天 · 上手（可选）", "Glossary": "名词表",
    "Papers": "论文", "Datasets": "数据集", "Research topics": "研究课题", "Literature review": "文献综述", "Knowledge map": "知识图谱",
    "Relationships": "论文关系", "Talks": "报告", "Slides & talk": "幻灯片与讲稿",
    "General anomaly detection": "通用异常检测", "Single-cell": "单细胞",
    "Spatial transcriptomics": "空间转录组", "Virtual tissues": "虚拟组织",
    "Histopathology": "组织病理", "Foundation models": "基础模型", "Pathology": "病理",
    "Imaging": "医学影像", "Competitions": "竞赛",
    "Biomedical agents & evaluation": "生物医学智能体与评测",
    "EHR & patient trajectories": "电子病历与病程", "Other": "其他",
}


def _write_mkdocs(metas, modules, datasets=(), topics=()) -> None:
    bycat = defaultdict(list)
    for m in metas:
        bycat[m.get("category", "other")].append(m)

    nav = ["  - Home: index.md"]
    if modules:
        nav.append("  - Onboarding:")
        nav.append("    - onboarding/index.md")
        for day, label in ((1, "Day 1 · Understand"), (2, "Day 2 · Hands-on (optional)")):
            pages = [m for m in modules if m.get("day") == day]
            if pages:
                nav.append(f"    - {label}:")
                nav.extend(f"      - onboarding/{build_glossary.page_name(m)}" for m in pages)
        nav.append("    - Glossary: onboarding/glossary.md")
    if datasets:
        nav.append("  - Datasets:")
        nav.append("    - datasets/index.md")
        nav.extend(f"    - datasets/{d['id']}.md" for d in datasets)
    if topics:
        nav.append("  - Research topics:")
        nav.extend(f"    - research/{_topic_page(t)}" for t in topics)
    nav += ["  - Papers:",
            "    - papers/index.md",
            "    - Literature review: literature-review.md",
            "    - Knowledge map: knowledge-map.md",
            "    - Relationships: relationships.md"]
    for c in CAT_ORDER:
        items = sorted(bycat.get(c, []), key=lambda x: -(x.get("relevance") == "high"))
        if not items:
            continue
        nav.append(f"    - {CAT_LABEL.get(c, c)}:")
        for m in items:
            title = (m.get("title") or m["id"]).replace('"', "'")
            nav.append(f'      - "{title}": papers/{m["_dir"]}/index.md')
    nav.append("  - Talks:")
    nav.append("    - Slides & talk: slides.md")
    nav_zh = "\n".join(f'            "{k}": "{v}"' for k, v in NAV_ZH.items())

    yml = f"""site_name: Omics AI Handbook
site_description: {DIRECTION}
theme:
  name: material
  language: en
  palette:
    - scheme: default
      primary: custom
      accent: custom
      toggle: {{icon: material/weather-night, name: Switch to dark mode}}
    - scheme: slate
      primary: custom
      accent: custom
      toggle: {{icon: material/weather-sunny, name: Switch to light mode}}
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.footer
    - navigation.top
    - search.highlight
    - content.code.copy
plugins:
  - search
  - mermaid2
  - i18n:
      docs_structure: suffix
      fallback_to_default: true
      reconfigure_material: true
      reconfigure_search: true
      languages:
        - locale: en
          default: true
          name: English
          build: true
        - locale: zh
          name: 中文
          build: true
          nav_translations:
{nav_zh}
extra_css:
  - assets/extra.css
  - onboarding/onboarding.css
extra_javascript:
  - onboarding/onboarding.js
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:mermaid2.fence_mermaid_custom
nav:
{chr(10).join(nav)}
"""
    (ROOT / "mkdocs.yml").write_text(yml, encoding="utf-8")


if __name__ == "__main__":
    main()
