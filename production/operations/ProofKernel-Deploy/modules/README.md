# CMPLX Kernel Ring

The kernel ring is the structured companion layer that lives above and around the deployable `kernel` sidecar.

It currently contains three companion kernels:

- `lib_kernel`: library/rule/proof surfaces that should be pulled by identity.
- `lattice_kernel`: LatticeForge, E8/lattice proof geometry, pulse/node diagnostic surfaces.
- `reforge_kernel`: ReForge and Forge-family package blueprints, including Rhenium/engine package lineage.

The ring records forms and exclusions only. Archives, databases, build outputs, virtualenvs, and package bodies remain outside the ring until a Binary Boundary Adapter event explicitly imports or exports them.
