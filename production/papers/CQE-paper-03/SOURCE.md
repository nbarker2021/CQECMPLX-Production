# Paper 03 - D4/J3 Triality

## Status

Core proof paper. Establishes the first explicit triality surface: axis/sheet labeling, rotation/reflection equivalence, and Jordan carrier behavior, anchored on the rigorous chart-to-`J_3(O)` isomorphism (T3) and the n=3 SU(3) Weyl closure (T4/T5). Proof-facing; this is the corpus's rigorous spine.

## Abstract

We make the corpus's triality structure explicit and prove it on three coupled surfaces. First, the chart map `phi(L, C, R) = diag(L, C, R)` is a structure-preserving bijection between the 8 chart states and 8 distinguished diagonal elements of the exceptional Jordan algebra `J_3(O)`: shell equals trace, the `L <-> R` reflection equals the `(1 3)` permutation, the `shell = 2` stratum equals the three trace-2 idempotents, and the readout law equals the diagonal-emission projection (Theorem T3, verified with zero mismatches across 6,272 individual checks at depth 4096). Second, the `D_4` antipodal codec partitions the 8 chart states into four axes carrying an `(axis, sheet)` label, losslessly recovering the full chart trajectory and exposing the `D_4` diagram's triality of order-2 transpositions. Third, the 3-step conditional transition on the `shell = 2` stratum closes exactly as `M_3 = (1/3)(T_(1,2) + T_(1,3) + T_(2,3))` over the rationals, with `M_3^2 = M_3` (rank-1 idempotent), identifying `n = 3` as the exact mixing time — the `S_3 = W(SU(3))` Weyl action restricted to the diagonal, which is the zero-weight space of the `F_4` fundamental representation. The three surfaces share one permutation group, `S_3`, acting as: a relabeling of axes (`D_4`), a rotation/reflection equivalence on idempotents (`J_3(O)`), and the exact Weyl mixing of the carrier (transition matrix). That shared `S_3` is the triality.

## Central Thesis

Represent axis/sheet labeling, rotation/reflection equivalence, and Jordan carrier behavior as the first explicit triality surface: one `S_3` action that simultaneously relabels the `D_4` axes, permutes the `J_3(O)` trace-2 idempotents, and supplies the exact n=3 Weyl closure of the carrier.

## Scope Boundary

This paper claims the chart-`J_3(O)` isomorphism (T3), the `D_4` lossless codec, and the exact n=3 SU(3) Weyl closure (T4/T5), each with a named executable verifier. It claims the *structural* unification of these three under one `S_3` action. It does not claim the full continuous `F_4` transport (that is bridged via the zero-weight space identification in PROOF Paper 03a and remains partly an obligation), nor the `D_4` triality automorphism group `S_3` as a full computation beyond the order-2 diagram involutions registered in `terminal_tree.py`. Excess interpretation is logged as obligation.

## Definitions

- **Chart map** `phi`: `phi(L, C, R) := diag(L, C, R)`, the identity-on-3-tuples map into the diagonal subalgebra of `J_3(O)` (PROOF Paper 02, Definition 2.1; `jordan_j3.py :: J3O.from_diagonal`).
- **`J_3(O)`**: the 27-dimensional exceptional Jordan algebra of `3x3` Hermitian octonionic matrices under `A o B := (AB + BA)/2` (`jordan_j3.py :: J3O`).
- **Diagonal idempotent** `E_ii`: `diag` with 1 at position `i`, else 0; `E_ii o E_ii = E_ii`, `E_ii o E_jj = 0` for `i != j` (`jordan_j3.py :: diagonal_idempotent`).
- **Trace-2 idempotent**: `E_ii + E_jj`; the three are `C- = E_11+E_22` `(1,1,0)`, `C0 = E_11+E_33` `(1,0,1)`, `C+ = E_22+E_33` `(0,1,1)` (`jordan_j3.py :: trace_2_idempotent`, `J3_TRACE2_*`).
- **Weyl `(1 3)` transposition**: the `L <-> R` involution `diag(a,b,c) -> diag(c,b,a)` (`jordan_j3.py :: weyl_13_transposition`).
- **`D_4` antipodal codec**: the partition of the 8 chart states into 4 antipodal axes `{0,1,2,3}` plus a binary sheet sign, losslessly equivalent to the joint chart trajectory (`chart_codec_d4.py :: ANTIPODAL_LABEL`, `SHEET_SIGN`).
- **n=3 closure matrix** `M_3`: the renormalized 3-step conditional transition on the `shell = 2` stratum (`f4_action.py :: n_step_shell2_conditional_3x3_exact`).
- **Triality surface**: the single `S_3` action realized identically as `D_4` axis relabeling, `J_3(O)` idempotent permutation, and the carrier's Weyl mixing.

