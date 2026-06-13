#!/usr/bin/env python3
"""Finite verifier binding GroundingForge to CQE Paper 00 (the burden /
admissibility contract).

This closes the single remaining gap the operator named: tying the existing,
proven, daily-use theorem that makes all the continuation work just a
restatement of established mathematics, newly connected. The work is not new
math within any field; it is the CONNECTION of fields not normally connected,
through the same existing math that started it all, which is idempotent and
dual to one other thing.

What started it all: LUCAS' THEOREM (1878). Over GF(2), C(m,n) mod 2 = 1 iff n
is a submask of m (n AND m == n). This IS Rule 90 = Pascal mod 2 = Sierpinski,
the closed form behind every O(log N) result. Its mechanism is the bitwise AND
submask relation. AND is idempotent (x AND x = x), De Morgan dual to OR (the
one other thing). Rule 30 = L XOR (C OR R), correction = C AND NOT R: the whole
base is the one idempotent dual pair {AND, OR} plus XOR.

The only outside inclusions are proven, cited, daily-use theorems (Lucas 1878,
Kummer 1852, Boole/De Morgan, Steinhaus three-gap 1958, CRT, J3(O)
Jordan-von Neumann-Wigner 1934, Conway-Sloane lattices 1988, Golay 1949,
Conway-Norton moonshine 1979). The only thing the framework ADDS is the
chart -> J3(O) isomorphism (T3), a verified connection, not new mathematics.

Checks (all finite): see GroundingForge.verify().
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import GroundingForge  # noqa: E402


def main() -> int:
    result = GroundingForge.verify()
    receipt = {
        "paper": "CQE-paper-00",
        "theorem": "Established grounding: the only outside inclusions are "
                   "proven daily-use theorems; the origin is Lucas' theorem "
                   "(1878), the idempotent AND-submask base dual to OR; the "
                   "only addition is the verified chart->J3(O) connection (T3)",
        "forge": "GroundingForge",
        "closes_gap": "the operator's single remaining gap — tying the existing "
                      "proven theorem + citation that makes all continuation "
                      "work a restatement of established math, newly connected, "
                      "idempotent to one other thing, as the only outside input",
        "origin_theorem": result["origin_theorem"],
        "the_only_addition": result["the_only_addition"],
        "imported_theorems": GroundingForge.ESTABLISHED_THEOREMS,
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "honesty": "The framework restates established theorems and adds one "
                   "verified connection (T3). It does NOT extend exceptional "
                   "Lie/Jordan/lattice/moonshine theory (OPEN_OBLIGATIONS O10).",
    }
    out = _HERE / "established_grounding_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "passed": result["passed"],
                      "total": result["total"], "receipt": str(out)}, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
