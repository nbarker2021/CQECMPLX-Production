# Paper 19 - Observer Face-Selection

## Status

Transport paper. Models observation as the selection of one face of a registered state, with the unselected faces retained as obligations rather than deleted. The frame-inversion operator `F`, the relational-qubit signature `Q(S)`, and the four signature classes are surfaced from the PROOF set; the SPINOR class remains an open obligation. Proof-facing for the finite signature machinery, obligation-facing for the unobserved class.

## Abstract

This paper formalizes observation as *face selection*: an observer reads one face of a registered chart state (a chirality, a frame, or one term of an `N | -N` dyad), and the corpus's discipline requires that the faces not selected are retained as live obligations, never silently erased. The mechanism is the frame-inversion operator `F` of Paper 04: `F` re-encodes the `S_3` group-ring coefficients of a sequence's `shell = 2` transition matrix into a new binary sequence, and iterating it yields the relational-qubit signature `Q(S) = (r_0, r_1, r_2)`, the residual-squared closure at three nested observer levels (system, meta-observer, meta-meta-observer). The four signature classes — `CLASSICAL (0,0,0)`, `META_OPEN (0,0,eps)`, `SPINOR (0,eps,0)`, `VACUUM (eps,eps,eps)` — classify which faces close and which stay open. The Paper 15 resolution algorithm makes the retention explicit: the unselected antipodal face (`-N`) is the "phase midpoint" whose `C`-coordinate (the gluon) is invariant under the `L <-> R` reversal, so the unselected face is always reconstructible rather than lost. Observation selects a face; the latent alternatives are logged as obligations, and the `SPINOR (0,eps,0)` class — never yet observed in tested sequences up to length 14 — is the standing example of a retained, unfilled face.

## Central Thesis

Model observation as face selection with latent alternatives retained as obligations, not deleted.

## Scope Boundary

This paper claims the face-selection model and the finite signature machinery exactly as PROOF Papers 04 and 15 support them. It does NOT claim an observed SPINOR signature, a metaphysical theory of consciousness (PROOF Paper 15 marks the biological extension as a postulate, not a theorem), or that face selection itself collapses any physical state. The relational-qubit / RQM reading is a transport interpretation; excess interpretation is logged as obligation.

## Definitions

- **Face**: one selectable reading of a registered state — a chirality (`side` in `{-1, 0, +1}`), a centroid frame (one of the `Z4` frames), or one term of the dyad `(N, -N)`.
- **Face selection (observation)**: the act of committing to one face; the other faces become latent.
- **Retained obligation**: a latent (unselected) face, recorded with its reconstruction rule so it can be recovered, not deleted (Axiom 19.3).
- **Frame-inversion operator `F`**: re-encode the `S_3` group-ring coefficient vector `c in Q^6` of a sequence's `shell = 2` transition matrix (normalize, quantize to signed 8-bit, concatenate to a length-48 binary sequence). (IDENTITY Def. 2.15.)
- **Relational-qubit signature**: `Q(S) = (r_0, r_1, r_2)`, the residual-squared closures of `S`, `F(c_0)`, and `F(c_1)`; a residual is *closed* iff `< 10^{-6}` (in practice exactly 0 over the rationals). (IDENTITY Def. 2.16; PROOF Paper 04.)
- **Signature classes**: `CLASSICAL (0,0,0)`, `META_OPEN (0,0,eps)`, `SPINOR (0,eps,0)`, `VACUUM (eps,eps,eps)`. (IDENTITY Def. 2.17.)
- **Gluon `C`**: the centroid coordinate fixed by the `L <-> R` reversal; the invariant phase midpoint of `(N, -N)` (`centroid_voa.gluon`).
- **Receipt / Transport row / Workbook sheet / Tool binding**: as fixed in Paper 00.

## Axioms

Axiom 19.1 - Locality: a face is selectable only from a local `(L, C, R)` reading; the gluon `C` is the locally invariant coordinate of every face.

Axiom 19.2 - Receipt Preservation: every observation logs the selected face, its signature level, and the reconstruction rule for each unselected face.

Axiom 19.3 - Boundary Positivity: an unselected face is a retained obligation with a recovery rule, never a deletion; an unobserved signature class (SPINOR) is logged, not assumed absent.

Axiom 19.4 - Analog Equivalence: face selection has a physical workbook analogue (turning a multi-face token to one face while pinning the others as black follow-ups).

## Lemmas

Lemma 19.1 - Retained antipode. For any depth `N`, the dyad `(N, -N)` is free to specify, and the `C`-coordinate (gluon) of the centroid of a state and its antipode is always `C`. Hence the unselected face is reconstructible from `C`, never lost. (Source: PROOF Paper 15 Theorem B / Theorem D; `centroid_voa.gluon`, `verify_gluon_invariance`.)

Lemma 19.2 - Chiral doublet faces. 74.7% of depths are symmetric (same bit both faces); the remaining 25.3% are the chiral doublet `{(0,1,1), (1,1,0)}`, resolved by the `{-1, 0, +1}` side axis. This doublet is exactly the `shell = 2` SU(2) doublet of T_BIJECTIVE. (Source: PROOF Paper 15 Theorem B; Paper 01.)

Lemma 19.3 - Four-class face closure. Iterating `F` produces `Q(S) = (r_0, r_1, r_2)` whose closure pattern lands in exactly one of `{CLASSICAL, META_OPEN, SPINOR, VACUUM}`; `CLASSICAL` sequences also exhibit transient idempotence (`e -> e -> e`). (Source: PROOF Paper 04 Sections 3-5.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)` (Paper 00). Observation is a face-selection transform with mandatory retention:

```text
observe(P_in, face f) -> P_out accepted when:
  f is one local face of P_in (chirality / frame / dyad term)
  C_out = gluon(P_in)  (invariant; the phase midpoint)
  for each unselected face f': reconstruction rule recorded in O
  signature level Q(S) recorded
