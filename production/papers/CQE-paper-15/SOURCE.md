# Paper 15 - QFT/Higgs Mass-Residue Carrier

## Status

HORIZON paper. Treats mass/residue as a carrier effect requiring local transport evidence and explicit obligations. The substrate-side constructions (the `F_2` Majorana-parity / Arf-invariant gluing, the `voa_weight` conformal-weight analog) are grounded in named modules. Every mass-generation / Higgs claim is a candidate hypothesis with a heavy obligation section. As in the umbrella's Discussion, this paper applies the substrate and does not claim to extend quantum field theory.

## Abstract

In the transport contract, nothing is intrinsic until it is carried: a quantity exists for the corpus only as a *carrier effect* witnessed by a local readout and a receipt. This paper takes the candidate interpretation that *mass* — and more generally a *residue* surviving cancellation — is such a carrier effect, and demands local transport evidence plus explicit obligations before any physical reading. The substrate side is concrete. Rule 30's `GF(2)` transition `L + C + R + C·R` splits into a linear part `L+C+R` (Rule 90) and a bilinear obstruction `C·R`; that obstruction is, by definition, an `F_2` quadratic form, and `f2_majorana.py` attaches to it the Arf invariant, with the Majorana-parity `Z_2` grading of a Clifford algebra `Cl(n,0)` as its physical companion (fermion-parity superselection in spin chains / topological superconductors). The corpus's "mass" analog is the *correction residue*: the carry-firing term `C AND NOT R` that survives the skip-pad filter (PROOF Paper 16; `rule30_nth_bit.py`), and the `voa_weight` of `centroid_voa.py` provides a conformal-weight-like grading (`Z(q) = 2 q^0 + 6 q^5`: vacua at weight 0, excited states at weight 5). We read "mass = surviving residue weight" as the candidate carrier effect. The Higgs / mass-generation physics is a candidate hypothesis only; the obligation section is deliberately heavy. The contribution is a disciplined residue-as-carrier framing, not a claim about how particles acquire mass.

## Central Thesis

Treat mass/residue as a carrier effect requiring local transport evidence and explicit obligations.

## Scope Boundary

This paper claims only: (1) Rule 30's transition decomposes as `L+C+R` plus the `F_2` bilinear obstruction `C·R`, whose Arf invariant is `0` (`f2_majorana.py` verification); (2) the corpus's `voa_weight` partitions the 8 chart states into a vacuum sector (weight 0) and an excited sector (weight 5), the candidate conformal-weight analog (`centroid_voa.py`); (3) "mass/residue = surviving carrier weight" is a coherent re-reading of the correction-residue apparatus. It does NOT claim to derive particle masses, the Higgs mechanism, electroweak symmetry breaking, Yukawa couplings, or any measured mass. Every physical statement is a candidate hypothesis with a named falsifier. Treating any as proven physics is out of scope.

## Definitions

- **Carrier effect**: a quantity that exists for the corpus only when witnessed by a local readout and a receipt (Paper 00 contract); nothing is intrinsic without transport evidence.
- **Linear part / obstruction**: Rule 30 `= L XOR C XOR R XOR (C·R)` over `GF(2)`; `L+C+R` is the linear (Rule 90) part, `C·R` the bilinear obstruction (`f2_majorana.py` background).
- **`F_2` quadratic form / Arf invariant**: `Q(v)=v^T A v` over `F_2` with bilinear `B(v,w)=Q(v+w)+Q(v)+Q(w)`; two non-degenerate forms with the same `B` are isometric iff their Arf invariants agree (Arf 1941; `f2_majorana.py`).
- **Majorana-parity grading**: the `Z_2` grading of `Cl(n,0)` by the parity of Majorana monomials; physically fermion-parity superselection (`f2_majorana.py` background).
- **Correction residue (mass analog)**: the carry-firing term `C AND NOT R` that survives the skip-pad filter and propagates to the final bit (PROOF Paper 16 Sections III, VI; `rule30_nth_bit.py` correction firing).
- **VOA weight (conformal-weight analog)**: `voa_weight(s) = sum of 3-conjugate wrap steps`; `0` for the two true vacua, `5` for the six excited states; seed partition `Z(q)=2q^0+6q^5` (`centroid_voa.py`).
- **Mass (physical, OBLIGATION)**: the QFT/Higgs sense; here a candidate interpretation only.

