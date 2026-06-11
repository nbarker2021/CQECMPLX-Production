#!/usr/bin/env python3
"""
Unit tests for physics engines
"""
import pytest
import numpy as np
import math
from meta_material_system.physics_engines import (
    Rule30Lattice, LCR,
    SKAction,
    Octonion, oloid_winding_full, cayley_dickson_oloid_normal_form,
    MandelbrotBoundary,
    E8Lattice,
    VOAMooshine,
    RecursiveMaterialEngine,
    validate_full_map,
)

class TestRule30Lattice:
    """Tests for Rule 30 causal lattice"""
    
    def test_basic_evolution(self):
        lattice = Rule30Lattice(width=65)
        history = lattice.evolve_full(5)
        assert history.shape == (6, 65)
        assert history[0, 32] == 1  # seed at center
    
    def test_center_column(self):
        lattice = Rule30Lattice(width=65)
        center = lattice.center_column(10)
        assert len(center) == 11
        assert center[0] == 1  # initial seed
    
    def test_lcr_next_C(self):
        state = LCR(1, 0, 1)
        # Rule 30: 101 -> 1 (L=1, C=0, R=1) -> binary 101 = 5 -> RULE30[5] = 1
        # Wait: RULE30[5] = 0 (index 5 = binary 101 = 5)
        # Let's check: 111->0, 110->0, 101->0, 100->1, 011->1, 010->1, 001->1, 000->0
        # 101 is index 5, value = 0
        assert state.next_C() == 0
    
    def test_lcr_gamma(self):
        state = LCR(1, 0, 1)
        assert state.gamma() == 0


class TestSKAction:
    """Tests for SK-combinator action"""
    
    def setup_method(self):
        self.sk = SKAction()
    
    def test_stream_entropy(self):
        # Uniform stream -> max entropy
        bits = np.array([0, 1, 0, 1, 0, 1])
        assert self.sk._stream_entropy(bits) == 1.0
        
        # Uniform all 0 -> min entropy (should return 1.0 for max structure)
        bits = np.zeros(10)
        assert self.sk._stream_entropy(bits) == 1.0
        
        # Bias
        bits = np.array([1, 1, 1, 0])
        entropy = self.sk._stream_entropy(bits)
        assert 0 < entropy < 1.0
    
    def test_readout_action(self):
        rule30_center = np.array([1]*512 + [0]*512)  # biased
        mandelbrot_bits = [[0,1,0,1]*256 for _ in range(4)]
        voa_matches = [{"match": True} for _ in range(5)]
        e8_reduction = 10.0
        
        action = self.sk.readout_action(
            rule30_center=np.array(rule30_center),
            mandelbrot_bits=mandelbrot_bits,
            voa_matches=[{"match": True}]*5,
            e8_reduction=10.0,
            gluon_mass_1=1.0,
            gluon_mass_2=1.0,
            depth=1024
        )
        assert action > 0


class TestOctonion:
    """Tests for octonion algebra"""
    
    def test_multiplication(self):
        a = Octonion(np.array([1,0,0,0,0,0,0,0]))
        b = Octonion(np.array([1,0,0,0,0,0,0,0]))
        c = a * b
        assert abs(c.norm_sq() - 1.0) < 1e-10
    
    def test_norm(self):
        oct = Octonion(np.array([3,4,0,0,0,0,0,0]))
        assert abs(oct.norm() - 5.0) < 1e-10
    
    def test_conjugation(self):
        oct = Octonion(np.array([3,1,2,3,4,5,6,7]))
        conj = oct.conj()
        assert conj.v[0] == 3
        assert conj.v[1] == -1
    
    def test_unit(self):
        oct = Octonion(np.array([3,4,0,0,0,0,0,0]))
        unit = oct.unit()
        assert abs(unit.norm() - 1.0) < 1e-10


class TestOloid:
    """Tests for oloid geometry"""
    
    def test_winding(self):
        oct = Octonion(np.array([1,0,0,0,0,0,0,0]))
        result = oloid_winding_full(oct, steps=100)
        
        assert result["winding_number"] == 1
        assert "unit_octonion" in result
        assert "trajectory" in result
    
    def test_closure(self):
        oct = Octonion(np.array([1,0,0,0,0,0,0,0]))
        result = cayley_dickson_oloid_normal_form(oct)
        assert result["closure"] is True


class TestMandelbrotBoundary:
    """Tests for Mandelbrot boundary scalar"""
    
    def setup_method(self):
        self.mandelbrot = MandelbrotBoundary()
    
    def test_boundary_scalar_at_depth(self):
        result = self.mandelbrot.boundary_scalar_at_depth(256)
        
        assert result["depth"] == 256
        assert result["light_settings"] == 4
        assert "predictions" in result
        assert len(result["predictions"]) == 4
        # The 4 light settings generate distinct but valid prediction sequences
        assert all(len(p) == 256 for p in result["predictions"])



