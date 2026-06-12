# Paper 23 - FoldForge Protein Folding

## Status

Horizon / speculative layer with explicit obligations. Connects a real scientific domain (protein structure and backbone topology) to the corpus substrate. The link (oloid winding number <-> backbone fold/knot invariant; chart sweep <-> contact map) is the contribution. No biological prediction is claimed as proven; predictive test against deposited structures is the central obligation, stated with a falsifier.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

A protein backbone is a one-dimensional chain that folds into a three-dimensional structure whose topology — including, rarely, genuine knots — is functionally significant. The corpus already carries a discrete topological invariant for a swept chain: the oloid winding number, computed by `rule30_oloid_winding_from_n` as the accumulated `2*pi` rotation of the rolling-oloid spinor frame along the chart, with an explicit `candidate_witness` status and an open all-`N` extraction gap. We propose registering a residue chain as a chart sweep, the residue-residue contact map as the receipt of that sweep, and the oloid winding / bifurcation trace as a *candidate topological descriptor* of the fold. The contribution is the registration map, not a folding engine: modern structure prediction (AlphaFold [AlphaFoldNature]) already attains high accuracy from sequence and coevolution, and predicts complex backbone knots [ProteinKnots]. The corpus does not compete with that; it asks a narrower, falsifiable question — does the substrate's winding/bifurcation trace correlate with topological features (contact order, knot type) of deposited structures? Every emitted fold descriptor is a candidate with a contact-map receipt and an obligation: validate against PDB structures or be rejected.

## Central Thesis

Apply the same ribbon/bifurcation logic to protein-chain fold hypotheses with contact-map and topology receipts.

## Scope Boundary

This paper claims (i) a registration of a residue chain into the chart sweep, (ii) a contact-map receipt format, and (iii) a winding/bifurcation descriptor with `candidate_witness` status. It does NOT claim to predict a native structure, free energy, or fold rate, and it does NOT claim parity with AlphaFold. The descriptor's biological meaning is entirely an obligation. Excess interpretation is logged, not promoted.

## Definitions

- **C**: the active center; here, the residue at chain position `n`.
- **L/R**: the two opposed boundary directions relative to `C`; here, residues `n-1` and `n+1` along the backbone.
- **Residue chart**: the sweep of overlapping triples `(res_{n-1}, res_n, res_{n+1})` along the chain, after a binary/coarse encoding of a per-residue property (e.g., hydrophobic = 1, polar = 0).
- **Contact map**: the symmetric matrix `K_{ij} = 1` iff residues `i, j` are within a distance threshold in 3D; the standard topology-bearing receipt of a fold.
- **Oloid winding number** `w(N)`: the corpus's accumulated spinor-frame rotation along the chart to depth `N` (`rule30_oloid_winding_from_n`); a discrete candidate fold invariant.
- **Bifurcation**: a substrate fold event where the local geometry class changes (`rule30_oloid_bifurcation_detector`); proposed as a candidate marker of a turn / topological transition.
- **Knot type**: the prime-knot classification of the (closed) backbone, the strongest topological label [ProteinKnots].
- **Receipt**: a replayable record carrying the contact map, the winding trace, the bifurcation list, and obligation status.
- **Tool binding**: the lattice-forge oloid / winding module family.

## Axioms

Axiom 23.1 - Locality: a fold descriptor is admissible only if it is built from local `(L, C, R)` residue windows before any global topology is asserted.

Axiom 23.2 - Receipt Preservation: no fold descriptor is accepted unless its contact map, winding trace, and obligation status can be logged and replayed.

Axiom 23.3 - Boundary Positivity: a residue window that fails the contact threshold or the winding extractor is data — it becomes an obligation, never a silent deletion.

Axiom 23.4 - Analog Exposure Equivalence: every accepted descriptor has a physical workbook analogue (a beaded string folded over a peg grid encoding contacts).

## Lemmas

Lemma 23.1 - A residue window that preserves its center `C` and records its `L/R` neighbors can be transported into the contact ledger without erasing non-contacting alternatives (kept as obligation rows). (Basis: contact is a local-window predicate.)

Lemma 23.2 - A tool-emitted contact map and a workbook bead-and-peg model that encode the same residue contacts are equivalent receipts at different media layers.

Lemma 23.3 - The oloid winding number `w(N)` is a homotopy-style discrete invariant of the swept frame; a `side` reversal contributes a full inversion and a `side`-to-`null` step contributes a half inversion (per `rule30_winding_number_proof`). This is offered as a *candidate* correlate of backbone topology, carrying the corpus's standing open gap: a depth-only extractor of `w(N)` from `N` alone is not yet proven (DEPTH_ONLY_WINDING_EXTRACTOR_PENDING).

## Formalism / Calculus Sketch

A fold-candidate state is `F = (C, L, R, B, T, O)`: residue center, two backbone neighbors, bifurcation rule `B`, winding transform `T`, obligation set `O`. Acceptance:

