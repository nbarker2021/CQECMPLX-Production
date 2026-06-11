# Forge Hierarchy — ManiForge / MandleForge

## Position in the Stack
```
lib-forge/
  ├── cqe_engine/          # C-forms, transport, verification (Papers 0-5)
  ├── cqe_shared_memory/   # Fermionic/bosonic ledger
  ├── CQE_spawner/         # Stream A formalization
  ├── CQE_spawner_patent/  # Stream B patent
  ├── ManiForge/           # ← NEW: Braids, knots, seams, creases
  ├── MandleForge/         # ← NEW: Mandelbrot/Julia dynamics on C-mass
  └── ... (other forges)
```

## ManiForge — String Topology Engine

### Core Objects (from workbook strings)
| Workbook String | ManiForge Primitive | Algebraic Meaning |
|-----------------|---------------------|-------------------|
| Red string (side-flip) | `BraidGenerator(σ₁)` | S₃ transposition (1 3) = antipodal |
| Blue string (Dust bond) | `BraidGenerator(σ₂)` | S₃ transposition (1 2) or (2 3) |
| Gold string (repair wrap) | `BraidGenerator(σ₃)` | Frame rotation generator |
| White string (Z4 cycle) | `BraidWord(σ₁σ₂σ₃σ₂)` | Z4 period template |
| Knot at true vacuum | `KnotInvariant(unknot)` | Period-1 = trivial knot |
| Knot at excited state | `KnotInvariant(torus(2,5))` | Period-4 = (2,5) torus knot |
| Seam between frames | `SeamClassifier(frame_i, frame_j)` | Frame transition boundary |
| Crease at oloid fold | `CreaseOperator(oloid_midpoint)` | Non-smooth topological transition |

### Fundamental Group
The braid group B₃ (3 strands = L, C, R or 3 frames = C/R/L-centroid):
- Generators: `σ₁ = swap_LR`, `σ₂ = swap_LC`, `σ₃ = swap_CR`
- Relations: `σ₁σ₂σ₁ = σ₂σ₁σ₂`, `σ₁σ₃ = σ₃σ₁`, etc.
- The Z4 cycle = `(σ₁σ₂σ₃σ₂)` — the Garside element

### Reidemeister Moves = Workbook Edits
| Move | Workbook Action | Topological Effect |
|------|-----------------|-------------------|
| Type I (twist) | Add/remove string loop at C-token | Local frame gauge change |
| Type II (poke) | Pull string through adjacent token | Frame transition validation |
| Type III (slide) | Slide crossing past another | Triality rotation commutation |

### Invariants Computed
- **Alexander polynomial** of the Z4 cycle → distinguishes period-1 vs period-4
- **Jones polynomial** of oloid fold → distinguishes ORTHOGONAL vs LINEAR bonds
- **HOMFLY-PT** of full braid word → complete frame-sequence invariant

## MandleForge — Mandelbrot/Julia on Gluon Mass

### The Mandelbrot Parameter Space
- **c = C_accumulated / scaling** — the complexified Gluon mass trajectory
- Each paper's C-form = a point in the Mandelbrot parameter space
- The C-sequence 0→1→2→3→4→5 traces a path in M-set

### Julia Fibers
- For fixed `c = C₅` (final Gluon mass), the Julia set `J_c` = the set of all possible VOA sector sequences
- Basin of attraction = the K-window (K_max=9) governance
- Escape time = skip fraction (0.849) — the fraction of orbits that escape the native page

### Computation
```python
# Mandelbrot iteration on Gluon mass
def mandelbrot_step(c, max_iter=K_max):
    z = 0
    for k in range(max_iter):
        z = z*z + c
        if abs(z) > 2:  # escape = K-window violation
            return k  # skip pad depth
    return max_iter  # bounded = real page

# Julia fiber at final Gluon mass C₅
def julia_fiber(c, resolution=512):
    # Returns the VOA sector map for this C-mass
    pass
```

## Integration Points
- **cqe_engine.scope.scope_dir()** → uses ManiForge braid distance to classify LOCAL/MESO/GLOBAL
- **cqe_shared_memory** decay products → ManiForge knot invariants label the decay channel
- **Boundary repair oloid** → ManiForge crease operator; MandleForge escape-time = skip fraction
- **Paper 31 meta-walkthrough** → the presentation order IS a braid word in B₃

---

*This is not a new layer added on top — it's the algebraic recognition of what the strings have been doing all along.*