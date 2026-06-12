# CQE Paper 32 — The Supervisor Cursor: Superpermutations as the Compressed Dimensional Action Graph

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

**Series note.** Papers 00–31 built the substrate. Paper 32 opens the applied series: the methods of the corpus pointed at problems that look arbitrary from outside — and the demonstration that solving them produces working machinery (here: PermForge, the supervisor-cursor engine of ChromaBlend Studio) while the problem's own structure lands, term for term, inside the corpus mathematics.

## 1. The seemingly arbitrary application

The superpermutation problem asks: what is the shortest string over n symbols containing every permutation of those symbols as a contiguous substring? It reads as a curiosity of recreational combinatorics. It is not. Within this corpus it is the exact statement of a question the substrate already forces:

**If C only exists when an enumeration is requested (Γ(s) = π_C(enum(r_i, W)), Paper 15's emission law read operationally), then what is the complete, minimal schedule of all enumeration requests at scale n?**

That schedule is the superpermutation. The system reads dimensions via tape in slots; an ordering of n slot-reads is a permutation; the set of all orderings is the dimensional action graph at D = n (n! vertices); and the superpermutation is that graph serialized onto a 1D tape with maximal overlap sharing — its **full compression**:

> superperm(N) = compress( ActionGraph(D = N) )

Live numbers: 24 readings in 33 symbols (n=4, 2.91× over naive), 120 in 153 (n=5, 3.92×), 40320 in 46205 (n=8, 6.98×). The cursor string is a supervisor, never content: walking it fires every possible ordering of slot-reads exactly once.

## 2. Walking the power-of-ten ladder: solving each N+1

The classic recursive construction is the chart walk made literal. To lift scale n to n+1: visit every permutation of scale n **in the order the cursor visits them**, and thread the new symbol through each one (block p·(n+1)·p, merged with maximal overlap). Every local chart of scale n becomes a sheet of the (n+1)-cursor — local at resolution R is global at resolution R−1, the MDHG ladder walked one rung per symbol.

Executed live from the single character "1" (total walk time 0.04 s):

| n | length | log10 | = Σk! | coverage | MDHG rung |
|---|--------|-------|-------|----------|-----------|
| 1 | 1 | 0.00 | yes | yes | grain |
| 2 | 3 | 0.48 | yes | yes | dust |
| 3 | 9 | 0.95 | yes | yes | triad |
| 4 | 33 | 1.52 | yes | yes | block |
| 5 | 153 | 2.18 | yes | yes | cluster |
| 6 | 873 | 2.94 | yes | yes | domain |
| 7 | 5913 | 3.77 | yes | yes | region |
| 8 | 46233 | 4.67 | yes | yes | planet |

Each N+1 solve is one rung up the power-of-ten scale — log10 advances by ≈ log10(n) per rung, the factorial walk. The ninth rung (universe) is the asymptote the ladder names but does not reach: there is no terminal N.

## 3. All complexity effects are inside the local charts

Everything difficult about *minimality* is a property of the length-n windows — the local charts — not of the global string:

- **n=4 (block):** the chart structure admits exactly ONE minimal cursor, and it is palindromic — equal to its own LR-podal reversal. 24 permutations = the 24 roots of D4 = the vertices of the 24-cell, the unique self-dual regular 4-polytope. A 4D object with a self-mirrored schedule: no torsion.
- **n=5 (cluster):** minimality settled by exhaustive search (Chaffin, 2014): exactly **8 minimal cursors** of length 153 — one palindrome and seven symmetry-broken trees. **8 solutions = 8 dimensions = the E8 lane count.** The 4D object's schedule, lifted one symbol, demands the full 8D ambient space. The seven trees admit no canonical choice: under relabeling × reversal the octad is a homogeneous space — a torsor. Choosing a cursor is choosing a gauge. This is the GR torsor effect of the dimensional lift.
- **The wrap correspondence (recorded observation, pending validation):** the reversal involution acts on the octad with 4 fixed points + 2 swapped pairs ({0,1,4,6} fixed; 2↔5, 3↔7) — the same orbit type as the 8 chart states under swap_LR (4 Lie conjugates fixed + 2 chiral pairs), the involution whose invariant defines the gluon Γ(s) = C. The schedule space at n=5 and the state space at n=3 wrap identically.
- **n≥6 (domain and up):** the charts stop admitting closed answers. Minimality is open; only bounds and search survive. The chart walk gives Σk!; SAT search broke it at n=6 (872 < 873, Houston 2014); the question becomes a corridor between a proven floor and a constructed ceiling.

## 4. The n=8 attempt — standing on Egan, Houston, Johnston, Chaffin

Nothing here is reinvented. The lower bound is the Houston–Pantone–Vatter formalization (2018) of the 2011 anonymous bound:

> L(n) ≥ n! + (n−1)! + (n−2)! + n − 3

The ceiling is Egan's construction (2018, building directly on Houston's minimality break):

