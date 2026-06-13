#!/usr/bin/env python3
"""Reapplication verifier: the D12 idempotent chain (T_D12_CHAIN), bound into
CQE Paper 03 (D4 / J3 triality surface).

T_D12_CHAIN is recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers
in lattice_forge/d12_action.py, vendored in the production substrate, bound to
no production paper. It is the natural companion of the S3 annealing
(ConvergeForge) and the D4 chart atlas (ConvergeForge.d4_atlas) already bound
to this paper, and it ties to the idempotent grounding (GroundingForge, p00):
the D12 action on the D4 chart is realized by idempotents, and the chain of
idempotents preserves the trace-2 stratum.

Theorems reapplied (each runs its substrate verifier):
  - D12 group axioms (closure, identity, inverses)
  - D12 idempotent chain (the chain of idempotent color actions)
  - D12 action matches the Weyl (1,3) involution
  - D12 color action preserves the trace-2 idempotent stratum
  - D12 conjugation permutes the D4 antipodal axis classes
  - D12 orbit structure on the D4 chart states

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

from lattice_forge import d12_action as d12  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    results = {
        "d12_group_axioms": d12.verify_d12_group_axioms(),
        "d12_idempotent_chain": d12.verify_d12_idempotent_chain(),
        "d12_action_matches_weyl_13": d12.verify_d12_action_matches_weyl_13(),
        "d12_color_action_preserves_trace2": d12.verify_d12_color_action_preserves_trace2(),
        "d12_conjugation_permutes_d4_axis_classes": d12.verify_d12_conjugation_permutes_d4_axis_classes(),
        "d12_orbit_on_d4_states": d12.verify_d12_orbit_on_d4_states(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"

    receipt = {
        "paper": "CQE-paper-03",
        "theorem": "D12 idempotent chain (T_D12_CHAIN): the D12 group acts on "
                   "the D4 chart by idempotents, matches the Weyl (1,3) "
                   "involution, preserves the trace-2 idempotent stratum, and "
                   "permutes the D4 antipodal axis classes",
        "forge": "lattice_forge.d12_action (reapplied)",
        "reapplication": True,
        "closes": "paper-binding gap for THEOREM_REGISTRY T_D12_CHAIN (PROVEN, "
                  "verifiers in lattice_forge/d12_action.py, bound to no "
                  "production paper)",
        "ties_to": "GroundingForge p00 (idempotence as binding invariant), "
                   "ConvergeForge p03 (S3 annealing + D4 atlas)",
        "source_module": "lattice_forge/d12_action.py",
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    out = _HERE / "d12_idempotent_chain_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
