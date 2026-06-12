# Paper 13 - Standard-Model Quark-Face Transport

## Status

Physics-application paper. Maps color-state and interaction analogs into a disciplined quark-face transport read over the `J_3(O)` / `F_4` substrate, without overclaiming physical proof. The algebraic transport (chart states to trace-2 idempotents to `S_3`/`SU(3)` Weyl action) is proof-facing; every physical identification is an explicit obligation. Builds on Papers 01, 03, 13 (PROOF set) and `IDENTITY_PAPER` Sections 3, 6.4.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

The substrate registers a sequence's local `(L, C, R)` chart state into the diagonal of `J_3(O)`, the natural 3-position Hermitian-octonion algebra whose automorphism group is `F_4` (PROOF Paper 13). On the `shell=2` stratum the three states `{(1,1,0),(1,0,1),(0,1,1)}` are exactly the three trace-2 idempotents `{E11+E22, E11+E33, E22+E33}` on which the `SU(3)` Weyl group `S_3` acts by permuting diagonal indices (`f4_action.py`). This paper reads that structure as a *quark-face transport*: the three diagonal positions are treated as the three color faces, the `shell=2` doublet carries the `SU(2)` spin-1/2 structure on a single tape (Paper 01, `T_BIJECTIVE`), and the bounded `G_2 -> F_4 -> T5A` conjugate route (`g2_f4_t5_conjugate.py`) classifies an already-enumerated bit through at most three named exceptional-group stages. We catalogue the framework's color/interaction analogs — the three trace-2 idempotents as a color triple, the side-flip `b` as a chirality (weak-parity) operation, and the umbrella's map of the CKM CP-violating phase and weak parity violation to "closed worldsheets" (`IDENTITY_PAPER` 6.4). Every one of these is an *algebraic correspondence in the substrate*, not a derivation of Standard Model physics. The physical claims are marked as obligations with falsifiers; the substrate's role, as in the umbrella's Discussion, is to apply classified mathematics to registered sequences, not to extend physics.

## Central Thesis

Map color-state and interaction analogs into a disciplined quark-face transport read, without overclaiming physical proof.

## Scope Boundary

This paper claims the algebraic facts: the `shell=2` stratum equals the three trace-2 idempotents; `S_3 = W(SU(3))` permutes them; the bounded `G_2/F_4/T5A` route is a three-stage classifier of an oracle-enumerated bit (not a depth-`N` derivation, per `g2_f4_t5_conjugate.py` module docstring and `transport_obligations.py` classification `bounded_local`). It does NOT claim that quarks, color charge, the strong/weak interactions, or the CKM matrix are derived, explained, or predicted by the substrate. All such identifications are obligations. Any reading that treats the color-face transport as a physics proof is out of scope.

## Definitions

- **Quark face**: one of the three diagonal positions of `diag(L,C,R)` in `J_3(O)`; the substrate's color-analog coordinate. There are exactly three, matching `SU(3)` fundamental dimension.
- **Color triple**: the three trace-2 idempotents `C- = E11+E22 = (1,1,0)`, `C0 = E11+E33 = (1,0,1)`, `C+ = E22+E33 = (0,1,1)` (`f4_action.py` index map).
- **Color Weyl action**: the `S_3` permutation of diagonal indices `(1,2,3)`, equal to `W(SU(3))`; the chart `L<->R` reflection is the transposition `(1 3)` (`f4_action.py`; `IDENTITY_PAPER` Theorem T3).
- **Spin doublet (single tape)**: the `shell=2` side-flip `b: (1,1,0) <-> (0,1,1)` fixing `(1,0,1)`, carrying `+spin/null/-spin` (Paper 01, `T_BIJECTIVE`).
- **Conjugate route**: the bounded `G_2 -> F_4 -> T5A` path of length `<= 3` classifying an enumerated bit, keyed by the D4 antipodal axis (`g2_f4_t5_conjugate.py`, `conjugate_triple_route`).
- **Closed worldsheet (analog)**: the umbrella's term for a sequence whose frame-inversion residual closes; CKM CP-phase and weak parity violation are mapped to such (`IDENTITY_PAPER` 6.4) — a correspondence, not a physical derivation.

