# 🖥️ OPENCODE CLI TERMINAL - INTEGRATED AGENT GUIDE

## What You Now Have

An **OpenCode CLI terminal service** with a **pre-configured agent** that:
- Runs as a dedicated Docker container
- Integrates with your proof kernel infrastructure
- Provides interactive terminal for kernel operations
- Automatically connects to kernel API
- Supports direct validation commands

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────┐
│ Host                                     │
│ ┌────────────────────────────────────┐  │
│ │ Browser/Terminal Access            │  │
│ │ (localhost:8765 + 8766)            │  │
│ └────────────────┬─────────────────────┘  │
│                  │                        │
│        ┌─────────┴────────┐               │
│        │                  │               │
└────────┼──────────────────┼───────────────┘
         │                  │
         ↓                  ↓
    ┌─────────────────┐  ┌─────────────────┐
    │ proof-kernel    │  │ opencode-cli    │
    │ (Level 0)       │  │ (Terminal)      │
    │ 4GB, 4CPU       │  │ 2GB, 2CPU       │
    │ Orchestrator    │  │ Agent + REPL    │
    └─────────────────┘  └─────────────────┘
          │                     │
          └─────────┬───────────┘
                    │ (Direct API)
              ┌─────┴─────┐
              │ Shared    │
              │ Network   │
              │ & Docker  │
              └───────────┘
                    │
                    ↓
          ┌─────────────────┐
          │ Level 1 Paper   │
          │ Validators      │
          │ (Spawned on     │
          │  demand)        │
          └─────────────────┘
```

---

## 🚀 Quick Start

### 1. Start Both Services

```bash
cd D:\CQECMPLX-ProofValidatedSuite\kernel

# Start orchestrator + OpenCode terminal
docker-compose -f docker-compose-kernel-with-opencode.yml up -d

# Verify both running
docker ps | grep cqecmplx
```

Expected output:
```
cqecmplx-proof-kernel          Running
cqecmplx-opencode-cli          Running
cqecmplx-docker-provider       Running
```

### 2. Access OpenCode Terminal

```bash
# Option A: Direct shell access
docker exec -it cqecmplx-opencode-cli bash

# Option B: Interactive terminal
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh
```

### 3. Use Interactive Commands

```python
# Inside the OpenCode CLI terminal

# Validate a single paper
> validate("CQE-paper-00")

# Validate multiple papers
> validate(["CQE-paper-00", "CQE-paper-01", "CQE-paper-02"])

# Check kernel status
> status()

# Access kernel directly
> requests.get(endpoint + "/api/health")
```

---

## 📋 File Structure

```
kernel/
├── docker-compose-kernel-with-opencode.yml
│   ├─ proof-kernel service (Level 0)
│   ├─ opencode-terminal service (Level 1)
│   └─ docker-provider service
│
└── scripts/
    └── opencode-start.sh
        ├─ Verifies configuration
        ├─ Creates workspace
        ├─ Generates agent config
        ├─ Sets up kernel connection
        └─ Launches REPL terminal
```

---

## 🔧 OpenCode Terminal Features

### 1. Auto-Configuration
```
✓ Workspace created at /opt/opencode
✓ Agent registered as "cqecmplx-agent"
✓ Kernel connection established
✓ History enabled (1000 lines)
```

### 2. Pre-Configured Agent
```json
{
  "agent": {
    "name": "cqecmplx-agent",
    "type": "docker",
    "kernel_aware": true,
    "capabilities": [
      "container_management",
      "kernel_communication",
      "dna_validation",
      "receipt_retrieval",
      "paper_orchestration"
    ]
  }
}
```

### 3. Interactive REPL
```python
# Available in terminal:
terminal          # Terminal object with methods
validate()        # Validate papers
status()          # Get kernel status
requests          # HTTP client
json              # JSON utilities
endpoint          # Kernel URL
```

---

## 💬 Common Commands

### Validate Papers

```bash
# Terminal command
docker exec -it cqecmplx-opencode-cli python3 << 'EOF'
from pathlib import Path
exec(Path('/opt/opencode/kernel-connect.py').read_text())

# Inside Python:
terminal = OpenCodeTerminal("http://proof-kernel:8765")
terminal.validate(["CQE-paper-00", "CQE-paper-01"])
EOF
```

### Check Kernel Health

```bash
docker exec -it cqecmplx-opencode-cli curl http://proof-kernel:8765/health | jq .
```

### Monitor Paper Validators Spawning

```bash
# From host (in separate terminal)
watch 'docker ps -a | grep paper-validator'
```

### Get OpenCode Terminal Logs

```bash
docker logs -f cqecmplx-opencode-cli
```

---

## 🔌 Integration Points

### 1. Kernel Communication
```python
# Terminal ↔ Kernel API
kernel_endpoint = "http://proof-kernel:8765"
requests.post(f"{kernel_endpoint}/api/validate", json={...})
```

### 2. Docker Interaction
```
Terminal container has access to:
- /var/run/docker.sock (read-only)
- cqecmplx-kernel-net (shared network)
- kernel_state volume (read-only)
```

### 3. Shared Network
```
All containers on: 172.20.0.0/16
- proof-kernel: 172.20.0.2
- opencode-terminal: 172.20.0.3
- docker-provider: 172.20.0.4
- Level 1 validators: 172.20.0.5+
```

---

## 📊 Resource Allocation

```
OpenCode Terminal (opencode-cli):
  Memory: 2GB (50% of kernel, same as Level 1 papers)
  CPU: 2 cores
  Processes: 2048
  Files: 32768
```

This allows the terminal to run as if it were a Level 1 container, capable of spawning Level 2 tools if needed.

---

## 🎯 Example Workflows

### Workflow 1: Single Paper Validation

```bash
# Start terminal
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh

