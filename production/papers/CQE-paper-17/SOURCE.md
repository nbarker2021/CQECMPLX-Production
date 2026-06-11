# Paper 17 - E6-E8 Error-Correction Tower

## Status

Transport paper. Surfaces the lattice-code backbone `1 -> 3 -> 7 -> 8 -> 24 -> 72` as an error-correction tower from local roots to larger closure frames, with the `W(E_8)` lookup table carried as an explicit open obligation. Proof-facing where the verifier exists, obligation-facing otherwise.

## Abstract

This paper registers error-correction candidates as towered lattice transitions: each step moves a local readout window into a strictly larger closure frame, and each frame is a *forced* code at its dimension. The backbone is the chain `1 -> 3 -> 7 -> 8 -> 24 -> 72`, in which `n=1` is the `Z/2` repetition code (D1 raw bit), `n=3` is the `S_3` neighborhood, `n=7` is the `(7,4,3)` Hamming code whose weight-3 codewords are the Fano-plane lines (= octonion multiplication triples), `n=8` is the `(8,4,4)` doubly-even self-dual extended Hamming code generating the `E_8` root lattice by Construction A, `n=24` is the `(24,12,8)` Golay code carrying the Leech construction's `3 x 8` geometry, and `n=72` is the Nebe extremal even unimodular lattice that terminates the chain at the sheet K-bound `K_max = 9 = 3^2`. The transitions `E_6 -> E_7 -> E_8` sit inside this tower as the exceptional rungs; `E_6` appears as a Niemeier component (e.g. `Niemeier:A11_D7_E6`) and `E_8^3` is the unique determinant-one direct-sum landing form. The executable verifier `verify_lattice_code_chain` confirms every code parameter and the powered shortcut `1 -> 9 -> 49 -> 72`; the `O(N)` -> sub-`O(N)` extraction at the `E_8` Weyl scale (the order-`696729600` `W(E_8)` lookup table) is NOT built here and is carried as the umbrella's open obligation O1.

## Central Thesis

Represent error-correction candidates as towered lattice transitions from lower local roots to larger closure frames.

## Scope Boundary

This paper claims the code-parameter tower and its forced-step structure exactly as the `lattice_codes` verifier supports them, plus the registered `E_8^3` / Niemeier landing forms as *registered targets*. It does NOT claim a constructed Leech overlattice, a computed `W(E_8)` extraction table, or a depth-`N` cold-start fingerprint. Those are obligations logged below. The `E_6 -> E_8` "error-correction" reading is a transport interpretation of the code tower, not a new coding theorem.

## Definitions

- **Local root frame**: the smallest carrier at a given rung — the `(L, C, R)` window (D1/D2), then the Fano/octonion frame (D3), the `E_8` chart frame (D4), and so on.
- **Closure frame**: the lattice or code into which a local frame embeds at the next rung; each is the unique forced code at its dimension.
- **Tower transition**: a step `n -> n'` in the chain, accepted only when the larger frame is a self-orthogonal / doubly-even / extremal code containing the smaller frame's structure.
- **Forced parameter**: a chain value (`1, 3, 7, 8, 24, 72`) determined by the previous value under the constraint of being the unique perfect / self-dual / extremal code at that dimension.
- **Sheet K-bound**: `K_max = 9 = 3^2`, the maximum Hamming distance from the first enumerated anchor event at which a state still expresses on the current Nebe-72 sheet.
- **Landing form**: a registered rank-24 Niemeier or Leech terminal target (e.g. `Niemeier:E8^3`, `Niemeier:Leech`).
- **Receipt / Transport row / Workbook sheet / Tool binding**: as fixed in Paper 00.

## Axioms

Axiom 17.1 - Locality: every accepted error-correction claim must be readable through a local root frame before it is lifted to a closure frame.

Axiom 17.2 - Receipt Preservation: no tower transition is accepted unless the code parameters, self-duality / minimum-distance checks, and any unresolved glue residue can be logged and replayed.

