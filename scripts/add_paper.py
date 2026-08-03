#!/usr/bin/env python3
"""Add a new reading-list item to the repo — the standardized entry point.

Creates papers/<slug>/ with metadata.yaml, deep-read.md, ai-ready.md (from
templates/) and a citation.bib fragment, fetching metadata automatically.

Usage:
    python scripts/add_paper.py <url|doi|arxiv> \
        --category foundation --relevance high [--slug my-slug]

After running, edit papers/<slug>/deep-read.md, then:
    python scripts/build_bib.py && python scripts/build_relationships.py && python scripts/build_site.py
"""
from __future__ import annotations

import argparse
import datetime
import re
from pathlib import Path

import fetch_metadata as fm

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
TPL = ROOT / "templates"

CATEGORIES = [
    "single-cell", "spatial", "virtual-tissue", "histopath",
    "foundation", "pathology", "imaging", "competition", "other",
]


def yaml_dump(meta: dict) -> str:
    """Minimal, schema-specific YAML emitter (no PyYAML dependency at add-time)."""
    def scalar(v):
        if v is None:
            return "null"
        if isinstance(v, bool):
            return "true" if v else "false"
        if isinstance(v, int):
            return str(v)
        s = str(v).replace('"', '\\"')
        return f'"{s}"'

    lines = []
    order = ["id", "title", "authors", "year", "venue", "type", "category",
             "relevance", "access", "url", "doi", "arxiv", "s2_id", "bibkey",
             "tags", "related", "status", "added"]
    for k in order:
        v = meta.get(k)
        if isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                lines.extend(f"  - {scalar(x)}" for x in v)
        else:
            lines.append(f"{k}: {scalar(v)}")
    return "\n".join(lines) + "\n"


def bibkey_from_bibtex(bibtex: str, fallback: str) -> str:
    m = re.search(r"@\w+\{([^,]+),", bibtex or "")
    return m.group(1).strip() if m else fallback


def fill(template: str, meta: dict) -> str:
    reps = {
        "TITLE": meta.get("title", ""),
        "BIBKEY": meta.get("bibkey", ""),
        "VENUE": meta.get("venue", ""),
        "YEAR": str(meta.get("year") or ""),
        "CATEGORY": meta.get("category", ""),
        "RELEVANCE": meta.get("relevance", ""),
        "ACCESS": meta.get("access", ""),
        "URL": meta.get("url", ""),
        "STATUS": meta.get("status", ""),
        "AUTHORS": "; ".join(meta.get("authors", [])),
        "DOI": meta.get("doi", ""),
        "ABSTRACT": meta.get("abstract", "") or "_(not available — see source)_",
        "BIBTEX": meta.get("bibtex", "") or "% no BibTeX fetched",
    }
    for k, v in reps.items():
        template = template.replace("{{" + k + "}}", v)
    return template


def main() -> None:
    ap = argparse.ArgumentParser(description="Add a paper to the repo.")
    ap.add_argument("ref", help="URL, DOI, or arXiv id")
    ap.add_argument("--category", default="other", choices=CATEGORIES)
    ap.add_argument("--relevance", default="medium", choices=["high", "medium", "low"])
    ap.add_argument("--access", default="", choices=["", "open", "paywall", "abstract-only"])
    ap.add_argument("--slug", default="", help="override folder slug")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    print(f"→ fetching metadata for {args.ref} ...")
    meta = fm.fetch(args.ref)
    if args.access:
        meta["access"] = args.access
    meta.setdefault("access", "open")
    meta.setdefault("tags", [])
    meta.setdefault("related", [])
    meta["category"] = args.category
    meta["relevance"] = args.relevance
    meta["added"] = datetime.date.today().isoformat()
    meta["status"] = "abstract-only" if not meta.get("references") and meta.get(
        "access") == "paywall" else meta.get("status", "complete")

    slug = args.slug or fm.slugify(
        (meta.get("title") or meta.get("arxiv") or meta.get("doi") or args.ref)
    )
    meta["id"] = slug
    meta["bibkey"] = bibkey_from_bibtex(meta.get("bibtex", ""), slug)

    dest = PAPERS / slug
    if dest.exists() and not args.force:
        print(f"! {dest} already exists (use --force to overwrite metadata).")
        return
    dest.mkdir(parents=True, exist_ok=True)

    (dest / "metadata.yaml").write_text(yaml_dump(meta), encoding="utf-8")
    if meta.get("bibtex"):
        (dest / "citation.bib").write_text(meta["bibtex"] + "\n", encoding="utf-8")
    for name in ("deep-read.md", "ai-ready.md"):
        tpl = (TPL / f"{name.replace('.md', '.template.md')}").read_text(encoding="utf-8")
        out = dest / name
        if out.exists() and not args.force:
            continue
        out.write_text(fill(tpl, meta), encoding="utf-8")

    print(f"✓ created papers/{slug}/  ({meta.get('title','?')[:70]})")
    print(f"  bibkey={meta['bibkey']}  s2_id={meta.get('s2_id','')}  status={meta['status']}")
    print("  next: edit deep-read.md, then run build_bib / build_relationships / build_site")


if __name__ == "__main__":
    main()
