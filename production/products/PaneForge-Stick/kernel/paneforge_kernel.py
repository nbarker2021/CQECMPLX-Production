"""
PaneForge Kernel — lattice_forge living under the calendar as a kernel.

THE EVENT LAW (constitutional, applies to every single item built):
  Every event in ALL interactions, at least once, MUST be:
    1. COMPUTED   — adapted through lattice_forge (Binary Boundary Adapter)
    2. SAVED      — stored as a lib item (MMDB crystal)
    3. VALIDATED  — invariants checked against the framework
    4. RECEIPTED  — a Merkle receipt minted, tied to exactly 2 other things:
                      link[0] = the crystal id (the saved lib item)
                      link[1] = the previous receipt hash (the chain)
  After that it is reusable forever for nearly free (SpeedLight idempotent
  cache, f(f(x)) = f(x): a repeat of the same event is a pure lookup).

The Binary Boundary Adapter (lattice_forge.binary_boundary_adapter) is THE
adapter: any payload — calendar event, layout change, cell background, widget
move — serializes to bytes and adapts into the framework with HEAD/TAIL Lie
conjugate boundaries, arc type, and carry density. Nothing enters the system
without passing through it once.

Runs from the stick. Serves the PWA + a JSON API on one port. Stdlib-only
HTTP so the stick needs nothing installed beyond Python.
"""
from __future__ import annotations

import hashlib
import json
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlparse

# ─── Locate and mount the kernel libs (lattice_forge MUST live here) ─────────

import os

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent                      # D:\PaneForge (or the stick root)
_APP_DIR = _ROOT / "app"
_DATA_DIR = Path(os.environ.get("PANEFORGE_DATA", _ROOT / "data"))
_DATA_DIR.mkdir(parents=True, exist_ok=True)

def _find_lib_forge() -> Optional[Path]:
    """Resolve lib-forge. The stick-local bundle ALWAYS wins (position-
    independent USB layout); the production tree is the dev fallback."""
    candidates = [_ROOT / "lib-forge"]                  # stick layout first
    for base in (_ROOT, *_ROOT.parents):
        candidates.append(base / "lib-forge")
        candidates.append(base / "CQE_CMPLX" / "CQECMPLX-Production" / "lib-forge")
    candidates.append(Path("D:/CQE_CMPLX/CQECMPLX-Production/lib-forge"))
    for c in candidates:
        if (c / "ChromaForge").is_dir():
            return c
    return None

_LIB_FORGE = _find_lib_forge()
if _LIB_FORGE is None:
    raise SystemExit("PaneForge kernel requires lib-forge (ChromaForge + cqe_engine + lattice_forge).")
if str(_LIB_FORGE) not in sys.path:
    sys.path.insert(0, str(_LIB_FORGE))

def _mount_lattice_forge() -> Optional[Path]:
    """Make `lattice_forge` importable. Stick layout (lib-forge/lattice_forge)
    is checked first, then the full PROOF source tree. The kernel needs only
    the BBA chain (binary_boundary_adapter + centroid_voa, pure stdlib)."""
    if (_LIB_FORGE / "lattice_forge").is_dir():
        return _LIB_FORGE                       # already on sys.path
    for base in (_ROOT, *_ROOT.parents):
        for rel in (("CQE_CMPLX", "CMPLX-R30-main", "PROOF", "src"),
                    ("CMPLX-R30-main", "PROOF", "src")):
            cand = base.joinpath(*rel)
            if (cand / "lattice_forge").is_dir():
                if str(cand) not in sys.path:
                    sys.path.insert(0, str(cand))
                return cand
    return None

if _mount_lattice_forge() is None:
    raise SystemExit("PaneForge kernel requires lattice_forge (BBA chain).")

# The kernel: ChromaForge engines + the Binary Boundary Adapter
from ChromaForge import ChromaForgeEngine, COUPLING            # noqa: E402
from lattice_forge.binary_boundary_adapter import adapt as bba_adapt   # noqa: E402
from lattice_forge.centroid_voa import LIE_CONJUGATES          # noqa: E402
# PixelForge: surfaces (adaptive resolution), ink (stylus/touch/pointer), frames
from PixelForge import PixelForgeEngine                        # noqa: E402
# FridgeForge: fridge/cabinet scan -> inventory -> shopping list -> meal ideas
from FridgeForge import FridgeForgeEngine                      # noqa: E402
# LinkForge: any external database -> one receipted lib item (lookup table)
from LinkForge import LinkForgeEngine                          # noqa: E402


