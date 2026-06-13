# Master Topic Package Blueprint

This repository should treat each final paper/topic as a master proof package,
not as a loose aggregation of drafts. The master package leads with the formal
math and proof claims. Toolkits, workbooks, analog procedures, kernels, and
receipts are supplemental validation layers that allow a reader to replay or
audit a selected claim.

## Recovered Source Rule

Historical files often mark items as open because they were open at that
checkpoint. Before any final paper repeats an "open" label, it must be
superposed with later closure material from:

- `D:\CQE_CMPLX\historical_pastworks\Kimi_Agent_Rule30InvariantProof(2).zip`
- `D:\CQE_CMPLX\historical_pastworks\CMPLX-R30-FINAL-SUBMISSION.tar.gz`
- `D:\CQE_CMPLX\historical_pastworks\CMPLX-R30-full-checkpoint-v7.tar.gz`
- `D:\CQE_CMPLX\historical_pastworks\CQECMPLX-ProofValidatedSuite.zip`
- top-level reports in `D:\CQE_CMPLX\historical_pastworks`

The paper voice should say: claim, formal structure, proof, evidence, and
current boundary. Historical obligations belong in the supplement unless they
are needed to explain a theorem's status.

## Master Package Shape

Every topic gets the same shape:

```text
MASTER_<topic>_PAPER.md
MASTER_<topic>_PAPER.pdf
MASTER_<topic>_SUPPLEMENT.md
MASTER_<topic>_SUPPLEMENT.pdf
MASTER_<topic>_EVIDENCE_INDEX.json
receipts/
tools/
paper_assets/
```

The paper is the formal presentation. The supplement is the complete audit
layer. The evidence index is the machine-readable map between claims, files,
tests, receipts, and current status.

## Required Paper Sections

1. Abstract
2. Definitions and notation
3. Claim inventory
4. Theorems and proof bodies
5. Verification summary
6. Current boundary and caveats
7. Reproduction pointers

The paper should not foreground analog or workbook language. Those are valid
only as replay mechanisms after the formal object is stated.

## Required Supplement Sections

1. Historical lineage
2. Source inventory
3. Historical open-obligation ledger
4. Later closure evidence
5. Falsified branches and discarded hypotheses
6. Receipt/test summaries
7. Kernel/lib/tool bindings
8. Analog and workbook replay guide
9. Glossary and symbol table

## Current Closure Map

| Topic | Historical state | Later evidence | Paper posture |
|---|---|---|---|
| Rule 30 emission law | Kimi theorem candidate | zero-defect verification at 4096/8192 and multi-depth 256-16384 | proven finite local law |
| At-most-3 wrap | Kimi theorem candidate | all 8 states close in 0, 2, or 3 steps | proven chart-state closure |
| `M_3` idempotency | Kimi theorem candidate | exact rational `M_3^2 = M_3` | proven algebraic identity |
| Wolfram Problems 1/2 | Kimi transport proof | final submission and proof cards | proof-facing core topic |
| O3 universality | historically open | Hamming-centroid all-256 CA result and Game of Life generalization | closed by exhaustive finite/state tests |
| O1' MT parity primitive | historically not implemented | closure report says implemented and verified for 1A/2A/3A/4A | closed as computational primitive |
| O2 VOA transport | historically not implemented | closure report says closed with caveats | closed as combinatorial transport, not full VOA algebra unless strengthened |
| O2' nth-bit extraction | partial/open in Kimi | Lucas skip, dyadic periodicity, compiled lookup, final Problem 3 claim | reconciliation required |
| Monster correction-class link | speculative | later correlation tests falsified | keep as falsified branch in supplement |
| Weyl orbit correction clustering | speculative/open | later tests not supported | keep as falsified/disproven branch |

## Proof-First Constraint

The proof-carrying paper owns the topic. Everything else is supporting
material. Analog checks, by-hand procedures, sidecar calls, Docker adapters,
and workbook sheets are included because they make the proof auditable, not
because the reader is expected to perform the whole framework manually.

## Observer Enumeration Constraint

The final suite must restore the observer term as a primary formal object:
the chosen enumeration event at step 00, the center `C`, the linked `N` and
`N|-N` accounting substrate, and the fact that later state evolution is an
effect of that initial selection plus recorded validation.

