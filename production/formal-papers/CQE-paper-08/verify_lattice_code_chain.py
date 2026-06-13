#!/usr/bin/env python3
"""Reapplication verifier: the lattice code chain (T8 family), bound into
CQE Paper 08 (E8 / Niemeier / Leech closure).

Recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers in
lattice_forge/lattice_codes.py, vendored in the production substrate, bound to
no production paper. This is the 1 -> 3 -> 7 -> 8 -> 24 -> 72 lattice code
chain (repetition, Fano/Hamming(7,4,3), extended Hamming(8,4,4)/E8, Golay
(24,12,8)/Leech, Nebe 72) that E8Forge and LeechForge culminate, and the
structural spine of PFC-1 (the D1->D2->D3->D4->Monster->Nebe->A64 chain).

Theorems reapplied (each runs its substrate verifier):
  - extended Hamming(8,4,4) -> E8 Construction A
  - Fano / Hamming(7,4,3) (the octonion multiplication structure)
  - Golay(24,12,8) -> Leech
  - the full lattice code chain
  - the parameter chain and the powered (1->9->49->72) shortcut

Nothing here is new mathematics; it is the reapplication of proven verifiers
to the obligation that they were never paper-bound.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import lattice_codes as lc  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    results = {
        "extended_hamming_8_e8": lc.verify_extended_hamming_8(),
        "hamming_7_fano": lc.verify_hamming_7_fano(),
        "golay_24": lc.verify_golay_24(),
        "lattice_code_chain": lc.verify_lattice_code_chain(),
        "parameter_chain": lc.verify_parameter_chain(),
        "powered_chain": lc.verify_powered_chain(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "Lattice code chain (T8 family): 1->3->7->8->24->72 "
                   "(repetition, Fano/Hamming(7,4,3), ext Hamming(8,4,4)/E8, "
                   "Golay(24,12,8)/Leech, Nebe 72), with the powered shortcut",
        "forge": "lattice_forge.lattice_codes (reapplied)",
        "reapplication": True,
        "closes": "paper-binding gap for the lattice code chain verifiers "
                  "(PROVEN, lattice_forge/lattice_codes.py, bound to no paper)",
        "ties_to": "E8Forge + LeechForge (p08, p17), PFC-1 chain structure",
        "source_module": "lattice_forge/lattice_codes.py",
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    out = _HERE / "lattice_code_chain_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
