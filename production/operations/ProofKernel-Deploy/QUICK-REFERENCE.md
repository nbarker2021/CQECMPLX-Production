# HIERARCHICAL KERNEL — QUICK REFERENCE

## One-Line Summary
**Orchestrator spawns paper validators at 50% resources. Each validator runs DNA folding locally & globally, proves isomorphism.**

---

## File Structure

```
kernel/
├── docker-compose-kernel-validated.yml    # Hierarchical compose template
├── cmplx_proof_kernel/
│   ├── orchestrator.py                   # Level 0 (Master)
│   ├── paper_validator.py                # Level 1 (Per-Paper)
│   ├── falsifier.py                      # DNA folding + convergence
│   ├── workbook.py                       # Sheet ⇄ Tool isomorphism
│   ├── platforms.py                      # Per-paper validation rules
│   └── kernel_core.py                    # Core types
└── HIERARCHICAL-KERNEL-GUIDE.md         # Full guide (this file)
```

---

## Quick Commands

```bash
# Start orchestrator (Level 0)
docker-compose -f docker-compose-kernel-validated.yml up -d proof-kernel

# Validate papers
curl -X POST http://localhost:8765/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "papers": ["CQE-paper-00", "CQE-paper-01"],
    "token_string": "ATCGATCG..."
  }'

# Watch orchestration
docker logs -f cqecmplx-proof-kernel
docker ps -a | grep paper-validator
docker stats --no-stream

# Check Level 1 memory (should be 2GB)
docker inspect cqecmplx-paper-00-validator | grep '"Memory"'
```

---

## Resource Hierarchy

```
Level 0 (Master Orchestrator)
  Memory: 4GB    | CPU: 4   | Processes: 4096 | Open Files: 65536
  
  → Spawns 8 concurrent Level 1 containers (50% each)
  
  Level 1 (Paper Validator) × N
    Memory: 2GB  | CPU: 2   | Processes: 2048 | Open Files: 32768
    
    → Can spawn Level 2 containers (50% each)
    
    Level 2 (Tool Runner) × M
      Memory: 1GB | CPU: 1   | Processes: 1024 | Open Files: 16384
      
      → Cannot spawn Level 3 (resources exhausted)
```

**Rule**: Child = 50% of Parent (every layer, every resource).

---

## Data Flow

```
1. HTTP Request (POST /api/validate)
   ↓
2. Level 0 Orchestrator receives papers list
   ↓
3. For each paper:
   └─ Spawn Level 1 Paper Validator (2GB, 2 CPU)
     ├─ Validate at LOCAL scale (paper's native scale)
     │  └─ DNA folding, workbook operations, local frames/eigenvalues
     ├─ Validate at GLOBAL scale (full convergence)
     │  └─ Falsifier test, Z4 cycles, iterative convergence
     └─ Check ISOMORPHISM (local effects == global effects?)
   ↓
4. Collect all receipts from Level 1 containers
   ↓
5. Return orchestrator receipt with all sub-receipts
```

---

## Environment Variables (Auto-Set)

### Level 0 (Master)
```
KERNEL_LEVEL=0
KERNEL_ROLE=orchestrator
KERNEL_MAX_MEMORY_MB=4096
KERNEL_MAX_CPU=4
CHILD_MEMORY_MB=2048        # What to give Level 1
CHILD_CPU=2.0
```

### Level 1 (Paper Validator)
```
KERNEL_LEVEL=1
KERNEL_ROLE=paper_validator
PAPER_ID=CQE-paper-00
KERNEL_MAX_MEMORY_MB=2048
KERNEL_MAX_CPU=2.0
CHILD_MEMORY_MB=1024        # What to give Level 2
CHILD_CPU=1.0
DNA_VALIDATION_MODE=paper
```

### Level 2 (Tool Runner) [if spawned]
```
KERNEL_LEVEL=2
KERNEL_ROLE=tool_runner
KERNEL_MAX_MEMORY_MB=1024
KERNEL_MAX_CPU=1.0
DNA_VALIDATION_MODE=theorem
```

---

## Receipt Structure

