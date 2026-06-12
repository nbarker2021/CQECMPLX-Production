# CQE-paper-06 - Causal Code Kernel

Block: `block-00-papers-01-08`

Role: `paper_body_work`

This paper is treated as body work under the Paper 00 operating contract.

Suite edges: `CQE-paper-05` -> `CQE-paper-06` -> `CQE-paper-07`

Block edges: `CQE-paper-05` -> `CQE-paper-06` -> `CQE-paper-07`

Central thesis: Cast every dependency between objects, proofs, tools, and papers as a typed causal edge.

## Claims

Status: `seeded`

Cast every dependency between objects, proofs, tools, and papers as a typed causal edge.

Polished claim: every production dependency must be represented as a typed causal edge with source, target, edge type, receipt, and status. Closed proof-support edges must be acyclic; open obligations remain open rather than being counted as proof closure.

Required next action: Connect this polished theorem to cqe_engine.formal and populate the full 32-paper graph from formal receipts.

## Math

Status: `source-bound`

Use the paper body axioms, lemmas, and formalism as the math intake.

Required next action: Promote every symbolic statement into a normalized claim row with assumptions and receipts.

## Formal, Normal, Closed-Form Algebra and Calculus

Status: `source-bound`

Use `production/formal-papers/CQE-paper-06/FORMAL_PAPER.md`, `01-CQE-formal/FORMAL.md`, and recovered algebra/PDF evidence.

Required next action: Split normal form, closed form, algebraic operators, calculus/window operators, and open obligations.

## By-Hand Reconstruction

Status: `source-bound`

Use 03-CQE-workbook/WORKBOOK.md plus the analog toolkit guides.

Required next action: Write the physical reconstruction steps and boundary-collision handling for the paper.

## Code Rebuild

Status: `source-bound`

Use 02-CQE-tool/TOOL.md and run.py when present.

Required next action: Bind a replayable command or mark the missing executable as an obligation.

## Installable Lib Bindings

Status: `seeded`

forgefactory.paper06_causal_code

Required next action: Resolve this binding into production/lib-forge or mark it as an adapter route.

## Tests and Receipts

Status: `seeded`

Every validation and diagnostic must support hidden-guess ablation when training mode is enabled. Paper 06 now includes `production/formal-papers/CQE-paper-06/causal_code_receipt.json`, which verifies typed edges, allowed statuses, acyclic proof support, open obligation tracking, and rejection of invalid edges.

Required next action: Add positive, negative, boundary, and wrap tests with receipts.

## Deployment Kernel

Status: `seeded`

Deployable individually as CQE-paper-06 and selectable through the master suite.

Required next action: Expose paper, block, and suite selectors with no duplicate routing logic.

## Source Binding

- `body`: `production\papers\CQE-paper-06\PAPER-BODY.md` (present)
- `source`: `production\papers\CQE-paper-06\SOURCE.md` (present)
- `formal`: `production\papers\CQE-paper-06\01-CQE-formal\FORMAL.md` (present)
- `tool`: `production\papers\CQE-paper-06\02-CQE-tool\TOOL.md` (present)
- `tool_runner`: `production\papers\CQE-paper-06\02-CQE-tool\run.py` (missing)
- `workbook`: `production\papers\CQE-paper-06\03-CQE-workbook\WORKBOOK.md` (present)
- `recovered_output`: `production\lib-forge\recovered\papers_output\CQE-paper-06.md` (present)
