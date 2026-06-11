#!/usr/bin/env python3
"""Build the 32-paper kernel registry and block manifests.

The generated files are intentionally lightweight: they bind each paper to
claims, math/formal work, hand work, code rebuild paths, lib bindings,
validation, and deployment hooks without duplicating the source papers.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


COMPONENTS = [
    ("claims", "Claims"),
    ("math", "Math"),
    ("formal_algebra_calculus", "Formal, Normal, Closed-Form Algebra and Calculus"),
    ("hand_work", "By-Hand Reconstruction"),
    ("code_rebuild", "Code Rebuild"),
    ("lib_bindings", "Installable Lib Bindings"),
    ("tests_and_receipts", "Tests and Receipts"),
    ("deployment_kernel", "Deployment Kernel"),
]

EVIDENCE_ROOTS = [
    "production/papers",
    "production/_meta/PAPER-INTENT-INDEX.md",
    "production/_meta/paper_intent_index.json",
    "production/lib-forge/recovered/papers_output",
    "production/lib-forge/recovered/MASTER_PDF",
    "production/lib-forge/engines",
    "production/tool-families",
    "production/operations/ProofKernel-Deploy",
    "D:/CQE_CMPLX/CMPLX-Kernel/kernel/lib-forge",
    "D:/CQE_CMPLX/CQECMPLX-ProofValidatedSuite",
    "D:/CQE_CMPLX/CMPLX-PartsFactory-main/packages/lattice-forge",
    "D:/CQE_CMPLX/Claude-Codex-Memory/Claude work/CL-Paper-Evidence-DB",
]

BLOCKS = [
    ("block-00-papers-01-08", 1, 8, "First Carrier Chain Through Closure"),
    ("block-01-papers-09-16", 9, 16, "Time, Receipts, Admission, Physics Interfaces, and Continuum Edges"),
    ("block-02-papers-17-24", 17, 24, "Correction Towers, Representation Routes, Applied Forge, and Game Automata"),
    ("block-03-papers-25-32", 25, 32, "Energy Horizons, Observer Delay, Grand Ribbon, Meta Walkthrough, and Supervisor Cursor"),
]


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def rel_exists(path: Path) -> bool:
    return path.exists()


def paper32_from_folder(repo_root: Path) -> dict:
    path = repo_root / "production" / "papers" / "CQE-paper-32" / "PAPER-BODY.md"
    text = path.read_text(encoding="utf-8")
    first_line = next(line.strip("# ").strip() for line in text.splitlines() if line.startswith("#"))
    return {
        "n": "32",
        "title": "The Supervisor Cursor",
        "status": "Applied series / verifier-backed operational paper",
        "abstract": "Paper 32 opens the applied series by treating superpermutations as compressed dimensional action graphs and binding that solve to PermForge and GraphStax tooling.",
        "thesis": "Use superpermutation schedules as supervisor cursors: compressed action graphs that enumerate every requested ordering while producing deployable PermForge/GraphStax machinery.",
        "scope": first_line,
        "tool": "- Module: `GraphStax.permforge`\n- Required outputs: coverage receipts, cursor schedules, bounds ladder, and supervisor scheduler records.",
    }


def load_index(repo_root: Path) -> tuple[dict, list[dict]]:
    index_path = repo_root / "production" / "_meta" / "paper_intent_index.json"
    papers = json.loads(index_path.read_text(encoding="utf-8"))
    preamble = next(p for p in papers if p["n"] == "00")
    selected = [p for p in papers if 1 <= int(p["n"]) <= 31]
    if (repo_root / "production" / "papers" / "CQE-paper-32").exists():
        selected.append(paper32_from_folder(repo_root))
    selected.sort(key=lambda p: int(p["n"]))
    if len(selected) != 32:
        raise SystemExit(f"expected exactly 32 active papers (01-32), found {len(selected)}")
    return preamble, selected


def source_paths(repo_root: Path, paper_n: str) -> dict:
    base = Path("production") / "papers" / f"CQE-paper-{paper_n}"
    paths = {
        "body": str(base / "PAPER-BODY.md"),
        "source": str(base / "SOURCE.md"),
        "formal": str(base / "01-CQE-formal" / "FORMAL.md"),
        "tool": str(base / "02-CQE-tool" / "TOOL.md"),
        "tool_runner": str(base / "02-CQE-tool" / "run.py"),
        "workbook": str(base / "03-CQE-workbook" / "WORKBOOK.md"),
        "recovered_output": str(Path("production") / "lib-forge" / "recovered" / "papers_output" / f"CQE-paper-{paper_n}.md"),
    }
    return {
        key: {"path": value, "present": rel_exists(repo_root / value)}
        for key, value in paths.items()
    }


def component_map(paper: dict, paper_n: str) -> dict:
    tool_text = paper.get("tool", "")
    module_match = re.search(r"`([^`]+)`", tool_text)
    module = module_match.group(1) if module_match else f"forgefactory.paper{paper_n}_{slug(paper['title']).replace('-', '_')}"
    return {
        "claims": {
            "status": "seeded",
            "primary_content": paper["thesis"],
            "required_action": "Separate method claims from domain claims before peer-review promotion.",
        },
        "math": {
            "status": "source-bound",
            "primary_content": "Use the paper body axioms, lemmas, and formalism as the math intake.",
            "required_action": "Promote every symbolic statement into a normalized claim row with assumptions and receipts.",
        },
        "formal_algebra_calculus": {
            "status": "source-bound",
            "primary_content": "Use 01-CQE-formal/FORMAL.md and recovered algebra/PDF evidence.",
            "required_action": "Split normal form, closed form, algebraic operators, calculus/window operators, and open obligations.",
        },
        "hand_work": {
            "status": "source-bound",
            "primary_content": "Use 03-CQE-workbook/WORKBOOK.md plus the analog toolkit guides.",
            "required_action": "Write the physical reconstruction steps and boundary-collision handling for the paper.",
        },
        "code_rebuild": {
            "status": "source-bound",
            "primary_content": "Use 02-CQE-tool/TOOL.md and run.py when present.",
            "required_action": "Bind a replayable command or mark the missing executable as an obligation.",
        },
        "lib_bindings": {
            "status": "seeded",
            "primary_content": module,
            "required_action": "Resolve this binding into production/lib-forge or mark it as an adapter route.",
        },
        "tests_and_receipts": {
            "status": "seeded",
            "primary_content": "Every validation and diagnostic must support hidden-guess ablation when training mode is enabled.",
            "required_action": "Add positive, negative, boundary, and wrap tests with receipts.",
        },
        "deployment_kernel": {
            "status": "seeded",
            "primary_content": f"Deployable individually as CQE-paper-{paper_n} and selectable through the master suite.",
            "required_action": "Expose paper, block, and suite selectors with no duplicate routing logic.",
        },
    }


def make_registry(repo_root: Path, preamble: dict, papers: list[dict]) -> dict:
    registry_papers = []
    for paper in papers:
        n = paper["n"]
        idx = int(n)
        block_id, block_start, block_end, block_title = next(
            block for block in BLOCKS if block[1] <= idx <= block[2]
        )
        role = "paper_body_work"
        registry_papers.append(
            {
                "id": f"CQE-paper-{n}",
                "n": n,
                "title": paper["title"],
                "slug": slug(paper["title"]),
                "status": paper["status"],
                "role": role,
                "block": block_id,
                "block_title": block_title,
                "suite_previous": "CQE-paper-32" if idx == 1 else f"CQE-paper-{idx - 1:02d}",
                "suite_next": "CQE-paper-01" if idx == 32 else f"CQE-paper-{idx + 1:02d}",
                "block_previous": f"CQE-paper-{block_end if idx == block_start else idx - 1:02d}",
                "block_next": f"CQE-paper-{block_start if idx == block_end else idx + 1:02d}",
                "central_thesis": paper["thesis"],
                "components": component_map(paper, n),
                "sources": source_paths(repo_root, n),
            }
        )
    return {
        "suite": "CQECMPLX 32-Paper Kernel Suite",
        "paper_count": 32,
        "block_count": 4,
        "papers_per_block": 8,
        "component_count_per_paper": 8,
        "preamble_contract": {
            "id": "CQE-paper-00",
            "title": preamble["title"],
            "role": "past_burden_minimum_information_contract",
            "central_thesis": preamble["thesis"],
            "note": "Paper 00 is outside the four active windows. It is the inherited minimum contract for information burden and method, not the body of work being enumerated.",
            "sources": source_paths(repo_root, "00"),
        },
        "edge_policy": {
            "suite_wrap": "Paper 32 wraps to Paper 01 for active-suite retest; Paper 00 remains the inherited method contract outside the window.",
            "block_wrap": "Each 8-paper block has a local wrap from its last paper back to its first.",
            "boundary_collision": "A failed or partial edge is recorded as an obligation/correction surface, not erased.",
        },
        "required_components": [
            {"id": key, "label": label} for key, label in COMPONENTS
        ],
        "evidence_roots": EVIDENCE_ROOTS,
        "blocks": [
            {
                "id": block_id,
                "title": title,
                "start": f"CQE-paper-{start:02d}",
                "end": f"CQE-paper-{end:02d}",
                "papers": [f"CQE-paper-{n:02d}" for n in range(start, end + 1)],
                "previous_block": BLOCKS[(i - 1) % 4][0],
                "next_block": BLOCKS[(i + 1) % 4][0],
            }
            for i, (block_id, start, end, title) in enumerate(BLOCKS)
        ],
        "papers": registry_papers,
    }


def paper_markdown(entry: dict) -> str:
    component_lines = []
    for key, label in COMPONENTS:
        data = entry["components"][key]
        component_lines.append(
            f"## {label}\n\n"
            f"Status: `{data['status']}`\n\n"
            f"{data['primary_content']}\n\n"
            f"Required next action: {data['required_action']}\n"
        )
    source_lines = [
        f"- `{name}`: `{meta['path']}` ({'present' if meta['present'] else 'missing'})"
        for name, meta in entry["sources"].items()
    ]
    role_note = (
        "This paper is the preamble and method gate. It defines the operating contract "
        "used by the other papers; it is not treated as the whole thesis of the suite."
        if entry["role"] == "preamble_method_gate"
        else "This paper is treated as body work under the Paper 00 operating contract."
    )
    return (
        f"# {entry['id']} - {entry['title']} Kernel\n\n"
        f"Block: `{entry['block']}`\n\n"
        f"Role: `{entry['role']}`\n\n"
        f"{role_note}\n\n"
        f"Suite edges: `{entry['suite_previous']}` -> `{entry['id']}` -> `{entry['suite_next']}`\n\n"
        f"Block edges: `{entry['block_previous']}` -> `{entry['id']}` -> `{entry['block_next']}`\n\n"
        f"Central thesis: {entry['central_thesis']}\n\n"
        + "\n".join(component_lines)
        + "\n## Source Binding\n\n"
        + "\n".join(source_lines)
        + "\n"
    )


def block_markdown(registry: dict, block: dict) -> str:
    papers = [p for p in registry["papers"] if p["id"] in block["papers"]]
    paper_lines = [
        f"- `{p['id']}` - {p['title']} ({p['role']}): {p['central_thesis']}"
        for p in papers
    ]
    return (
        f"# {block['id']} - {block['title']}\n\n"
        f"Range: `{block['start']}` through `{block['end']}`\n\n"
        f"Block neighbors: `{block['previous_block']}` -> `{block['id']}` -> `{block['next_block']}`\n\n"
        "This block is one of the four required 8-paper sets. Its local wrap test moves "
        f"from `{block['end']}` back to `{block['start']}` while the master suite keeps "
        "the global Paper 31 -> Paper 00 wrap.\n\n"
        "## Paper Set\n\n"
        + "\n".join(paper_lines)
        + "\n\n## Required Completion Pass\n\n"
        "For every paper in this block, complete the eight paper-kernel components: "
        "claims, math, formal algebra/calculus, by-hand reconstruction, code rebuild, "
        "installable lib bindings, tests/receipts, and deployment kernel. Paper 00 remains "
        "outside the active window as the inherited minimum information contract.\n"
    )


def write_outputs(repo_root: Path, registry: dict) -> None:
    out = repo_root / "production" / "paper-kernels"
    blocks_dir = out / "blocks"
    papers_dir = out / "papers"
    out.mkdir(parents=True, exist_ok=True)
    blocks_dir.mkdir(parents=True, exist_ok=True)
    papers_dir.mkdir(parents=True, exist_ok=True)

    (out / "PAPER_KERNEL_REGISTRY.json").write_text(
        json.dumps(registry, indent=2) + "\n", encoding="utf-8"
    )
    (out / "README.md").write_text(
        "# CQECMPLX 32-Paper Kernel Suite\n\n"
        "This suite treats Papers 01-32 as four active blocks of eight papers. "
        "Each paper receives the same eight deployable kernel components so it can "
        "run alone or as part of the master suite.\n\n"
        "Paper 00 is outside the active windows. It is the past burden: the minimum "
        "information contract and method requirement inherited by every active paper.\n\n"
        "Primary registry: `PAPER_KERNEL_REGISTRY.json`.\n\n"
        "Block manifests live under `blocks/`; per-paper kernels live under `papers/`.\n",
        encoding="utf-8",
    )
    (out / "PAPER_KERNEL_COMPONENT_SCHEMA.md").write_text(
        "# Paper Kernel Component Schema\n\n"
        "Every CQECMPLX paper kernel has exactly eight required components.\n\n"
        + "\n".join(f"{i + 1}. **{label}** (`{key}`)" for i, (key, label) in enumerate(COMPONENTS))
        + "\n\n"
        "Validation rule: any diagnostic, validation, or test that is not purely math-based "
        "must support the hidden-guess honesty layer when training mode is enabled. The guess "
        "is made before the answer/reconciliation layer is revealed.\n",
        encoding="utf-8",
    )
    for block in registry["blocks"]:
        block_path = blocks_dir / block["id"]
        block_path.mkdir(parents=True, exist_ok=True)
        (block_path / "BLOCK_KERNEL.md").write_text(block_markdown(registry, block), encoding="utf-8")
        (block_path / "block_manifest.json").write_text(
            json.dumps(block, indent=2) + "\n", encoding="utf-8"
        )
    for entry in registry["papers"]:
        paper_path = papers_dir / entry["id"]
        paper_path.mkdir(parents=True, exist_ok=True)
        (paper_path / "PAPER_KERNEL.md").write_text(paper_markdown(entry), encoding="utf-8")
        (paper_path / "paper_kernel_manifest.json").write_text(
            json.dumps(entry, indent=2) + "\n", encoding="utf-8"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="CQECMPLX-Production repository root")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    preamble, papers = load_index(repo_root)
    registry = make_registry(repo_root, preamble, papers)
    write_outputs(repo_root, registry)
    print("wrote 32 paper kernels in 4 blocks of 8")


if __name__ == "__main__":
    main()
