# HIERARCHICAL KERNEL ARCHITECTURE — VISUAL DIAGRAMS

## 1. Overall Hierarchy Tree

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│                      LEVEL 0: ORCHESTRATOR                             │
│                   (4GB RAM, 4 CPU, 4096 processes)                    │
│                     cqecmplx-proof-kernel                              │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │ Role: Parse requests, route to papers, collect receipts         │ │
│  │ Entry: python -m cmplx_proof_kernel.orchestrator                │ │
│  │ API: http://localhost:8765                                       │ │
│  │ Max Spawned: 8 concurrent Level 1 validators                    │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ↓50%  ↓50%  ↓50%  ↓50%  ↓50%  ↓50%  ↓50%  ↓50%                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
         │        │        │        │        │        │        │        │
         ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓
    ┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐...
    │ LEVEL 1 ││ LEVEL 1 ││ LEVEL 1 ││ LEVEL 1 ││ LEVEL 1 │
    │ Paper00 ││ Paper01 ││ Paper02 ││ Paper03 ││ Paper04 │
    │ (2GB, 2 ││ (2GB, 2 ││ (2GB, 2 ││ (2GB, 2 ││ (2GB, 2 │
    │ CPU)    ││ CPU)    ││ CPU)    ││ CPU)    ││ CPU)    │
    └─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
        │           │           │           │
        ↓50%        ↓50%        ↓50%        ↓50%
        │           │           │           │
    ┌─────────┐    ┌─────────┐
    │ LEVEL 2 │    │ LEVEL 2 │
    │ Tool-00 │    │ Tool-01 │
    │ (1GB, 1 │    │ (1GB, 1 │
    │ CPU)    │    │ CPU)    │
    └─────────┘    └─────────┘
```

**Key**: Each child has exactly 50% of parent's resources (guaranteed by Docker).

---

## 2. Orchestration Data Flow

```
┌──────────────────────┐
│ HTTP POST Request    │
│ /api/validate        │
│ { papers: [...] }    │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────────────────────────────────┐
│      Level 0 Orchestrator                        │
│  Parse request, enumerate papers                 │
│  Max concurrent = 8                              │
└──────────┬───────────────────────────────────────┘
           │
           │ Batch 1: [Paper-00, 01, 02, 03, 04, 05, 06, 07]
           │
      ┌────┴─────────────────────────┬──────────────┬──────────────┐
      │                              │              │              │
      ↓                              ↓              ↓              ↓
 ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
 │ L1 Container │  │ L1 Container │  │ L1 Container │  │ L1 Container │
 │ Paper-00    │  │ Paper-01     │  │ Paper-02     │  │ Paper-03     │
 │ (2GB, 2CPU) │  │ (2GB, 2CPU)  │  │ (2GB, 2CPU)  │  │ (2GB, 2CPU)  │
 └────┬────────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
      │                  │                 │                 │
      ├─ Local Scale    ├─ Local Scale    ├─ Local Scale    ├─ Local Scale
      │  (paper-native) │  (paper-native) │  (paper-native) │  (paper-native)
      │                 │                 │                 │
      ├─ Global Scale   ├─ Global Scale   ├─ Global Scale   ├─ Global Scale
      │  (convergence)  │  (convergence)  │  (convergence)  │  (convergence)
      │                 │                 │                 │
      ├─ Isomorphism?   ├─ Isomorphism?   ├─ Isomorphism?   ├─ Isomorphism?
      │  (local==global)│  (local==global)│  (local==global)│  (local==global)
      │                 │                 │                 │
      ↓                 ↓                 ↓                 ↓
 ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
 │ Receipt     │  │ Receipt      │  │ Receipt      │  │ Receipt      │
 │ (JSON)      │  │ (JSON)       │  │ (JSON)       │  │ (JSON)       │
 └─────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
      │                  │                 │                 │
      └──────────────────┴─────────────────┴─────────────────┘
                         │
                         ↓
          ┌──────────────────────────────────────┐
          │ Level 0 Collects all Receipts        │
          │ Aggregates into Orchestrator Receipt │
          │ { papers_passed: 4, papers_failed: 0,│
          │   results: [...], total_duration: ...}
          └──────────────────────────────────────┘
                         │
                         ↓
          ┌──────────────────────────────────────┐
          │ Return to Client (HTTP 200)          │
          │ Full JSON with all sub-receipts      │
          └──────────────────────────────────────┘
