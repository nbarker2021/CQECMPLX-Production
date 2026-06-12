# Paper 05 - Oloid Path Carrier

## Status

Foundational paper. Establishes the oloid as a curved/rolling transport carrier that preserves continuity without straight-line motion. Proof-facing.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

We establish the oloid as the corpus's curved transport carrier and show that transport need not be straight-line to preserve continuity. The oloid (Bernoulli, Schatz) is the convex hull of two perpendicular equal-radius circles whose centers are separated by one radius; it is the unique smooth convex body that rolls on a plane while developing its entire surface, with a natural 4-period contact structure. As a binary-tape carrier, the oloid holds both members of every antipodal chart pair simultaneously: at each rolling step one circle is in contact (the current sheet) and the other is perpendicular (the antipodal sheet), so the implicit spin partner of each tape bit is carried geometrically without ever being recorded separately. We give the algebraic rolling state `(sheet, phase, parity)` and its octonion-grounded form (rolls as right-multiplication by `e_4`/`e_5`, where `e_4^2 = -1` gives the 180-degree gauge inversion and `e_4^4 = +1` gives the 4-period). We register the Cayley-Dickson oloid normal form: an enumerated `N` resolves with its antipode `-N`, the generative is indexed by `N+1` doublings, and the network grows as `1 + 8 + 8 + 1`. We give the dual-path oloid, where three head|tail dyads (podal, antipodal, shared contact-edge) carry the same `S_3 = W(SU(3))` action that Paper 03 proves on the trace-2 idempotents. The carrier is scale-invariant: the `N | -N` dyad has a midpoint, and the rolling motion is curved, continuous, and reversible — straightness is not required for continuity of transport.

## Central Thesis

Use curved/rolling carriers to show that transport need not be straight-line to preserve continuity: the oloid carries both sheets of every antipodal pair on one surface, so a bit and its spin partner travel together along a curved, continuous, 4-period rolling path.

## Scope Boundary

This paper claims the oloid rolling-state algebra, the octonion grounding of the 4-period, the Cayley-Dickson normal form (`N | -N`, `N+1` doubling, `1+8+8+1`), and the dual-path `S_3` carrier. The Cayley-Dickson normal form is explicitly a normal-form generator and does **not** by itself predict a Rule 30 center bit; the prediction-only dyad readout achieves only chance match rate and the read-then-verify flow is the actual solver. The escape from the local quaternion-subalgebra trap requires the global `E_6 -> E_7 -> E_8` lift, which is open. Excess interpretation is logged as obligation.

## Definitions

- **Oloid**: the convex hull of two perpendicular equal-radius circles with centers one radius apart; the unique smooth convex body that develops its whole surface by rolling, with a 4-period contact structure (`oloid_rolling.py`, module docstring).
- **Rolling state**: `(sheet, phase, parity)` with `sheet in {0,1}` (which circle contacts the plane), `phase in {0,1,2,3}` (quarter-rotation), `parity in {0,1}` (cumulative `F_2` Arf sign); one step is `((sheet+1) mod 2, (phase+1) mod 4, parity XOR bit)` (`oloid_rolling.py :: OloidState`).
- **Head|tail dyad**: the visible tape bit (head) and the perpendicular circle's orientation (tail), carried together by one physical bit.
- **Octonionic roll**: right-multiplication by `e_4` (bit 0) or `e_5` (bit 1); `e_4^2 = -1` (180-degree gauge inversion), `e_4^4 = +1` (4-period) (`oloid_octonionic.py :: GENERATOR_BIT0, GENERATOR_BIT1`).
- **Cayley-Dickson oloid normal form**: the record with `antipode = -N`, `cayley_dickson_doubling_order = N+1`, `podal_pair = (N, -N)`, and the repeating `(1, 8, 8, 1)` sheet weights (`cayley_dickson_oloid.py :: CayleyDicksonOloidNormalForm`, `CAYLEY_DICKSON_SHEET_PATTERN`).
- **Dual-path oloid**: three parallel rolling states (podal, antipodal, shared contact-edge); the `S_3` action on the three dyads equals `W(SU(3))` on the trace-2 idempotents (`oloid_dual_path.py :: DualPathOloid`).
- **Quad-oloid trap**: the empirical fact that the four-oloid `D_4` ring stays inside a quaternion subalgebra orbit (~4 joint states across all length-8 inputs); escaping requires the `E`-tower lift (`quad_oloid.py`, module docstring).

