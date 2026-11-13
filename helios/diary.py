"""Daily outputs for the observer: site diary, morning brief, dashboard STATUS.md, register exports, S-curve."""
from __future__ import annotations
import datetime as dt, json
from . import world, registers, progress, clock, numbering
from .render import xlsx

ROOT = world.ROOT


def write_diary(day: int, today: dict, director: dict, role_summaries: dict[str, str], produced: dict[str, dict], applied_log: list[str]) -> str:
    d = clock.date_of(day); roles = world.roles()
    lines = [f"# {clock.label(day)}", "", f"**Phase(s):** {', '.join(today['phases'])}  ",
             f"**Weather:** {today['weather']['condition']}, {today['weather']['tmin']}..{today['weather']['tmax']} °C" + (" — **site lost day**" if today['weather']['lost_day'] else "") + "  ",
             f"**Site manpower:** {director.get('site', {}).get('manpower', 0)}  ", "", "## Narrative", director.get("narrative", ""), ""]
    if director.get("events_interpretation"):
        lines += ["## Events"] + [f"- **{e['event_id']}** — {e['visible_description']}" + (f" (affects: {', '.join(a['id'] + ('+%dd' % a['slip_days'] if a['slip_days'] else '') for a in e['affected_activities'])})" if e.get('affected_activities') else "") for e in director["events_interpretation"]] + [""]
    lines.append("## What people did")
    for rid, s in role_summaries.items():
        r = roles[rid]; p = produced.get(rid, {})
        made = ", ".join(f"{v} {k}" for k, v in p.items() if v)
        lines.append(f"- **{r['name']}** ({r['title']}): {s}" + (f" _[{made}]_" if made else ""))
    lines += ["", "## Files produced"] + [f"- {l}" for l in applied_log if l.startswith(("DOC", "LETTER", "MOM"))] or ["- none"]
    acts = progress.load(); plan = progress.planned_pct(acts, d); earn = progress.earned_pct(acts)
    lines += ["", "## Progress", f"Planned {plan:.2f}% | Earned {earn:.2f}% | SPI {(earn / plan if plan else 1):.2f} | Forecast completion {progress.forecast_completion(acts)}", ""]
    txt = "\n".join(lines) + "\n"
    p = ROOT / "diary" / f"{d.isoformat()}_D{day:03d}.md"; p.parent.mkdir(exist_ok=True); p.write_text(txt, encoding="utf-8")
    return txt


