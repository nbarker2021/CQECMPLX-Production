# Paper 21 - MorphForge / PolyForge / MorphoniX

## Abstract

Paper 21 defines the applied Forge reader. Its closed result is not that every
symbol, material, organism, or CAD object is already solved. Its closed result is
that an observed object can be converted into a grid-swept ribbon, encoded as a
lossless symmetric-group word, accounted as morphon records, and landed in the
24-dimensional terminal template while every unfinished bridge remains explicit.

The receipt for this paper verifies a Rule-30 shell-2 ribbon through depth 4096.
It contains 1569 shell-2 states and a 1568-step S3 word with zero round-trip
mismatches. The morphonics ledger closes its schema with 5 morphons, 5
transforms, 5 projections, 3 accounting records, 3 bridges, 11 claims, 3 explicit
failure records, and 5 passing morphon closure tests. The terminal landing form
used by the paper is the canonical `Niemeier:E8^3` composition tree: ambient
dimension 24, root rank 24, and residue closed by required index.

This is enough to prove the MorphForge reading contract. It is not enough to
claim cross-medium equivalence, a Mandelbrot boundary theorem, a Leech lattice
construction, TF1 closure, biological closure, material closure, or CAD closure.
Those items remain open obligations unless later papers attach domain-specific
verifiers.

## Definitions

An observation event begins when an observer chooses a centroid or object to
enumerate. Paper 21 treats that choice as a ribbon source: a sequence of local
windows that may be read as left, center, and right boundary states.

A ribbon is a finite ordered list of such windows. A shell-2 ribbon is the
subtrajectory selected by the local shell rule used by the included Rule-30 chart
codec. A fold is a non-identity transition in the symmetric group S3. A morphon
is a ledger row that records a source, transform, projection, accounting link,
and claim status for a readable object. A terminal landing template is the
24-dimensional composition tree used to place the reading into the lattice suite
without treating the placement as a stronger construction than the receipt
actually proves.

## Claims

1. The chart codec closes a lossless ribbon encoding.

The verifier reports `status = pass`, `round_trip_mismatches = 0`, and
`first_mismatch = null` for the Rule-30 shell-2 trajectory through depth 4096.
The shell-2 ribbon has length 1569, and its S3 word has length 1568, exactly one
transition per adjacent pair of shell states.

2. Folds are observable as non-identity S3 steps.

The receipt records 494 identity self-loops and 1074 non-identity transitions.
The non-identity transitions observed in this run are transposition-class steps:
197 `(1 2)`, 594 `(1 3)`, and 283 `(2 3)` events. The two 3-cycle counts are
zero in this receipt. Paper 21 therefore proves a fold classifier for this
ribbon, not a universal theorem that every future ribbon has the same element
distribution.

3. The morphonics model closes as an accounting substrate with carried gaps.

The morphonics verifier returns `pass_with_open_gaps`. Schema status is `pass`;
all five morphon closure tests pass; and the three open failure labels are
explicit: `PENDING_IMPORT`, `MISSING_MORPHISM`, and `PENDING_MEASUREMENT`.

4. The terminal landing form is a 24-dimensional template, not a Leech
construction.

The terminal tree is `Niemeier:E8^3`, with ambient dimension 24, root rank 24,
three component-action branches, 24 compact involution slots, and residue closed
by required index. This proves that the MorphForge reader can land its accounting
in the 24-dimensional lattice package. It does not prove a Leech import unless
the missing Golay or Construction-A data are supplied.

5. Applied-domain claims inherit the substrate and the residue.

GraphSTX calendar flows, FridgeForge recipe flows, CADForge/WireBlock design
flows, metamaterial sketches, TF1 examples, biological examples, and other
product-facing uses may all use the Paper 21 reader. They do not become closed
scientific claims from that inheritance alone. Each must attach a domain receipt
or carry an open-obligation label.

## Theorem 21

The MorphForge reader is a valid CQE applied-reader kernel exactly when it
returns three artifacts for a chosen observation event:

1. a lossless ribbon word,
2. a morphon accounting ledger with explicit closure and failure statuses, and
3. a terminal landing template whose strength is not overstated.

## Proof

Run `verify_morphforge_ribbon.py`. The first check verifies that the chart codec
round-trips the shell-2 trajectory with no mismatches. Because the encoded word
has one element for every adjacent pair in the shell-2 ribbon, the word is not a
summary or illustrative sketch; it is a reversible reading of the selected
subtrajectory.

The second and third checks classify the transition content of that word. The
identity self-loops preserve local state. The 1074 non-identity steps are the
fold events in this receipt. Since the verifier also reports the S3 element
counts, a reviewer can falsify the fold claim by finding a mismatch between the
word, the decoded ribbon, and the reported counts.

The fourth through seventh checks examine the morphonics ledger. The model is
accepted only as `pass_with_open_gaps`; it is not allowed to silently promote
unresolved bridges into solved claims. Every morphon has a passing closure test,
and the missing Leech import, expanded morphism witnesses, and TF1 measurement
remain named failure records.

The final check lands the reading in the `Niemeier:E8^3` terminal tree. The
receipt confirms the 24-dimensional rank and residue condition needed for the
suite-level placement. Because the receipt identifies the evidence level as a
template, the proof does not smuggle in a completed Leech construction or a
domain-specific experimental proof.

Therefore Paper 21 proves the applied Forge reading and accounting kernel while
preserving the exact boundary of what is not yet closed.

## Receipt

The formal receipt is generated at:

`production/formal-papers/CQE-paper-21/morphforge_ribbon_receipt.json`

The paper passes when every listed check passes and the remaining obligations
are carried in the receipt rather than omitted from it.

## Falsification Conditions

Paper 21 fails if the shell-2 word does not decode back to the selected ribbon,
if the word length differs from the number of adjacent shell transitions, if the
reported S3 counts disagree with the encoded word, if a morphon lacks accounting
closure, if an open bridge is promoted without a verifier, or if the terminal
landing is represented as stronger than its receipt.

## Suite Role

Paper 20 supplies the ledger admission rule. Paper 21 supplies the applied
reader used by later product, material, biological, and design papers. Papers 22
through 24 may inherit the ribbon, fold, morphon, and terminal-template
discipline, but they must add their own domain verifiers before claiming closure.

## Conclusion

MorphForge, PolyForge, and MorphoniX are the same formal move at different
scales: choose the observation event, read the local windows as a reversible
ribbon, account the transformation in the morphon ledger, and land only the
verified result into the lattice suite. The power of the method is not that it
declares every bridge solved. The power is that it makes each bridge visible,
portable, and testable.