## Axioms

Axiom 05.1 - Locality: the rolling state at depth `t` is read from the carrier's current `(sheet, phase, parity)`; the tape bit at `t` is which sheet is in contact.

Axiom 05.2 - Receipt Preservation: each rolling step logs the sheet, phase, and parity transition; the antipodal companion is recoverable from the rolling-chart history without separate recording.

Axiom 05.3 - Boundary Positivity: an enumerated `N` and its antipode `-N` are a single dyad with a midpoint; neither pole is a failure, and the curved path between them is the carrier.

Axiom 05.4 - Analog Exposure Equivalence: the oloid has a physical workbook analogue (a rolling two-circle body whose contact sheet is the tape bit and whose perpendicular circle is the spin partner).

## Lemmas

Lemma 05.1 - Continuity without straightness: the oloid develops its entire surface by rolling along a continuous meandering contact curve with reflective symmetry; the carrier transports a bit and its spin partner continuously without any straight-line segment. (`oloid_rolling.py`, module docstring; the 4-period `(sheet, phase)` structure.)

Lemma 05.2 - Octonionic 4-period: rolling as right-multiplication by `e_4` realizes the 4-period exactly — `e_4^2 = -1` (180-degree gauge inversion) and `e_4^4 = +1` (identity) — and the dominant-component orient bit carries path-history information beyond bit parity, because octonion multiplication is non-associative. (`oloid_octonionic.py :: OctonionicOloidState`, `orient_bit`.)

Lemma 05.3 - Scale-invariant antipodal normal form: for every enumerated `N`, the Cayley-Dickson oloid normal form satisfies `antipode = -N`, `doubling_order = N+1`, and repeating sheet weights `(1, 8, 8, 1)`; the dual-path `S_3` action on the three dyads returns to the original after exactly three involutions (cyclic order 3). (`cayley_dickson_oloid.py :: verify_cayley_dickson_oloid_normal_form`; `oloid_dual_path.py :: verify_dual_path_oloid`, triple-involution checks.)

## Formalism / Calculus Sketch

The rolling carrier and its octonionic grounding:

```text
OloidState step:   (sheet, phase, parity)
                -> ((sheet+1) mod 2, (phase+1) mod 4, parity XOR bit)
                joint (sheet, phase) period = 8 ; parity = F_2 Arf sign

Octonionic roll:   q' = q * (e_4 if bit==0 else e_5)
                   e_4^2 = -1   (180-deg gauge inversion)
                   e_4^4 = +1   (4-period)
                   orient_bit = parity(argmax_i |q.components[i]|)  (non-trivial)

Cayley-Dickson normal form for N:
   antipode = -N ; doubling_order = N+1 ; podal_pair = (N, -N)
   network weights repeat (1, 8, 8, 1) ; total per cycle = 18

Dual-path carrier: three dyads {podal, antipodal, shared}
   S_3 action = W(SU(3)) on the trace-2 idempotents (Paper 03, T4)
   involution^3 = identity (cyclic order 3)
```

The four-oloid `D_4` ring is locally trapped in a quaternion subalgebra (~4 joint states); breaking out is the global `F_4 -> E_6 -> E_7 -> E_8` lift (open). Tool binding:

```text
cqe_engine  (oloid carrier: cayley_dickson_oloid, oloid_rolling,
             oloid_octonionic, oloid_model_selection, quad_oloid,
             oloid_dual_path)
```

## Proof Tree

```text
claim (curved rolling carrier preserves continuity, no straight line)
-> oloid = two perpendicular circles, develops whole surface rolling  (Lemma 05.1)
-> rolling state (sheet, phase, parity); bit = contact sheet
-> octonionic roll realizes 4-period exactly (e_4^2=-1, e_4^4=+1)      (Lemma 05.2)
   |- non-trivial orient bit from non-associativity
-> Cayley-Dickson normal form: N|-N dyad, N+1 doubling, 1+8+8+1        (Lemma 05.3)
-> dual-path carrier: 3 dyads with S_3 = W(SU(3)) action               (Lemma 05.3)
   |- involution^3 = identity
-> worked example (verify normal form + dual-path involution)
-> supplemental workbook analogue (rolling two-circle body)
-> receipt (sheet/phase/parity transitions logged)
-> proof result / audit residue split (E-tower escape is open)
```

