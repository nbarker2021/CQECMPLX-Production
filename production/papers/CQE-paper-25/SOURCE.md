# Paper 25 - Energetic Traversal Maps

## Status

Applied / horizon layer. Adds an energy-and-traversal ledger to the transforms used across the corpus (cross-language, figure, material, and fold transports of Papers 18-24). The provable content is the NSL conservation accounting (`ledger/nsl.py`) and the bounded transport-obligation layer (`transport_obligations.py`); the "energy" is the analog-math conservation quantity, not a physical joule count unless a domain calibrates it.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

Every transport in the corpus moves a registered state from a source object to a target object. This paper attaches an *energy and traversal ledger* to each such move so that a transport is accepted only if its boundary cost is accounted for. The load-bearing object is the Noether-Shannon-Landauer boundary term `NSLTerm` of `ledger/nsl.py`, whose conservation reading is `Theta = alpha*N + beta*S + gamma*L - absorption <= 0` (the unit-agnostic form; the Morphonics functional writes it as `Theta(phi) = wN*N + wS*S + wL*L + wG*G + wO*O`). Here `N` is the Noether / conservation mismatch, `S` the Shannon / information mismatch, `L` the Landauer / irreversible-execution cost, `G` the geometric glue mismatch, and `O` the obstruction penalty. A traversal map is the sequence of transports along a path, and its ledger is the running sum of these boundary terms, exactly the bounded four-layer transport ledger of `transport_obligations.py`. The "energy" weight per chart state is read from the corpus's own VOA weight `voa_weight` (the seed partition `Z(q) = 2q^0 + 6q^5`: vacua cost 0, excited states cost 5). The contribution is the ledger discipline: `DeltaPhi = DeltaN + DeltaI + DeltaL <= 0` over a traversal is the acceptance gate, and any traversal whose ledger does not close is carried as an open obligation with its boundary residue logged, not erased.

## Central Thesis

Add energy and traversal ledgers to cross-language, figure, material, and fold transformations.

## Scope Boundary

This paper claims (i) a typed energy ledger per transport built from the `NSLTerm` boundary terms, (ii) a traversal ledger that sums them along a path and applies the `Theta <= 0` acceptance gate, and (iii) that the four corpus transport layers of `transport_obligations.py` are the canonical traversal spine. It does NOT claim that the corpus energy maps to physical joules, that any specific transform is thermodynamically optimal, or that `Theta` subsumes the named physical laws (the Morphonics model itself tags that subsumption claim `OVERCLAIM`). Calibration of units is an obligation. Excess interpretation is logged, not promoted.

## Definitions

- **C (active transport)**: the transport currently being weighed; its center is the preserved invariant the transform claims to carry.
- **L / R (cost boundaries)**: the two opposed boundary readouts of a transport - what is preserved (`L`) versus what is lost / residual (`R`); the asymmetry is the cost.
- **NSL boundary term**: `NSLTerm(noether_residue, shannon_residue, landauer_cost, absorption_capacity, alpha, beta, gamma)` with `theta = alpha*N + beta*S + gamma*L - absorption` and `closes_internally = (theta <= 0)` (`ledger/nsl.py`).
- **Energy ledger**: the per-transport record of its NSL term and `theta`.
- **Traversal map**: an ordered path of transports; its ledger is the running sum of NSL terms.
- **Conservation gate (NSL)**: a traversal is accepted iff `DeltaPhi = DeltaN + DeltaI + DeltaL <= 0` (the corpus conservation law, equivalently `Theta <= 0`).
- **voa_weight**: the corpus's intrinsic per-state weight (`centroid_voa.voa_weight`), seed partition `Z(q) = 2q^0 + 6q^5`; used as the analog energy of a chart state.
- **Transport row / Receipt / Supplemental workbook sheet / Tool binding**: as defined in Paper 00.

## Axioms

