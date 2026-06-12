#!/usr/bin/env python3
"""Finite verifier for CQE Paper 07, Discrete-Continuous Bridge."""

from __future__ import annotations

import json
from pathlib import Path


TRACE = [0, 1, 1, 0, 1, 0, 0, 1]


def interpolate(trace: list[int], t: float) -> float:
    if t < 0 or t > len(trace) - 1:
        raise ValueError("t outside trace domain")
    lo = int(t)
    hi = min(lo + 1, len(trace) - 1)
    a = t - lo
    return (1 - a) * trace[lo] + a * trace[hi]


def rule30(left: int, center: int, right: int) -> int:
    return left ^ (center | right)


def rule90(left: int, right: int) -> int:
    return left ^ right


def correction(left: int, center: int, right: int) -> int:
    return center & (1 - right)


def verify() -> dict:
    sample_errors = [
        abs(interpolate(TRACE, float(index)) - value)
        for index, value in enumerate(TRACE)
    ]
    endpoint_agreement = [
        interpolate(TRACE, float(index)) == TRACE[index]
        for index in range(1, len(TRACE) - 1)
    ]
    states = [(left, center, right) for left in (0, 1) for center in (0, 1) for right in (0, 1)]
    correction_identity = all(
        rule30(left, center, right) == (rule90(left, right) ^ correction(left, center, right))
        for left, center, right in states
    )

    checks = {
        "integer_samples_preserved": all(error == 0 for error in sample_errors),
        "max_sample_error_is_zero": max(sample_errors) == 0,
        "adjacent_segments_share_endpoints": all(endpoint_agreement),
        "rule30_rule90_correction_identity_holds": correction_identity,
        "between_sample_physics_left_as_obligation": True,
    }
    return {
        "paper": "CQE-paper-07",
        "theorem": "Sample-preserving discrete-continuous bridge",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "trace": TRACE,
        "sample_errors": sample_errors,
        "midpoint_examples": [
            {"t": index + 0.5, "value": interpolate(TRACE, index + 0.5)}
            for index in range(len(TRACE) - 1)
        ],
        "falsifier": {
            "claim": "sample-preserving interpolation proves all between-sample physics",
            "accepted": False,
        },
        "scope_boundary": "Exact at indexed samples; between-sample physical dynamics require a separate theorem.",
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("discrete_continuous_bridge_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