Axiom 17.3 - Boundary Positivity: a rung whose closure (e.g. the Leech landing) is not yet constructed is data; it is logged as an obligation, never silently promoted to a proof.

Axiom 17.4 - Analog Equivalence: each rung has a physical workbook analogue (a code-card laid at increasing dimension on the matching color sheet).

## Lemmas

Lemma 17.1 - Forced Hamming/Fano rung. The `(7,4,3)` Hamming code has exactly 7 weight-3 codewords whose supports are the 7 lines of `PG(2,2)`, which are the 7 quaternionic triples of octonion multiplication. (Verified: `verify_hamming_7_fano`, weight distribution `{0:1, 3:7, 4:7, 7:1}`.)

Lemma 17.2 - Forced `E_8` rung. The `(8,4,4)` extended Hamming code is doubly-even and self-dual with weight distribution `{0:1, 4:14, 8:1}`; it is the unique such code in dimension 8 and generates `E_8` by Construction A. (Verified: `verify_extended_hamming_8`.)

Lemma 17.3 - Terminal Nebe rung. `72 = 8 x 9 = |D4 chart| x 3^2`; the Nebe lattice in dimension 72 is extremal with minimum norm `2*floor(72/24)+2 = 8`, setting the sheet K-bound `K_max = 9`. (Verified: `verify_powered_chain`.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)` (Paper 00). At rung `n`, the closure frame `Frame(n)` is a code; a tower transition is accepted when:

```text
Frame(n)  embeds in  Frame(n')   (n' = next chain value)
Frame(n') is the forced code at dim n'  (perfect / self-dual / extremal)
parameters (length, dim, min-distance) verified over F_2
residual glue (uncertified overlattice action) recorded in O, not erased
```

The base chain and its powered shortcut:

```text
base:     1 -> 3 -> 7 -> 8 -> 24 -> 72
codes:    (1,1,1)  S_3  (7,4,3)  (8,4,4)  (24,12,8)  Nebe-72
tower:    D1      D2    D3-Fano  D4=E_8   Leech-seed  K-bound terminal
powered:  1^2=1   3^2=9   7^2=49   8*9=72
exceptional rungs: E_6 (Niemeier component) -> E_7 -> E_8 (E_8^3 index-1 landing)
```

Tool binding:

```text
cqe_engine  (lattice_forge.lattice_codes: verify_lattice_code_chain,
             verify_hamming_7_fano, verify_extended_hamming_8,
             verify_golay_24, verify_powered_chain;
             lattice_forge.unipotent_orbits for E6/E7/E8 orbit lookup)
```

## Proof Tree

```text
claim (error-correction candidates = towered lattice transitions)
-> local root frame (L,C,R window)
-> forced rung n=7  (Hamming/Fano/octonion, Lemma 17.1)
-> forced rung n=8  (E_8 by Construction A, Lemma 17.2)
-> rung n=24        (Golay = 3 x D4, Leech-construction ingredients)
-> terminal n=72    (Nebe extremal, K_max=9, Lemma 17.3)
-> E_6 -> E_7 -> E_8 exceptional rungs (Niemeier components / E_8^3 landing)
-> worked example (full chain verifier)
-> workbook analogue (code-card stack)
-> receipt
-> proof (parameters) / obligation (Leech landing, W(E_8) table)
```

## Practical Solved Example

**Domain:** a multi-stage parity tower in which each rung catches a strictly larger fault class — the corpus's reference error-correction tower.

**Procedure:** run `verify_lattice_code_chain()`; it composes the five rung verifiers and the powered-chain check.

**Solved Output:** each rung verifies with real numbers from the source:
- `n=7`: 16 codewords, minimum weight 3, weight distribution `{0:1, 3:7, 4:7, 7:1}`; the 7 weight-3 supports equal the Fano lines.
- `n=8`: 16 codewords, minimum weight 4, all weights `= 0 mod 4`, self-dual, weight distribution `{0:1, 4:14, 8:1}` — the `E_8` seed.
- `n=24`: 12 x 24 systematic Golay generators, all generator weights `>= 8` and `= 0 mod 4`, structured as `24 = 3 x 8`; `leech_construction_proved = False` is recorded.
- `n=72`: `8*9 = 72`, extremal minimum norm 8, `K_max = 9`.

The example is solved because the same rung parameters reproduce from the formal table, the `verify_lattice_code_chain` verifier, and the analog code-card stack. The `E_8`-scale extraction table is explicitly absent (obligation O1).

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.lattice_codes`, `lattice_forge.unipotent_orbits`).
- Functions: `verify_lattice_code_chain`, `verify_hamming_7_fano`, `verify_extended_hamming_8`, `verify_golay_24`, `verify_powered_chain`; `unipotent_orbits_for_group("E6"|"E7"|"E8")`, `closure_landing_candidates`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run the chain verifier and confirm `status == "pass"`; emit at least one proof row (a verified rung) and one obligation row (the Leech landing or `W(E_8)` table).