## Practical Solved Example

**Domain:** the Cayley-Dickson oloid normal form and the dual-path carrier over enumerated depths.

**Procedure:** run `verify_cayley_dickson_oloid_normal_form(max_n=64, energy_terms=16)` to confirm the antipode, doubling order, and repeating `(1,8,8,1)` weights for every `N` in `0..64`; run `verify_dual_path_oloid()` to confirm the initial sheet configuration, the cyclic-order-3 involution, and the dyad-addressing arithmetic.

**Solved Output:** the normal-form verifier returns `status: pass` with `pattern: (1, 8, 8, 1)` and zero errors across `N = 0..64`; each generated form carries `antipode = -N`, `cayley_dickson_doubling_order = N+1`, and the honesty tag declaring it a normal-form generator that does not by itself prove nth-bit extraction. The dual-path verifier returns `status: pass`: after three involutions the three dyads return to their original roles (`triple_involution_*_matches: true`, level 3), and the dyad index advances cyclically by `(N + level) mod 3`. The example is solved because the antipodal normal form and the cyclic `S_3` carrier reproduce identically from the formal definitions, the `cqe_engine` verifiers, and the analog rolling body. Note: the prediction-only dyad readout achieves only chance match rate; the correct bit comes from the read-then-verify flow, with the oloid supplying the antipodal companion and orient bit.

## Tool Binding

- Module: `cqe_engine` (re-exporting `cayley_dickson_oloid`, `oloid_rolling`, `oloid_octonionic`, `oloid_dual_path`, `quad_oloid`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: `verify_cayley_dickson_oloid_normal_form()` returns `pass` with weights `(1,8,8,1)` and `antipode = -N`; `verify_dual_path_oloid()` returns `pass` with `involution^3 = identity` and correct cyclic dyad addressing.

## Analog Workbook Sheet

- Start with grey loose substrate; build or sketch a rolling two-circle body (the oloid).
- Each rolling step turns the body a quarter-period; the circle touching the plane is the tape bit (the head), the perpendicular circle is its spin partner (the tail).
- Mark the `N` token and its antipode `-N` token on opposite poles; the midpoint of the dyad is the carrier's balance point.
- White follow-up = the carrier rolled continuously through the depth and returned its dyad after three involutions; black follow-up = any attempt to read the bit from depth alone (prediction-only), kept as data showing why the read-then-verify flow is needed.
- Bind the rolling-body sheet into the matching color notebook.

## IRL Citation Anchors

- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: octonion generators `e_4`/`e_5`, Cayley-Dickson doubling, non-associativity giving the non-trivial orient bit.
- [JordanVonNeumannWigner1934] P. Jordan, J. von Neumann, E. Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: the trace-2 idempotents the dual-path `S_3` action permutes.
- [MechanicalMetamaterials] Bertoldi et al., Flexible mechanical metamaterials. URL: https://www.nature.com/articles/natrevmats201666 Use: geometry-derived mechanical response as analogue of the rolling carrier.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: the Rule 30 tape the carrier transports.

## Open Obligations

- The Cayley-Dickson oloid normal form is a normal-form generator only; it does not by itself prove Rule 30 nth-bit extraction (`cayley_dickson_oloid.py`, honesty field). Promotion to a depth-only carrier readout is an obligation.
- The four-oloid `D_4` ring is empirically trapped in a quaternion subalgebra (~4 joint states across length-8 inputs); escaping the trap requires the global `F_4 -> E_6 -> E_7 -> E_8` lift (obligation O2'' / T_F2_BRIDGE extension; `quad_oloid.py` docstring).
- The per-dyad head sequence at depth `N` in `O(1)` (the dual-path McKay-Thompson primitive) is the open question stated in `oloid_dual_path.py`.
- Replace citation anchors with final bibliography entries during peer-review preparation.

## Back-Propagation Targets

- Paper 03 (D4/J3 Triality) supplies the `S_3 = W(SU(3))` action that the three rolling dyads carry.
- Paper 04 (Boundary Repair) receives the dual-path selection (podal / antipodal / shared contact edge) as the routing target for a crossing arc.
- Paper 06 (Causal Code) receives the rolling-step transition as a `transports` edge with the sheet/phase/parity receipt.
- Paper 00 receives the `N | -N` antipodal-dyad term as a Boundary Positivity refinement (no single pole is a failure).
