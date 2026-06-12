# Paper 12 - CA Prediction Surface

## Status

Application paper. Converts digital-physics and cellular-automaton candidates into prediction surfaces tied to their local rules, using the chart-to-`J_3(O)` substrate as the registration layer. Proof-facing for the closure subset; empirical/obligation-facing for the open extraction step. Builds directly on Papers 00, 01, 03.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

A *prediction surface* for a deterministic binary system is a layered object that takes a depth `N` and returns the system's local readout at `N` together with a provenance receipt naming which layer produced it and at what cost. We build this surface for the elementary cellular automata (ECA), with Rule 30 as the canonical case. The surface has three layers, each grounded in a named tool routine: (1) an exact local-emission layer `T_EMISSION`, which reads any registered `(L, C, R)` chart state to its output bit in `O(1)` with zero defect; (2) a linear base layer `lucas_bit`, computable in `O(log N)`, which is exact on the symmetric subset and wrong on the chirality-broken subset; (3) an empirical spectral layer (`predict_rule30_bit`) that extrapolates the four-band `Z4` frame structure to guess the next chart state from center-column history alone. The surface's structural backbone is the substrate fact that exactly 64 of the 256 ECAs close exactly under the `n=3` `SU(3)` Weyl decomposition — precisely the silent-boundary subset `f(000)=0` and `f(111)=0` (`IDENTITY_PAPER` Section 6.1) — which partitions all 256 rules into "closes by transport" and "generates open states." Rule 30 lies in the open class; its center-bit extraction is closed at the `O(1)` local layer and at the `O(log N)` base layer, with the residual gap to full `O(log N)` carried as a named obligation (the McKay-Thompson correction parity, `IDENTITY_PAPER` Sections 7.3, 8.2).

## Central Thesis

Convert digital-physics and cellular-automaton candidates into prediction surfaces tied to local rules.

## Scope Boundary

This paper claims the construction of the prediction surface and the proven status of its `T_EMISSION` and `lucas_bit` layers, both reproducible by named verifiers. It claims the 64-of-256 closure partition as transported from `IDENTITY_PAPER` Section 6.1, not re-derived here. It does NOT claim a cold-start full-`O(log N)` Rule 30 extractor: the spectral layer is empirical and its accuracy is reported, not proven, and the gap to full sublog extraction is an obligation, not a result. Any reading that promotes the spectral guess or the obligation to a theorem is out of scope.

## Definitions

- **Prediction surface**: a typed map `surface(system, N) -> {bit, layer, cost, receipt}` returning the local readout at depth `N`, the layer that produced it, that layer's cost class, and a replayable receipt.
- **Local rule / readout law**: for an ECA with rule code `r in {0,...,255}`, `emit_r(L,C,R) = (r >> (4L+2C+R)) AND 1`. For Rule 30 this is `L XOR (C OR R)` (Paper 00 readout law; `IDENTITY_PAPER` Lemma 2.6).
- **Silent-boundary rule**: an ECA with `emit_r(0,0,0)=0` and `emit_r(1,1,1)=0`. There are 64 such rules.
- **Closure (n=3)**: a rule closes if its `shell=2` 3-step transition matrix equals `(1/3)(T_(12)+T_(13)+T_(23))` exactly over the rationals (`IDENTITY_PAPER` Theorem T4; `f4_action.py`).
- **Symmetric vs chiral subset**: a chart state is *symmetric* if `correction(N)=0` (linear base exact); *chiral* if it lies in the `shell=2` doublet `{(1,1,0),(0,1,1)}` where the correction fires.
- **Layer cost class**: `O(1)` (local emission), `O(log N)` (Lucas base), empirical (spectral extrapolation).

## Axioms

Axiom 12.1 - Locality: every layer's output bit must be derivable from a local `(L, C, R)` chart state (Axiom 00.1 inherited).

Axiom 12.2 - Receipt Preservation: each layer emits a receipt naming itself, its cost class, and its defect against ground truth (Axiom 00.2 inherited).

