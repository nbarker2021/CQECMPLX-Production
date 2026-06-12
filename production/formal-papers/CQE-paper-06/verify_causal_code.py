#!/usr/bin/env python3
"""Finite verifier for CQE Paper 06, Causal Code."""

from __future__ import annotations

import json
from pathlib import Path


ALLOWED_TYPES = {
    "uses",
    "proves",
    "refines",
    "obligates",
    "transports",
    "repairs",
    "constrains",
    "verifies",
}
ALLOWED_STATUSES = {"open", "closed", "deferred", "rejected"}
REQUIRED_FIELDS = {"source", "target", "edge_type", "receipt", "status"}
PROOF_SUPPORT_TYPES = {"uses", "proves", "refines", "transports", "repairs", "constrains", "verifies"}


EDGES = [
    {"source": "CQE-paper-00", "target": "CQE-paper-01", "edge_type": "uses", "receipt": "paper00-contract", "status": "closed"},
    {"source": "CQE-paper-01", "target": "CQE-paper-02", "edge_type": "uses", "receipt": "lcr-carrier-receipt", "status": "closed"},
    {"source": "CQE-paper-02", "target": "CQE-paper-03", "edge_type": "transports", "receipt": "correction-surface-receipt", "status": "closed"},
    {"source": "CQE-paper-03", "target": "CQE-paper-04", "edge_type": "constrains", "receipt": "triality-surface-receipt", "status": "closed"},
    {"source": "CQE-paper-04", "target": "CQE-paper-05", "edge_type": "repairs", "receipt": "boundary-repair-receipt", "status": "closed"},
    {"source": "CQE-paper-05", "target": "CQE-paper-06", "edge_type": "transports", "receipt": "oloid-path-carrier-receipt", "status": "closed"},
    {"source": "CQE-paper-06", "target": "cqe_engine.formal", "edge_type": "obligates", "receipt": "paper06-open-obligation", "status": "open"},
]


def valid_edge(edge: dict) -> bool:
    return (
        REQUIRED_FIELDS.issubset(edge)
        and edge["edge_type"] in ALLOWED_TYPES
        and edge["status"] in ALLOWED_STATUSES
        and bool(edge["receipt"])
    )


def has_cycle(edges: list[dict]) -> bool:
    graph: dict[str, list[str]] = {}
    for edge in edges:
        if edge["edge_type"] not in PROOF_SUPPORT_TYPES or edge["status"] != "closed":
            continue
        graph.setdefault(edge["source"], []).append(edge["target"])

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for target in graph.get(node, []):
            if visit(target):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in graph)


def verify() -> dict:
    invalid_missing_receipt = {"source": "A", "target": "B", "edge_type": "uses", "status": "closed"}
    invalid_unknown_type = {"source": "A", "target": "B", "edge_type": "magically_proves", "receipt": "x", "status": "closed"}
    hidden_cycle = [
        {"source": "A", "target": "B", "edge_type": "proves", "receipt": "ab", "status": "closed"},
        {"source": "B", "target": "A", "edge_type": "proves", "receipt": "ba", "status": "closed"},
    ]

    checks = {
        "all_edges_have_required_fields": all(REQUIRED_FIELDS.issubset(edge) for edge in EDGES),
        "all_edges_have_allowed_type_and_status": all(valid_edge(edge) for edge in EDGES),
        "closed_proof_support_graph_is_acyclic": not has_cycle(EDGES),
        "open_obligations_remain_open": any(edge["status"] == "open" and edge["edge_type"] == "obligates" for edge in EDGES),
        "missing_receipt_rejected": not valid_edge(invalid_missing_receipt),
        "unknown_type_rejected": not valid_edge(invalid_unknown_type),
        "hidden_proof_cycle_rejected": has_cycle(hidden_cycle),
    }

    return {
        "paper": "CQE-paper-06",
        "theorem": "Typed causal edge contract",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "edges": EDGES,
        "falsifiers": {
            "missing_receipt_accepted": valid_edge(invalid_missing_receipt),
            "unknown_type_accepted": valid_edge(invalid_unknown_type),
            "hidden_cycle_detected": has_cycle(hidden_cycle),
        },
        "corrected_claim": "Causal code tracks open obligations explicitly; it does not declare the corpus fully resolved.",
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("causal_code_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
