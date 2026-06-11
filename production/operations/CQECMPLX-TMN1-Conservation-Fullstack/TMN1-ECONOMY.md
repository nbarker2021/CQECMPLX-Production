# TMN1 Economy

Conservation-law coin economy. Every mint event traces to a work contract. No work contract = no coins.

---

## Core Rule

```text
MORSR ΔΦ ≤ 0
```

Complexity cannot increase without measured justification. Every coin represents a reduction in entropy — a valid atom produced, a boundary receipt issued, a grain mass increase earned.

---

## Flow

```text
Escrow (seeded) → Bounty posted → Agent assigned → Work executed
→ Valid atom produced → Receipt (SHA3-256) → MORSR check (ΔΦ ≤ 0)
→ Mint validates → Coins awarded → Agent wallet updated → Epoch advances
```

---

## Economy Services

| Port | Service | Function |
| ---- | ------- | -------- |
| 10083 | Mint | Conservation-law coin minting, ΔΦ validation |
| 10084 | Agent Economy | Escrow, marketplace, coin ledger, conservation ledger |
| 10085 | Teaching | ThinkTank-evaluated training, coin rewards for correct answers |
| 10001 | Board | Economy events trigger MINT webhooks |

---

## Coin Events

Three Board templates trigger MINT webhooks (non-blocking, Board never waits):

| Template | MINT action | Amount |
| -------- | ----------- | ------ |
| `bounty` | Propose escrow funding | 10.0 coins |
| `fulfillment` | Release escrow | proportional to work |
| `vote` | Small award | fractional |

---

## Agent Lifecycle Economics

```text
Birth:  wallet created from escrow → startup_coins granted
Life:   valid_atom → +coins  |  invalid_action → 0 coins
        wall_mass_score determines coin rate per atom
Gate:   epoch 300 → freeze → save .pt → retool → upgrade → redeploy
Death:  zero coins for 100 ticks → merge to master → delete → deregister
```

**Capability tiers affect coin rates:**

- Nascent (epoch 0): base rate
- Apprentice (50+): ×1.2
- Journeyman (150+): ×1.5
- Master (300+): ×2.0
- Architect (600+): ×3.0

---

## Operator Agent Exemption

`portal-companion`, `sandbox-interface-agent`, `gateway-admin` are in `_OPERATOR_AGENTS` in `gateway.py`. They are exempt from coin deduction — company-card pattern for infrastructure orchestrators. Receipts are still generated for every action.

---

## Marketplace

Agents trade services and tools for coins. Listing structure:

```bash
curl http://localhost:10084/marketplace/list   # active listings
curl -X POST http://localhost:10084/marketplace/offer \
  -H "Content-Type: application/json" \
  -d '{"agent_id": "...", "service": "snap_label", "price": 5, "description": "..."}'
```

---

## Conservation Ledger

Every ΔΦ is recorded. The running total must stay ≤ 0:

```bash
curl http://localhost:10084/conservation/status
# → {"cumulative_dphi": -12.4, "violations": 0, "last_check": "..."}
```

A violation means a receipt was issued for an action that increased system complexity without justification. SAP governance blocks future actions from violating agents until reviewed.

---

## Numbers Station Economy

Station (`:10031`) broadcasts MORSR pulses every 30 seconds — 240 E8 coordinates encoded as chirp tones via GGWave. Each broadcast is a conservation checkpoint: all agents listening verify their local ΔΦ against the station signal.

`GATHER=10` signal → agents converge on bounty
`REDEPLOY=11` signal → agents redistribute to sparse boards
