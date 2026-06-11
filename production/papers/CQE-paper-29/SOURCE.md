# Paper 29 - Monster/Universal Energy-Bound Hypotheses

## Status

Horizon / highest-speculation layer. This paper carries the heaviest obligation section in the corpus. The only proof-bearing content is (i) the exact arithmetic identity `196883 = 47 x 59 x 71` and McKay's `196884 = 1 + 196883`, and (ii) the finite VOA-weight partition function `Z(q) = 2q^0 + 6q^5` (`centroid_voa.verify_voa_sector_decomposition`). Every "energy bound" is a candidate hypothesis with an explicit falsifier. Proof-facing in form, horizon in claim.

## Abstract

This paper records high-speculation finite-group and energy-bound ideas as candidate horizons, with falsifier obligations attached to each. The substrate supplies two facts that are genuinely proven and two readings that are not. PROVEN: the Monster's smallest faithful complex representation has dimension `196883 = 47 x 59 x 71` (the product of the three largest supersingular primes), with McKay's `196884 = 1 + 196883` (PROOF Paper 05); and the finite VOA-weight label partitions the eight chart states as `Z(q) = 2q^0 + 6q^5` - two weight-0 vacua and six weight-5 excited states (`centroid_voa.verify_voa_sector_decomposition`). NOT PROVEN: that the VOA weight is a physical energy; that the Monster representation dimension is an energy ceiling; that the Pariah / Happy Family closure inversion (PROOF Paper 11) bounds anything physical. We treat the VOA weight as an *energy analog* and the Monster dimension as a *combinatorial ceiling analog*, and we make no physical-energy claim. The corpus's existing caution governs: per `centroid_voa`, "any VOA or Moonshine identification requires an additional transport theorem", and per IDENTITY_PAPER Section 8 the universality across native-state spaces is structural, not proven. This paper exists to *quarantine* the energy-bound speculation behind explicit falsifiers, not to advance it.

## Central Thesis

Record high-speculation finite-group/energy-bound ideas as candidate horizons with strict falsifier obligations.

## Scope Boundary

This paper claims ONLY the two proven facts: the supersingular-prime identity for `196883` and the finite partition function `Z(q) = 2q^0 + 6q^5`. It does NOT claim that VOA weight is physical energy, that any Monster-related number is an energy bound, or that the framework extends physics. Per IDENTITY_PAPER Section 9, the corpus "does not claim to extend Monstrous Moonshine; it applies it." Every energy reading is a candidate hypothesis with a falsifier. The bounded D4 closure results (Papers 05, 11) are cited as the framework's *finite* identities, not as physical theorems. This is the corpus's heaviest-obligation paper; the Open Obligations section is load-bearing.

## Definitions

- **C**: the active center; the gluon-invariant coordinate (`centroid_voa.gluon`).
- **L/R**: opposed boundary directions relative to `C`.
- **VOA weight (energy analog)**: `voa_weight(s)`, the sum of the three-conjugate wrap-step label `(w1, w2, w3)`; equals 0 on the two true vacua and 5 on the six excited states (`centroid_voa.voa_weight`).
- **Seed partition function**: `Z(q) = 2q^0 + 6q^5`, the generating function of the VOA-weight distribution over the eight chart states (`verify_voa_sector_decomposition`).
- **Monster dimension**: `196883 = 47 x 59 x 71`, the dimension of the Monster's smallest faithful complex representation (PROOF Paper 05).
- **McKay decomposition**: `196884 = 1 + 196883` (trivial observer + D4-closed Monster representation).
- **Pariah boundary (cited)**: the 6 Pariah sporadic groups close (`res^2 = 0`) under the n=3 SU(3) Weyl test while the 20 Happy Family groups open (`res^2 ~ 0.444`) - the framework's identification of Pariahs as `-1` boundary states (PROOF Paper 11, T_D4_5).
- **Energy bound (candidate hypothesis)**: any proposed inequality reading a VOA weight or a Monster number as a physical energy ceiling. Unproven by construction.
- **Transport row / Receipt / Workbook sheet / Tool binding**: as in Paper 00.