def write_brief(day: int, today: dict, director: dict, produced: dict, applied_log: list[str]) -> None:
    d = clock.date_of(day); acts = progress.load(); plan = progress.planned_pct(acts, d); earn = progress.earned_pct(acts)
    open_actions = [a for a in registers.read("actions") if a["status"] == "Open"]
    open_rfi = [r for r in registers.read("rfi") if r["status"].lower() not in ("closed", "answered")]
    open_ncr = [r for r in registers.read("ncr") if r["status"].lower() != "closed"]
    letters = [r for r in registers.read("correspondence") if int(r["day"]) == day]
    docs = [r for r in registers.read("documents") if int(r["issued_day"]) == day]
    lines = [f"# Morning brief — {clock.label(day)}", "", f"_{director.get('narrative','')}_", "",
             "| Planned % | Earned % | SPI | Forecast PAC | Open actions | Open RFIs | Open NCRs |", "|---|---|---|---|---|---|---|",
             f"| {plan:.1f} | {earn:.1f} | {(earn / plan if plan else 1):.2f} | {progress.forecast_completion(acts)} | {len(open_actions)} | {len(open_rfi)} | {len(open_ncr)} |", "",
             "## Today's documents"] + [f"- `{r['doc_no']}` {r['title']} (Rev {r['rev']}) — {r['path']}" for r in docs] + (["- none"] if not docs else []) + \
            ["", "## Today's letters"] + [f"- `{r['ref']}` {r['from_role']} → {r['to_role']}: {r['subject']}" for r in letters] + (["- none"] if not letters else []) + \
            ["", "## Watch list"] + [f"- {e['visible_description']}" for e in director.get("events_interpretation", [])] + (["- quiet day"] if not director.get("events_interpretation") else []) + \
            ["", "## Next 14 days (schedule)"] + [f"- {a['id']} {a['name']} — forecast start {a['forecast_start']}" for a in progress.upcoming(acts, d)[:12]]
    p = ROOT / "brief" / f"{d.isoformat()}_D{day:03d}.md"; p.parent.mkdir(exist_ok=True); p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_registers(day: int) -> None:
    d = clock.date_of(day)
    targets = {"documents": ("18", "03", "Master Document Register"), "correspondence": ("18", "01", "Correspondence Log"),
               "risk": ("1", "06", "Risk Register"), "actions": ("1", "09", "Action Register"), "change": ("1", "10", "Change Register"),
               "procurement": ("4", "09", "Procurement Register"), "rfi": ("10", "05", "RFI and MIR Register"), "ncr": ("10", "03", "NCR Register"),
               "payments": ("8", "02", "Payment Register"), "hse": ("11", "03", "HSE Statistics")}
    for name, (top, sub, title) in targets.items():
        rows = registers.read(name)
        xlsx.table(numbering.folder(top, sub) / f"HEL001-REG-{name.upper()}.xlsx", sheet=name.title(), columns=registers.SCHEMAS[name],
                   rows=[[r.get(c, "") for c in registers.SCHEMAS[name]] for r in rows], title=f"{title} — updated {d:%d %b %Y}")
    acts = progress.load()
    xlsx.schedule(numbering.folder("1", "04") / "HEL001-G000-P-&SCH-00001-00_Baseline_and_Update_L3.xlsx", title="HELIOS Schedule L3 — baseline vs update",
                  activities=[{**a, "start": a["forecast_start"], "finish": a["forecast_finish"]} for a in acts], data_date=d)
    progress.s_curve_png(ROOT / "dashboard" / "s_curve.png", acts, registers.read("progress"), d)


def record_progress(day: int, note: str = "") -> None:
    d = clock.date_of(day); acts = progress.load(); plan = progress.planned_pct(acts, d); earn = progress.earned_pct(acts)
    registers.append("progress", {"day": day, "date": d.isoformat(), "planned_pct": plan, "earned_pct": earn, "actual_cost_pct": earn,
                                  "spi": round(earn / plan, 3) if plan else 1.0, "cpi": 1.0, "note": note})


def write_status(day: int, today: dict, director: dict) -> None:
    d = clock.date_of(day); acts = progress.load(); plan = progress.planned_pct(acts, d); earn = progress.earned_pct(acts)
    docs = registers.read("documents"); let = registers.read("correspondence")
    active = progress.active_on(acts, d)
    lines = [f"# HELIOS — Project Status", "", f"**Data date:** {clock.label(day)} | **Phase(s):** {', '.join(today['phases'])} | **Forecast PAC:** {progress.forecast_completion(acts)} (baseline 2028-05-31)", "",
             f"**Progress:** planned {plan:.1f}% · earned {earn:.1f}% · SPI {(earn / plan if plan else 1):.2f}", "", "![S-curve](s_curve.png)", "",
             f"**Documents issued:** {len(docs)} · **Letters:** {len(let)} · **Open actions:** {sum(a['status']=='Open' for a in registers.read('actions'))} · **Open RFIs:** {sum(r['status'].lower() not in ('closed','answered') for r in registers.read('rfi'))} · **NCRs open:** {sum(r['status'].lower()!='closed' for r in registers.read('ncr'))}", "",
             "## Active activities", "| ID | Activity | Forecast | % |", "|---|---|---|---|"] + [f"| {a['id']} | {a['name']} | {a['forecast_start']} → {a['forecast_finish']} | {a.get('pct_complete',0):.0f} |" for a in active[:25]] + \
            ["", "## Latest narrative", director.get("narrative", ""), "", "## Recent documents"] + [f"- `{r['doc_no']}` {r['title']} (Day {r['issued_day']})" for r in docs[-15:]]
    (ROOT / "dashboard" / "STATUS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
