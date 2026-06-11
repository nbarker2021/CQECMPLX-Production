# Paper 26 - Z-Pinch and Shear Horizon

## Status

Horizon / high-speculation layer with heavy obligation accounting. The proof-bearing content is the carrier-residue algebra of the Oloid rolling model; every plasma-physical reading is an explicitly flagged candidate hypothesis. Strictly separated from the proven layers (Papers 00-16). Proof-facing in form, horizon in claim.

## Abstract

This paper isolates a single proof-bearing object - the Oloid rolling carrier and its octonionic grounding - and asks what, if anything, can be said about *first-shear*, *pinch*, and *friction-like generation* as analog readings of that carrier. The Oloid is the unique convex body that rolls without slipping while sweeping its entire surface, with a natural 4-period contact structure (`oloid_rolling.py`); its octonion grounding replaces the integer phase counter with right-multiplication by `e_4` (bit 0) and `e_5` (bit 1), where `e_4^2 = -1` is the 180-degree gauge inversion and `e_4^4 = +1` is the rolling period (`oloid_octonionic.py`). The carrier produces a *residue* - the cumulative Arf parity and the non-associative orient bit - that survives the visible-tape projection. We treat "shear" as the analog of the orient-bit divergence between the `e_4` and `e_5` generators, and "pinch" as the analog of a residue-grade collapse in the transport ledger (`transport_obligations.py`). We make no plasma-physics claim. The plasma reading is recorded as a candidate hypothesis carrying its own falsifier. The proven content is exactly the finite carrier algebra and its verifier; everything past that is obligation.

## Central Thesis

Speculatively examine first-shear, pinch, and friction-like generation as a later horizon paper requiring strict separation from proven layers.

## Scope Boundary

This paper claims only (i) the carrier-residue algebra established by `verify_oloid_rolling` and `verify_octonionic_oloid`, and (ii) the four-row transport-obligation ledger structure that classifies any further lift as `bounded_local`, `registered_landing_forms`, or `open`. It does NOT claim that the Oloid carrier models a physical Z-pinch, a magnetic-confinement shear layer, or any friction mechanism. Those identifications are candidate hypotheses logged in Open Obligations with falsifiers. Any reading that exceeds the carrier verifier or the ledger row is obligation, not proof. The paper is downstream of Paper 01 (the carrier minimality argument) and Paper 16 (the digit rollout) and does not feed back into the proof stack.

## Definitions

- **C**: the active center of a readout window; the LR-podal-invariant coordinate (`centroid_voa.gluon` returns `C`).
- **L/R**: the two opposed boundary directions read relative to `C`.
- **Oloid carrier state**: the tuple `(sheet, phase, parity)` with `sheet` in `{0,1}`, `phase` in `{0,1,2,3}`, `parity` in `{0,1}`, evolved by `state' = ((sheet+1) mod 2, (phase+1) mod 4, parity XOR bit)` (`oloid_rolling.OloidState`).
- **Octonionic carrier**: the carrier whose roll is right-multiplication by `e_4` (bit 0) or `e_5` (bit 1) on an actual `Octonion` (`oloid_octonionic.OctonionicOloidState`).
- **First-shear (analog)**: the orient-bit divergence between two carriers driven by the same tape but distinct generators - a path-history feature that pure parity counting misses (`orient_bit`, `dominant_basis_index`).
- **Pinch (analog)**: a residue-grade collapse - the event in which a transport row's preserved quantity drops a grade and the lift is reclassified from `bounded_local` to `open` (`transport_obligations`).
- **Carrier residue**: the part of the carrier state not recoverable from the visible head bit alone - the Arf parity and the octonion dominant-component index.
- **Transport row / Receipt / Workbook sheet / Tool binding**: as fixed in Paper 00.

## Axioms

Axiom 26.1 - Locality: every accepted claim must be readable through a local `(L, C, R)` window before it is lifted to a larger frame.

Axiom 26.2 - Receipt Preservation: no transform is accepted unless its inputs, output, and unresolved residue can be logged and replayed.

Axiom 26.3 - Boundary Positivity: failed, partial, or mismatched routes are data; they become obligations or correction surfaces, never silent deletions. For a horizon paper this axiom dominates: a physical reading that cannot be witnessed is logged, not promoted.

Axiom 26.4 - Analog Equivalence: if a claim belongs to the main corpus it must have a physical workbook analogue. The shear/pinch readings here are analog *only*; their workbook sheet records them as black-follow-up (unresolved) until a witness exists.

## Lemmas

Lemma 26.1 - Carrier residue is real and non-trivial. The octonionic orient bit is not a function of the last tape bit alone: by `verify_octonionic_oloid` the imaginary-unit products are non-associative (`(e_1 e_2) e_4 != e_1 (e_2 e_4)`), so the dominant-component index carries genuine path history. (Basis: `oloid_octonionic.verify_octonionic_oloid`, key `non_associative_imaginary_units`.)

Lemma 26.2 - The carrier period is exactly 4. Four rolls with a fixed bit return the integer carrier to its initial state, and `e_4^4 = +1` returns the octonionic carrier to identity. (Basis: `verify_oloid_rolling` keys `bit0_period_4`, `bit1_period_4`; `verify_octonionic_oloid` keys `e4_fourth_is_one`, `four_rolls_bit0_return_to_initial`.)

