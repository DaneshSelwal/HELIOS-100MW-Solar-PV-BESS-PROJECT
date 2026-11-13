"""Schedule progress & earned value: planned % by date from baseline weights, actual progress tracking, S-curve."""
from __future__ import annotations
import datetime as dt, json
from .world import ROOT, schedule

STATE = ROOT / "state"
ACT_FILE = STATE / "activities.json"     # live copy of L3 with pct_complete / actual dates / forecast


def _d(x) -> dt.date:
    return x if isinstance(x, dt.date) else dt.date.fromisoformat(str(x))


def baseline() -> list[dict]:
    acts = schedule()["level3"]; tot = sum(a["weight"] for a in acts) or 1
    out = []
    for a in acts:
        b = dict(a); b["w"] = a["weight"] / tot; b["start"] = str(a["start"]); b["finish"] = str(a["finish"])
        b.setdefault("pct_complete", 0); b.setdefault("actual_start", None); b.setdefault("actual_finish", None)
        b.setdefault("forecast_start", b["start"]); b.setdefault("forecast_finish", b["finish"])
        out.append(b)
    return out


def load() -> list[dict]:
    if ACT_FILE.exists():
        return json.loads(ACT_FILE.read_text(encoding="utf-8"))
    acts = baseline(); save(acts); return acts


def save(acts: list[dict]) -> None:
    STATE.mkdir(exist_ok=True); ACT_FILE.write_text(json.dumps(acts, indent=1), encoding="utf-8")


def planned_pct(acts: list[dict], on: dt.date) -> float:
    tot = 0.0
    for a in acts:
        s, f = _d(a["start"]), _d(a["finish"])
        if on >= f: frac = 1.0
        elif on < s: frac = 0.0
        else: frac = ((on - s).days + 1) / ((f - s).days + 1)
        tot += a["w"] * frac
    return round(100 * tot, 2)


def earned_pct(acts: list[dict]) -> float:
    return round(100 * sum(a["w"] * (a.get("pct_complete") or 0) / 100 for a in acts), 2)


def advance_naturally(acts: list[dict], on: dt.date, productivity: float = 1.0, lost_day: bool = False) -> list[str]:
    """Default progress model: activities in their forecast window progress linearly * productivity.
    Returns list of activity ids that progressed. The Director can override via explicit updates."""
    moved = []
    if lost_day:
        return moved
    for a in acts:
        if a.get("milestone"):
            continue
        s, f = _d(a["forecast_start"]), _d(a["forecast_finish"])
        if s <= on <= f and (a.get("pct_complete") or 0) < 100:
            dur = (f - s).days + 1
            inc = 100 / dur * productivity
            if not a.get("actual_start"):
                a["actual_start"] = on.isoformat()
            a["pct_complete"] = min(100.0, round((a.get("pct_complete") or 0) + inc, 2))
            if a["pct_complete"] >= 100:
                a["actual_finish"] = on.isoformat()
            moved.append(a["id"])
        elif on > f and (a.get("pct_complete") or 0) < 100 and a.get("actual_start"):
            # overran forecast finish: slip forecast by one day, keep progressing slowly
            a["forecast_finish"] = (f + dt.timedelta(days=1)).isoformat()
            a["pct_complete"] = min(100.0, round((a.get("pct_complete") or 0) + 100 / max(5, (f - s).days + 1) * 0.6 * productivity, 2))
            if a["pct_complete"] >= 100:
                a["actual_finish"] = on.isoformat()
            moved.append(a["id"])
    return moved


def slip(acts: list[dict], activity_id: str, days: int, cascade: bool = True) -> list[str]:
    """Push an activity's forecast by N days and cascade to successors (finish-to-start, simple)."""
    byid = {a["id"]: a for a in acts}; touched = []
    def push(aid: str, d: int):
        a = byid[aid]
        if (a.get("pct_complete") or 0) >= 100: return
        a["forecast_start"] = (_d(a["forecast_start"]) + dt.timedelta(days=d)).isoformat()
        a["forecast_finish"] = (_d(a["forecast_finish"]) + dt.timedelta(days=d)).isoformat()
        touched.append(aid)
        if cascade:
            for b in acts:
                if aid in b.get("pred", []) and _d(b["forecast_start"]) < _d(a["forecast_finish"]) + dt.timedelta(days=1):
                    push(b["id"], (_d(a["forecast_finish"]) + dt.timedelta(days=1) - _d(b["forecast_start"])).days)
    push(activity_id, days); return touched


def forecast_completion(acts: list[dict]) -> dt.date:
    return max(_d(a["forecast_finish"]) for a in acts)


def active_on(acts: list[dict], on: dt.date) -> list[dict]:
    return [a for a in acts if _d(a["forecast_start"]) <= on <= _d(a["forecast_finish"]) and (a.get("pct_complete") or 0) < 100]


def upcoming(acts: list[dict], on: dt.date, days: int = 14) -> list[dict]:
    return [a for a in acts if on < _d(a["forecast_start"]) <= on + dt.timedelta(days=days)]


def s_curve_png(path, acts: list[dict], progress_rows: list[dict], data_date: dt.date) -> None:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    start = min(_d(a["start"]) for a in acts); end = max(_d(a["finish"]) for a in acts)
    days = [(start + dt.timedelta(days=i)) for i in range(0, (end - start).days + 1, 7)]
    plan = [planned_pct(acts, d) for d in days]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(days, plan, label="Planned (baseline)", color="#1F3A5F")
    if progress_rows:
        xs = [_d(r["date"]) for r in progress_rows]; ys = [float(r["earned_pct"]) for r in progress_rows]
        ax.plot(xs, ys, label="Earned (actual)", color="#2E7D32", linewidth=2)
    ax.axvline(data_date, color="#C62828", linestyle="--", label=f"Data date {data_date}")
    ax.set_ylabel("% complete"); ax.set_ylim(0, 100); ax.grid(alpha=.3); ax.legend(); ax.set_title("HELIOS — Overall progress S-curve")
    fig.autofmt_xdate(); fig.tight_layout(); fig.savefig(path, dpi=130); plt.close(fig)