## Axioms

Axiom 13.1 - Locality: a color-face read is admissible only from a local `(L,C,R)` chart state (Axiom 00.1).

Axiom 13.2 - Receipt Preservation: every transport step (idempotent assignment, Weyl permutation, conjugate-route stage) logs inputs, output, and residue (Axiom 00.2).

Axiom 13.3 - Boundary Positivity: a physical identification that the substrate cannot derive is recorded as an obligation, never asserted as proof (Axiom 00.3, sharpened for physics).

Axiom 13.4 - Analog Exposure Equivalence: the color triple has a physical workbook analogue (a three-face token with a swap operation).

## Lemmas

Lemma 13.1 - Color-triple identification. The three `shell=2` chart states map bijectively to the three trace-2 idempotents of `J_3(O)`, verified by `verify_j3o_axioms` (`jordan_j3.py`) and indexed in `f4_action.py`. Basis: Paper 03 / `IDENTITY_PAPER` Theorem T3, clause "shell=2 stratum corresponds bijectively to the three trace-2 idempotents."

Lemma 13.2 - Color Weyl closure. The `S_3` group ring decomposition of the `shell=2` 3-step transition matrix is `(1/3)(T_(12)+T_(13)+T_(23))` exactly over the rationals, rank-1 idempotent (`IDENTITY_PAPER` Theorems T4, T5; `f4_action.py` `verify_n3_su3_closure_exact`). The `SU(3)` Weyl action is therefore the substrate's color-mixing operation.

Lemma 13.3 - Bounded conjugate route. For an oracle-enumerated bit at `n`, `conjugate_triple_route` returns a path in `{[], [G2], [G2,F4], [G2,F4,T5A]}` keyed by the D4 antipodal axis of the chart state; this is a `bounded_local` classifier, not a cold-start depth-`N` readout (`g2_f4_t5_conjugate.py`; `transport_obligations.py` row `J3O_TO_G2_F4_T5A_ROUTE`).

## Formalism / Calculus Sketch

The quark-face transport composes three named maps; the SU(2)/SU(3) reading sits on the substrate, and the physics layer is held off-shell:

```text
(L,C,R)  --phi-->  diag(L,C,R) in J_3(O)            [Paper 03, T3]
shell=2  --=-->   {C-,C0,C+} trace-2 idempotents    [Lemma 13.1, f4_action]
S_3 = W(SU(3)) permutes {C-,C0,C+}                   [Lemma 13.2, T4/T5]
side-flip b: C- <-> C+, fix C0  = SU(2) doublet      [Paper 01, T_BIJECTIVE]
G2 -> F4 -> T5A bounded route classifies bit at n    [Lemma 13.3]
---- physics layer (OBLIGATION, off-shell) ----
{color charge, quark generations, CKM CP phase,
 weak parity violation}  := candidate identifications
 mapped to closed worldsheets (IDENTITY 6.4), NOT derived
```

The `SU(2)` shell=2 doublet plus the three color faces give the substrate's "doublet + color" picture: a single-tape spin-1/2 doublet (Paper 01) carried on a 3-color-face register. Tool binding:

```text
cqe_engine  (f4_action: S3_PERMUTATIONS, n=3 closure, trace-2 idempotents;
             g2_f4_t5_conjugate: conjugate_triple_route, T_5A_COEFFICIENTS;
             jordan_j3: verify_j3o_axioms; centroid_voa: gluon, swap_LR)
```

## Proof Tree

```text
claim (color-state + interaction analogs -> disciplined quark-face read)
-> phi registration to J_3(O) diagonal (T3)
-> shell=2 = three trace-2 idempotents (Lemma 13.1)
-> S_3 = W(SU(3)) color permutation, n=3 closure (Lemma 13.2)
-> single-tape SU(2) doublet via b (Paper 01)
-> bounded G2/F4/T5A route classifies enumerated bit (Lemma 13.3)
-> physical identifications (color, CKM, weak parity) => OBLIGATION
-> worked example (Rule 30 shell=2 color faces)
-> supplemental workbook analogue (three-face token + swap)
-> receipt + obligation split
```

