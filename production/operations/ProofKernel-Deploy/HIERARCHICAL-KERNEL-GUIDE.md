# 🏗️ HIERARCHICAL KERNEL ORCHESTRATION GUIDE

## Template Architecture: One-Level-Down Constraint

Your kernel now enforces **strict hierarchical resource allocation** where every spawned container operates at exactly 50% of its parent's resources.

---

## 📊 THE HIERARCHY

```
┌─────────────────────────────────────────────────────────────┐
│ LEVEL 0: Master Orchestrator (Kernel)                       │
│ Resources: 4GB RAM, 4 CPU cores                             │
│ Role: Routes requests, spawns paper validators              │
│ Max children: 8 (configurable)                              │
└─────────────────────────────────────────────────────────────┘
    │
    ├─► LEVEL 1a: Paper 00 Validator (2GB, 2 CPU)
    ├─► LEVEL 1b: Paper 01 Validator (2GB, 2 CPU)
    ├─► LEVEL 1c: Paper 02 Validator (2GB, 2 CPU)
    ├─► LEVEL 1d: Paper 03 Validator (2GB, 2 CPU)
    │     │
    │     ├─► LEVEL 2a: Tool Runner (1GB, 1 CPU) [if needed]
    │     └─► LEVEL 2b: Tool Runner (1GB, 1 CPU) [if needed]
    │
    └─► [... up to 8 Level 1 containers ...] 
```

**Key Constraint**: Every child gets exactly **50% of parent's resources**.

- Level 0: 4GB → Level 1 gets 2GB (50%)
- Level 1: 2GB → Level 2 gets 1GB (50%)
- Level 2: 1GB → [Cannot spawn Level 3]

---

## 🚀 QUICK START

### 1. Start the Hierarchical Kernel

```bash
cd D:\CQECMPLX-ProofValidatedSuite\kernel

# Start the master orchestrator (Level 0)
docker-compose -f docker-compose-kernel-validated.yml up -d proof-kernel

# Verify it's running
docker logs -f cqecmplx-proof-kernel
```

### 2. Trigger Validation (Any Paper)

```bash
# Validate all papers (spawns 8 concurrent Level 1 validators)
curl -X POST http://localhost:8765/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "papers": ["CQE-paper-00", "CQE-paper-01", "CQE-paper-02", "CQE-paper-03"],
    "token_string": "ATCGATCGATCGATCG..."
  }'

# Or validate one paper
curl -X POST http://localhost:8765/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "paper_id": "CQE-paper-00",
    "token_string": "ATCGATCGATCGATCG..."
  }'
```

### 3. Monitor Hierarchy in Real-Time

```bash
# Watch Level 0 orchestrator logs
docker logs -f cqecmplx-proof-kernel

# Watch Level 1 paper validators spawning
docker ps -a | grep paper-validator

# Watch resource usage (Level 1 containers should have 2GB max)
docker stats cqecmplx-paper-*-validator
```

---

## 🔧 HOW THE HIERARCHY WORKS

### Level 0 → Level 1 (Master → Paper Validators)

When you POST to `/api/validate` with papers:

```python
# Level 0 receives request
orchestrator = HierarchicalOrchestrator(level=0, child_memory_mb=2048, child_cpu=2.0)

# For each paper, spawn Level 1 container with 50% resources
for paper_id in papers:
    container = orchestrator.spawn_child_container(
        paper_id=paper_id,
        constraints=HierarchyConstraint(
            level=1,
            memory_mb=2048,        # 50% of Level 0 (4096 / 2)
            cpu=2.0,               # 50% of Level 0 (4 / 2)
            ulimit_nproc=2048,     # 50% of Level 0 (4096 / 2)
            ulimit_nofile=32768,   # 50% of Level 0 (65536 / 2)
        )
    )
    # Container runs: paper_validator.py --paper-id CQE-paper-XX
```

### Level 1 → Level 2 (Paper Validator → Tools)

If a paper validator needs to spawn theorem verifiers:

```python
# Level 1 validator receives constraints
validator = PaperValidator(
    paper_id="CQE-paper-00",
    level=1,
    max_child_memory_mb=1024,  # 50% of Level 1 (2048 / 2)
    max_child_cpu=1.0,         # 50% of Level 1 (2 / 2)
)

# Can spawn Level 2 tool runners with those constraints
container = validator.spawn_tool_runner(
    constraints=HierarchyConstraint(
        level=2,
        memory_mb=1024,        # 50% of Level 1
        cpu=1.0,
        ulimit_nproc=1024,
        ulimit_nofile=16384,
    )
)
```

---

## 📋 RESOURCE ALLOCATION TABLE

| Level | Role | Memory | CPU | Processes | Open Files | Max Children |
|-------|------|--------|-----|-----------|------------|--------------|
| **0** | Orchestrator | 4GB | 4 | 4096 | 65536 | 8 |
| **1** | Paper Validator | 2GB | 2 | 2048 | 32768 | 4 |
| **2** | Tool Runner | 1GB | 1 | 1024 | 16384 | 0 |

**Each row is 50% of the row above.**

---

## 🧬 DNA FOLDING INTEGRATION

Each paper validator runs DNA folding at **two scales**:

### Local Scale (Paper's Native)
```python
# Run at the paper's presentation scale
local_result = await validator._validate_local_scale(token_string)
# Returns: frames, eigenvalues, workbook operations at paper's specific scale
```

### Global Scale (Full Convergence)
```python
# Run at full global scale with iterative convergence
global_result = await validator._validate_global_scale(token_string)
# Returns: falsifier iterations, Z4 cycles, proven status
```

### Isomorphism Check
```python
# Verify effects are identical at both scales (what you intended!)
isomorphic = validator._check_isomorphism(local_result, global_result)
# Returns: True if local effects match global effects
```

