# Docker Tool Adapter

The kernel can discover and operate the external Docker tool root at:

```text
D:\DockerContainers
```

Docker is installed on this machine:

```text
Docker 29.5.2
Docker Compose v5.1.4
```

## Operator APIs

- `GET /api/docker/status`
- `GET /api/docker/inventory`
- `GET /api/docker/ps?compose_file=docker-compose.yml`
- `POST /api/docker/up`
- `POST /api/docker/down`

## Control Gate

Discovery and status are always read-only. Container start/stop actions require:

```text
CMPLX_DOCKER_ENABLE_CONTROL=1
```

This keeps Docker plug-and-play for local work without letting every web/API
host mutate containers by accident.

## External Root Rule

The kernel does not copy `D:\DockerContainers` into the deployable runtime. It
treats that folder as an external machine-operation tool root behind the
Universal Adapter and Binary Boundary Adapter.

## Kernel-Only Docker-In-Docker

The bigger deployment shape is the kernel itself as the operator container,
with Docker CLI inside the kernel image and a DinD daemon supplied by Compose.

Files:

```text
deploy/docker/Dockerfile.kernel
deploy/docker/docker-compose.kernel-dind.yml
deploy/docker/docker-compose.kernel-socket.yml
```

Run the DinD form:

```bash
docker compose -f deploy/docker/docker-compose.kernel-dind.yml up --build
```

In that mode:

```text
kernel container + Docker CLI + DinD daemon + Compose = Docker control through the kernel
```

`D:\DockerContainers` is mounted read-only as `/workspace/docker-tools` so the
kernel can inspect and operate the existing Compose/tooling surface without
embedding it into the kernel image.

## Compose Boundary

Internally, the adapter only resolves compose files below the Docker tool root.
Externally, new needs enter as Binary Boundary Adapter compose inserts. See:

```text
docs/DOCKER_COMPOSE_BOUNDARY.md
```

## Notable Surfaces Found

- workstation and live-testing Compose services;
- hardened and advanced Compose stacks;
- Postgres and Redis config;
- observability config;
- Kubernetes and Helm deployment material;
- ReForge MCP toolkit configs and server files.
