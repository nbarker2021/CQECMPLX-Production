# CQECMPLX-Production White-Room Manifest

## Identity (lineage-disconnected)

- **Substrate:** CQE — *Cartan Quadratic Equivalence* (math, axioms, formalism, papers, engine).
- **Products:** CMPLX-1T — *Complexity*, the "1T" identity (compressed complex + small adapter layer).
- **Engine room:** `lib-forge/` — the heart, called at live time by every CQE tool and every CMPLX-1T product.

## Source-of-truth

- The 32-paper intent comes verbatim from:
  - `D:\review_staging\Papers00_30_BestForm_extracted\Papers00_30_BestForm_v0_1\PAPERS_00_30_COMBINED_BEST_FORM_v0_1.md`
- The 32-paper per-paper files are in the same extracted folder under `papers_md/`.
- Lineage source material is allowed but never authoritative:
  - `D:\CQE_CMPLX` (Kimi / Manus / Barker / R30 corpus)
  - `D:\DockerContainers` (ForgeFactory session master, MCP toolkit)
  - The unstaged ReForge workspace mounted by the toolkit

## Reassembly rule

For each of the 32 papers:

1. Capture intent verbatim from the combined MD → `CQE-paper-NN/INTENT.md`.
2. Reassemble Block A (formal), Block B (tool), Block C (workbook) under the new identity.
3. The `lib-forge/CQE-engine` is the runtime for Block B and the back-prop registry.

## Re-evaluation rule

**Only after all 32 papers are reassembled** do we re-evaluate "what is proven vs not." That re-evaluation uses the new identity, not the lineage language. Old "open obligation" language is treated as a checkpoint, not as authority.

## What goes where

- `_meta/` — this manifest, the naming law, the paper intent index, the boot log.
- `lib-forge/CQE-engine/` — the substrate engine (Ribbon, Arity, Hydrate, BackProp, Transport, Registry).
- `papers/CQE-paper-NN/` — 3 blocks per paper, one folder each.
- `cmplx-1t-tools/` — productized apps built on top of the papers.
- `proof-receipts/` — receipts from every Block B run, indexed by paper.

## Status

- 2026-06-07: skeleton created; 32 paper folders, 3 block subfolders each, naming law written, source-of-truth locked.
- Next: `CQE-paper-00` set as the template (Block A/B/C from verbatim Paper 00 of the combined doc), then replicate for all 32.