Axiom 25.1 - Locality: a traversal cost is admissible only if each step is weighed through a single local transport `(L, C, R)` before the path total is asserted.

Axiom 25.2 - Receipt Preservation: no transport is accepted unless its NSL term, `theta`, and boundary residue can be logged and replayed.

Axiom 25.3 - Boundary Positivity: a non-closing transport (`theta > 0`) is data - it becomes an obligation with its residue recorded, never a silent deletion.

Axiom 25.4 - Analog Exposure Equivalence: every accepted traversal has a physical workbook analogue (a weighted bead string whose bead sizes are the step costs).

Axiom 25.5 - Unit Honesty: the NSL terms are unit-agnostic; a physical-energy reading requires a calibration obligation and is never promoted from the analog ledger alone.

## Lemmas

Lemma 25.1 - A transport that preserves its center `C` and records its `L/R` (preserved-vs-residual) asymmetry can be transported into the energy ledger without erasing the unaccounted residue; the residue enters `O`, never deletion. (Basis: `NSLTerm` carries `noether_residue`, `shannon_residue`, and `landauer_cost` explicitly; `morphonics` `RESIDUE_UNACCOUNTED` is a failure label.)

Lemma 25.2 - A tool-emitted NSL ledger row and a workbook weighted-bead string that encode the same step costs and closure status are equivalent receipts at different media layers. (Basis: Lemma 00.2.)

Lemma 25.3 - Traversal additivity: along a path, `Theta_path = sum_i Theta_i` when terms share units (or after weights normalize them), so the conservation gate `Theta_path <= 0` is the sum of step gates. The intrinsic per-state cost of a chart state is `voa_weight`, with vacua at 0 and excited states at 5 (`Z(q) = 2q^0 + 6q^5`); this gives every chart state a default analog energy before domain calibration. (Basis: `NSLTerm.theta` is linear in the residues; `centroid_voa.verify_voa_sector_decomposition`.)

## Formalism / Calculus Sketch

A transport state is `P = (C, L, R, B, T, O)`. Each transport `T` emits an NSL term; a traversal sums them:

```text
transport_i: T_i(P) -> P'
NSLTerm_i = (N_i, S_i, L_i, absorption_i)   # theta_i = alpha*N + beta*S + gamma*L - absorption
accept_i iff theta_i <= 0  (else log obligation with residue)
traversal Theta = sum_i theta_i
DeltaPhi = DeltaN + DeltaI + DeltaL <= 0     # NSL conservation gate over the path
default per-state cost = voa_weight(state)   # Z(q) = 2q^0 + 6q^5
```

The traversal spine is the four-layer transport ledger of `transport_obligations.py`:
`LCR -> D4 (axis,sheet)`, `D4 -> J3(O) diagonal carrier`, `J3(O) -> G2/F4/T5A route`, `route -> Niemeier landing forms`, with classifications `demonstrated / bounded_local / registered_landing_forms`. Each layer carries an `nsl_boundary` row in the ledger (`Ledger.nsl_boundary`). Tool binding:

```text
cqe_engine  (ledger.nsl: NSLTerm; ledger.ledger: Ledger.nsl_boundary;
             transport_obligations: transport_obligations, verify_transport_obligations;
             centroid_voa: voa_weight)
```

## Proof Tree

```text
claim (every transport carries an accountable energy/traversal ledger)
-> local transport (L,C,R): preserved vs residual
-> NSL boundary term (N, S, L, absorption)
-> step gate theta_i <= 0  (else obligation)
-> traversal sum Theta = sum theta_i
-> NSL conservation gate DeltaPhi <= 0
-> default per-state cost voa_weight (Z(q)=2q^0+6q^5)
-> worked example (two supply-chain paths)
-> supplemental workbook analogue (weighted bead string)
-> receipt
-> proof (ledger closes) / obligation (theta > 0, or unit calibration)
```

## Practical Solved Example

