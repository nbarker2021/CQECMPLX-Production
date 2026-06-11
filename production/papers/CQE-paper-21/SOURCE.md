# Paper 21 - MorphForge / PolyForge / MorphoniX

## Status

Transport / applied-bridge paper. Reads glyphs, numbers, shapes, and tokens as grid-swept ribbons whose bifurcations define folds and continuations, backed by the executable `morphonics_model_v0_2` ledger, the `chart_codec` `S_3`-word ribbon, and the terminal composition tree. This is the bridge into the applied Forge papers 22-24. Proof-facing where the codec/model verifier exists; horizon-facing where the cross-medium bridges are open.

## Abstract

This paper formalizes the Forge reading discipline: any source object — a glyph, a numeral, a shape, a token — is swept across the chart grid as a ribbon of overlapping `(L, C, R)` windows, and the ribbon's *bifurcations* (points where the local readout admits more than one continuation) are its fold points. Three real substrates back the reading. (1) The Morphonics State Closure model (`morphonics_model_v0_2`) is an executable ledger of *morphons* — bounded, projected, transformed, observed state packets — each with a primitive state, boundary, projections, transforms, invariants, reconstruction rule, accounting record, and residue; `verify_morphonics_model` returns `pass_with_open_gaps`, and the model's guiding rule is that no model is closed unless its presented state can be decomposed into primitive admissible states and reassembled while preserving declared invariants and accounting for all residue. (2) The chart codec (`chart_codec`) encodes a ribbon's `shell = 2` sub-trajectory as a word in `S_3` (the Weyl group of `SU(3) subset F_4`): each step is a named group element (`e` plus the three transpositions), the round trip is exact and lossless, and `verify_chart_codec` confirms zero mismatches to depth 4096. (3) The terminal composition tree (`terminal_tree`, via `Ledger.terminal_tree`) gives each ribbon a 24D landing form with component embeddings and a residue status. The fold = bifurcation reading is the bridge into the applied Forge papers 22-24; the cross-medium "unibeam" equivalence and the Mandelbrot-boundary chart are surfaced as explicit open obligations.

## Central Thesis

Read glyphs, numbers, shapes, and tokens as grid-swept ribbons whose bifurcations define folds and continuations.

## Scope Boundary

This paper claims the ribbon-reading discipline and the morphon-ledger / chart-codec machinery exactly as `morphonics.py`, `chart_codec.py`, and `terminal_tree.py` support them. It does NOT claim a closed cross-medium equivalence ("light and data are physically identical" is hardened to OVERCLAIM in the model), a literal Mandelbrot identification (CONJ, requires a supplied semiconjugacy), or any biology/materials claim — glyphs and shapes are used to SHOW the connection, not to make a domain claim. Excess interpretation is logged as obligation.

## Definitions

- **Ribbon**: the sequence of overlapping `(L, C, R)` chart windows obtained by sweeping a source object (glyph/number/shape/token) across the chart grid.
- **Fold (bifurcation)**: a ribbon point where the local readout admits more than one legal continuation; in the codec it is a non-identity `S_3` step (a transposition) rather than a self-loop `e`.
- **Continuation**: the next ribbon segment selected at a fold; unselected continuations are residue retained per the morphon accounting rule.
- **Morphon**: a bounded typed projected state packet `(visible_state, primitive_state, boundary, projections, transforms, invariants, reconstruction, accounting, evidence_status, residue, chart)` (`morphonics.MorphonRecord`).
- **`S_3` ribbon word**: the lossless encoding of a `shell = 2` sub-trajectory as `(start_state, word)` over `S_3 = {e, (1 2), (1 3), (2 3), (1 2 3), (1 3 2)}` (`chart_codec.encode` / `decode`).
- **Terminal landing**: the 24D Niemeier/Leech composition tree assigned to a ribbon (`terminal_tree.build_terminal_composition_tree`).
- **Theta accounting**: the transition-defect functional `Theta(phi) = wN*N + wS*S + wL*L + wG*G + wO*O` (Noether/Shannon/Landauer/geometric/obstruction terms), with `Theta <= 0` closed, `0 < Theta <= eps` glue-resolvable, else obstructed (`morphonics` accounting record).
- **Receipt / Transport row / Workbook sheet / Tool binding**: as fixed in Paper 00.

## Axioms

Axiom 21.1 - Locality: a ribbon is read window by window; each fold is decided from a local `(L, C, R)` reading before any larger landing is assigned.