## Axioms

Axiom 29.1 - Locality: every accepted claim must be readable through a local `(L, C, R)` window before lifting.

Axiom 29.2 - Receipt Preservation: no transform is accepted unless inputs, output, and residue are logged and replayable.

Axiom 29.3 - Boundary Positivity: failed, partial, or mismatched routes are data. For this paper the dominant data are the *unwitnessed* energy readings, logged as obligations.

Axiom 29.4 - Analog Equivalence: a main-corpus claim has a physical workbook analogue. The energy readings here are analog only; their sheet records them as black follow-up until a witness exists.

## Lemmas

Lemma 29.1 - The VOA-weight partition is exact and finite. The eight chart states split into exactly two weight-0 vacua `{(0,0,0),(1,1,1)}` and six weight-5 excited states, giving `Z(q) = 2q^0 + 6q^5`. (Basis: `centroid_voa.verify_voa_sector_decomposition`, status pass.)

Lemma 29.2 - The Monster dimension is an exact arithmetic identity. `196883 = 47 x 59 x 71`, the product of the three largest supersingular primes, and `196884 = 1 + 196883` is McKay's observation. This is a fact about the Monster and the j-function, transported, not a new theorem. (Basis: PROOF Paper 05 Sections 3.1-3.2; IDENTITY_PAPER Theorem D4.)

Lemma 29.3 - No energy claim is licensed by Lemmas 29.1-29.2. The VOA weight is a wrap-step count; the Monster dimension is a representation dimension. Neither carries units of energy, and the corpus explicitly requires "an additional transport theorem" for any VOA/Moonshine identification, which this paper does not supply. (Basis: `centroid_voa.verify_centroid_voa_chain` `chain_conclusion`; IDENTITY_PAPER Section 9.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)`. The proven content:

```text
weights:  voa_weight(s) in {0, 5}            for s in the 8 chart states
vacua:    {(0,0,0),(1,1,1)}  -> weight 0     (2 states)
excited:  the other 6 states -> weight 5     (6 states)
Z(q) = 2 q^0 + 6 q^5                         [PROVEN, finite identity]
monster:  196883 = 47 * 59 * 71              [PROVEN arithmetic]
mckay:    196884 = 1 + 196883                [PROVEN arithmetic]
```

The quarantined candidate hypotheses (NOT proven):

```text
H1 (energy analog):   "VOA weight 5 is an excitation energy gap"   -> OBLIGATION
H2 (ceiling analog):  "196883 is a state-count ceiling"            -> OBLIGATION
H3 (boundary analog): "Pariah closure bounds a physical boundary"  -> OBLIGATION
each Hk carries an explicit falsifier in Open Obligations
```

Tool binding:

```text
cqe_engine  (lattice_forge: centroid_voa.voa_weight / verify_voa_sector_decomposition /
             verify_centroid_voa_chain)
