"""One commit per simulated day; push to origin. Never commits the gitignored reference material."""
from __future__ import annotations
import subprocess
from .world import ROOT


def _git(*args: str, check: bool = True) -> str:
    p = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)
    if check and p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {p.stderr.strip()[:300]}")
    return p.stdout.strip()


def current_branch() -> str:
    return _git("rev-parse", "--abbrev-ref", "HEAD")


def commit_day(day: int, date_iso: str, summary: str, push: bool = True) -> str | None:
    _git("add", "-A")
    if not _git("status", "--porcelain"):
        return None
    msg = f"Day {day:03d} ({date_iso}): {summary}\n\nCo-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
    _git("commit", "-q", "-m", msg)
    sha = _git("rev-parse", "--short", "HEAD")
    if push:
        try:
            _git("push", "-q", "-u", "origin", current_branch())
        except RuntimeError as e:
            print("push failed (will retry next day):", e)
    return sha


def rollback_to_head() -> None:
    """Discard all uncommitted changes (used when a day fails mid-way)."""
    _git("reset", "-q", "--hard", "HEAD"); _git("clean", "-fdq", "--", "project", "correspondence", "diary", "brief", "dashboard", "state")
