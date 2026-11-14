"""Prompt and JSON-schema builders for the Simulation Director and for role agents."""
from __future__ import annotations
import json
from . import world, registers, personas

DIRECTOR_SCHEMA = {
    "type": "object",
    "properties": {
        "narrative": {"type": "string", "description": "2-4 sentences: what kind of day this is on the project"},
        "events_interpretation": {"type": "array", "items": {"type": "object", "properties": {
            "event_id": {"type": "string"}, "visible_description": {"type": "string"},
            "affected_activities": {"type": "array", "items": {"type": "object", "properties": {"id": {"type": "string"}, "slip_days": {"type": "integer"}}, "required": ["id", "slip_days"]}},
            "affected_roles": {"type": "array", "items": {"type": "string"}}}, "required": ["event_id", "visible_description", "affected_activities", "affected_roles"]}},
        "day_plan": {"type": "array", "items": {"type": "object", "properties": {
            "role": {"type": "string"}, "tasks": {"type": "array", "items": {"type": "string"}},
            "must_produce": {"type": "array", "items": {"type": "object", "properties": {
                "kind": {"type": "string", "enum": ["document", "letter", "email", "mom", "register", "schedule_update"]},
                "title": {"type": "string"}, "to_role": {"type": "string"}, "folder": {"type": "string"},
                "area": {"type": "string"}, "disc": {"type": "string"}, "type": {"type": "string"}, "dept": {"type": "string"}, "mom_kind": {"type": "string"},
                "attendees": {"type": "array", "items": {"type": "string"}}, "notes": {"type": "string"}}, "required": ["kind", "title"]}}},
            "required": ["role", "tasks", "must_produce"]}},
        "site": {"type": "object", "properties": {"manpower": {"type": "integer"}, "productivity": {"type": "number"}}, "required": ["manpower", "productivity"]},
        "notes_for_log": {"type": "string"}},
    "required": ["narrative", "events_interpretation", "day_plan", "site", "notes_for_log"]}

SECTION = {"type": "object", "properties": {
    "heading": {"type": "string"}, "paragraphs": {"type": "array", "items": {"type": "string"}},
    "bullets": {"type": "array", "items": {"type": "string"}},
    "table": {"type": "object", "properties": {"columns": {"type": "array", "items": {"type": "string"}},
                                                "rows": {"type": "array", "items": {"type": "array", "items": {"type": "string"}}}}}},
    "required": ["heading"]}

AGENT_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string", "description": "2-3 sentences, first person, what you did today — goes in the site diary"},
        "documents": {"type": "array", "items": {"type": "object", "properties": {
            "title": {"type": "string"}, "folder": {"type": "string"}, "area": {"type": "string"}, "disc": {"type": "string"},
            "type": {"type": "string"}, "rev": {"type": "string"}, "status": {"type": "string"},
            "sections": {"type": "array", "items": SECTION}}, "required": ["title", "folder", "area", "disc", "type", "sections"]}},
        "letters": {"type": "array", "items": {"type": "object", "properties": {
            "to_role": {"type": "string"}, "dept": {"type": "string"}, "subject": {"type": "string"},
            "body_paragraphs": {"type": "array", "items": {"type": "string"}}, "cc_roles": {"type": "array", "items": {"type": "string"}},
            "reply_to_ref": {"type": "string"}, "attachments": {"type": "array", "items": {"type": "string"}},
            "requires_response_by_day": {"type": "integer"}}, "required": ["to_role", "dept", "subject", "body_paragraphs"]}},
        "emails": {"type": "array", "items": {"type": "object", "properties": {
            "to_roles": {"type": "array", "items": {"type": "string"}}, "subject": {"type": "string"}, "body": {"type": "string"}}, "required": ["to_roles", "subject", "body"]}},
        "meeting_minutes": {"type": "array", "items": {"type": "object", "properties": {
            "mom_kind": {"type": "string"}, "title": {"type": "string"}, "venue": {"type": "string"},
            "attendee_roles": {"type": "array", "items": {"type": "string"}},
            "items": {"type": "array", "items": {"type": "object", "properties": {"topic": {"type": "string"}, "discussion": {"type": "string"}}, "required": ["topic", "discussion"]}},
            "actions": {"type": "array", "items": {"type": "object", "properties": {"action": {"type": "string"}, "owner_role": {"type": "string"}, "due_date": {"type": "string"}}, "required": ["action", "owner_role", "due_date"]}}},
            "required": ["mom_kind", "title", "attendee_roles", "items", "actions"]}},
        "register_updates": {"type": "array", "items": {"type": "object", "properties": {
            "register": {"type": "string", "enum": ["rfi", "ncr", "risk", "change", "procurement", "actions", "hse", "payments"]},
            "op": {"type": "string", "enum": ["append", "update"]}, "key": {"type": "string"}, "value": {"type": "string"},
            "row": {"type": "object", "additionalProperties": {"type": "string"}}}, "required": ["register", "op", "row"]}},
        "schedule_updates": {"type": "array", "items": {"type": "object", "properties": {
            "activity_id": {"type": "string"}, "pct_complete": {"type": "number"}, "slip_days": {"type": "integer"}, "note": {"type": "string"}}, "required": ["activity_id", "note"]}},
        "requests": {"type": "array", "items": {"type": "object", "properties": {
            "to_role": {"type": "string"}, "what": {"type": "string"}, "due_day": {"type": "integer"}}, "required": ["to_role", "what"]}}},
    "required": ["summary", "documents", "letters", "emails", "meeting_minutes", "register_updates", "schedule_updates", "requests"]}


