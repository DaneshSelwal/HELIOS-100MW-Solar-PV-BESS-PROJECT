# HELIOS — Agent-run EPC Simulation

**HELIOS** simulates a complete EPC (Engineering, Procurement, Construction) company delivering a
fictional **100 MWac Solar PV + 50 MW / 100 MWh BESS** power plant in the Navoi region of Uzbekistan,
from contract signature to Provisional Acceptance.

Every role in the EPC company, the client organisation and each external party (subcontractors,
suppliers, grid operator, authorities) is an **AI agent with a name and a persona**. The simulation
advances **one day at a time, on demand**. Each day the agents hold meetings, write letters, raise
RFIs, update schedules and produce the real documents a project produces, as genuine Word/Excel/PDF
files filed in a document-control folder tree with proper numbering. Every simulated day is one git
commit, so the whole project history can be replayed.

The only human is a read-only observer.

> All companies, people, sites, figures and documents in this repository are **fictional**.
> Nothing here is from, or about, any real project or organisation.

## Layout

| Path | What lives there |
|---|---|
| `HELIOS_LOG.md` | Running log of everything done to build and run the simulation |
| `world/` | The "bible": project charter, organisations, personas, numbering scheme, baseline schedule, event deck |
| `.claude/agents/` | Agent personas (Claude Code custom agents) |
| `helios/` | Python orchestrator: clock, events, engine adapters, renderers, registers, git |
| `project/` | Simulated Document Control System (real folder tree with numbered docx/xlsx/pdf) |
| `correspondence/` | Letters, emails, minutes of meeting by month |
| `diary/` | One site diary entry per simulated day |
| `brief/` | One-page morning brief per simulated day for the observer |
| `dashboard/` | Auto-generated project status |
| `state/` | Machine state: clock, registers, agent inboxes |

## Running

The simulation is driven from Claude Code: *"move next day"* or *"advance 3 days"* runs `/helios-next [n]`.
Equivalent terminal command: `python -m helios next 3`. Status: `python -m helios status`.

## Status

See `HELIOS_LOG.md` and `dashboard/STATUS.md`.
