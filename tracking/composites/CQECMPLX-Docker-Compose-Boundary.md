# CQECMPLX-Docker-Compose-Boundary

Status: `trackable-composite`

Route: `production/adapters` + `production/kernel-runtime`

## Composite Identity

`CQECMPLX-Docker-Compose-Boundary` is the Docker/Compose handshake layer for the
kernel. It treats Docker as a host capability used by the kernel, not as a
reason to import every local container workspace.

## Boundary Rule

Internal compose layers must stay below kernel level.

External needs must enter through a boundary insert record that follows the
provided schema/template.

## Included Source Families

- Kernel Dockerfile and socket/DinD compose forms.
- Compose boundary insert schema and template.
- Docker tool adapter documentation.
- ProofValidatedSuite validated hierarchical compose file.
- DockerContainers as a referenced platform source, not a wholesale import.

## Required Adapter Layer

- Binary Boundary Adapter
- Universal Adapter Programs
- explicit host/network handshake rules

## Promotion Gates

1. No unreviewed host-specific absolute paths in promoted compose files.
2. No secrets, `.env`, local volumes, or runtime logs.
3. Internal kernel compose remains structurally below the kernel.
4. External inserts are represented as boundary records.
5. Docker CLI/daemon is documented as an optional host capability.

## Source Bindings

- `tracking/source-bindings/CQECMPLX-Docker-Compose-Boundary.json`
- `tracking/promotion-manifests/CQECMPLX-Docker-Compose-Boundary.manifest.json`