## Analog Workbook Sheet

- Start with grey loose substrate.
- Place the `C` token at the local center of a 3-cell strip (the `n=3` rung).
- Lay a code-card for each rung in increasing size: a 7-card Fano triangle, an 8-card `E_8` square, a 24-card `3 x 8` block, a 72-card Nebe panel.
- Mark active color gradients red/green/blue on the `n=3` rung (the three `S_3` settings).
- Use string to bind the accepted tower route from `n=1` up to the highest verified rung.
- White follow-up = a verified rung (proof continuation); black follow-up = an un-constructed landing (obligation) — mark the Leech card and the `W(E_8)` table card black.
- Bind the finished stack into the matching color notebook.

## IRL Citation Anchors

- [Conway1999] J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups (3rd ed.), Springer. Use: Hamming/Golay codes, `E_8` and Leech construction, Niemeier classification.
- [Niemeier1973] H.-V. Niemeier, Definite quadratische Formen der Dimension 24 und Diskriminante 1, J. Number Theory 5, 142-178. Use: the 24 rank-24 even unimodular landing forms.
- [Nebe2012] G. Nebe, An even unimodular 72-dimensional lattice of minimum norm 8, J. reine angew. Math. 673, 237-247. Use: the Nebe terminal of the chain.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: Fano-plane / octonion multiplication structure at `n=7`.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: receipts and obligation ledger.

## Open Obligations

- **O1 (W(E_8) table, IDENTITY 8.1):** the `2.6` GB precomputed `W(E_8)` Weyl-element lookup table (order `696729600`) is not constructed here. It is engineering-tractable and would mechanically demonstrate the sub-`O(N)` extraction at the `E_8` scale beyond the `F_4` scale; carried open.
- **Leech landing:** `verify_golay_24` records `leech_construction_proved = False`; the rootless Leech overlattice glue action is a separate obligation (see `enumerated_glue` / Paper 18 routes).
- **E_6 -> E_7 -> E_8 closure assignment:** `unipotent_orbits` exposes lookup only and does not assert that an orbit label closes a CMPLX obligation; the exact rung-to-orbit assignment is open.
- Replace citation anchors with final bibliography entries; add one falsifier rung the tool must reject (a code that fails self-duality or minimum distance).

## Back-Propagation Targets

- Paper 00 receives the "tower transition" and "sheet K-bound" contract terms.
- Paper 18 receives the Golay / `E_8^3` / Leech landing forms as the substrate of its representation routes.
- Paper 20 receives this paper's verified rungs and open landings as ledger rows.
- The analog workbook manual receives the code-card stack rule.
- Paper 31 records how the rung-by-rung presentation order is itself an enacted `(L, C, R)` lift.
