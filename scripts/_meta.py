"""Load papers/<slug>/metadata.yaml.

Prefers PyYAML; falls back to a minimal parser that understands the exact
subset our add_paper.py emitter produces (scalars + simple `- ` lists), so
build scripts run even before `pip install -r requirements.txt`.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"


def _mini_load(text: str) -> dict:
    out: dict = {}
    key = None
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") and key is not None:
            out.setdefault(key, [])
            out[key].append(_scalar(raw[4:].strip()))
            continue
        if ":" in raw and not raw.startswith(" "):
            k, _, v = raw.partition(":")
            key = k.strip()
            v = v.strip()
            if v == "" or v == "[]":
                out[key] = [] if v == "[]" else ""
                if v == "":
                    out[key] = None  # a following `- ` list, or empty
            else:
                out[key] = _scalar(v)
    return out


def _scalar(v: str):
    v = v.strip()
    if v in ("null", "~", ""):
        return None
    if v == "true":
        return True
    if v == "false":
        return False
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1].replace('\\"', '"')
    if v.lstrip("-").isdigit():
        return int(v)
    return v


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text) or {}
        return data
    except Exception:
        return _mini_load(text)


def all_meta() -> list[dict]:
    metas = []
    for f in sorted(PAPERS.glob("*/metadata.yaml")):
        m = load(f)
        m.setdefault("id", f.parent.name)
        m["_dir"] = f.parent.name
        metas.append(m)
    return metas
