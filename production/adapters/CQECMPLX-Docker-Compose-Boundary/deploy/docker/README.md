# CMPLX Kernel Docker Deployments

These files deploy the kernel itself as the operator surface.

## Kernel-Only Docker-In-Docker

Run:

```bash
docker compose -f deploy/docker/docker-compose.kernel-dind.yml up --build
```

Open:

```text
http://127.0.0.1:8765
```

This creates:

- `cmplx-kernel`: the kernel operator container with Python and Docker CLI.
- `kernel-dind`: a Docker daemon sidecar.

The kernel talks to Docker through:

```text
DOCKER_HOST=tcp://kernel-dind:2375
```

That is the distilled Docker-in-Docker path: kernel plus Compose equals a
self-contained machine-operation environment.

The Compose file mounts:

- `D:\DockerContainers` to `/workspace/docker-tools`;
- `D:\CMPLX-Kernel\kernel_ring` to `/opt/kernel_ring`.

## Host Socket Variant

Run:

```bash
docker compose -f deploy/docker/docker-compose.kernel-socket.yml up --build
```

This uses the host Docker socket instead of a DinD sidecar. It is simpler, but
it gives the container access to the host Docker daemon.

## Control Gate

Container discovery works by default. Start/stop actions require:

```text
CMPLX_DOCKER_ENABLE_CONTROL=1
```

Set `CMPLX_OPERATOR_TOKEN` before exposing the operator beyond localhost.
