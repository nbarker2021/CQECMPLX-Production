# ✅ HIERARCHICAL KERNEL — VERIFICATION & DEPLOYMENT CHECKLIST

## Pre-Flight Checklist (Before First Run)

- [ ] **Environment Ready**
  - [ ] Docker installed (`docker --version`)
  - [ ] Docker Compose installed (`docker-compose --version`)
  - [ ] Python 3.10+ available in container
  - [ ] Docker socket at `/var/run/docker.sock` accessible

- [ ] **Files Present**
  - [ ] `docker-compose-kernel-validated.yml` exists
  - [ ] `cmplx_proof_kernel/orchestrator.py` exists
  - [ ] `cmplx_proof_kernel/paper_validator.py` exists
  - [ ] `cmplx_proof_kernel/falsifier.py` exists
  - [ ] `cmplx_proof_kernel/workbook.py` exists
  - [ ] `cmplx_proof_kernel/platforms.py` exists

- [ ] **Documentation Present**
  - [ ] `HIERARCHICAL-KERNEL-GUIDE.md` exists
  - [ ] `QUICK-REFERENCE.md` exists
  - [ ] `ARCHITECTURE-DIAGRAMS.md` exists
  - [ ] `README-HIERARCHICAL-INDEX.md` exists

- [ ] **Configuration Reviewed**
  - [ ] Resource allocation (4GB, 4 CPU for Level 0)
  - [ ] Child allocation (2GB, 2 CPU for Level 1)
  - [ ] Network configuration (172.20.0.0/16)
  - [ ] Port mappings (8765 for API)

---

## Deployment Checklist

### Step 1: Start Orchestrator

- [ ] Navigate to kernel directory
  ```bash
  cd D:\CQECMPLX-ProofValidatedSuite\kernel
  ```

- [ ] Start services
  ```bash
  docker-compose -f docker-compose-kernel-validated.yml up -d proof-kernel
  ```

- [ ] Verify service started
  ```bash
  docker ps | grep cqecmplx-proof-kernel
  ```
  Expected: Container running with status "Up X seconds"

- [ ] Check logs for errors
  ```bash
  docker logs cqecmplx-proof-kernel
  ```
  Expected: "Starting AI/ML Toolkit..." or similar startup message

### Step 2: Verify Network

- [ ] Check network exists
  ```bash
  docker network ls | grep cqecmplx-kernel-net
  ```
  Expected: Network listed

- [ ] Verify container on network
  ```bash
  docker network inspect cqecmplx-kernel-net
  ```
  Expected: `cqecmplx-proof-kernel` listed in Containers

### Step 3: Test HTTP API

- [ ] Check health endpoint
  ```bash
  curl http://localhost:8765/health
  ```
  Expected: `{"status": "healthy"}` or similar

- [ ] List papers (if implemented)
  ```bash
  curl http://localhost:8765/api/papers
  ```

### Step 4: Verify Resource Constraints

- [ ] Check Level 0 memory limit
  ```bash
  docker inspect cqecmplx-proof-kernel | grep -A2 '"Memory"'
  ```
  Expected: `4294967296` (bytes = 4GB)

- [ ] Check Level 0 CPU limit
  ```bash
  docker inspect cqecmplx-proof-kernel | grep -A2 '"CpuPeriod"'
  ```
  Expected: `"CpuPeriod": 100000, "CpuQuota": 400000` (4 cores)

- [ ] Check Level 0 ulimits
  ```bash
  docker exec cqecmplx-proof-kernel ulimit -u
  ```
  Expected: `4096` (processes)

### Step 5: Trigger Validation (Single Paper)

- [ ] Send validation request
  ```bash
  curl -X POST http://localhost:8765/api/validate \
    -H "Content-Type: application/json" \
    -d '{
      "papers": ["CQE-paper-00"],
      "token_string": "ATCGATCGATCGATCG"
    }'
  ```

- [ ] Monitor orchestrator logs
  ```bash
  docker logs -f cqecmplx-proof-kernel
  ```
  Expected: Logs showing "Validating CQE-paper-00", container spawn, etc.

