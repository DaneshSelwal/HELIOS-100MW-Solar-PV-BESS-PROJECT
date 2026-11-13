# HELIOS LOG

Single running record of everything done on this project: build steps, decisions, trial runs and every
simulated day advanced. Newest entries at the bottom. Dates in `YYYY-MM-DD` are real dates; `Day NNN`
is simulated project time (Day 0 = contract signature, 1 Dec 2026).

---

## 2026-11-13 — Brainstorm, planning and readiness checks

**Idea.** Danesh (planning dept, EPC renewable project, Uzbekistan) wants to learn end-to-end EPC
workflow and AI agents by simulating a whole EPC company with named AI agents running a fictional
100 MW Solar PV + BESS project day by day, producing every real document.

**Decisions made.**
- Fictional project: EPC "Helios EPC LLC", client "Qizilqum Solar Energy JSC" (IPP), Navoi region,
  100 MWac PV + 50 MW/100 MWh BESS, lump-sum ≈ USD 95 M, FIDIC Silver based, Day 0 = 1 Dec 2026,
  PAC target 18 months later.
- Observer only; days advance on demand from Claude Code; English only; real docx/xlsx/pdf files.
- Engine: `agy` CLI headless with JSON schema. Opus = Simulation Director, Sonnet = senior roles,
  Gemini 3.8 Flash = simple roles. Weekly agy budget managed by Claude; clean pause on quota.
  Second line = Claude Code subagents (Pro plan, used sparingly). No API keys.
- Teams: ~12 EPC agents, 4 client agents, one point-of-contact agent per external party.
- v1 features: hidden ground truth, earned value + delay analysis, money flow, engineering data
  (layout/BOQ), document-control realism, Uzbek regulatory flavour, closeout & lessons learned,
  morning brief + monthly newsletter, live dashboard on GitHub Pages.
  Excluded from v1: office politics, interview mode, what-if branches.
- Mandatory trial: smoke tests + 7-day dress rehearsal on branch `trial`, then reset and start real Day 0.

**Readiness checks (all passed or resolved).**
- `agy -p` headless + `--json-schema`: works (Flash now; Claude/Gemini-4 quota resets in ~4 days).
- Gemini CLI: free tier discontinued → dropped. Gemini desktop app: not drivable from Claude Code → not used.
- GitHub push auth: OK (`git push --dry-run`). Python libs present; `reportlab` installed today.
- Folder tree / numbering reference received as `SK_inspire.md` (74k lines). Contains real names →
  **gitignored, never pushed**. Only an anonymised scheme derived from it goes in the repo.

**Build log.**
- M0: created folder skeleton, `.gitignore`, `README.md`, this log, `requirements.txt`.
