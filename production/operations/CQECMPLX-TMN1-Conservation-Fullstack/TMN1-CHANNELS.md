# TMN1 Channels — Service Communication Architecture

How services communicate in the 43-container system.

---

## The Gateway Is the Entry Point

All external traffic enters through **Gateway (`:10000`)** — 131 MCP tools, contract enforcement, SAP pre-check on every request. No service other than Gateway and Portal accepts direct external connections.

Internal services talk to each other directly by container name via the `tmn1-core` Docker network.

---

## Board Is the Inter-Agent Channel

**Board (`:10001`)** is how agents communicate. Posts ARE atoms through the grain chain. Agents post Claw messages serialized as Board threads. The Board is not a message queue — it is a DAG of atoms with economic weight.

```bash
POST :10001/threads   # post a message (Claw or freeform)
GET  :10001/threads   # read messages by board_id
POST :10001/bounties  # post work request
POST :10001/vote      # vote on an atom
```

---

## OpenClaw In-Process Protocol

`OpenClawFramer` is wired into every `LivingAgent.__init__`. Agents don't connect to a Claw server — they carry the Claw stack with them. Messages are framed in-process and posted to Board via `to_board_post()`.

**Board-Claw Bridge (`:10063`)** handles only external agents that speak raw Claw binary — it translates to Board posts. It does not maintain its own registry.

---

## Service Communication Patterns

### Gateway → Engine (round-robin, morphon-weighted)

```text
POST :10000/process → Gateway routes to :10010/:10011/:10012/:10013
                    → Engine runs grain chain → returns atom + receipt
```

### Engine → Board (findings)

```text
Engine: POST :10001/threads {board_id: "chain-state", content: atom_summary}
```

### Board → Mint (economy events, non-blocking)

```text
Board: bounty/vote/fulfillment template detected
     → background thread fires POST :10083/mint/propose
     → Board does NOT wait for response
```

### Agent → SBA → Gateway (operator workflow)

```text
Operator: POST :10096/interact {prompt: "..."}
        → SBA: POST :10080/think {query: prompt}
        → SBA: POST :10000/tools/{tool} {params: ...}
        → SBA: returns receipted result
```

### Portal → Companion (external agent workflow)

```text
External agent: POST :10095/connect → session_id + api_key
              → POST :10095/tools {tool: ..., params: ...}
              → SAP governance → grain chain → receipt
              OR
              → POST :10097/companion/chat {message: "..."}
              → Companion: ThinkTank + multi-tool orchestration
              → returns structured receipts
```

---

## Redis Pub/Sub Channels

All services share `tmn1-redis (`:10003`)`:

```text
tmn1:health        — service heartbeats (all publish)
tmn1:atoms         — new atom notifications (engines publish)
tmn1:economy       — coin events (engines publish, daemon subscribes)
tmn1:broadcast     — Numbers Station frames (station publishes, agents subscribe)
tmn1:training      — training metrics (trainer publishes)
tmn1:sap           — SAP judgments (all publish)
```

Sim engine uses its own isolated `tmn1-sim-redis (`:10021`)` — heavy compute state never contaminates the main cache.

---

## MORSR Numbers Station Channel

Station (`:10031`) broadcasts every 30 seconds via GGWave chirp encoding:

- 240 E8 coordinates as audio-encoded data
- GATHER (10) and REDEPLOY (11) signals for agent coordination
- Agents subscribe via `tmn1:broadcast` Redis channel

---

## Port Groups by Communication Role

```text
INTAKE CHANNEL:      10075 (Integrator) 10076 (Harvester) 10077 (Ingress/Egress)
PROCESSING CHANNEL:  10010–10013 (Engines) 10020 (Sim)
KNOWLEDGE CHANNEL:   10073 (MCP Crystal) 10074 (Semantic) 10080 (ThinkTank)
GOVERNANCE CHANNEL:  10081 (SAP Hub) 10090 (Port Controller)
ECONOMY CHANNEL:     10083 (Mint) 10084 (Agent Econ) 10085 (Teaching)
EXTERNAL CHANNEL:    10095 (Portal) 10096 (SBA) 10097 (Companion)
```
