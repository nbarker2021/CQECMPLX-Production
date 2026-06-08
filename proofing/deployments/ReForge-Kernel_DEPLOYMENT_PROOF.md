# ReForge Kernel Deployment Proof

## Identity

`ReForge Kernel` is the Forge-family package umbrella. It maps ReForge,
LatticeForge-descended package concepts, Rhenium/engine lineage, and named Forge
identity blueprints.

## Deployment Surface

```text
D:\CMPLX-Kernel\kernel_ring\reforge_kernel
```

Sources represented:

- `D:\CQE_CMPLX\ForgeFactory_ReForge_Session_Master_v0_2`
- `D:\CQE_CMPLX\ForgeFamilyBlueprint`
- `D:\CQE_CMPLX\lattice_forge_analysis.md`
- `D:\CQE_CMPLX\lattice_forge_code_review.md`
- `D:\CQECMPLX-Production\lib-forge\MandleForge`
- `D:\CQECMPLX-Production\lib-forge\ManiForge`

## Proof Artifacts

- `KERNEL.md`
- `HANDSHAKE.md`
- `FORM_INDEX.json`
- `sources/*/FORM.md`
- `sources/*/FORM.json`
- `sources/*/file_index.curated.txt`
- `sources/*/payload_exclusions.txt`

## Payload Policy

ReForge package archives are not copied into the ring. They are represented in
`payload_exclusions.txt` receipts. Any archive body must enter through a Binary
Boundary Adapter event with a receipt and a production proof decision.

## Production Split

The ReForge Kernel promotes the method and package identity schema first:

```text
named Forge identity -> CQE proof route -> adapter boundary -> product package
```

Raw package archives, session exports, and generated package bodies remain
outside production until a proof doc names the exact import.

## State

`slice-ready`

The first safe slice is the form/index ReForge Kernel. Package bodies are
airlock material until explicitly promoted.
