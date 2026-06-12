# Paper 00 - Baseline Transport Contract

## Status

Foundational contract paper. Defines the corpus-wide substrate, vocabulary, and acceptance discipline that every later paper inherits. Proof-facing.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

This paper fixes the contract under which the entire corpus operates. Every claim in every later paper is a *transported state*: a local `(L, C, R)` readout window, an algebraic registration of that window into a known mathematical object, a transform that moves the registered state, and a replayable receipt that records the move together with any unresolved residue. The load-bearing object is the exceptional Jordan algebra `J_3(O)` of `3x3` Hermitian octonionic matrices and its automorphism group `F_4`; the load-bearing primitive is the chart-to-`J_3(O)` map `phi(L, C, R) = diag(L, C, R)`, under which the local readout law is exactly Wolfram's Rule 30. The contract's purpose is to make every downstream result a *transport of known theorems* onto a registered sequence, rather than a fresh claim requiring independent proof. Acceptance is local, receipts are mandatory, failures are data, and every main-corpus claim has a physical workbook analogue. Build-method details are retained only in appendices, receipts, and the Paper 31 meta-walkthrough.

## Central Thesis

Define the corpus-wide contract: every claim is a transported state with provenance, receipt, worked example, tool binding, and workbook representation, registered through the chart-to-`J_3(O)` substrate so that classical theorems transport onto the registered object as corollaries.

## Scope Boundary

This paper claims only the contract itself and the substrate definitions it rests on. It does not prove the downstream applications; it specifies the form every downstream proof result or audit residue must take. Any interpretation that exceeds what the math, proof tree, citations, tool receipts, and supplemental workbook evidence can support is logged as an obligation rather than promoted to proof.

## Definitions

- **Chart**: for a binary sequence `c_1, c_2, ...`, the sequence of overlapping triples `(L_n, C_n, R_n) := (c_{n-1}, c_n, c_{n+1})`, indexed `n = 2, 3, ...`.
- **Chart state**: an element `(L, C, R)` of `{0,1}^3`; there are exactly 8, indexed by `4L + 2C + R`.
- **Shell**: `shell(L, C, R) := L + C + R` in `{0, 1, 2, 3}` — the integer occupancy of the window. It is the `J_3(O)` trace of the registered element.
- **Side (chirality)**: `side(L, C, R) := sgn(R - L)` in `{-1, 0, +1}`.
- **Readout law**: `bit(L, C, R) := 1` iff `shell = 1`, or `shell = 2 and R > L`. By enumeration this equals `L XOR (C OR R)`, which is Rule 30.
- **C as the active center**: `C` is the center of the readout window — the local quantity preserved under the `L <-> R` reflection. `L` and `R` are the two opposed boundary directions read relative to `C`.
- **Transport row**: a typed record carrying a claim, its source, the transform applied, the resulting state, and its obligation status.
- **Receipt**: a replayable record of an operation — its inputs, output, and unresolved residue.
- **Supplemental workbook sheet**: the analog (physical) realization of a proof state through color, token, string, page, and white/black follow-up.
- **Tool binding**: the ForgeFactory / lattice-forge module family that makes a paper executable and testable.

## Axioms

Axiom 00.1 - Locality: every accepted claim must be readable through a local `(L, C, R)` window before it is lifted to a larger frame.

Axiom 00.2 - Receipt Preservation: no transform is accepted unless its inputs, output, and unresolved residue can be logged and replayed.

Axiom 00.3 - Boundary Positivity: failed, partial, or mismatched routes are data; they become obligations or correction surfaces, never silent deletions.

Axiom 00.4 - Analog Exposure Equivalence: if a claim belongs to the main corpus, it can be exposed through a physical workbook analogue that encodes the same center, boundary, and obligation state.

## Lemmas

Lemma 00.1 - If a local state preserves `C` and records its `L/R` residue, it can be transported into a proof ledger without erasing unresolved alternatives. (Basis: the readout law depends only on `shell` and `side`, both reconstructible from `(L, C, R)`.)

Lemma 00.2 - A tool output and a supplemental workbook sheet that encode the same center, boundary, and obligation state are equivalent receipts at different media layers.

Lemma 00.3 - The readout law is Rule 30. (Verified by enumeration of all 8 chart states; see the truth table in Paper 01 and `IDENTITY_PAPER` Lemma 2.6.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)`: center, two boundary readouts, boundary rule `B`, tool transform `T`, and obligation set `O`. A local transform is accepted when:

```text
T(P_in) -> P_out
receipt(P_in, T, P_out, O) exists and is replayable
C_out is defined
unresolved residue is recorded in O, not erased
```

The substrate registration is the map `phi(L, C, R) = diag(L, C, R)` into the diagonal subalgebra of `J_3(O)`. Under `phi`: `shell = trace`, the `L <-> R` reflection is the `(1 3)` permutation, and the `shell = 2` stratum maps to the three trace-2 idempotents. Because `phi` is a structure-preserving bijection (Paper 03 / `IDENTITY_PAPER` Theorem T3), any theorem about `F_4` acting on `J_3(O)` transports onto the registered sequence. For Paper 00 the tool binding is:

```text
cqe_engine  (lattice_forge substrate: chart, readout, J_3(O) registration, receipts)
```

## Proof Tree

```text
claim
-> local (L,C,R) window
-> readout law (= Rule 30)
-> J_3(O) registration (phi)
-> transported theorem (F_4 corollary) OR logged obligation
-> worked example (non-toy)
-> supplemental workbook analogue
-> receipt
-> proof result / audit residue split
```

## Practical Solved Example

**Domain:** Rule 30's canonical center column, the corpus's reference sequence.

**Procedure:** generate the chart of the center column to depth 4096; register each chart state via `phi`; verify the five preservation properties (bijection, trace = shell, Weyl = `(1 3)`, `shell=2` -> trace-2 idempotents, readout = diagonal emission); emit a receipt of the check counts.

**Solved Output:** the registration holds with zero mismatches across 6,272 individual checks at 4096 depths (`IDENTITY_PAPER` Section 3; `verify_chart_j3o_isomorphism`). The example is solved because the same five properties can be reproduced from the formal statement, the `cqe_engine` verifier, and the analog workbook sheet.

## Tool Binding

- Module: `cqe_engine` (re-exporting the `lattice_forge` substrate).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: register Rule 30's chart at depth >= 4096 and confirm zero preservation mismatches; emit at least one proof row and one obligation row.

## Analog Workbook Sheet

- Start with grey loose substrate.
- Place the `C` token at the local center; place `L` and `R` tokens to either side.
- Color the shell (count of set bits) and mark the side (which boundary leads).
- Use string to bind the accepted transport route.
- White follow-up = proof continuation; black follow-up = obligation / unresolved residue.
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 and the elementary CA framing.
- [JordanVonNeumannWigner1934] P. Jordan, J. von Neumann, E. Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: the `J_3(O)` substrate.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: information channel / receipt framing.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: provenance and derivation ledgers.

## Open Obligations

- The contract asserts that any deterministic system with a lossless encoder into `F_4` inherits the same downstream transport (`IDENTITY_PAPER` 8.6); the universal form of this claim is structural and is carried as an obligation, with specific systems verified case by case in later papers.
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add one falsifier case the tool must reject or defer.

## Back-Propagation Targets

- This paper is the back-propagation sink: any new contract term required by a later paper is added here.
- The ForgeFactory / lattice_forge registry records the `cqe_engine` substrate surface.
- The analog workbook manual records the base `(C, L, R)` sheet rule.
- Paper 31 records how the presentation order of the corpus is itself an enacted `(L, C, R)` process.
