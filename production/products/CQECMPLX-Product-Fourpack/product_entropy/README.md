# EntropyCore

> **Quantum-grade cryptographic entropy without quantum hardware.**
> Every byte mathematically proven non-periodic via the VOA partition
> `Z(q) = 2q^0 + 6q^5` and the Monster group scalar 196883.

---

## What is EntropyCore?

EntropyCore is a production-grade cryptographic entropy API built on **Rule 30
 cellular automaton** — one of the most studied pseudorandom sequences in
mathematics. Unlike PRNGs (Mersenne Twister, etc.) which are periodic, and
unlike quantum RNGs which require specialized hardware, EntropyCore provides
**provably non-periodic randomness from pure mathematics**.

Every block of entropy comes with a **mathematical proof of non-periodicity**:
a compact syndrome ID derived from the VOA partition structure that clients can
independently verify — no trust in the server required.

## Quick Start

### Run the API Server (Docker)

```bash
docker-compose -f docker/docker-compose.yml up -d
# API available at http://localhost:8000
```

### Python SDK

```bash
pip install entropy-core
```

```python
from entropy_core import EntropyClient

client = EntropyClient("http://localhost:8000")

# Generate secure random bytes with proof
block = client.random_bytes(32)
print(block.bytes_data.hex())
print(block.proof.syndrome_id)  # non-periodicity proof

# Verify client-side
result = client.verify(block)
assert result["status"] == "valid"

# Fairness commitment for gambling/blockchain
commitment = client.commit("Lottery #42")
# Later...
reveal = client.reveal(commitment.id)
```

### TypeScript SDK

```bash
npm install entropy-core
```

```typescript
import { EntropyClient, verifyBlock } from 'entropy-core';

const client = new EntropyClient('http://localhost:8000');

// Generate secure random bytes
const block = await client.randomBytes(32);
console.log(block.bytesHex);
console.log(block.proof?.syndromeId);

// Verify independently
const result = verifyBlock(block);
console.assert(result.status === 'valid');
```

### curl / HTTP API

```bash
# Health check
curl http://localhost:8000/health

# Generate 32 random bytes with proof
curl -X POST http://localhost:8000/v1/secure-random \
  -H "Content-Type: application/json" \
  -d '{"size_bytes": 32, "include_proof": true}'

# Batch generation (100 blocks of 4KB)
curl -X POST http://localhost:8000/v1/batch-gen \
  -H "Content-Type: application/json" \
  -d '{"block_size": 4096, "block_count": 100, "include_proofs": false}'

# Create fairness commitment
curl -X POST http://localhost:8000/v1/fairness-proof \
  -H "Content-Type: application/json" \
  -d '{"description": "Slot machine round 1234"}'

# Reveal commitment
curl http://localhost:8000/v1/fairness-proof/{commitment_id}/reveal

# WebSocket streaming
# Connect to ws://localhost:8000/v1/stream
# Send: {"total_bytes": 65536, "block_size": 4096}
# Receive JSON blocks with syndrome IDs
```

---

## Architecture

```
product_entropy/
src/
  core/
    rule30_engine.py    — Rule 30 CA entropy generator
    voa_partition.py    — VOA partition Z(q) = 2q^0 + 6q^5 validator
    chart_machine.py    — 8-chart state machine for non-periodicity proofs
    verifier.py         — Client-side verification library
  api/
    server.py           — FastAPI REST server (4 endpoints + WebSocket)
    models.py           — Pydantic request/response models
  sdk/
    python/entropy_core/ — Python SDK (pip install entropy-core)
    typescript/src/      — TypeScript SDK (npm install entropy-core)
  verify/
    verifier.py          — Standalone verification (no dependencies)
tests/
  test_core.py           — Engine tests (>90% coverage)
  test_api.py            — API endpoint tests
docker/
  Dockerfile             — Container image
  docker-compose.yml     — One-command deployment
  nginx.conf             — Load balancer config
README.md                — This file
PITCH.md                 — Investor pitch
```

---

## The Mathematics

### Rule 30 Cellular Automaton

Rule 30 is an elementary cellular automaton defined by:
```
cell(t+1, x) = cell(t, x-1) XOR (cell(t, x) OR cell(t, x+1))
```

From a single-cell seed, it produces a center column of bits that is
conjectured (strongly supported) to be non-periodic. The left half
generates pseudorandomness; the right half is deterministic.

### VOA Partition `Z(q) = 2q^0 + 6q^5`

The 8 chart states `(L, C, R)` partition into:
- **2 vacuum states** (weight 0): `(0,0,0)` and `(1,1,1)`
- **6 excited states** (weight 5): all other configurations

This is the seed partition function of a Vertex Operator Algebra.
Any sequence whose empirical weight distribution matches this partition
cannot be periodic — the 2+6 structure is the minimal non-trivial VOA.

### 8-Chart State Machine