**Domain:** a route-cost map comparing two equivalent supply-chain paths between the same source and target object (the original scope's two-path comparison).

**Procedure:** register each path as a traversal over the four-layer transport spine; for each step, fill an `NSLTerm` with the conservation mismatch (`N`), information mismatch (`S`), and irreversible cost (`L`); compute `theta_i` per step and `Theta_path` per path; compare the two path totals; flag any step with `theta_i > 0` as an obligation carrying its residue.

**Solved Output (what is actually established):** the two paths receive reproducible traversal ledgers; the path with the smaller `Theta_path` is the leaner traversal *in the analog ledger*; steps that fail `theta_i <= 0` are emitted as obligations, not hidden. The example is solved in the corpus sense - the ledgers reproduce identically from `verify_transport_obligations`, the `NSLTerm` accounting, and the workbook bead string. What is NOT established: that `Theta` is a physical energy, or that the leaner-ledger path is cheaper in real cost - those require unit calibration (Axiom 25.5) and are obligations. The Morphonics model explicitly tags the "NSL unifies the physical laws" reading as `OVERCLAIM`; this paper inherits that boundary.

## Tool Binding

- Module: `cqe_engine` (`ledger.nsl.NSLTerm`; `ledger.ledger.Ledger.nsl_boundary`; `transport_obligations.transport_obligations`, `verify_transport_obligations`; `centroid_voa.voa_weight`).
- Verifiers: `verify_transport_obligations`, `verify_voa_sector_decomposition`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: weigh one traversal of two or more steps, emit a closing ledger (`Theta <= 0`) for at least one path and one obligation row for a step with `theta > 0` or an uncalibrated unit. Smoke test produces at least one proof-like row (closed ledger) and one obligation-like row.

## Analog Workbook Sheet

- Start with grey loose substrate; lay the traversal path as a string of pages, one per transport step.
- Place the `C` token at each step's preserved invariant; place `L` (preserved) and `R` (residual) tokens to either side.
- Thread a bead per step whose size encodes the step cost `theta_i`; the whole string's bead mass is `Theta_path`.
- Use string to bind the chosen route; compare two strings side by side for the two-path example.
- White follow-up = a traversal whose total bead mass closes (`Theta <= 0`); black follow-up = any step bead that overflows (`theta > 0`) or an uncalibrated cost.
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [Shannon1948] Shannon, C. E. (1948). A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: the information-mismatch term `S` and the channel / receipt framing of a transport.
- [W3C_PROV] W3C PROV Overview / PROV-DM provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: traversal as a provenance derivation chain with logged boundary terms.

## Open Obligations

- **Unit-calibration obligation (with falsifier).** The NSL terms are unit-agnostic. Falsifier: if a domain assigns physical units to `N, S, L` and the additivity (Lemma 25.3) fails to hold under those units, the linear ledger is downgraded and per-domain weights `alpha, beta, gamma` must be re-derived.
- **OVERCLAIM boundary (inherited).** No claim that `Theta` subsumes Noether / Shannon / Landauer laws; this is carried from the Morphonics `claim:nsl_unification` `OVERCLAIM` tag.
- The `absorption_capacity` term has no calibrated source in the applied domains; carry as `PENDING_MEASUREMENT`.
- Add one domain-expert (operations research / thermodynamics) critique pass.
- Replace citation anchors with final bibliography entries during peer-review preparation.

## Back-Propagation Targets

- Paper 00 receives the "energy/traversal ledger gate (`DeltaPhi <= 0`)" term and the Unit-Honesty axiom (Axiom 25.5).
- Papers 22-24 receive the per-transport NSL ledger row format (material closure, fold winding, and CA steps each gain an energy receipt).
- The lattice_forge registry records the `ledger.nsl` / `transport_obligations` traversal surface.
- The analog workbook manual receives the weighted-bead-string sheet rule.
- Paper 31 records how this paper's presentation order (step -> term -> gate -> path sum) enacts the same `(L, C, R)` process.