# In terminal
> validate("CQE-paper-00")
Validating 1 paper(s)...
{
  "orchestrator_id": "orch-xyz123",
  "papers_validated": 1,
  "papers_passed": 1,
  "results": [...]
}
```

### Workflow 2: Batch Validation with Monitoring

```bash
# Terminal 1: Start validation
docker exec -it cqecmplx-opencode-cli python3 << 'EOF'
terminal.validate([f"CQE-paper-{i:02d}" for i in range(8)])
EOF

# Terminal 2: Monitor spawning
watch 'docker ps -a | grep paper-validator | wc -l'

# Terminal 3: Monitor resources
watch 'docker stats --no-stream'
```

### Workflow 3: Interactive Inspection

```python
# In terminal REPL

# Get kernel status
status_response = status()
print(f"Active papers: {status_response.get('active_papers', 0)}")

# Validate specific paper
result = validate("CQE-paper-00")
print(f"Status: {result['results'][0]['status']}")

# Get receipt
receipt_id = result['results'][0]['receipt']['receipt_id']
receipt = requests.get(f"{endpoint}/api/receipts/{receipt_id}").json()
print(f"Local result: {receipt['local_result']}")
print(f"Global result: {receipt['global_result']}")
print(f"Isomorphic: {receipt['isomorphic']}")
```

---

## 🔍 Troubleshooting

### Terminal Won't Start

```bash
# Check logs
docker logs cqecmplx-opencode-cli

# Verify kernel is running
docker logs cqecmplx-proof-kernel

# Manual connection test
docker exec cqecmplx-opencode-cli \
  curl -v http://proof-kernel:8765/health
```

### Agent Not Registering

```bash
# Check agent config
docker exec cqecmplx-opencode-cli \
  cat /home/developer/.opencode/config/agent-config.json

# Kernel might not support agent registration (non-fatal)
# Terminal will still work for validation
```

### Validation Hanging

```bash
# Check resource usage
docker stats cqecmplx-opencode-cli

# Check if Level 1 validators are spawning
docker ps -a | grep paper-validator

# Increase timeout if needed
# Validation can take 5-10min for all 32 papers
```

### Network Issues

```bash
# Verify network connection
docker exec cqecmplx-opencode-cli \
  ping -c 3 proof-kernel

# Expected: ping succeeds
```

---

## 📈 Advanced Usage

### Custom Validation Function

```python
# In terminal, create custom function
def validate_with_callback(papers, callback):
    """Validate papers with real-time callback"""
    result = terminal.validate(papers)
    for paper_result in result.get('results', []):
        callback(paper_result)
    return result

# Use it
def print_result(r):
    print(f"{r['paper_id']}: {r['status']}")

validate_with_callback(["CQE-paper-00", "CQE-paper-01"], print_result)
```

### Receipt Processing

```python
# Retrieve and analyze all receipts
def analyze_receipts(paper_ids):
    for paper_id in paper_ids:
        # Request validation
        result = validate(paper_id)
        receipt = result['results'][0]['receipt']
        
        # Analyze
        print(f"{paper_id}:")
        print(f"  Local: {receipt['local_result']['theorems_passed']} passed")
        print(f"  Global: {receipt['global_result']['theorems_passed']} passed")
        print(f"  Isomorphic: {receipt['isomorphic']}")

analyze_receipts([f"CQE-paper-{i:02d}" for i in range(5)])
```

### Kernel Exploration

```python
# Get available endpoints
response = requests.get(f"{endpoint}/api/papers")
papers = response.json()
print(f"Available papers: {len(papers)}")

# Check active validations
response = requests.get(f"{endpoint}/api/status")
status = response.json()
print(f"Active papers: {status.get('active_papers', 0)}")
print(f"Completed: {status.get('completed_papers', 0)}")
```

---

## 🔐 Security

### OpenCode Terminal Isolation
- Runs as separate container (isolated from kernel)
- Read-only access to kernel state
- Docker socket mounted read-only (where possible)
- Network isolated to cqecmplx-kernel-net

### Agent Security
- No hardcoded credentials
- Environment-based configuration
- Audit logging enabled
- Sandbox mode by default

---

## 📝 Configuration Options

Edit `docker-compose-kernel-with-opencode.yml` to customize:

```yaml
opencode-terminal:
  mem_limit: 2g          # Change terminal memory
  cpus: 2.0              # Change terminal CPU
  
  environment:
    OPENCODE_AGENT_MODE: "enabled"  # or "disabled"
    OPENCODE_AUTO_CONNECT: "true"   # or "false"
    OPENCODE_HISTORY_SIZE: "1000"   # Change history
```

---

## ✅ Verification Checklist

- [ ] Both services running: `docker ps | grep cqecmplx`
- [ ] Kernel healthy: `curl http://localhost:8765/health`
- [ ] Terminal connecting: `docker logs cqecmplx-opencode-cli`
- [ ] Agent configured: `docker exec opencode-cli cat /home/developer/.opencode/config/agent-config.json`
- [ ] Can validate: `docker exec opencode-cli python3 /opt/opencode/kernel-connect.py`

---

## 🎉 Summary

You now have:

✅ **Dedicated OpenCode Terminal** — Separate container for CLI
✅ **Pre-Configured Agent** — Auto-registers with kernel
✅ **Interactive REPL** — Python shell with kernel methods
✅ **Direct Kernel Integration** — Terminal ↔ Kernel API
✅ **Validation Commands** — Single-line paper validation
✅ **Network Integration** — Shared network with infrastructure

Start with:
```bash
docker-compose -f docker-compose-kernel-with-opencode.yml up -d
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh
```

Then use `validate()` and `status()` commands! 🚀