```json
{
  "orchestrator_id": "orch-xyz123",
  "level": 0,
  "papers_validated": 4,
  "papers_passed": 3,
  "papers_failed": 1,
  "total_duration_seconds": 45.3,
  "results": [
    {
      "paper_id": "CQE-paper-00",
      "status": "pass",
      "duration_seconds": 12.5,
      "receipt": {
        "receipt_id": "rcpt-abc123",
        "paper_id": "CQE-paper-00",
        "status": "pass",
        "local_result": {
          "theorems_passed": 3,
          "theorems_failed": 0,
          "frames": [1, 4, 4, 4, 1, 4, 4, 4],
          "workbook_operations": 5
        },
        "global_result": {
          "theorems_passed": 1,
          "theorems_failed": 0,
          "z4_cycles": 2,
          "falsifier_iterations": 3
        },
        "isomorphic": true
      }
    },
    ...
  ]
}
```

---

## DNA Folding Integration

Each paper validator tests:

### ✓ Local Scale
- Paper's native DNA encoding
- Workbook operations at paper's scale
- Frames: [1, 4, 4, 4] repeating pattern
- Eigenvalues: {1, -1, i, -i}

### ✓ Global Scale
- Full DNA sequence convergence
- Falsifier test (5 checks)
- Iterative refinement until proven
- Z4 cycle verification

### ✓ Isomorphism
- Local effects appear at global scale
- No scale-dependent divergence
- Proves hand-folding rules hold everywhere

---

## Hierarchy Enforcement

**Docker limits applied to each container:**

```bash
# Level 0
--memory 4g
--cpus 4.0
--ulimit nproc=4096
--ulimit nofile=65536

# Level 1 (spawned by Level 0)
--memory 2g         # 50% of parent
--cpus 2.0          # 50% of parent
--ulimit nproc=2048 # 50% of parent
--ulimit nofile=32768 # 50% of parent

# Level 2 (if spawned by Level 1)
--memory 1g         # 50% of parent
--cpus 1.0          # 50% of parent
--ulimit nproc=1024 # 50% of parent
--ulimit nofile=16384 # 50% of parent
```

**No child can exceed parent's allocation.** Enforced by Docker daemon.

---

## Testing Hierarchy

```bash
# Terminal 1: Watch orchestrator
docker logs -f cqecmplx-proof-kernel

# Terminal 2: Trigger validation
curl -X POST http://localhost:8765/api/validate \
  -H "Content-Type: application/json" \
  -d '{"papers": ["CQE-paper-00", "CQE-paper-01", "CQE-paper-02", "CQE-paper-03"]}'

# Terminal 3: Watch Level 1 containers spawn
watch 'docker ps -a | grep paper-validator'

# Terminal 4: Monitor resources
docker stats --no-stream | grep cqecmplx

# Verify Level 1 has 2GB limit
docker inspect cqecmplx-paper-00-validator-* | grep '"Memory"'
# Output: 2147483648 (bytes) = 2GB ✓
```

---

## Customization

### Change Master Resource Allocation
Edit `docker-compose-kernel-validated.yml`:
```yaml
proof-kernel:
  mem_limit: 8g        # ← Change this
  cpus: 8.0            # ← Change this
  # Children get 50% automatically
```

### Change Max Concurrent Papers
Edit compose or CLI:
```bash
--max-papers 16        # Was 8, now 16 concurrent
```

### Add Custom DNA Folding Logic
Edit `cmplx_proof_kernel/paper_validator.py`:
```python
async def _validate_local_scale(self, token_string):
    # Your DNA folding code here
    pass

async def _validate_global_scale(self, token_string):
    # Your convergence code here
    pass
```

---

## Troubleshooting

| Issue | Check |
|-------|-------|
| Orchestrator won't start | `docker logs cqecmplx-proof-kernel` |
| Level 1 containers crash | `docker logs cqecmplx-paper-*-validator-*` |
| Memory limit exceeded | Check `docker inspect` for actual limits |
| No JSON receipt | Ensure container logs end with `{...}` |
| Validation hangs | Check `docker stats` for resource starvation |
| Isomorphism fails | DNA folding logic mismatch (local vs global) |

---

## API Endpoints

```
POST /api/validate
  Body: { "papers": ["CQE-paper-00", ...], "token_string": "..." }
  Returns: Orchestrator receipt

GET /api/health
  Returns: {"status": "healthy", ...}

GET /api/papers
  Returns: List of registered papers

GET /api/receipts/{receipt_id}
  Returns: Individual receipt
```

---

## Summary

✅ **Hierarchical**: 3-level constraint (0→1→2)
✅ **One-Level-Down**: Each child gets 50% of parent
✅ **DNA-Native**: Local + Global DNA folding with isomorphism
✅ **Scalable**: Easily add 32 papers with independent platforms
✅ **Deterministic**: Hashed receipts, reproducible validation

Ready to validate the Wolfram Prize proofs! 🚀
