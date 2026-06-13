# Paper 23 - FoldForge Protein Folding

## Abstract

Paper 23 applies the Forge reading discipline to protein-chain descriptors. Its
closed result is not a protein structure predictor. Its closed result is a
replayable descriptor receipt: a residue chain is converted into local `(L, C,
R)` windows, a contact-map receipt is generated, local side changes are marked
as candidate bifurcations, and the result is paired with the bounded oloid
winding substrate and its explicit open gaps.

The receipt proves that FoldForge can emit candidate fold/topology descriptors
without hiding the difference between a descriptor and a biological prediction.
It does not claim native coordinates, free-energy minima, fold rates, AlphaFold
parity, PDB validation, or measured thermodynamic behavior.

## Closed Evidence

The verifier uses the sequence `MKTFFVLLLCTFTVLA` as a compact demonstration
chain. It encodes residues by a simple hydrophobic/polar bit, produces 16 local
windows, and has 14 complete interior `(L, C, R)` windows. The contact-map
heuristic emits a symmetric, zero-diagonal map with nonzero contacts. Local side
changes in the residue windows become candidate bifurcation marks.

The lattice substrate contributes a bounded winding witness. With `max_depth =
512` and `max_order = 4`, the winding proof returns `pass_with_open_gaps`; its
schema verifier passes; its operator is stable across pages; and its finite
operator has 8 states. The standing gap is named:
`DEPTH_ONLY_WINDING_EXTRACTOR_PENDING`.

The direct oloid predictor is not promoted beyond its evidence. On a 128-depth
window it returns `pass_with_open_gaps` with defects, so Paper 23 treats it as
diagnostic substrate rather than biological proof. The bifurcation detector
schema also passes with open gaps and carries
`MIGRATION_DIRECTION_FORCED_BY_PARITY_PENDING`.

## Definitions

A residue chart is the sequence of overlapping local windows
`(residue[n-1], residue[n], residue[n+1])`. `C` is the active residue. `L` and
`R` are its two backbone neighbors. A contact map is a symmetric matrix recording
which residue pairs satisfy the selected contact predicate. In this verifier the
predicate is deliberately simple: separated hydrophobic residues form a
candidate contact. A bifurcation mark is a side-change event in the local
window, used as a candidate turn or topology marker.

A winding trace is the bounded oloid/spinor trace supplied by the lattice
substrate. It is a trace witness, not a depth-only theorem. A FoldForge descriptor
is admitted only when it carries both its contact-map receipt and its open
validation obligations.

## Claims

1. A residue chain can be read as local CQE windows.

The verifier constructs one chart row per residue and confirms that the interior
chain has complete left-center-right windows.

2. A replayable contact-map receipt can be emitted.

The example contact map is symmetric, has zero diagonal, has nonzero contacts,
and has density strictly between 0 and 1. This proves the receipt format and
replay rule, not biological correctness.

3. Local side changes can be marked as candidate fold events.

The local window sequence emits side-change marks. These marks are descriptors
only; they become biological claims only after comparison to deposited or
experimentally measured structures.

4. The oloid winding substrate is bounded and honest about its gap.

The winding model verifies as a bounded trace witness with a stable 8-state
operator. It also carries the depth-only extractor gap, so the paper does not
claim a closed all-`N` winding formula.

5. FoldForge remains a candidate descriptor until validated.

The direct oloid predictor and bifurcation detector both carry open gaps. Paper
23 treats those gaps as part of the result.

## Theorem 23

FoldForge is a valid CQE protein-fold descriptor kernel when it returns a
replayable residue-window chart, contact-map receipt, candidate bifurcation list,
bounded winding witness, and explicit validation obligations for a chosen
protein-chain observation.

## Proof

Run `verify_foldforge_descriptor.py`. The first check builds the residue chart
and verifies the local-window count. This imports the Paper 21 reader into a
protein-chain setting without making any global structure claim.

The second check builds the contact map. Symmetry and zero diagonal are required
because a residue-residue contact is an unordered relation and a residue is not
treated as contacting itself. Nonzero contact density proves that the example
produces a reviewable receipt.

The third check marks local side changes. These marks are the candidate
bifurcations. They are useful precisely because they are not allowed to become
turn, knot, or fold claims without a later PDB comparison.

The fourth check verifies the bounded winding substrate. The accepted claim is
the bounded trace witness and stable operator. The receipt also records
`DEPTH_ONLY_WINDING_EXTRACTOR_PENDING`, so an all-depth shortcut is not silently
claimed.

The fifth and sixth checks confirm that the less-closed substrate components
remain visible. The oloid predictor has defects in the tested window, and the
bifurcation detector carries its parity-direction gap. Because the verifier
passes only while those gaps remain explicit, the paper proves the descriptor
kernel and not a biological structure theorem.

Therefore Paper 23 closes FoldForge as a reproducible contact-map and topology
descriptor surface with open biological validation obligations.

## Receipt

The formal receipt is generated at:

`production/formal-papers/CQE-paper-23/foldforge_descriptor_receipt.json`

## Open Obligations

PDB validation remains open. Native structure prediction is not claimed.
Depth-only winding extraction remains open. The biological encoding remains a
demonstration choice. Fold-rate and thermodynamic validation remain open.

## Suite Role

Paper 22 proves the applied candidate-ledger pattern. Paper 23 uses the same
pattern for protein-chain descriptors. Paper 24 may reuse the local-window and
path-descriptor discipline for game or automata lattices, but it must not inherit
protein-specific biological claims.
