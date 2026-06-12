# cqecmplx-forge

The installable Forge ring of the CQE/CMPLX tool family.

```
pip install cqecmplx-forge          # stdlib-only core
pip install cqecmplx-forge[predictors]   # + numpy/scipy spectral predictors
```

## What you get (eight top-level packages)

| Package | Role |
|---|---|
| `lattice_forge` | The proven substrate: Rule 30 chart algebra, J3(O)/F4 registration, Binary Boundary Adapter, lattice code chains, oloid carriers, ledgers |
| `ChromaForge`   | The Event Law machinery: Merkle receipts, conservation, idempotent cache (f(f(x))=f(x)), crystal store |
| `GraphStax`     | Graph identity: bit -> C-gluon resolution, AGRM routing, the superpermutation supervisor cursor (PermForge) |
| `PixelForge`    | Display/input plane: adaptive-resolution surfaces, stylus/touch ink with pressure+tilt, E8 projection, deterministic frame streams |
| `FridgeForge`   | Applied engine: inventory lexicon, kid/adult meal lanes with hard constraints, templated shopping lists |
| `LinkForge`     | External databases as lib items: json/csv/ics linked once, receipted, reused |
| `MandleForge` / `ManiForge` | Forge conventions for Mandelbrot/manifold surfaces |

## Quick check

```python
from lattice_forge.binary_boundary_adapter import adapt
from ChromaForge import ChromaForgeEngine
from GraphStax import coverage_check, SUPERPERM_N4

print(adapt(b"hello")["arc_type"])
print(ChromaForgeEngine().execute("hello")["receipt"]["receipt_hash"][:12])
print(coverage_check(SUPERPERM_N4, 4))   # True
```

Source of truth: https://github.com/nbarker2021/CQECMPLX-Production
