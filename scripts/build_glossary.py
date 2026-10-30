#!/usr/bin/env python3
"""Render the trilingual (EN / 中文 / Deutsch) glossary into the onboarding section.

Source of truth: glossary/*.yaml — terms with names and one-sentence definitions
in English, Chinese and German, plus the papers they appear in. Which onboarding
module teaches a term is set in onboarding/modules.yaml (`terms:` per module).

Output: docs/onboarding/glossary.md and .zh.md. Terms are ordered by the module
that teaches them; terms no module claims follow, grouped by domain. Each term
heading carries an anchor (`#<id>`) so module pages can link to it.
build_site.py imports this module to add a "Terms in this module" table to each
onboarding page and calls write() itself, so running this script alone is only
needed to refresh the glossary without rebuilding the site.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml  # provided by requirements.txt

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "glossary"
MODULES = ROOT / "onboarding" / "modules.yaml"
OUT = ROOT / "docs" / "onboarding"

DOMAIN_ORDER = [
    ("single-cell", "Single-cell / 单细胞"),
    ("nephrology-clinical", "Nephrology & clinical / 肾脏与临床"),
    ("spatial-omics", "Spatial omics / 空间组学"),
    ("pathology-histology", "Histopathology / 组织病理"),
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
            merged.setdefault("id", key)
            by_id[key] = merged
    return list(by_id.values())


def load_modules() -> list[dict]:
    if not MODULES.exists():
        return []
    return yaml.safe_load(MODULES.read_text(encoding="utf-8")) or []


def page_name(module: dict) -> str:
    """docs/onboarding/<stem>.md for a module (the start page is the section index)."""
    return "index.md" if module["id"] == "start" else module["file"]


def _pick(t: dict, lang: str, field: str) -> str:
    """Language-first value: def_zh on the zh page, def_en on the en page."""
    return t.get(f"{field}_{lang}") or t.get(f"{field}_en") or ""


def _entry(t: dict, lang: str, taught_in: dict | None) -> str:
    en, zh, de = t.get("en", ""), t.get("zh", ""), t.get("de", "")
    first, second = (zh, en) if lang == "zh" else (en, zh)
    head = " · ".join(x for x in [first, second] if x)
    lines = [f"### {head} {{#{t['id']}}}", ""]
    defs = [("中文", "def_zh"), ("EN", "def_en")] if lang == "zh" else [("EN", "def_en"), ("中文", "def_zh")]
    for label, key in defs:
        if t.get(key):
            lines.append(f"- **{label}** — {t[key]}")
    if de or t.get("def_de"):
        lines.append(f"- **DE** — {de}" + (f": {t['def_de']}" if t.get("def_de") else ""))
    if taught_in:
        title = taught_in["title"]["zh" if lang == "zh" else "en"]
        lab = "在入门里讲" if lang == "zh" else "Explained in"
        lines.append(f"- _{lab}:_ [{title}]({page_name(taught_in)})")
    seen = t.get("seen_in") or []
    if seen:
        links = ", ".join(f"[`{s}`](../papers/{s}/index.md)" for s in seen)
        lab = "出现于" if lang == "zh" else "Seen in"
        lines.append(f"- _{lab}:_ {links}")
    lines.append("")
    return "\n".join(lines)


def term_module_map(modules: list[dict]) -> dict[str, dict]:
    out = {}
    for m in modules:
        for tid in m.get("terms") or []:
            out.setdefault(tid, m)
    return out


def render(terms: list[dict], modules: list[dict], lang: str) -> str:
    by_id = {t["id"]: t for t in terms}
    taught = term_module_map(modules)
    if lang == "zh":
        out = ["# 名词表\n",
               f"> 共 {len(terms)} 个术语，每条都有**中文 / 英文 / 德文**名称和一句话解释。"
               "前面按入门模块的顺序排（读到哪个模块就看哪一组），后面是读论文时会遇到的其他词，按领域分组。"
               "源文件在 `glossary/*.yaml`。\n"]
    else:
        out = ["# Glossary\n",
               f"> {len(terms)} terms, each with a **English / 中文 / Deutsch** name and a one-sentence "
               "definition. The first groups follow the onboarding modules (read the group for the "
               "module you are on); the rest are terms you meet in the papers, grouped by domain. "
               "Source files: `glossary/*.yaml`.\n"]
    for m in modules:
        ids = [i for i in (m.get("terms") or []) if i in by_id]
        if not ids:
            continue
        title = m["title"]["zh" if lang == "zh" else "en"]
        out.append(f"## {title}\n")
        out.extend(_entry(by_id[i], lang, m) for i in ids)
    rest = defaultdict(list)
    for t in terms:
        if t["id"] not in taught:
            rest[t.get("domain", "general")].append(t)
    if rest:
        out.append("## 读论文时会遇到的其他词\n" if lang == "zh" else "## More terms from the papers\n")
        for dom in [d for d, _ in DOMAIN_ORDER] + sorted(set(rest) - set(DOMAIN_LABEL)):
            items = sorted(rest.get(dom, []), key=lambda x: x.get("en", "").lower())
            if not items:
                continue
            label = DOMAIN_LABEL.get(dom, dom)
            label = label.split(" / ")[1] if (lang == "zh" and " / " in label) else label.split(" / ")[0]
            out.append(f"### {label}\n")
            out.extend(_entry(t, lang, None).replace("### ", "#### ", 1) for t in items)
    return "\n".join(out) + "\n"


def module_table(module: dict, terms: list[dict], lang: str) -> str:
    """The 'Terms in this module' table appended to an onboarding page."""
    by_id = {t["id"]: t for t in terms}
    ids = [i for i in (module.get("terms") or []) if i in by_id]
    if not ids:
        return ""
    if lang == "zh":   # the Chinese page pairs each term with its English name; the English page stays English
        rows = ["## 本模块名词\n", "| 中文 | English | 一句话 |", "|---|---|---|"]
    else:
        rows = ["## Terms in this module\n", "| Term | In one sentence |", "|---|---|"]
    for i in ids:
        t = by_id[i]
        d = _pick(t, lang, "def").replace("|", "\\|")
        if lang == "zh":
            rows.append(f"| [{t.get('zh', '')}](glossary.md#{i}) | {t.get('en', '')} | {d} |")
        else:
            rows.append(f"| [{t.get('en', '')}](glossary.md#{i}) | {d} |")
    return "\n".join(rows) + "\n"


def write() -> int:
    terms = load_terms()
    if not terms:
        print("! glossary/*.yaml missing or empty — nothing to build")
        return 0
    modules = load_modules()
    missing = sorted({i for m in modules for i in (m.get("terms") or [])} - {t["id"] for t in terms})
    if missing:
        print(f"! onboarding/modules.yaml names unknown glossary ids: {', '.join(missing)}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "glossary.md").write_text(render(terms, modules, "en"), encoding="utf-8")
    (OUT / "glossary.zh.md").write_text(render(terms, modules, "zh"), encoding="utf-8")
    return len(terms)


def main() -> None:
    n = write()
    if n:
        print(f"✓ glossary: {n} terms → docs/onboarding/glossary.md (+ .zh)")


if __name__ == "__main__":
    main()
