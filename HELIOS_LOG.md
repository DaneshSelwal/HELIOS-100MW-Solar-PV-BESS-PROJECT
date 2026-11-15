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
- M1: world bible written — `world/charter.yaml` (facts, milestones, parties, calendar), `world/numbering.yaml`
  (anonymised numbering grammar + 18-department folder tree → 107 folders created under `project/`),
  `world/org_epc.yaml` (12 roles), `world/org_client.yaml` (4), `world/externals.yaml` (10 POCs + Simulation
  Director), `world/baseline_schedule.yaml` (6 phases, 18 WBS, 88 L3 activities, links validated),
  `world/truth.yaml` (hidden ground truth: geotech, supplier reliability, weather, 10 scripted surprises —
  never shown to agents), `world/event_deck.yaml` (recurring meetings/reports + random events).
  `helios/personas.py` generates 26 persona files in `.claude/agents/` from the org YAML.

## 2026-11-14/15 — 7-day dress rehearsal completed (branch `trial`, local only)

**Result.** Days 0-7 ran end to end through the manual engine (Claude Code subagents: Director = opus, roles = sonnet/haiku),
one commit per day. Output on the trial branch: 21 numbered documents (contract summary, document control procedure,
project charter, org chart + RACI, NTP checklist, stakeholder register, L1/L2 milestone schedule, engineering execution
plan, procurement plan, subcontracting strategy, risk register with 18 risks, HSE plan, quality plan, project execution
plan, progress measurement procedure, kick-off agenda), 14 letters, 2 MOMs (kick-off, weekly progress meeting No. 1),
38 emails, 41 open actions, 5 procurement packages, daily diary + morning brief + dashboard, L3 schedule with Gantt.
Document quality judged good: correct numbers, names, clauses and dates; agents flag their own assumptions.

**Cost observed.** ~45-60k tokens per role per day, 4-5 roles + Director per day ≈ 250k tokens of Claude Code (Pro)
quota per simulated day. The Pro 5-hour limit was hit once (Day 4, two agents resumed after reset without loss).
agy stayed exhausted the whole trial.

**Gaps found → fixed on `main` (not on the trial branch).**
1. Inbox summaries truncated letters at 600 chars → full text + file path now carried.
2. Agents did not see meeting decisions → MOM text mirror, last minutes included in every prompt.
3. Agents could not re-read their own earlier documents (invented inconsistent dates) → text mirror of every
   document; each role gets its last 2 documents in full; reviewers get the full text of documents transmitted to them.
4. Document Controller inbox piled up (23 notices) → transmittals are now generated automatically by Python
   (no model call) whenever an EPC deliverable is issued for review; client PM and OWE receive them.
5. Director picked the same senior roles repeatedly → explicit priority rules (scripted deliverables, then stale
   inboxes, then active activities, rotate every ~10 days); reviewers must answer with a comment sheet + review code.
6. Scripted deliverables fell on a Sunday → moved to Day 6.
7. Earlier: dashboard folder lost on rollback; quota cooldown; double salutation in letters.

**State.** `main` is clean (no simulation state) and holds all fixes. `trial` branch keeps the 7 rehearsal days for review.
Real Day 0 starts on `main` on the user's command ("move 1 day"). agy quota expected back ~16-17 Nov; it will be tried
first automatically, subagents otherwise.
