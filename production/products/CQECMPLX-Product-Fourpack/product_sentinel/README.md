# Sentinel — Zero-Trust Security Monitor

> **Your infrastructure's immune system — every anomaly mathematically proven, not guessed.**

Sentinel is a production-grade zero-trust security monitoring platform that uses syndrome-based mathematical validation to detect anomalies. Unlike rule-based SIEMs (Splunk, QRadar) or ML-based tools (CrowdStrike, Datadog) that guess, Sentinel **proves** every alert with mathematical certainty.

## The Problem

SOC teams are drowning. The average enterprise generates 10,000+ security alerts per day. 93% are false positives. Current tools can't distinguish signal from noise, can't prove an alert is valid, and can't catch zero-day attacks that don't match known signatures.

## The Solution: Mathematical Anomaly Detection

Sentinel uses the CMPLX-R30 syndrome framework — an 8-syndrome, 64-bit checkpointing system with a VOA partition ratio that forms a **physical law** of your infrastructure:

```
VOA Partition Z(q) = 2q^0 + 6q^5
```

This means **25% of your system's state should be invariant** and **75% should vary in predictable patterns**. When this ratio breaks — proven with binomial p-values and standard deviations — you have an anomaly. Not a guess. A mathematical proof.

## Key Differentiator

| Tool | Detection Method | Zero-Day Catch | Proof of Validity |
|------|-----------------|----------------|-------------------|
| **Splunk** | Rule-based | No | No |
| **CrowdStrike** | ML/signature | Sometimes | No |
| **Datadog** | Statistical | Rarely | No |
| **Sentinel** | **Mathematical VOA** | **Yes** | **Binomial p-value** |

**Splunk uses rules. CrowdStrike uses ML. Sentinel uses mathematics.**

## Architecture

```
sentinel/
  src/
    core/        # Syndrome fingerprinting engine (8-syndrome + 64-bit IDs)
    voa/         # VOA partition ratio checker (2:6 invariant:variable)
    detector/    # Real-time anomaly detection with chart state deviations
    api/         # FastAPI server with 4 endpoints + WebSocket
    agents/      # Lightweight monitoring agents (Linux / Windows / K8s)
  docker/        # Docker Compose demo stack (Prometheus + Sentinel + Grafana)
  tests/         # pytest suite with attack simulation scenarios
```

## Quick Start

### 1. Install

```bash
pip install -e .
# or with dev dependencies:
pip install -e ".[dev]"
```

### 2. Start the API Server

```bash
uvicorn sentinel.api.server:app --host 0.0.0.0 --port 8000
```

### 3. Learn a Baseline (Your Infrastructure's "DNA")

```bash
curl -X POST http://localhost:8000/baseline \
  -H "Content-Type: application/json" \
  -d '{
    "source": "web-server-01",
    "label": "Production web server",
    "metrics": {
      "cpu_percent": 45,
      "memory_percent": 60,
      "disk_percent": 30
    }
  }'
```

### 4. Monitor for Anomalies

```bash
curl -X POST http://localhost:8000/monitor \
  -H "Content-Type: application/json" \
  -d '{
    "source": "web-server-01",
    "metrics": {
      "cpu_percent": 95,
      "memory_percent": 92,
      "disk_percent": 35
    }
  }'
```

Every response includes the VOA ratio, standard deviation, p-value, and proof statement.

### 5. View Alerts (with Mathematical Proof)

```bash
curl "http://localhost:8000/alerts?severity=critical&limit=10"
```

Every alert includes:
- **VOA deviation** in standard deviations
- **Binomial p-value** (probability this is natural)
- **Confidence percentage**
- **Syndrome-level breakdown**
- **Proof hash** for tamper verification

### 6. Audit Trail (Immutable Checkpoints)

```bash
curl "http://localhost:8000/audit?source=web-server-01"
```

Every system state transition is recorded with a 64-bit ID in a cryptographically chained ledger.

## Docker Compose (Full Demo Stack)

