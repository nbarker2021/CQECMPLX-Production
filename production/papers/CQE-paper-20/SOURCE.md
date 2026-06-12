# Paper 20 - Layer-2 Synthesis Ledger

## Status

Transport / aggregation paper. Defines the Layer-2 ledger that aggregates prediction and theory-admission results into typed routes — solved, open, failed, and transported — backed by the executable `lattice_forge.ledger` substrate, the `transport_obligations` layer, and the `contributions_registry` governance gate. Proof-facing: the ledger machinery is executable; the aggregate verdicts it carries inherit each row's own status.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

This paper specifies the synthesis ledger that sits one layer above the individual results: it aggregates the outputs of the admission papers (theory-admission, Paper 11) and the prediction papers (Paper 12) into a single auditable record of typed routes. Each route is classified into one of the corpus's standing buckets — `demonstrated` (solved), `open`, `bounded_local` / `registered_landing_forms` (transported but not closed), and `forbidden` / failed — so that no result is silently promoted and no obstruction is silently dropped. Three real substrates back the ledger. (1) The SQLite morphism/admissibility ledger (`lattice_forge.ledger.Ledger`) holds objects, exact root vectors, admissibility edges, terminal 24D forms, glue requirements, and closure obstructions, with `Ledger.can_close` answering reachability queries (`yes`, `yes_with_template_glue`, `no`, `unknown`) and `Ledger.verify` checking seeded invariants (e.g. `E_8` = 240 roots, all 24 Niemeier terminals at rank 24, Leech root-rank 0). (2) The transport-obligation layer (`transport_obligations`) declares the four named transport edges with explicit classifications and proof boundaries, verified by `verify_transport_obligations` with overall status `pass_with_open_lifts`. (3) The contributions registry (`contributions_registry.Registry`) is the governance gate: every new fact must pass a named deterministic validator before becoming durable, with `(validated_by, rationale, timestamp)` recorded. The ledger is the corpus's honest scoreboard: it reports what is solved, what is open, what failed, and what was transported without closure.

## Central Thesis

Aggregate prediction and theory-admission results into a ledger of solved, open, failed, and transported routes.

## Scope Boundary

This paper claims the ledger's structure, query surface, and governance discipline exactly as `lattice_forge.ledger`, `transport_obligations`, and `contributions_registry` implement them. It does NOT itself prove any aggregated result; each ledger row inherits the status of its source paper. An `unknown` reachability answer or a `pass_with_open_lifts` verdict is reported as-is, never upgraded. The ledger aggregates Paper 11 (admission) and Paper 12 (prediction); it does not re-derive them.

## Definitions

- **Route**: a typed ledger row carrying a claim, source object/target, transform, preserved quantity, failure condition, witness, and classification.
- **Classification (route status)**: one of `demonstrated`, `bounded_local`, `bounded_external`, `registered_landing_forms`, `open` (from `transport_obligations.CLASSIFICATIONS`); plus admissibility-edge statuses `legal`, `forbidden`, and query verdicts `yes`, `yes_with_template_glue`, `no`, `unknown`.
- **Admissibility edge**: a recorded `source -> target` transition with a status; the ledger's reachability graph (`Ledger.edges_from`, `Ledger.descendants`, `Ledger.can_close`).
- **Terminal form**: a registered rank-24 Niemeier or Leech destination (`terminal_24d_forms`), with discriminant profile and composition tree.
- **Closure obstruction**: a recorded reason a route does not close (`closure_obstruction_registry`).
- **Governance gate**: the `contributions_registry.Registry.propose` path — a named validator runs a deterministic boolean check and records `(validated_by, rationale, validated_at)` before any new fact is committed.
- **Receipt / Transport row / Supplemental workbook sheet / Tool binding**: as fixed in Paper 00.

## Axioms

Axiom 20.1 - Locality: a route enters the ledger only with a named local witness (a verifier function or seeded invariant), never as a bare assertion.

Axiom 20.2 - Receipt Preservation: every committed row records its validator, rationale, and timestamp; every transport edge records its proof boundary.

