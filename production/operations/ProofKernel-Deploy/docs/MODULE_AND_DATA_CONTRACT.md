# Module And Data Contract

CMPLX-Kernel now has a small dynamic module and data layer.

## Module Registry

File:

```text
modules/MODULE_REGISTRY.json
```

Schema:

```text
schemas/module_registry.schema.json
```

Every module declares:

- `module_id`
- `title`
- `kind`
- `status`
- `entrypoint`
- `capabilities`

## Dynamic State

The runtime state store uses SQLite through the Python standard library.

Default file:

```text
data/kernel_state.sqlite3
```

Tables:

- `kernel_events`: append-only event receipts.
- `module_state`: current state per module.

The database is generated runtime state. It is not part of the portable source
package unless an explicit Binary Boundary Adapter receipt promotes a snapshot.

## Modular Rule

All future modules should enter in this order:

```text
identity -> registry entry -> adapter boundary -> proof receipt -> optional UI surface
```

If a module stores data, it must name whether that data is runtime state,
source material, proof artifact, or production lib behavior.

## Current Built-Ins

- `sidecar-runtime`
- `operator-web`
- `kernel-state-store`
- `kernel-ring-loader`
- `docker-tool-root`
- `kernel-explorer`
- `operator-security`

External machine-operation roots, such as `D:\DockerContainers`, remain outside
the portable runtime and are reached through adapter contracts.