```

---

## 3. Resource Hierarchy Enforcement

```
┌─────────────────────────────────────────────────────────────────┐
│ LEVEL 0: Master Orchestrator                                    │
│                                                                 │
│ Memory:        4 GB     ──────┐                                 │
│ CPU:           4 cores  ──────┤── Level 0 Full Allocation      │
│ Processes:     4096     ──────┤                                 │
│ Open Files:    65536    ──────┘                                 │
│                                                                 │
│  Docker Limits:                                                 │
│  ├─ mem_limit: 4g                                              │
│  ├─ cpus: 4.0                                                  │
│  ├─ ulimit nproc: 4096                                         │
│  └─ ulimit nofile: 65536                                       │
│                                                                 │
│  Orchestrator Computes Child Allocation:                       │
│  ├─ CHILD_MEMORY_MB = 4096 ÷ 2 = 2048                          │
│  ├─ CHILD_CPU = 4.0 ÷ 2 = 2.0                                  │
│  ├─ CHILD_ULIMIT_NPROC = 4096 ÷ 2 = 2048                       │
│  └─ CHILD_ULIMIT_NOFILE = 65536 ÷ 2 = 32768                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────────────┐
        │ LEVEL 1: Paper Validator (spawned, Level 0 aware)  │
        │ Inherits 50% of parent's allocation                │
        │                                                     │
        │ Memory:        2 GB     ──────┐                    │
        │ CPU:           2 cores  ──────┤── Level 1 Full     │
        │ Processes:     2048     ──────┤   Allocation       │
        │ Open Files:    32768    ──────┘   (Parent-Limited) │
        │                                                     │
        │ Docker Limits (set by orchestrator):               │
        │ ├─ mem_limit: 2g        (50% of Level 0)          │
        │ ├─ cpus: 2.0            (50% of Level 0)          │
        │ ├─ ulimit nproc: 2048   (50% of Level 0)          │
        │ └─ ulimit nofile: 32768 (50% of Level 0)          │
        │                                                     │
        │ Paper Validator Computes Grandchild Allocation:    │
        │ ├─ GRANDCHILD_MEMORY_MB = 2048 ÷ 2 = 1024         │
        │ ├─ GRANDCHILD_CPU = 2.0 ÷ 2 = 1.0                 │
        │ ├─ GRANDCHILD_ULIMIT_NPROC = 2048 ÷ 2 = 1024      │
        │ └─ GRANDCHILD_ULIMIT_NOFILE = 32768 ÷ 2 = 16384   │
        │                                                     │
        └─────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────────────────┐
        │ LEVEL 2: Tool Runner (optional, if spawned)        │
        │ Inherits 50% of parent's allocation                │
        │                                                     │
        │ Memory:        1 GB     ──────┐                    │
        │ CPU:           1 core   ──────┤── Level 2 Full     │
        │ Processes:     1024     ──────┤   Allocation       │
        │ Open Files:    16384    ──────┘   (Parent-Limited) │
        │                                                     │
        │ Docker Limits (set by Level 1):                    │
        │ ├─ mem_limit: 1g        (50% of Level 1)          │
        │ ├─ cpus: 1.0            (50% of Level 1)          │
        │ ├─ ulimit nproc: 1024   (50% of Level 1)          │
        │ └─ ulimit nofile: 16384 (50% of Level 1)          │
        │                                                     │
        │ Tool Runner Cannot Spawn Level 3:                  │
        │ └─ Resources would be 512MB, 0.5 CPU (infeasible) │
        │                                                     │
        └─────────────────────────────────────────────────────┘