```

## Proof Tree

```text
claim (energy-bound horizons)
-> local (L,C,R) window; C = gluon invariant
-> VOA-weight label (w1,w2,w3)
-> finite partition Z(q) = 2q^0 + 6q^5        [PROVEN]
-> Monster dim 196883 = 47*59*71              [PROVEN arithmetic, transported]
-> McKay 196884 = 1 + 196883                  [PROVEN arithmetic]
-> "VOA weight is energy"                      [H1: OBLIGATION + falsifier]
-> "196883 is an energy/state ceiling"         [H2: OBLIGATION + falsifier]
-> "Pariah closure is a physical bound"         [H3: OBLIGATION + falsifier]
-> workbook analogue (black follow-up)
-> receipt
```

## Practical Solved Example

**Domain:** the eight chart states of the corpus reference sequence, scored by VOA weight, alongside the supersingular-prime factorization of the Monster dimension. Non-toy: these are the exact objects of PROOF Papers 05 and the `centroid_voa` verifier.

**Procedure:** compute `voa_weight(s)` for all eight states; assemble `Z(q)`; verify `47 x 59 x 71 = 196883` and `1 + 196883 = 196884`; attempt to attach an energy reading H1 to the weight-5 sector and *record that no witness function exists*; emit a receipt with one proof row (the partition function and arithmetic identity) and three obligation rows (H1, H2, H3).

**Solved Output:** the example is solved as a quarantine: the finite partition function and the arithmetic identity reproduce exactly from `verify_voa_sector_decomposition` and direct multiplication; the three energy readings are logged as black-follow-up obligations with no witness. The honest output is two proven facts and three explicitly-unproven hypotheses, each falsifiable. This is the intended deliverable of a heaviest-obligation horizon paper.

## Tool Binding

- Module: `cqe_engine` re-exporting `lattice_forge.centroid_voa`.
- Functions: `voa_weight`, `verify_voa_sector_decomposition`, `verify_centroid_voa_chain`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: confirm `verify_voa_sector_decomposition` status pass and `Z(q) = 2q^0 + 6q^5`; confirm `47*59*71 == 196883`; emit one proof row and at least three obligation rows (one per energy hypothesis).

## Analog Workbook Sheet

- Start with grey loose substrate.
- Lay the eight chart-state cards; color each by its VOA weight (0 for the two vacua, 5 for the six excited).
- Place a heavy weight token on each excited card - this is the *energy analog only*, marked with a black tag (unwitnessed).
- Write the factorization `196883 = 47 x 59 x 71` on the binding card; this is the only ink that is white follow-up (proven).
- Use string to bind the proven partition; leave the three energy-hypothesis threads loose and black-tagged.
- White follow-up = the partition function and arithmetic identity; black follow-up = every energy reading.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [ConwayNorton1979] J. H. Conway, S. P. Norton, Monstrous Moonshine, Bull. London Math. Soc. 11, 308-339. Use: the Monster, the j-function coefficient 196884.
- [Borcherds1992] R. Borcherds, Monstrous Moonshine and monstrous Lie superalgebras, Invent. Math. 109, 405-444. Use: the VOA proof of Moonshine (the additional transport theorem this paper does NOT supply).
- [Griess1982] R. L. Griess, The Friendly Giant, Invent. Math. 69, 1-102. Use: Monster construction; Pariah/Happy Family partition context.
- [OEIS] OEIS Foundation, On-Line Encyclopedia of Integer Sequences. URL: https://oeis.org/ Use: supersingular primes and 196883/196884 as recorded sequence entries.

## Open Obligations

- HEAVIEST OBLIGATION SECTION OF THE CORPUS.
- H1 (energy analog): the VOA weight is NOT shown to be a physical energy. Falsifier: any physical system whose excitation gap contradicts the 0-vs-5 weight split, OR the absence of any units-bearing map from wrap-steps to joules. The tool must defer H1 until such a map exists.
- H2 (ceiling analog): `196883` is NOT shown to be an energy or state-count ceiling. Falsifier: a counted state space exceeding 196883 under the same D4 closure, OR the lack of a proved fingerprint-to-Monster map (open per IDENTITY_PAPER Section 8.2).
- H3 (Pariah boundary): the Pariah closure inversion (PROOF Paper 11) is encoding-specific (bit-length parity) and is NOT a physical bound. Falsifier: an isomorphism-invariant encoding that breaks the closure inversion (Paper 11 Section 6 caveat).
- The "additional transport theorem" that would license any VOA/Moonshine energy identification is OPEN (`verify_centroid_voa_chain` chain_conclusion). No part of this paper supplies it.
- IDENTITY_PAPER Section 8.3 (SPINOR signature not yet empirically observed) and 8.4 (27-dim meta-vignette closure open) are inherited as open.
- Replace citation anchors with final bibliography entries.

## Back-Propagation Targets

- Paper 00 receives the term "energy analog" with its mandatory black-tag (unwitnessed) discipline.
- Paper 05 / Paper 11 receive the note that their results are cited here as finite identities only, never as energy bounds.
- The analog workbook manual receives the weight-token + black-tag sheet rule.
- Paper 31 records how this paper's quarantine of speculation is itself an enacted `(L, C, R)` boundary read - the strictest one in the corpus.