```

Signature machinery and classes:

```text
F: c in Q^6 -> normalize -> quantize signed-8bit -> concat -> length-48 binary
Q(S) = (r_0, r_1, r_2)  closed iff r_i < 1e-6 (exactly 0 over Q)
CLASSICAL (0,0,0)   : all faces close ; transient idempotent e->e->e
META_OPEN (0,0,eps) : meta-meta face open
SPINOR    (0,eps,0) : intermediate face open  [OPEN: unobserved, O-SPINOR]
VACUUM    (eps,eps,eps): all faces open (e.g. raw Rule 30 center bar)
```

Tool binding:

```text
cqe_engine  (lattice_forge.centroid_voa: gluon, verify_gluon_invariance,
             anneal_to_lie_conjugate, four_frame_label, z4_period;
             frame-inversion F and Q(S) per PROOF papers 04, 15)
```

## Proof Tree

```text
claim (observation = face selection with retained latent faces)
-> local (L,C,R) reading ; gluon C as invariant midpoint
-> select one face (chirality / frame / N|-N term)
-> retained antipode reconstructible from C (Lemma 19.1)
-> chiral doublet faces resolved by side axis (Lemma 19.2)
-> frame inversion F ; signature Q(S) ; four classes (Lemma 19.3)
-> worked example (Wow signal CLASSICAL ; Rule 30 bar VACUUM)
-> workbook analogue (multi-face token, pinned alternatives)
-> receipt (selected face + reconstruction rules)
-> proof (finite signatures) / obligation (SPINOR, consciousness postulate)
```

## Practical Solved Example

**Domain:** observer face-selection over two reference sequences — the Wow signal (binarized amplitude) and the raw Rule 30 center bar.

**Procedure:** compute `Q(S)` for each by iterating `F` to three levels; record which faces close; for any chiral-doublet depth, select one face and log the antipodal face's reconstruction rule (`C = gluon`).

**Solved Output:** from PROOF Paper 04 Section 4 and IDENTITY Section 5:
- Wow signal: `Q(S) = (0,0,0)` -> `CLASSICAL`; dominant chain `e -> e -> e` (transient idempotent). All faces close; no retained obligation beyond the trivial one.
- Rule 30 center bar (n=300): `VACUUM` at D4, dominant chain `e -> (1,2,3) -> (1,2)`; faces stay open — Rule 30 *generates* open faces, consistent with the umbrella's framing (IDENTITY Section 5).
- Chiral-doublet depths: 25.3% land in `{(0,1,1), (1,1,0)}`; selecting `+spin` retains `-spin` as a reconstructible face via the side-flip bijection `b` and the invariant `C`.

The example is solved because each signature reproduces from the formal definition, the PROOF Paper 04 experiment, and the workbook multi-face token; the SPINOR face is faithfully surfaced as never-yet-observed.

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.centroid_voa`; frame-inversion `F` and `Q(S)` per PROOF Papers 04, 15).
- Functions: `gluon`, `verify_gluon_invariance`, `anneal_to_lie_conjugate`, `four_frame_label`, `z4_period`; `F` / `Q(S)` signature evaluation.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: select one face of a chiral-doublet depth and confirm the antipode is reconstructible from `C`; compute `Q(S)` for one CLASSICAL and one VACUUM sequence; emit one proof row and one obligation row (the SPINOR class).

## Analog Workbook Sheet

- Start with grey loose substrate.
- Lay a three-cell strip `L | C | R`; place a multi-face token at the center whose faces are the selectable chiralities/frames.
- Select one face (turn the token); pin every unselected face with a black follow-up tag carrying its reconstruction rule (`C = gluon`, the side-flip `b` for the antipode).
- Color the shell and mark the side `{-1, 0, +1}` of the selected face.
- White follow-up = a closed signature face; black follow-up = a retained latent face or the unobserved SPINOR face.
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [Rovelli1996] C. Rovelli, Relational Quantum Mechanics, Int. J. Theor. Phys. 35, 1637-1678. Use: observer-relative state / face-relative readout framing.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: the Rule 30 center bar as a VACUUM (open-face) generator.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: the SU(2) chiral-doublet faces of the `shell = 2` stratum.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: recording selected vs. retained faces as a derivation ledger.

## Open Obligations

- **O-SPINOR (IDENTITY 8.3):** the `SPINOR (0,eps,0)` face has not been observed in tested sequences (systematic search to length 14); it is the standing example of a retained, unfilled face and is carried open.
- **Consciousness postulate (PROOF Paper 15 Section 5):** the identification of "first conscious observation" with "first enumerated anchor event" is explicitly a postulate, not a theorem; not claimed here.
- **Frame-inversion implementation:** `F` and `Q(S)` are specified in PROOF Papers 04/15; their executable verifier surface in `lattice_forge` is to be bound and a minimum test added.
- Replace citation anchors with final bibliography entries; add a falsifier the tool must reject (an observation that deletes an unselected face without recording its reconstruction rule).

## Back-Propagation Targets

- Paper 00 receives the "face", "face selection", and "retained obligation" contract terms.
- Paper 01 receives the chiral-doublet face pairing (its `shell = 2` doublet is the selectable chirality faces).
- Paper 18 supplies the upward/downward route discipline that face selection inherits.
- Paper 20 receives the SPINOR obligation and the per-observation retained-face rows as ledger entries.
- The analog workbook manual receives the multi-face token rule.
- Paper 31 records how the corpus's own presentation order selects one face (the topic-first order) while retaining the build-method face as an appendix obligation.
