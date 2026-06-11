# CMPLXUNI Navigation Hub

> **Internal Module Traversal Guide**  
> *Node-to-node navigation for CMPLXUNI components*

**Parent:** [README.md](./README.md) | **Ecosystem:** [CMPLX-1T NAVIGATION.md](../NAVIGATION.md)  
**You Are Here:** `repos/cmplx-uni/NAVIGATION.md` → Internal navigation

---

## 🗺️ CMPLXUNI Module Map

```
cmplx-uni/
├── NAVIGATION.md              ← You are here
├── README.md                  → [Overview](README.md)
├── AGENTS.md                  → [Agent Guide](AGENTS.md)
│
┌──┴─────────────────────────────────────────────────────┐
│                    MODULES                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐                  │
│  │   lattice/   │    │ unified_/    │                  │
│  │  → E8/Leech  │    │   families/  │                  │
│  └──────┬───────┘    │  → Families  │                  │
│         │            └──────┬───────┘                  │
│  ┌──────▼───────┐          │                          │
│  │  thinktank/  │    ┌──────▼───────┐                  │
│  │ → Deliberate │    │     mcp/     │                  │
│  └──────────────┘    │  → MCP OS    │                  │
│                      └──────────────┘                  │
│                                                         │
│  ┌──────────────┐    ┌──────────────┐                  │
│  │     hub/     │    │     cli/     │                  │
│  │  → Runtime   │    │  → Commands  │                  │
│  └──────────────┘    └──────────────┘                  │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                  APPLICATIONS                           │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐                  │
│  │ cmplx-nextjs │    │     mmdb/    │                  │
│  │  → Web UI    │    │  → Database  │                  │
│  └──────────────┘    └──────────────┘                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Primary Navigation Paths

### Path A: Geometric Intelligence (lattice/)

**Current:** `NAVIGATION.md` → **Destination:** E8/Leech lattice

| Component | Location | Purpose |
|-----------|----------|---------|
| **E8Lattice** | `src/cmplx/lattice/e8.py` | E8 root system |
| **LeechLattice** | `src/cmplx/lattice/leech.py` | 24D lattice |
| **Niemeier** | `src/cmplx/lattice/niemeier.py` | Classification |

**Key Classes:**
```python
from cmplx.lattice import E8Lattice, LeechLattice

lattice = E8Lattice()
leech = LeechLattice()
```

---

### Path B: Unified Families (unified_families/)

**Current:** `NAVIGATION.md` → **Destination:** Family system

| Component | Location | Purpose |
|-----------|----------|---------|
| **FamilyManager** | `src/cmplx/unified_families/manager.py` | Lifecycle |
| **FamilyRegistry** | `src/cmplx/unified_families/registry.py` | Discovery |
| **SNAP Labels** | `src/cmplx/unified_families/snap.py` | Tagging |

**Usage:**
```python
from cmplx.unified_families import FamilyManager

manager = FamilyManager()
family = manager.create_family("research")
```

---

### Path C: ThinkTank (thinktank/)

**Current:** `NAVIGATION.md` → **Destination:** Deliberation

| Component | Location | Purpose |
|-----------|----------|---------|
| **DeliberationEngine** | `src/cmplx/thinktank/engine.py` | Core deliberation |
| **PerspectiveSystem** | `src/cmplx/thinktank/perspectives.py` | Multi-view |
| **Consensus** | `src/cmplx/thinktank/consensus.py` | Agreement |

**Usage:**
```python
from cmplx.thinktank import ThinkTank

tank = ThinkTank()
result = tank.deliberate(query, perspectives=["analyst"])
```

---

### Path D: Applications

**Current:** `NAVIGATION.md` → **Destination:** End-user systems

| System | Location | Access |
|--------|----------|--------|
| **Next.js UI** | `cmplx-nextjs/` | http://localhost:3000 |
| **MMDB** | `mmdb/` | TCP configurable |

---

## 🔄 Cross-Module Workflows

### Workflow 1: Lattice → Family
```
NAVIGATION.md → lattice/E8Lattice → unified_families/FamilyManager
```

### Workflow 2: Family → ThinkTank
```
NAVIGATION.md → unified_families/ → thinktank/DeliberationEngine
```

### Workflow 3: Full Pipeline
```
lattice/ → unified_families/ → thinktank/ → cmplx-nextjs/
```

---

## 🌐 Ecosystem Navigation

### Up to CMPLX-1T
- **[CMPLX-1T Root](../../README.md)** - Master showroom
- **[CMPLX-1T NAVIGATION.md](../NAVIGATION.md)** - Full ecosystem map
- **[CMPLX-1T AGENTS.md](../AGENTS.md)** - Root agent guide

### Related Layers
- **[CMPLX-Baseline](../cmplx-baseline/)** ← L1-L3 (Parent layer)
- **[CMPLXDevKit](../cmplx-devkit/)** ← L5-L6 (Ancestor layer)
- **[CMPLXMCP](../cmplx-mcp/)** ← L7 (Parent layer)

---

## 📋 Quick Reference

| Task | Start | Via | End |
|------|-------|-----|-----|
| **Lattice Work** | [AGENTS.md](AGENTS.md) | `src/cmplx/lattice/` | `e8.py`, `leech.py` |
| **Family Work** | [AGENTS.md](AGENTS.md) | `src/cmplx/unified_families/` | `manager.py` |
| **ThinkTank** | [AGENTS.md](AGENTS.md) | `src/cmplx/thinktank/` | `engine.py` |
| **UI Work** | [README.md](README.md) | `cmplx-nextjs/` | React components |

---

**Parent:** [README.md](./README.md) | **Ecosystem:** [CMPLX-1T](../)

*"Navigate geometric intelligence layer by layer."*