- [ ] Monitor Level 1 container spawn
  ```bash
  watch 'docker ps -a | grep paper-validator'
  ```
  Expected: `cqecmplx-paper-00-validator-XXXXXXXX` appears

### Step 6: Verify Level 1 Constraints

- [ ] Get Level 1 container name
  ```bash
  docker ps -a | grep paper-validator | head -1 | awk '{print $NF}'
  # Output: cqecmplx-paper-00-validator-XXXXXXXX
  ```

- [ ] Check Level 1 memory (should be 2GB)
  ```bash
  docker inspect cqecmplx-paper-00-validator-XXXXXXXX | grep '"Memory"'
  ```
  Expected: `2147483648` (bytes = 2GB)

- [ ] Check Level 1 CPU (should be 2 cores)
  ```bash
  docker inspect cqecmplx-paper-00-validator-XXXXXXXX | grep -A1 '"CpuQuota"'
  ```
  Expected: `"CpuQuota": 200000` (2 cores)

- [ ] Check Level 1 ulimits
  ```bash
  docker exec cqecmplx-paper-00-validator-XXXXXXXX ulimit -u
  ```
  Expected: `2048` (processes)

### Step 7: Verify Receipt Generation

- [ ] Wait for validation to complete
  - Monitor `docker logs -f cqecmplx-proof-kernel` for completion

- [ ] Check HTTP response
  ```bash
  curl http://localhost:8765/api/receipts/rcpt-XXXXX
  ```
  Expected: JSON receipt with `status: "pass"` or `"fail"`

- [ ] Verify receipt structure
  ```bash
  # Last API response should contain:
  # - orchestrator_id
  # - papers_validated
  # - papers_passed
  # - papers_failed
  # - total_duration_seconds
  # - results: [...]
  ```

### Step 8: Batch Validation (Multiple Papers)

- [ ] Request validation of 4 papers
  ```bash
  curl -X POST http://localhost:8765/api/validate \
    -H "Content-Type: application/json" \
    -d '{
      "papers": [
        "CQE-paper-00",
        "CQE-paper-01",
        "CQE-paper-02",
        "CQE-paper-03"
      ],
      "token_string": "ATCGATCGATCGATCG"
    }'
  ```

- [ ] Monitor Level 1 spawning (should spawn 4 concurrently)
  ```bash
  watch 'docker ps -a | grep paper-validator'
  ```
  Expected: 4 `cqecmplx-paper-XX-validator-*` containers

- [ ] Monitor resource usage
  ```bash
  docker stats --no-stream | grep cqecmplx
  ```
  Expected: Each L1 container ~2GB (or less if not using full allocation)

- [ ] Verify no L1 exceeds 2GB
  ```bash
  for container in $(docker ps -a | grep paper-validator | awk '{print $NF}'); do
    echo "$container: $(docker inspect $container | grep '"Memory"' | head -1)"
  done
  ```
  Expected: All containers show `2147483648` (2GB max)

---

## Integration Checklist (After Orchestrator Verified)

- [ ] **Paper Platforms Ready**
  - [ ] PaperPlatform base class understood
  - [ ] Paper00, Paper01, etc. stubs loaded
  - [ ] Verifier functions stub-ified but callable

- [ ] **DNA Folding Logic**
  - [ ] Local scale DNA folding implementation plan
  - [ ] Global scale convergence plan
  - [ ] Isomorphism check logic designed
  - [ ] Test sequences prepared

- [ ] **Custom Validators**
  - [ ] Per-paper validator logic implemented
  - [ ] Local scale tests passing
  - [ ] Global scale tests passing
  - [ ] Isomorphism verified

- [ ] **Receipt Validation**
  - [ ] Receipts parse as valid JSON
  - [ ] Hash verification works
  - [ ] Status correctly set
  - [ ] Results embedded as expected

---

## Production Readiness Checklist

- [ ] **Stability**
  - [ ] Orchestrator runs continuously
  - [ ] L1 containers complete successfully
  - [ ] No memory leaks observed (monitor `docker stats`)
  - [ ] Network stable (no disconnections)

