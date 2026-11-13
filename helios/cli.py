"""python -m helios next [n] | status | usage"""
from __future__ import annotations
import sys, json
from . import clock, orchestrator, registers, progress
from .engine import agy


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "status"
    if cmd == "next":
        n = int(argv[1]) if len(argv) > 1 else 1
        flags = set(argv[2:]); push = "--no-push" not in flags; dry = "--dry" in flags
        start = clock.load()["day"] + 1
        for day in range(start, start + n):
            print(f"=== {clock.label(day)} ===", flush=True)
            try:
                res = orchestrator.run_day(day, push=push, dry=dry)
            except agy.QuotaExhausted as e:
                print(f"PAUSED: quota exhausted on {e.model} — {e.message}"); return 2
            print(f"roles: {res['roles']}\nproduced: {res['produced']}\nmodels: {res['models']}\ncommit: {res['commit']} ({res['secs']} s)", flush=True)
        return 0
    if cmd == "status":
        c = clock.load(); print(json.dumps(c, indent=2))
        if c["day"] >= 0:
            acts = progress.load(); d = clock.date_of(c["day"])
            print(f"planned {progress.planned_pct(acts, d):.2f}% | earned {progress.earned_pct(acts):.2f}% | forecast PAC {progress.forecast_completion(acts)}")
            print(f"documents {len(registers.read('documents'))} | letters {len(registers.read('correspondence'))} | open actions {sum(a['status']=='Open' for a in registers.read('actions'))}")
        return 0
    if cmd == "usage":
        print(json.dumps(agy.usage_summary(argv[1] if len(argv) > 1 else None), indent=2)); return 0
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
