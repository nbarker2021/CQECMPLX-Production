# Block 01 Dyad Brief - Papers 1 and 8

Source: Dyad Agent A, read-only synthesis. No files edited by agent.

## Paper 1

Final scientific focus:

Paper 1 is the minimal carrier theorem. The integer paper should prove that
`(L,C,R)` is the smallest ordered local carrier preserving one
observer-selected center and two distinguishable boundary addresses. It should
also prove the binary inventory facts: eight states, shell counts `1,3,3,1`,
left-right reversal `rho(L,C,R) = (R,C,L)`, center preservation, involution,
four fixed states, two reversal pairs, and the correction that opposition is
address-based rather than value-based.

Proof/evidence files:

```text
Papers/Source/CQE-paper-01.md
production/formal-papers/CQE-paper-01/FORMAL_PAPER.md
production/formal-papers/CQE-paper-01/verify_lcr_carrier.py
production/formal-papers/CQE-paper-01/lcr_carrier_receipt.json
production/papers/CQE-paper-01/SOURCE.md
production/papers/CQE-paper-01/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-01/02-CQE-tool/TOOL.md
production/papers/CQE-paper-01/02-CQE-tool/run.py
production/papers/CQE-paper-01/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-01/PAPER_KERNEL.md
```

Verifier/receipt status:

`verify_lcr_carrier.py` passes. Receipt confirms:

```text
8 states
center preserved under reversal
reversal is involution
shell multiplicities 1,3,3,1
fixed orbit count 4
paired orbit count 2
value-inequality overclaim rejected by (1,0,1)
minimal address count 3
```

Integer paper vs supplements:

- Integer Paper 1: minimal carrier theorem, finite binary inventory, reversal
  theorem, shell theorem, falsifier for value-inequality, exact receipt
  results.
- Paper 1.25: verifier, analog three-cell strip, hidden-guess diagnostic
  prompts.
- Paper 1.50: later papers must state center, boundary addresses, transform,
  imported receipt, and proof status.
- Paper 1.75: precondition export: what Paper 2+ may import from LCR and what
  must remain visible when lifted.

Important rewrite caution:

Older Paper 1 source claims a fuller single-tape SU(2) doublet and Rule
30/J3(O) bridge. The top-level rewrite should bound this: Paper 1 proves the
finite carrier facts and exports the `shell=2` doublet interface for later
papers to complete.

## Paper 8

Final scientific focus:

Paper 8 closes the first block by proving the local lattice closure template:

```text
1 -> 3 -> 7 -> 8 -> 24
with powered terminal 72 = 8 x 9
```

The integer paper should prove local combinatorial closure only: Fano/Hamming
at 7, extended Hamming/E8 seed at 8, Golay ingredients and `24 = 3 x 8`,
powered `72`, sheet bound `K=9`, and Gamma72 transport boundary. It should not
claim rootless Leech landing, Gamma72 polarization, or uniqueness of all
closure chains unless later explicit verifiers are supplied.

Proof/evidence files:

```text
production/formal-papers/CQE-paper-08/FORMAL_PAPER.md
production/formal-papers/CQE-paper-08/verify_lattice_closure_template.py
production/formal-papers/CQE-paper-08/lattice_closure_template_receipt.json
production/papers/CQE-paper-08/SOURCE.md
production/papers/CQE-paper-08/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-08/02-CQE-tool/TOOL.md
production/papers/CQE-paper-08/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-08/PAPER_KERNEL.md
production/packages/cqecmplx-forge/src/lattice_forge/lattice_codes.py
production/packages/cqecmplx-forge/src/lattice_forge/nebe_gamma72.py
```

Verifier/receipt status:

`verify_lattice_closure_template.py` passes. Receipt confirms:

```text
code chain passes
Fano/Hamming identity passes
extended Hamming/E8 seed passes
Golay ingredient passes without Leech overclaim
powered 72 = 8 x 9 sheet bound passes
Gamma72 three-sheet transport passes without landing overclaim
Leech landing overclaim rejected
Gamma72 landing overclaim rejected
K_max = 9
nebe_dim = 72
extremal min norm = 8
gamma72_landing_proved = false
```

Integer paper vs supplements:

- Integer Paper 8: proof of local lattice closure template, exact verifier
  facts, theorem boundary, falsifiers.
- Paper 8.25: code-chain verifier, `lattice_forge` functions, expected receipt
  fields.
- Paper 8.50: what may be imported as proved versus what remains
  registered/open.
- Paper 8.75: exports `K=9`, `72=8x9`, `24=3x8`, and the local closure
  scaffold into Papers 9+.

Important rewrite caution:

`production/papers/CQE-paper-08/02-CQE-tool/TOOL.md` says the tool discharges
every obligation, but the formal receipt rejects that. Rewrite should follow
the receipt: the tool proves local closure facts and preserves global landings
as obligations.

## Dyad Cross-Link

The dyad relation is carrier to closure:

```text
Paper 1: local carrier
(L,C,R), 8 binary states, shell grading, center-preserving reversal

Paper 8: closure scaffold
1 -> 3 -> 7 -> 8 -> 24 -> 72
```

Formal bridge:

- Paper 1 establishes the 3-address carrier and 8-state binary chart.
- Paper 8 uses `8` as the D4/E8 chart rung: extended Hamming `(8,4,4)` and E8
  seed.
- Paper 8 uses `24 = 3 x 8`, which should be written as three copies of the
  Paper-1-style local chart lifted into Golay/Leech-facing carrier geometry,
  but only as local carrier geometry, not completed Leech landing.
- Paper 8 closes the block edge back to Paper 1: `CQE-paper-08 -> CQE-paper-01`.

Actionable rewrite direction:

Paper 1 should stay small and exact. Paper 8 should explicitly say: the LCR
carrier is the local object being lifted; lattice closure is the first
block-level scaffold showing how that carrier can be preserved through
higher-dimensional code forms.
