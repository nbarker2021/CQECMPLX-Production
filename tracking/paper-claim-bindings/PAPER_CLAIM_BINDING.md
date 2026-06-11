# Paper Claim Binding

Created: 2026-06-11

This is the first binding scaffold for paper-bound claims across the local
Production, AirLock, and Kernel roots.

## Roots

| Root | Role |
|---|---|
| `D:\CQE_CMPLX\CQECMPLX-Production` | main local paper/proof body |
| `D:\CQE_CMPLX\CMPLX-Kernel\kernel\lib-forge` | kernel copy of lib-forge paper and summary material |
| `D:\CQE_CMPLX\CQECMPLX-AirLock` | lineage source for CQE engine, cqe-production, and ForgeFactory |

## First Binding Families

| Family | Production Evidence | Kernel Evidence | AirLock Evidence | Action |
|---|---|---|---|---|
| `CQE-paper-00..32` | `papers/CQE-paper-*` and `PDF_MASTER` | `lib-forge/papers_output/CQE-paper-*` | `cqe-production-v0.1/papers` for paper 00 lineage | bind text-first |
| `Paper 00 axioms/lemmas` | `lib-forge/cqe-paper-00__*` | `kernel/lib-forge/cqe-paper-00__*` | `cqe-production-v0.1/papers/01-CQE-formal` | compare variants |
| `Folded Strand master paper` | `lib-forge/MASTER_PAPER_Folded_Strand.md` | `kernel/lib-forge/MASTER_PAPER_Folded_Strand.md` | not yet bound | compare hashes later |
| `Final formal paper` | `lib-forge/FINAL_FORMAL_PAPER.md` | `kernel/lib-forge/FINAL_FORMAL_PAPER.md` | not yet bound | compare hashes later |
| `MetaMaterial Designer paper` | `lib-forge/meta_material_system/META_MATERIAL_DESIGNER_PAPER.md` | `kernel/lib-forge/meta_material_system/META_MATERIAL_DESIGNER_PAPER.md` | not yet bound | route through MetaMaterial package |
| `ForgeFactory paper tooling` | not primary | not primary | `forgefactory-v0.3-lineage-read/.../PAPER_TOOLING_PLAN_v0_3.md` | bind to AirLock lineage |

## Rules

- This scaffold binds claims to evidence paths; it does not certify the claims.
- Text and receipt material come before PDFs and generated kits.
- Superseded PDFs remain lineage-only until explicitly cited.
- AirLock material is lineage/review evidence, not a raw promotion source.

Machine-readable binding:

```text
tracking/paper-claim-bindings/PAPER_CLAIM_BINDING.json
```
