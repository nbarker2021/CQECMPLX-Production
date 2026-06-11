# TMN1 Playbooks

Operational templates for common workflows. Each playbook is itself an atom — it goes through the grain chain, gets SNAP labels, and can be invoked by agents as a tool.

---

## Playbook: Ingest New Content Family

Use when adding a new family of source material.

```bash
# 1. Add content root to harvester env
#    (infrastructure/docker-compose.yml → tmn1-harvester → CONTENT_ROOT_N)

# 2. Trigger discovery (dry run first)
curl -X POST http://localhost:10076/scan \
  -H "Content-Type: application/json" \
  -d '{"dry_run": true}'

# 3. Review discovered items with family labels
curl "http://localhost:10076/items?status=discovered"

# 4. Run ingestion
curl -X POST http://localhost:10076/scan \
  -H "Content-Type: application/json" \
  -d '{"dry_run": false}'

# 5. Verify atoms created
curl "http://localhost:10000/atoms/search?q=family.<name>&limit=10"
```

**Family labels** are auto-detected from path. 19 canonical families: morphonic, tarpit, e8, cqe, lattice, quadratic_frame, snaplat, complex_t, quorum, lsdt, uhp, agrm_mdhg, snap, cmplx, lowest_priority, promutate_construct, aletheia, bridge, kimi.

---

## Playbook: Port External Code (UPP)

Universal Port Protocol — 6 phases for all external code.

```bash
# Phase 1: DISCOVER — what exists
curl -X POST http://localhost:10075/discover \
  -H "Content-Type: application/json" \
  -d '{"path": "/host/source_dir", "family": "morphonic"}'

# Phase 2: ATTACH — bind to retooling namespace
curl -X POST http://localhost:10075/attach \
  -H "Content-Type: application/json" \
  -d '{"source_id": "...", "target_package": "retooling.morphonic"}'

# Phase 3-6: STUDY → RECANONIZE → VALIDATE → INTEGRATE (automated)
curl -X POST http://localhost:10075/integrate \
  -H "Content-Type: application/json" \
  -d '{"source_id": "...", "auto": true}'
```

Everything outside TMN1 is latent content, already waiting to be ported. The UPP is the formal protocol for that transition.

---

## Playbook: Run Crystallization Cycle

Use after significant new intake to crystallize segments into the MCP tool registry.

```bash
# 1. Apply canon to all uncrystallized segments
curl -X POST http://localhost:10089/apply_canon

# 2. Monitor progress
watch -n 5 'curl -s http://localhost:10089/crystal/status'

# 3. Verify MCP Crystal picked up new tools
curl http://localhost:10073/status

# 4. Force SBA tool map refresh
curl -X POST http://localhost:10096/register_tools
```

---

## Playbook: Spawn and Assign Agent

```bash
# 1. Spawn agent via identity service
curl -X POST http://localhost:10032/agents/spawn \
  -H "Content-Type: application/json" \
  -d '{"tier": "nascent", "domain": "geometry", "initial_coins": 100}'

# 2. Post bounty for the work
curl -X POST http://localhost:10001/bounties \
  -H "Content-Type: application/json" \
  -d '{
    "requested_by": "operator",
    "need": "extend E8 lattice atom coverage",
    "context": "current atoms: 6985, target: 10000",
    "blocking": "crystal expansion"
  }'

# 3. Daemon assigns agent to bounty on next 30s tick
curl http://localhost:10030/status  # confirm assignment
```

---

## Playbook: Connect External Agent via Portal

```bash
# 1. Connect (get session credentials)
curl -X POST http://localhost:10095/connect \
  -H "Content-Type: application/json" \
  -d '{
    "agent_name": "research-agent",
    "model": "claude-opus-4-6",
    "purpose": "explore E8 geometry"
  }'

# 2. Use tools (replace API_KEY with response value)
curl -X POST http://localhost:10095/tools \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: API_KEY" \
  -d '{"tool": "process_atom", "params": {"content": "E8 lattice geometry"}}'

# 3. Review reports
curl "http://localhost:10095/reports/ACTION_ID?type=expanded" \
  -H "X-Api-Key: API_KEY"

# 4. Commit findings (optional)
curl -X POST http://localhost:10095/commit \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: API_KEY" \
  -d '{"action_ids": ["..."], "justification": "extended geometry coverage"}'
```

---

## Playbook: MDHG Hash Exploration

```bash
# 1. Create sandbox session
SESSION=$(curl -s -X POST http://localhost:10062/session/create | python -c "import sys,json; print(json.load(sys.stdin)['session_id'])")

# 2. Navigate through levels
curl -X POST http://localhost:10062/session/navigate \
  -H "Content-Type: application/json" \
  -d "{\"session_id\": \"$SESSION\", \"level\": \"Planet\", \"content\": \"E8 lattice atom\"}"

# 3. Cross-correlate with other hashes
curl -X POST http://localhost:10062/session/cross_correlate \
  -H "Content-Type: application/json" \
  -d "{\"session_id\": \"$SESSION\", \"hashes\": {\"atom_1\": \"...\", \"atom_2\": \"...\"}}"

# 4. Teardown
curl -X DELETE "http://localhost:10062/session/$SESSION"
```

---

## Playbook: Image Rebuild and Deploy

```bash
# 1. Build (runs smoke tests for all roles)
cd d:/CMPLX-TMN1
./infrastructure/build.sh

# 2. Tag as master if stable
./infrastructure/build.sh --master

# 3. Rolling restart (picks up new image without downtime)
cd infrastructure
docker compose up -d

# 4. Verify
docker compose ps              # all 43 Up
curl http://localhost:10000/health
curl http://localhost:10096/status
```

---

## Playbook: Diagnose a Stuck Service

```bash
# 1. Check logs
docker compose logs --tail=50 tmn1-<service>

# 2. Check health
curl http://localhost:<port>/health

# 3. Check dependencies
docker compose ps | grep -E "tmn1-pg|tmn1-redis|tmn1-board"

# 4. Restart in order
docker compose restart tmn1-<service>

# 5. If persistent: full rebuild
./infrastructure/build.sh && docker compose up -d tmn1-<service>
```