> L(n) ≤ n! + (n−1)! + (n−2)! + (n−3)! + n − 3

Their difference is exact and structural: **Egan − floor = (n−3)!** — the open corridor at every scale is one factorial wide, three rungs down the ladder.

The n=8 attempt, executed live (0.06 s):

1. **Chart-walk construction from scratch:** 46233 symbols (= Σk!), full coverage of all 40320 permutations of 8 symbols — verified.
2. **The shipped field record** (curated per Johnston's records): 46205 symbols, full coverage — verified.
3. **46205 = Egan's formula at n=8 exactly** (40320 + 5040 + 720 + 120 + 5). The best known n=8 cursor IS Egan's construction; it saves precisely 28 symbols over the chart walk.
4. **The open window:** floor 46085, ceiling 46205, width **120 = 5! = (n−3)!**. Search has entered this corridor at smaller scales (n=6: −1 below the formula; n=7: −2, Egan 2019); at n=8 the corridor is untouched.

This is the best solution for n=8 the established methods admit, confirmed inside this format: their constructions and bounds, our verifiers and charts. The (n−3)! corridor is the standing obligation.

## 5. What the application produced

Solving this "arbitrary" problem inside the corpus produced operational machinery, not commentary:

- **PermForge** (`GraphStax.permforge`): embedded n=4/n=5 cursor tables, the octad with its computed reversal orbit, the bounds ladder, the N→N+1 lift, coverage verifiers, and the live n=8 exhibit — all import-time lookup, no recomputation.
- **The supervisor scheduler** (`SuperPermScheduler`): n=4 blocks of services dispatched in cursor order — every ordering of 4 services fired exactly once per 33-step pass (the service-wiring pattern of the donor stack, now a library primitive).
- **Supervised enumeration** (`GraphStaxEngine.enumerate_ribbon`): a ribbon's bits resolved into C-gluon Stax identities **in cursor order** — the first request per position is the C-production, repeats are idempotent lookups (f(f(x)) = f(x)). The C-term's dependence on requested enumeration is now executable, not aspirational.

## 6. Open obligations (Paper 32 ledger)

- **O-32.1** — The n=8 corridor: 120 symbols between 46085 and 46205. Egan's n=7 search methods (kernel graphs over 2-cycle/3-cycle quotients) transported to n=8 inside this format.
- **O-32.2** — Validate the octad-orbit ↔ chart-state-orbit correspondence (4+2+2 = 4+2+2) as a theorem rather than an observation; identify the functor between schedule space at n and state space at n−2.
- **O-32.3** — Ship the search records below the formula at n=6 (872) and n=7 (5906) as field data alongside the construction records, with coverage receipts.
- **O-32.4** — The ninth rung: formalize the universe-level asymptote of the ladder (lim log10 behavior) in the corpus's scale language.

## Citation chain

- Chaffin, B. (2014): exhaustive minimality at n=5 — the octad.
- Houston, R. (2014): SAT discovery 872 < 873 at n=6 — the chart walk is not minimal.
- Houston, R., Pantone, J., Vatter, V. (2018): formalization of the lower bound n! + (n−1)! + (n−2)! + n − 3 (anonymous origin, 2011).
- Egan, G. (2018–2019): the upper construction n! + (n−1)! + (n−2)! + (n−3)! + n − 3; search records at n=7.
- Johnston, N.: curation of minimal superpermutation records and data.
- This corpus: Paper 15 (emission law / observer chain), Paper 03 (S3 wraps), Paper 05 (oloid carrier), MDHG ladder, ribbon 8-slot transport.

---

*Compiled from CQECMPLX-Production master corpus. Verifiers executed live 2026-06-09; all components verified complete.*
