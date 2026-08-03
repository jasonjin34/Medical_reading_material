#!/usr/bin/env python3
"""Assemble the MkDocs site under docs/ and (re)generate mkdocs.yml nav.

Copies each paper's deep-read + ai-ready into docs/papers/<slug>/, brings in
the literature review and relationship graph, builds a landing index from the
metadata, and writes a category-grouped nav. Idempotent.
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


def fix_links(text: str) -> str:
    """Rewrite repo-relative links for the flattened docs/ layout."""
    text = text.replace("../papers/", "papers/")
    text = text.replace("relationships/relationships.md", "relationships.md")
    text = re.sub(r"papers/([^/()\s]+)/deep-read\.md", r"papers/\1/index.md", text)
    return text


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
        dr = (src / "deep-read.md")
        ar = (src / "ai-ready.md")
        if dr.exists():
            body = fix_links(dr.read_text(encoding="utf-8"))
            if ar.exists():
                body += "\n\n---\n\n📄 **[AI-ready 全文/full-text extract →](ai-ready.md)**\n"
            (dst / "index.md").write_text(body, encoding="utf-8")
        if ar.exists():
            (dst / "ai-ready.md").write_text(ar.read_text(encoding="utf-8"), encoding="utf-8")

    # top-level pages
    for name in ("literature-review.md",):
        f = ROOT / name
        if f.exists():
            (DOCS / name).write_text(fix_links(f.read_text(encoding="utf-8")), encoding="utf-8")
    rel = ROOT / "relationships" / "relationships.md"
    if rel.exists():
        (DOCS / "relationships.md").write_text(fix_links(rel.read_text(encoding="utf-8")), encoding="utf-8")
    # make the bib downloadable from the site
    bib = ROOT / "references.bib"
    if bib.exists():
        shutil.copyfile(bib, DOCS / "references.bib")

    _write_index(metas)
    _write_mkdocs(metas)
    print(f"✓ site: {len(metas)} papers into docs/, mkdocs.yml nav regenerated")


def _write_index(metas) -> None:
    bycat = defaultdict(list)
    for m in metas:
        bycat[m.get("category", "other")].append(m)
    rows = ["# Medical reading material\n",
            f"> **Research direction / 研究方向:** {DIRECTION}\n",
            "Detect regions of biomedical images & spatial-omics changed by disease or "
            "drug perturbation → model them as *virtual tissues* → predict key genes to "
            "**revert** the anomaly.\n",
            "A living, searchable literature base. New papers are added with "
            "`python scripts/add_paper.py <url> --category <c> --relevance <r>`.\n",
            "See **[Literature review](literature-review.md)** and "
            "**[Paper relationships](relationships.md)**.\n",
            "## Reading list\n",
            "| Paper | Category | Relevance | Access |",
            "|---|---|---|---|"]
    for c in CAT_ORDER:
        for m in sorted(bycat.get(c, []), key=lambda x: -(x.get("relevance") == "high")):
            star = " ★" if m.get("relevance") == "high" else ""
            title = (m.get("title") or m["id"])
            rows.append(
                f"| [{title}](papers/{m['_dir']}/index.md){star} | {CAT_LABEL.get(c, c)} "
                f"| {m.get('relevance','')} | {m.get('access','')} |"
            )
    (DOCS / "index.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


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
  palette:
    - scheme: default
      toggle: {{icon: material/weather-night, name: Dark mode}}
    - scheme: slate
      toggle: {{icon: material/weather-sunny, name: Light mode}}
  features:
    - navigation.sections
    - navigation.top
    - search.highlight
    - content.code.copy
plugins:
  - search
  - mermaid2
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
