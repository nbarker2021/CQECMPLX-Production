# TMN1 Docker Deployment

43 services. One image. Port range `10000-10099`.

```bash
cd infrastructure && docker compose up -d
```

---

## Single Image Architecture

Every service is `tmn1:latest`. Role is set via `TMN1_ROLE` environment variable in docker-compose.yml. No role = no separate Dockerfile. This is the invariant.

```text
Infrastructure new service → new TMN1_ROLE in entrypoint.py → new block in docker-compose.yml
NOT → new Dockerfile → new image
```

Build:

```bash
cd d:/CMPLX-TMN1
./infrastructure/build.sh           # builds tmn1:latest
./infrastructure/build.sh --master  # also tags as tmn1:master (stable release)
```

---

## Full Port Map

```text
CORE SERVICES (10000-10009)
  10000  tmn1-gateway              — Unified API, 131 MCP tools, contract enforcement
  10001  tmn1-board                — Agent communication, economy, 39 boards, SAP governance
  10002  tmn1-pg                   — PostgreSQL 16 (shared relational state, PG-primary layer)
  10003  tmn1-redis                — Redis pub/sub, SpeedLight cache, session store

ENGINES (10010-10019)
  10010  tmn1-engine-0             — Geometry/TarPit domain
  10011  tmn1-engine-1             — SNAP/Code domain
  10012  tmn1-engine-2             — Agent/Philosophy domain
  10013  tmn1-engine-3             — Physics/Economics domain

SIMULATION (10020-10029)
  10020  tmn1-sim                  — Tick economy, physics, divergence detection
  10021  tmn1-sim-redis            — Sim-local Redis (isolated entity state)

AGENTS (10030-10039)
  10030  tmn1-daemon               — 30s cooperative tick, bounty distribution
  10031  tmn1-station              — MORSR Numbers Station, 240 E8 chirp broadcast
  10032  tmn1-identity             — Agent register, respawn, access keys
  10033  tmn1-coop                 — Agent Cooperative (multi-agent coordination)
  10035  tmn1-intake-agent         — Intake pipeline agent

TRAINING (10040-10049)
  10040  tmn1-trainer              — ThinkTank: 8 nanoGPT domain specialists in quorum

DASHBOARD (10050-10059)
  10050  tmn1-dashboard            — System monitoring + economy dashboard

ARENA (10060-10069)
  10060  tmn1-arena                — Training capsule, fractal CA economy, variable terminal
  10061  tmn1-ca-sim               — CA Sim: 10 Wolfram channels, 24 Niemeier panels
  10062  tmn1-mdhg-sandbox         — MDHG Sandbox: isolated hash fabric scratchpads
  10063  tmn1-board-claw-bridge    — Board-Claw Bridge: binary Claw ↔ Board post protocol
  10064  tmn1-token-ir             — Token IR: Base100 4-layer encoding pipeline

MCP / SEMANTIC / INTAKE (10070-10079)
  10073  tmn1-mcp                  — MCP Crystal: 209 tools as n=4 crystal blocks
  10074  tmn1-semantic             — Semantic: 18-wave pipeline (atom meanings, D6/D7 bridge)
  10075  tmn1-integrator           — Universal Port Protocol: 6-phase porting for all external code
  10076  tmn1-harvester            — Content Harvester: Atlas+Library ingestion with family dedup
  10077  tmn1-ingress-egress       — SubdockCrew intake + MoE ThinkTank egress

MASTERS (10080-10089)
  10080  tmn1-thinktank            — ThinkTank: 8 KarpathyFleet bots in quorum
  10081  tmn1-sap                  — SAP Hub: Sentinel→Arbiter→Porter governance
  10082  tmn1-speedlight           — SpeedLight: Base100 IR + geometric proximity cache
  10083  tmn1-mint                 — Mint: conservation-law coin minting
  10084  tmn1-economy              — Agent Economy: escrow, marketplace, conservation ledger
  10085  tmn1-teaching             — Teaching: ThinkTank-evaluated agent training
  10086  tmn1-cpl                  — CPL: Crystal Projection Library quasi-crystal sandbox
  10087  tmn1-atlas                — Atlas: atlas_ir + 24 CQE tools + CMPLX Runtime
  10088  tmn1-library              — Library: 7-stage doc pipeline, 692 RAG cards indexed
  10089  tmn1-staging              — Staging: mass canonicalization, 1,451 segments active

CONTROL / PORTAL (10090-10099)
  10090  tmn1-port-controller      — Port Controller: service topology management
  10091  tmn1-paper-harvester      — Paper Harvester: academic paper ingestion
  10092  tmn1-free5e-porter        — Free5e Porter: D&D content porting (external agent work)
  10095  tmn1-portal               — Portal: external AI DMZ, shadow entity management
  10096  tmn1-sandbox-interface-agent — SBA: operator entrypoint, MESO-tier LivingAgent
  10097  tmn1-portal-companion     — Portal Companion: session-scoped AI orchestrator
```