## Practical Solved Example

**Domain:** the `shell=2` stratum of Rule 30's center-column chart, read as color faces.

**Procedure:** extract the three `shell=2` states; assign them to `{C-, C0, C+}` via the `f4_action.py` index map; apply the six `S_3` permutations (`S3_PERMUTATIONS`) and confirm the 3-step transition matrix decomposes as `(1/3)(T_12+T_13+T_23)` with residual squared exactly `0` over the rationals (`verify_n3_su3_closure_exact`); apply the side-flip `b` and confirm `C- <-> C+`, `C0` fixed.

**Solved Output:** the color triple closes under the `SU(3)` Weyl action exactly (residual `0`, rank-1 idempotent `M_3^2=M_3`; `IDENTITY_PAPER` Section 4 reports `n=1` residual `0.816`, `n=2` residual `0.370`, `n=3` machine zero). The single-tape doublet reproduces the `+spin/null/-spin` assignment of Paper 01. The example is solved at the algebraic layer: the color-face transport reproduces identically from the formal maps, the `cqe_engine` verifiers, and the workbook three-face token. The physical reading (these faces "are" quark colors) is logged as an obligation, not solved.

## Tool Binding

- Module: `cqe_engine` (`f4_action`, `g2_f4_t5_conjugate`, `jordan_j3`, `centroid_voa`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv` (the physics obligations live here).
- Minimum test: confirm `verify_j3o_axioms` passes; confirm `verify_n3_su3_closure_exact` returns residual `0`; confirm `conjugate_triple_route` returns a path of length `<= 3` keyed by the antipodal axis; confirm the obligation ledger contains at least one physics row marked `open`/`candidate`.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a token with three faces labelled `C-`, `C0`, `C+`.
- Color the two set faces of the current `shell=2` state; the cleared face is the null pivot `C0`.
- The swap operation `b` turns the token over, exchanging `C-` and `C+` (the chirality/weak-parity analog).
- White follow-up = a closed color cycle under the three `S_3` swaps; black follow-up = any physical claim (quark, CKM, weak parity) — these are bound as obligation cards, never as proof.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Tits1966] J. Tits, Algebres alternatives, algebres de Jordan et algebres de Lie exceptionnelles, Indag. Math. 28, 223-237. Use: the Magic Square / `F_4` construction.
- [Freudenthal1963] H. Freudenthal, Lie Groups in the Foundations of Geometry, Adv. Math. 1, 145-190. Use: exceptional-group geometry.
- [JordanVonNeumannWigner1934] Jordan, von Neumann, Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: `J_3(O)` and trace-2 idempotents.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: `G_2 = Aut(O)`, `F_4 = Aut(J_3(O))`, octonion/SU structure.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: the registered Rule 30 sequence.

## Open Obligations

- The identification of the three trace-2 idempotents with physical quark color charges is a candidate analog, not derived. Falsifier: a color-face assignment that breaks `S_3` closure (Lemma 13.2 would reject it). The physics-as-proof step is OPEN.
- The umbrella's mapping of the CKM CP-violating phase and weak parity violation to "closed worldsheets" (`IDENTITY_PAPER` 6.4) is an algebraic correspondence; deriving the measured CKM phase or the V-A structure from the substrate is OPEN.
- The `G_2 x F_4 -> E_8` decomposition `(G2 + F4) + (7 x 26) = 248` (PROOF Paper 13 Section 3.4) is a representation-theory fact transported, not a physical unification claim.
- Replace citation anchors with final bibliography entries.

## Back-Propagation Targets

- Paper 01 receives the color-face reading of the single-tape `SU(2)` doublet.
- Paper 03 receives the color-triple / `SU(3)` Weyl identification (`f4_action`).
- Papers 14 and 15 (horizon) receive the discipline that physical claims are obligations with falsifiers.
- The analog workbook manual receives the three-face color token rule.
- Paper 31 records how the disciplined obligation split is enacted in the corpus order.
