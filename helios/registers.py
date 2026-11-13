"""CSV-backed project registers and agent inboxes (state/registers/*.csv, state/inbox/<role>.json)."""
from __future__ import annotations
import csv, json, pathlib
from .world import ROOT

REG_DIR = ROOT / "state" / "registers"
INBOX_DIR = ROOT / "state" / "inbox"

SCHEMAS: dict[str, list[str]] = {
    "documents":      ["doc_no", "title", "type", "area", "discipline", "rev", "status", "originator", "owner_role", "issued_day", "issued_date", "path", "review_code", "notes"],
    "correspondence": ["ref", "day", "date", "from_org", "from_role", "to_org", "to_role", "subject", "kind", "reply_to", "path", "status"],
    "rfi":            ["ref", "day", "date", "area", "discipline", "raised_by", "subject", "status", "answered_day", "answer_summary"],
    "ncr":            ["ref", "day", "date", "area", "raised_by", "description", "severity", "status", "closed_day", "root_cause"],
    "risk":           ["id", "day_raised", "category", "description", "probability", "impact", "score", "owner", "mitigation", "status"],
    "change":         ["ref", "day", "date", "title", "raised_by", "type", "cost_impact_usd", "time_impact_days", "status", "notes"],
    "procurement":    ["package", "vendor", "stage", "rfq_day", "award_day", "po_ref", "value_usd", "promised_delivery", "forecast_delivery", "status", "notes"],
    "actions":        ["id", "day", "source", "action", "owner", "due_date", "status", "closed_day"],
    "payments":       ["ref", "day", "date", "kind", "party", "period", "gross_usd", "retention_usd", "advance_recovery_usd", "net_usd", "status"],
    "progress":       ["day", "date", "planned_pct", "earned_pct", "actual_cost_pct", "spi", "cpi", "note"],
    "hse":            ["day", "date", "manpower", "manhours", "near_miss", "first_aid", "lti", "toolbox_talks", "note"],
    "events":         ["day", "date", "event_id", "description", "visible_to", "effect"],
}


def path(name: str) -> pathlib.Path:
    REG_DIR.mkdir(parents=True, exist_ok=True)
    return REG_DIR / f"{name}.csv"


def read(name: str) -> list[dict]:
    p = path(name)
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(name: str, rows: list[dict]) -> None:
    cols = SCHEMAS[name]
    with open(path(name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


def append(name: str, row: dict) -> None:
    rows = read(name); rows.append(row); write(name, rows)


def update_where(name: str, key: str, value: str, **changes) -> int:
    rows = read(name); n = 0
    for r in rows:
        if r.get(key) == value:
            r.update({k: str(v) for k, v in changes.items()}); n += 1
    write(name, rows); return n


def init_all() -> None:
    for name in SCHEMAS:
        if not path(name).exists():
            write(name, [])


# ---------------- inboxes ----------------
def inbox_path(role_id: str) -> pathlib.Path:
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    return INBOX_DIR / f"{role_id}.json"


def inbox(role_id: str) -> list[dict]:
    p = inbox_path(role_id)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def send(role_id: str, item: dict) -> None:
    """item: {day, from, kind, ref, subject, summary, due_day?}"""
    items = inbox(role_id); items.append(item)
    inbox_path(role_id).write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")


def clear(role_id: str, refs: list[str]) -> None:
    items = [i for i in inbox(role_id) if i.get("ref") not in refs]
    inbox_path(role_id).write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")


def all_inboxes() -> dict[str, list[dict]]:
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in INBOX_DIR.glob("*.json")}
