# ⚡ OPENCODE CLI QUICK START

## Start Services (1 Command)

```bash
cd D:\CQECMPLX-ProofValidatedSuite\kernel
docker-compose -f docker-compose-kernel-with-opencode.yml up -d
```

## Access Terminal (Choose One)

### Option A: Interactive Python REPL
```bash
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh
```

### Option B: Direct Bash
```bash
docker exec -it cqecmplx-opencode-cli bash
```

### Option C: Non-Interactive Command
```bash
docker exec cqecmplx-opencode-cli python3 << 'EOF'
import requests, json
result = requests.post("http://proof-kernel:8765/api/validate", 
    json={"papers": ["CQE-paper-00"], "token_string": "ATCGATCG"}).json()
print(json.dumps(result, indent=2))
EOF
```

---

## Common Commands

### In Interactive Terminal

```python
# Validate single paper
validate("CQE-paper-00")

# Validate batch
validate(["CQE-paper-00", "CQE-paper-01", "CQE-paper-02"])

# Check kernel status
status()

# Get response object
resp = requests.get("http://proof-kernel:8765/api/health")
print(resp.json())

# Access endpoint URL
print(endpoint)  # "http://proof-kernel:8765"
```

### From Host (Non-Interactive)

```bash
# Validate papers
docker exec cqecmplx-opencode-cli curl -X POST http://proof-kernel:8765/api/validate \
  -H "Content-Type: application/json" \
  -d '{"papers": ["CQE-paper-00"], "token_string": "ATCGATCG"}' | jq .

# Check kernel health
docker exec cqecmplx-opencode-cli curl http://proof-kernel:8765/health | jq .

# View configuration
docker exec cqecmplx-opencode-cli cat /home/developer/.opencode/config/agent-config.json | jq .
```

---

## Monitor

### Watch Terminal Logs
```bash
docker logs -f cqecmplx-opencode-cli
```

### Watch Kernel Logs
```bash
docker logs -f cqecmplx-proof-kernel
```

### Watch Level 1 Validators Spawn
```bash
watch 'docker ps -a | grep paper-validator'
```

### Check Resource Usage
```bash
docker stats --no-stream | grep cqecmplx
```

---

## Architecture

```
Terminal (2GB, 2 CPU)
    ↓
Kernel API (http://proof-kernel:8765)
    ↓
Orchestrator (4GB, 4 CPU)
    ├─ Spawns Level 1 (8 concurrent)
    └─ Each gets 2GB, 2 CPU
```

---

## Services

```
Service                Container Name              Port
─────────────────────────────────────────────────────────
Proof Kernel           cqecmplx-proof-kernel       8765
OpenCode Terminal      cqecmplx-opencode-cli       8766
Docker Provider        cqecmplx-docker-provider    (internal)
```

---

## Quick Validation Loop

```bash
# Terminal 1: Start services
docker-compose -f docker-compose-kernel-with-opencode.yml up -d

# Terminal 2: Monitor hierarchy
watch 'docker ps -a | grep -E "paper-validator|opencode"'

# Terminal 3: Run terminal and validate
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh

# In terminal:
> validate(["CQE-paper-00", "CQE-paper-01"])
```

---

## Files

| File | Purpose |
|------|---------|
| docker-compose-kernel-with-opencode.yml | Service definitions |
| scripts/opencode-start.sh | Terminal initialization |
| /opt/opencode/kernel-connect.py | Kernel connection helper |
| /opt/opencode/cli-startup.sh | REPL launcher |

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Terminal won't start | `docker logs cqecmplx-opencode-cli` |
| Can't connect to kernel | `docker exec opencode-cli curl http://proof-kernel:8765/health` |
| Validation times out | Check `docker stats` for resource starvation |
| No validators spawning | Verify kernel is running: `docker logs cqecmplx-proof-kernel` |

---

## Status

✅ OpenCode CLI terminal integrated
✅ Agent pre-configured
✅ Kernel communication established
✅ Ready for validation

**Start with**:
```bash
docker-compose -f docker-compose-kernel-with-opencode.yml up -d
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh
```

Then use `validate()` to test! 🚀
