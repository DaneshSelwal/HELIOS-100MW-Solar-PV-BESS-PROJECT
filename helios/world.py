"""Load the world bible (world/*.yaml) into plain dicts."""
from __future__ import annotations
import pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORLD = ROOT / "world"


def load(name: str) -> dict:
    with open(WORLD / f"{name}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def charter() -> dict:
    return load("charter")


def numbering() -> dict:
    return load("numbering")


def schedule() -> dict:
    return load("baseline_schedule")


def event_deck() -> dict:
    return load("event_deck")


def truth() -> dict:
    """Hidden ground truth. Only the event engine may call this; never pass to agents."""
    return load("truth")


def roles() -> dict[str, dict]:
    """All agent roles keyed by id, with 'org' set to HEP / QSE / OWE / external code."""
    out: dict[str, dict] = {}
    for r in load("org_epc")["roles"]:
        r = dict(r); r["org"] = "HEP"; r["kind"] = "epc"; out[r["id"]] = r
    for r in load("org_client")["roles"]:
        r = dict(r); r["org"] = r.get("organisation", "QSE"); r["kind"] = "client"; out[r["id"]] = r
    ext = load("externals")
    for r in ext["roles"]:
        r = dict(r); r["org"] = r["code"]; r.setdefault("kind", "external"); out[r["id"]] = r
    return out


def director() -> dict:
    return load("externals")["director"]
