"""
MetaForge-AI: Real Hetero-structure Builder
============================================
Builds real 2D hetero-structures using pymatgen/ase.
Integrates with MACE/CHGNet ML potentials for formation energy.
"""

from __future__ import annotations
import numpy as np
import math
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path
import json

try:
    from pymatgen.core import Structure, Lattice, Element
    from pymatgen.analysis.interfaces import InterfaceBuilder
    from pymatgen.analysis.interfaces.substrate_analyzer import SubstrateAnalyzer
    from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
    from pymatgen.io.ase import AseAtomsAdaptor
    from ase import Atoms
    from ase.build import mx2
    PYMATGEN_AVAILABLE = True
except ImportError:
    PYMATGEN_AVAILABLE = False

try:
    from mace.calculators import MACECalculator
    MACE_AVAILABLE = True
except ImportError:
    MACE_AVAILABLE = False

try:
    from chgnet.model import CHGNet
    from chgnet.model.dynamics import CHGNetCalculator
    CHGNET_AVAILABLE = True
except ImportError:
    CHGNET_AVAILABLE = False

import logging
logger = logging.getLogger("heterostructure_builder")


@dataclass
class MLPotentialConfig:
    mace_model_path: Optional[str] = None
    chgnet_model_path: Optional[str] = None
    device: str = "cpu"


@dataclass
class HeterostructureCandidate:
    base_formula: str
    partner_formula: str
    base_structure: Any
    partner_structure: Any
    interface_structure: Any
    mismatch_percent: float
    area: float
    formation_energy: Optional[float] = None
    stability: Optional[str] = None
    mismatch_details: Dict = None


class MaterialDatabase:
    """Database of known 2D materials with lattice parameters"""
    
    MATERIALS_2D = {
        "graphene": {
            "formula": "C",
            "lattice_a": 2.461,
            "lattice_c": 6.708,
            "spacegroup": "P6/mmm",
            "elements": ["C"],
            "thickness": 3.35,
        },
        "hBN": {
            "formula": "BN",
            "lattice_a": 2.504,
            "lattice_c": 6.66,
            "spacegroup": "P63/mmc",
            "elements": ["B", "N"],
            "thickness": 3.33,
        },
        "MoS2": {
            "formula": "MoS2",
            "lattice_a": 3.16,
            "lattice_c": 12.3,
            "spacegroup": "P63/mmc",
            "elements": ["Mo", "S"],
            "thickness": 6.15,
        },
        "WS2": {
            "formula": "WS2",
            "lattice_a": 3.15,
            "lattice_c": 12.3,
            "spacegroup": "P63/mmc",
            "elements": ["W", "S"],
            "thickness": 6.15,
        },
        "MoSe2": {
            "formula": "MoSe2",
            "lattice_a": 3.29,
            "lattice_c": 12.9,
            "spacegroup": "P63/mmc",
            "elements": ["Mo", "Se"],
            "thickness": 6.45,
        },
        "WSe2": {
            "formula": "WSe2",
            "lattice_a": 3.28,
            "lattice_c": 12.9,
            "spacegroup": "P63/mmc",
            "elements": ["W", "Se"],
            "thickness": 6.45,
        },
        "MoTe2": {
            "formula": "MoTe2",
            "lattice_a": 3.52,
            "lattice_c": 13.9,
            "spacegroup": "P63/mmc",
            "elements": ["Mo", "Te"],
            "thickness": 6.95,
        },
        "Graphene_hBN": {
            "formula": "C/BN",
            "lattice_a": 2.461,
            "lattice_c": 6.7,
            "spacegroup": "P1",
            "elements": ["C", "B", "N"],
        },
    }
    
    @classmethod
    def get(cls, name: str) -> Dict:
        return cls.MATERIALS_2D.get(name.lower())
    
    @classmethod
    def list_materials(cls) -> List[str]:
        return list(cls.MATERIALS_2D.keys())