## Axioms

Axiom 15.1 - Locality: a residue must be witnessed by a local `(L,C,R)` readout before any mass interpretation (Axiom 00.1).

Axiom 15.2 - Receipt Preservation: every residue logs the cancellation it survived, its weight, and its remaining obligation (Axiom 00.2).

Axiom 15.3 - Boundary Positivity: a residue that survives cancellation is data (a carrier effect), not noise to discard (Axiom 00.3).

Axiom 15.4 - Analog Equivalence: the residue weight has a workbook analogue (a token whose color survives a fold-cancellation).

## Lemmas

Lemma 15.1 - The obstruction is an `F_2` quadratic form with Arf invariant 0. Rule 30's bilinear obstruction `C·R` is an `F_2` quadratic form; `f2_majorana.py` computes its Arf invariant as `0`, and two windows glue losslessly iff their Arf invariants match. Basis: Arf's theorem (1941), `F2Quadratic` and the module's verification.

Lemma 15.2 - Residue carries a graded weight. `voa_weight` partitions the 8 chart states into 2 vacua (weight 0) and 6 excited states (weight 5), with seed partition `Z(q)=2q^0+6q^5` (`verify_voa_sector_decomposition`, `centroid_voa.py`). The weight is a finite chart identity; the module's own conclusion states any VOA/Moonshine identification requires an additional transport theorem.

Lemma 15.3 - The mass-analog residue is the surviving carry. Of the carry-firing positions (`C AND NOT R`), approximately 90% are skip pads (cancel, invisible globally) and ~10% propagate to the final bit (PROOF Paper 16 Section VI). The propagating residue is the candidate "mass": the part that survives cancellation and changes the answer. Its parity is governed by the McKay-Thompson series (PROOF Paper 16; OPEN).

## Formalism / Calculus Sketch

The residue-as-carrier view reads a local route, separates linear from obstruction, and weighs what survives:

```text
carrier(route):
  split: Rule30 = (L+C+R)  XOR  (C·R)           [linear ; obstruction]
  obstruction C·R -> F_2 quadratic form Q        [Lemma 15.1]
    Arf(Q) = 0 ; windows glue iff Arf matches     [f2_majorana]
  carry-firing positions (C AND NOT R):
     ~90% skip-pad  -> cancel (no carrier)         [Lemma 15.3]
     ~10% propagate -> surviving residue           [candidate "mass"]
  weigh survivor: voa_weight(s) in {0 (vacuum), 5 (excited)}  [Lemma 15.2]
  emit receipt(route, residue, weight)
---- physics layer (OBLIGATION, off-shell, HEAVY) ----
candidate: surviving residue weight  <->  particle mass
candidate: vacuum sector (weight 0)  <->  massless / vacuum
candidate: Majorana Z_2 grading      <->  fermion-parity / Higgs sector
NONE derived; falsifiers below.
```

The intended reading: mass is not stored in the bit; it is the *weight of the residue that survives cancellation* as a carrier effect, witnessed locally and graded by `voa_weight`. Tool binding:

```text
cqe_engine  (f2_majorana: F2Quadratic, Arf invariant, Majorana parity;
             centroid_voa: voa_weight, Z(q)=2q^0+6q^5, TRUE_VACUA;
             rule30_nth_bit: correction firing, skip-pad survival)
```

## Proof Tree

```text
claim (mass/residue := surviving carrier effect, with obligations)
-> split Rule 30 = linear (L+C+R) XOR obstruction (C·R)
-> Lemma 15.1: obstruction is F_2 quadratic, Arf = 0, gluing rule
-> Lemma 15.3: ~10% of carries survive skip-pad filter (the residue)
-> Lemma 15.2: voa_weight grades survivor (0 vacuum / 5 excited)
-> mass := surviving residue weight (candidate carrier effect)
-> physical mass / Higgs / EWSB => OBLIGATION (heavy) + falsifiers
-> worked example (Rule 30 obstruction Arf + VOA weights)
-> workbook analogue (color surviving a fold-cancellation)
-> receipt + obligation split
```

## Practical Solved Example

