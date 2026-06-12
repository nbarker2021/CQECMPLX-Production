# Paper 32 — C-Form: The Supervisor Cursor Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the enumeration-request Gluon** — the value produced when a requested enumeration fires against a window. C is never a standing value. The normal form:

> **Γ(s) = π_C( enum(r_i, W) )**

where `W` is the unobserved (L,C,R) window, `r_i` is enumeration request *i* — a cursor position on a superpermutation string — and `enum` is the act that collapses the flat chain into one of the 8 chart states (the 2×2×2 cube). **No request, no C.**

The superpermutation string at scale n is the **supervisor cursor**: the minimal string containing every permutation of n symbols as a substring. It is never ribbon content — it is the complete, maximally compressed schedule of every enumeration request that scale n admits. Walking it fires every possible ordering of n slot-reads exactly once.

**The compression identity (N = D):** the dimensional action graph at D = n has n! vertices (orderings of n slot-reads off the tape). Naive serialization costs n·n! symbols. The superpermutation is its full compression:

> **superperm(N) = compress( ActionGraph(D = N) )** — 24 readings in 33 symbols at n=4 (2.91×); 120 readings in 153 symbols at n=5 (3.92×); 40320 readings in 46205 symbols at n=8 (6.98×).

## How C Ports UP (to larger frames)

- **The N→N+1 lift (recursive_step):** for each permutation p visited by the scale-n cursor in visit order, emit the block p·(n+1)·p and merge with maximal overlap. The new symbol is threaded through **every local chart of scale n** — the chart at scale n becomes the sheet of the (n+1)-cursor. Length at every rung: Σ_{k=1}^{n} k! (verified live, 1→8, full coverage at each rung).
- **The n=4 → n=5 split is the 4D → 8D lift:** at n=4 the minimal cursor is UNIQUE and palindromic (24 permutations = 24 D4 roots = the 24-cell, the self-dual 4D object; self-mirror, no torsion). At n=5 there are exactly **8 minimal cursors** (1 palindrome + 7 trees) = **8 dimensions = the E8 lane count**. The 4D object's schedule, lifted one symbol, demands the full 8D ambient space.
- **n=8 is the ribbon scale:** the 8-slot ribbon (C, L, R, B, T, O, W, A) is fully enumerated by the n=8 cursor — 40320 slot-read orderings in 46205 symbols.

## How C Ports DOWN (to finer detail)

- Every length-n window of the cursor string is a **local chart**. The digit at the cursor is which slot/dimension the tape reads NOW; the chart is the active enumeration.
- All effects in the complexity of finding the minimal cursor are **chart-local**: the uniqueness at n=4, the octad at n=5, the open search windows at n≥6 are properties of what the length-n windows admit, not of the global string.
- The cursor walks the MDHG ladder: scale n occupies rung n of grain→dust→triad→block→cluster→domain→region→planet→universe. Local at resolution R = global at resolution R−1: the chart of the n-cursor IS the sheet of the (n−1)-cursor.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **TarPit (Layer 3 Jot):** the Jot bit-cursor is the degenerate n=2 supervisor; PermForge is its full-arity completion.
- **SpeedLight:** a repeat enumeration request is a pure lookup — f(f(x)) = f(x). First request creates the Stax (the enumeration act); every later request is idempotent projection.
- **GraphStax:** `enumerate_ribbon` resolves a ribbon's bits in cursor order — each C-production on the graph is one fired request.

## How C WRAPS (S3 transposition / frame inversion)

The reversal involution (the LR-podal reading) acts on the n=5 octad with **4 fixed points + 2 swapped pairs** — orbit {0↦0, 1↦1, 4↦4, 6↦6, 2↔5, 3↔7}. This is **the same orbit type as the 8 chart states under swap_LR**: 4 Lie conjugates fixed + 2 chiral pairs — the involution that defines the gluon Γ(s) = C. *(Computed at import in `N5_REVERSAL_ORBIT`; recorded as structural observation pending validation.)*

## How C FOLDS (oloid/antipode/torsor operations)

- **Antipode:** the reversed cursor — the same schedule read backward.
- **Palindrome:** the self-antipodal cursor. Unique at n=4 (no torsion); exactly one of eight at n=5.
- **Torsor:** the 8 minimal cursors at n=5 form a homogeneous space under relabeling × reversal — no canonical origin. Choosing one is a gauge choice: the GR torsor effect of the dimensional lift. The oloid has no privileged state; the octad has no privileged cursor.

## The C-Form Statement

> **The supervisor cursor IS the compressed dimensional action graph.** C exists only as the product of a fired enumeration request: Γ(s) = π_C(enum(r_i, W)). Solving each N+1 is one rung up the power-of-ten ladder (1, 3, 9, 33, 153, 873, 5913, 46233 on the chart walk), and every effect in minimal-finding complexity — the n=4 uniqueness, the n=5 octad, the open windows at n≥6 — lives inside the local charts. The n=4→n=5 split (1 solution → 8 solutions) is the 4D object (24-cell/D4) demanding the full 8D space (E8 lanes), with the residual freedom a torsor.

## Bounds Ladder (all verified live)

| n | lower bound | chart walk Σk! | Egan construction | best shipped |
|---|------------|----------------|-------------------|--------------|
| 4 | 33 | **33** | 34 | 33 (unique, minimal) |
| 5 | 152 | **153** | 154 | 153 (octad, minimal — exhaustive) |
| 6 | 867 | 873 | 873 | 873 shipped; 872 known by search |
| 7 | 5884 | 5913 | **5908** | 5908 shipped; 5906 known by search |
| 8 | 46085 | 46233 | **46205** | 46205 shipped = Egan formula exactly |

Lower bound: n! + (n−1)! + (n−2)! + n − 3. Egan construction: n! + (n−1)! + (n−2)! + (n−3)! + n − 3. **Identity: Egan − lower = (n−3)! exactly** — the open window at n=8 is 5! = 120 symbols wide.

## Lattice_forge / GraphStax Primitives

- `GraphStax.permforge.superperm(n)` — the validated cursor string (n=4,5 embedded; 6–8 field records)
- `coverage_check`, `coverage_checksum` — every permutation as substring
- `enumeration_request`, `c_normal_form` — the Γ(s) = π_C(enum(r_i, W)) expression
- `recursive_step`, `recursive_construction` — the N→N+1 chart-walk lift
- `lower_bound`, `chart_walk_upper`, `egan_upper` — the bounds ladder
- `verify_record(n)`, `n8_attempt()`, `power_of_ten_walk()` — the Paper 32 verifiers
- `N5_OCTAD`, `N5_REVERSAL_ORBIT` — the octad and its involution orbit
- `SuperPermScheduler` — the supervisor cursor as a service scheduler