---

## Network Topology

```yaml
networks:
  tmn1-core:    # All 43 services — internal communication
  tmn1-sim:     # Sim + Sim-Redis isolated — heavy compute sandbox
```

Sim communicates with the main system only via gateway HTTP (crosses network boundary).

---

## Volume Architecture

```text
Host Path                          Container Path     Mode
d:/CMPLX-TMN1/databases/          /data              rw      ALL services
d:/CMPLX-TMN1/retooling/src/      /src               ro      Most services
d:/CMPLX-TMN1/nanoGPT/            /nanogpt           ro      Gateway, Engines, Trainer
d:/CMPLX-TMN1/karpathy_agents/    /models            rw      Engines, Trainer, Arena
d:/CMPLX-TMN1/databases/pgdata/   (pg volume)        rw      tmn1-pg
d:/CMPLX-TMN1/databases/redis/    (redis volume)     rw      tmn1-redis
```

Source code is **mounted read-only at runtime** — code changes do not require image rebuild.

---

## Startup

```bash
# Full system (all 43 services, ordered by depends_on)
cd d:/CMPLX-TMN1/infrastructure
docker compose up -d

# Health check
docker compose ps

# Verify key services
curl http://localhost:10000/health    # Gateway
curl http://localhost:10001/health    # Board
curl http://localhost:10080/health    # ThinkTank
curl http://localhost:10096/status    # SBA (MESO tier, 131 tools)
```

---

## Database State

```text
d:/CMPLX-TMN1/databases/
├── tmn1.db           — 6,985 atoms, 8,556 receipts, 3M+ DAG edges, 2,897 agents
├── staging.db        — 1,451 canon segments in crystal_active state
├── board.db          — 39 boards, 174 bounties
├── pgdata/           — PostgreSQL data (PG-primary layer for most services)
├── redis/            — Redis AOF files
└── agent_images/     — TMN neural network .pt files (agent identity = grain mass history)
```

---

## Comparison

| Metric | Beta | TMN1 |
|--------|------|-------|
| Containers | 104+ | 43 |
| Docker images | 44 (48GB) | 1 (tmn1:latest) + 3 base |
| Ports | 200+ (3000-9090) | 43 (10000-10099) |
| PostgreSQL instances | 26 | 1 |
| Redis instances | 27 | 2 |
| Compose files | 6+ | 1 (+ arena.compose.yml) |

---

## Adding a New Service

1. Write `retooling/src/retooling/<pkg>/<service>.py` (single file, FastAPI `app`, `run()` function)
2. Add `elif role == "<role_name>":` block to `infrastructure/entrypoint.py`
3. Add service block to `infrastructure/docker-compose.yml` using `<<: *tmn1-common` anchor
4. Run `./infrastructure/build.sh` to pick up the new role

No new Dockerfile. No new image. The manifold grows through the role map.
