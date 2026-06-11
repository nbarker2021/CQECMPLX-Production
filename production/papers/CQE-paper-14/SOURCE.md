# Paper 14 - GR Boundary-Repair Curvature

## Status

HORIZON paper. Frames curvature as a boundary-repair demand in the transport view. The substrate-side construction (boundary-repair as the obligation/correction operation, curved carriers via the oloid) is grounded in named modules and the corpus contract. Every General Relativity claim is a candidate interpretation carried as an explicit obligation with a falsifier. As in the umbrella's Discussion, this paper does not extend physics; it applies the substrate and is honest about the gap.

## Abstract

In the transport contract, a route that fails to close locally is not deleted: its unresolved residue is logged as an obligation and becomes a *boundary-repair* demand — the explicit work needed to reconcile a local readout with its surrounding frame (Axiom 00.3; `transport_obligations.py`). This paper takes the candidate interpretation that *curvature*, in the General Relativity sense, plays the same role: a measure of how much a flat (geodesic, parallel-transport) closure must be repaired to match the actual neighborhood. We make the structural side precise and the physical side honest. On the substrate side: the corpus already carries a "boundary-repair" operation in the Paper 04 frame-inversion / correction apparatus and a *curved carrier* in the Cayley-Dickson oloid normal form (`cayley_dickson_oloid.py`), whose `N`-with-antipode-`-N`, `1+8+8+1` rolling structure provides a non-flat path on which the three `shell=2` dyads roll (`oloid_dual_path.py`). The transport-obligation ledger gives a typed `demonstrated / bounded_local / open` grading of repair demands. On the physics side: the identification "curvature = boundary-repair demand" and any connection to the Einstein field equations are candidate hypotheses, listed as obligations with falsifiers, not derived. The contribution is a disciplined framing, not a claim about gravity.

## Central Thesis

Frame curvature as a boundary-repair demand in the transport view.

## Scope Boundary

This paper claims only: (1) that the transport contract already encodes a boundary-repair operation (the residue-to-obligation map, Axiom 00.3, `transport_obligations.py`); (2) that the substrate has explicit *curved carriers* (the oloid normal form and dual-path roller) on which local states are transported; (3) that "curvature as repair demand" is a coherent re-reading of (1) and (2). It does NOT claim to derive the Einstein field equations, the Riemann or Ricci tensor, geodesic deviation, or any measured gravitational quantity. Every physical statement here is a candidate hypothesis with a named falsifier. Treating any of them as proven physics is out of scope.

## Definitions

- **Boundary-repair demand**: the unresolved residue `O` of a local transform that fails to close in its frame; the explicit work logged so the residue is reconciled, not erased (Axiom 00.3; receipt residue, Paper 00).
- **Flat closure**: a route whose `shell=2` transition closes under the `n=3` `SU(3)` Weyl identity with residual `0` (`f4_action.py`); the substrate's analog of zero-curvature parallel transport.
- **Repair magnitude**: the number / size of obligation rows a route accrues; the substrate's scalar analog of a curvature measure (NOT a metric tensor).
- **Curved carrier (oloid)**: the Cayley-Dickson oloid normal form, an `N`/`-N` antipodal, `1+8+8+1`-weighted non-flat carrier on which states roll (`cayley_dickson_oloid.py`, `oloid_dual_path.py`).
- **Geodesic analog**: the podal path of the dual-path oloid (`dyad_0`), read as the "straight" reference against which the antipodal and contact-edge dyads bend.
- **Curvature (physical, OBLIGATION)**: the GR sense — the failure of parallel transport to return a vector unchanged around a loop; here a candidate interpretation only.

## Axioms

Axiom 14.1 - Locality: a repair demand must be readable from a local `(L,C,R)` window before any frame-scale interpretation (Axiom 00.1).

Axiom 14.2 - Receipt Preservation: every repair logs its input residue, the repair applied, and the remaining residue (Axiom 00.2).