# ─── The Event Law ────────────────────────────────────────────────────────────

class EventLaw:
    """compute -> save -> validate -> receipt(2 links) -> reuse free."""

    def __init__(self, data_dir: Path):
        self.engine = ChromaForgeEngine()
        self.data_dir = data_dir
        self._ledger_path = data_dir / "receipts.jsonl"
        self._lock = threading.Lock()

    @staticmethod
    def _key(kind: str, canon: str) -> str:
        return hashlib.sha256(f"{kind}:{canon}".encode()).hexdigest()[:32]

    def process(self, kind: str, payload: Dict[str, Any],
                agent_id: str = "paneforge") -> Dict[str, Any]:
        canon = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        key = self._key(kind, canon)

        with self._lock:
            # REUSE — idempotent: same event = pure lookup, nearly free
            hit = self.engine.speedlight.get(key)
            if hit["hit"]:
                out = dict(hit["result"])
                out["reused"] = True
                return out

            t0 = time.time()

            # 1. COMPUTE — the Binary Boundary Adapter is THE adapter
            bba = bba_adapt(canon.encode("utf-8"), window=16)
            adapted = {
                "head": list(bba["head"]),
                "tail": list(bba["tail"]),
                "arc_type": bba["arc_type"],
                "matched": bba["matched"],
                "carry_density": round(bba["summary"]["carry_density"], 4),
                "lie_contact_fraction": round(bba["summary"]["lie_contact_fraction"], 4),
                "shadow": "".join(str(b) for b in bba["summary"]["shadow_sequence"]),
            }

            # 2. SAVE — the event becomes a lib item (crystal)
            crystal = self.engine.mmdb.store(
                content=canon,
                snap_labels=[f"kind:{kind}", f"arc:{bba['arc_type']}",
                             f"head:{bba['head']}", f"tail:{bba['tail']}"],
                domain="paneforge.event",
                metadata={"kind": kind, "bba": adapted},
            )

            # 3. VALIDATE — framework invariants
            head_t, tail_t = tuple(bba["head"]), tuple(bba["tail"])
            valid = (
                head_t in LIE_CONJUGATES
                and tail_t in LIE_CONJUGATES
                and bba["summary"]["n_bits"] >= 3
                and crystal["content_hash"]
                   == hashlib.sha256(canon.encode()).hexdigest()[:16]
            )

            # 4. RECEIPT — tied to exactly 2 other things:
            #    link[0] = crystal id (the saved lib item)
            #    link[1] = previous receipt hash (the chain head)
            links = [crystal["crystal_id"], self.engine.receipt.head]
            receipt = self.engine.receipt.mint(
                receipt_type="PROCESS",
                agent_id=agent_id,
                atom_id=crystal["crystal_id"],
                operation=f"event.{kind}",
                input_data=canon[:64],
                output_data=adapted["shadow"],
                delta_phi=-COUPLING,
                snap_labels=[f"link:{links[0]}", f"link:{links[1]}",
                             f"valid:{valid}"],
            )
            self.engine.conservation.track(
                delta_phi=-COUPLING, delta_n=-COUPLING,
                agent_id=agent_id, service="paneforge.kernel",
                atom_id=crystal["crystal_id"], operation=f"event.{kind}",
            )

            result = {
                "ok": True,
                "valid": valid,
                "kind": kind,
                "key": key,
                "crystal_id": crystal["crystal_id"],
                "receipt_hash": receipt["receipt_hash"],
                "links": links,
                "adapted": adapted,
                "elapsed_ms": round((time.time() - t0) * 1000, 2),
                "reused": False,
            }

            # 5. REUSE — cache for nearly-free repeats (priority channel 9)
            self.engine.speedlight.put(key, result, channel=9,
                                       fn_name=f"event.{kind}")

            # Append-only receipt ledger on the stick
            with open(self._ledger_path, "a", encoding="utf-8") as f:
                f.write(json.dumps({"receipt": receipt, "links": links,
                                    "kind": kind, "valid": valid}) + "\n")
            return result

    def status(self) -> Dict[str, Any]:
        return {
            "lib_forge": str(_LIB_FORGE),
            "gluon_wired": True,
            "receipts": self.engine.receipt.length,
            "receipt_head": self.engine.receipt.head,
            "crystals": self.engine.mmdb.count,
            "cache": self.engine.speedlight.stats(),
            "conservation_cumulative": self.engine.conservation.cumulative,
        }