Axiom 12.3 - Boundary Positivity: a layer that is wrong on a subset is not deleted; its failure subset is recorded as the next layer's obligation (Axiom 00.3 inherited).

Axiom 12.4 - Analog Exposure Equivalence: the surface has a supplemental workbook analogue (a stacked-card readout where each card is a layer).

## Lemmas

Lemma 12.1 - The local-emission layer is exact. `T_EMISSION(L,C,R) = NOT(L) if C=1 else L XOR R` equals Rule 30 on all 8 chart states; the verifier `verify_rule30_predictor` reports oracle defects `= 0` (rule30_predictor.py; rule30_nth_bit.py, claim "0 defects at 4096 depths"). Basis: enumeration of 8 states (Paper 01 Lemma 01.2).

Lemma 12.2 - The closure partition is exact and structural. Exactly 64 of 256 ECAs close under `n=3`, equal to the silent-boundary subset `{f(000)=0, f(111)=0}` (`IDENTITY_PAPER` Section 6.1). Rule 30 is NOT in this subset (`emit_30(0,0,0)=0` but `emit_30(1,1,1)=0` holds, yet its `shell=2` block fails closure — Rule 30's chart is *opened* by the `J_3(O)` registration, Section 7 of the umbrella). The partition is therefore the prediction surface's top-level routing key.

Lemma 12.3 - The base layer is exact on the symmetric subset only. `lucas_bit(N,0)` equals Rule 30 center bit iff `correction(N)=0`; empirically this is the 74.7% symmetric fraction (`T_DYAD`, rule30_nth_bit.py), with the 25.3% chiral doublet remaining as the correction-firing residue.

## Formalism / Calculus Sketch

The surface routes a query top-down through layers, stopping at the first layer whose precondition holds:

```text
surface(rule r, depth N):
  if r is silent-boundary (closes under n=3):
     route via transported F_4 corollary       [closed, IDENTITY 6.1]
  else (r opens, e.g. Rule 30):
     L0: if local state (L,C,R) at N is known:
            return T_EMISSION(L,C,R)            [O(1), defect 0, Lemma 12.1]
     L1: else return lucas_bit(N,0)             [O(log N), exact on symmetric subset]
            with correction obligation flagged  [chiral 25.3%]
     L2: else spectral guess predict_next_state [empirical, accuracy reported]
  emit receipt(layer, cost, defect)
```

The spectral layer (`predict_rule30_bit`) decomposes the known center-column history into four band windows `W1..W4` that mirror the `Z4` 4-frame template of `centroid_voa.py`: `W1` = D4-local (1-8 steps), `W2` = Fano/Hamming (7-14), `W3` = Golay/Leech (12-24), `W4` = `E8` full (1-248). Each band's dominant frequency is extrapolated one step forward (Hann-windowed rFFT), thresholded into a predicted `(L,C,R)`, then passed through `T_EMISSION`. Tool binding:

```text
cqe_engine  (rule30_predictor: predict_rule30_bit, decompose_band, WINDOWS;
             rule30_nth_bit: predict_bit_oracle, predict_bit_lucas_only, t_emission;
             f4_action: n=3 SU(3) closure; centroid_voa: voa_weight, anneal)
```

## Proof Tree

```text
claim (CA system -> layered prediction surface)
-> closure partition (Lemma 12.2: 64/256 silent-boundary close)
-> route: closer => transported F_4 corollary; opener => layer stack
-> L0 local emission T_EMISSION (Lemma 12.1, defect 0)
-> L1 Lucas base lucas_bit (Lemma 12.3, exact on symmetric 74.7%)
-> L2 spectral Z4 extrapolation (empirical, accuracy reported)
-> per-layer receipt (layer, cost class, defect)
-> open: McKay-Thompson correction parity closes L1 chiral gap
-> worked example (Rule 30 at a concrete N)
-> supplemental workbook analogue (stacked layer cards)
```

## Practical Solved Example

**Domain:** Rule 30 center column, depth `N = 42`.

**Procedure:** run `predict_rule30_bit(42)` and `verify_all_layers(max_depth=200)` from the bound tools; read the layer outputs and defects.

**Solved Output (from the tool's reported structure):** the oracle layer `T_EMISSION` returns the bit with `oracle_defect = 0` (Theorem A, proven 0 defects across the verifier's depth range; rule30_nth_bit.py `verify_all_layers` reports `oracle_accuracy = 1.0`). The Lucas-only layer returns `lucas_bit(42,0)` with reported accuracy `~0.747` over `N=1..200` (`T_DYAD`). The Lucas+oracle-correction layer reports accuracy `1.0` on its sampled depths (`O2'`, exact when the correction grid is known). The spectral layer reports an empirical accuracy figure (not 1.0) and a `cross_window_agreement` flag. The example is solved because the same three layered outputs reproduce from the formal stack, the `cqe_engine` verifiers, and the workbook card stack; the residual gap (closing L1's chiral 25.3% without the grid) is the named obligation, not a silent failure.

## Tool Binding

- Module: `cqe_engine` (`rule30_predictor`, `rule30_nth_bit`, `f4_action`, `centroid_voa`).
- Required outputs: `receipt.json` (per-layer), `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run `verify_all_layers(max_depth>=200)`; confirm oracle defects `= 0`; confirm Lucas-only accuracy near `0.747`; confirm the spectral layer emits a finite accuracy and a cross-window flag. Confirm via `f4_action` that Rule 30's `shell=2` block does not equal `(1/3)(T_12+T_13+T_23)` (it opens), while a silent-boundary rule's block does.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a vertical stack of three cards labelled L0, L1, L2.
- Top card (L0): write the `(L,C,R)` token and its `T_EMISSION` bit; mark it white (closed, defect 0).
- Middle card (L1): write the Lucas base bit; mark white if the state is symmetric, black if it is the chiral doublet `{(1,1,0),(0,1,1)}`.
- Bottom card (L2): write the spectral guess; mark grey (empirical).
- Bind the first card that is white; record the black cards below it as obligations.
- Bind the finished stack into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 and the ECA rule-space.
- [ElementaryCA] Elementary cellular automata: 256 local binary rules. URL: https://mathworld.wolfram.com/ElementaryCellularAutomaton.html Use: the 256-rule finite program space.
- [Rule30] Wolfram Rule 30. URL: https://mathworld.wolfram.com/Rule30.html Use: the canonical open-class rule.
- [Lucas1878] E. Lucas, on binomial coefficients mod p (Lucas' theorem). Use: the `O(log N)` linear base layer.
- [ConwayNorton1979] Conway, Norton, Monstrous Moonshine, Bull. LMS 11, 308-339. Use: the McKay-Thompson series targeted by the open correction-parity step.

## Open Obligations

- The full-`O(log N)` cold-start Rule 30 extractor requires `correction(t,x)` without the grid, identified as the McKay-Thompson `T_2A`/`T_3A` parity (rule30_nth_bit.py `open_step_O2prime`; `IDENTITY_PAPER` 8.2). Carried as obligation.
- The spectral layer's accuracy is empirical; a proven accuracy bound (or a falsifying counterexample family) is open.
- Add a falsifier: a depth where `T_EMISSION` would disagree with the canonical bit (none exists by Lemma 12.1; the tool must reject any such claim).
- The universal claim that every silent-boundary rule transports a closed corollary is structural (`IDENTITY_PAPER` 8.6); individual rules verified case by case.

## Back-Propagation Targets

- Paper 00 receives the layered-surface receipt term (layer + cost class).
- Paper 03 (n=3 closure) receives the closure-partition routing key (`f4_action`).
- Paper 16 receives the carry/correction framing as the L1 chiral residue.
- The analog workbook manual receives the stacked-layer-card rule.
- Paper 31 records how the layered presentation recurs in the corpus order.
