"""Event engine: recurring items, random draws (seeded), hidden-truth surprises. Produces the day's 'happenings'
that the Simulation Director turns into concrete work. Only this module reads world/truth.yaml."""
from __future__ import annotations
import datetime as dt, random
from . import world, clock

WEEKDAYS = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}


def _rng(day: int) -> random.Random:
    return random.Random(f"{world.charter()['simulation']['seed']}-{day}")


def recurring(day: int) -> list[dict]:
    d = clock.date_of(day); out = []
    for r in world.event_deck()["recurring"]:
        if day < r.get("from_day", 0) or day > r.get("to_day", 10**6):
            continue
        hit = False
        if r.get("daily"):
            hit = clock.is_working_day(d)
        elif "weekday" in r:
            hit = d.weekday() == WEEKDAYS[r["weekday"]]
            if hit and r.get("every_n_weeks", 1) > 1:
                hit = ((day - r.get("from_day", 0)) // 7) % r["every_n_weeks"] == 0
        elif "day_of_month" in r:
            hit = d.day == r["day_of_month"]
        if hit:
            out.append({"id": r["id"], "kind": "recurring", "name": r["name"], "owner": r["owner"], "output": r.get("output")})
    return out


def random_events(day: int) -> list[dict]:
    d = clock.date_of(day)
    if not clock.is_working_day(d):
        return []
    rng = _rng(day); phases = set(clock.phases_on(d)); out = []
    roles = world.roles()
    subs = [r for r, v in roles.items() if v.get("kind") == "external" and roles[r].get("kind") == "external" and v.get("code", "").startswith("S")]
    vendors = [r for r, v in roles.items() if v.get("kind") == "external" and v.get("code", "").startswith("V")]
    auths = ["grid-operator", "local-authority"]
    for e in world.event_deck()["random"]:
        if not (set(e["phase"]) & phases):
            continue
        if rng.random() < e["p"]:
            owner = e["owner"]
            if owner == "random_subcontractor": owner = rng.choice(subs)
            elif owner == "random_vendor": owner = rng.choice(vendors)
            elif owner == "random_authority": owner = rng.choice(auths)
            out.append({"id": e["id"], "kind": "random", "name": e["name"], "owner": owner})
    return out


def weather(day: int) -> dict:
    """Visible weather for the day, drawn from hidden monthly climate. lost_day=True means site work stops."""
    d = clock.date_of(day); rng = _rng(day * 7 + 1)
    m = world.truth()["weather_navoi_monthly"][f"{d.month:02d}"]
    tmin = m["tmin"] + rng.randint(-3, 3); tmax = m["tmax"] + rng.randint(-3, 3)
    p_lost = m["lost_days"] / 26
    r = rng.random()
    if r < p_lost * 0.5:
        cond, lost = ("strong wind (>12 m/s), lifting works stopped" if m["wind_days"] >= 4 else "heavy rain, earthworks stopped"), True
    elif r < p_lost:
        cond, lost = ("dust storm, site evacuated to camp" if d.month in (4, 5, 9, 10) else ("extreme heat, work 13:00-16:00 suspended" if tmax >= 38 else "rain, partial stoppage")), True
    elif r < p_lost + 0.15:
        cond, lost = "overcast, moderate wind", False
    else:
        cond, lost = ("clear, hot" if tmax >= 33 else "clear" if tmax >= 15 else "clear, cold"), False
    return {"tmin": tmin, "tmax": tmax, "condition": cond, "lost_day": lost}


def surprises(day: int) -> list[dict]:
    return [{"id": s["id"], "kind": "surprise", "name": s["text"], "owner": "simulation-director"}
            for s in world.truth()["scripted_surprises"] if s["day"] == day]


def today(day: int) -> dict:
    d = clock.date_of(day)
    return {"day": day, "date": d.isoformat(), "weekday": d.strftime("%A"), "working_day": clock.is_working_day(d),
            "phases": clock.phases_on(d), "weather": weather(day),
            "happenings": recurring(day) + random_events(day) + surprises(day)}
