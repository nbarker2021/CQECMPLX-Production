# Paper 11 - Theory Admission Gate

## Status

Admission-gate paper. Defines the discipline by which an external theory enters the corpus as a *transport candidate*, and how its closure result classifies it as admitted, boundary, or rejected - turning failures into boundary receipts rather than dismissals. Grounded in the Pariah/Happy-Family inversion (PROOF Paper 11). Proof-facing. Inherits the Paper 00 contract.

## Abstract

This paper admits external theories as transport candidates whose failures become boundary receipts rather than summary dismissals. An external theory enters by an encoder that maps its objects to a binary tape (the worked case is *bit-length parity* of a group order), after which the same `n = 3` SU(3) Weyl test is applied. The admission gate has three outlets: *admitted* (closes, `res^2 = 0`, idempotent), *boundary* (closes where the established theory does not, marking a `-1` boundary state), and *rejected-as-datum* (does not close under the declared encoder, logged as an open-encoder obligation rather than a dismissal). The load-bearing empirical case is the Pariah/Happy-Family inversion from PROOF Paper 11: under bit-length parity, the 6 Pariah sporadic groups (`J_1, J_3, J_4, Ru, ON, Ly`) close (`res^2 = 0`, chain `e -> e -> e`) while the 20 Happy Family groups open (`res^2 ~ 0.444`). The Pariahs - outside the Monster's Happy Family - are thereby identified as the `-1` boundary states of the Monster expansion at the D4 closure level (`IDENTITY_PAPER` 6.7). The gate's discipline is that this is a *boundary receipt for a specific encoder*, not a new theorem in finite-group theory; an alternative encoder may classify differently, and that fact is itself recorded.

## Central Thesis

Admit external theories as transport candidates whose failures become boundary receipts rather than summary dismissals.

## Scope Boundary

This paper claims the admission *gate* - the encoder-declared, three-outlet classifier - and the specific Pariah/Happy-Family inversion under bit-length parity (PROOF Paper 11 Theorem T_D4_5). It does NOT claim a new finite-group-theory result, nor that the closure is encoder-independent: PROOF Paper 11 Section 6 states the result holds for the bit-length parity encoding and that alternative encodings may differ. The gate admits theories as *candidates*; admission is a closure observation under a declared encoder, not a proof about the theory's content. Excess interpretation is logged as obligation.

## Definitions

- **Transport candidate**: an external theory presented for admission via a declared encoder to a binary tape; not yet classified.
- **Admission encoder**: the map from a theory's objects to a binary sequence. The worked encoder is *bit-length parity*: for a group `G`, write `|G|` in binary and take the parity of its bit-length; collect over a class of groups in canonical order (PROOF Paper 11 Section 2).
- **n=3 closure test**: the `shell = 2` conditional transition matrix at `n = 3`, decomposed in the `S_3` group ring; the residual squared `res^2` and the dominant chain are the test outputs (`IDENTITY_PAPER` T4; PROOF Paper 07 Definition 1.1).
- **Admitted**: a candidate whose encoded tape closes (`res^2 < 10^-6`, idempotent); the established theory's structure transports onto it.
- **Boundary (`-1`) state**: a candidate that closes precisely where the surrounding established structure does NOT - e.g. the Pariahs closing while the Happy Family opens; identified as a `-1` boundary of the larger expansion (`IDENTITY_PAPER` 6.7; PROOF Paper 11 Section 4).
- **Rejected-as-datum**: a candidate that does not close under the declared encoder; recorded as an open-encoder obligation (try another encoder), never a dismissal.
- **Happy Family / Pariah**: the 20 sporadic groups that are subquotients of the Monster `M`, versus the 6 (`J_1, J_3, J_4, Ru, ON, Ly`) that are not (Griess 1982; PROOF Paper 11 Section 1).

## Axioms

Axiom 11.1 - Locality: a candidate is admitted only through the same local `(L, C, R)` chart machinery as a native sequence; no external theory bypasses the chart.

Axiom 11.2 - Receipt Preservation: the admission encoder is part of the receipt; the closure verdict is bound to its declared encoder and is meaningless without it.

Axiom 11.3 - Boundary Positivity: a failure to close is a boundary receipt (a `-1` state, or an open-encoder datum), never a summary dismissal of the theory.

