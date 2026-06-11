# Operator Web Console

The operator console is a local web frontend for the kernel sidecar.

Run it with:

```bash
python boot.py --serve
```

Default URL:

```text
http://127.0.0.1:8765
```

## Included APIs

- `GET /api/health`
- `GET /api/modules`
- `GET /api/kernel-ring`
- `GET /api/events?limit=50`
- `GET /api/proofs`
- `GET /api/repo-forms`
- `GET /api/package/manifest?limit=200`
- `GET /api/docker/status`
- `GET /api/docker/inventory`
- `GET /api/docker/ps?compose_file=docker-compose.yml`
- `POST /api/process`
- `POST /api/module-state`
- `POST /api/docker/up`
- `POST /api/docker/down`
- `POST /api/docker/boundary-insert`

## Security Options

- `CMPLX_OPERATOR_TOKEN`: enables bearer-token auth when set.
- `CMPLX_OPERATOR_CORS_ORIGIN`: enables a specific CORS origin when set.
- `CMPLX_OPERATOR_MAX_BODY_BYTES`: request body limit, default `1048576`.
- `CMPLX_OPERATOR_RATE_LIMIT_PER_MINUTE`: per-client rate limit, default `120`.

Docker start/stop actions are also gated by:

```text
CMPLX_DOCKER_ENABLE_CONTROL=1
```

## State

The console uses `data/kernel_state.sqlite3` for event receipts and module
state. This file is runtime state and should not be promoted as source.

## Boundary Rule

The web console is a host adapter over the same sidecar contract. It does not
change the kernel rule:

```text
token string -> boundary frame -> diagnostics -> enriched text -> receipt
```

Training mode still controls Hidden Guess Result receipts.
