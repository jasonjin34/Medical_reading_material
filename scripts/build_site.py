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

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DIRECTION = "Anomaly-detection-based virtual tissue modelling"

CAT_ORDER = ["single-cell", "spatial", "virtual-tissue", "histopath",
             "foundation", "pathology", "imaging", "competition", "other"]
CAT_LABEL = {
    "single-cell": "Single-cell", "spatial": "Spatial transcriptomics",
    "virtual-tissue": "Virtual tissues", "histopath": "Histopathology",
    "foundation": "Foundation models", "pathology": "Pathology",
    "imaging": "Imaging", "competition": "Competitions", "other": "Other",
}

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
        if s == "---":
            out.append(line); mode = "both"; continue
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

    # top-level bilingual pages
    _emit_split(ROOT / "literature-review.md", "literature-review")
    _emit_split(ROOT / "relationships" / "relationships.md", "relationships")

    _write_index(metas)

    bib = ROOT / "references.bib"
    if bib.exists():
        shutil.copyfile(bib, DOCS / "references.bib")

    _write_mkdocs(metas)
    print(f"✓ site: {len(metas)} papers × (en+zh), mkdocs.yml (i18n) regenerated")


def _emit_split(src: Path, stem: str) -> None:
    if not src.exists():
        return
    raw = src.read_text(encoding="utf-8")
    (DOCS / f"{stem}.md").write_text(fix_links(split_bilingual(raw, "en")), encoding="utf-8")
    (DOCS / f"{stem}.zh.md").write_text(fix_links(split_bilingual(raw, "zh")), encoding="utf-8")


def _index_text(metas, lang: str) -> str:
    bycat = defaultdict(list)
    for m in metas:
        bycat[m.get("category", "other")].append(m)
    if lang == "en":
        head = [
            "# Medical reading material\n",
            f"> **Research direction:** {DIRECTION}\n",
            "Detect regions of biomedical images & spatial-omics changed by disease or "
            "drug perturbation → model them as *virtual tissues* → predict key genes to "
            "**revert** the anomaly.\n",
            "A living, searchable literature base. Add a paper with "
            "`python scripts/add_paper.py <url> --category <c> --relevance <r>`.\n",
            "See the **[Literature review](literature-review.md)** and "
            "**[Paper relationships](relationships.md)**.\n",
            "## Reading list\n",
            "| Paper | Category | Relevance | Access |",
            "|---|---|---|---|",
        ]
    else:
        head = [
            "# 医学文献库\n",
            f"> **研究方向:** {DIRECTION}(异常检测驱动的虚拟组织建模)\n",
            "检测因疾病或药物扰动而改变的生物医学影像与空间组学区域 → 建成*虚拟组织* → "
            "预测能**逆转**异常的关键基因。\n",
            "一个可搜索、可持续增长的文献库。添加论文:"
            "`python scripts/add_paper.py <url> --category <c> --relevance <r>`。\n",
            "见 **[文献综述](literature-review.md)** 与 **[论文关系](relationships.md)**。\n",
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
                f"| [{title}](papers/{m['_dir']}/index.md){star} | {CAT_LABEL.get(c, c)} "
                f"| {m.get('relevance','')} | {m.get('access','')} |"
            )
    return "\n".join(head + rows) + "\n"


def _write_index(metas) -> None:
    (DOCS / "index.md").write_text(_index_text(metas, "en"), encoding="utf-8")
    (DOCS / "index.zh.md").write_text(_index_text(metas, "zh"), encoding="utf-8")


def _write_mkdocs(metas) -> None:
    bycat = defaultdict(list)
    for m in metas:
        bycat[m.get("category", "other")].append(m)

    nav = ["  - Home: index.md",
           "  - Literature review: literature-review.md",
           "  - Relationships: relationships.md",
           "  - Papers:"]
    for c in CAT_ORDER:
        items = sorted(bycat.get(c, []), key=lambda x: -(x.get("relevance") == "high"))
        if not items:
            continue
        nav.append(f"    - {CAT_LABEL.get(c, c)}:")
        for m in items:
            title = (m.get("title") or m["id"]).replace('"', "'")
            nav.append(f'      - "{title}": papers/{m["_dir"]}/index.md')

    yml = f"""site_name: Medical Reading Material
site_description: {DIRECTION}
theme:
  name: material
  language: en
  palette:
    - scheme: default
      toggle: {{icon: material/weather-night, name: Switch to dark mode}}
    - scheme: slate
      toggle: {{icon: material/weather-sunny, name: Switch to light mode}}
  features:
    - navigation.sections
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
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
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