- [ ] **Performance**
  - [ ] Single paper validation < 30 seconds
  - [ ] Batch of 8 papers < 60 seconds
  - [ ] Resource utilization reasonable
  - [ ] No CPU throttling

- [ ] **Error Handling**
  - [ ] Malformed requests return 400
  - [ ] Invalid papers return 404
  - [ ] Timeout gracefully after 1 hour
  - [ ] Errors logged and reported

- [ ] **Documentation**
  - [ ] Setup instructions complete
  - [ ] Quick reference available
  - [ ] Troubleshooting guide updated
  - [ ] Architecture diagrams accurate

- [ ] **Security**
  - [ ] Docker socket properly mounted (read-only where possible)
  - [ ] No hardcoded credentials in images
  - [ ] Containers run as non-root
  - [ ] Network properly isolated

---

## Full Suite Validation (All 32 Papers)

- [ ] Request all papers
  ```bash
  curl -X POST http://localhost:8765/api/validate \
    -H "Content-Type: application/json" \
    -d '{
      "papers": [
        "CQE-paper-00", "CQE-paper-01", ..., "CQE-paper-31"
      ],
      "token_string": "ATCGATCGATCGATCGATCG..."
    }'
  ```

- [ ] Monitor hierarchy spawn
  ```bash
  # Terminal 1: Orchestrator
  docker logs -f cqecmplx-proof-kernel
  
  # Terminal 2: L1 containers
  watch 'docker ps -a | grep paper-validator | wc -l'
  
  # Terminal 3: Resources
  watch 'docker stats --no-stream'
  ```

- [ ] Verify correct concurrency
  - Max 8 L1 containers running at once
  - Each consuming ~2GB max
  - No L1 container exceeds Level 0 allocation

- [ ] Collect final receipts
  ```bash
  # Extract from last response
  curl http://localhost:8765/api/receipts | jq .
  ```

- [ ] Verify all receipts valid
  - All 32 papers have receipts
  - All receipts contain hash
  - All receipts contain local + global results
  - All contain isomorphism check

---

## Troubleshooting During Deployment

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Orchestrator won't start | Check docker socket | Verify `/var/run/docker.sock` exists |
| L1 containers crash | Check logs | `docker logs cqecmplx-paper-*-validator-*` |
| Memory limit exceeded | Check docker inspect | Verify `-m 2g` in compose file |
| API not responding | Check port binding | `docker port cqecmplx-proof-kernel` |
| L1 not spawning | Check docker socket permissions | `chmod` docker socket if needed |
| Receipt missing hash | Check paper_validator code | Verify hash computation in code |
| Isomorphism always false | Check DNA logic | Verify local/global scaling |
| Timeout | Check resource starvation | Monitor `docker stats` |

---

## Post-Deployment

- [ ] **Backup & Archive**
  - [ ] Save docker-compose file
  - [ ] Save all implementation code
  - [ ] Archive all receipts
  - [ ] Document any customizations

- [ ] **Monitoring Setup**
  - [ ] Enable container log rotation
  - [ ] Set up metrics collection (if desired)
  - [ ] Define alerting (if desired)

- [ ] **Knowledge Transfer**
  - [ ] Document deployment procedure
  - [ ] Document paper addition process
  - [ ] Train team on troubleshooting
  - [ ] Create runbook for common tasks

---

## Final Verification

- [ ] **All checklist items completed** ✓
- [ ] **Orchestrator running** ✓
- [ ] **Level 1 containers spawning** ✓
- [ ] **Receipts generating** ✓
- [ ] **Constraints enforced** ✓
- [ ] **Documentation complete** ✓

**Status**: **READY FOR PRODUCTION** 🚀

---

## Notes & Observations

**Date Started**: _____________
**Deployment Started**: _____________
**Orchestrator First Run**: _____________
**First Validation Complete**: _____________
**Full Suite Validated**: _____________

**Observations**:
```
(Record any notes, issues resolved, customizations made)
```

**Next Steps**:
```
(List follow-up tasks, optimizations, etc.)
```

---

**Deployment Complete!** Your hierarchical kernel is ready for validation. 🎉