## Axioms

Axiom 03.1 - Locality: every triality claim is read from a local `(L, C, R)` window, registered via `phi`, before any lift to the `F_4` / `E_8` frame.

Axiom 03.2 - Receipt Preservation: every isomorphism and closure check emits a count of mismatches and a residual; no preservation property is asserted without its verifier output.

Axiom 03.3 - Boundary Positivity: the `D_4` sheet sequence's residual structure (the "second sheet" the triadic `S_3` codec collapses away) is data carried by the codec, not discarded.

Axiom 03.4 - Analog Equivalence: the triality has a physical workbook analogue (a three-vertex token whose rotation/reflection moves are the `S_3` permutations on the trace-2 idempotents).

## Lemmas

Lemma 03.1 - `J_3(O)` axioms: the diagonal idempotents are idempotent and Jordan-orthogonal, sum to the identity; the three trace-2 idempotents have trace 2 and are idempotent; the `(1 3)` transposition fixes `C0 = E_11+E_33` and swaps `C- = E_11+E_22 <-> C+ = E_22+E_33`. (`jordan_j3.py :: verify_j3o_axioms`, all checks pass.)

Lemma 03.2 - `D_4` lossless triality labeling: the four antipodal axes are `{(0,0,0),(1,1,1)}`, `{(1,0,0),(0,1,1)}`, `{(0,1,0),(1,0,1)}`, `{(0,0,1),(1,1,0)}`; the `(axis, sheet)` encoding round-trips with zero mismatches, and the `D_4` diagram carries order-2 fork-swap and triality transpositions. (`chart_codec_d4.py :: verify_chart_codec_d4`; `terminal_tree.py :: _diagram_involutions` for the `D4` triality_transposition entries.)

Lemma 03.3 - n=3 exact closure and mixing time: `M_3 = (1/3)(T_(1,2) + T_(1,3) + T_(2,3))` over `Q`, with `S_3` group-ring coefficients `(e, (12), (13), (23), (123), (132)) = (0, 1/3, 1/3, 1/3, 0, 0)`, coefficient sum 1, residual squared 0; and `M_3^2 = M_3` exactly. The closure scale is exactly 3 (residual 0.816 at n=1, 0.370 at n=2, machine zero at n>=3). (`f4_action.py :: verify_n3_su3_closure_exact`, `search_for_su3_closure_scale`.)

## Formalism / Calculus Sketch

The three triality surfaces share the `S_3 = {e, (12), (13), (23), (123), (132)}` permutation group:

```text
surface          object acted on              S_3 action
---------------  --------------------------   -------------------------------
D_4 codec        4 antipodal axes + sheet     relabel axes; diagram triality
                                              (order-2 transpositions)
J_3(O) carrier   3 trace-2 idempotents        permute_indices(perm);
                                              (1 3) = chart Weyl L<->R
transition mtx   shell=2 conditional flow     M_3 = (1/3) sum of the three
                                              transpositions = uniform doubly
                                              stochastic = W(SU(3)) mixing
```

The bridge that makes this rigorous (PROOF Paper 03a): the diagonal subalgebra is the **zero-weight space** of the 26-dimensional `F_4` fundamental representation. The Weyl group preserves the zero-weight space, so the n=3 closure is the exact restriction of the `F_4` Weyl action to the chart, not a relabeling. Tool binding:

```text
cqe_engine  (jordan_j3: J3O, verify_j3o_axioms; chart_codec_d4:
             verify_chart_codec_d4; f4_action: verify_n3_su3_closure_exact)
```

## Proof Tree

```text
claim (one S_3 triality across D_4 / J_3(O) / carrier)
-> phi is a structure-preserving bijection                      (T3 / Lemma 03.1)
   |- shell = trace
   |- L<->R reflection = (1 3) permutation
   |- shell=2 stratum = three trace-2 idempotents
   |- readout law = diagonal emission
-> D_4 codec losslessly labels the 8 states by (axis, sheet)    (Lemma 03.2)
   |- D_4 diagram triality = order-2 transpositions
-> shell=2 carrier closes at n=3 as (1/3) sum of transpositions  (Lemma 03.3)
   |- M_3^2 = M_3  (rank-1 idempotent, exact mixing time 3)
-> zero-weight-space bridge (Paper 03a) makes transport exact
-> worked example (Rule 30 chart at depth 4096)
-> workbook analogue (three-vertex S_3 token)
-> receipt
-> proof / obligation split
```

