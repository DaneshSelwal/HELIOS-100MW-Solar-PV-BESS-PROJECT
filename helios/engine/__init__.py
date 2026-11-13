"""Engine front door. Tries agy first; if quota is exhausted, falls back to the MANUAL engine:
the prompt is written to state/manual/<key>.prompt.md (+ .schema.json) and ManualNeeded is raised.
Whoever answers (a Claude Code subagent, or a human pasting into any chat model) saves the JSON reply as
state/manual/<key>.json; the next run picks it up without calling agy."""
from __future__ import annotations
import json, pathlib
from ..world import ROOT
from . import agy

MANUAL = ROOT / "state" / "manual"


class ManualNeeded(RuntimeError):
    def __init__(self, keys: list[str]):
        super().__init__("manual answers needed: " + ", ".join(keys)); self.keys = keys


def answer_path(key: str) -> pathlib.Path:
    return MANUAL / f"{key}.json"


def run(key: str, prompt: str, model: str, schema: dict, *, timeout_s: int = 300, manual_ok: bool = True) -> tuple[dict, str]:
    MANUAL.mkdir(parents=True, exist_ok=True)
    ap = answer_path(key)
    if ap.exists():
        data = json.loads(ap.read_text(encoding="utf-8"))
        missing = [k for k in schema.get("required", []) if k not in data]
        if missing:
            raise RuntimeError(f"{ap.name} is missing required keys {missing}")
        return data, "manual"
    try:
        return agy.run(prompt, model, schema, timeout_s=timeout_s)
    except agy.QuotaExhausted:
        if not manual_ok:
            raise
        (MANUAL / f"{key}.prompt.md").write_text(prompt, encoding="utf-8")
        (MANUAL / f"{key}.schema.json").write_text(json.dumps(schema, indent=1), encoding="utf-8")
        (MANUAL / f"{key}.model").write_text(model, encoding="utf-8")
        raise ManualNeeded([key])


def pending() -> list[dict]:
    MANUAL.mkdir(parents=True, exist_ok=True)
    out = []
    for p in sorted(MANUAL.glob("*.prompt.md")):
        key = p.name[:-len(".prompt.md")]
        if not answer_path(key).exists():
            out.append({"key": key, "prompt": str(p.relative_to(ROOT)), "schema": str((MANUAL / f"{key}.schema.json").relative_to(ROOT)),
                        "model": (MANUAL / f"{key}.model").read_text().strip() if (MANUAL / f"{key}.model").exists() else ""})
    return out


def clear_day(day: int) -> None:
    for p in MANUAL.glob(f"D{day:03d}_*"):
        p.unlink()