---

## 🎯 DOCKER-COMPOSE USAGE

### Start Everything

```bash
docker-compose -f docker-compose-kernel-validated.yml up -d

# This starts:
# 1. proof-kernel (Level 0 orchestrator)
# 2. docker-provider (docker-dind for Level 1+ spawning)
```

### Start Just the Orchestrator (Minimal)

```bash
docker-compose -f docker-compose-kernel-validated.yml up -d proof-kernel

# This is enough. Paper validators spawn dynamically when needed.
```

### Validate a Specific Paper via CLI

```bash
# Inside the kernel container
docker exec cqecmplx-proof-kernel python -m cmplx_proof_kernel.orchestrator \
  --level 0 \
  --papers CQE-paper-00 CQE-paper-01 \
  --token-string "ATCGATCG..."

# Output: Full orchestration receipt with all sub-receipts
```

---

## 🔍 MONITORING & DEBUGGING

### Watch Orchestration Hierarchy

```bash
# Terminal 1: Level 0 orchestrator
docker logs -f cqecmplx-proof-kernel

# Terminal 2: Level 1 validators (as they spawn)
watch 'docker ps -a | grep paper-validator | head -20'

# Terminal 3: Resource usage
watch 'docker stats --no-stream | grep cqecmplx'
```

### Verify Hierarchy Constraints

```bash
# Check Level 1 container memory limit (should be 2GB)
docker inspect cqecmplx-paper-00-validator | grep -A5 '"Memory"'
# Expected output: "Memory": 2147483648 (bytes = 2GB)

# Check Level 1 container CPU limit
docker inspect cqecmplx-paper-00-validator | grep -A5 '"CpuPeriod"'
# Expected output: "CpuPeriod": 100000, "CpuQuota": 200000 (= 2 cores)

# Check ulimits (should be 50% of Level 0)
docker exec cqecmplx-paper-00-validator ulimit -u
# Expected output: 2048 (50% of 4096)
```

### Extract Receipt from Container

```bash
# Get receipt from completed container
docker logs cqecmplx-paper-00-validator | tail -1 | python -m json.tool

# Or retrieve from orchestrator
curl http://localhost:8765/api/receipts/rcpt-XXXXX
```

---

## 🛠️ CUSTOMIZATION

### Change Resource Hierarchy

Edit `docker-compose-kernel-validated.yml`:

```yaml
# Change Level 0 allocation
proof-kernel:
  mem_limit: 8g        # ← Change this (was 4g)
  cpus: 8.0            # ← Change this (was 4.0)
  
# Children automatically get 50%
# CHILD_MEMORY_MB: 4096 (50% of 8GB)
# CHILD_CPU: 4.0 (50% of 8.0)
```

### Change Max Concurrent Papers

In docker-compose:

```yaml
proof-kernel:
  entrypoint: [
    "python", "-m", "cmplx_proof_kernel.orchestrator",
    "--max-papers", "16"  # ← Was 8, now 16 concurrent
  ]
```

### Custom Paper Validator Logic

Extend `PaperValidator` in `paper_validator.py`:

```python
class CustomPaperValidator(PaperValidator):
    async def _validate_local_scale(self, token_string):
        # Your custom DNA folding logic
        pass
    
    async def _validate_global_scale(self, token_string):
        # Your custom global validation
        pass
```

---

## 📦 FILES CREATED

1. **docker-compose-kernel-validated.yml**
   - Hierarchical compose file (Level 0 + Level 1 template)
   - Enforces 50% resource allocation

2. **cmplx_proof_kernel/orchestrator.py**
   - Level 0 orchestrator
   - Spawns paper validators with constraints

3. **cmplx_proof_kernel/paper_validator.py**
   - Level 1 paper validator
   - Runs DNA folding at local + global scales
   - Checks isomorphism

---

## ✅ VERIFICATION CHECKLIST

- [ ] `docker-compose -f docker-compose-kernel-validated.yml up -d`
- [ ] `docker ps` shows `cqecmplx-proof-kernel` running
- [ ] `docker logs cqecmplx-proof-kernel` shows "Starting orchestrator"
- [ ] POST to `http://localhost:8765/api/validate` triggers validation
- [ ] `docker ps` shows Level 1 `paper-validator` containers spawning
- [ ] Each Level 1 container has 2GB memory limit (check via `docker inspect`)
- [ ] Validation completes and returns JSON receipt
- [ ] Receipt includes both local and global results
- [ ] Isomorphism check passes (local effects == global effects)

---

## 🎯 KEY CONCEPT: ONE-LEVEL-DOWN

This is the **core constraint**:

```
Parent Level 0: 4GB, 4 CPU
    │
    └─ Child Level 1: 2GB, 2 CPU (50% of parent)
       │
       └─ Grandchild Level 2: 1GB, 1 CPU (50% of parent)
          │
          └─ [NO Level 3 - resources exhausted]
```

**Every container knows only its own level's constraints, plus what to give children.**

- Level 0 knows: "I'm 4GB. I'll give children 2GB."
- Level 1 knows: "I'm 2GB. I'll give children 1GB."
- Level 2 knows: "I'm 1GB. I can't spawn children."

This ensures **no child ever exceeds parent's allocation**, and **hierarchy is enforced automatically**.

---

## 🚀 NEXT STEPS

1. **Start the orchestrator**: `docker-compose up -d proof-kernel`
2. **Validate a paper**: `curl -X POST http://localhost:8765/api/validate`
3. **Monitor hierarchy**: `docker ps -a` and `docker stats`
4. **Add your DNA folding logic** to `PaperValidator` methods
5. **Implement per-paper platforms** that extend `PaperPlatform`

Your hierarchical kernel is ready! 🎉