```text
T(residue_chart) -> F
receipt(F) = {contact_map K, winding_trace w(.), bifurcations, status}
status in {candidate_witness, pass_with_open_gaps}   # never "proven"
obligation: validate_against_PDB(F) is OPEN
open_gap: DEPTH_ONLY_WINDING_EXTRACTOR_PENDING (inherited from substrate)
```

Substrate link: encode the chain to a binary residue chart; sweep with the chart readout; accumulate `w(N)` via the rolling-oloid frame; flag bifurcations as candidate turn/topology markers; build `K` as the receipt. Tool binding:

```text
cqe_engine  (rule30_oloid_winding_from_n, rule30_oloid_antipodal_winding,
             rule30_oloid_bifurcation_detector, rule30_winding_number_proof)
```

## Proof Tree

```text
claim (substrate emits candidate fold/topology descriptors)
-> binary residue chart (local windows)
-> contact-map receipt K
-> oloid winding trace w(N)  [candidate invariant]
-> bifurcation markers       [candidate turns]
-> fold descriptor F (status: candidate_witness)
-> PDB-validation obligation (OPEN, with falsifier)
-> depth-only-extractor open gap (inherited)
-> supplemental workbook analogue (bead string + peg grid)
-> receipt
```

## Practical Solved Example

**Domain:** a short peptide with a known deposited structure, hydrophobicity-encoded to a binary residue chart.

**Procedure:** sweep the residue chart; compute the winding trace `w(N)` and bifurcation list; build the predicted contact map from windows whose center and both boundaries are hydrophobic (a crude contact heuristic); compare the bifurcation positions against the deposited structure's turn positions.

**Solved Output (what is actually established):** the pipeline emits a reproducible contact-map receipt, a winding trace, and a bifurcation list with `status = candidate_witness`, plus the obligation row `validate_against_PDB`. The example is "solved" only in the corpus sense — the descriptor reproduces identically from the formal sweep rule, the `cqe_engine` winding functions, and the workbook bead string. No biological fold is predicted; the agreement (or disagreement) of bifurcations with real turns is precisely the open obligation. AlphaFold [AlphaFoldNature] remains the accuracy reference, and complex backbone knots [ProteinKnots] are the hardest test cases for any topological descriptor.

## Tool Binding

- Module: `cqe_engine` (`rule30_oloid_winding_from_n`, `rule30_oloid_antipodal_winding`, `rule30_oloid_bifurcation_detector`, `rule30_winding_number_proof`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: emit one contact-map receipt and one winding trace with `status = candidate_witness`; emit the inherited open-gap row (`DEPTH_ONLY_WINDING_EXTRACTOR_PENDING`) and one obligation row (`validate_against_PDB`).

## Analog Workbook Sheet

- Start with grey loose substrate; lay a peg grid (rows = residue index).
- Thread a beaded string along the backbone; place the `C` bead at the center residue, `L`/`R` beads adjacent.
- Pin contacts where two beads meet a shared peg (the analog contact map).
- Mark a colored bead at each bifurcation (candidate turn); wind the string for the oloid trace.
- White follow-up = a contact/winding pattern that matches a known structure (candidate validated); black follow-up = a mismatch (obligation).
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [AlphaFoldNature] Jumper et al. Highly accurate protein structure prediction with AlphaFold. Nature 2021. URL: https://www.nature.com/articles/s41586-021-03819-2 Use: protein structure prediction accuracy reference (background; not claimed to be matched).
- [ProteinKnots] Brems et al. AlphaFold predicts the most complex protein knot and composite protein knots. URL: https://arxiv.org/abs/2207.07410 Use: backbone topological complexity / knots — the hardest test for the winding descriptor.
- [Rule30] Wolfram Rule 30. URL: https://mathworld.wolfram.com/Rule30.html Use: the chart readout law underlying the residue sweep.

## Open Obligations

- **PDB predictive test (primary, with falsifier).** Compute `w(N)` and bifurcation traces for a held-out set of deposited structures and test whether they correlate with contact order and/or knot type. Falsifier: if no statistically significant correlation survives a permutation null over a representative chain set, the winding-as-fold-invariant hypothesis (Lemma 23.3) is rejected.
- **Depth-only winding extractor (inherited open gap).** `w(N)` is currently read from the swept spinor trace; a modular / continuous-kinematic extractor computing `w(N)` from `N` directly is not yet proven.
- **Encoding obligation:** the binary residue encoding (hydrophobicity) is a placeholder; a coevolution-aware or physicochemical multi-bit encoding is unspecified.
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add one domain-expert (structural biology) critique pass.

## Back-Propagation Targets

- Paper 00 receives the term "inherited open gap" propagation discipline if not already present.
- Paper 21 (MorphForge) receives the bifurcation -> turn-marker correspondence.
- The lattice-forge registry records the winding/bifurcation fold-descriptor surface.
- The analog workbook manual receives the bead-string / peg-grid contact rule.
- Paper 31 records how this paper's presentation order enacts the same `(L, C, R)` sweep.
