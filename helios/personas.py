"""Generate .claude/agents/<id>.md persona files from the world org files.

The same persona text is used as the system prompt for agy runs (see engine/agy.py),
so the agents behave identically whichever engine runs them.
"""
from __future__ import annotations
import pathlib
from . import world

AGENTS_DIR = world.ROOT / ".claude" / "agents"

CLAUDE_MODEL = {"A": "haiku", "B": "sonnet", "C": "opus"}

COMMON_RULES = """
## How you work (rules for every HELIOS agent)
- You are a real professional on a real project. Stay in character; never mention that you are an AI or a simulation.
- Everything you write becomes a real project document or letter. Use the document numbering scheme and the
  folder tree given in the task context. Dates must be the simulated project date given in the context.
- Be concrete: real quantities, dates, drawing numbers, clause references, names of colleagues (from the org chart).
- Do not invent facts that contradict the project charter, the schedule or earlier documents in your context.
- When you need information from another role, request it with a letter/email/meeting request rather than inventing it.
- Keep professional EPC tone and formats: letters (ref, date, subject, body, sign-off), MOMs (attendees, items, actions),
  reports (summary, progress, issues, look-ahead), registers (rows).
- Return ONLY what the JSON schema in the task asks for.
"""


def persona_markdown(r: dict, charter: dict) -> str:
    kind = r.get("kind", "epc")
    org_name = {
        "HEP": charter["parties"]["epc"]["name"],
        "QSE": charter["parties"]["client"]["name"],
        "OWE": charter["parties"]["owners_engineer"]["name"],
    }.get(r["org"], r.get("company", r["org"]))
    lines = [f"# {r['name']} — {r['title']}", "",
             f"**Organisation:** {org_name} ({r['org']})  ",
             f"**Project:** {charter['project']['name']} ({charter['project']['code']})  "]
    if r.get("package"):
        lines.append(f"**Scope / package:** {r['package']}  ")
    if r.get("reports_to"):
        boss = world.roles().get(r["reports_to"], {})
        lines.append(f"**Reports to:** {boss.get('name', r['reports_to'])} ({boss.get('title', '')})  ")
    lines += ["", "## Background", r["background"], "", "## Personality and style", r["personality"], ""]
    if r.get("responsibilities"):
        lines += ["## Responsibilities"] + [f"- {x}" for x in r["responsibilities"]] + [""]
    if r.get("owns_documents"):
        lines += ["## Documents you own"] + [f"- {x}" for x in r["owns_documents"]] + [""]
    if kind == "external":
        lines += ["## Relationship", f"You are the single point of contact of {r['company']} towards Helios EPC LLC. "
                  "You act in your company's commercial interest while remaining professional and contractually correct.", ""]
    lines.append(COMMON_RULES.strip())
    return "\n".join(lines) + "\n"


def write_all() -> list[pathlib.Path]:
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    ch = world.charter()
    written = []
    for rid, r in world.roles().items():
        body = persona_markdown(r, ch)
        tier = r.get("tier", "A")
        desc = f"HELIOS agent: {r['name']}, {r['title']} at {r.get('company', r['org'])}. Use when this role must act in the HELIOS simulation."
        fm = ("---\n"
              f"name: {rid}\n"
              f"description: {desc}\n"
              f"model: {CLAUDE_MODEL.get(tier, 'haiku')}\n"
              "tools: Read, Glob, Grep\n"
              "---\n\n")
        p = AGENTS_DIR / f"{rid}.md"
        p.write_text(fm + body, encoding="utf-8")
        written.append(p)
    return written


def system_prompt(role_id: str) -> str:
    """Persona text without the Claude Code frontmatter — used as agy system prompt."""
    txt = (AGENTS_DIR / f"{role_id}.md").read_text(encoding="utf-8")
    if txt.startswith("---"):
        txt = txt.split("---", 2)[2]
    return txt.strip()


if __name__ == "__main__":
    for p in write_all():
        print("wrote", p.relative_to(world.ROOT))
