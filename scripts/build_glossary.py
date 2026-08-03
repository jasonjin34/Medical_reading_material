#!/usr/bin/env python3
"""Render the trilingual (EN / 中文 / Deutsch) glossary.

Source of truth: glossary/terms.yaml — a list of terms, each with names and
one-sentence definitions in English, Chinese, and German, plus the papers it
appears in. Output: docs/glossary.md and docs/glossary.zh.md (the entries are
identical and trilingual; only the page intro is localized).
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml  # provided by requirements.txt

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "glossary"
DOCS = ROOT / "docs"

DOMAIN_ORDER = [
    ("pathology-histology", "Histopathology / 组织病理"),
    ("spatial-omics", "Spatial omics / 空间组学"),
    ("single-cell", "Single-cell / 单细胞"),
    ("oncology-clinical", "Oncology & clinical / 肿瘤与临床"),
    ("cardiology-imaging", "Cardiology & imaging / 心脏与影像"),
    ("foundation-models", "Foundation models / 基础模型"),
    ("ml-methods", "ML methods / 机器学习方法"),
    ("general", "General / 通用"),
]
DOMAIN_LABEL = dict(DOMAIN_ORDER)


def load_terms() -> list[dict]:
    """Merge every glossary/*.yaml file, de-duplicating by id (or lowercased en)."""
    if not GLOSSARY.is_dir():
        return []
    by_id: dict[str, dict] = {}
    for f in sorted(GLOSSARY.glob("*.yaml")):
        data = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        for t in data:
            if not t.get("en"):
                continue
            key = (t.get("id") or t["en"]).strip().lower()
            merged = {**by_id.get(key, {}), **t}
            # union seen_in across files
            seen = sorted(set((by_id.get(key, {}).get("seen_in") or []))
                          | set(t.get("seen_in") or []))
            if seen:
                merged["seen_in"] = seen
            by_id[key] = merged
    return list(by_id.values())


def _entry(t: dict) -> str:
    en, zh, de = t.get("en", ""), t.get("zh", ""), t.get("de", "")
    head = " · ".join(x for x in [en, zh, de] if x)
    lines = [f"### {head}", ""]
    if t.get("def_en"):
        lines.append(f"- **EN** — {t['def_en']}")
    if t.get("def_zh"):
        lines.append(f"- **中文** — {t['def_zh']}")
    if t.get("def_de"):
        lines.append(f"- **DE** — {t['def_de']}")
    seen = t.get("seen_in") or []
    if seen:
        links = ", ".join(f"[`{s}`](papers/{s}/index.md)" for s in seen)
        lines.append(f"- _Seen in / 出现于:_ {links}")
    lines.append("")
    return "\n".join(lines)


def _render(terms: list[dict], lang: str) -> str:
    bydom = defaultdict(list)
    for t in terms:
        bydom[t.get("domain", "general")].append(t)

    if lang == "zh":
        head = ["# 术语表 / Glossary\n",
                f"> {len(terms)} 条医学与机器学习术语,每条含**英文 / 中文 / 德语**名称与解释。"
                "随论文增长;编辑 `glossary/terms.yaml` 后运行 `python scripts/build_glossary.py`。\n"]
    else:
        head = ["# Glossary / 术语表\n",
                f"> {len(terms)} medical & machine-learning terms, each with an "
                "**English / 中文 / Deutsch** name and definition. Grows with the library; "
                "edit `glossary/terms.yaml` then run `python scripts/build_glossary.py`.\n"]

    out = head
    for dom, label in DOMAIN_ORDER:
        items = sorted(bydom.get(dom, []), key=lambda x: x.get("en", "").lower())
        if not items:
            continue
        out.append(f"## {label}\n")
        out.extend(_entry(t) for t in items)
    # any domain not in the fixed order
    for dom in sorted(set(bydom) - set(DOMAIN_LABEL)):
        out.append(f"## {dom}\n")
        out.extend(_entry(t) for t in sorted(bydom[dom], key=lambda x: x.get("en", "").lower()))
    return "\n".join(out) + "\n"


def main() -> None:
    terms = load_terms()
    if not terms:
        print("! glossary/terms.yaml missing or empty — nothing to build")
        return
    DOCS.mkdir(exist_ok=True)
    (DOCS / "glossary.md").write_text(_render(terms, "en"), encoding="utf-8")
    (DOCS / "glossary.zh.md").write_text(_render(terms, "zh"), encoding="utf-8")
    print(f"✓ glossary: {len(terms)} terms → docs/glossary.md (+ .zh)")


if __name__ == "__main__":
    main()
