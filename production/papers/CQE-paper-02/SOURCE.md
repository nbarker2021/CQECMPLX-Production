# Paper 02 - Correction Surface

## Status

Foundational paper. Establishes the correction surface: the discipline of treating failure, mismatch, and nonlinear residue as positive correction data rather than dismissal. Proof-facing.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

We define the corpus's *correction surface*: the typed object that absorbs the difference between a sequence's actual behavior and its nearest linear approximation, and converts that difference into reusable data. The load-bearing fact is the GF(2) linearization identity `Rule_30(L, C, R) = Rule_90(L, R) XOR correction(L, C, R)`, where `correction(L, C, R) = C AND NOT R`. Rule 90 is the linear part (a single XOR with a closed-form Lucas solution); the correction term is the exact, localized nonlinear residue that distinguishes Rule 30 from its linear shadow. We show that the correction tape is not noise to be discarded but a single-bit projection of the umbrella's `D_4` antipodal chart state, firing precisely on the two chart states `{(0,1,0), (1,1,0)}`. The same residue, lifted to the relational-frame layer, is the four-class closure taxonomy `{CLASSICAL, META_OPEN, SPINOR, VACUUM}` of Paper 04 of the PROOF set: each class is a record of *which observer frame the residue fails to close in*, never a verdict that the sequence is malformed. Correction data is therefore positive: it routes, it constrains the next legal move, and it is logged, not deleted.

## Central Thesis

Treat failure, mismatch, and nonlinear residue as positive correction data rather than dismissal: the difference between a sequence and its linear shadow is an exact, typed object that carries information, routes the next step, and is preserved as a receipt.

## Scope Boundary

This paper claims the linearization identity, the localization of the correction tape onto the `D_4` codec, and the framing of the relational-closure classes as correction data. It does not claim that the correction tape collapses to a polylog orbit count (that is the open computational question in `rule90_linearization.py`), nor that the spinor class has been empirically observed (it has not; see Open Obligations). Excess interpretation is logged as obligation.

## Definitions

- **Linear shadow**: for a chart state `(L, C, R)`, the Rule 90 value `Rule_90(L, R) := L XOR R` — the part of the readout that uses no center cell and no nonlinear coupling.
- **Correction term**: `correction(L, C, R) := C AND NOT R`, equivalently `C AND (1 - R)`; the GF(2) difference `Rule_30 - Rule_90` (`rule90_linearization.py :: correction`).
- **Correction tape**: the depth-indexed sequence of correction-term values along a column of the chart.
- **Correction firing**: the event `correction = 1`, which occurs exactly on the two chart states `{(0,1,0), (1,1,0)}` (`rule90_linearization.py :: CORRECTION_FIRING_AXES_SHEETS`).
- **Cascade level**: the depth of a window in the fallback hierarchy — `0` at a Lie-conjugate rest state, `1` when a linear CA suffices, `2` when the correction (frustrated bond `C=1, R=0`) must fire (`binary_boundary_adapter.py :: cascade_level`, `emission_level`).
- **Relational closure class**: one of `{CLASSICAL, META_OPEN, SPINOR, VACUUM}`, recording at which level (direct / first frame inversion / second frame inversion) the residual squared fails to close (PROOF Paper 04, Definitions 2.16-2.17).
- **Correction surface**: the union of all correction tapes and relational closure records of a sequence, treated as a single positive-data object rather than as discarded error.

## Axioms

Axiom 02.1 - Locality: the correction term is read from a single `(L, C, R)` window; `correction(L, C, R) = C AND NOT R` depends on no wider context.

Axiom 02.2 - Receipt Preservation: every correction firing is logged with the chart state that produced it and the depth at which it fired; corrections are never silently merged into the linear shadow.

Axiom 02.3 - Boundary Positivity: a nonzero correction term, an open relational-closure class, and a crossing arc are all *data*. They constrain the next legal route; they are never grounds for rejecting the sequence.

Axiom 02.4 - Analog Exposure Equivalence: a correction firing has a physical workbook analogue (a frustrated-bond token: gluon active, write channel silent).

## Lemmas

Lemma 02.1 - Linearization identity: `Rule_30(L, C, R) = Rule_90(L, R) XOR correction(L, C, R)` for all 8 chart states. (Verified by enumeration; `rule90_linearization.py :: linearization_identity_holds`.)

Lemma 02.2 - Correction localization: the correction tape at the center column is nonzero iff the chart state is in `{(0,1,0), (1,1,0)}`, which in the `D_4` antipodal codec is exactly `(axis 2, sheet 0) OR (axis 3, sheet 1)`. (Basis: `rule90_linearization.py :: correction_from_chart`, keyed on `ANTIPODAL_LABEL` and `SHEET_SIGN` from `chart_codec_d4.py`.)

Lemma 02.3 - Linear closed form: the linear shadow Rule 90 from a single-cell seed has the closed-form Lucas solution `lucas_bit(d, x)` (1 iff `(d+x)` even and `k = (d+x)/2` is a bit-subset of `d`), computable in `O(log d)`. The nonlinearity of Rule 30 is therefore wholly concentrated in the correction tape. (`rule90_linearization.py :: lucas_bit`; the Pascal recurrence is checked by `contribution_validators.py :: lucas_recurrence_validator`.)

## Formalism / Calculus Sketch

