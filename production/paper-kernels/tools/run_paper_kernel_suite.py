#!/usr/bin/env python3
"""Run/select CQECMPLX paper kernels and emit receipts.

This is a structural runner: it verifies source bindings, component coverage,
edge/wrap rules, and hidden-guess readiness. It does not claim to discharge the
paper mathematics; it prepares the deployable receipt layer each paper needs.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load_registry(repo_root: Path) -> dict:
    path = repo_root / "production" / "paper-kernels" / "PAPER_KERNEL_REGISTRY.json"
    return json.loads(path.read_text(encoding="utf-8"))


def paper_ids_for_selector(registry: dict, selector: str) -> list[str]:
    papers = registry["papers"]
    by_id = {paper["id"]: paper for paper in papers}
    blocks = {block["id"]: block for block in registry["blocks"]}
    if selector == "suite":
        return [paper["id"] for paper in papers]
    if selector in blocks:
        return blocks[selector]["papers"]
    if selector in by_id:
        return [selector]
    raise SystemExit(f"unknown selector: {selector}")


def validate_paper(repo_root: Path, paper: dict, training_mode: bool) -> dict:
    missing_sources = [
        name for name, meta in paper["sources"].items()
        if not meta["present"] and name != "tool_runner"
    ]
    optional_missing = [
        name for name, meta in paper["sources"].items()
        if not meta["present"] and name == "tool_runner"
    ]
    component_count = len(paper["components"])
    component_ids = sorted(paper["components"].keys())
    expected_components = sorted([
        "claims",
        "math",
        "formal_algebra_calculus",
        "hand_work",
        "code_rebuild",
        "lib_bindings",
        "tests_and_receipts",
        "deployment_kernel",
    ])
    component_ok = component_count == 8 and component_ids == expected_components
    hidden_guess_ready = training_mode or "hidden-guess" in paper["components"]["tests_and_receipts"]["primary_content"].lower()
    kernel_file = repo_root / "production" / "paper-kernels" / "papers" / paper["id"] / "PAPER_KERNEL.md"
    manifest_file = repo_root / "production" / "paper-kernels" / "papers" / paper["id"] / "paper_kernel_manifest.json"
    return {
        "paper": paper["id"],
        "title": paper["title"],
        "block": paper["block"],
        "component_count": component_count,
        "component_ok": component_ok,
        "required_sources_missing": missing_sources,
        "optional_sources_missing": optional_missing,
        "kernel_file_present": kernel_file.exists(),
        "manifest_file_present": manifest_file.exists(),
        "suite_previous": paper["suite_previous"],
        "suite_next": paper["suite_next"],
        "block_previous": paper["block_previous"],
        "block_next": paper["block_next"],
        "hidden_guess_ready": hidden_guess_ready,
        "training_mode": training_mode,
        "status": "pass" if component_ok and not missing_sources and kernel_file.exists() and manifest_file.exists() and hidden_guess_ready else "needs-work",
    }


def run(repo_root: Path, selector: str, training_mode: bool, write_receipt: bool) -> dict:
    registry = load_registry(repo_root)
    ids = paper_ids_for_selector(registry, selector)
    by_id = {paper["id"]: paper for paper in registry["papers"]}
    results = [validate_paper(repo_root, by_id[paper_id], training_mode) for paper_id in ids]
    receipt = {
        "suite": registry["suite"],
        "selector": selector,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "paper_00_contract": registry["preamble_contract"]["id"],
        "paper_00_role": registry["preamble_contract"]["role"],
        "training_mode": training_mode,
        "selected_count": len(results),
        "pass_count": sum(1 for result in results if result["status"] == "pass"),
        "needs_work_count": sum(1 for result in results if result["status"] != "pass"),
        "results": results,
    }
    if write_receipt:
        receipt_dir = repo_root / "production" / "paper-kernels" / "receipts"
        receipt_dir.mkdir(parents=True, exist_ok=True)
        safe_selector = selector.replace("/", "_")
        out = receipt_dir / f"{safe_selector}_receipt.json"
        out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        receipt["receipt_path"] = str(out.relative_to(repo_root))
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--selector", default="suite", help="suite, block id, or CQE-paper-NN")
    parser.add_argument("--training-mode", action="store_true", help="Enable hidden-guess honesty layer as mandatory.")
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = run(Path(args.repo_root).resolve(), args.selector, args.training_mode, args.write_receipt)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
