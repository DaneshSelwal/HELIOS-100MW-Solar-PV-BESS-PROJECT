"""The daily loop: events → Director plan → role agents → apply → diary/brief/dashboard → commit."""
from __future__ import annotations
import datetime as dt, json, time, traceback
from . import world, clock, events, prompts, registers, progress, actions, diary, git_ops
from .engine import agy

ROOT = world.ROOT
MAX_ROLES_PER_DAY = 7


def _acts_summary(acts: list[dict], d: dt.date) -> str:
    rows = progress.active_on(acts, d) + progress.upcoming(acts, d, 21)
    return "\n".join(f"{a['id']} | {a['name']} | {a['start']}→{a['finish']} | fc {a['forecast_start']}→{a['forecast_finish']} | {a.get('pct_complete',0):.0f}%" for a in rows[:60]) or "(nothing active yet)"


def _acts_for_role(acts: list[dict], d: dt.date, role_id: str) -> str:
    wbs_map = {"epc-engineering-lead": "W03 W04 W05 W06", "epc-scm-lead": "W07 W09", "epc-buyer": "W07 W09", "epc-construction-manager": "W10 W11 W12 W13 W14 W15",
               "sub-civil": "W10 W11", "sub-mms": "W11 W12", "sub-electrical": "W13", "sub-substation": "W14", "epc-contracts-manager": "W08"}
    allowed = wbs_map.get(role_id)
    rows = [a for a in progress.active_on(acts, d) + progress.upcoming(acts, d, 30) if not allowed or a["wbs"] in allowed.split()]
    return "\n".join(f"{a['id']} ({a['wbs']}) {a['name']}: fc {a['forecast_start']}→{a['forecast_finish']}, {a.get('pct_complete',0):.0f}% complete" for a in rows[:40]) or "(no activities in your window yet)"


def _open_items() -> str:
    acts = [f"ACTION {a['id']} {a['action'][:70]} (owner {a['owner']}, due {a['due_date']})" for a in registers.read("actions") if a["status"] == "Open"][-25:]
    rfis = [f"RFI {r['ref']} {r['subject'][:70]} ({r['status']})" for r in registers.read("rfi") if r["status"].lower() not in ("closed", "answered")][-15:]
    ncrs = [f"NCR {r['ref']} {r['description'][:70]} ({r['status']})" for r in registers.read("ncr") if r["status"].lower() != "closed"][-10:]
    return "\n".join(acts + rfis + ncrs) or "(none)"


def _due_today(day: int) -> list[dict]:
    return [dict(x) for x in world.load("genesis")["deliverables"] if x["day"] == day]


def _yesterday_diary(day: int) -> str:
    if day <= 0: return "(project starts today)"
    p = ROOT / "diary" / f"{clock.date_of(day - 1).isoformat()}_D{day - 1:03d}.md"
    return p.read_text(encoding="utf-8") if p.exists() else "(no diary yesterday)"


