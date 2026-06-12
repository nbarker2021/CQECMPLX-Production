# Paper 16 - Continuum Edge Residuals

## Status

Application paper. Uses powers of ten and edge residuals as practical windows into unsolved continuum depth, grounded in the digit-rollout argument (PROOF Paper 16, "The Digit Rollout") and the carry/correction apparatus. Proof-facing for the local rollout and `T_WRAP` closure; obligation-facing for the global continuum depth that finer resolution keeps exposing. Builds on Papers 00, 01, 03, 12.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

A positional number is not a stored integer but a *dimensional state*: the symbol `1000` means position 3 active with positions 2, 1, 0 confirmed reset, and to mean that, a reader must in principle have rolled each lower bar from `0` to `9` and back to rest (PROOF Paper 16, "The Digit Rollout"). Each power of ten is the same rollout one level higher; refining resolution (adding a digit) does not finish the count, it exposes a new *edge residual* — the carry in flight at the boundary between the resolved interior and the not-yet-resolved next position. This paper makes that "local-inside-global" structure a practical instrument. The local side is closed: every 3-bit neighborhood anneals to one of the four Lie-conjugate rest states `{(0,0,0),(0,1,0),(1,0,1),(1,1,1)}` in at most three `S_3` transposition steps (`T_WRAP`, `centroid_voa.py` `verify_hamming_centroid_universality`), and the carry event is exactly the frustrated state `C=1, R=0`, with local correction `NOT(L)` (PROOF Paper 16 Sections III, V, VI). The global side is open: the propagating-correction sum over the light cone (the ~10% of carries that survive the skip-pad filter) requires the McKay-Thompson series parity to collapse from `O(N)` to `O(log N)` (PROOF Paper 16 Section VI; `IDENTITY_PAPER` 8.2). Powers of ten give the practical windowing scale; edge residuals are the readable trace of the continuum depth that each finer window re-exposes rather than removes.

## Central Thesis

Use powers of ten and edge residuals as practical windows into unsolved continuum depth.

## Scope Boundary

This paper claims: (1) the digit-rollout reading of positional notation as a dimensional state (PROOF Paper 16); (2) the local closure `T_WRAP` (every state anneals in `<=3` `S_3` steps) and the local carry identification (`C=1, R=0`, correction `NOT(L)`), both reproducible by named verifiers; (3) that powers of ten are a practical windowing scale and edge residuals are the readable trace of continuum depth. It does NOT claim the global continuum is resolved: the propagating-correction sum's collapse to `O(log N)` is an obligation (the McKay-Thompson primitive). It does not claim that adding digits ever terminates the count. Any reading that treats edge residuals as a closed-form continuum solution is out of scope.

## Definitions

- **Dimensional state**: a positional value read as which positions are active and which are confirmed reset; `1000` = position 3 active, positions 2,1,0 reset (PROOF Paper 16 Section IV).
- **Rollout**: the in-principle traversal of a digit position from `0` through its base back to rest; the reset to zero is the act that licenses the next position (PROOF Paper 16 Section IV).
- **Edge residual**: the carry in flight at the boundary between resolved interior and the next position; the frustrated state `C=1, R=0` (PROOF Paper 16 Section VI).
- **Carry event / frustrated bond**: the `shell`-window state where the gluon `C` is active but the write wire `R` is silent; resolved locally by `NOT(L)` (PROOF Paper 16 Sections III, V).
- **Lie-conjugate rest state**: one of `{(0,0,0),(0,1,0),(1,0,1),(1,1,1)}`, the `L=R` attractors where read and write balance (`centroid_voa.py` `LIE_CONJUGATES`).
- **Power-of-ten window**: a resolution scale `10^k`; the practical aperture for sampling the rollout; corpus page size is the `Z/2` analog at `4096 = 2^12` (`IDENTITY_PAPER` 8.5).
- **Continuum depth (OBLIGATION)**: the global structure that each finer window re-exposes; not closed here.

## Axioms