Axiom 11.4 - Analog Equivalence: the gate has a workbook analogue - a three-outlet sorter (admitted / boundary / rejected-as-datum) with the encoder written on each card.

## Lemmas

Lemma 11.1 - Encoder-bound verdict: the closure outcome is a property of the (theory, encoder) pair. (Basis: PROOF Paper 11 Section 6 - the result holds for bit-length parity; alternative encodings may differ.) Hence every admission verdict carries its encoder, and a different encoder is a different admission attempt, not a contradiction.

Lemma 11.2 - The Pariah/Happy-Family inversion: under bit-length parity, the 6 Pariah groups close (`res^2 = 0`, dominant chain `e -> e -> e`, idempotent) and the 20 Happy Family groups open (`res^2 ~ 0.444`, non-idempotent). (Basis: PROOF Paper 11 Section 3, Theorem T_D4_5; verifier `exp_pariah_boundary.py`, extending `exp_monster_moonshine.py`.) This is an exact behavioral inversion of the established Monster-membership partition.

Lemma 11.3 - Boundary identification: a candidate that closes where its surrounding established structure opens is a `-1` boundary state of that structure's expansion. (Basis: `IDENTITY_PAPER` 6.7 - the D4 ground state is the spinor signature `(0, eps, 0)`, requiring a closed observer state of dimension 1 plus an open measurement space of dimension `196883`; the Happy Family populates the open `196883`-dim space, the Pariahs the closed observer boundary.) The gate routes such candidates to the *boundary* outlet, not *rejected*.

## Formalism / Calculus Sketch

An admission state is `A = (Th, E, b, Q, cls, O)`: the candidate theory `Th`, the declared encoder `E`, the encoded tape `b = E(Th)`, the closure signature `Q = (res^2, dominant_chain, idempotent)`, the classification `cls`, and the obligation set `O`. The gate decides:

```text
E declared and logged                         (Axiom 11.2)
b = E(Th)                                      (e.g. bit-length parity of group orders)
chart(b) -> shell=2 n=3 matrix -> res^2, chain, idempotent
if res^2 < 1e-6 and idempotent:
    if surrounding established structure does NOT close: cls = boundary (-1 state)
    else:                                                cls = admitted
else:
    cls = rejected-as-datum ; O += "try alternative encoder"   (NOT a dismissal)
```

The boundary outlet is the gate's distinctive feature: the Pariahs are not rejected for being outside the Monster - they are *admitted as the boundary* the Monster expansion needs. The discipline mirrors Axiom 00.3 (Boundary Positivity) lifted from local states to whole theories. Tool binding:

```text
cqe_engine  (experiment harness: exp_pariah_boundary.py, exp_monster_moonshine.py;
             the n=3 S_3 group-ring decomposition routine shared with Paper 07)
```

## Proof Tree

```text
claim (external theories enter as candidates; failures become boundary receipts)
-> declare admission encoder E (Lemma 11.1)
-> b = E(Th) (bit-length parity for groups)
-> n=3 closure test -> (res^2, dominant chain, idempotent)
-> three-outlet gate:
     closes + surrounding closes        -> admitted
     closes + surrounding opens         -> boundary (-1 state) (Lemma 11.3)
     does not close under E             -> rejected-as-datum -> open-encoder obligation
-> Pariah/Happy-Family inversion (Lemma 11.2, T_D4_5)
-> worked example (exp_pariah_boundary.py)
-> workbook analogue (three-outlet sorter)
-> receipt (encoder + signature + classification)
```

## Practical Solved Example

**Domain:** admission of the 26 sporadic simple groups, partitioned into the 20 Happy Family and the 6 Pariah groups, under the bit-length parity encoder.

**Procedure:** for each group, write `|G|` in binary and take its bit-length parity; collect the Happy Family parities and the Pariah parities into two tapes in canonical classification order (e.g. `M`: order ~`8.08 x 10^53`, ~179 bits, parity 1; `B`: ~`4.15 x 10^33`, ~112 bits, parity 0; `J_1`: order `175560`, 18 bits, parity 0). Apply the `n = 3` closure test to each tape via `exp_pariah_boundary.py`.