def run_day(day: int, *, push: bool = True, max_roles: int = MAX_ROLES_PER_DAY, dry: bool = False) -> dict:
    """Simulate one day. On any failure the working tree is rolled back to the last commit."""
    t0 = time.time(); d = clock.date_of(day); today = events.today(day); today["max_roles"] = max_roles
    registers.init_all(); acts = progress.load()
    models_used: dict[str, str] = {}
    try:
        # 1. Director
        director_cfg = world.director()
        due = _due_today(day)
        dprompt = prompts.director_prompt(today, _acts_summary(acts, d), due, registers.all_inboxes(), _yesterday_diary(day), _open_items())
        if today["working_day"] or today["happenings"] or due:
            director, m = agy.run(dprompt, director_cfg["model"], prompts.DIRECTOR_SCHEMA, timeout_s=240)
            models_used["simulation-director"] = m
        else:
            director = {"narrative": f"{today['weekday']}: non-working day. No site or office activity.", "events_interpretation": [], "day_plan": [], "site": {"manpower": 0, "productivity": 0}, "notes_for_log": ""}
        # ensure scripted deliverables are present even if the Director forgot them
        plan_by_role: dict[str, dict] = {}
        for p in director.get("day_plan", []):
            if p["role"] in world.roles():
                plan_by_role.setdefault(p["role"], {"tasks": [], "must_produce": []})
                plan_by_role[p["role"]]["tasks"] += p.get("tasks", []); plan_by_role[p["role"]]["must_produce"] += p.get("must_produce", [])
        for x in due:
            pr = plan_by_role.setdefault(x["owner"], {"tasks": [], "must_produce": []})
            if not any(mp.get("title") == x["title"] for mp in pr["must_produce"]):
                mp = {k: v for k, v in x.items() if k not in ("day", "owner")}
                if mp["kind"] == "letter": mp["to_role"] = mp.pop("to")
                pr["must_produce"].append(mp)
        roles_today = list(plan_by_role)[:max_roles]
        # 2. apply event slips from Director
        for e in director.get("events_interpretation", []):
            for a in e.get("affected_activities", []):
                if a.get("slip_days"):
                    progress.slip(acts, a["id"], int(a["slip_days"]))
            registers.append("events", {"day": day, "date": d.isoformat(), "event_id": e["event_id"], "description": e["visible_description"], "visible_to": ",".join(e.get("affected_roles", [])), "effect": json.dumps(e.get("affected_activities", []))})
        progress.save(acts)
        # 3. natural progress
        prod = float(director.get("site", {}).get("productivity", 1.0) or 0)
        if today["working_day"]:
            progress.advance_naturally(acts, d, productivity=max(0.0, min(1.3, prod)) if day >= 0 else 1.0, lost_day=today["weather"]["lost_day"])
            progress.save(acts)
        # 4. role agents
        summaries: dict[str, str] = {}; produced: dict[str, dict] = {}; applied_log: list[str] = []
        roles = world.roles()
        for rid in roles_today:
            r = roles[rid]; inbox = registers.inbox(rid)
            prompt = prompts.agent_prompt(rid, today, plan_by_role[rid], inbox[-12:], _acts_for_role(acts, d, rid), "")
            heavy = any(mp.get("kind") in ("document",) and ("Contract" in mp.get("title", "") or "Execution Plan" in mp.get("title", "")) for mp in plan_by_role[rid]["must_produce"])
            model = r.get("heavy_model") if heavy and r.get("heavy_model") else r["model"]
            if dry:
                out, m = {"summary": "(dry run)", "documents": [], "letters": [], "emails": [], "meeting_minutes": [], "register_updates": [], "schedule_updates": [], "requests": []}, "dry"
            else:
                out, m = agy.run(prompt, model, prompts.AGENT_SCHEMA, timeout_s=420)
            models_used[rid] = m
            produced[rid] = actions.apply(rid, out, day, applied_log)
            summaries[rid] = out.get("summary", "")
            registers.clear(rid, [i.get("ref") for i in inbox])   # handled
        # 5. observer outputs
        acts = progress.load()
        diary.record_progress(day, director.get("notes_for_log", "")[:120])
        diary.write_diary(day, today, director, summaries, produced, applied_log)
        diary.write_brief(day, today, director, produced, applied_log)
        diary.export_registers(day); diary.write_status(day, today, director)
        clock.save(day, "ok")
        _append_log(day, today, director, roles_today, produced, models_used, time.time() - t0)
        # 6. commit
        sha = git_ops.commit_day(day, d.isoformat(), (director.get("narrative", "")[:70] or "quiet day"), push=push)
        return {"day": day, "date": d.isoformat(), "roles": roles_today, "produced": produced, "models": models_used, "commit": sha, "secs": round(time.time() - t0)}
    except agy.QuotaExhausted as e:
        git_ops.rollback_to_head()
        _append_log_line(f"- Day {day:03d} PAUSED — quota exhausted on {e.model}: {e.message}. State rolled back; re-run when quota resets.")
        raise
    except Exception:
        git_ops.rollback_to_head()
        _append_log_line(f"- Day {day:03d} FAILED and rolled back:\n```\n{traceback.format_exc()[-1500:]}\n```")
        raise


def _append_log_line(line: str) -> None:
    with open(ROOT / "HELIOS_LOG.md", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _append_log(day, today, director, roles_today, produced, models, secs) -> None:
    tot = {k: sum(p.get(k, 0) for p in produced.values()) for k in ("documents", "letters", "emails", "moms", "registers", "schedule", "requests")}
    u = agy.usage_summary(dt.datetime.now().replace(microsecond=0).isoformat()[:10])
    calls = sum(v["calls"] for v in u.values()); toks = sum(v["in"] + v["out"] for v in u.values())
    _append_log_line(f"- **{clock.label(day)}** [{int(secs)} s] roles: {', '.join(roles_today) or 'none'} | produced: " +
                     ", ".join(f"{v} {k}" for k, v in tot.items() if v) + f" | models: {', '.join(sorted(set(models.values())))} | agy today so far: {calls} calls, {toks:,} tokens. {director.get('notes_for_log','')[:160]}")