A correction-surface state is `K = (L, C, R, lin, corr, level, class)`: the window, its linear shadow `lin = L XOR R`, the correction bit `corr = C AND NOT R`, the cascade level, and the relational closure class. The center bit at depth `N` decomposes as:

```text
Rule_30_center(N) = lucas_bit(N, 0)
                  XOR  XOR over (t < N, x in light cone) of
                         lucas_bit(N-1-t, -x) * corr(t, x)

  base term      = the linear (Rule 90) shadow, O(log N) per term
  correction sum = the localized nonlinear residue, fires only on
                   chart states {(0,1,0), (1,1,0)}
```

The relational lift re-encodes the `S_3` group-ring coefficients of the transition matrix into a new sequence (the frame-inversion operator `F` of PROOF Paper 04) and records the residual squared at three nested observer levels as `Q(S) = (r_0, r_1, r_2)`. The class is then read off:

```text
CLASSICAL  (0, 0, 0)        residue closes at every frame
META_OPEN  (0, 0, eps)      closes for two observers, opens at the meta-meta level
SPINOR     (0, eps, 0)      closes direct + meta-meta, intermediate frame open (4pi return)
VACUUM     (eps, eps, eps)  no relational definition closes at any frame
```

Tool binding:

```text
cqe_engine  (correction surface: rule90_linearization, substrate_map,
             contribution_validators; the GF(2) correction term and its
             D_4 localization)
```

## Proof Tree

```text
claim (residue is positive correction data, not error)
-> linearization identity  Rule_30 = Rule_90 XOR correction   (Lemma 02.1)
-> linear shadow has closed form (Lucas)                       (Lemma 02.3)
-> correction tape localizes onto D_4 chart states             (Lemma 02.2)
-> cascade level / emission level typing                       (binary_boundary_adapter)
-> relational closure class  {CLASSICAL, META_OPEN, SPINOR, VACUUM}
-> worked example (Rule 30 center decomposition)
-> supplemental workbook analogue (frustrated-bond token)
-> receipt (correction firing logged with state and depth)
-> proof result / audit residue split
```

## Practical Solved Example

**Domain:** Rule 30's center column reconstructed via the Rule 90 + correction decomposition.

**Procedure:** for each depth `N` in `{1, 2, 3, 5, 8, 16, 32, 64, 128, 256, 512, 1024}`, compute the base Lucas term, accumulate the localized correction sum over the light cone, and compare the reconstructed center bit against direct simulation (`rule90_linearization.py :: rule30_center_via_decomposition`, wrapped by `verify_rule90_linearization`).

**Solved Output:** the truth-table identity holds across all 8 states; the Lucas closed form matches direct Rule 90 at depth 64 across the full row; and the correction-augmented decomposition reproduces the direct Rule 30 center bit at every tested depth (`status: pass`, `decomposition_matches_at_all_depths: true`). The correction terms are not discarded — they are the exact, counted set of contributions that turn the linear shadow into Rule 30. The example is solved because the same reconstruction is reproducible from the formal identity, the `cqe_engine` verifier, and the analog frustrated-bond tally.

## Tool Binding

- Module: `cqe_engine` (re-exporting `rule90_linearization`, `substrate_map`, `contribution_validators`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: confirm `linearization_identity_holds()`; reconstruct the Rule 30 center bit at depth >= 256 via `rule30_center_via_decomposition` with zero mismatches; log each correction firing as a correction-surface receipt row.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a three-cell strip `L | C | R`.
- Color the linear shadow `L XOR R` in one color (the Rule 90 background).
- Place a distinct frustrated-bond token wherever `C = 1` and `R = 0` (the correction fires): gluon active, write channel silent.
- White follow-up = the correction closed the route (a legal next move); black follow-up = an open relational class (the residue did not close at some frame) — kept as data, never erased.
- Bind the finished sheet, including all firing tokens, into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 and Rule 90 as elementary CA.
- [Rule30] Wolfram Rule 30 / elementary cellular automata. URL: https://mathworld.wolfram.com/Rule30.html Use: the local rule whose nonlinear residue is the correction term.
- [ElementaryCA] Elementary cellular automata: 256 local binary rules. URL: https://mathworld.wolfram.com/ElementaryCellularAutomaton.html Use: Rule 90 (linear) vs Rule 30 (nonlinear) within the same rule space.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: residue / correction as channel information, not noise.

## Open Obligations

- Whether the contributing `(t, x)` correction pairs cluster into `D_4`-Weyl-octonionic orbits whose XOR-sums collapse to a polylog count of surviving orbits is the open computational question stated in `rule90_linearization.py` (Wolfram Problem 3 in this framing). It is carried as an obligation, not a proof.
- The `SPINOR` closure class `(0, eps, 0)` has not been observed in any tested sequence (systematic search to length 14 in PROOF Paper 04); its existence is structural and remains open.
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add one falsifier: a chart state outside `{(0,1,0), (1,1,0)}` that the correction tape claims fires, which the tool must reject.

## Back-Propagation Targets

- Paper 00 receives the Boundary Positivity term as the correction-surface discipline (Axiom 00.3 specialized to nonlinear residue).
- Paper 04 (Boundary Repair) receives the correction-firing record as the input typed-constraint for the next legal route.
- Paper 06 (Causal Code) receives the correction firing as a `refines`/`obligates` edge with a receipt.
- The analog workbook manual receives the frustrated-bond token rule.