Axiom 16.1 - Locality: an edge residual is read from a local `(L,C,R)` carry window before any global interpretation (Axiom 00.1).

Axiom 16.2 - Receipt Preservation: every rollout step logs the bar's extension, its reset, and any carry residue (Axiom 00.2).

Axiom 16.3 - Boundary Positivity: a carry in flight is the edge residual, not an error; finer resolution exposes more residual, never less (Axiom 00.3).

Axiom 16.4 - Analog Exposure Equivalence: the rollout has a supplemental workbook analogue (a bar that extends and returns to rest before the next bar may begin).

## Lemmas

Lemma 16.1 - Local rollout always closes. Every one of the 8 chart states anneals to a Lie-conjugate rest state in at most 3 `S_3` transposition steps, independent of the CA rule (`T_WRAP`; `centroid_voa.py` `verify_hamming_centroid_universality`, claim "all 8 chart states close to a Lie conjugate in <=3 S3 steps"). The bound 3 is tight: it is the number of transpositions to reach identity in `S_3` (PROOF Paper 16 Section V).

Lemma 16.2 - The edge residual is exactly the frustrated carry. The carry fires iff `C=1, R=0`; the term distinguishing Rule 30 from the linear base Rule 90 is precisely `C AND NOT R` (PROOF Paper 16 Sections III, VI; `rule90_linearization.py` correction). This is the readable local trace of the rollout's incomplete carry.

Lemma 16.3 - Finer resolution exposes, not closes. Each power of ten is the rollout one level higher (PROOF Paper 16 Section IV); ~90% of carry-firing positions are skip pads that cancel globally and ~10% propagate (PROOF Paper 16 Section VI; `rule30_nth_bit.py`). Adding a digit re-exposes a new edge residual; the global propagating sum is `O(N)` until the McKay-Thompson parity collapses it (OPEN, `IDENTITY_PAPER` 8.2).

## Formalism / Calculus Sketch

The instrument windows the rollout at a power-of-ten scale and reads the edge residual:

```text
edge_read(value, window 10^k):
  resolve interior digits 0..k-1 (rolled to rest)   [Lemma 16.1, T_WRAP]
  read boundary state at position k:
     if C=1 and R=0:  edge residual = carry in flight [Lemma 16.2]
        local correction = NOT(L)                      [PROOF P16 V]
     else:            no residual at this edge (rest)
  refine: window -> 10^(k+1)
     re-exposes a NEW edge residual at position k+1    [Lemma 16.3]
  global: sum propagating carries over light cone       [O(N), OPEN]
  emit receipt(window, edge residual, local correction)
```

The continuum depth is the limit the windowing never reaches: `Rule_30_center(N) = LucasBit(N,0) XOR sum_corrections`, where the Lucas base is the structurally predictable quasi-period and the correction sum is the aggregate of surviving edge residuals (PROOF Paper 16 Sections VI, IX). Tool binding:

```text
cqe_engine  (centroid_voa: anneal_to_lie_conjugate, LIE_CONJUGATES, T_WRAP;
             rule90_linearization: lucas_bit, correction (C AND NOT R);
             rule30_nth_bit: predict_bit_lucas_correction, skip-pad survival)
```

## Proof Tree

```text
claim (powers of ten + edge residuals = windows into continuum depth)
-> dimensional-state reading of positional notation (PROOF P16 IV)
-> Lemma 16.1: local rollout closes in <=3 S_3 steps (T_WRAP)
-> Lemma 16.2: edge residual = frustrated carry C=1,R=0, corr = NOT(L)
-> Lemma 16.3: finer resolution re-exposes a new edge residual
-> global correction sum over light cone (O(N))
-> continuum depth closure => OBLIGATION (McKay-Thompson parity)
-> worked example (rollout windows on Rule 30 center column)
-> supplemental workbook analogue (bar extends, returns to rest, next bar begins)
-> receipt + obligation split
```

## Practical Solved Example

**Domain:** Rule 30's center column, windowed at increasing power-of-ten depths, reading edge residuals.

