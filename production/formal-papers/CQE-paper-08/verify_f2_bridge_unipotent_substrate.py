#!/usr/bin/env python3
"""Reapplication verifier: the F2 Majorana bridge, E8 unipotent orbits, and the
substrate map, bound into CQE Paper 08 (E8 / Niemeier / Leech closure).

Recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers in
lattice_forge/{f2_majorana,unipotent_orbits,substrate_map}.py, vendored, bound
to no production paper.

Theorems reapplied (each runs its substrate verifier):
  - F2 Majorana: F2 quadratic-form / Arf-invariant governance (the algebraic
    core of obligation O2'' T_F2_BRIDGE)
  - unipotent orbit tables (E8 nilpotent / unipotent orbit structure)
  - substrate map (the lattice-forge substrate identity map)

O2'' NOTE (honest): obligation O2'' (T_F2_BRIDGE governance) records the
algebraic core as implemented and the full population of the registry across
the umbrella's surface as the open scope. This binds the PROVEN algebraic core
(verify_f2_majorana — Arf invariants, edge-glue isometry); the registry
population remains open and is NOT claimed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import f2_majorana, unipotent_orbits, substrate_map  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    results = {
        "f2_majorana_arf_bridge": f2_majorana.verify_f2_majorana(),
        "unipotent_orbit_tables": unipotent_orbits.verify_unipotent_orbit_tables(),
        "substrate_map": substrate_map.verify_substrate_map(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "F2 Majorana Arf bridge + E8 unipotent orbits + substrate "
                   "map: the F2 quadratic-form governance core, the unipotent "
                   "orbit tables, and the substrate identity map",
        "forge": "lattice_forge.{f2_majorana,unipotent_orbits,substrate_map} (reapplied)",
        "reapplication": True,
        "advances_obligation": {
            "obligation": "O2'' (T_F2_BRIDGE governance), "
                          "CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md",
            "proven_now": "the algebraic core (Arf invariants, edge-glue "
                          "isometry) via verify_f2_majorana",
            "still_open": "full population of the contributions registry across "
                          "the umbrella's surface — NOT claimed",
        },
        "source_modules": ["f2_majorana", "unipotent_orbits", "substrate_map"],
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    out = _HERE / "f2_bridge_unipotent_substrate_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
