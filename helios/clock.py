"""Simulation calendar: day counter <-> date, working days, phase detection, holidays."""
from __future__ import annotations
import datetime as dt, json
from .world import ROOT, charter, schedule, event_deck

STATE = ROOT / "state"
CLOCK = STATE / "clock.json"


def day0() -> dt.date:
    return dt.date.fromisoformat(str(charter()["simulation"]["day0"]))


def date_of(day: int) -> dt.date:
    return day0() + dt.timedelta(days=day)


def day_of(d: dt.date) -> int:
    return (d - day0()).days


def holidays() -> set[dt.date]:
    ch = charter()["calendar"]
    hs = set()
    for k in ("public_holidays_2027", "public_holidays_2028"):
        for x in ch.get(k, []):
            hs.add(dt.date.fromisoformat(str(x)))
    for h in event_deck().get("holidays_extra", []):
        d0 = dt.date.fromisoformat(str(h["date"]))
        for i in range(int(h.get("days", 1))):
            hs.add(d0 + dt.timedelta(days=i))
    return hs


def is_working_day(d: dt.date) -> bool:
    return d.weekday() != 6 and d not in holidays()   # Mon-Sat site week


def phases_on(d: dt.date) -> list[str]:
    out = []
    for p in schedule()["level1"]:
        if dt.date.fromisoformat(str(p["start"])) <= d <= dt.date.fromisoformat(str(p["finish"])):
            out.append(p["id"])
    return out or ["P6"]


def load() -> dict:
    if CLOCK.exists():
        return json.loads(CLOCK.read_text())
    return {"day": -1, "date": None, "status": "not_started"}


def save(day: int, status: str = "ok") -> dict:
    STATE.mkdir(exist_ok=True)
    c = {"day": day, "date": date_of(day).isoformat(), "weekday": date_of(day).strftime("%a"),
         "working_day": is_working_day(date_of(day)), "phases": phases_on(date_of(day)), "status": status}
    CLOCK.write_text(json.dumps(c, indent=2))
    return c


def label(day: int) -> str:
    d = date_of(day)
    return f"Day {day:03d} ({d.isoformat()}, {d.strftime('%a')})"
