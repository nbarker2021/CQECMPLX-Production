# Paper 07 - Discrete-Continuous Bridge

## Status

Bridge paper. Establishes the discrete-to-continuous interface of the corpus: the conditions under which a sampled continuous signal enters the same `(L, C, R)` chart machinery as a deterministic binary sequence, and the n=3 closure that the two share. Proof-facing, with explicit separation of static-template results from temporal-trace results. Inherits the Paper 00 contract.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

This paper defines the bridge where discrete state changes approximate continuous dynamics through indexed windows. The corpus registers binary sequences via the chart `(L_n, C_n, R_n) = (c_{n-1}, c_n, c_{n+1})`; a continuous signal enters the same machinery by *indexed discretization* - sampling, thresholding, and parity encoding into a binary tape, after which the identical `shell = 2` conditional transition matrix is computed. The load-bearing claim is that the `n = 3` SU(3) Weyl closure (`IDENTITY_PAPER` Theorem T4) is the *shared* signature across both regimes: it holds for purely discrete sequences (cellular automata, number-theoretic parities) and for discretized continuous measurements (the Planck 2018 cosmic-microwave-background TT spectrum evaluated cumulatively, the Hawking thermal Planck spectrum across mass scales). The bridge is conditional, not universal: closure depends on how the continuous signal is windowed (cumulative versus raw), and the static chart-label template must be distinguished from the actual temporal trace. We surface the closure as an empirical signature catalogued in `IDENTITY_PAPER` Section 6 and verified by the experiment harness, and we carry the universality of the bridge itself as an open obligation.

## Central Thesis

Define the bridge where discrete state changes approximate continuous dynamics through indexed windows.

## Scope Boundary

This paper claims that *indexed discretization* maps a sampled continuous signal into the chart, and that the n=3 closure is the property both regimes can share under the right windowing. It does not claim that every continuous signal closes, nor that closure of a discretized signal proves any physical fact about its source. It explicitly separates the *static* Z4 chart-label template (a property of the 8 chart states, always true) from the *temporal* trace (the actual Rule 30 evolution, which does NOT inherit the static periods - `verify_temporal_z4_scope`). Excess interpretation is logged as obligation.

## Definitions

- **Indexed window**: a fixed-width slice `(c_{n-w}, ..., c_n, ..., c_{n+w})` of a binary tape, indexed by its center position `n`. The corpus base window is `w = 1`, the `(L, C, R)` triple.
- **Indexed discretization**: the encoder taking a real-valued sampled signal `x_1, x_2, ...` to a binary tape, e.g. by thresholding (`b_i = 1` iff `x_i > theta`), parity of a rounded quantum, or cumulative-partial-sum parity. The encoder is the bridge map; it is lossy and must be declared with the receipt.
- **Static chart-label template**: the `four_frame_label` assignment on the 8 chart states and its Z4 orbit structure (`verify_z4_period_template`): a property of the state set, independent of any tape.
- **Temporal trace**: the actual sequence of chart states produced by stepping a dynamical law (e.g. Rule 30) to depth `N`. The temporal trace need not inherit the static template's periodicity.
- **Closure-coherent (sampled)**: a discretized signal whose `shell = 2` conditional transition matrix at `n = 3` is an exact `S_3` group-ring element with residual squared `< 10^-6` (Paper 07 of the PROOF set, Definition 1.1).
- **Cumulative encoding**: the discretization of partial sums `S_k = sum_{i<=k} x_i` rather than raw samples `x_i`; the CMB TT spectrum closes cumulatively but not raw (`IDENTITY_PAPER` 6.4).

## Axioms

Axiom 07.1 - Locality: a discretized signal is admitted only through the same local `(L, C, R)` window as a native binary sequence; no continuous-domain readout bypasses the chart.

Axiom 07.2 - Receipt Preservation: the discretization encoder (sampling rate, threshold, cumulative/raw choice) is part of the receipt; a closure result is meaningless without its declared encoder.

