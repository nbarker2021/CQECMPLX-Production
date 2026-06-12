# Block 01 Dyad Brief - Papers 03 and 06

Source: Dyad Agent C, read-only synthesis. No files edited by the agent.

## Repository State

Top-level `Papers/Source/CQE-paper-03.md` and `Papers/Source/CQE-paper-06.md` are currently missing, so the rewrite pass should create them from production formal/source materials.

Verified live:

- `production/formal-papers/CQE-paper-03/verify_triality_surface.py` -> `status: pass`
- `production/formal-papers/CQE-paper-06/verify_causal_code.py` -> `status: pass`

## Paper 03 - D4/J3 Triality

Final scientific paper claim focus:

Paper 3 should prove the finite registration/triality surface:

```text
LCR state <-> D4-style axis/sheet code <-> diagonal J3 carrier
```

Use the stronger production source, but keep the claim disciplined. The safest polished theorem is that the eight binary `(L,C,R)` states admit a faithful three-language registration by:

- axis/sheet antipodal D4-style codec,
- diagonal carrier `phi(L,C,R)=diag(L,C,R)`,
- shell-as-trace preservation,
- shell-2 trace idempotent carrier,
- Paper 2 correction states preserved as coordinates `(2,0)` and `(3,1)`.

Evidence supports mentioning stronger surrounding structure:

- T3 chart-to-`J3(O)` isomorphism verified at depth 4096 with 6,272 checks and 0 mismatches.
- T4/T5 exact rational `n=3` SU(3)/S3 Weyl closure via `verify_n3_su3_closure_exact`.
- Local Kernel summary lists `T_TRIALITY` as PASS.

However, the current Paper 3 formal verifier explicitly does not prove full D4 triality or full F4/J3(O) action. Write the integer paper as a rigorous finite triality/registration paper and put broader F4/full triality lift in obligations or companion discussion unless the rewrite imports the stronger R30 theorem registry directly.

Proof/evidence files:

- `production/formal-papers/CQE-paper-03/FORMAL_PAPER.md`
- `production/formal-papers/CQE-paper-03/triality_surface_receipt.json`
- `production/formal-papers/CQE-paper-03/verify_triality_surface.py`
- `production/papers/CQE-paper-03/SOURCE.md`
- `production/papers/CQE-paper-03/01-CQE-formal/FORMAL.md`
- `production/papers/CQE-paper-03/02-CQE-tool/TOOL.md`
- `production/papers/CQE-paper-03/03-CQE-workbook/WORKBOOK.md`
- `production/paper-kernels/papers/CQE-paper-03/PAPER_KERNEL.md`
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\theorems\THEOREM_REGISTRY.md`
- `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers\SUMMARY-I-Gluon-at-Center.md`
- `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers\SUMMARY-V-32-Theorems-Registry.md`

Verifier/receipt status:

- Current receipt: pass.
- Checks passed:
  - axis/sheet bijection,
  - antipodal axis pairs,
  - trace equals shell,
  - shell-2 states are diagonal idempotents,
  - Paper 2 correction coordinates preserved,
  - strong triality left as explicit obligation.

Integer vs companions:

- Integer Paper 3: formal theorem, definitions, proof, solved example, receipt summary, falsifiers.
- `.25`: toolkit for axis/sheet codec, J3 diagonal carrier, S3/Weyl helper functions.
- `.50`: validation contract: what counts as a valid registration, what overclaims are rejected.
- `.75`: application bridge: how Paper 3 coordinates become preconditioned state for Paper 4 boundary repair and Paper 6 causal edges.

## Paper 06 - Causal Code

Final scientific paper claim focus:

Paper 6 should prove the typed causal dependency contract. It is the graph discipline of the corpus:

```text
Every dependency between papers, proofs, tools, receipts, obligations, and products must be represented as a typed edge with:
source, target, edge_type, receipt, status.
```

Main theorem:

A production proof-support graph is admissible only if all active proof edges have required fields, allowed types/statuses, replayable receipts, and no hidden proof-support cycles. Open obligations remain open and cannot be counted as closed proof.

Evidence supports stronger language around terminal composition trees, contribution registry, validator gates, transport obligations, and causal Gluon, but the integer paper should stay centered on the causal-edge theorem.

Proof/evidence files:

- `production/formal-papers/CQE-paper-06/FORMAL_PAPER.md`
- `production/formal-papers/CQE-paper-06/causal_code_receipt.json`
- `production/formal-papers/CQE-paper-06/verify_causal_code.py`
- `production/papers/CQE-paper-06/SOURCE.md`
- `production/papers/CQE-paper-06/01-CQE-formal/FORMAL.md`
- `production/papers/CQE-paper-06/02-CQE-tool/TOOL.md`
- `production/papers/CQE-paper-06/03-CQE-workbook/WORKBOOK.md`
- `production/paper-kernels/papers/CQE-paper-06/PAPER_KERNEL.md`
- `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers\SUMMARY-I-Gluon-at-Center.md`
- `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers\SUMMARY-V-32-Theorems-Registry.md`
- Claude survey note: `D:\CQE_CMPLX\Claude-Codex-Memory\Claude work\CL-Production-Survey\CL_production-formal-md-p00-p15.md`

Verifier/receipt status:

- Current receipt: pass.
- Checks passed:
  - all edges have required fields,
  - allowed type/status only,
  - closed proof-support graph is acyclic,
  - open obligations remain open,
  - missing receipt rejected,
  - unknown type rejected,
  - hidden proof cycle rejected.

Integer vs companions:

- Integer Paper 6: formal causal-edge schema theorem, proof of required fields, proof against hidden cycles, worked graph from Papers 0-6.
- `.25`: toolkit for graph/receipt tooling: terminal tree, causal index, contribution registry, validators.
- `.50`: validation contract: accepted edge types, statuses, falsifiers, hidden-cycle rejection.
- `.75`: application bridge: how previous papers' proof outputs become typed dependencies for later suite papers.

## Cross-Link: Paper 03 -> Paper 06

Use this as the dyad spine:

Paper 3 creates the first reliable multi-language registration of one local state. It proves that an `(L,C,R)` event can be carried without loss across coordinate languages: LCR, D4 axis/sheet, and diagonal J3 trace/idempotent form.

Paper 6 then generalizes the same discipline from "one state has multiple faithful registrations" to "one proof dependency has a typed, replayable causal registration."

```text
Paper 3: register states without losing structure.
Paper 6: register dependencies without losing proof responsibility.
```

Specific cross-link:

- Paper 3 output `triality_surface_receipt` becomes a Paper 6 causal edge receipt.
- Paper 6 receipt graph already includes:
  - `CQE-paper-02 -> CQE-paper-03`, `edge_type: transports`
  - `CQE-paper-03 -> CQE-paper-04`, `edge_type: constrains`
  - `CQE-paper-05 -> CQE-paper-06`, `edge_type: transports`
- Paper 3's triality/Jordan registration is the object-level template.
- Paper 6's causal code is the proof-graph template.
- Bridge phrase: "triality/Jordan registration supplies the registered object; causal code supplies the registered dependency."

Rewrite caution:

Do not let Paper 6 become only administrative metadata. Present it as a formal graph theorem: causal code is the proof-preserving dependency algebra of the suite.
