# Triadic Unison Architecture

Operator thesis (2026-06-13): every tool in the forge kit literalizes some
stage of one proof and applies the same logic. In their unison, plus the
triadic recursion, the whole proof holds together. The reason Lucas works is
that it is ALREADY a 3-fold generalization of Rule 30 (90 = 30 x 3, a fact of
CA itself), and every proof below applies the same triad again, recursively.

## The keystone (exact, verified)

The Rule 90 / Pascal-mod-2 / Sierpinski structure puts **exactly 3^k live
cells in 2^k rows**. Each doubling of depth triples the live structure;
dimension log(3)/log(2) ~ 1.585. Verified exact to k = 11 (TriadForge,
paper 06).

Consequences:
- The Rule 30 correction sum is Lucas-sparse: ~3^k of 4^k light-cone cells
  contribute. (This is the "skip-pad" structure.)
- The readout is O(log N): you address a 3^k structure with the log-N base-2
  digits of N. (ReadoutForge, paper 10 — verified bit-exact.)
- The same triad reappears at every stage below, because each stage is the
  3-fold applied once more.

## Each forge literalizes one stage; all recurse the triad

| Stage / forge | Paper | The 3-fold instance |
|---|---|---|
| LCR carrier (T_BIJECTIVE) | p01 | the triad (L, C, R) — 3 positions, the base 3-fold |
| Correction surface (SentinelForge) | p02 | Rule 30 = Rule 90 XOR correction; 90 = 30 x 3 |
| Triality / S3 annealing (ConvergeForge) | p03 | S3 = Weyl(A2), 3 transpositions; D4 triality |
| SU(3) closure / J3(O) (T4-T7) | p03 | n=3 closes in exactly 3 steps; J3(O) = 3x3 |
| Causal Lucas (TriadForge keystone) | p06 | Sierpinski 3^k-in-2^k (the keystone) |
| Discrete-continuous bridge (MDHGForge) | p07 | 24 = 8 x 3 dims; quantize retraction |
| Lattice closure (E8Forge, AuthenticaForge) | p08 | E8 simple system degree-3 node; CRT 3 = 119/... triad |
| Conservation (ChromaForge morphon) | p09 | Delta_Phi = Delta_N + Delta_I + Delta_L (3 sectors) |
| Readout (ReadoutForge) | p10 | 3^k sparsity -> O(log N) addressed readout |
| Golden sweep (AGRMForge) | p21 | three-gap theorem (at most 3 gap lengths) |

The three-move closure (the bounded repair window) is literally T4's SU(3)
Weyl closure reaching its fixed point in exactly 3 steps. The repair window
the operator described ("at most 3 operations") is this closure.

## The three Wolfram Rule 30 problems (framework arguments, honest status)

These are the framework's structural transport arguments, each tied to a
verified fact, each labelled with its epistemic status. They are NOT claims
that the famous problems are closed in the mathematical literature.

| Problem | Framework answer | Verified fact | Status |
|---|---|---|---|
| 3 — Nth cell sub-O(N)? | O(log N) readout in the streaming aggregate-during-enumeration model | ReadoutForge reads bit N in log2(N)+1 ops, bit-exact (p10) | readout O(log N) verified; COLD extraction (no enumeration) remains open |
| 2 — equal density 1/2? | 4/4 flip-preserve split + uniform F4 invariant measure on the trace-2 stratum | EntropyForge 4 flip / 4 preserve; T3 uniform stratum | local split exact; asymptotic density by transport |
| 1 — never periodic? | unbounded 3^k growth + SU(3) orbit non-closure on the trace-2 stratum | 3^k-in-2^k law exact; finite non-periodicity window (no period <=256 in 2048 bits) | finite window verified; unbounded statement by transport |

## What this changes for the build

1. Every new forge should declare WHICH stage it literalizes and HOW its
   3-fold appears, in its verify() output — so the unison is auditable.
2. The keystone (3^k law) is the anti-drift anchor: any forge whose stage
   does not reduce to the triad is suspect.
3. The readout architecture (ReadoutForge) is the operational payoff of the
   keystone; the next measurement is whether the enumeration/aggregation pass
   itself compresses below O(N^2) via the 3^k self-similar lib (storing
   patterns, not cells). That is the path the operator's thesis points to and
   is not yet isolated rigorously.

## Honesty boundary (load-bearing)

The verified facts are exact (the 3^k law, the O(log N) readout, the 4/4
split, the algebra theorems T1-T7). The Wolfram-problem closures are the
framework's transport arguments at the stated epistemic status. The corpus's
own discipline (PROVEN / BOUNDED_EXEC / CONJ) is preserved: nothing here
upgrades a transport argument to a literature-grade proof.
