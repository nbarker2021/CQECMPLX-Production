# Paper 09 - Hamiltonian Temporal Emergence

## Status

Temporal-emergence paper. Describes how a global temporal structure (the ordered corpus of papers, or the depth axis of a sequence) emerges as the readout of sliding local windows whose centers `C` are carried forward and back. Establishes the iterated 1-3 / 1-5 / 1-7 bar reading and ties it to the static/temporal separation of the chart. Proof-facing. Inherits the Paper 00 contract.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

This paper describes local-inside-global temporal emergence as Hamiltonian-window readout over transported states. A "Hamiltonian window" is a fixed-width sliding frame over an ordered sequence of already-transported states; reading the window forward (carry the centers `C` along) and backward (validate the reverse transport) produces a surviving composite center that is itself a new state at the next order. Iterating this readout - first with 1-3 bar (3-frame) windows, then 1-5 bar (5-frame), then 1-7 bar (7-frame) - emits successive higher-order states, exactly as `hamiltonian_windows.iterative_hamiltonian` emits Papers 6, 7, 8 from the base C-forms of Papers 0-5 (`BASE_C_FORMS`). The global temporal object (the paper sequence, or the depth-indexed trace) is therefore not assumed; it *emerges* as the fixed point of local window reads. We ground the local-center primitive in `IDENTITY_PAPER` Section 2 (the chart's center `C` is the quantity preserved under the `L <-> R` reflection) and the temporal subtlety in `temporal_z4_scope`: the static window template does not by itself dictate the temporal trace, so emergence must be read off the actual carried states, not inferred from the static frame.

## Central Thesis

Describe local-inside-global temporal emergence as Hamiltonian-window readout over transported states.

## Scope Boundary

This paper claims the window-readout mechanism and its iteration through orders 2, 3, 4 (1-3, 1-5, 1-7 bar), as realized by `iterative_hamiltonian`. It does NOT claim that the emergent higher-order states are independently validated theorems - they are *composites* of their source centers, carried with provenance, and the validity of each underlying center is the responsibility of its own paper. The reverse-pass `validated: True` flag in `read_backward` asserts only that the reverse transport string is well-formed, not that the physics is proved. Excess interpretation is logged as obligation.

## Definitions

- **C-form**: the surviving center of a paper - the local quantity it preserves (`BASE_C_FORMS`). Examples: Paper 0 `Gluon_Gamma = C(L,C,R)`; Paper 1 `SideFlip_C1 = side-flip fixed center (1,0,1)`; Paper 3 `Triality_C3 = true vacua {(0,0,0),(1,1,1)}`; Paper 4 `Repair_C4 = oloid midpoint s* = (N + -N)/2`; Paper 5 `Carrier_C5 = accumulated XOR mass`, verified at `K_max = 9`.
- **Hamiltonian window**: a fixed-width slice of width `w in {3, 5, 7}` over the ordered C-form sequence, indexed by its start (`hamiltonian_read`). Order 2 -> width 3, order 3 -> width 5, order 4 -> width 7 (`window_sizes = {2:3, 3:5, 4:7}`).
- **Forward pass**: the carry-forward read `carry_forward` - concatenate the window's centers into a transport string `C_0 -> C_1 -> ... -> C_k` and form the composite center `C[name_0...name_k]`.
- **Backward pass**: the reverse read `read_backward` - reverse the transport string `C_k <- ... <- C_0` and emit the surviving `hamiltonian_C` (the composite center), flagged `validated: True` for well-formedness.
- **Surviving center**: the `surviving_C` of a `WindowRead` - the composite center that survives both passes and becomes a state at the next order.
- **Order / bar**: the readout depth; 1-3 bar = order 2 over Papers 0-5 -> Paper 6; 1-5 bar = order 3 over Papers 0-6 -> Paper 7; 1-7 bar = order 4 over Papers 0-7 -> Paper 8 (module docstring).
- **Temporal emergence**: the appearance of the global ordered sequence as the fixed point of iterated local window reads, rather than as a pre-given timeline.

## Axioms

Axiom 09.1 - Locality: every emergent higher-order state is read from a single fixed-width window of already-local states; no global timeline is consulted to produce it.

Axiom 09.2 - Receipt Preservation: each `WindowRead` records its order, window size, start index, source C-sequence, forward pass, and backward pass - a replayable receipt of the emergence step.

Axiom 09.3 - Boundary Positivity: a window that cannot be read (fewer source states than the window width, `hamiltonian_read` returns `[]`) is a recorded boundary - "not enough papers yet" - not an error.

Axiom 09.4 - Analog Exposure Equivalence: the readout has a supplemental workbook analogue - a sliding cardboard frame of 3, 5, or 7 cells dragged across a row of center-tokens, with a forward and a flip-back trace.

## Lemmas

Lemma 09.1 - Center carry: a Hamiltonian window's forward pass carries the centers `C` of its source states without erasing them (`carry_forward` concatenates the full center string). (Basis: the readout law and the corpus rely only on `C` being preserved under the `L <-> R` reflection, `IDENTITY_PAPER` 2.1 / Definition 2.5; Paper 00 Lemma 00.1.) Hence the composite center is reconstructible from its parts.

Lemma 09.2 - Order recursion: reading order `k` over `m` source states emits `m - w + 1` surviving centers (`w` the window width), whose union is the single state at the next paper index. (Basis: `iterative_hamiltonian` appends `paper6_c, paper7_c, paper8_c`, each the `||`-join of its order's surviving centers.) The orders are strictly sequential: order 2 must run before order 3 has its Paper 6 input.

Lemma 09.3 - Static frame insufficiency: the window frame is a static object (a fixed width), but the surviving centers depend on the actual transported states inside it, which form a temporal trace that does not inherit the static frame's periodicity. (Basis: `verify_temporal_z4_scope` returns `status = "static_template_only"`; the temporal label trace fails periods 1, 2, 4.) Hence temporal emergence must be read off the carried states, not predicted from the frame alone.

## Formalism / Calculus Sketch

A window read is `H = (k, w, i, S, fwd, bwd, C*)`: order `k`, width `w`, start `i`, source slice `S = [s_i, ..., s_{i+w-1}]`, forward pass `fwd`, backward pass `bwd`, and surviving center `C*`. A read is accepted when:

```text
w = window_sizes[k]                          (3, 5, or 7)
len(source) >= w                             else [] (Axiom 09.3 boundary)
fwd = carry_forward(S)  -> transport "C_i -> ... -> C_{i+w-1}", composite_C
bwd = read_backward(fwd, S) -> reverse string, hamiltonian_C = fwd.composite_C
C* = bwd.hamiltonian_C                        (survives both passes)
next-order state = "||".join(C* over all windows at order k)
```

Emergence is the fixed-point iteration: start with `BASE_C_FORMS` (Papers 0-5), apply order 2 to emit Paper 6, append it, apply order 3 to emit Paper 7, append, apply order 4 to emit Paper 8. The global ordered corpus is the limit of this local process - local-inside-global. The window's reach is bounded by the sheet `K = 9` carrier (Paper 5 `Carrier_C5` verified at `K_max = 9`, cross-referenced to the Nebe sheet bound of Paper 08). Tool binding:

```text
cqe_engine  (hamiltonian_windows: iterative_hamiltonian, hamiltonian_read, carry_forward,
             read_backward, BASE_C_FORMS; lattice_forge.temporal_z4_scope for the
             static/temporal separation)
```

## Proof Tree

```text
claim (global temporal order emerges from local window reads)
-> BASE_C_FORMS (Papers 0-5 centers)
-> order 2 (1-3 bar): 3-frame windows -> surviving centers -> Paper 6
-> order 3 (1-5 bar): 5-frame windows over 0-6 -> Paper 7
-> order 4 (1-7 bar): 7-frame window over 0-7 -> Paper 8
-> each read: forward carry (Lemma 09.1) + backward validate
-> static frame insufficiency (Lemma 09.3, verify_temporal_z4_scope)
-> emergence = fixed point of iterated reads (Lemma 09.2)
-> worked example (iterative_hamiltonian run)
-> supplemental workbook analogue (sliding frame over center-tokens)
-> receipt (per-WindowRead)
```

## Practical Solved Example

**Domain:** the iterated Hamiltonian reading of the corpus's own base centers.

**Procedure:** call `iterative_hamiltonian()`. It (a) copies `BASE_C_FORMS` (Papers 0-5: `Gluon_Gamma`, `SideFlip_C1`, `Correction_C2`, `Triality_C3`, `Repair_C4`, `Carrier_C5`); (b) runs `hamiltonian_read(2, papers)` - 3-frame windows over the six base centers - and joins the surviving centers into `paper6_c`; (c) appends Paper 6 and runs `hamiltonian_read(3, papers)` - 5-frame windows over Papers 0-6 - into `paper7_c`; (d) appends Paper 7 and runs `hamiltonian_read(4, papers)` - the 7-frame window over Papers 0-7 - into `paper8_c`.

**Solved Output:** order 2 over six base centers yields `6 - 3 + 1 = 4` window reads (start indices 0-3), whose surviving composite centers join into Paper 6's C-form `Hamiltonian_2nd`, with `window = 3` and recorded `source_windows = [(0,2),(1,3),(2,4),(3,5)]`. Order 3 over the now-seven papers yields `7 - 5 + 1 = 3` reads -> Paper 7 `Hamiltonian_3rd`, `window = 5`. Order 4 over the eight papers yields `8 - 7 + 1 = 2` reads -> Paper 8 `Hamiltonian_4th`, `window = 7`. Each surviving center carries its source-window provenance; the global sequence Papers 0-8 has emerged from purely local reads. The complementary caution is `verify_temporal_z4_scope` (`status = "static_template_only"`): the static window frame does not by itself fix the temporal trace, so the emergence is genuinely a property of the carried states. The example is solved because the order counts, window sizes, and provenance reproduce identically from `iterative_hamiltonian`, the formal recursion, and the workbook sliding frame.

## Tool Binding

- Module: `cqe_engine` (`hamiltonian_windows.iterative_hamiltonian`, `hamiltonian_read`, `carry_forward`, `read_backward`, `BASE_C_FORMS`; `lattice_forge.temporal_z4_scope.verify_temporal_z4_scope`).
- Required outputs: `receipt.json` (the list of `WindowRead` records), `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run `iterative_hamiltonian()` and confirm 4 reads at order 2, 3 at order 3, 2 at order 4, with each surviving center carrying its `source_windows`; run `verify_temporal_z4_scope` and confirm `status = "static_template_only"` (the static frame does not dictate the trace).

## Analog Workbook Sheet

- Start with grey loose substrate; lay a row of center-tokens, one per base paper (Papers 0-5).
- Cut a cardboard frame with 3 windows (order 2). Slide it left-to-right; at each stop, read the three centers forward (left to right) and then flip the frame to read them back (right to left). Write the surviving composite center on a new token.
- Add the new tokens to the row, then cut a 5-window frame (order 3) and repeat; then a 7-window frame (order 4).
- White follow-up = a window whose forward and back reads agree (a clean surviving center); black follow-up = a window with too few tokens to fill the frame (boundary).
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: the local-window readout law whose center is carried forward.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: forward/backward channel reads and the receipt of a carried state.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: the `source_windows` provenance carried by each emergent state.
- [JordanVonNeumannWigner1934] Jordan, von Neumann, Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: the center `C` as the `J_3(O)`-trace-preserved quantity under the `L <-> R` reflection.

## Open Obligations

- The reverse-pass `validated: True` flag asserts only well-formedness of the reverse transport string; a substantive validation that the backward read reconstructs the forward physics is open.
- The convergence/termination of the iteration beyond order 4 (1-7 bar) is not derived; whether higher orders stabilize or diverge is open.
- The relation between the window reach and the Paper 08 sheet bound `K = 9` is stated (Paper 5 `Carrier_C5` verified at `K_max = 9`) but not proved to be the exact limit of a single window's transport.
- Replace citation anchors with final bibliography entries.

## Back-Propagation Targets

- Paper 00 receives the C-form term (every paper now declares its surviving center for window reading).
- Paper 05 receives the `K_max = 9` carrier bound as the reach limit of the accumulated-XOR center.
- Paper 08 receives the cross-reference that the window reach is bounded by the same sheet `K = 9`.
- The ForgeFactory / lattice_forge registry records `hamiltonian_windows` as the temporal-emergence engine.
- Paper 31 records how the corpus's own presentation order is the order-2/3/4 Hamiltonian read of its base centers.
