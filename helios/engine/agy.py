"""agy CLI adapter: run a persona with a task and get schema-validated JSON back.

Budget rules (see world/externals.yaml + HELIOS_LOG.md):
- Every call is logged to state/usage.jsonl (model, tokens, seconds, status).
- On quota exhaustion (HTTP 429 / RESOURCE_EXHAUSTED) we try the fallback chain once, then raise
  QuotaExhausted so the day can be rolled back cleanly.
"""
from __future__ import annotations
import json, os, subprocess, tempfile, time, pathlib, datetime as dt
from ..world import ROOT

STATE = ROOT / "state"
USAGE_LOG = STATE / "usage.jsonl"

FALLBACK_CHAIN = {
    "claude-opus-5-5-medium": ["claude-sonnet-5-5-medium", "gemini-4-hydrogen-medium", "gemini-3.8-flash-high"],
    "claude-sonnet-5-5-medium": ["gemini-4-hydrogen-medium", "gemini-3.8-flash-high"],
    "gemini-4-hydrogen-medium": ["gemini-3.8-flash-high"],
    "gemini-3.8-flash-medium": ["gemini-3.8-flash-low"],
    "gemini-3.8-flash-high": ["gemini-3.8-flash-medium"],
}


class EngineError(RuntimeError):
    pass


class QuotaExhausted(EngineError):
    def __init__(self, model: str, message: str):
        super().__init__(f"{model}: {message}")
        self.model, self.message = model, message


def _log(entry: dict) -> None:
    STATE.mkdir(exist_ok=True)
    entry["ts"] = dt.datetime.now().isoformat(timespec="seconds")
    with open(USAGE_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _run_once(prompt: str, model: str, schema: dict | None, timeout_s: int, cwd: pathlib.Path) -> dict:
    args = ["agy", "-p", prompt, "--model", model, "--output-format", "json",
            "--print-timeout", f"{timeout_s}s", "--mode", "plan"]
    tmp = None
    if schema is not None:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        json.dump(schema, tmp); tmp.close()
        args += ["--json-schema", tmp.name]
    t0 = time.time()
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout_s + 30, cwd=str(cwd))
    finally:
        if tmp:
            os.unlink(tmp.name)
    secs = round(time.time() - t0, 1)
    # agy prints one JSON object on the last line of stdout
    line = next((l for l in reversed(proc.stdout.strip().splitlines()) if l.startswith("{")), None)
    if line is None:
        _log({"model": model, "status": "NO_JSON", "secs": secs})
        raise EngineError(f"agy returned no JSON (rc={proc.returncode}): {proc.stderr[-400:]}")
    out = json.loads(line)
    usage = out.get("usage", {})
    _log({"model": model, "status": out.get("status"), "secs": secs,
          "in": usage.get("input_tokens", 0), "out": usage.get("output_tokens", 0),
          "think": usage.get("thinking_tokens", 0), "error": out.get("error")})
    if out.get("status") != "SUCCESS":
        err = str(out.get("error", ""))
        if "quota" in err.lower() or "RESOURCE_EXHAUSTED" in proc.stdout or "429" in err:
            raise QuotaExhausted(model, err)
        raise EngineError(f"agy error on {model}: {err[:300]}")
    return out


def run(prompt: str, model: str, schema: dict | None = None, *, timeout_s: int = 300,
        allow_fallback: bool = True, cwd: pathlib.Path | None = None) -> tuple[dict, str]:
    """Run prompt; return (parsed_json_response, model_actually_used).

    If `schema` is given the response text is parsed as JSON matching that schema.
    """
    cwd = cwd or ROOT
    chain = [model] + (FALLBACK_CHAIN.get(model, []) if allow_fallback else [])
    last: Exception | None = None
    for m in chain:
        try:
            out = _run_once(prompt, m, schema, timeout_s, cwd)
            text = out.get("response", "")
            if schema is not None:
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    # strip code fences if the model wrapped it
                    cleaned = text.strip().strip("`")
                    cleaned = cleaned[cleaned.find("{"): cleaned.rfind("}") + 1]
                    data = json.loads(cleaned)
                return data, m
            return {"text": text}, m
        except QuotaExhausted as e:
            last = e
            continue
    assert last is not None
    raise last


def usage_summary(since_iso: str | None = None) -> dict:
    """Totals per model from state/usage.jsonl (optionally since an ISO timestamp)."""
    tot: dict[str, dict] = {}
    if not USAGE_LOG.exists():
        return tot
    for line in USAGE_LOG.read_text(encoding="utf-8").splitlines():
        e = json.loads(line)
        if since_iso and e["ts"] < since_iso:
            continue
        t = tot.setdefault(e["model"], {"calls": 0, "ok": 0, "in": 0, "out": 0, "secs": 0.0})
        t["calls"] += 1; t["ok"] += e.get("status") == "SUCCESS"
        t["in"] += e.get("in", 0); t["out"] += e.get("out", 0); t["secs"] += e.get("secs", 0)
    return tot