```bash
cd docker
docker-compose up -d
```

Services:
- **Sentinel API**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/sentinel)

## Monitoring Agents

### Linux Agent

```bash
python -m sentinel.agents.linux_agent \
  --api-url http://sentinel:8000 \
  --source web-server-01 \
  --interval 30
```

### Kubernetes Agent (DaemonSet)

```bash
# See docker/k8s-agent.yaml for full manifest
kubectl apply -f docker/k8s-agent.yaml
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/health` | GET | Health check |
| `/baseline` | POST | Learn normal syndrome fingerprint |
| `/monitor` | POST | Real-time anomaly detection |
| `/alerts` | GET | Query alerts with proof |
| `/audit` | GET | Immutable checkpoint log |
| `/stats` | GET | Service statistics |
| `/stream` | WS | WebSocket real-time alerts |

## The Mathematics

### 8-Syndrome System

Every system state maps to one of 8 LocalTriad patterns (3-bit LCR combinations):

| Syndrome | Triad | Type | Geometry Level |
|----------|-------|------|----------------|
| 0 | (0,0,0) | Deep Invariant | 0 |
| 1 | (0,0,1) | Variable | 2 |
| 2 | (0,1,0) | Level-1 Invariant | 1 |
| 3 | (0,1,1) | Variable | 2 |
| 4 | (1,0,0) | Variable | 2 |
| 5 | (1,0,1) | Level-1 Invariant | 1 |
| 6 | (1,1,0) | Variable | 2 |
| 7 | (1,1,1) | Deep Invariant | 0 |

### VOA Partition

```
Z(q) = 2q^0 + 6q^5
```

- **2 deep invariants** (q^0 = constant, never change)
- **6 variables** (q^5 = responds to pressure)
- **Expected ratio: 2/8 = 25% invariant, 6/8 = 75% variable**

When this ratio deviates, the binomial p-value tells you exactly how unlikely that is:
- **p > 0.05**: Nominal (healthy)
- **0.01 < p < 0.05**: Elevated (watch)
- **0.001 < p < 0.01**: Warning (investigate)
- **p < 0.001**: Critical/ Emergency (confirmed compromise)

### 64-Bit Checkpoint IDs

Every system state transition gets a 64-bit ID encoding:
- Syndrome index (3 bits)
- Geometry level (3 bits)
- Emission + correction (2 bits)
- Chart state index (6 bits)
- Monotonic sequence (50 bits)

Checkpoints are cryptographically chained — modify any entry, all subsequent hashes become invalid.

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=sentinel

# Run specific attack scenarios
pytest tests/test_attack_scenarios.py -v

# Run core mathematical validation
pytest tests/test_core.py -v
```

## Attack Simulation Scenarios

Sentinel includes simulated attack scenarios that validate detection:

1. **DDoS Attack** — total pattern collapse (0% invariant)
2. **Credential Stuffing** — repeated failed login patterns
3. **Data Exfiltration** — sustained high outbound traffic
4. **Cryptojacking** — CPU saturation (100% invariant)
5. **Lateral Movement** — abnormal process/network patterns
6. **Zero-Day (Unknown)** — what rules miss, math catches

```bash
pytest tests/test_attack_scenarios.py -v
```

## Configuration

### Detection Rules

```python
from sentinel.detector.detector import DetectionRule

rule = DetectionRule(
    name="strict",
    description="High-sensitivity rule",
    min_sigma=1.5,                    # trigger at 1.5 std dev
    min_p_value=0.05,                 # trigger if p < 0.05
    max_transitions_per_window=100,   # chart transition limit
    window_seconds=60,                # observation window
    sources=["web-*", "api-*"],       # source filter
    actions=["log", "webhook", "pagerduty"],
)
```

## Requirements

- Python 3.10+
- No external database required (file-based persistence)
- Optional: Docker, Kubernetes

## License

MIT — see LICENSE file for details.

---

**Sentinel**: Your infrastructure's immune system — mathematically proven anomaly detection.