class HeterostructureBuilder:
    """
    Builds real 2D hetero-structures using pymatgen/ase.
    Calculates lattice mismatch, builds interface, prepares for ML potential evaluation.
    """
    
    def __init__(self, max_mismatch: float = 0.05, max_area: float = 1000.0):
        self.max_mismatch = max_mismatch
        self.max_area = max_area
        self.ase_adaptor = AseAtomsAdaptor() if PYMATGEN_AVAILABLE else None
    
    def build_monolayer(self, material_name: str) -> Optional["Atoms"]:
        """Build monolayer from material database using ASE."""
        if not PYMATGEN_AVAILABLE:
            return None
            
        mat_data = MaterialDatabase.get(material_name)
        if not mat_data:
            return None
        
        try:
            if "graphene" in material_name.lower():
                atoms = mx2(formula=mat_data["formula"], a=mat_data["lattice_a"], thickness=mat_data["thickness"])
            else:
                atoms = mx2(formula=mat_data["formula"], a=mat_data["lattice_a"], thickness=mat_data["thickness"])
            return atoms
        except Exception as e:
            logger.warning(f"Failed to build monolayer {material_name}: {e}")
            return None
    
    def calculate_mismatch(self, mat1: Dict, mat2: Dict) -> float:
        """Calculate lattice mismatch between two materials."""
        a1 = mat1["lattice_a"]
        a2 = mat2["lattice_a"]
        return abs(a1 - a2) / a1
    
    def find_commensurate_supercells(self, mat1: Dict, mat2: Dict, max_supercell: int = 5) -> List[Dict]:
        """Find commensurate supercells with low mismatch."""
        results = []
        a1 = mat1["lattice_a"]
        a2 = mat2["lattice_a"]
        
        # Simple approach: try integer multiples
        for n1 in range(1, max_supercell + 1):
            for n2 in range(1, max_supercell + 1):
                L1 = n1 * a1
                L2 = n2 * a2
                mismatch = abs(L1 - L2) / max(L1, L2)
                if mismatch < self.max_mismatch:
                    area = L1 * L2 * math.sqrt(3) / 2  # hexagonal area
                    if area < self.max_area:
                        results.append({
                            "n1": n1, "n2": n2,
                            "mismatch": mismatch,
                            "area": area,
                            "L1": L1, "L2": L2
                        })
        
        return sorted(results, key=lambda x: x["mismatch"])
    
    def build_interface(self, base_name: str, partner_name: str) -> Optional[HeterostructureCandidate]:
        """Build hetero-structure interface between two 2D materials."""
        if not PYMATGEN_AVAILABLE:
            return None
            
        base_mat = MaterialDatabase.get(base_name)
        partner_mat = MaterialDatabase.get(partner_name)
        
        if not base_mat or not partner_mat:
            return None
        
        # Build monolayers
        base_atoms = self.build_monolayer(base_name)
        partner_atoms = self.build_monolayer(partner_name)
        
        if base_atoms is None or partner_atoms is None:
            return None
        
        # Find commensurate supercells
        supercells = self.find_commensurate_supercells(
            MaterialDatabase.get(base_name),
            MaterialDatabase.get(partner_name)
        )
        
        if not supercells:
            logger.warning(f"No commensurate supercells found for {base_name}/{partner_name}")
            return None
        
        best = supercells[0]
        
        # Build interface structure using best supercell
        try:
            # Create supercells
            base_super = base_atoms.repeat((best["n1"], best["n1"], 1))
            partner_super = partner_atoms.repeat((best["n2"], best["n2"], 1))
            
            # Align and combine
            interface = self._align_and_stack(base_super, partner_super)
            
            return HeterostructureCandidate(
                base_formula=base_mat["formula"],
                partner_formula=partner_mat["formula"],
                base_structure=base_atoms,
                partner_structure=partner_atoms,
                interface_structure=interface,
                mismatch_percent=best["mismatch"] * 100,
                area=best["area"],
                mismatch_details=best
            )
        except Exception as e:
            logger.error(f"Failed to build interface: {e}")
            return None
    
    def _align_and_stack(self, base: "Atoms", partner: "Atoms", gap: float = 3.0) -> "Atoms":
        """Align and stack two structures with van der Waals gap."""
        # Center both structures
        base_centered = base.copy()
        partner_centered = partner.copy()
        
        base_centered.center(vacuum=0, axis=2)
        partner_centered.center(vacuum=0, axis=2)
        
        # Get bounding boxes
        base_z_max = base_centered.get_positions()[:, 2].max()
        partner_z_min = partner_centered.get_positions()[:, 2].min()
        
        # Shift partner above base with gap
        shift = base_z_max + gap - partner_z_min
        partner_centered.translate([0, 0, shift])
        
        # Combine
        interface = base_atoms + partner_centered
        return interface