Axiom 14.3 - Boundary Positivity: a route that fails to close flat is data; its residue IS the repair demand, never a silent loss (Axiom 00.3 — this paper's load-bearing axiom).

Axiom 14.4 - Analog Equivalence: the repair demand has a workbook analogue (a string that must be re-tensioned across a fold).

## Lemmas

Lemma 14.1 - Repair is the contract's residue map. The transport ledger grades each layer as `demonstrated`, `bounded_local`, `bounded_external`, `registered_landing_forms`, or `open`, with an explicit `proof_boundary` per row (`transport_obligations.py`, `CLASSIFICATIONS`). The repair demand of a route is exactly its non-`demonstrated` residue. Basis: `transport_obligations()` returns four typed layers, each with a `failure_condition` and `proof_boundary`.

Lemma 14.2 - Flat closure has zero repair. A route whose `shell=2` block equals `(1/3)(T_12+T_13+T_23)` has residual squared `0` and accrues no obligation row at the closure layer (`f4_action.py`, `IDENTITY_PAPER` T4/T5). This is the substrate's zero-curvature reference.

Lemma 14.3 - Curved carriers exist and carry an `S_3` structure. The oloid normal form is non-flat (`1+8+8+1` antipodal rolling, `cayley_dickson_oloid.py`); its three dyads (podal, antipodal, contact-edge) carry the same `S_3 = W(SU(3))` action as the three trace-2 idempotents (`oloid_dual_path.py` docstring; `IDENTITY_PAPER` T4). The carrier is explicitly documented as a normal-form generator, not a Rule 30 predictor (module honesty field).

## Formalism / Calculus Sketch

The repair view reads a local route, attempts flat closure, and measures the residue:

```text
repair(route):
  attempt flat closure (n=3 SU(3) Weyl identity)   [Lemma 14.2]
  if residual == 0:   repair_demand = 0             [flat / zero-curvature analog]
  else:               residue -> obligation row     [Axiom 14.3, Lemma 14.1]
                      repair_demand = ledger grade   [demonstrated..open]
  roll the unresolved state on the oloid carrier     [Lemma 14.3]
  emit receipt(route, repair_demand, residue)
---- physics layer (OBLIGATION, off-shell) ----
candidate: repair_demand  <->  curvature scalar
candidate: oloid bend     <->  geodesic deviation
candidate: ledger closure <->  Einstein field eq. balance
NONE of these is derived; each carries a falsifier below.
```

The intended reading: a "flat" computation (one that closes by transport) needs no repair, like a region of zero curvature; a computation whose local readouts do not match their frame accrues repair demands, the candidate analog of curvature. Tool binding:

```text
cqe_engine  (transport_obligations: layers, CLASSIFICATIONS, proof_boundary;
             cayley_dickson_oloid: normal_form, 1+8+8+1, antipode;
             oloid_dual_path: dyad_index_at_depth, three-dyad S_3 roll;
             f4_action: flat-closure reference)
```

## Proof Tree

```text
claim (curvature := boundary-repair demand, transport view)
-> Axiom 14.3: failed-flat-closure residue = repair demand
-> Lemma 14.1: repair demand = ledger's non-demonstrated residue
-> Lemma 14.2: flat closure (n=3 Weyl) => zero repair (zero-curvature ref)
-> Lemma 14.3: oloid curved carrier exists, S_3-structured
-> repair magnitude = ledger grade (scalar analog)
-> physical curvature / Einstein field eq. => OBLIGATION + falsifier
-> worked example (a closing route vs an opening route)
-> workbook analogue (re-tensioned string across a fold)
-> receipt + obligation split
```

## Practical Solved Example

**Domain:** two routes in the substrate — a silent-boundary ECA (flat closer) versus Rule 30 (opener) — read as zero-repair versus repair-demanding.

**Procedure:** for each route, attempt flat closure via `f4_action`'s `n=3` decomposition; record whether residual is `0`; for the opener, roll the unresolved `shell=2` state on the dual-path oloid and read the dyad index at a sample depth `N` via `dyad_index_at_depth(N, level)`; grade the residue via `transport_obligations()`.

**Solved Output:** the silent-boundary closer has residual `0` and repair demand `0` (Lemma 14.2 — the substrate's flat region). Rule 30 opens: its `shell=2` block does not equal `(1/3)(T_12+T_13+T_23)`, so it accrues a residue, which the ledger grades (the closure-to-Niemeier landing layer is `registered_landing_forms`, the conjugate route is `bounded_local`, the cold-start extraction is `open`). The oloid carries the unresolved state on its three `S_3` dyads. The example is solved at the substrate layer: the repair demand reproduces from the formal residue map, the `cqe_engine` ledger, and the workbook re-tension sheet. The physical reading (this repair demand "is" spacetime curvature) is NOT solved — it is the obligation below.

## Tool Binding

- Module: `cqe_engine` (`transport_obligations`, `cayley_dickson_oloid`, `oloid_dual_path`, `f4_action`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv` (the GR obligations live here, marked `candidate`/`open`).
- Minimum test: confirm `transport_obligations()` returns typed layers with `proof_boundary` fields; confirm a flat closer has residual `0` (zero repair); confirm Rule 30 accrues a residue; confirm `cayley_dickson_oloid` honesty field disclaims bit-prediction; confirm at least one GR obligation row is present and NOT marked proven.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a strip and fold it (introduce a physical bend = the oloid carrier).
- Place the local `(L,C,R)` tokens along the strip; tension a string along the podal (geodesic) reference.
- If the string returns to its start tension after crossing the fold, repair demand = 0 (flat). If it must be re-tensioned, the re-tension amount is the repair demand (curvature analog).
- White follow-up = a route that closes with no re-tension; black follow-up = the re-tension residue AND every physical (GR) claim — both bound as obligation cards.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Einstein1915] A. Einstein, Die Feldgleichungen der Gravitation (the field equations), Sitzungsber. Preuss. Akad. Wiss. Use: GR curvature as BACKGROUND ONLY; not derived here.
- [MTW1973] Misner, Thorne, Wheeler, Gravitation. Use: parallel transport / geodesic deviation as the background notion the repair-demand analog gestures at.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: the octonionic / oloid carrier structure.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: the obligation/repair ledger as a derivation record.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 as the registered opener.

## Open Obligations

- "Curvature = boundary-repair demand" is a candidate interpretation. Falsifier: a physical curvature scenario with zero repair demand in the substrate, or a high-repair route with zero physical curvature, would break the analogy. This identification is OPEN.
- No connection to the Einstein field equations is derived; relating the ledger's closure balance to `G_uv = 8 pi T_uv` is OPEN and may be false.
- The oloid carrier is a normal-form generator (`cayley_dickson_oloid.py` honesty field); it does not predict a Rule 30 bit, and any geometric-deviation-to-physics map is OPEN (the dual-path `O(1)` per-dyad head lookup is itself open, `oloid_dual_path.py`).
- This paper is HORIZON: it asserts no physical result. All physics rows in the ledger are `candidate`/`open`.

## Back-Propagation Targets

- Paper 00 receives the repair-demand reading of the residue-to-obligation map (Axiom 00.3).
- Paper 04 (frame inversion / correction) receives the boundary-repair operation interpretation.
- Paper 13 receives the discipline (physics claims are obligations with falsifiers).
- Paper 15 (horizon) shares the same obligation discipline.
- The analog workbook manual receives the re-tensioned-string-across-a-fold rule.