**Domain:** Rule 30's bilinear obstruction `C·R` and the 8-state `voa_weight` partition, read as a residue carrier.

**Procedure:** build the `F_2` quadratic form for `C·R` via `f2_majorana.F2Quadratic`; compute its Arf invariant; compute `voa_weight(s)` for all 8 chart states via `centroid_voa`; read the surviving correction fraction from the carry/skip-pad apparatus.

**Solved Output:** the obstruction's Arf invariant is `0` (Lemma 15.1; `f2_majorana.py` verification), so windows glue losslessly along matching boundaries. The `voa_weight` partition is exactly `2` vacua at weight `0` (`(0,0,0)`, `(1,1,1)`) and `6` excited states at weight `5`, seed partition `Z(q)=2q^0+6q^5` (`verify_voa_sector_decomposition`). The surviving-carry fraction is ~10% (Lemma 15.3). The example is solved at the substrate layer: the residue, its gluing rule, and its weight grading reproduce from the formal split, the `cqe_engine` modules, and the workbook fold-cancellation sheet. The physical reading (this surviving weight "is" a particle mass) is NOT solved — it is the heavy obligation below.

## Tool Binding

- Module: `cqe_engine` (`f2_majorana`, `centroid_voa`, `rule30_nth_bit`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv` (the Higgs/mass obligations live here, marked `candidate`/`open`).
- Minimum test: confirm `f2_majorana` reports Arf invariant `0` for `C·R` and the Arf-matching gluing rule; confirm `verify_voa_sector_decomposition` returns `Z(q)=2q^0+6q^5` with 2 vacua and 6 weight-5 states; confirm the obligation ledger contains the mass/Higgs rows marked NOT proven.

## Analog Workbook Sheet

- Start with grey loose substrate; lay the local `(L,C,R)` tokens.
- Fold the strip to cancel the linear (Rule 90) part; what remains visible after the fold is the obstruction residue.
- Color the residue token by its `voa_weight`: grey (weight 0, vacuum) or a marked color (weight 5, excited / carrier).
- White follow-up = a residue whose Arf matches its neighbor (glues, carries cleanly); black follow-up = the surviving residue weight AND every physical (mass/Higgs) claim — both bound as obligation cards.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Arf1941] C. Arf, Untersuchungen ueber quadratische Formen in Koerpern der Charakteristik 2. Use: the Arf invariant of the `F_2` obstruction.
- [JordanVonNeumannWigner1934] Jordan, von Neumann, Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: the algebraic substrate the weight grading sits in.
- [ConwayNorton1979] Conway, Norton, Monstrous Moonshine, Bull. LMS 11, 308-339. Use: the McKay-Thompson series governing residue survival (OPEN target).
- [Higgs1964] P. W. Higgs, Broken symmetries and the masses of gauge bosons (BACKGROUND ONLY). Use: the physical mass-generation notion the carrier analog gestures at; NOT derived.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 and the `GF(2)` transition split.

## Open Obligations

- "Mass = surviving residue weight" is a candidate carrier interpretation. Falsifier: a massive physical state mapping to weight-0 vacuum, or a weight-5 residue with no physical mass, would break the analogy. This identification is OPEN.
- No derivation of the Higgs mechanism, electroweak symmetry breaking, Yukawa couplings, or any numerical mass is offered; all are OPEN and may be false. This is the heavy obligation: the substrate provides a grading, not a mass-generation theorem.
- The Majorana-parity `Z_2` grading is the discrete companion to fermion-parity superselection (`f2_majorana.py`); identifying it with a physical fermion/Higgs sector is OPEN.
- The residue-survival parity is governed by the McKay-Thompson series (PROOF Paper 16); the closed-form survival map is OPEN (`IDENTITY_PAPER` 8.2). `centroid_voa.py` itself states any VOA/Moonshine identification needs an additional transport theorem.
- This paper is HORIZON: it asserts no physical result.

## Back-Propagation Targets

- Paper 00 receives the carrier-effect reading (nothing intrinsic without transport evidence).
- Paper 05 (Monster / VOA) receives the `voa_weight` conformal-weight-analog framing.
- Paper 16 receives the surviving-correction-residue identification.
- Paper 14 (horizon) shares the obligation discipline.
- The analog workbook manual receives the fold-cancellation residue-color rule.