```

---

## 4. DNA Folding Process (Per Paper Validator)

```
LEVEL 1 Paper Validator Receives: token_string + paper_id
                    │
                    ├─ Load paper platform (CQE-paper-XX)
                    │
                    ├─────────────────────────────────────────┐
                    │                                         │
        ┌───────────┴────────────────┐         ┌──────────────┴────────┐
        │                            │         │                       │
        ↓                            ↓         ↓                       ↓
    LOCAL SCALE                 GLOBAL SCALE              ISOMORPHISM CHECK
    (Paper-Native)               (Full Convergence)        (Local == Global?)
    
    ├─ Load theorems             ├─ Run falsifier test     ├─ Compare frames
    ├─ Run workbook ops          ├─ Iterative convergence  ├─ Compare eigenvalues
    ├─ Compute frames            ├─ Verify Z4 cycles       ├─ Check pattern match
    ├─ Compute eigenvalues       ├─ Check all 5 conditions ├─ Return: true/false
    └─ Return LocalScaleResult   └─ Return GlobalScaleResult
    
    LocalScaleResult {            GlobalScaleResult {      Result {
      frames: [1,4,4,4,...],        falsifier_iters: 3,    isomorphic: bool,
      eigenvalues: [{...}],         z4_cycles: 2,          local_frames: [...],
      theorems_passed: 3,           theorems_passed: 1,    global_frames: [...],
      workbook_ops: 5,              theorems_failed: 0,    all_consistent: bool
    }                             }
        │                           │
        └───────────────┬───────────┘
                        │
                        ↓
        ┌───────────────────────────────────────┐
        │ FINAL RECEIPT (JSON)                  │
        │ ┌─────────────────────────────────┐  │
        │ │ receipt_id: "rcpt-xyz"          │  │
        │ │ paper_id: "CQE-paper-00"        │  │
        │ │ status: "pass" or "fail"        │  │
        │ │ local_result: {...}             │  │
        │ │ global_result: {...}            │  │
        │ │ isomorphic: true/false          │  │
        │ │ duration_seconds: 12.5          │  │
        │ └─────────────────────────────────┘  │
        │                                       │
        │ Emit: print(json.dumps(receipt))    │
        └───────────────────────────────────────┘
```

---

## 5. Constraint Enforcement Timeline

```
T=0: User requests validation
     │
     ├─► Level 0 starts
     │   Memory: 4GB ✓
     │   CPU: 4 cores ✓
     │
T=1: Level 0 spawns Level 1 containers (8 concurrent)
     │
     ├─► Paper-00 Container
     │   Memory: 2GB (LIMITED BY DOCKER) ✓
     │   CPU: 2 cores (LIMITED BY DOCKER) ✓
     │   ulimit nproc: 2048 (LIMITED BY DOCKER) ✓
     │   ulimit nofile: 32768 (LIMITED BY DOCKER) ✓
     │
     ├─► Paper-01 Container
     │   Memory: 2GB (LIMITED BY DOCKER) ✓
     │   CPU: 2 cores (LIMITED BY DOCKER) ✓
     │   ...
     │
T=2-30: Level 1 containers run DNA folding
     │
     ├─► Paper-00:
     │   ├─ Local scale: frames, eigenvalues
     │   ├─ Global scale: falsifier, convergence
     │   └─ Isomorphism: compare results
     │
     └─► Paper-01, 02, 03, ...
         (same process)
     
T=31: Level 1 containers complete, emit receipts
     │
     └─► Level 0 collects all receipts
         Aggregates: papers_passed=8, papers_failed=0
         Returns to client
         
T=32: Orchestration complete
      All Level 1 containers cleaned up
      Docker enforces Level 0 still has 4GB
      (even though 8×2GB children exist temporarily)
```

**Key Point**: Docker enforces memory limits **per container**. If 8 Level 1 containers run concurrently, each gets exactly 2GB (50% of Level 0's 4GB), and the orchestrator still maintains its 4GB.

---

## 6. Container Naming Convention

```
Level 0 (Always singleton):
└─ cqecmplx-proof-kernel
   (fixed name, always running)

Level 1 (Spawned dynamically):
└─ cqecmplx-paper-{paper_id}-validator-{random_hex}
   Examples:
   ├─ cqecmplx-paper-00-validator-a1b2c3d4
   ├─ cqecmplx-paper-01-validator-e5f6g7h8
   ├─ cqecmplx-paper-02-validator-i9j0k1l2
   └─ ...

Level 2 (Optional, spawned by L1):
└─ cqecmplx-tool-{tool_id}-{random_hex}
   Examples:
   ├─ cqecmplx-tool-verifier-m3n4o5p6
   └─ cqecmplx-tool-falsifier-q7r8s9t0

Lifecycle:
├─ T=1s: L1 containers spawn
├─ T=2-30s: L1 containers run
├─ T=31s: L1 containers complete
└─ T=32s: `docker rm` cleans them up
```

---

## 7. Configuration Matrix

```
┌────────┬──────────┬────────────┬────────────┬───────────┬────────┐
│ Level  │ Memory   │ CPU Cores  │ Processes  │ Files     │ Max    │
│        │          │            │ (nproc)    │ (nofile)  │ Kids   │
├────────┼──────────┼────────────┼────────────┼───────────┼────────┤
│ L0     │ 4 GB     │ 4          │ 4096       │ 65536     │ 8      │
│ L1     │ 2 GB     │ 2          │ 2048       │ 32768     │ 2-4    │
│ L2     │ 1 GB     │ 1          │ 1024       │ 16384     │ 0      │
└────────┴──────────┴────────────┴────────────┴───────────┴────────┘

Calculation:
└─ Child = Parent ÷ 2 (all dimensions)
└─ No child can exceed parent
└─ No negotiation (enforced by Docker daemon)
```

---

## Summary

✅ **Clear Hierarchy**: L0 → L1 → L2
✅ **Strict Constraints**: 50% rule at each level
✅ **Automatic Enforcement**: Docker daemon handles it
✅ **Scalable**: Easy to add 32 papers
✅ **DNA-Aware**: Local + Global + Isomorphism check per paper

This is your production-grade kernel orchestration template! 🚀
