# Kernel Ring

The CMPLX Kernel Ring is the companion layer that lives above and around the
deployable `D:\CMPLX-Kernel\kernel` sidecar.

It exists so the main kernel can stay small and portable while still having
structured access to reusable libraries, LatticeForge/lattice proof surfaces,
and ReForge/Forge-family package identities.

## Location

```text
D:\CMPLX-Kernel\kernel_ring
```

Machine-readable entry:

```text
D:\CMPLX-Kernel\kernel_ring\KERNEL_RING_MANIFEST.json
```

## Companion Kernels

| Kernel | Role | Sources | Curated files | Payload exclusions |
|---|---|---:|---:|---:|
| `lib_kernel` | Library, rule, proof, and lib-forge surfaces | 8 | 101 | 0 |
| `lattice_kernel` | LatticeForge, E8/lattice geometry, and pulse-node diagnostics | 11 | 862 | 2 |
| `reforge_kernel` | ReForge and Forge-family package blueprints | 6 | 28 | 57 |

## Contract

- The ring is form-only.
- The ring records identity, file shape, proof route, and payload exclusions.
- The ring does not copy zip, tar, database, virtualenv, build, or package bodies.
- Binary/package movement requires the Binary Boundary Adapter.
- Repo, API, model, MCP, and network handshakes require the Universal Adapter.
- CQE maps engine -> math/proof anchor -> product surface before promotion.
- Hidden Guess Result remains quiet unless `training_mode` is enabled, or a local
  full-program run explicitly requires the full diagnostic layer.

## Promotion Meaning

The ring does not promote these sources into production by copying them whole.
It makes each family addressable as a kernel-grade source of truth. Production
promotion still requires exact slices, receipts, proof docs, and adapter gates.