Axiom 20.3 - Boundary Positivity: `open`, `unknown`, `forbidden`, and `pass_with_open_lifts` are first-class ledger states — failures and obstructions are stored, not discarded.

Axiom 20.4 - Analog Exposure Equivalence: the ledger has a physical workbook analogue (a four-column board: solved / open / failed / transported, bound by route string).

## Lemmas

Lemma 20.1 - Seeded-invariant integrity. `Ledger.verify` checks the seeded exact root counts (`A1:2, A2:6, D4:24, G2:12, F4:48, E6:72, E7:126, E8:240`) and that every rootful terminal has rank 24 while `Niemeier:Leech` has root-rank 0; it returns `status = "pass"` only when all checks and the 30+ registry tables are populated. (Source: `ledger.ledger.Ledger.verify`.)

Lemma 20.2 - Four-edge transport with open lifts. `transport_obligations` declares exactly four transport edges (LCR->D4, D4->J3(O), J3(O)->G2/F4/T5A, exceptional->Niemeier) with classifications `demonstrated, demonstrated, bounded_local, registered_landing_forms`; `verify_transport_obligations` returns `status = "pass_with_open_lifts"` with `open_lift_count = 2`. (Source: `transport_obligations.verify_transport_obligations`.)

Lemma 20.3 - Gated durability. A new fact becomes a durable contribution only via `Registry.propose(kind, key, value, provenance, validator_name)`, where the named validator returns `(accepted, rationale)`; rejected proposals are recorded with their rejection reason. (Source: `contributions_registry.Registry`.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)` (Paper 00). The ledger is a typed multiset of routes plus a reachability graph and a governance gate:

```text
route = {claim, source, target, transform, preserved, failure_condition,
         witness, classification, proof_boundary}
classification in {demonstrated, bounded_local, bounded_external,
                   registered_landing_forms, open}
reachability: can_close(source, target) ->
   {yes, yes_with_template_glue, no, unknown}
commit(fact): propose(kind,key,value,provenance,validator) ->
   validator(kind,key,value) = (accepted, rationale)
   accepted -> durable row with (validated_by, rationale, validated_at)
   rejected -> recorded with rejection_reason
aggregate verdict = multiset of source-paper statuses; no upgrade
```

Tool binding:

```text
cqe_engine  (lattice_forge.ledger: Ledger (open/create/can_close/verify/summary),
             ledger.build (NIEMEIER_FORMS, build_seed_database), ledger.nsl,
             ledger.exact, ledger.schema;
             lattice_forge.transport_obligations: transport_obligations,
             verify_transport_obligations;
             lattice_forge.contributions_registry: Registry)
