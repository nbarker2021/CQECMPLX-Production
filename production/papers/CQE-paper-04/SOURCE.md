# Paper 04 - Boundary Repair

## Status

Foundational paper. Defines boundary repair as the transport operation that converts a failed join into a typed constraint for the next legal route. Proof-facing.

## Abstract

We define *boundary repair*: the operation that takes a join which failed to close — a sequence window whose head and tail do not land on the same carrier circle — and converts that failure into a typed constraint that names the exact tail needed to make a legal route. The Binary Boundary Adapter reads the last `window` bits of any binary sequence, unaltered, and computes the head and tail Lie-conjugate rest states that bound it. When head and tail lie on the same oloid circle (`F` or `P`), the arc is *closed*; when they do not, the arc is *crossing*, and the adapter emits the `matching_tail` — the specific rest state the tail would need for closure. This matching tail is the repair: it is not a correction of the data (the input is never modified) but a typed constraint on the next legal continuation. We tie boundary repair to the correction surface of Paper 02 (the frustrated-bond carry, `C=1, R=0`, that no linear rule resolves) and to the dual-path oloid carrier (Paper 05), where a failed join on one path is routed onto the antipodal or shared contact-edge path rather than dropped. Boundary repair is the corpus's ErrorWall discipline: failures become routing data classified into a small set of transport layers, each with a named witness and an explicit proof boundary.

## Central Thesis

Define boundary repair as the transport operation that converts failed joins into typed constraints for the next legal route: a non-closing arc names the rest state it would need to close, and that name becomes the constraint the next transport step must satisfy.

## Scope Boundary

This paper claims the boundary-repair operation (the head/tail/matching-tail computation) and its classification into the four named transport layers with explicit proof boundaries. It does not claim that any layer beyond the demonstrated ones derives a center bit from depth `N`; the transport ledger explicitly carries the `bounded_local` and `registered_landing_forms` layers as open lifts. Excess interpretation is logged as obligation.

## Definitions

- **Lie conjugate (rest state)**: a chart state with `L = R` — read-write balance, the bar at zero, carry resolved (`binary_boundary_adapter.py`, physical interpretation block).
- **Oloid circle**: the two equal-radius circles of the rolling carrier; `CIRCLE_F = {(0,1,0),(1,1,1)}` (gluon-bound) and `CIRCLE_P = {(0,0,0),(1,0,1)}` (gluon-free) (`binary_boundary_adapter.py :: CIRCLE_F, CIRCLE_P`).
- **Head / tail**: the entry and exit Lie-conjugate rest states bounding a window, obtained by annealing the entry/exit triads to their rest states (`binary_boundary_adapter.py :: adapt`, via `anneal_to_lie_conjugate`).
- **Closed arc / crossing arc**: closed iff head and tail are on the same circle (`matched = (head_circle == tail_circle)`); otherwise crossing (`arc_type`).
- **Matching tail (the repair)**: when an arc is crossing, the partner rest state the tail would need for closure (`binary_boundary_adapter.py :: matching_tail`, via `_partner`).
- **Carry / frustrated bond**: the state `C=1, R=0` where the correction must fire; the boundary defect that no linear rule explains (`binary_boundary_adapter.py :: CORRECTION_FIRING`).
- **Transport obligation layer**: one of four typed transport rows, each with a source object, target object, map, preserved quantity, failure condition, named witness, classification, and proof boundary (`transport_obligations.py :: transport_obligations`).

## Axioms

Axiom 04.1 - Locality: a join is read from a local window; head and tail are computed from the entry and exit triads of that window only, with one bit of boundary context each.

Axiom 04.2 - Receipt Preservation: a failed join emits a receipt naming its head, tail, circles, arc type, and matching tail; the input bits are never modified (the adapter is read-only).

Axiom 04.3 - Boundary Positivity: a crossing arc is not an error — it is a typed constraint (the matching tail) that the next legal route must satisfy. A repair routes; it does not delete.

Axiom 04.4 - Analog Equivalence: a boundary repair has a physical workbook analogue (two tokens on a circle strip; a crossing pair names the token the tail must become to close).

## Lemmas

Lemma 04.1 - Arc closure decidability: for any window of >= 3 bits, the adapter deterministically computes head, tail, their circles, and `matched`; the arc is closed iff `head_circle == tail_circle`. (`binary_boundary_adapter.py :: adapt`.)

