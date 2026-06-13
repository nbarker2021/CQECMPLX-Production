# Reapplication Ledger

Working premise (operator directive, 2026-06-13): most things marked "open"
or "obligation" in the corpus were already solved somewhere in the workspace;
the resolution simply was never reapplied to the state that records the
obligation. This ledger records obligations whose existing resolution has now
been found and reapplied into the production paper-bound space.

A reapplication is not new work. It binds an already-proven module or an
already-built forge to the obligation it silently resolves, with a passing
verifier and a receipt, and records what remains genuinely open.

## Reapplied 2026-06-13

| Obligation | Source ledger | Existing resolution (was unused) | Reapplied to | Receipt | Status |
|---|---|---|---|---|---|
| O2' verifiable core: Rule 30 = Rule 90 (+) correction, Lucas closed-form, depth-N decomposition | `CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md` | `lattice_forge/rule90_linearization.py` — proven with its own passing verifier, vendored into the production substrate, bound to no paper | `formal-papers/CQE-paper-06/verify_rule90_lucas_decomposition.py` | `rule90_lucas_decomposition_receipt.json` (7/7) | core CLOSED; O(log N) McKay-Thompson collapse stays open |
| PFC-2 named computation: enumerate the 240 E8 roots from Construction A | `CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md` | `E8Forge` (promoted 2026-06-12) — exact 240-root enumeration | `formal-papers/CQE-paper-08/verify_e8_hemisphere_partition.py` | `e8_hemisphere_partition_receipt.json` (5/5) | enumeration BUILT, 240/120-pair/clean-split confirmed; the "13 half-vignettes" geometric count and the alpha=1/137 physics remain OPEN and are explicitly not claimed |

## What each reapplication confirmed

### O2' core (paper 06)

- Rule_30(L,C,R) = Rule_90(L,R) XOR (C AND NOT R) at the truth table.
- Rule 90 from a single cell = the Lucas closed-form (Pascal's triangle mod 2
  = Sierpinski gasket), an O(log d) bit-AND; re-derived independently against
  Pascal mod 2 over d = 0..39.
- The Rule 30 center bit reconstructs exactly from the Lucas-sparse light-cone
  decomposition, matching direct simulation at depths 1..1024.
- The correction fires exactly on chart states {(0,1,0),(1,1,0)}, agreeing
  with the D4 codec projection.
- Sierpinski self-similarity at power-of-two rows.

Still open (NOT reapplied, genuinely unresolved): the O(log N) collapse of the
correction sum via the McKay-Thompson coefficient-parity primitive (O1, O2).

### PFC-2 enumeration (paper 08)

- The 240-root enumeration PFC-2 names as its closing computation now exists
  (E8Forge); confirmed 240 roots, antipodal pairing into 120 pairs, and a
  clean linear-functional hemisphere split 120/120.
- The integer decomposition 120 + 13 + 4 = 137 and 240 - 137 = 103 is
  consistent arithmetic over the enumerated set.

Explicitly NOT claimed (honesty boundary): the "13 boundary half-vignettes"
count is an observer-light-cone geometric claim not fixed by root enumeration;
the identification 1/137 = the fine structure constant is a physical
hypothesis. Neither is tested or endorsed.

## Next reapplication candidates (existing resolutions to locate and bind)

- O8 cross-page commutativity / spinor double cover: check whether `F^2` frame
  inversion semantics are already verified in `centroid_voa.py` / T_BIJECTIVE
  tests and bind to the observer paper (19).
- O7 Niemeier exact glue cosets: check whether the PartsFactory / lattice_forge
  Niemeier construction already carries explicit Construction A glue codes.
- Theorem registry sweep: cross-reference `CMPLX-R30-main/PROOF/theorems/
  THEOREM_REGISTRY.md` proven theorems (T1-T8 + named) against the production
  formal-papers bindings; bind any proven-with-verifier theorem not yet
  represented.
