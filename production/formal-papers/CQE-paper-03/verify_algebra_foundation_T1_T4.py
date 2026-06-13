#!/usr/bin/env python3
"""Reapplication verifier: the algebra-foundation theorems T1-T4, bound into
CQE Paper 03 (D4 / J3 triality surface).

These four theorems are recorded PROVEN with named verifiers in
CMPLX-R30-main/PROOF/theorems/THEOREM_REGISTRY.md, and their verifier modules
are vendored in the production substrate (lattice_forge), but none was bound
to a production paper. The proofs existed and pass; they simply had not been
reapplied into the paper-bound space. Paper 03 is their natural home: it is
the J3(O) triality surface, where ConvergeForge already carries the S3
annealing and the D4 chart atlas.

Theorems reapplied (each runs its registry-named verifier):
  T1  Octonion algebra axioms        — octonion.verify_octonion_axioms()
  T2  J3(O) Jordan algebra axioms     — jordan_j3.verify_j3o_axioms()
  T3  Chart -> J3(O) isomorphism      — rule30.verify_chart_j3o_isomorphism()
  T4  Exact n=3 SU(3) Weyl closure    — f4_action.verify_n3_su3_closure_exact()

T3 is the load-bearing bridge: the chart's local (L,C,R) state IS a J3(O)
diagonal element, the shell=2 stratum IS the trace-2 idempotent stratum, and
the Weyl L<->R involution IS the (1,3) transposition in J3(O). T4 shows the
3-step shell=2 transition matrix is an EXACT rational combination of S3
permutation matrices (not approximate) — the chart's SU(3) Weyl coherence.

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

from lattice_forge import octonion, jordan_j3, rule30, f4_action  # noqa: E402


def main() -> int:
    t1 = octonion.verify_octonion_axioms()
    t2 = jordan_j3.verify_j3o_axioms()
    t3 = rule30.verify_chart_j3o_isomorphism(max_depth=512)
    t4 = f4_action.verify_n3_su3_closure_exact()

    checks = {
        "T1_octonion_axioms": t1.get("status") == "pass",
        "T2_j3o_jordan_axioms": t2.get("status") == "pass",
        "T3_chart_j3o_isomorphism": t3.get("status") == "pass",
        "T3_zero_bijection_failures": t3.get("bijection_failures") == 0,
        "T3_shell2_is_trace2_idempotent_stratum": (
            t3.get("trace_2_all_idempotent") is True
            and t3.get("trace_2_idempotent_count") == t3.get("trace_2_stratum_count")
        ),
        "T4_su3_closure_exact": t4.get("status") == "pass",
        "T4_is_exact_group_ring_element": t4.get("is_exact_group_ring_element") is True,
        "T4_residual_squared_zero": t4.get("residual_squared_exact") == "0",
    }
    status = "pass" if all(checks.values()) else "fail"

    receipt = {
        "paper": "CQE-paper-03",
        "theorem": "Algebra foundation T1-T4 reapplied: octonion axioms, "
                   "J3(O) Jordan axioms, chart->J3(O) isomorphism, exact n=3 "
                   "SU(3) Weyl closure",
        "reapplication": True,
        "closes": "the paper-binding gap for THEOREM_REGISTRY T1, T2, T3, T4 "
                  "(PROVEN with verifiers, vendored in the substrate, but bound "
                  "to no production paper)",
        "source_modules": [
            "lattice_forge/octonion.py :: verify_octonion_axioms",
            "lattice_forge/jordan_j3.py :: verify_j3o_axioms",
            "lattice_forge/rule30.py :: verify_chart_j3o_isomorphism",
            "lattice_forge/f4_action.py :: verify_n3_su3_closure_exact",
        ],
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "verifier_receipts": {
            "T1": {"checks_passed": t1.get("checks_passed")},
            "T2": {"checks_passed": t2.get("checks_passed")},
            "T3": {"max_depth": t3.get("max_depth"),
                   "bijection_failures": t3.get("bijection_failures"),
                   "trace_2_stratum_count": t3.get("trace_2_stratum_count")},
            "T4": {"s3_coefficients": t4.get("s3_coefficients_exact_strings"),
                   "coefficient_sum_exact": t4.get("coefficient_sum_exact")},
        },
    }
    out = _HERE / "algebra_foundation_T1_T4_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