Axiom 21.2 - Receipt Preservation: every ribbon step logs its `S_3` element, its morphon record, and its residue; the round trip must be replayable (decode == encode).

Axiom 21.3 - Boundary Positivity: an unselected continuation, a non-closing `Theta`, or a pending bridge is residue/obligation — classified, never discarded (`morphonics` failure labels).

Axiom 21.4 - Analog Equivalence: ribbon reading has a physical workbook analogue (a string ribbon laid over the chart grid, knotted at each fold).

## Lemmas

Lemma 21.1 - Lossless ribbon word. The `shell = 2` sub-trajectory of a ribbon encodes as an `S_3` word with exact, lossless round trip: any two distinct `shell = 2` states differ in exactly two positions, so a unique transposition maps one to the next, and `decode(encode(.))` reproduces the `(depth, state)` sequence with zero mismatches to depth 4096. (Verified: `chart_codec.verify_chart_codec`.)

Lemma 21.2 - Folds are non-identity steps. A ribbon fold is a non-identity `S_3` element (a transposition); a self-loop `e` is a non-fold continuation. The per-step symbolic entropy is `log2(4) = 2` bits (`e` plus 3 transpositions), bounding the raw `shell = 2` state entropy `log2(3) ~ 1.585`. (Source: `chart_codec` module; `element_counts`, `identity_self_loops`, `non_identity_steps`.)

Lemma 21.3 - Ledger-closed reading. A morphon is closure-valid only when its primitive fields are present and its accounting record is linked; `verify_morphonics_model` returns `pass_with_open_gaps` with all morphon closure tests passing and the open research gaps enumerated as failure records. (Verified: `morphonics.verify_morphonics_model`.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)` (Paper 00). A ribbon reading is a windowed sweep with folds, an `S_3` encoding, and a morphon ledger:

```text
ribbon(source) = [ (L_n, C_n, R_n) ]_n     (grid sweep)
fold at n  iff  shell2 step S_3 element != e   (Lemma 21.2)
encode(shell2_ribbon) = (start_state, word in S_3*)   (lossless, Lemma 21.1)
decode(encode(r)) == r                                 (exact round trip)
morphon(r): primitive_state, boundary, projections, transforms,
            invariants, reconstruction, accounting (Theta), residue
closure: R(D(m)) compared to invariant-aware epsilon ; Theta<=0 closed
landing: build_terminal_composition_tree(ledger, terminal_id) (24D)
```

Tool binding:

```text
cqe_engine  (lattice_forge.morphonics: morphonics_model_v0_2,
             verify_morphonics_model, MorphonRecord, AccountingRecord;
             lattice_forge.chart_codec: encode, decode, apply_s3,
             shell2_transition_element, verify_chart_codec;
             lattice_forge.terminal_tree: build_terminal_composition_tree)
```

## Proof Tree

```text
claim (glyphs/numbers/shapes/tokens = grid-swept ribbons with fold bifurcations)
-> local (L,C,R) window sweep over the source object
-> shell=2 sub-ribbon
-> S_3 word encoding (lossless round trip) [Lemma 21.1]
-> folds = non-identity S_3 steps [Lemma 21.2]
-> morphon ledger per segment (primitive/boundary/accounting/residue) [Lemma 21.3]
-> terminal 24D landing form (composition tree)
-> worked example (OCR/typography glyph ribbon)
-> workbook analogue (knotted string ribbon over the grid)
-> receipt
-> proof (codec + ledger schema) / obligation (unibeam, Mandelbrot, TF1)
```

## Practical Solved Example

**Domain:** an OCR / typography pipeline — glyph forms become route skeletons swept across the chart grid, with token candidates emerging at folds. (This is the applied bridge into Papers 22-24.)

**Procedure:** sweep a glyph's binarized skeleton into a ribbon of `(L, C, R)` windows; extract the `shell = 2` sub-ribbon; encode it as an `S_3` word; mark each non-identity step as a fold; assemble the morphon record and check closure; run `verify_chart_codec` and `verify_morphonics_model` on the reference data.

**Solved Output:** with real numbers and statuses from the source:
- Codec: `verify_chart_codec(max_depth=4096)` returns `status = "pass"`, `round_trip_mismatches = 0`, with `element_counts` over `{e, (1 2), (1 3), (2 3), (1 2 3), (1 3 2)}` separating `identity_self_loops` (non-folds) from `non_identity_steps` (folds); `bits_per_step_codec = 2.0` vs `bits_per_shell2_step_raw = 1.585`.
- Morphon ledger: `verify_morphonics_model(morphonics_model_v0_2(...))` returns `status = "pass_with_open_gaps"`, with all morphon closure tests passing and `open_gap_count` enumerating the pending bridges; the `morphon:rule30_center` record is `EXEC` (center bit determined by its full causal cone), the OCR-style `morphon:ai_response` record is `MODEL`.
- Landing: each ribbon's terminal composition tree carries ambient dimension 24 and a residue status (e.g. `residue_closes_by_required_index`).

The example is solved (for the codec and ledger schema) because the lossless ribbon word and the morphon closure reproduce from the formal definition, the `chart_codec` / `morphonics` verifiers, and the workbook knotted-ribbon sheet; the cross-medium and Mandelbrot readings are surfaced as obligations.

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.morphonics`, `lattice_forge.chart_codec`, `lattice_forge.terminal_tree`).
- Functions: `morphonics_model_v0_2`, `verify_morphonics_model`; `encode`, `decode`, `apply_s3`, `shell2_transition_element`, `verify_chart_codec`; `build_terminal_composition_tree`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: encode and decode one glyph ribbon's `shell = 2` sub-trajectory with zero round-trip mismatches; build its morphon record and confirm closure; emit one proof row (a closed fold ribbon) and one obligation row (a pending bridge).