**Procedure:** for a sample depth `N`, anneal the local state via `anneal_to_lie_conjugate` and confirm it reaches a Lie-conjugate rest state in `<=3` steps; identify carry positions by `C=1, R=0` and apply local correction `NOT(L)`; run `predict_bit_lucas_correction(N)` to separate the Lucas base from the propagating correction residue; refine the window and observe a fresh edge residual.

**Solved Output:** every sampled state closes locally in `<=3` steps (Lemma 16.1; `verify_hamming_centroid_universality` passes). The carry positions are exactly `C=1, R=0`, corrected by `NOT(L)` (Lemma 16.2). The Lucas base predicts ~74.7% of center bits; the surviving ~10% of carries are the propagating edge residuals that the base misses (Lemma 16.3; `rule30_nth_bit.py` reports oracle accuracy `1.0` with the residue included, Lucas-only ~`0.747`). Refining from `10^k` to `10^(k+1)` re-exposes a new edge residual rather than finishing the count. The example is solved at the local/windowing layer: the rollout closure and edge-residual reading reproduce from the formal sketch, the `cqe_engine` verifiers, and the workbook bar. The global continuum closure (collapsing the `O(N)` correction sum) is the obligation below.

## Tool Binding

- Module: `cqe_engine` (`centroid_voa`, `rule90_linearization`, `rule30_nth_bit`).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: confirm `verify_hamming_centroid_universality` passes (all 8 states close `<=3` steps); confirm carry firing exactly at `C=1, R=0`; confirm `predict_bit_lucas_correction` is exact with the correction grid and Lucas-only is ~`0.747`; confirm an obligation row for the `O(N) -> O(log N)` correction-sum collapse.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a vertical stack of bars, one per digit position (units, tens, hundreds, ...).
- Extend the units bar through its count and return it to rest before extending the tens bar (the rollout discipline).
- Mark a carry in flight (`C=1, R=0`) at any boundary with a black edge token; apply `NOT(L)` to read it.
- White follow-up = a position fully rolled to rest (closed); black follow-up = the edge residual at the current window AND the global continuum depth — bound as obligation cards.
- Bind into the matching color notebook; refining the window adds a new bar above, with its own fresh edge token.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 as the windowed sequence.
- [Lucas1878] E. Lucas, binomial coefficients mod p (Lucas' theorem). Use: the quasi-periodic base of the digit rollout.
- [ConwayNorton1979] Conway, Norton, Monstrous Moonshine, Bull. LMS 11, 308-339. Use: the McKay-Thompson series governing which edge residuals propagate (OPEN target).
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: the receipt/encoding view of each rollout window.
- [OEIS] On-Line Encyclopedia of Integer Sequences. URL: https://oeis.org/ Use: the integer-sequence / digit-pattern repository for cross-checking rollout traces.

## Open Obligations

- Collapsing the propagating-correction sum from `O(N)` to `O(log N)` requires the McKay-Thompson `T_2A`/`T_3A` parity primitive (PROOF Paper 16 Section VI; `IDENTITY_PAPER` 8.2). This is the continuum-depth closure and is OPEN.
- "Edge residuals as windows into continuum depth" is an instrument framing; a closed-form continuum solution is NOT claimed and adding digits never terminates the count.
- The ~90% skip-pad / ~10% propagating split is reported empirically (PROOF Paper 16); a proven survival law is OPEN.
- Add a falsifier: a depth where local rollout fails to close in `<=3` steps (none exists by Lemma 16.1; the tool must reject any such claim).

## Back-Propagation Targets

- Paper 00 receives the dimensional-state / receipt-per-window reading.
- Paper 12 receives the edge residual as the L1 chiral/correction residue of the prediction surface.
- Paper 15 (horizon) receives the surviving-residue-as-carrier link.
- The analog workbook manual receives the stacked-bar rollout rule.
- Paper 31 records how the windowing-into-depth recurs in the corpus presentation order.
