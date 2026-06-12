# Paper 06 - Causal Code

## Status

Foundational paper. Casts every dependency between objects, proofs, tools, and papers as a typed causal edge with a receipt. Proof-facing; this is the corpus's dependency-graph layer.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

We define the corpus's *causal code*: the discipline of representing every dependency — between mathematical objects, proofs, executable tools, and papers — as a typed directed edge that carries a receipt. The edge types are `proves`, `uses`, `refines`, `obligates`, and `transports`. Each edge names its source, its target, the operator that produced it, and a deterministic witness: a verifier function, a content hash, or an explicit proof boundary. We ground this in two real mechanisms. First, the terminal composition tree (`build_terminal_composition_tree`) generates a canonical directed graph of typed action edges (`add_component`) and involution generators over an immutable seed ledger, attaching a SHA-256 content hash and a residue trace to every state and edge — a worked example of a fully typed causal graph with receipts. Second, the contributions registry persists every new fact as a row `(kind, key, value, provenance, validated_by, rationale, content_hash)`, admitting it only through an `F_2`-deterministic validation gate that records the witness identity. Together with the transport-obligation ledger's four layers (each carrying a classification and a named witness), these give every dependency in the corpus a type and a replayable receipt, so the corpus is itself a typed causal graph rather than a flat pile of claims.

## Central Thesis

Cast every dependency between objects, proofs, tools, and papers as a typed causal edge: `proves`, `uses`, `refines`, `obligates`, `transports`, each carrying a source, a target, an operator, and a deterministic receipt.

## Scope Boundary

This paper claims the edge-typing discipline and grounds it in the terminal composition tree, the contributions registry, and the transport-obligation ledger. It does not claim that the full corpus graph has been materialized end-to-end, nor that every registered landing form has a proved fingerprint map (it does not). Edges whose witness is a bounded-local classifier or a registered-only target are typed `obligates`/`transports` with their proof boundary recorded, never promoted to `proves`. Excess interpretation is logged as obligation.

## Definitions

- **Causal edge**: a typed directed dependency `(source, target, type, operator, receipt)`.
- **Edge types**: `proves` (a proof or verifier establishes a target), `uses` (a target depends on a source object/tool), `refines` (a target sharpens a source claim), `obligates` (a target carries an open obligation from a source), `transports` (a target is a transported state of a source under a named map).
- **Receipt**: the deterministic witness attached to an edge — a verifier function name, a SHA-256 content hash, a residue trace, or an explicit proof boundary string.
- **Terminal composition tree**: a generated directed graph over the immutable seed ledger, with `add_component` action edges, involution-generator families, a residue trace, and a closure-residue status; each state and edge carries a SHA-256 `state_id`/`edge_id` (`terminal_tree.py :: build_terminal_composition_tree`).
- **Contribution row**: a persisted fact `(kind, key, value, provenance, validated_by, validation_rationale, validated_at, content_hash)`, admitted only via a validator gate (`contributions_registry.py`, `SCHEMA`).
- **Validation gate**: an `F_2`-deterministic check returning `(accepted, rationale)`; same input gives same decision (`contribution_validators.py`, e.g. `lucas_recurrence_validator`, `rule30_decomposition_validator`).
- **Transport layer**: a typed transport edge with a classification (`demonstrated`, `bounded_local`, `registered_landing_forms`, ...) and a named witness and proof boundary (`transport_obligations.py`).

## Axioms

Axiom 06.1 - Locality: every causal edge names a single source and a single target; composite dependencies are decomposed into local typed edges before being lifted.

Axiom 06.2 - Receipt Preservation: no edge is accepted without a deterministic receipt — a verifier name, a content hash, a residue trace, or an explicit proof boundary. The receipt is persisted with the edge.

Axiom 06.3 - Boundary Positivity: an `obligates` edge is a first-class dependency, not a defect; an open lift is recorded with its proof boundary and carried forward, never deleted.

Axiom 06.4 - Analog Exposure Equivalence: a causal edge has a physical workbook analogue (a string of a specific color binding a source token to a target token, tagged with its receipt).

## Lemmas

Lemma 06.1 - Typed graph generation with receipts: the terminal composition tree generates a canonical directed graph whose states and edges each carry a SHA-256 hash, whose action edges are typed `add_component` with an `operator` and a `residue_delta`, and whose closure residue is reported `residue_closes_by_required_index` or `residue_trace_unresolved`. The route is unique after component ordering and orbit quotient. (`terminal_tree.py :: build_terminal_composition_tree`, `terminal_tree_summary`.)

Lemma 06.2 - Gated provenance: a fact becomes a durable contribution row only after a validator gate accepts it; the gate is `F_2`-deterministic and its identity (`validated_by`) plus rationale are stored with the row under a `UNIQUE(kind, key_json)` constraint and a content hash. (`contributions_registry.py :: SCHEMA`; `contribution_validators.py :: install_default_validators` registering `f2_arf`, `lucas_recurrence`, `rule30_decomposition`, `f2_edge_glue`.)

Lemma 06.3 - Typed transport with explicit boundary: every transport edge carries a classification in `{demonstrated, bounded_local, bounded_external, registered_landing_forms, open}`, a named witness, and a proof boundary; the verifier returns `pass_with_open_lifts` precisely when the demonstrated witnesses pass while non-demonstrated lifts stay visibly open. (`transport_obligations.py :: transport_obligations`, `verify_transport_obligations`.)

## Formalism / Calculus Sketch

A causal edge and its receipt:

