# Docker Compose Boundary

The kernel has two Docker rules.

## Internal Rule

Internally, Docker operations are structurally limited to existing compose
layers below the kernel level.

Default below-kernel root:

```text
D:\DockerContainers
```

The Docker adapter resolves compose files only inside that root. The kernel does
not treat arbitrary host paths as Docker control surfaces.

## External Insert Rule

Externally, new needs enter as compose inserts, not direct edits to the base
compose files.

The insert shape is defined by:

```text
deploy/docker/boundary-inserts/compose-insert.schema.json
deploy/docker/boundary-inserts/compose-insert.template.json
```

The Binary Boundary Adapter frames the insert as:

```text
boundary_type=docker_compose_insert
target_compose=<below-kernel-compose-file>
compose_overlay=<compose override fragment>
sha256=<stable boundary hash>
payload_b64=<portable insert body>
```

Operationally, the insert is applied as an override:

```bash
docker compose -f D:\DockerContainers\docker-compose.yml -f insert.override.yml up
```

The base layer remains the known machine layer. The insert is the new need.

## Operator API

Frame an insert:

```text
POST /api/docker/boundary-insert
```

This returns a Binary Boundary Adapter frame. It does not write or start
containers by itself.
