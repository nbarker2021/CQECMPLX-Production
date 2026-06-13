#!/usr/bin/env python3
"""Finite verifier binding ReadoutForge to CQE Paper 10 (T10 Master Receipt).

This settles the O(log N) Rule 30 readout question correctly. The earlier
verdict (verify_correction_extraction_verdict.py, paper-06) answered COLD
single-bit extraction with no enumeration and found it open — which is the
Wolfram Rule 30 Problem 3. That was the wrong question for this architecture.

The architecture is the STREAMING / aggregate-during-enumeration model: the
table creation, plotting, organizing, and addressing happen DURING the
enumeration, before any state uses the data. By readout time the correction
for bit N is already accumulated in the lib, addressed by N. Then

    readout(N) = LucasBit(N, 0) XOR lib[N]

is O(log N): a Lucas bit-AND over the ~log2(N) bits of N plus one addressed
lib lookup. Measured: reading bit 511 costs 10 operations (9 Lucas + 1
lookup) = log2(511)+1. Bit-exact against direct simulation for every N to
depth 512. The frontier repair window is exactly 1 (the newest row's diagonal
term), closed by the three-move SU(3) Weyl closure (T4).

What this DOES claim (verified, bit-exact): once the lib is built by the
enumeration you are already doing, every center bit reads out in O(log N),
reuse is free (Event Law / SpeedLight idempotence), and per-step novelty is a
bounded repair window.

What this does NOT claim: cold single-bit extraction with no prior
enumeration in O(log N). That remains the open Wolfram Rule 30 Problem 3. The
aggregation pass itself is the enumeration cost; this verifier bounds the
READOUT, not the enumeration.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import ReadoutForge  # noqa: E402


def main() -> int:
    result = ReadoutForge.verify()
    receipt = {
        "paper": "CQE-paper-10",
        "theorem": "O(log N) Rule 30 readout by aggregate-during-enumeration: "
                   "readout(N) = LucasBit(N,0) XOR lib[N], one log-N addressing "
                   "plus one addressed lookup, bit-exact, bounded (<=1) frontier "
                   "repair window, free idempotent reuse",
        "forge": "ReadoutForge",
        "corrects_prior_verdict": {
            "prior": "formal-papers/CQE-paper-06/correction_extraction_verdict_receipt.json",
            "what_prior_answered": "cold single-bit extraction with no "
                                   "enumeration — found open (Wolfram Problem 3)",
            "why_it_was_the_wrong_question": "the architecture aggregates the "
                                             "correction into the lib DURING "
                                             "enumeration; readout addresses "
                                             "what is already built, it does "
                                             "not recompute it cold",
        },
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "measured": result["measured"],
        "still_open": "cold O(log N) single-bit extraction with no prior "
                      "enumeration = Wolfram Rule 30 Problem 3 — NOT claimed; "
                      "the enumeration/aggregation pass is the amortized cost",
    }
    out = _HERE / "ologn_readout_architecture_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "passed": result["passed"],
                      "total": result["total"], "receipt": str(out)}, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
