"""Allocate document numbers from world/numbering.yaml and resolve filing paths."""
from __future__ import annotations
import json, re
from .world import ROOT, numbering

STATE = ROOT / "state"
COUNTERS = STATE / "counters.json"


def _load() -> dict:
    return json.loads(COUNTERS.read_text()) if COUNTERS.exists() else {}


def _save(c: dict) -> None:
    STATE.mkdir(exist_ok=True)
    COUNTERS.write_text(json.dumps(c, indent=2, sort_keys=True))


def next_seq(key: str) -> int:
    c = _load(); c[key] = c.get(key, 0) + 1; _save(c); return c[key]


def technical(area: str, disc: str, dtype: str, rev: str = "A") -> str:
    n = numbering(); seq = next_seq(f"tech|{area}|{disc}|{dtype}")
    return n["patterns"]["technical"].format(project=n["project_code"], area=area, disc=disc, type=dtype, seq=seq, rev=rev)


def letter(dept: str, frm: str, to: str) -> str:
    n = numbering(); seq = next_seq(f"letter|{dept}|{frm}|{to}")
    return n["patterns"]["letter"].format(project=n["project_code"], dept=dept, **{"from": frm}, to=to, seq=seq)


def site_form(area: str, disc: str, form: str) -> str:
    n = numbering(); seq = next_seq(f"form|{area}|{disc}|{form}")
    return n["patterns"]["site_form"].format(project=n["project_code"], area=area, disc=disc, form=form, seq=seq)


def mgmt_plan(dept: str, frm: str, to: str, rev2: str = "00") -> str:
    n = numbering(); seq = next_seq(f"plan|{dept}|{frm}|{to}")
    return n["patterns"]["mgmt_plan"].format(dept=dept, **{"from": frm}, to=to, seq=seq, rev2=rev2)


def transmittal(frm: str, to: str) -> str:
    n = numbering(); seq = next_seq(f"tx|{frm}|{to}")
    return n["patterns"]["transmittal"].format(project=n["project_code"], **{"from": frm}, to=to, seq=seq)


def mom(kind: str) -> str:
    n = numbering(); seq = next_seq(f"mom|{kind}")
    return n["patterns"]["mom"].format(project=n["project_code"], kind=kind, seq=seq)


def safe_title(title: str, maxlen: int = 60) -> str:
    t = re.sub(r"[^\w\s\-&]+", "", title).strip()
    t = re.sub(r"\s+", "_", t)
    return t[:maxlen]


def folder(top_key: str, sub_key: str) -> "pathlib.Path":
    """Resolve a project folder by prefix numbers, e.g. folder('1', '04') -> project/1_Project_Mgmt/04_Schedule."""
    import pathlib
    tree = numbering()["folder_tree"]
    top = next(k for k in tree if k.split("_")[0] == str(top_key))
    sub = next(s for s in tree[top] if s.split("_")[0] == str(sub_key))
    p = ROOT / "project" / top / sub
    p.mkdir(parents=True, exist_ok=True)
    return p