## Analog Workbook Sheet

- Start with grey loose substrate; lay the chart grid as a ruled page.
- Sweep a string ribbon across the grid following the source glyph/number/shape; at each cell read `(L, C, R)` with the `C` token at the center.
- Tie a knot at every fold (a non-identity `S_3` step); leave straight runs for self-loop `e` continuations.
- Color red/green/blue for the three `S_3` settings; tag each knot with its transposition name.
- White follow-up = a closed, losslessly-decodable ribbon; black follow-up = an unselected continuation, a non-closing `Theta`, or a pending bridge.
- Bind the finished ribbon page into the matching color notebook.

## IRL Citation Anchors

- [OEIS] OEIS Foundation / On-Line Encyclopedia of Integer Sequences. URL: https://oeis.org/ Use: numbers/sequences as ribbon sources; recurrence and pattern records.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: ribbon as an encoded channel; per-step entropy bound.
- [Mandelbrot1982] B. Mandelbrot, The Fractal Geometry of Nature, W. H. Freeman. Use: the conjectural fold-boundary chart (CONJ, requires a supplied semiconjugacy).
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: `S_3` as the Weyl group of `SU(3) subset F_4` underlying the codec.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: morphon receipts and residue accounting.

## Open Obligations

- **Unibeam cross-medium equivalence:** `claim:unibeam_equivalence` is hardened to OVERCLAIM and the bridge `bridge:unibeam_cross_medium_equivalence` is `PENDING_MEASUREMENT` — cross-medium equivalence requires a measured round trip `F(T1(s)) ~= T2(F(s))` plus medium cost. Carried open.
- **Mandelbrot / fractal boundary chart:** `claim:fractal_chart` is CONJ and `projection:fractal_boundary_chart` requires validating `f(M(Psi)) ~= f(Psi)^2 + c`; formal only when a semiconjugacy or explicit boundedness map is supplied.
- **TF1 / Leech import (PENDING_IMPORT):** `morphon:niemeier_terminal_tree` carries `failure:leech_construction_pending` (import Golay/Construction-A records for Leech) and the `mscf_to_lattice_forge_24d` bridge needs expanded involution witnesses; the TF1 Navier-Stokes bridge is `PENDING_MEASUREMENT`.
- Replace citation anchors with final bibliography entries; add a falsifier the tool must reject (a ribbon whose `S_3` word fails to round-trip, which `verify_chart_codec` must flag).

## Back-Propagation Targets

- Paper 00 receives the "ribbon", "fold/bifurcation", and "morphon" contract terms.
- Paper 01 receives the `shell = 2` stratum reading the codec depends on; Paper 17 receives the 24D terminal landing forms used here.
- Papers 22-24 (applied Forge) inherit the ribbon-reading discipline as their entry contract.
- Paper 20 receives the unibeam / Mandelbrot / TF1 obligations and the closed-ribbon proofs as ledger rows.
- The analog workbook manual receives the knotted-string-ribbon rule.
- Paper 31 records how the corpus's own glyph-to-paper rendering is itself a grid-swept ribbon with fold points at each section boundary.
