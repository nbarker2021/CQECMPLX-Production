# Paper 08 - E8 / Niemeier / Leech Closure

## Status

Lattice-template paper. Establishes the `(1, 3, 7, 8, 24)` code chain and its powered extension to dimension 72 (the Nebe lattice) as the combinatorial backbone for transport, with each step's claim explicitly classified as *demonstrated locally* or *open obligation*. Local derivation precedes any universality assertion. Proof-facing. Inherits the Paper 00 contract.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

This paper uses high-dimensional lattice analogs as closure templates for transport without claiming global universality before local derivation. The corpus already registers the 3-cell chart into `J_3(O)`; here we surface the discrete code chain that the chart's parameters trace as scale increases: `1` (the `Z/2` raw bit), `3` (the `S_3` neighborhood / three trace-2 idempotents), `7` (the Fano plane `PG(2,2)` = the 7 imaginary octonion units), `8` (the `(8,4,4)` extended Hamming code = the `E_8` root lattice via Construction A), `24` (the `(24,12,8)` binary Golay code, an ingredient of the Leech lattice), and the powered terminal `72 = 8 x 9` (the Nebe extremal even unimodular lattice). Each parameter is the unique self-orthogonal doubly-even perfect or extremal code at its dimension. We verify the *local* facts that the modules certify - the Fano-line/Hamming-codeword identity, `E_8` self-duality and double-evenness, Golay self-orthogonality and the `24 = 3 x 8` carrier geometry, and the `72`-dimensional sheet bound - and we keep the *global* lift (the rootless Leech landing, the `Gamma_72` glue action, and the cold-start fingerprint map) explicitly open. The discipline is local-derivation-first: a verifier that returns `pass` certifies only the combinatorial fact it tests, never the universality it is a template for.

## Central Thesis

Use high-dimensional lattice analogs as closure templates for transport without claiming global universality before local derivation.

## Scope Boundary

This paper claims the *local* combinatorial identities of the code chain `(1, 3, 7, 8, 24, 72)` and their correspondence to the chart's scale parameters, each backed by a named verifier. It does NOT claim the Leech lattice landing (`verify_golay_24` returns `leech_construction_proved = False`), the `Gamma_72` glue action (`verify_nebe_gamma72_contract` returns `gamma72_landing_proved = False`), or any cold-start map from depth `N` to a lattice fingerprint. Every "the chain forces..." statement is a uniqueness claim about codes at fixed dimension, not a transport theorem. Excess interpretation is logged as obligation.

## Definitions

- **Code chain**: the sequence of parameters `(1, 3, 7, 8, 24)` with terminal extension `72`, each the dimension of a distinguished binary code or lattice (`lattice_codes.py`).
- **Fano plane `PG(2,2)`**: the 7-point, 7-line projective plane; its 7 points are the imaginary octonion units `e_1..e_7`, its 7 lines are the quaternionic triples (`FANO_LINES_7`, `verify_hamming_7_fano`).
- **`(7,4,3)` Hamming code**: the perfect single-error-correcting binary code; its 7 weight-3 codewords' supports are exactly the Fano lines (`verify_hamming_7_fano`).
- **`(8,4,4)` extended Hamming code**: the doubly-even self-dual code; via Construction A it gives the `E_8` root lattice (`verify_extended_hamming_8`).
- **`(24,12,8)` binary Golay code**: the unique doubly-even self-dual length-24 code with minimum weight 8; a Leech-construction ingredient (`verify_golay_24`).
- **Construction A**: the standard map from a binary code `C` of length `n` to a lattice in `R^n` (`Z^n` scaled by `1/sqrt(2)` with the code as `mod 2` reductions); applied to `(8,4,4)` it yields `E_8`.
- **Nebe lattice (dimension 72)**: the unique extremal even unimodular lattice in dimension 72; here `72 = 8 x 9 = |D4 chart| x 3^2` is the *sheet K bound* (`verify_powered_chain`, `nebe_gamma72.py`).
- **Sheet K bound**: states at Hamming distance `K = 1..9` from the first enumerated event are expressible in the current sheet; `K > 9` requires a new anchor (`lattice_codes.py` docstring; `verify_powered_chain` `sheet_K_bound = 9`).
- **Landing form / registered target**: a named terminal lattice (a Niemeier root system or Leech sheet) recorded in the registry as a transport target, NOT as a proved computation (`transport_obligations.py`, classification `registered_landing_forms`).

## Axioms

Axiom 08.1 - Locality: each chain parameter is admitted only via a local combinatorial verifier that tests the code/lattice at that fixed dimension; no parameter is admitted by analogy to its neighbors.

Axiom 08.2 - Receipt Preservation: each verifier emits a status (`pass`/`fail`), the explicit fact tested, and the proof boundary it does NOT cross (e.g. `leech_construction_proved = False`).