# ─── Application state (the calendar itself) ─────────────────────────────────

_DEFAULT_STATE: Dict[str, Any] = {
    "mode": "LOCAL",                       # LOCAL | HYBRID | CLOUD
    "loadout": {                           # dynamic loadout — user-configurable
        "rail_width_pct": 26,
        "weeks": 2,
        "widgets": {"clock": True, "date": True, "photo": True,
                    "weather": True, "forecast": True, "grid": True},
    },
    "cells": {},                           # per-cell overrides: {"2026-10-12": {"bg": "#16324a", "img": ""}}
    "events": [],                          # [{id, date, time, text, color}]
    "surfaces": {},                        # surface_id -> descriptor (adaptive resolution)
    "ink": [],                             # receipted strokes (stylus/touch), logical coords
    "fridge": {"inventory": {}, "profiles": {}},   # FridgeForge persistence
    "links": {},                           # name -> linked-database record (lib items)
    "sync": {"last": 0, "log": []},        # daily git sync channel state
}


class StateStore:
    """Persistent calendar state on the stick. Every mutation passes the Event Law first."""

    def __init__(self, data_dir: Path, law: EventLaw):
        self.path = data_dir / "state.json"
        self.law = law
        self.pixel = PixelForgeEngine()      # surfaces + ink + frames
        self.fridge = FridgeForgeEngine()    # inventory + meals + shopping
        self.links = LinkForgeEngine()       # external databases as lib items
        self._lock = threading.Lock()
        if self.path.is_file():
            self.state = json.loads(self.path.read_text(encoding="utf-8"))
            for k, v in _DEFAULT_STATE.items():     # forward-fill new buckets
                self.state.setdefault(k, json.loads(json.dumps(v)))
            # re-register persisted surfaces into the live engine
            for sid, d in self.state.get("surfaces", {}).items():
                self.pixel.register_surface(d["width"], d["height"],
                                            d.get("dpr", 1.0),
                                            d.get("kind", "screen"),
                                            surface_id=sid,
                                            input_caps=d.get("input_caps"))
            self.fridge.restore(self.state.get("fridge", {}))
        else:
            self.state = json.loads(json.dumps(_DEFAULT_STATE))
            self._flush()

    def _flush(self) -> None:
        self.path.write_text(json.dumps(self.state, indent=1), encoding="utf-8")

    def apply(self, kind: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Event Law first; only a receipted, valid event may mutate state."""
        law_result = self.law.process(kind, payload)
        if not law_result.get("valid", False) and not law_result.get("reused"):
            return {"ok": False, "error": "event failed validation", "law": law_result}

        with self._lock:
            if kind == "event.add":
                ev = {"id": law_result["key"][:12],
                      "date": payload.get("date", ""),
                      "time": payload.get("time", ""),
                      "text": payload.get("text", ""),
                      "color": payload.get("color", "b")}
                if not any(e["id"] == ev["id"] for e in self.state["events"]):
                    self.state["events"].append(ev)
            elif kind == "event.remove":
                self.state["events"] = [e for e in self.state["events"]
                                        if e["id"] != payload.get("id")]
            elif kind == "cell.bg":
                date = payload.get("date", "")
                if date:
                    cell = self.state["cells"].setdefault(date, {})
                    if "bg" in payload:  cell["bg"] = payload["bg"]
                    if "img" in payload: cell["img"] = payload["img"]
            elif kind == "loadout.set":
                lo = self.state["loadout"]
                for k in ("rail_width_pct", "weeks"):
                    if k in payload: lo[k] = payload[k]
                if isinstance(payload.get("widgets"), dict):
                    lo["widgets"].update(payload["widgets"])
            elif kind == "mode.set":
                if payload.get("mode") in ("LOCAL", "HYBRID", "CLOUD"):
                    self.state["mode"] = payload["mode"]
            elif kind == "surface.register":
                d = self.pixel.register_surface(
                    int(payload.get("width", 0)), int(payload.get("height", 0)),
                    float(payload.get("dpr", 1.0)),
                    payload.get("kind", "screen"),
                    surface_id=payload.get("surface_id"),
                    input_caps=payload.get("input_caps"))
                self.state["surfaces"][d["surface_id"]] = d
            elif kind == "surface.resize":
                d = self.pixel.resize_surface(
                    payload.get("surface_id", ""),
                    int(payload.get("width", 0)), int(payload.get("height", 0)),
                    payload.get("dpr"))
                if d:
                    self.state["surfaces"][d["surface_id"]] = d
            elif kind == "ink.stroke":
                rec = self.pixel.ingest_stroke(
                    payload.get("surface_id", ""),
                    payload.get("points", []),
                    kind=payload.get("pointer", "pen"),
                    color=payload.get("color", "#e8eaed"),
                    target=payload.get("target"))
                if rec:
                    rec["receipt_hash"] = law_result.get("receipt_hash", "")
                    self.state["ink"].append(rec)
            elif kind == "ink.clear":
                tgt = payload.get("target")
                self.state["ink"] = ([] if not tgt else
                    [s for s in self.state["ink"] if s.get("target") != tgt])
            elif kind == "fridge.scan":
                import base64
                img = b""
                if payload.get("image_b64"):
                    try:
                        img = base64.b64decode(payload["image_b64"])
                    except Exception:
                        img = b""
                rec = self.fridge.scan(img, caption=payload.get("caption", ""),
                                       filename=payload.get("filename", ""))
                # auto-confirm matched items into inventory
                self.fridge.confirm([m["key"] for m in rec["matched"]])
                self.state["fridge"] = self.fridge.export()
                self.state["fridge"]["last_scan"] = {
                    k: rec[k] for k in ("scan_id", "image_hash", "matched",
                                        "vision_available", "note")}
            elif kind == "fridge.item.add":
                self.fridge.add_item(payload.get("name", ""),
                                     int(payload.get("qty", 1)))
                self.state["fridge"] = self.fridge.export()
            elif kind == "fridge.item.remove":
                self.fridge.remove_item(payload.get("key", ""))
                self.state["fridge"] = self.fridge.export()
            elif kind == "fridge.profile.set":
                self.fridge.set_profile(payload.get("lane", "adult"),
                                        likes=payload.get("likes"),
                                        dislikes=payload.get("dislikes"),
                                        tags=payload.get("tags"))
                self.state["fridge"] = self.fridge.export()
            elif kind == "fridge.suggest":
                ideas = self.fridge.meal_ideas(
                    payload.get("meal", "dinner"),
                    lane=payload.get("lane", "adult"),
                    extra_tags=payload.get("tags", []))
                self.state["fridge"] = self.fridge.export()
                self.state["fridge"]["last_ideas"] = ideas
            elif kind == "fridge.list":
                sl = self.fridge.shopping_list(payload.get("recipes", []))
                self.state["fridge"] = self.fridge.export()
                self.state["fridge"]["shopping_list"] = sl
            elif kind in ("link.set", "link.refresh"):
                if kind == "link.refresh":
                    prev = self.state["links"].get(payload.get("name", ""), {})
                    payload = {k: prev.get(k) for k in
                               ("name", "source", "format", "kind")} | {"inline": None}
                rec = self.links.link(
                    payload.get("name", ""), payload.get("source", ""),
                    fmt=payload.get("format", "json"),
                    kind=payload.get("kind", "data"),
                    fetcher=self._fetcher_for(payload.get("kind", "data")),
                    inline=payload.get("inline"))
                self.state["links"][rec.get("name", "?")] = rec
            elif kind == "sync.now":
                self.state["sync"] = run_git_sync(self.state.get("sync", {}),
                                                  self.state.get("mode", "LOCAL"))
            # unknown kinds: receipted but state-neutral (still lib items)
            self._flush()

        return {"ok": True, "law": law_result, "state": self.state}

    def _fetcher_for(self, link_kind: str):
        """Connectivity-mode gate (the user's three-mode toggle, enforced):
        LOCAL  -> no url fetching at all
        HYBRID -> ONLY calendar-kind links may go online
        CLOUD  -> everything may fetch"""
        mode = self.state.get("mode", "LOCAL")
        if mode == "LOCAL":
            return None
        if mode == "HYBRID" and link_kind != "calendar":
            return None

        def fetch(url: str) -> str:
            import urllib.request
            req = urllib.request.Request(url, headers={"User-Agent": "PaneForge/0.1"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.read().decode("utf-8", errors="replace")
        return fetch


# ─── Daily git sync — the curated-lib update channel ─────────────────────────
# The company curates the lib + datasets upstream; sticks pull daily.
# LOCAL mode never syncs (pure offline); HYBRID/CLOUD pull from the stick's
# own git remote (first-party update channel). Every sync is an EVENT.

SYNC_INTERVAL_S = 24 * 3600

def run_git_sync(sync_state: Dict[str, Any], mode: str) -> Dict[str, Any]:
    import subprocess
    log = list(sync_state.get("log", []))[-19:]
    entry: Dict[str, Any] = {"ts": time.time(), "mode": mode}
    if mode == "LOCAL":
        entry["result"] = "skipped: LOCAL mode is fully offline"
    elif not (_ROOT / ".git").is_dir():
        entry["result"] = "skipped: no git checkout at stick root (first-run sticks sync once a remote is set)"
    else:
        try:
            r = subprocess.run(["git", "pull", "--ff-only"], cwd=str(_ROOT),
                               capture_output=True, text=True, timeout=120)
            entry["result"] = (r.stdout or r.stderr or "").strip()[:400]
            entry["ok"] = r.returncode == 0
        except Exception as exc:
            entry["result"] = f"sync failed: {exc}"
            entry["ok"] = False
    log.append(entry)
    return {"last": time.time(), "log": log}


def _sync_timer(store_ref) -> None:
    """Daemon: checks hourly; fires a receipted sync.now daily."""
    while True:
        time.sleep(3600)
        try:
            last = store_ref.state.get("sync", {}).get("last", 0)
            if time.time() - last >= SYNC_INTERVAL_S:
                store_ref.apply("sync.now", {"trigger": "daily-timer"})
        except Exception:
            pass


# ─── HTTP server (stdlib only — nothing to install on the stick) ─────────────

_MIME = {".html": "text/html", ".js": "text/javascript", ".css": "text/css",
         ".svg": "image/svg+xml", ".webmanifest": "application/manifest+json",
         ".json": "application/json", ".png": "image/png", ".jpg": "image/jpeg"}

law = EventLaw(_DATA_DIR)
store = StateStore(_DATA_DIR, law)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str = "application/json") -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj: Any, code: int = 200) -> None:
        self._send(code, json.dumps(obj).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            return self._json({"ok": True, "service": "paneforge-kernel",
                               "law": "compute->save->validate->receipt(2)->reuse",
                               "receipts": law.engine.receipt.length})
        if path == "/api/state":
            return self._json({"state": store.state, "kernel": law.status()})
        if path == "/api/receipts":
            return self._json({"recent": law.engine.receipt.recent(20),
                               "head": law.engine.receipt.head,
                               "length": law.engine.receipt.length})
        if path == "/api/kernel":
            st = law.status()
            st["pixelforge"] = store.pixel.status()
            return self._json(st)
        # static PWA
        rel = "index.html" if path in ("/", "") else path.lstrip("/")
        f = (_APP_DIR / rel).resolve()
        if _APP_DIR.resolve() in f.parents or f == (_APP_DIR / "index.html").resolve():
            if f.is_file():
                return self._send(200, f.read_bytes(),
                                  _MIME.get(f.suffix, "application/octet-stream"))
        return self._json({"error": "not found"}, 404)

    MAX_BODY = 2_000_000        # 2 MB cap — a stroke with thousands of points fits

    def do_POST(self):
        path = urlparse(self.path).path
        n = int(self.headers.get("Content-Length", 0))
        if n > self.MAX_BODY:
            return self._json({"ok": False, "error": "payload too large"}, 413)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except (json.JSONDecodeError, UnicodeDecodeError):
            return self._json({"ok": False, "error": "bad json"}, 400)
        if not isinstance(body, dict):
            return self._json({"ok": False, "error": "object body required"}, 400)
        if path == "/api/event":
            kind = body.get("kind", "")
            payload = body.get("payload", {})
            if not kind or not isinstance(kind, str) or len(kind) > 64:
                return self._json({"ok": False, "error": "kind required"}, 400)
            if not isinstance(payload, dict):
                return self._json({"ok": False, "error": "payload must be object"}, 400)
            try:
                return self._json(store.apply(kind, payload))
            except Exception as exc:                      # law must never 500 silently
                return self._json({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, 500)
        return self._json({"error": "not found"}, 404)


def main(port: int = 8770) -> None:
    print(f"PaneForge kernel | lib-forge: {_LIB_FORGE}")
    print(f"  Event Law active: compute -> save -> validate -> receipt(2 links) -> reuse")
    print(f"  Daily lib sync: git channel ({'active' if (_ROOT / '.git').is_dir() else 'no checkout yet'})")
    print(f"  Display + control + API: http://localhost:{port}/")
    threading.Thread(target=_sync_timer, args=(store,), daemon=True).start()
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8770)
