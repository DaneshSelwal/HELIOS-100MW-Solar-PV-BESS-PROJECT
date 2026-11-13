---
name: helios-next
description: Advance the HELIOS EPC simulation by N simulated days (default 1). Use when the user says "move next day", "advance 3 days", "next day", "run the simulation", or invokes /helios-next.
---

# /helios-next [n]

Advance the HELIOS simulation by `n` days (default 1). Each day: event engine → Simulation Director (agy) → role agents (agy) →
real docx/xlsx files, registers, diary, morning brief, dashboard → one git commit per day → push.

Steps:
1. Run `python3 -m helios next <n>` from the repo root (`/Users/danesh/Desktop/HELIOS_PROJECT`). It prints per-day roles, outputs, models and commit.
   Expect 1-6 minutes per simulated day. Use a generous Bash timeout (600000) and run in background for n > 2.
2. If it prints `PAUSED: quota exhausted`, tell the user which model is exhausted and when it resets (the message contains it); do not retry.
3. Reply to the user with a very short digest: day/date, who acted, what files were produced (paths), and point to
   `brief/<date>_D<day>.md` and `dashboard/STATUS.md`. Do not paste whole documents.
4. Do not edit project documents by hand; every change goes through the simulation.