**Solved Output:** the 6-group Pariah tape returns `res^2 = 0.00` (CLOSED), dominant chain `e -> e -> e`, idempotent yes; the 20-group Happy Family tape returns `res^2 ~ 0.444` (OPEN), variable dominant chain (typically `e -> (1,2,3) -> (1,2)`), not idempotent (PROOF Paper 11 Section 3, Theorem T_D4_5). The gate therefore routes the Pariahs to the *boundary* outlet - the `-1` boundary states of the Monster expansion at the D4 closure level - and the Happy Family to the open-bulk side (the `196883`-dim measurement space). Crucially, the Happy Family is NOT rejected: its open signature is a recorded datum, and PROOF Paper 11 Section 6 logs that the verdict is encoder-bound (bit-length parity), so an alternative encoder is a separate admission attempt. The example is solved because the inversion, the two signatures, and the encoder caveat reproduce identically from `exp_pariah_boundary.py`, the formal gate, and the three-outlet workbook sorter.

## Tool Binding

- Module: `cqe_engine` (experiment harness `exp_pariah_boundary.py`, extending `exp_monster_moonshine.py`; the shared `n = 3` `S_3` group-ring decomposition used by Paper 07).
- Required outputs: `receipt.json` (must include the declared encoder), `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: encode the 6 Pariah and 20 Happy Family group orders by bit-length parity; confirm the Pariah tape returns `res^2 ~ 0` (closed, idempotent) and the Happy Family tape `res^2 ~ 0.444` (open); emit one *boundary* row (Pariahs) and one *rejected-as-datum* obligation row demonstrating an encoder that does not close.

## Analog Workbook Sheet

- Start with grey loose substrate; make a card for each candidate theory and write the chosen encoder on the card.
- Fill the card's strip by the encoder (bit-length parity of each group order), then read its `shell = 2` windows and tally closure.
- Drop the card into one of three trays: white tray = admitted (closes with its surroundings); half-black tray = boundary / `-1` state (closes where the surroundings open - the Pariah tray); black tray = rejected-as-datum (did not close under this encoder).
- A black-tray card is never thrown away: clip a follow-up note "try encoder E'" and return it to the input pile.
- Bind the admitted and boundary cards into the matching color notebook; keep the rejected-as-datum cards in the open-obligation folder.

## IRL Citation Anchors

- [ConwaySloane1999] J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups (3rd ed.), Springer, 1999. Use: the Monster, Leech lattice, and sporadic-group context for the admission gate.
- [Niemeier1973] H.-V. Niemeier, Definite quadratische Formen der Dimension 24 und Diskriminante 1, J. Number Theory 5, 142-178, 1973. Use: the rank-24 lattice landscape against which Monster-boundary structure is read.
- [OEIS] OEIS Foundation, On-Line Encyclopedia of Integer Sequences. URL: https://oeis.org/ Use: canonical sporadic-group orders and their bit-length sequences for the encoder.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: the boundary receipt and encoder provenance attached to each admission verdict.

## Open Obligations

- The closure result is bound to the bit-length parity encoder (PROOF Paper 11 Section 6); whether character-table-based or isomorphism-invariant encoders give the same Pariah/Happy-Family inversion is open.
- The identification of the Pariahs as `-1` boundary states is a structural reading of the D4 closure (`IDENTITY_PAPER` 6.7), not a new finite-group theorem; the algebraic role is surfaced, not proved.
- The gate's *admitted* outlet is defined but not exercised on a worked external theory here (the worked case is the *boundary* outlet); an admitted-outlet example is an obligation.
- The `196883 = 47 . 59 . 71` Monster representation dimension is cited as the open measurement space; its exact role in the gate's boundary count is structural and open.
- Replace citation anchors with final bibliography entries.

## Back-Propagation Targets

- Paper 00 receives the three-outlet admission vocabulary (admitted / boundary / rejected-as-datum) as a lift of Boundary Positivity to whole theories.
- Paper 07 receives the confirmation that the `n = 3` closure test is the shared admission criterion across sequence families and external theories.
- Paper 10 receives the rejected-as-datum rows as open-encoder obligations in the master receipt.
- The ForgeFactory / lattice_forge registry records `exp_pariah_boundary` as the admission-gate witness.
- Paper 31 records how the corpus's own admission of external mathematics (Monster, Pariahs) is an enacted pass through this very gate.