def charter_brief() -> str:
    c = world.charter(); p = c["project"]; k = p["contract"]
    ms = "; ".join(f"{m['code']} {m['name']} {m['date']}" for m in p["key_milestones"])
    return (f"PROJECT: {p['name']} ({p['code']}), {p['site']['name']}, {p['region']}, {p['country']}. "
            f"{p['capacity']['pv_ac_mw']} MWac / {p['capacity']['pv_dc_mwp']} MWp PV ({p['capacity']['pv_blocks']} blocks PV1-PV4, single-axis trackers, "
            f"{p['capacity']['module_wp']} Wp modules), BESS {p['capacity']['bess_power_mw']} MW / {p['capacity']['bess_energy_mwh']} MWh, "
            f"{p['capacity']['grid_connection_kv']} kV grid connection via 9 km OHTL. Site: {p['site']['description'].strip()} "
            f"CONTRACT: {k['type']}, USD {k['value_usd']:,}, signed {k['signed']} (Day 0), NTP {k['ntp']}, advance {k['advance_payment_pct']}%, retention {k['retention_pct']}%, "
            f"delay LDs {k['delay_ld_pct_per_week']}%/week capped {k['delay_ld_cap_pct']}%, time for completion {k['time_for_completion_months']} months, PAC target {k['pac_target']}. "
            f"PARTIES: EPC {c['parties']['epc']['name']} (HEP); Client {c['parties']['client']['name']} (QSE) — {c['parties']['client']['description']} "
            f"Owner's Engineer {c['parties']['owners_engineer']['name']} (OWE); grid operator {c['parties']['grid_operator']['name']} (GRD); authorities {c['parties']['authority']['name']} (GOV). "
            f"MILESTONES: {ms}. Site works Mon-Sat.")


def org_chart() -> str:
    lines = []
    for rid, r in world.roles().items():
        org = r.get("company") or r["org"]
        lines.append(f"- {rid}: {r['name']}, {r['title']} ({org})" + (f" — {r['package']}" if r.get("package") else ""))
    return "\n".join(lines)


def numbering_help() -> str:
    n = world.numbering()
    folders = "; ".join(f"{t.split('_')[0]}/{s.split('_')[0]}={t}/{s}" for t, subs in n["folder_tree"].items() for s in subs)
    return (f"DOC TYPES: {', '.join(f'{k}={v}' for k, v in n['doc_types'].items())}. AREAS: {', '.join(n['areas'])}. "
            f"DISCIPLINES: {', '.join(f'{k}={v}' for k, v in n['disciplines'].items())}. DEPTS (letters): {', '.join(n['departments'])}. "
            f"FOLDERS (use 'top/sub' codes): {folders}")


def recent_docs(limit: int = 40) -> str:
    rows = registers.read("documents")[-limit:]
    return "\n".join(f"- {r['doc_no']} {r['title']} (Rev {r['rev']}, {r['status']}, day {r['issued_day']})" for r in rows) or "- none yet"


def recent_letters(limit: int = 30) -> str:
    rows = registers.read("correspondence")[-limit:]
    return "\n".join(f"- {r['ref']} day {r['day']} {r['from_role']} → {r['to_role']}: {r['subject']} [{r['status']}]" for r in rows) or "- none yet"


def recent_moms(n: int = 2, max_chars: int = 5000) -> str:
    mm = world.ROOT / "state" / "moms"
    files = sorted(mm.glob("*.md"))[-n:] if mm.exists() else []
    txt = "\n\n".join(f.read_text(encoding="utf-8") for f in files)
    return txt[-max_chars:] if txt else "(no meetings yet)"