class TestE8Lattice:
    """Tests for E8 root lattice"""
    
    def setup_method(self):
        self.e8 = E8Lattice()
    
    def test_roots_count(self):
        assert len(self.e8.roots) == 240
    
    def test_root_norms(self):
        for root in self.e8.roots[:10]:
            norm_sq = np.sum(root**2)
            assert abs(norm_sq - 2.0) < 1e-10
    
    def test_mass_reduction(self):
        base = 1.0
        reduced = self.e8.mass_reduction(base, layers=2)
        assert reduced < base
        assert reduced > 0


class TestVOAMooshine:
    """Tests for VOA/Moonshine"""
    
    def setup_method(self):
        self.voa = VOAMooshine()
    
    def test_verify_character(self):
        result = self.voa.verify_character(10)
        assert result["honesty"] == "CONJ"
        assert "matches" in result
        assert result["best_hypothesis"] == "k=firing_count"


class TestRecursiveMaterialEngine:
    """Integration tests for full engine"""
    
    def setup_method(self):
        self.engine = RecursiveMaterialEngine()
    
    def test_compute_formation_energy_graphene_hbn(self):
        gr = {"gluon_mass": 0.98, "formation_energy": 0.0, "lattice_constants": {"a": 2.461}}
        hbn = {"gluon_mass": 0.87, "formation_energy": -0.5, "lattice_constants": {"a": 2.504}}
        
        result = self.engine.compute_formation_energy(gr, hbn, depth=256, layers=2)
        
        assert "formation_energy" in result
        assert "components" in result
        assert "full_trace" in result
        assert 0 < result["formation_energy"] < 200  # reasonable range
    
    def test_all_material_pairs(self):
        gr = {"gluon_mass": 0.98, "formation_energy": 0.0, "lattice_constants": {"a": 2.461}}
        hbn = {"gluon_mass": 0.87, "formation_energy": -0.5, "lattice_constants": {"a": 2.504}}
        mos2 = {"gluon_mass": 1.02, "formation_energy": -1.2, "lattice_constants": {"a": 3.16}}
        ws2 = {"gluon_mass": 1.05, "formation_energy": -1.3, "lattice_constants": {"a": 3.15}}
        
        pairs = [("Gr/hBN", gr, hbn), ("MoS2/WS2", mos2, ws2)]
        
        for name, base, partner in pairs:
            result = self.engine.compute_formation_energy(base, partner, depth=128, layers=2)
            assert result["formation_energy"] > 0
            assert "sk_action" in result["components"]


class TestMaterialValidation:
    """Tests for material validation"""
    
    def test_valid_material(self):
        from meta_material_system.material_db import MaterialProperties
        from meta_material_system.meta_material_designer import validate_material_properties
        
        mat = MaterialProperties(
            name="Test", formula="XY", density=2.5, youngs_modulus=100,
            tensile_strength=100, thermal_conductivity=50, band_gap=1.0,
            crystal_structure="Hex", lattice_constants={"a": 3.0},
            space_group="Test", poisson_ratio=0.25, hardness=5.0,
            melting_point=1500, thermal_expansion=5e-6,
            electrical_conductivity=1000, gluon_mass=1.0,
            formation_energy=-1.0, oloid_closure=True, production_key="test"
        )
        # Should not raise
        validate_material_properties(mat)
    
    def test_invalid_material(self):
        from meta_material_system.material_db import MaterialProperties
        from meta_material_system.meta_material_designer import validate_material_properties, ValidationError
        
        mat = MaterialProperties(
            name="Bad", formula="X", density=-1.0, youngs_modulus=100,
            tensile_strength=100, thermal_conductivity=50, band_gap=1.0,
            crystal_structure="Hex", lattice_constants={"a": 3.0},
            space_group="Test", poisson_ratio=0.25, hardness=5.0,
            melting_point=1500, thermal_expansion=5e-6,
            electrical_conductivity=1000, gluon_mass=1.0,
            formation_energy=-1.0, oloid_closure=True, production_key="test"
        )
        with pytest.raises(ValidationError):
            validate_material_properties(mat)


class TestPipelineIntegration:
    """Integration tests for full pipeline"""
    
    def test_material_database(self):
        from meta_material_system.material_db import list_materials, get_material
        
        mats = list_materials()
        assert len(mats) >= 23  # at least 23 materials
        assert "Graphene" in mats
        assert "Hexagonal Boron Nitride" in mats
        
        gr = get_material("graphene")
        assert gr is not None
        assert gr.name == "Graphene"
        assert gr.gluon_mass == 0.98
    
    def test_pareto_partnering(self):
        from meta_material_system.pareto_partnering import find_pareto_partners
        from meta_material_system.material_db import get_material, list_materials
        
        base = get_material("graphene")
        all_mats = [get_material(k) for k in list_materials()]
        partners = find_pareto_partners(base, all_mats)
        
        assert len(partners) >= 5
        assert partners[0].material_b.name == "Hexagonal Boron Nitride"
        assert partners[0].pareto_score > 0.8


if __name__ == "__main__":
    pytest.main([__file__, "-v"])