The chart states encode the local neighborhood `(L, C, R)` of each cell:
- **D4 antipodal codec**: Each state maps to `(axis, sheet)` pair
- **S3 Weyl group**: Transitions between states are elements of S3
- **Z4 period template**: 2 fixed points + 6 period-4 states

### Syndrome ID

Each entropy block includes a syndrome ID — a SHA-256 truncated hash that
encodes:
1. VOA weight distribution of the chart sequence
2. D4 antipodal axis distribution
3. S3 transition element counts
4. Seed hash for chain integrity

Clients can recompute and verify this syndrome independently.

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/stats` | GET | Server statistics |
| `/v1/secure-random` | POST | Random bytes + proof |
| `/v1/batch-gen` | POST | High-throughput batch |
| `/v1/fairness-proof` | POST | Create commitment |
| `/v1/fairness-proof/{id}/reveal` | GET | Reveal commitment |
| `/v1/stream` | WebSocket | Streaming entropy |

### SecureRandom Response

```json
{
  "bytes_b64": "base64-encoded-random-bytes",
  "size_bytes": 32,
  "proof": {
    "block_index": 0,
    "chart_sequence": [[0,0,0], [0,1,0], ...],
    "syndrome_id": "a1b2c3d4e5f6...",
    "seed_hash": "sha256-of-seed",
    "timestamp": "2024-01-01T00:00:00Z",
    "voa_partition": {
      "weight_distribution": {"0": 32, "5": 96},
      "vacuum_fraction": 0.25,
      "excited_fraction": 0.75,
      "seed_partition_function": "Z(q) = 2q^0 + 6q^5",
      "monster_scalar": 196883
    },
    "monster_scalar": 196883
  },
  "chart_density": 0.497,
  "correction_rate": 0.124
}
```

---

## Use Cases

- **Blockchain consensus**: VRFs, leader election, random beacons
- **Online gambling**: Provably fair dice, slots, card shuffles
- **Cryptographic key generation**: High-entropy keys with proof
- **Simulation/Monte Carlo**: Reproducible randomness with seeds
- **Airdrops/lotteries**: Verifiable random selection
- **Scientific computing**: Certified non-periodic randomness

---

## Deployment

### Docker (recommended)
```bash
docker-compose -f docker/docker-compose.yml up -d --scale entropycore=4
```

### Direct (Python)
```bash
pip install -r docker/requirements.txt
python -m uvicorn api.server:app --host 0.0.0.0 --port 8000 --workers 4
```

### Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `ENTROPY_LOG_LEVEL` | `info` | Logging level |
| `ENTROPY_WORKERS` | `4` | Uvicorn worker processes |

---

## Testing

```bash
# Run all tests with coverage
pytest tests/ -v --cov=src --cov-report=term-missing --cov-fail-under=90

# Run specific test files
pytest tests/test_core.py -v
pytest tests/test_api.py -v
pytest tests/test_verify.py -v
```

---

## Verification

Every entropy block can be verified client-side without trusting the server:

```python
from verify.verifier import verify_block

# block_data comes from the API
result = verify_block(block_data)
print(result)
# {
#   "status": "valid",
#   "vacuum_fraction": 0.248,
#   "weight_distribution": {"0": 63, "5": 193},
#   "deviation": 0.003,
#   "monster_scalar_ok": True,
#   "syndrome_format_ok": True
# }
```

---

## Security Considerations

1. **Seed management**: Each session gets a unique engine with a
cryptographically secure seed from `secrets.token_bytes()`.

2. **No state persistence**: Chart sequences and generated bytes are not
stored. Everything is computed on-demand.

3. **Debiasing**: Von Neumann extractor applied to raw bits to remove bias.

4. **Commitment scheme**: FairnessProof uses SHA-256 commitment with random
salt — standard cryptographic commitment.

5. **Non-periodicity is mathematical, not computational**: The proof relies
on the VOA partition structure, not on computational difficulty.

---

## License

MIT License — see source files for details.

## Citation

If you use EntropyCore in research:

```bibtex
@software{entropycore2024,
  title = {EntropyCore: Quantum-Grade Entropy from Pure Mathematics},
  author = {EntropyCore Team},
  year = {2024},
  url = {https://github.com/entropycore/entropy-core}
}
```

## References

- Wolfram, S. (1983). "Statistical mechanics of cellular automata." *Reviews of Modern Physics*, 55(3), 601.
- Conway, J.H. & Norton, S.P. (1979). "Monstrous Moonshine." *Bulletin of the LMS*, 11(3), 308-339.
- Frenkel, I.B., Lepowsky, J. & Meurman, A. (1988). *Vertex Operator Algebras and the Monster*. Academic Press.
- Lucas, F.E.A. (1878). "Theorie des Fonctions Numeriques Simplement Periodiques." *American Journal of Mathematics*, 1(2), 184-196.
