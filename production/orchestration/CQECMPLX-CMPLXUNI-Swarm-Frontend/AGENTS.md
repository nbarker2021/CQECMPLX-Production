# CMPLXUNI - Agent Integration Guide

> **AI Agent Guide - CMPLXUNI**  
> *Layer L8: Families, E8/Leech Lattice, MMDB*

**Parent Navigation:** [CMPLX-1T NAVIGATION.md](../NAVIGATION.md) | **CMPLXUNI README:** [README.md](./README.md)  
**You Are Here:** `repos/cmplx-uni/AGENTS.md` → Agent guide for L8 enterprise layer

---

## 🎯 Agent Traversal Paths

```
START: CMPLXUNI AGENTS.md (you are here)
  → PATH 1: [README.md] → Component overview
  → PATH 2: [NAVIGATION.md] → Internal module map
  → PATH 3: [src/cmplx/lattice/] → E8/Leech implementation
  → PATH 4: [src/cmplx/unified_families/] → Family system
  → PATH 5: [src/cmplx/thinktank/] → Deliberation engine
  → PATH 6: [../NAVIGATION.md] → Cross-repo navigation
END: Context acquired, begin L8 work
```

---

## 🧩 Core Components

### Geometric Intelligence (`src/cmplx/lattice/`)
E8/Leech lattice operations:
- **E8Lattice** - 8-dimensional root system
- **LeechLattice** - 24-dimensional unimodular lattice
- **NiemeierLattices** - Classification system
- **SNAP** - Type-agnostic coordinates

### Unified Families (`src/cmplx/unified_families/`)
Family-based computation:
- **FamilyManager** - Lifecycle management
- **FamilyRegistry** - Discovery and routing
- **SNAP Labels** - Universal tagging

### ThinkTank (`src/cmplx/thinktank/`)
Deliberation system:
- **DeliberationEngine** - Core deliberation
- **PerspectiveSystem** - Multi-viewpoint analysis
- **ConsensusBuilding** - Agreement algorithms

---

## 🔗 Cross-Repository Links

### Parent Context
- **[CMPLX-1T Root](../../README.md)** - Master showroom
- **[CMPLX-1T AGENTS.md](../AGENTS.md)** - Root agent standards
- **[CMPLX-1T NAVIGATION.md](../NAVIGATION.md)** - Ecosystem navigation

### Related Repos
- **[CMPLX-Baseline](../cmplx-baseline/)** ← L1-L3 infrastructure
- **[CMPLXDevKit](../cmplx-devkit/)** ← L5-L6 development
- **[CMPLXMCP](../cmplx-mcp/)** ← L7 composables (sibling)

---

## 🛠️ Development Standards

### Geometric Computing
```python
from cmplx.lattice import E8Lattice

# Initialize lattice
lattice = E8Lattice()

# Generate root system
roots = lattice.generate_root_system()

# SNAP coordinates
snap = lattice.snap_to_e8(vector)
```

### Family Management
```python
from cmplx.unified_families import FamilyManager

manager = FamilyManager()
family = manager.create_family("name", config={})
```

### ThinkTank Usage
```python
from cmplx.thinktank import ThinkTank

tank = ThinkTank()
result = tank.deliberate(query, perspectives=["analyst", "critic"])
```

---

## 📝 Key Patterns

| Pattern | Implementation | Module |
|---------|---------------|--------|
| **Lattice Operations** | E8/Leech classes | `lattice/` |
| **Family Pattern** | Manager/Registry | `unified_families/` |
| **Deliberation** | Multi-perspective | `thinktank/` |

---

## 🔄 Navigation Reference

**Back to:** [README.md](README.md) | [NAVIGATION.md](NAVIGATION.md)  
**Up to:** [CMPLX-1T AGENTS.md](../AGENTS.md) | [CMPLX-1T NAVIGATION.md](../NAVIGATION.md)