```text
edge = (source, target, type, operator, receipt)
type in {proves, uses, refines, obligates, transports}

receipt is one of:
   verifier_name        e.g. verify_n3_su3_closure_exact   (proves)
   content_hash         SHA-256 over canonical JSON payload (terminal tree)
   residue_trace        emergent_residue_from_component_action
   proof_boundary       explicit string for obligates/transports edges
```

Three real graph generators in the substrate:

```text
build_terminal_composition_tree(ledger, terminal_id)
   -> route states (SHA-256 state_id) + add_component edges (SHA-256 edge_id)
      + involution-generator families + residue trace + closure residue

contributions_registry.propose(...) -> validator gate -> durable row
   row = (kind, key, value, provenance, validated_by, rationale, hash)

verify_transport_obligations() -> typed transport layers
   each: classification + witness + proof_boundary
   status = pass_with_open_lifts
```

Tool binding:

```text
cqe_engine  (causal code: terminal_tree (build_terminal_composition_tree),
             contributions_registry, contribution_validators,
             transport_obligations)
```

## Proof Tree

```text
claim (every dependency is a typed causal edge with a receipt)
-> edge types {proves, uses, refines, obligates, transports}
-> typed graph generation with SHA-256 receipts                 (Lemma 06.1)
   |- add_component action edges + residue trace
   |- closure residue status (closes_by_required_index | unresolved)
-> gated provenance: validator must accept before durability     (Lemma 06.2)
   |- F_2-deterministic gate; validated_by + rationale persisted
-> typed transport with explicit proof boundary                  (Lemma 06.3)
   |- demonstrated witnesses pass; open lifts stay visible
-> worked example (terminal tree + transport ledger)
-> supplemental workbook analogue (colored receipt-tagged strings)
-> receipt (every edge carries verifier / hash / boundary)
-> proof result / audit residue split
```

## Practical Solved Example

**Domain:** the corpus's own dependency graph, instantiated on a terminal composition tree and the transport-obligation ledger.

**Procedure:** generate a terminal composition tree via `build_terminal_composition_tree(ledger, terminal_id)` for a registered rank-24 terminal and inspect its typed `add_component` edges, SHA-256 state/edge hashes, and closure-residue status; then run `verify_transport_obligations()` to read the four typed transport layers with their classifications and witnesses.

**Solved Output:** the composition tree returns `status: generated_canonical_composition_tree` (or `rootless_terminal_pending_import` for the Leech terminal), a `composition_route` of states each with a SHA-256 `state_id`, `action_edges` each typed `add_component` with an `operator` and `residue_delta`, an `involution_tree` of lifted source reflection generators, and a `closure_residue` reporting whether the residue closes by the required overlattice index. The transport verifier returns `status: pass_with_open_lifts` with `demonstrated_count` for the two demonstrated layers and `open_lift_count` for the bounded/registered layers, every row carrying the required fields and a valid classification. The example is solved because every dependency in the generated graph is typed and carries a receipt (a hash, a residue trace, or a named witness with a proof boundary), reproducible from the formal definitions, the `cqe_engine` generators, and the analog receipt-string sheet.

## Tool Binding

- Module: `cqe_engine` (re-exporting `terminal_tree`, `contributions_registry`, `contribution_validators`, `transport_obligations`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: `build_terminal_composition_tree` returns a route and action edges with SHA-256 ids and a closure-residue status; a proposed contribution is admitted only after a validator returns `(True, rationale)` and is persisted with `validated_by`; `verify_transport_obligations()` returns `pass_with_open_lifts`.

## Analog Workbook Sheet

- Start with grey loose substrate; lay one token per object, proof, tool, and paper.
- Bind each dependency with a colored string whose color encodes the edge type: `proves`, `uses`, `refines`, `obligates`, `transports`.
- Tag each string with its receipt: a verifier name, a content-hash fragment, or a proof-boundary note.
- White follow-up = a `proves` edge with a passing verifier; black follow-up = an `obligates`/`transports` edge with an open proof boundary, kept as a first-class dependency.
- Bind the receipt-tagged graph sheet into the matching color notebook.

## IRL Citation Anchors

- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: typed derivation edges, provenance, and derivation ledgers — the direct model for the causal code.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: each edge as a channel carrying a state from source to target with a receipt.
- [JupyterRepro] Jupyter Project documentation. URL: https://jupyter.org/documentation Use: reproducible, replayable computational receipts.
- [OEIS] On-Line Encyclopedia of Integer Sequences. URL: https://oeis.org/ Use: a content-addressed registry of facts admitted under identifying keys, analogue of the contributions registry.

## Open Obligations

- The full corpus dependency graph (every object, proof, tool, and paper as nodes with typed edges) is not materialized end-to-end in this submission; the terminal tree and transport ledger are worked instances, and the global graph is an obligation.
- The `registered_landing_forms` transport edges carry registered rank-24 targets with no proved fingerprint-to-landing map (`verify_niemeier_landing_registry`, `fingerprint_map_proved: False`); these stay typed `obligates`/`transports`, not `proves`.
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add a falsifier: a proposed contribution whose value disagrees with its validator's recomputation (e.g. a wrong Arf invariant or a Lucas term violating the Pascal recurrence), which the gate must reject.

## Back-Propagation Targets

- Paper 00 receives the causal-edge typing as the formal shape of every transport row in the contract.
- Papers 02-05 each contribute their verifier names as the receipts on their `proves` edges (`verify_rule90_linearization`, `verify_n3_su3_closure_exact`, `verify_j3o_axioms`, `verify_transport_obligations`, `verify_cayley_dickson_oloid_normal_form`, `verify_dual_path_oloid`).
- The contributions registry records every new fact a later paper depends on, gated by its validator.
- Paper 31 records how the presentation order of the corpus is itself a typed causal walk over these edges.