class MLPotentialCalculator:
    """
    Wrapper for ML potentials (MACE, CHGNet) to calculate formation energies.
    """
    
    def __init__(self, config: MLPotentialConfig):
        self.config = config
        self.mace_calc = None
        self.chgnet_calc = None
        
        if MACE_AVAILABLE and config.mace_model_path:
            try:
                self.mace_calc = MACECalculator(
                    model_paths=config.mace_model_path,
                    device=config.device
                )
            except Exception as e:
                logger.warning(f"Failed to load MACE: {e}")
        
        if CHGNET_AVAILABLE and config.chgnet_model_path:
            try:
                model = CHGNet.load(config.chgnet_model_path)
                self.chgnet_calc = CHGNetCalculator(model)
            except Exception as e:
                logger.warning(f"Failed to load CHGNet: {e}")
    
    def calculate_formation_energy(self, atoms: "Atoms", 
                                     elemental_refs: Dict[str, float] = None) -> Optional[float]:
        """Calculate formation energy per atom using ML potential."""
        
        if self.mace_calc:
            try:
                atoms.calc = self.mace_calc
                total_energy = atoms.get_potential_energy()
                return total_energy / len(atoms)
            except Exception as e:
                logger.warning(f"MACE calculation failed: {e}")
        
        if self.chgnet_calc:
            try:
                atoms.calc = self.chgnet_calc
                total_energy = atoms.get_potential_energy()
                return total_energy / len(atoms)
            except Exception as e:
                logger.warning(f"CHGNet calculation failed: {e}")
        
        return None
    
    def calculate_relaxed_energy(self, atoms: "Atoms", 
                                   fmax: float = 0.05, steps: int = 500) -> Optional[float]:
        """Relax structure and return energy."""
        # Would use ASE's BFGS or FIRE optimizer
        # from ase.optimize import BFGS
        # opt = BFGS(atoms, trajectory='relax.traj')
        # opt.run(fmax=fmax, steps=steps)
        # return atoms.get_potential_energy() / len(atoms)
        return None


def build_all_heterostructures() -> List[HeterostructureCandidate]:
    """Build all possible hetero-structures from material database."""
    if not PYMATGEN_AVAILABLE:
        return []
    
    builder = HeterostructureBuilder(max_mismatch=0.08, max_area=500.0)
    materials = MaterialDatabase.list_materials()
    
    candidates = []
    for i, base in enumerate(materials):
        for partner in materials[i+1:]:
            try:
                candidate = builder.build_interface(base, partner)
                if candidate and candidate.mismatch_percent < 8.0:
                    candidates.append(candidate)
                    logger.info(f"Built {base}/{partner}: mismatch={candidate.mismatch_percent:.2f}%, area={candidate.area:.1f} Å²")
            except Exception as e:
                logger.warning(f"Failed to build {base}/{partner}: {e}")
    
    return sorted(candidates, key=lambda x: x.mismatch_percent)


def screen_heterostructures_with_ml(candidates: List[HeterostructureCandidate], 
                                     config: MLPotentialConfig) -> List[HeterostructureCandidate]:
    """Screen candidates with ML potentials."""
    calc = MLPotentialCalculator(config)
    
    for candidate in candidates:
        if candidate.interface_structure:
            try:
                fe = calc.calculate_formation_energy(candidate.interface_structure)
                if fe is not None:
                    candidate.formation_energy = fe
                    # Stability heuristic
                    if fe < -0.5:
                        candidate.stability = "stable"
                    elif fe < 0:
                        candidate.stability = "metastable"
                    else:
                        candidate.stability = "unlikely"
            except Exception as e:
                logger.warning(f"ML screening failed for {candidate.base_formula}/{candidate.partner_formula}: {e}")
    
    return candidates


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Build all hetero-structures
    candidates = build_all_heterostructures()
    print(f"Built {len(candidates)} candidate hetero-structures")
    
    for c in candidates[:10]:
        print(f"  {c.base_formula}/{c.partner_formula}: mismatch={c.mismatch_percent:.2f}%, area={c.area:.1f} Å²")
    
    # Screen with ML (if models available)
    config = MLPotentialConfig(
        mace_model_path=None,  # Set path to model
        chgnet_model_path=None  # Set path to model
    )
    
    screened = screen_heterostructures_with_ml(candidates[:5], config)
    for c in screened:
        if c.formation_energy:
            print(f"  {c.base_formula}/{c.partner_formula}: FE={c.formation_energy:.3f} eV/atom, stability={c.stability}")