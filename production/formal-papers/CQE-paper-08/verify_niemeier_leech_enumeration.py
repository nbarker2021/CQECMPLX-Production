#!/usr/bin/env python3
"""Reapplication verifier: the Niemeier / Leech enumeration, bound into
CQE Paper 08 (E8 / Niemeier / Leech closure), with the honest O7 status.

Recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers in
lattice_forge/{enumerated_glue,nebe_gamma72}.py, vendored, bound to no
production paper. This binds the substrate's Niemeier/Leech enumeration and
advances obligation O7 (Niemeier:E8^3 exact glue cosets).

Theorems reapplied (each runs its substrate verifier):
  - enumerated glue selector contract: deterministic selectors, block orders
    are permutations, all carriers are E8^3, Leech landing proved
  - Leech minimal landings + type-1/2/3 orbit enumerations
  - the Nebe 72-dimensional lattice contract

O7 STATUS (honest): the obligation O7 records the path F4 -> ... ->
Niemeier:E8^3 as registered with the exact integer-vector glue cosets at the
FINAL edge still open (computed as discriminant/index profiles, not explicit
coset representatives). This verifier confirms what IS proven — the E8^3
carrier structure, deterministic selectors, and Leech landing — and records
that the exact glue-coset representatives remain the pending_invariants part.
O7 is therefore PARTIALLY resolved, not fully closed; the pending part is not
claimed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import enumerated_glue as eg, nebe_gamma72 as nebe  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    glue = eg.verify_enumerated_glue_selector_contract()
    results = {
        "enumerated_glue_selector_contract": glue,
        "leech_minimal_landings": eg.verify_enumerated_leech_minimal_landings(),
        "leech_type1_orbit": eg.verify_enumerated_leech_type1_orbit(),
        "leech_type2_orbit": eg.verify_enumerated_leech_type2_orbit(),
        "leech_type3_orbit": eg.verify_enumerated_leech_type3_orbit(),
        "nebe_gamma72_contract": nebe.verify_nebe_gamma72_contract(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "Niemeier / Leech enumeration: deterministic glue selectors, "
                   "E8^3 carriers, Leech landing + type-1/2/3 orbits, Nebe 72 "
                   "contract",
        "forge": "lattice_forge.{enumerated_glue, nebe_gamma72} (reapplied)",
        "reapplication": True,
        "advances_obligation": {
            "obligation": "O7 (Niemeier:E8^3 exact glue cosets), "
                          "CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md",
            "proven_now": "E8^3 carrier structure, deterministic selectors, "
                          "Leech landing, type-1/2/3 orbits, Nebe 72 contract",
            "still_pending": "the exact integer-vector glue-coset representatives "
                             "at the final edge (the glue verifier's "
                             "pending_invariants) — NOT claimed",
            "status": "O7 PARTIALLY resolved",
        },
        "glue_contract_fields": {k: glue.get(k) for k in
                                 ("all_selectors_deterministic",
                                  "all_block_orders_are_permutations",
                                  "all_carriers_are_e8_cubed",
                                  "leech_landing_proved",
                                  "pending_invariants")},
        "source_modules": ["enumerated_glue", "nebe_gamma72"],
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    out = _HERE / "niemeier_leech_enumeration_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