Lemma 04.2 - Repair as named constraint: a crossing arc has a unique matching tail (the partner of the head's anneal target on its circle); supplying that tail converts the crossing arc into a closed arc. (`binary_boundary_adapter.py :: _partner`, `matching_tail`.)

Lemma 04.3 - Layered transport with explicit boundaries: boundary repairs compose along exactly four transport layers — `LCR_TO_D4_AXIS_SHEET` (demonstrated, witness `verify_chart_codec_d4`), `D4_TO_J3O_DIAGONAL_CARRIER` (demonstrated, witness `verify_j3o_axioms`), `J3O_TO_G2_F4_T5A_ROUTE` (bounded_local, witness `verify_conjugate_triple`), and `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` (registered_landing_forms). Each layer's failure condition is named, and lifts beyond the demonstrated layers stay visibly open. (`transport_obligations.py :: transport_obligations`, `verify_transport_obligations`.)

## Formalism / Calculus Sketch

A repair state is `B = (head, tail, head_circle, tail_circle, matched, matching_tail, layer)`. The repair operation:

```text
adapt(window):
    head  = anneal(entry triad)   # nearest Lie-conjugate rest state
    tail  = anneal(exit triad)
    matched = (circle(head) == circle(tail))
    if matched:  arc = closed_arc;   matching_tail = tail
    else:        arc = crossing_arc; matching_tail = partner(head on its circle)
    # input bits are never modified

repair(crossing_arc) -> typed constraint "next route must land tail on circle(head)"
```

Repairs compose along the transport ledger, each layer carrying a classification and a proof boundary:

```text
layer                                  classification             witness
LCR_TO_D4_AXIS_SHEET                    demonstrated               verify_chart_codec_d4
D4_TO_J3O_DIAGONAL_CARRIER              demonstrated               verify_j3o_axioms
J3O_TO_G2_F4_T5A_ROUTE                  bounded_local              verify_conjugate_triple
EXCEPTIONAL_ROUTE_TO_NIEMEIER_FORMS     registered_landing_forms   ledger registry
```

The frustrated bond `C=1, R=0` (Paper 02's correction firing) is precisely the boundary defect a repair must route past: the carry that only Rule 30's `NOT(L)` clause resolves. Tool binding:

```text
cqe_engine  (boundary repair: binary_boundary_adapter, oloid_dual_path,
             transport_obligations)
```

## Proof Tree

```text
claim (failed join -> typed constraint for next legal route)
-> read window, anneal entry/exit to head/tail rest states     (Lemma 04.1)
-> classify arc: closed (same circle) or crossing               (Lemma 04.1)
-> crossing arc emits matching_tail (the repair constraint)      (Lemma 04.2)
-> repair routes along the next legal transport layer            (Lemma 04.3)
   |- demonstrated layers carry exact witnesses
   |- bounded / registered layers stay visibly open
-> tie to correction surface: frustrated bond C=1,R=0 (Paper 02)
-> worked example (boundary adapt of a real bit window)
-> workbook analogue (circle-strip token repair)
-> receipt (head/tail/arc/matching_tail logged, input unmodified)
-> proof / obligation split
```

## Practical Solved Example

**Domain:** boundary repair of an arbitrary 16-bit window (e.g. the tail bits of a hex payload such as `deadbeefcafe1234`, the adapter's own CLI example), read unaltered.

**Procedure:** call `adapt(data, window=16)`; record the head and tail rest states, their circles, the arc type, and — if crossing — the `matching_tail`. Then run `verify_transport_obligations(max_depth=...)` to confirm the four-layer ledger is well-formed and the demonstrated local witnesses pass.

**Solved Output:** the adapter returns a head and tail Lie-conjugate state with circle labels `F`/`P`; the arc is reported `closed_arc` when the circles match and `crossing_arc` otherwise, with `matching_tail` naming the rest state needed to close — the repair constraint, with the input bits unchanged. `verify_transport_obligations` returns `status: pass_with_open_lifts`: the two demonstrated layers pass their witnesses (`verify_chart_codec_d4`, `verify_j3o_axioms`), while the `bounded_local` and `registered_landing_forms` layers are carried as open lifts with named proof boundaries. The example is solved because the repair constraint and the layer classification reproduce identically from the formal operation, the `cqe_engine` adapter, and the analog circle-strip sheet.

## Tool Binding

- Module: `cqe_engine` (re-exporting `binary_boundary_adapter`, `oloid_dual_path`, `transport_obligations`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: `adapt(window)` on a >= 3-bit input returns head, tail, arc type, and a matching tail for any crossing arc, leaving input bits unmodified; `verify_transport_obligations()` returns `pass_with_open_lifts` with all rows carrying the required fields and valid classifications.

## Analog Workbook Sheet

- Start with grey loose substrate; draw the two carrier circles `F` and `P`.
- Place the head token on its circle (the rest state the window came from) and the tail token on its circle (where it is heading).
- If both tokens are on the same circle, bind a closed-arc string between them (white follow-up).
- If they are on different circles, write the matching-tail token name beside the tail — the repair constraint — and mark a black follow-up (crossing arc, kept as routing data, input unchanged).
- Bind the sheet into the matching color notebook.

## IRL Citation Anchors

- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: the repair receipt as a derivation record with provenance.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: failed join treated as channel information, the constraint as a corrective symbol.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30's `C=1,R=0` frustrated bond as the canonical boundary defect.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: oloid / octonionic carrier background for the dual-path routing target.

## Open Obligations

- The `J3O_TO_G2_F4_T5A_ROUTE` layer is classified `bounded_local`: a local oracle-backed classifier exists, but it does not derive the bit from depth `N`. Promotion to a depth-only route is an obligation (`transport_obligations.py`, proof_boundary field).
- The `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` layer is `registered_landing_forms`: the rank-24 targets are registered, but no proved fingerprint-to-landing map exists (`verify_niemeier_landing_registry`, `fingerprint_map_proved: False`).
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add a falsifier: a window the adapter must refuse (fewer than 3 bits) or a matching tail that fails to close the arc when supplied, which the tool must reject.

## Back-Propagation Targets

- Paper 02 (Correction Surface) supplies the frustrated-bond defect that boundary repair routes past.
- Paper 05 (Oloid Path Carrier) receives the crossing-arc routing as the dual-path selection (podal / antipodal / shared contact edge).
- Paper 06 (Causal Code) receives each repair as a typed `obligates`/`transports` edge with the matching tail as its constraint and the layer witness as its receipt.
- Paper 00 receives the ErrorWall discipline as the Boundary Positivity axiom's operational form.