Axiom 08.3 - Boundary Positivity: an unproved global lift (Leech landing, `Gamma_72` glue) is a recorded obligation with a named witness, never a silent gap nor an inflated claim.

Axiom 08.4 - Analog Exposure Equivalence: the chain has a supplemental workbook analogue - nested frames of `1 / 3 / 7 / 8 / 24 / 72` tokens, with a black follow-up at the sheet bound `K = 9`.

## Axioms (chain-uniqueness, as obligations)

The "forced" character of the chain is stated by `verify_parameter_chain` as structural facts: `3 = |S_3 transpositions| = |trace-2 idempotents|`; `7 = |Fano points| = |octonion imaginaries| = 2^3 - 1`; `8 = 7 + 1 = |D4 chart| = dim O`; `24 = 3 x 8`. The Mersenne steps `1 -> 3 -> 7` satisfy `b = 2a + 1`. These are certified as combinatorial identities, not as a theorem that no other chain is possible; the latter is an obligation.

## Lemmas

Lemma 08.1 - Fano/Hamming identity: the `(7,4,3)` Hamming code has 16 codewords with weight distribution `{0:1, 3:7, 4:7, 7:1}`, and the supports of its 7 weight-3 codewords are exactly the 7 lines of `PG(2,2)`. (Basis: `verify_hamming_7_fano`, status `pass`.) Hence at `n = 7` the code, the Fano plane, and the octonion imaginary-unit structure are one object.

Lemma 08.2 - `E_8` characterization: the `(8,4,4)` extended Hamming code is doubly-even (all weights `= 0 mod 4`) and self-dual (`C = C^perp`), with weight distribution `{0:1, 4:14, 8:1}`. (Basis: `verify_extended_hamming_8`, status `pass`.) These two properties uniquely characterize `E_8` among even unimodular lattices in dimension 8 under Construction A.

Lemma 08.3 - Golay carrier and the open Leech lift: the `(24,12,8)` Golay generators are self-orthogonal and doubly-even, and `24 = 3 x 8` realizes three copies of the `D4` chart. (Basis: `verify_golay_24`, status `pass`.) But the same verifier returns `leech_construction_proved = False`; the rootless Leech landing is a separate glue-action obligation. The powered terminal `72` is the Nebe extremal dimension (extremal minimum norm `2*floor(72/24) + 2 = 8`, `verify_powered_chain`), and `verify_nebe_gamma72_contract` certifies only that arbitrary byte payloads reach three Leech sheets losslessly, with `gamma72_landing_proved = False`.

## Formalism / Calculus Sketch

A chain state is `K = (d, V, F, L, O)`: the dimension `d in {1,3,7,8,24,72}`, the verifier `V` for that dimension, the local fact `F` it certifies, the lift status `L in {demonstrated, registered_landing_forms, open}`, and the obligation set `O`. A chain step is accepted when:

```text
V(d) -> status pass        (the local code/lattice fact holds)
F recorded with its weight distribution / orthogonality data
L assigned: pass => demonstrated for the local fact only
            global landing => registered_landing_forms or open, NOT demonstrated
proof_boundary copied verbatim into O (e.g. leech_construction_proved=False)
```

The transport ladder is `LCR -> D4 -> J3(O) -> G2/F4 route -> Niemeier/Leech landing forms`, with classifications `demonstrated, demonstrated, bounded_local, registered_landing_forms` respectively (`transport_obligations.transport_obligations`). Only the first two rungs are `demonstrated`; the lattice landing rungs are bounded or registered. Tool binding:

```text
cqe_engine  (lattice_forge: lattice_codes.verify_lattice_code_chain
             [verify_parameter_chain, verify_hamming_7_fano, verify_extended_hamming_8,
              verify_golay_24, verify_powered_chain];
             nebe_gamma72.verify_nebe_gamma72_contract;
             transport_obligations.verify_transport_obligations)
```

## Proof Tree

```text
claim (lattice chain is the closure template; local first, global open)
-> n=1  Z/2 raw bit (D1)
-> n=3  S_3 neighborhood / 3 trace-2 idempotents (verify_parameter_chain)
-> n=7  Fano = (7,4,3) Hamming = octonion imaginaries (Lemma 08.1)
-> n=8  (8,4,4) self-dual doubly-even = E_8 via Construction A (Lemma 08.2)
-> n=24 (24,12,8) Golay self-orthogonal; 24 = 3 x 8 carrier (Lemma 08.3)
   -> Leech landing: leech_construction_proved = False  -> OBLIGATION
-> n=72 Nebe extremal dim; sheet K bound = 9 (verify_powered_chain)
   -> Gamma_72 glue: gamma72_landing_proved = False     -> OBLIGATION
-> worked example (verify_lattice_code_chain)
-> supplemental workbook analogue (nested-frame tokens, K=9 black follow-up)
-> receipt (per-dimension status + proof_boundary)
```

## Practical Solved Example