Lemma 26.3 - A pinch is a ledger reclassification, not a physical event. The transport ledger admits exactly five classifications `{demonstrated, bounded_local, bounded_external, registered_landing_forms, open}`; a "pinch" in this paper is precisely the transition of a row's classification toward `open` when its `preserved_quantity` can no longer be witnessed. (Basis: `transport_obligations.CLASSIFICATIONS` and the `proof_boundary` field of each row.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)`. The carrier transform `T` is the roll step. Acceptance:

```text
T(P_in) -> P_out
receipt(P_in, T, P_out, O) exists and is replayable
C_out is defined (gluon invariant: C survives the LR-podal reversal)
unresolved residue (Arf parity, orient bit) is recorded in O, not erased
```

The shear analog is the difference field between two carriers:

```text
shear(bits) := orient_bit(roll_octonion(bits, gen=e4)) XOR orient_bit(roll_octonion(bits, gen=e5))
```

This is nonzero exactly when the two generators' path histories disagree - the analog "first shear" between two confinement directions. The pinch analog is the ledger event:

```text
pinch(row) := (row.classification moves toward "open")
            iff row.preserved_quantity loses a witness
```

Tool binding:

```text
cqe_engine  (lattice_forge: oloid_rolling, oloid_octonionic, transport_obligations, centroid_voa)
```

## Proof Tree

```text
claim (carrier residue + analog shear/pinch)
-> local (L,C,R) window; C = gluon invariant
-> Oloid carrier step (sheet,phase,parity) ; period 4
-> octonionic grounding (e4^2 = -1, e4^4 = +1) ; non-associative orient bit
-> carrier residue (Arf parity, dominant index)  [PROVEN by verifiers]
-> shear analog = orient-bit divergence          [PROVEN as carrier identity]
-> pinch analog = ledger reclassification         [PROVEN as ledger structure]
-> plasma / friction physical reading             [OBLIGATION + falsifier]
-> workbook analogue (black follow-up until witnessed)
-> receipt
```

## Practical Solved Example

**Domain:** a 16-bit deterministic tape (the first 16 cells of Rule 30's center column), read as a carrier-residue and shear probe. This is non-toy: the same tape is the corpus reference sequence in Paper 00.

**Procedure:** roll the integer carrier and both octonionic carriers (`e_4`-driven and `e_5`-driven) across the 16 bits; record the landing `(sheet, phase, parity)`, the two orient bits, and the shear bit; build the four transport-obligation rows and record each row's classification and proof boundary; emit a receipt.

**Solved Output:** the example is solved because the carrier landing and the shear bit reproduce identically from (a) the formal roll recurrence, (b) `roll_chart_landing` / `roll_octonion`, and (c) the workbook flip strip. The shear bit is a genuine carrier invariant (Lemma 26.1). The plasma reading is NOT solved: it remains a black-follow-up obligation row, because no physical witness function exists. The honest output of this paper is exactly one proven carrier identity plus one open physical obligation.

## Tool Binding

- Module: `cqe_engine` re-exporting `lattice_forge.oloid_rolling`, `lattice_forge.oloid_octonionic`, `lattice_forge.transport_obligations`.
- Functions: `roll_chart_landing`, `roll_octonion`, `OctonionicOloidState.orient_bit`, `verify_oloid_rolling`, `verify_octonionic_oloid`, `transport_obligations`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: roll a 16-bit tape through both octonionic generators, confirm `verify_oloid_rolling` and `verify_octonionic_oloid` return status `pass`, and emit at least one proof row (carrier residue) and one obligation row (plasma reading).

## Analog Workbook Sheet

- Start with grey loose substrate.
- Place the `C` token at the local center; place `L` and `R` to either side.
- Lay a rolling strip with four contact arcs (the Oloid 4-period); roll it one quarter-turn per tape bit, flipping the visible sheet each step.
- Mark the Arf parity (cumulative flip count mod 2) as a colored bead.
- Mark the shear as a second thread: where the `e_4` and `e_5` beads diverge, tie a knot - this is the analog first-shear locus.
- White follow-up = a carrier residue that closes (proven). Black follow-up = the plasma/pinch reading (obligation, unresolved).
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 reference tape.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: octonion multiplication, `e_i^2 = -1`, non-associativity grounding the orient bit.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: receipts and the obligation ledger.
- [Sandia_Zpinch] Z-pinch / magnetized plasma confinement literature (placeholder anchor for the candidate physical reading). Use: the analog target ONLY; cited to mark, not to claim.

## Open Obligations

- HEAVY: the identification of the orient-bit shear with a physical plasma shear layer is a candidate hypothesis with NO witness. Falsifier: produce a physical shear observable whose sign disagrees with `shear(bits)` on a controlled tape; the tool must then reject or defer the reading.
- The "pinch = residue-grade collapse" reading is a ledger metaphor; it has no physical mass/current content. Falsifier: any plasma pinch whose onset is not expressible as a `preserved_quantity` witness loss.
- Provide a `bounded_external` witness (a real measurement) before any row leaves `open`.
- Replace the `[Sandia_Zpinch]` placeholder with a final bibliography entry.

## Back-Propagation Targets

- Paper 00 receives the term "carrier residue" and the five-classification ledger vocabulary.
- Paper 01 receives the note that the Oloid carrier is the rolling realization of the minimal `(L, C, R)` carrier.
- Paper 16 (the digit rollout) receives the orient-bit as the path-history feature on the rollout.
- The analog workbook manual receives the rolling-strip + shear-knot sheet rule.
- Paper 31 records how this horizon paper's strict proof/obligation split is itself an enacted `(L, C, R)` boundary read.