## Practical Solved Example

**Domain:** Rule 30's canonical center-column chart, registered through all three triality surfaces.

**Procedure:** (1) run `verify_j3o_axioms()` to confirm the `J_3(O)` structure and the `(1 3)` fixed-point / swap behavior on the trace-2 idempotents; (2) run `verify_chart_codec_d4(4096)` to confirm lossless `(axis, sheet)` round-trip over the depth-4096 trajectory; (3) run `verify_n3_su3_closure_exact()` to confirm the exact rational `S_3` decomposition and `M_3^2 = M_3`.

**Solved Output:** the `J_3(O)` axioms pass (`status: pass`), with `(1 3)` fixing `E_11+E_33` and swapping `E_11+E_22 <-> E_22+E_33`. The `D_4` codec round-trips with `round_trip_mismatches: 0` at depth 4096. The n=3 decomposition returns coefficients `(0, 1/3, 1/3, 1/3, 0, 0)`, residual squared exactly `0`, and `M_3^2 = M_3` over `Q`; the closure-scale search confirms residual 0.816 (n=1), 0.370 (n=2), machine zero (n>=3). The umbrella's combined T3 verifier (`verify_chart_j3o_isomorphism(max_depth=4096)`) reports `0` mismatches across `6272` individual checks with `trace_2_all_idempotent: true`. The example is solved because the same single `S_3` action reproduces identically on all three surfaces, from the formal statements and from the three `cqe_engine` verifiers.

## Tool Binding

- Module: `cqe_engine` (re-exporting `jordan_j3`, `chart_codec_d4`, `f4_action`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: `verify_j3o_axioms()` passes; `verify_chart_codec_d4(>=128)` reports zero round-trip mismatches; `verify_n3_su3_closure_exact()` returns the exact coefficients `(0, 1/3, 1/3, 1/3, 0, 0)` with zero residual and confirms `M_3^2 = M_3`.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a triangle with three labeled vertices (the three trace-2 idempotents `C-`, `C0`, `C+`).
- Each `S_3` move is a physical rotation or reflection of the triangle; the `(1 3)` reflection fixes `C0` and swaps `C-` with `C+`.
- Tag each vertex with its `D_4` axis label and sheet sign; confirm the labeling is recoverable after any rotation (lossless triality).
- White follow-up = the carrier closed under three `S_3` steps (the uniform-mixing pivot); black follow-up = any labeling that fails to round-trip, kept as data.
- Bind the triangle sheet into the matching color notebook.

## IRL Citation Anchors

- [JordanVonNeumannWigner1934] P. Jordan, J. von Neumann, E. Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: the `J_3(O)` substrate and its idempotents.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: octonionic structure, `F_4`/`J_3(O)`, triality background.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 readout registered through `phi`.
- [Rule30] Wolfram Rule 30. URL: https://mathworld.wolfram.com/Rule30.html Use: the canonical center-column sequence used in the worked example.

## Open Obligations

- The full continuous `F_4` transport rests on the zero-weight-space identification (PROOF Paper 03a, T_BRIDGE). The discrete-algebraic identification and the n=3 Weyl closure are proven; the lift of every `F_4` theorem whose proof uses more than the verified structural facts remains an obligation.
- The `D_4` triality automorphism group is exercised here only via the order-2 diagram involutions registered in `terminal_tree.py :: _diagram_involutions`; the full order-6 outer triality as a verified computation is open.
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add a falsifier: a `shell = 2` state assignment that breaks the `(1 3)` fixed-point/swap pattern, which `verify_j3o_axioms` must reject.

## Back-Propagation Targets

- Paper 00 receives the `phi` substrate registration and the trace = shell correspondence.
- Paper 01 supplies the `shell = 2` -> trace-2 idempotent correspondence this paper lifts to the full `S_3` triality.
- Paper 05 (Oloid Path Carrier) receives the n=3 `S_3 = W(SU(3))` action as the symmetry of the three rolling dyads.
- Paper 06 (Causal Code) receives T3 and T4/T5 as `proves` nodes with their verifier function names as receipts.