Axiom 07.3 - Boundary Positivity: a signal that fails to close under one encoding but closes under another (raw vs cumulative) is recorded as an encoder-boundary datum, not discarded.

Axiom 07.4 - Analog Exposure Equivalence: the bridge has a supplemental workbook analogue - a strip whose cells are filled by reading a physical gauge (sampling) and a black/white follow-up for closed/open.

## Lemmas

Lemma 07.1 - Static-temporal separation: the static four-frame Z4 label template has a well-defined orbit structure (2 fixed points, 6 period-4 states; `verify_z4_period_template`), but the tested Rule 30 label trace and center column do NOT inherit periods 1, 2, or 4. (Basis: `verify_temporal_z4_scope`, which returns `status = "static_template_only"` with explicit `label_counterexamples` and `center_counterexamples`.) Hence a static chart property may not transport to the temporal trace; the bridge must be checked on the trace itself.

Lemma 07.2 - Shared-signature: when a discretized continuous signal is closure-coherent, its `shell = 2` matrix at `n = 3` is the *same* idempotent `S_3` element `(1/3)(T_(1,2) + T_(1,3) + T_(2,3))` reached by closing discrete sequences (`IDENTITY_PAPER` T4-T5). The closure value does not distinguish discrete from continuous origin - this is what makes it a bridge.

Lemma 07.3 - Encoder-dependence: closure is a property of the (signal, encoder) pair, not the signal alone. The Planck CMB TT spectrum closes under cumulative encoding and does not close raw (`IDENTITY_PAPER` 6.4); the Wow signal closes in raw amplitude, spectral (FFT-magnitude), and ternary encodings (PROOF Paper 07 Section 5.3). The bridge therefore selects the encoder that exposes the underlying continuity.

## Formalism / Calculus Sketch

A bridge state is `B = (x, E, P, Q, O)`: the sampled real signal `x`, the declared encoder `E`, the resulting paper state `P = phi(E(x))`, the closure signature `Q`, and the obligation set `O`. The bridge is accepted when:

```text
E declared and logged in receipt
b = E(x)                          (indexed discretization to binary tape)
chart(b) -> shell=2 conditional transition matrix T
T(3) decomposed in S_3 group ring -> residual r^2
r^2 < 1e-6  => closure-coherent (closed)  else open boundary datum
static-template result NOT assumed for the temporal trace (Lemma 07.1)
```

The discrete limit recovers the native chart: when `x` is already in `{0,1}` and `E` is the identity, `B` reduces to the Paper 00 chart state. The continuous limit is approached by refining the sampling: as the sample spacing shrinks, the indexed window tracks a finer slice of the continuous trajectory, and the closure (when present) is the discrete witness of the trajectory's local smoothness. Tool binding:

```text
cqe_engine  (lattice_forge: temporal_z4_scope.verify_temporal_z4_scope;
             experiment harness exp_hawking_radiation, exp_wow_signal, CMB cumulative section)
```

## Proof Tree

```text
claim (discrete windows bridge to sampled continuous dynamics via n=3 closure)
-> declare encoder E (indexed discretization)
-> separate static template from temporal trace (Lemma 07.1, verify_temporal_z4_scope)
-> compute shell=2 n=3 matrix on the temporal/sampled tape
-> S_3 group-ring decomposition -> residual r^2
-> closure-coherent? (shared signature, Lemma 07.2)
   -> yes: bridge holds for (signal, encoder) (CMB cumulative, Hawking)
   -> no : encoder-boundary datum (raw CMB) -> obligation
-> worked example (CMB cumulative TT spectrum)
-> supplemental workbook analogue (gauge-read strip)
-> receipt (encoder + residual)
```

## Practical Solved Example

**Domain:** the discrete-continuous separation of Rule 30's own trace versus the static chart template (the cleanest reproducible bridge case, since it requires no external data file).

