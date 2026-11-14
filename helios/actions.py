"""Apply an agent's structured output: render files, file them, update registers, route inboxes."""
from __future__ import annotations
import datetime as dt, json, pathlib
from . import world, numbering, registers, progress, clock
from .render import docx as rdocx

ROOT = world.ROOT


def _org_name(role: dict) -> str:
    c = world.charter()["parties"]
    return {"HEP": c["epc"]["name"], "QSE": c["client"]["name"], "OWE": c["owners_engineer"]["name"]}.get(role["org"], role.get("company", role["org"]))


def _org_code(role: dict) -> str:
    return role.get("code") or role["org"]


def apply(role_id: str, out: dict, day: int, log: list[str]) -> dict:
    """Returns counts of what was produced."""
    roles = world.roles(); me = roles[role_id]; d = clock.date_of(day); ym = d.strftime("%Y-%m")
    n = {"documents": 0, "letters": 0, "emails": 0, "moms": 0, "registers": 0, "schedule": 0, "requests": 0}

    for doc in out.get("documents", []) or []:
        try:
            top, sub = (doc.get("folder") or "15/01").split("/")
            folder = numbering.folder(top, sub)
        except Exception:
            folder = numbering.folder("15", "01")
        area = doc.get("area") or "G000"; disc = (doc.get("disc") or "_")[:1]; dtype = doc.get("type") or "&RPT"
        if not dtype.startswith("&"): dtype = "&" + dtype[:3].upper()
        rev = doc.get("rev") or "A"; status = doc.get("status") or "Issued for Review"
        if dtype == "&PRC" and me["org"] == "HEP" and top == "1":
            num = numbering.mgmt_plan("PM", "HEP", "QSE", "00" if rev.isdigit() else "0A")
        else:
            num = numbering.technical(area, disc, dtype, rev)
        fname = f"{num}_{numbering.safe_title(doc['title'])}.docx"
        path = folder / fname
        rdocx.document(path, title=doc["title"], docnum=num, org=_org_name(me), date=d, sections=doc.get("sections") or [],
                       rev=rev, status=status, prepared_by=f"{me['name']} ({me['title']})",
                       approved_by=_approver(me, roles))
        registers.append("documents", {"doc_no": num, "title": doc["title"], "type": dtype, "area": area, "discipline": disc, "rev": rev,
                                       "status": status, "originator": _org_code(me), "owner_role": role_id, "issued_day": day,
                                       "issued_date": d.isoformat(), "path": str(path.relative_to(ROOT)), "review_code": "", "notes": ""})
        # notify document controller + OWE for review when it is an EPC deliverable
        if me["org"] == "HEP" and role_id != "epc-document-controller":
            registers.send("epc-document-controller", {"day": day, "from": role_id, "kind": "document_issued", "ref": num, "subject": doc["title"], "summary": f"Issued Rev {rev} — log and transmit to client if applicable"})
        n["documents"] += 1; log.append(f"DOC {num} {doc['title']} → {path.relative_to(ROOT)}")

    for let in out.get("letters", []) or []:
        to = roles.get(let.get("to_role"))
        if not to:
            log.append(f"SKIP letter: unknown to_role {let.get('to_role')}"); continue
        dept = (let.get("dept") or "PM")[:2].upper()
        ref = numbering.letter(dept, _org_code(me), _org_code(to))
        path = ROOT / "correspondence" / ym / f"{ref}_{numbering.safe_title(let['subject'], 50)}.docx"
        rdocx.letter(path, ref=ref, date=d, from_org=_org_name(me), from_person=me["name"], from_title=me["title"],
                     to_org=_org_name(to), to_person=to["name"], to_title=to["title"], subject=let["subject"],
                     body_paragraphs=let.get("body_paragraphs") or [], cc=[roles[c]["name"] + f" ({roles[c]['title']})" for c in (let.get("cc_roles") or []) if c in roles],
                     attachments=let.get("attachments"), reply_to_ref=let.get("reply_to_ref") or None)
        registers.append("correspondence", {"ref": ref, "day": day, "date": d.isoformat(), "from_org": _org_code(me), "from_role": role_id,
                                            "to_org": _org_code(to), "to_role": let["to_role"], "subject": let["subject"], "kind": "letter",
                                            "reply_to": let.get("reply_to_ref", ""), "path": str(path.relative_to(ROOT)), "status": "sent"})
        if let.get("reply_to_ref"):
            registers.update_where("correspondence", "ref", let["reply_to_ref"], status="answered")
        registers.send(let["to_role"], {"day": day, "from": role_id, "kind": "letter", "ref": ref, "subject": let["subject"],
                                        "summary": "\n".join(let.get("body_paragraphs") or [])[:3000], "path": str(path.relative_to(ROOT)), "due_day": let.get("requires_response_by_day") or day + 5})
        for c in let.get("cc_roles") or []:
            if c in roles:
                registers.send(c, {"day": day, "from": role_id, "kind": "cc", "ref": ref, "subject": let["subject"], "summary": "copied for information"})
        n["letters"] += 1; log.append(f"LETTER {ref} → {let['to_role']}: {let['subject']}")

    for em in out.get("emails", []) or []:
        path = ROOT / "correspondence" / ym / "emails" / f"D{day:03d}_{role_id}_{numbering.safe_title(em['subject'], 40)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        tos = ", ".join(roles[t]["name"] for t in em.get("to_roles", []) if t in roles)
        path.write_text(f"**From:** {me['name']} ({me['title']}, {_org_name(me)})  \n**To:** {tos}  \n**Date:** {d.isoformat()}  \n**Subject:** {em['subject']}\n\n{em['body']}\n", encoding="utf-8")
        for t in em.get("to_roles", []):
            if t in roles:
                registers.send(t, {"day": day, "from": role_id, "kind": "email", "ref": path.stem, "subject": em["subject"], "summary": em["body"][:2000]})
        n["emails"] += 1

    for m in out.get("meeting_minutes", []) or []:
        kind = (m.get("mom_kind") or "GEN")[:4].upper(); ref = numbering.mom(kind)
        path = numbering.folder("1", "09") / f"{ref}_{numbering.safe_title(m['title'], 50)}.docx"
        att = [f"{roles[a]['name']} ({roles[a]['title']}, {_org_code(roles[a])})" for a in m.get("attendee_roles", []) if a in roles]
        actions = []
        for i, a in enumerate(m.get("actions", []) or [], 1):
            owner = roles.get(a.get("owner_role"), {})
            actions.append({"no": i, "action": a["action"], "owner": owner.get("name", a.get("owner_role", "")), "due": a.get("due_date", ""), "status": "Open"})
            aid = f"ACT-{day:03d}-{kind}-{i:02d}"
            registers.append("actions", {"id": aid, "day": day, "source": ref, "action": a["action"], "owner": a.get("owner_role", ""), "due_date": a.get("due_date", ""), "status": "Open", "closed_day": ""})
            if a.get("owner_role") in roles:
                registers.send(a["owner_role"], {"day": day, "from": role_id, "kind": "action", "ref": aid, "subject": a["action"], "summary": f"Action from {ref}, due {a.get('due_date','')}", "due_day": day + 7})
        rdocx.mom(path, ref=ref, title=m["title"], date=d, venue=m.get("venue") or "Site office / Tashtkent office", chaired_by=me["name"],
                  attendees=att, items=m.get("items") or [], actions=actions, org=_org_name(me))
        mm = ROOT / "state" / "moms"; mm.mkdir(parents=True, exist_ok=True)
        (mm / f"D{day:03d}_{ref}.md").write_text(f"# {ref} {m['title']} ({d.isoformat()})\nAttendees: {'; '.join(att)}\n\n" +
            "\n".join(f"- {i.get('topic','')}: {i.get('discussion','')}" for i in (m.get('items') or [])) + "\n\nActions:\n" +
            "\n".join(f"- {a['action']} (owner {a['owner']}, due {a['due']})" for a in actions) + "\n", encoding="utf-8")
        registers.append("documents", {"doc_no": ref, "title": m["title"], "type": "&MOM", "area": "G000", "discipline": "P", "rev": "00", "status": "Issued",
                                       "originator": _org_code(me), "owner_role": role_id, "issued_day": day, "issued_date": d.isoformat(), "path": str(path.relative_to(ROOT)), "review_code": "", "notes": ""})
        for a in m.get("attendee_roles", []):
            if a in roles and a != role_id:
                registers.send(a, {"day": day, "from": role_id, "kind": "mom", "ref": ref, "subject": m["title"], "summary": "Minutes issued; review your actions"})
        n["moms"] += 1; log.append(f"MOM {ref} {m['title']}")

    for ru in out.get("register_updates", []) or []:
        reg = ru.get("register"); row = dict(ru.get("row") or {})
        if reg not in registers.SCHEMAS: continue
        if ru.get("op") == "update" and ru.get("key"):
            registers.update_where(reg, ru["key"], str(ru.get("value", "")), **row)
        else:
            row.setdefault("day", day); row.setdefault("date", d.isoformat())
            keyfield = {"rfi": "ref", "ncr": "ref", "change": "ref", "payments": "ref", "risk": "id", "actions": "id"}.get(reg)
            if keyfield and not row.get(keyfield):
                row[keyfield] = f"{reg.upper()}-{day:03d}-{len(registers.read(reg)) + 1:03d}"
            if reg in ("rfi", "ncr") and not row.get("raised_by"): row["raised_by"] = role_id
            if reg == "risk" and not row.get("day_raised"): row["day_raised"] = day
            registers.append(reg, row)
        n["registers"] += 1

    if out.get("schedule_updates"):
        acts = progress.load(); byid = {a["id"]: a for a in acts}
        for su in out["schedule_updates"]:
            a = byid.get(su.get("activity_id"))
            if not a: continue
            if su.get("pct_complete") is not None:
                a["pct_complete"] = max(float(a.get("pct_complete") or 0), min(100.0, float(su["pct_complete"])))
                if a["pct_complete"] > 0 and not a.get("actual_start"): a["actual_start"] = d.isoformat()
                if a["pct_complete"] >= 100 and not a.get("actual_finish"): a["actual_finish"] = d.isoformat()
            if su.get("slip_days"):
                progress.slip(acts, a["id"], int(su["slip_days"]))
            n["schedule"] += 1; log.append(f"SCHED {a['id']}: {su.get('note','')[:80]}")
        progress.save(acts)

    for rq in out.get("requests", []) or []:
        if rq.get("to_role") in roles:
            registers.send(rq["to_role"], {"day": day, "from": role_id, "kind": "request", "ref": f"REQ-{day:03d}-{role_id[:8]}", "subject": rq["what"][:120], "summary": rq["what"], "due_day": rq.get("due_day") or day + 3})
            n["requests"] += 1
    return n


def _approver(me: dict, roles: dict) -> str:
    boss = roles.get(me.get("reports_to") or "")
    return f"{boss['name']} ({boss['title']})" if boss else ""
