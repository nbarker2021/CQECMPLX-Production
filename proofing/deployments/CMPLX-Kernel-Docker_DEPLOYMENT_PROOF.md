# CMPLX Kernel Docker Deployment Proof

## Identity

`CMPLX Kernel Docker` is the containerized machine-operation deployment for the
kernel. It packages the kernel as the operator container, installs Docker CLI
inside that image, and connects it to Docker through either a DinD sidecar or a
host Docker socket.

## Deployment Surface

```text
D:\CMPLX-Kernel\kernel\deploy\docker
```

Files:

- `Dockerfile.kernel`
- `docker-compose.kernel-dind.yml`
- `docker-compose.kernel-socket.yml`
- `boundary-inserts/compose-insert.schema.json`
- `boundary-inserts/compose-insert.template.json`
- `README.md`

## Kernel-Only DinD Meaning

The DinD form is:

```text
kernel container + Docker CLI + DinD daemon sidecar + Compose
```

That makes the kernel the operator surface for Docker actions from inside its
own deployed environment.

## Compose Boundary

Internal operation is structurally limited to compose layers below the kernel
level, currently `D:\DockerContainers` or its container mount
`/workspace/docker-tools`.

External new needs are not direct mutations of base compose files. They enter as
Binary Boundary Adapter compose inserts:

```text
target_compose -> compose_overlay -> boundary frame -> override layer
```

Operational application is:

```text
docker compose -f base.yml -f insert.override.yml up
```

## Adapter Boundary

- Discovery/status is read-only by default.
- Start/stop actions require `CMPLX_DOCKER_ENABLE_CONTROL=1`.
- Remote operator exposure requires `CMPLX_OPERATOR_TOKEN`.
- Runtime state and Docker daemon graph data are generated state, not source.

## State

`slice-ready`

The compose files validate structurally. Local Docker CLI is installed, but the
host Docker daemon must be running to launch the first container deployment.