**Procedure:** call `verify_temporal_z4_scope(max_depth = 512)`. It (a) builds the static four-frame Z4 label template via `verify_z4_period_template`; (b) generates Rule 30's canonical rows to depth 512; (c) forms the predecessor `(L, C, R)` states and their four-frame labels; (d) tests whether the temporal label trace and the center column inherit periods 1, 2, or 4; (e) records counterexamples.

**Solved Output:** the routine returns `status = "static_template_only"`: the static template has its Z4 orbit structure, but the temporal trace does NOT inherit periods 1, 2, or 4, with explicit `label_counterexamples` and `center_counterexamples` reported. This is the load-bearing bridge fact: a property true of the discrete state-set (static) does not automatically transport to the continuous-like temporal evolution. The complementary positive case is the cumulative CMB TT spectrum (Planck 2018 R3), which closes exactly under cumulative encoding (`IDENTITY_PAPER` 6.4; PROOF Paper 07 Theorem T_UNIVERSAL_CMB) while the raw spectrum does not - confirming Lemma 07.3's encoder-dependence. The example is solved because the static/temporal split reproduces identically from `verify_temporal_z4_scope`, the formal statement, and the workbook gauge strip.

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.temporal_z4_scope.verify_temporal_z4_scope`; experiment harness `exp_hawking_radiation.py`, `exp_wow_signal.py`, and the CMB cumulative section of `run_all.py`).
- Required outputs: `receipt.json` (must include the declared encoder), `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run `verify_temporal_z4_scope(max_depth >= 512)` and confirm `status = "static_template_only"` with at least one temporal counterexample; emit one closed-bridge row (cumulative encoding) and one open-bridge row (raw encoding) for the same signal.

## Analog Workbook Sheet

- Start with grey loose substrate; lay an indexed strip of cells with a center mark.
- Read a physical gauge (a dial, a ruler, a thermometer) and fill each cell by threshold: above the line = 1, below = 0. Record the threshold on the sheet (this is the encoder).
- Slide the center mark along the strip; at each position read the `(L, C, R)` window.
- White follow-up = the strip's `shell = 2` windows close under the three-token flip; black follow-up = they do not, and the encoder is logged as a boundary.
- Re-fill the same strip with cumulative tallies (running totals) and compare: a strip that opens raw but closes cumulative is the canonical bridge sheet.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 temporal trace as the discrete reference dynamics.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: sampling and lossy-encoder framing for indexed discretization.
- [Planck2018] Planck Collaboration (2020), Planck 2018 results. I. Overview and the cosmological legacy of Planck, Astron. Astrophys. 641, A1. Use: the CMB TT power spectrum as the sampled continuous measurement that closes cumulatively.
- [Kraus1977] J. D. Kraus, R. S. Dixon (1977), Statistical analysis of the Wow signal, Big Ear Radio Observatory. Use: a continuous radio measurement that closes across multiple encodings.

## Open Obligations

- The universal form - "every sampled continuous signal with bounded local variation admits a closure-coherent encoder" - is structural and is carried as an obligation; only specific signals (cumulative CMB, Hawking spectrum, Wow signal) are verified case by case (`IDENTITY_PAPER` 8.6).
- The relationship between sampling rate and closure stability is not derived: at what sampling spacing does a closing signal stop closing? Open.
- The static-to-temporal transport failure (Lemma 07.1) is observed empirically up to depth 512; a proof that no Rule 30 temporal trace inherits the static Z4 periods is open.
- Replace citation anchors with final bibliography entries during peer-review preparation.

## Back-Propagation Targets

- Paper 00 receives the indexed-discretization encoder term (the encoder is now part of every receipt for a continuous-origin claim).
- Paper 01 receives the confirmation that the `shell = 2` doublet is the closure signature shared across discrete and sampled regimes.
- The ForgeFactory / lattice_forge registry records `temporal_z4_scope` as the static/temporal separation witness.
- The analog workbook manual receives the gauge-read bridge strip rule.
- Paper 31 records how the discrete presentation order of the corpus is itself a sampling of a continuous research trajectory.