def director_prompt(today: dict, acts_summary: str, due: list[dict], inboxes: dict, yesterday_diary: str, open_items: str) -> str:
    return f"""You are the SIMULATION DIRECTOR of HELIOS, an EPC project simulation. You never appear in documents. Your job today is to
decide what happens on the project and who works on what, so that the project team (AI agents) produce realistic documents.

{charter_brief()}

ORGANISATION (role ids → people):
{org_chart()}

TODAY: Day {today['day']} — {today['date']} ({today['weekday']}), working day: {today['working_day']}, phases: {today['phases']}.
WEATHER: {today['weather']['condition']}, {today['weather']['tmin']}..{today['weather']['tmax']} °C, site lost day: {today['weather']['lost_day']}.

HAPPENINGS DRAWN BY THE EVENT ENGINE (you must turn each into a concrete, visible description and consequences):
{json.dumps(today['happenings'], ensure_ascii=False, indent=0)}

SCRIPTED DELIVERABLES DUE TODAY (must be in day_plan with the given owner; keep folder/area/disc/type/to/dept/mom_kind/attendees as given):
{json.dumps(due, ensure_ascii=False, indent=0) if due else '[]'}

SCHEDULE STATUS (activities active or about to start; id | name | planned start-finish | forecast | % complete):
{acts_summary}

OPEN ITEMS / INBOXES (role → pending items):
{json.dumps(inboxes, ensure_ascii=False)[:6000]}

YESTERDAY'S DIARY:
{yesterday_diary[:3000]}

OPEN ACTIONS, RFIs, NCRs:
{open_items[:3000]}

RECENT MEETING MINUTES:
{recent_moms(1, 3000)}

RULES
- Pick 2 to {today.get('max_roles', 7)} roles to act today (fewer on quiet days; 0-1 on non-working days). Prefer roles with inbox items or scripted deliverables.
- Every must_produce item must be realistic for the phase and for that role. Letters need a to_role (a role id). Documents need folder (e.g. "1/04"), area, disc, type codes.
- Replies: if someone received a letter/request, the recipient should answer within a few days.
- Interpret surprises (kind=surprise) as something that becomes visible today through a report, inspection, letter or notice; list affected activities with slip_days (0 if unknown yet).
- Non-working day: usually empty day_plan; narrative only.
- Site manpower: 0 before mobilisation (~Day 90), ramping to ~900 at peak construction; productivity 1.0 normal, lower on bad weather.
Return ONLY JSON matching the schema."""


def agent_prompt(role_id: str, today: dict, plan_for_role: dict, inbox_items: list[dict], acts_for_role: str, extra_context: str) -> str:
    r = world.roles()[role_id]
    return f"""{personas.system_prompt(role_id)}

=== PROJECT BRIEF ===
{charter_brief()}

=== ORGANISATION (use role ids in to_role / attendee_roles / owner_role fields; use people's names inside document text) ===
{org_chart()}

=== DOCUMENT NUMBERING & FOLDERS ===
{numbering_help()}
Letters are numbered automatically; you only choose dept and recipient. Documents are numbered automatically from folder/area/disc/type.

=== TODAY ===
Day {today['day']} — {today['date']} ({today['weekday']}). Phases: {today['phases']}. Weather: {today['weather']['condition']}, {today['weather']['tmin']}..{today['weather']['tmax']} °C.

=== WHAT THE DAY LOOKS LIKE FOR YOU (from the project management) ===
Tasks: {json.dumps(plan_for_role.get('tasks', []), ensure_ascii=False)}
You MUST produce today: {json.dumps(plan_for_role.get('must_produce', []), ensure_ascii=False)}

=== YOUR INBOX (letters, requests, actions addressed to you) ===
{json.dumps(inbox_items, ensure_ascii=False, indent=0) if inbox_items else 'empty'}

=== SCHEDULE EXTRACT RELEVANT TO YOU ===
{acts_for_role}

=== RECENT DOCUMENTS ON THE PROJECT ===
{recent_docs()}

=== RECENT CORRESPONDENCE ===
{recent_letters()}

=== RECENT MEETING MINUTES (decisions and actions you are expected to know) ===
{recent_moms()}

{extra_context}

=== OUTPUT RULES ===
- Produce full, professional content. A document has 4-10 sections with real paragraphs, bullet lists and tables where appropriate
  (quantities, dates, responsibilities). Minimum ~400 words for plans/reports; letters 2-6 paragraphs.
- Use the exact codes requested in must_produce (folder, area, disc, type, dept, to_role, mom_kind, attendees).
- For a MOM, write 5-12 discussion items and 3-10 actions with owner_role (role id) and due_date (YYYY-MM-DD).
- register_updates: only for rfi/ncr/risk/change/procurement/actions/hse/payments; rows use the column names of that register
  (risk: id,category,description,probability,impact,score,owner,mitigation,status; actions: action,owner,due_date,status;
   procurement: package,vendor,stage,value_usd,promised_delivery,status,notes; rfi: area,discipline,subject,status;
   ncr: area,description,severity,status; change: title,type,cost_impact_usd,time_impact_days,status,notes;
   payments: kind,party,period,gross_usd,retention_usd,advance_recovery_usd,net_usd,status; hse: manpower,manhours,near_miss,first_aid,lti,toolbox_talks,note).
- schedule_updates only if you really know progress or delay of an activity (planning/construction roles mainly).
- requests: ask other roles for inputs you need (they will receive it in their inbox).
- summary: 2-3 sentences, first person, plain, for the site diary.
Return ONLY JSON matching the schema."""
