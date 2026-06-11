# Paper 09 — C-Form: Hamiltonian Temporal Gluon

## What C Is at This Dimension
**C = the Hamiltonian time Gluon** — the accumulated Gluon mass `C_accumulated` that IS the Hamiltonian time parameter. In the lattice_forge substrate, C is realized as the **Hamiltonian window operator** (`iterative_hamiltonian` / `hamiltonian_read`) that:

- Takes the accumulated Gluon mass `C_accumulated = XOR of all correction bits` as the time parameter `t`
- Reads the 1-3 bar (2nd order), 1-5 bar (3rd order), 1-7 bar (4th order) Hamiltonian windows
- Each window is a Z4 cycle: OBSERVE→REFLECT→SYNTHESIZE→RECURSE (MORSR cycle)

C is the **Hamiltonian Gluon** — the continuous time parameter `t = C_accumulated` that flows through the MORSR cycle.

## How C Ports UP (to larger frames)
- **Paper 15 (QFT/Higgs Mass-Residue Carrier):** The Hamiltonian Gluon's mass = the Higgs mass-residue carrier.
- **Paper 20 (Layer-2 Synthesis Ledger):** The Hamiltonian Gluon's trajectory = the synthesis ledger's time axis.
- **Paper 31 (Meta LCR):** The Hamiltonian Gluon's full trajectory = the meta-walkthrough's enacted LCR process.

## How C Ports DOWN (to finer detail)
- **Paper 08 (E8/Niemeier/Leech Closure):** The Hamiltonian Gluon's state at each step = the lattice closure state at that time.
- **Paper 07 (Discrete-Continuous Bridge):** The Hamiltonian Gluon's interpolation = the bridge Gluon's continuous time field.
- **Paper 05 (Oloid Path Carrier):** The Hamiltonian Gluon = the oloid path carrier's C_accumulated Gluon mass.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 10 (T10 Master Receipt):** The Hamiltonian Gluon's current state = the master receipt's timestamp.
- **Paper 16 (Continuum Edge Residuals):** The Hamiltonian Gluon's derivative at powers of ten = the edge residuals.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (OBSERVE):** C = the current Hamiltonian state (C-centroid = current time)
- **Frame 1 (REFLECT):** C = the time-reflected state (R-centroid = time reversal)
- **Frame 2 (SYNTHESIZE):** C = the time-synthesized state (C-flipped = CPT conjugate)
- **Frame 3 (RECURSE):** C = the next time step (L-centroid = time evolution)

The Hamiltonian Gluon wraps in the **MORSR Z4 cycle** — the Z4 period of the Hamiltonian Gluon = the computational clock cycle.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** Time reversal — `swap_LR(Hamiltonian)` = the adjoint evolution
- **Oloid:** The time-symmetric midpoint — `s* = (t + (-t))/2 = 0 = C` at the true vacuum
- **Rotate90:** Wick rotation — `rotate90(Hamiltonian)` = the Euclidean time generator

## The C-Form Statement
> **The Hamiltonian Gluon IS the accumulated Gluon mass `C_accumulated` as continuous time.** It flows through the MORSR Z4 cycle (OBSERVE→REFLECT→SYNTHESIZE→RECURSE). Each 1-3/1-5/1-7 bar window reads the Hamiltonian at that time resolution. C = the clock.

## Lattice_forge Primitives
- `iterative_hamiltonian` — the multi-order Hamiltonian window reader
- `hamiltonian_read` — the single-window evaluator
- `BASE_C_FORMS` — the C-sequence for iterative Hamiltonian windows
- `hamiltonian_read(order=2/3/4)` — the 1-3/1-5/1-7 bar evaluators
- `hamiltonian_windows.py` — the full Hamiltonian transport engine