```

## Proof Tree

```text
claim (Layer-2 ledger aggregates solved/open/failed/transported routes)
-> local witness per row (verifier or seeded invariant)
-> admissibility graph (edges, descendants, can_close) [Ledger]
-> seeded-invariant integrity (root counts, terminal ranks) [Lemma 20.1]
-> four transport edges, pass_with_open_lifts [Lemma 20.2]
-> governance gate (validator + rationale + timestamp) [Lemma 20.3]
-> aggregate of Paper 11 (admission) + Paper 12 (prediction) statuses
-> worked example (verify + can_close + transport verdict)
-> supplemental workbook analogue (four-column board)
-> receipt
-> per-row proof / open / failed / transported (no silent upgrade)
```

## Practical Solved Example

**Domain:** a Layer-2 aggregation run over the seeded morphism ledger and the transport-obligation layer.

**Procedure:** open the seed database (`Ledger.open`), run `Ledger.verify()` for invariant integrity, run a representative `Ledger.can_close(source, target)` query, and run `verify_transport_obligations()` for the transport verdict; record each result as a typed route.

**Solved Output:** with real numbers and statuses from the source:
- Invariant integrity: `Ledger.verify` confirms `E_8` = 240 roots, `F_4` = 48, `E_6` = 72, `E_7` = 126, `D4` = 24, and that all 24 terminal forms carry a discriminant profile, returning `status = "pass"` when the 30+ registry tables are populated.
- Reachability: `can_close` returns one of `{yes, yes_with_template_glue, no, unknown}`; a seeded legal path returns `yes` (or `yes_with_template_glue` when glue requirements attach), and an unseeded path returns `unknown` — recorded as an `open` route, not a failure.
- Transport verdict: `verify_transport_obligations` returns `status = "pass_with_open_lifts"`, `row_count = 4`, `demonstrated_count = 2`, `open_lift_count = 2` — two demonstrated edges (LCR->D4, D4->J3(O)) and two open lifts (J3(O)->G2/F4/T5A as `bounded_local`, exceptional->Niemeier as `registered_landing_forms`).

The example is solved (as an aggregation) because the four-bucket scoreboard reproduces from the formal definition, the `lattice_forge.ledger` / `transport_obligations` verifiers, and the workbook four-column board; no row is upgraded beyond its source status.

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.ledger`, `lattice_forge.transport_obligations`, `lattice_forge.contributions_registry`).
- Functions: `Ledger.open` / `Ledger.create` / `Ledger.can_close` / `Ledger.verify` / `Ledger.summary` / `Ledger.future_cone`; `transport_obligations`, `verify_transport_obligations`; `Registry.propose` / `Registry.lookup` / `Registry.all_entries` / `Registry.stats`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run `Ledger.verify` and confirm `status == "pass"`; run `verify_transport_obligations` and confirm `status == "pass_with_open_lifts"`; emit at least one solved route, one open route, and one transported (open-lift) route.

## Analog Workbook Sheet

- Start with grey loose substrate.
- Lay a four-column board: SOLVED (white), OPEN (black), FAILED (black with cross), TRANSPORTED (half white / half black).
- Place a `C`-tagged route card in the column matching its classification; the `C` token marks the witness (verifier or seeded invariant).
- Use string to bind each route from its source paper card (Paper 11 admission or Paper 12 prediction) to its bucket.
- White follow-up = a `demonstrated` route; black follow-up = an `open` / `unknown` / `forbidden` route; half-and-half = a `bounded_local` or `registered_landing_forms` transport.
- Bind the finished board into the matching color notebook.

## IRL Citation Anchors

- [W3C_PROV] W3C PROV Overview / PROV-DM provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: provenance, derivation ledgers, validator/rationale records.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: the ledger as a record of state transmission with accounted residue.
- [Conway1999] J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups (3rd ed.), Springer. Use: the seeded root systems and Niemeier terminal forms the ledger indexes.
- [SQLite] SQLite documentation. URL: https://www.sqlite.org/docs.html Use: the durable, queryable backing store for the ledger and contributions registry.

## Open Obligations

- **Open lifts (Lemma 20.2):** `verify_transport_obligations` carries `open_lift_count = 2` — the `J3(O) -> G2/F4/T5A` route is `bounded_local` (local classifier exists but does not derive the bit from depth `N`) and the `exceptional -> Niemeier` route is `registered_landing_forms` (registered targets, no proved fingerprint-to-landing map). Carried open.
- **`unknown` reachability rows:** any `can_close` answer of `unknown` ("no seeded admissibility path found") is a standing obligation to seed or refute that edge.
- **Closure obstructions:** rows in `closure_obstruction_registry` are retained failures; each requires a named next step before any upgrade.
- Replace citation anchors with final bibliography entries; add a falsifier the gate must reject (a proposed contribution whose validator returns `False`, recorded with its rejection reason).

## Back-Propagation Targets

- Paper 00 receives the "route classification" and "governance gate" contract terms.
- Paper 11 (admission) and Paper 12 (prediction) feed their per-result statuses into this ledger; their obligations appear here as `open` rows.
- Paper 17 contributes its verified rungs (solved) and the Leech/`W(E_8)` obligations (open) as ledger rows.
- Paper 18 contributes O1' and the SPINOR/correction-class obligations; Paper 19 contributes the retained-face rows.
- The analog workbook manual receives the four-column board rule.
- Paper 31 records how the ledger's solved/open/failed/transported partition mirrors the corpus's own white/black follow-up discipline.
