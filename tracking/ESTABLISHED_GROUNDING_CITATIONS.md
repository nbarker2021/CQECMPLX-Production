# Established Grounding Citations

Operator thesis (2026-06-13): the work is not new mathematics. It is JUST
connecting fields that are not normally connected, via the same existing math
that started it all — math that is idempotent, dual to one other thing. The
only parts brought in from outside are proven, validated normal forms of
theorems already used daily in all fields. Everything else is the connection.

This ledger names those theorems (the only outside inclusions) and the one
thing the framework adds.

## What started it all

**Lucas' theorem (Édouard Lucas, 1878).** Over GF(2),
`C(m, n) mod 2 = 1` iff `n` is a submask of `m` (`n AND m == n`). This IS
Rule 90 = Pascal's triangle mod 2 = the Sierpinski gasket — the closed form
behind every O(log N) result in the corpus. Its mechanism is the bitwise
**AND submask relation**.

`AND` is **idempotent** (`x AND x = x`) and, by De Morgan, **dual to OR** (the
"one other thing"). Rule 30 = `L XOR (C OR R)`; the correction = `C AND NOT R`;
Lucas = AND-submask. The entire base is the one idempotent dual pair
`{AND, OR}` plus XOR. Verified exhaustively (GroundingForge, paper 00).

## The only outside inclusions (proven, cited, daily-use)

| Theorem | Author, year | Used daily in | Instantiated by | Role |
|---|---|---|---|---|
| Lucas' theorem | Édouard Lucas, 1878 | combinatorics, number theory, CS | Rule 90 = Pascal mod 2 (rule90_linearization) | **the origin — idempotent AND-submask base** |
| Kummer's theorem | Ernst Kummer, 1852 | number theory | the Lucas-carry skip-pad filter | makes the correction Lucas-sparse |
| Boolean algebra / De Morgan | Boole 1847; De Morgan 1860 | all logic & computing | AND (correction) dual to OR (Rule 30) | the idempotent dual pair |
| Three-gap (Steinhaus) theorem | Sós, Surányi, Świerczkowski, 1957–58 | Diophantine approx., quasicrystals | AGRMForge golden sweep | optimal low-discrepancy reader |
| Chinese Remainder Theorem | Sunzi (~3rd–5th c.); Gauss 1801 | cryptography, signal processing | AuthenticaForge 5-term closure | digit-binding closure |
| Exceptional Jordan algebra J3(O) | Jordan–von Neumann–Wigner 1934; Jacobson; Albert | quantum theory, exceptional Lie groups | chart = J3(O) diagonal; shell-2 = trace-2 idempotent (T2, T3) | the idempotent normal form |
| E8 / Leech lattices, Construction A | Conway & Sloane, SPLAG 1988; Witt; Leech 1967 | coding, sphere packing, lattice crypto | E8Forge (240), LeechForge (196560) | high-dimensional closure frames |
| Extended Golay code, Steiner S(5,8,24) | Golay 1949; Witt 1938 | error-correcting codes | LeechForge Golay→Leech tower | the error-correction tower |
| Monstrous Moonshine, McKay-Thompson | Conway & Norton 1979; Borcherds 1992 | VOA / CFT, string theory | mckay_matrix_tables (783=3A, 4372=2A) | the moonshine layer (BOUNDED_EXEC) |

## The only thing the framework adds

**The chart → J3(O) isomorphism (Theorem T3).** The Rule 30 local `(L,C,R)`
state IS a J3(O) diagonal element; shell=2 IS the trace-2 idempotent stratum;
the Weyl `L↔R` involution IS the `(1,3)` transposition. **Verified** by
`rule30.verify_chart_j3o_isomorphism` (0 bijection failures to depth 512).

This is the only new thing — a **connection** between established fields, not
new mathematics within any of them. Once the connection holds, every F4 / J3 /
lattice / moonshine theorem transfers onto Rule 30 as a corollary *by transport
of structure*. The transport is what links the fields; the theorems
transported are all pre-existing and cited above.

## Why this is the binding invariant

Idempotence is what makes the connection hold and reusable:
- the origin (Lucas, AND-submask) is idempotent, dual to OR;
- the Jordan side connects via the **idempotent** Peirce decomposition (trace-2
  idempotent stratum);
- the readout/cache (Event Law, SpeedLight) is idempotent: `f(f(x)) = f(x)`;
- the repair window is the 3-move idempotent closure (T4, `M_3` rank-1
  idempotent).

The same idempotence appears on both sides of every connection — that is what
makes the isomorphism a *normal form* tie rather than a coincidence.

## Honesty boundary

The framework restates established theorems and adds one verified connection
(T3). It does NOT extend exceptional Lie / Jordan / lattice / moonshine theory
(OPEN_OBLIGATIONS O10). The corpus discipline (PROVEN / BOUNDED_EXEC / CONJ)
is preserved. The Wolfram-problem arguments remain transport arguments at their
stated status (TRIADIC_UNISON_ARCHITECTURE.md), not literature closures.