**Domain:** the full code chain `(1, 3, 7, 8, 24)` with powered terminal `72`.

**Procedure:** call `verify_lattice_code_chain()`. It runs five sub-verifiers: `verify_parameter_chain` (structural identities `3, 7=2^3-1, 8=7+1, 24=3x8`), `verify_hamming_7_fano` (Fano-line/codeword identity), `verify_extended_hamming_8` (`E_8` self-duality and double-evenness), `verify_golay_24` (Golay self-orthogonality and `24 = 3 x 8`), and `verify_powered_chain` (`1, 9, 49, 72` tensor capacities and the Nebe sheet bound).

**Solved Output:** each sub-verifier returns `status = "pass"` for the local combinatorial fact, with the certified data: `(7,4,3)` weight distribution `{0:1, 3:7, 4:7, 7:1}` and the 7 weight-3 supports equal to `FANO_LINES_7`; `(8,4,4)` weight distribution `{0:1, 4:14, 8:1}`, self-dual; Golay generators self-orthogonal and doubly-even; powered chain `{1^2: 1, 3^2: 9, 7^2: 49, 8x9: 72}` with `7^2 = 49 = 7 + 21 + 21` (the 21 antisymmetric entries = the `J_3(O)` off-diagonal octonion structure constants) and `sheet_K_bound = 9`, Nebe extremal minimum norm `8`. The chain-level result reports `golay_24: pass` while the deeper `verify_golay_24` payload carries `leech_construction_proved = False`. The example is solved precisely because the local facts certify and the global lifts remain explicitly open - which is the paper's thesis enacted.

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.lattice_codes.verify_lattice_code_chain` and its five sub-verifiers; `lattice_forge.nebe_gamma72.verify_nebe_gamma72_contract`; `lattice_forge.transport_obligations.verify_transport_obligations`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run `verify_lattice_code_chain()` and confirm all five sub-statuses `pass`; run `verify_nebe_gamma72_contract()` and confirm `all_three_sheet_round_trips_exact = True` while `gamma72_landing_proved = False`; emit one obligation row for the Leech landing and one for the `Gamma_72` glue.

## Analog Workbook Sheet

- Start with grey loose substrate.
- Lay nested frames: 1 token (bit), then a 3-token row (the neighborhood), then a 7-token Fano frame (7 dots, 7 lines), then an 8-token frame (Fano + 1 unit), then three 8-token copies (24), then the 72 sheet.
- Color a frame white when its local verifier passes (the code/lattice fact holds); leave the Leech and `Gamma_72` frames with a black follow-up (lift open).
- Mark the sheet bound: count Hamming distance `K` from the first enumerated token; at `K = 9` place a hard black edge - states past it need a new anchor.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [ConwaySloane1999] J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups (3rd ed.), Springer, 1999. Use: `E_8`, Construction A, the Golay code, and the Leech lattice.
- [Niemeier1973] H.-V. Niemeier, Definite quadratische Formen der Dimension 24 und Diskriminante 1, J. Number Theory 5, 142-178, 1973. Use: the 24 even unimodular lattices (Niemeier landing forms).
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205, 2002. Use: the Fano-plane / octonion-imaginary correspondence at `n = 7`.
- [Hurwitz1898] A. Hurwitz, Ueber die Composition der quadratischen Formen, Nachr. Ges. Wiss. Goettingen, 1898. Use: the normed-division-algebra dimensions `1, 2, 4, 8` underlying the `7 -> 8` extension.

## Open Obligations

- The rootless Leech landing from the Golay carrier is not proved (`verify_golay_24`: `leech_construction_proved = False`); the glue action is a named obligation.
- The `Gamma_72` glue action is not proved (`verify_nebe_gamma72_contract`: `gamma72_landing_proved = False`); only lossless three-sheet transport is certified, pending a selected Hermitian polarization matrix (`NEBE_HERMITIAN_STRUCTURE_COUNT = 9` candidates).
- The cold-start map from depth `N` to a Niemeier/Leech fingerprint is unproved (`verify_niemeier_landing_registry`: `fingerprint_map_proved = False`); landing forms are registered targets, not automatic closure.
- The chain-uniqueness claim ("no other chain works") is structural and carried as an obligation; the verifiers test fixed-dimension identities, not non-existence of alternatives.
- Replace citation anchors with final bibliography entries.

## Back-Propagation Targets

- Paper 00 receives the `registered_landing_forms` classification term (a target may be registered without being a proved computation).
- Paper 01 receives the `n = 3 -> 3` trace-2-idempotent anchor as the chain's `D2` rung.
- Paper 09 receives the sheet `K = 9` bound as the limit of a single Hamiltonian window's reach.
- The ForgeFactory / lattice_forge registry records `lattice_codes` and `nebe_gamma72` as the chain witnesses with their proof boundaries.
- Paper 31 records how the chain's scale ladder mirrors the corpus's own expansion from one bit to the full lattice substrate.
