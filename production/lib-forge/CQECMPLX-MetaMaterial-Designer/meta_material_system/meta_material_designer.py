#!/usr/bin/env python3
"""
MetaMaterial Design System - Main CLI Program
=============================================

A comprehensive metamaterial design system that:
1. Accepts a base material from user (database, file, or web)
2. Finds Pareto-optimal partner materials
3. Runs 10-fold recursive evaluation with error forms
4. Identifies seam/interlayer materials
5. Computes production energy and requirements
6. GENERATES PUBLICATION-QUALITY VISUALIZATIONS (standard output)

Usage:
    python meta_material_designer.py
    python meta_material_designer.py --material graphene
    python meta_material_designer.py --material-file custom_material.json
"""

import sys
import json
import argparse
import hashlib
import pickle
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

# Import our modules
from material_db import (
    MaterialProperties, 
    get_material, 
    list_materials, 
    MATERIAL_DATABASE,
    add_custom_material
)
from pareto_partnering import find_pareto_partners, print_pareto_results, ParetoPartner
from fold_evaluation import run_10_fold_evaluation, print_fold_sequence, FoldSequence
from seam_detection import detect_seam_candidates, print_seam_analysis, SeamCandidate
from production_energy import generate_production_plan, print_production_plan, ProductionPlan
from visualizers import (
    generate_all_visualizations,
    VisualizationOutput,
    render_visualizations_streamlit
)
from waste_explorer import calculate_flux_summary, render_flux_streamlit


# ─── Logging Configuration ───
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("meta_material_designer")


# ─── Custom Exceptions ───
class MaterialError(Exception):
    """Base exception for material-related errors"""
    pass

class MaterialNotFoundError(MaterialError):
    """Raised when material cannot be found"""
    pass

class MaterialValidationError(MaterialError):
    """Raised when material properties are invalid"""
    pass

class PipelineError(Exception):
    """Raised when pipeline step fails"""
    pass

class ValidationError(Exception):
    """Raised when validation fails"""
    pass


# ─── Validation Functions ───
def validate_material_properties(props: MaterialProperties) -> None:
    """Validate material properties are physically reasonable"""
    errors = []
    
    if props.density <= 0:
        errors.append("density must be positive")
    if props.youngs_modulus < 0:
        errors.append("youngs_modulus cannot be negative")
    if props.tensile_strength < 0:
        errors.append("tensile_strength cannot be negative")
    if props.thermal_conductivity < 0:
        errors.append("thermal_conductivity cannot be negative")
    if props.band_gap < 0:
        errors.append("band_gap cannot be negative")
    if props.hardness < 0:
        errors.append("hardness cannot be negative")
    if props.melting_point <= 0:
        errors.append("melting_point must be positive")
    if props.gluon_mass <= 0:
        errors.append("gluon_mass must be positive")
    if props.formation_energy > 100:  # arbitrary sanity check
        errors.append("formation_energy seems unreasonably high")
    if not (0 <= props.poisson_ratio <= 0.5):
        errors.append("poisson_ratio must be between 0 and 0.5")
    if props.thermal_expansion < -1e-4 or props.thermal_expansion > 1e-3:
        errors.append("thermal_expansion out of reasonable range")
    if not props.lattice_constants or 'a' not in props.lattice_constants:
        errors.append("lattice_constants must contain 'a'")
    if props.lattice_constants.get('a', 0) <= 0:
        errors.append("lattice constant 'a' must be positive")
    if props.space_group == "":
        errors.append("space_group cannot be empty")
    
    if errors:
        raise ValidationError(f"Material validation failed: {'; '.join(errors)}")


def validate_pipeline_state(designer: 'MetaMaterialDesigner', step: str) -> None:
    """Validate pipeline state at each step"""
    if step >= "base" and designer.base_material is None:
        raise PipelineError("Base material not selected")
    if step >= "partner" and designer.partner is None:
        raise PipelineError("Partner material not selected")
    if step >= "fold" and designer.fold_sequence is None:
        raise PipelineError("Fold sequence not computed")
    if step >= "seam" and not designer.seam_candidates:
        raise PipelineError("Seam candidates not computed")
    if step >= "production" and designer.production_plan is None:
        raise PipelineError("Production plan not generated")


# ─── Material Loading with Validation ───
def load_material_safe(source: str) -> MaterialProperties:
    """Load material with full validation"""
    mat = get_material(source)
    if mat:
        logger.info(f"Found in database: {mat.name}")
        validate_material_properties(mat)
        return mat
    
    path = Path(source)
    if path.exists():
        logger.info(f"Loading from file: {path}")
        return load_from_file_safe(path)
    
    raise MaterialNotFoundError(
        f"Could not find material: {source}. Available: {', '.join(list_materials())}"
    )


def load_from_file_safe(path: Path) -> MaterialProperties:
    """Load material from JSON file with validation"""
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise MaterialError(f"Invalid JSON in {path}: {e}")
    except Exception as e:
        raise MaterialError(f"Error reading {path}: {e}")
    
    # Validate required fields
    required_fields = {
        'name', 'formula', 'density', 'youngs_modulus', 'tensile_strength',
        'thermal_conductivity', 'band_gap', 'crystal_structure',
        'lattice_constants', 'space_group', 'poisson_ratio', 'hardness',
        'melting_point', 'thermal_expansion', 'electrical_conductivity',
        'gluon_mass', 'formation_energy', 'oloid_closure', 'production_key'
    }
    
    missing = required_fields - set(data.keys())
    if missing:
        raise ValidationError(f"Missing required fields: {missing}")
    
    # Create and validate
    try:
        mat = MaterialProperties(**data)
        validate_material_properties(mat)
        logger.info(f"Loaded custom material: {mat.name}")
        return mat
    except TypeError as e:
        raise ValidationError(f"Invalid material properties: {e}")


def safe_load_material(designer: 'MetaMaterialDesigner', source: str) -> MaterialProperties:
    """Wrapper that catches and logs all material loading errors"""
    try:
        mat = load_material_safe(source)
        return mat
    except (MaterialNotFoundError, ValidationError, MaterialError) as e:
        logger.error(f"Material loading failed: {e}")
        raise


@dataclass
class MetaMaterialDesigner:
    """Main orchestrator for the metamaterial design pipeline"""
    
    base_material: Optional[MaterialProperties] = None
    partner: Optional[MaterialProperties] = None
    pareto_partners: List[ParetoPartner] = None
    fold_sequence: Optional[FoldSequence] = None
    seam_candidates: List[SeamCandidate] = None
    production_plan: Optional[ProductionPlan] = None
    visualizations: Optional[VisualizationOutput] = None
    flux_summary: Optional[Dict] = None
    
    def __post_init__(self):
        self.pareto_partners = self.pareto_partners or []
        self.seam_candidates = self.seam_candidates or []
        
        # Visualization cache for instant lookup
        self.cache_dir = Path("viz_cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def load_material(self, source: str) -> MaterialProperties:
        """Load material with full validation"""
        return safe_load_material(self, source)
    
    def select_base_material(self, material_name: Optional[str] = None) -> bool:
        """Select base material with validation"""
        try:
            if material_name:
                self.base_material = self.load_material(material_name)
                logger.info(f"Base material selected: {self.base_material.name}")
                return True
            
            # Interactive selection
            print("\n" + "="*60)
            print("META-MATERIAL DESIGN SYSTEM")
            print("="*60)
            print("\nAvailable base materials in database:")
            mats = list_materials()
            for i, name in enumerate(mats, 1):
                mat = get_material(name)
                print(f"  {i}. {mat.name} ({mat.formula}) - Gluon: {mat.gluon_mass:.2f}, Energy: {mat.formation_energy:.2f} eV")
            
            print(f"  {len(mats)+1}. Load from file")
            print(f"  {len(mats)+2}. Create new material template")
            
            while True:
                try:
                    choice = input(f"\nSelect material (1-{len(mats)+2}): ").strip()
                    
                    if choice.isdigit():
                        idx = int(choice) - 1
                        if 0 <= idx < len(mats):
                            self.base_material = get_material(mats[idx])
                            print(f"✓ Selected: {self.base_material.name}")
                            return True
                        elif idx == len(mats):
                            filepath = input("Enter path to JSON file: ").strip()
                            self.base_material = self.load_material(filepath)
                            return self.base_material is not None
                        elif idx == len(mats) + 1:
                            template_path = input("Template path [material_template.json]: ").strip() or "material_template.json"
                            self.save_material_template(template_path)
                            continue
                    
                    # Try as name
                    self.base_material = self.load_material(choice)
                    return True
                    
                except KeyboardInterrupt:
                    print("\nCancelled")
                    return False
                except (MaterialError, ValidationError) as e:
                    logger.error(f"Selection failed: {e}")
                    
        except (MaterialError, ValidationError) as e:
            logger.error(f"Base material selection failed: {e}")
            return False
    
    def find_partners(self, top_n: int = 5) -> List[ParetoPartner]:
        """Find Pareto-optimal partners"""
        print(f"\n🔬 Finding Pareto partners for {self.base_material.name}...")
        
        all_materials = [get_material(k) for k in list_materials()]
        self.pareto_partners = find_pareto_partners(self.base_material, all_materials)
        
        print_pareto_results(self.pareto_partners, top_n)
        return self.pareto_partners
    
    def select_partner(self, partner_idx: Optional[int] = None) -> bool:
        """Select partner material"""
        
        if partner_idx is not None and 0 <= partner_idx < len(self.pareto_partners):
            self.partner = self.pareto_partners[partner_idx].material_b
            print(f"✓ Auto-selected partner: {self.partner.name}")
            return True
        
        if not self.pareto_partners:
            print("No partners found!")
            return False
        
        print(f"\nSelect partner (1-{min(10, len(self.pareto_partners))}) or enter custom name:")
        for i, p in enumerate(self.pareto_partners[:10]):
            print(f"  {i+1}. {p.material_b.name} - Pareto: {p.pareto_score:.3f}")
        
        while True:
            try:
                choice = input("Choice: ").strip()
                
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(self.pareto_partners):
                        self.partner = self.pareto_partners[idx].material_b
                        print(f"✓ Selected: {self.partner.name}")
                        return True
                
                # Try as name
                self.partner = self.load_material(choice)
                if self.partner:
                    return True
                    
            except KeyboardInterrupt:
                return False
    
    def run_fold_evaluation(self) -> FoldSequence:
        """Run 10-fold recursive evaluation"""
        print(f"\n🔄 Running 10-fold recursive evaluation...")
        print(f"   Base: {self.base_material.name} + Partner: {self.partner.name}")
        
        self.fold_sequence = run_10_fold_evaluation(self.base_material, self.partner)
        print_fold_sequence(self.fold_sequence)
        
        return self.fold_sequence
    
    def find_seams(self) -> List[SeamCandidate]:
        """Detect seam material candidates"""
        print(f"\n🔍 Analyzing seam material requirements...")
        
        self.seam_candidates = detect_seam_candidates(
            self.base_material, 
            self.partner, 
            self.fold_sequence
        )
        
        print_seam_analysis(self.seam_candidates, self.base_material, self.partner, self.fold_sequence)
        
        return self.seam_candidates
    
    def generate_production(self, area_cm2: float = 1.0) -> ProductionPlan:
        """Generate production plan"""
        print(f"\n🏭 Generating production plan for {area_cm2} cm²...")
        
        self.production_plan = generate_production_plan(
            self.base_material,
            self.partner,
            self.fold_sequence,
            self.seam_candidates,
            area_cm2
        )
        
        print_production_plan(self.production_plan)
        
        return self.production_plan

    def save_report(self, path: str = "metamaterial_report.json") -> str:
        """Save complete report to JSON"""
        report = {
            "base_material": self.base_material.__dict__ if self.base_material else None,
            "partner_material": self.partner.__dict__ if self.partner else None,
            "pareto_partners": [
                {
                    "material": p.material_b.name,
                    "pareto_score": p.pareto_score,
                    "lattice_match": p.lattice_match,
                    "property_synergy": p.property_synergy,
                    "gluon_coherence": p.gluon_coherence,
                    "oloid_compatibility": p.oloid_compatibility,
                    "interface_energy": p.interface_energy,
                    "strain_tolerance": p.strain_tolerance
                }
                for p in self.pareto_partners[:5]
            ],
            "fold_sequence": {
                "final_tensile": self.fold_sequence.final_tensile,
                "final_composite": self.fold_sequence.final_composite,
                "final_gluon_mass": self.fold_sequence.final_gluon_mass,
                "total_formation_energy": self.fold_sequence.total_formation_energy,
                "error_wall_summary": {k.value: v for k, v in self.fold_sequence.error_wall_summary.items()},
                "seam_candidates": self.fold_sequence.seam_candidates,
                "folds": [
                    {
                        "fold": f.fold_number,
                        "context": f.applied_context,
                        "gluon_mass": f.gluon_mass,
                        "tensile": f.tensile_strength,
                        "composite": f.composite_strength,
                        "formation_energy": f.formation_energy,
                        "error_walls": [w.wall_type.value for w in f.error_walls],
                        "oloid_closure": f.oloid_closure
                    }
                    for f in self.fold_sequence.folds
                ]
            } if self.fold_sequence else None,
            "seam_materials": [
                {
                    "material": s.material.name,
                    "role": s.role,
                    "placement": s.placement,
                    "effectiveness": s.effectiveness,
                    "reason": s.reason,
                    "thickness_nm": s.required_thickness
                }
                for s in self.seam_candidates
            ],
            "production_plan": {
                "total_energy_joules_per_cm2": self.production_plan.total_energy_joules_per_cm2,
                "total_time_hours": self.production_plan.total_time_hours,
                "max_temperature_K": self.production_plan.max_temperature_K,
                "max_pressure_atm": self.production_plan.max_pressure_atm,
                "estimated_cost_usd_per_cm2": self.production_plan.estimated_cost_usd_per_cm2,
                "scalability_score": self.production_plan.scalability_score,
                "steps": [
                    {
                        "name": s.name,
                        "energy_per_cm2": s.energy_per_cm2,
                        "time_hours": s.time_seconds / 3600,
                        "temperature_K": s.temperature_K,
                        "pressure_atm": s.pressure_atm,
                        "yield_rate": s.yield_rate,
                        "equipment": s.equipment
                    }
                    for s in self.production_plan.steps
                ]
            } if self.production_plan else None,
            "notes": self.production_plan.notes if self.production_plan else [],
            "flux_summary": self.flux_summary if self.flux_summary else None
        }
        
        with open(path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n📄 Full report saved to {path}")
        return path

    def generate_visualizations(self, theta_deg: float = 1.1) -> VisualizationOutput:
        """Generate all visualizations as standard pipeline output."""
        # Prepare data for visualizers
        base_props = self.base_material.__dict__ if self.base_material else {}
        partner_props = self.partner.__dict__ if self.partner else None
        
        pareto_results = []
        if self.pareto_partners:
            for p in self.pareto_partners[:5]:
                pareto_results.append({
                    'material': p.material_b.name,
                    'pareto_score': p.pareto_score,
                    'lattice_match': p.lattice_match,
                    'property_synergy': p.property_synergy,
                    'gluon_coherence': p.gluon_coherence,
                    'oloid_compatibility': p.oloid_compatibility,
                    'interface_energy': p.interface_energy,
                    'strain_tolerance': p.strain_tolerance,
                })
        
        fold_seq = None
        if self.fold_sequence:
            fold_seq = {
                'folds': [
                    {
                        'fold': f.fold_number,
                        'applied_context': f.applied_context,
                        'gluon_mass': f.gluon_mass,
                        'tensile_strength': f.tensile_strength,
                        'composite_strength': f.composite_strength,
                        'formation_energy': f.formation_energy,
                        'error_walls': {ew.wall_type.value: 1 for ew in f.error_walls},
                        'oloid_closure': f.oloid_closure
                    }
                    for f in self.fold_sequence.folds
                ]
            }
        
        seam_cands = []
        if self.seam_candidates:
            for s in self.seam_candidates:
                seam_cands.append({
                    'material': s.material.name,
                    'role': s.role,
                    'placement': s.placement,
                    'effectiveness': s.effectiveness,
                    'reason': s.reason,
                    'thickness_nm': s.required_thickness,
                })
        
        prod_plan = None
        if self.production_plan:
            prod_plan = {
                'steps': [
                    {
                        'name': s.name,
                        'energy_per_cm2': s.energy_per_cm2,
                        'time_hours': s.time_seconds / 3600,
                        'temperature_K': s.temperature_K,
                        'pressure_atm': s.pressure_atm,
                        'yield_rate': s.yield_rate,
                        'equipment': s.equipment
                    }
                    for s in self.production_plan.steps
                ]
            }
        
        # Generate cache key for instant lookup
        cache_key = self._get_cache_key()
        cache_file = self.cache_dir / f"{cache_key}.pkl"
        
        # Check cache first
        if cache_file.exists():
            try:
                with open(cache_file, 'rb') as f:
                    self.visualizations = pickle.load(f)
                print(f"✓ Loaded visualizations from cache: {cache_key}")
                return self.visualizations
            except Exception:
                pass  # Regenerate if cache corrupt
        
        # Generate visualizations
        print(f"🎨 Generating publication-quality visualizations...")
        self.visualizations = generate_all_visualizations(
            base_props, partner_props, pareto_results, fold_seq, seam_cands, prod_plan, theta_deg
        )
        
        # Save to cache
        with open(cache_file, 'wb') as f:
            pickle.dump(self.visualizations, f)
        print(f"✓ Visualizations generated and cached: {cache_key}")
        
        return self.visualizations
    
    def _get_cache_key(self) -> str:
        """Generate deterministic cache key from pipeline state."""
        parts = []
        if self.base_material:
            parts.append(f"base:{self.base_material.name}")
        if self.partner:
            parts.append(f"partner:{self.partner.name}")
        if self.fold_sequence:
            parts.append(f"folds:{self.fold_sequence.final_gluon_mass:.3f}:{self.fold_sequence.final_tensile:.0f}")
        if self.seam_candidates:
            parts.append(f"seams:{len(self.seam_candidates)}")
        if self.production_plan:
            parts.append(f"prod:{self.production_plan.total_energy_joules_per_cm2:.0f}")
        key_str = "|".join(parts)
        return hashlib.md5(key_str.encode()).hexdigest()[:12]
    
    def export_visualizations_html(self, output_dir: str = "viz_output") -> Path:
        """Export all visualizations as HTML files for embedding."""
        if not self.visualizations:
            raise ValueError("No visualizations generated yet. Run generate_visualizations() first.")
        
        out_dir = Path(output_dir)
        self.visualizations.save_all(out_dir)
        print(f"✓ Exported {len(self.visualizations.__dataclass_fields__)} visualizations to {out_dir}")
        return out_dir

    def run_full_pipeline(
        self, 
        material_name: Optional[str] = None,
        partner_idx: Optional[int] = None,
        area_cm2: float = 1.0,
        save_path: str = "metamaterial_report.json",
        generate_viz: bool = True,
        viz_output_dir: str = "viz_output"
    ) -> bool:
        """Run the complete design pipeline"""
        
        # Step 1: Select base material
        if not self.select_base_material(material_name):
            return False
        
        # Step 2: Find Pareto partners
        self.find_partners()
        
        # Step 3: Select partner
        if not self.select_partner(partner_idx):
            return False
        
        # Step 4: Run 10-fold evaluation
        self.run_fold_evaluation()
        
        # Step 5: Detect seam materials
        self.find_seams()
        
        # Step 6: Generate production plan
        self.generate_production(area_cm2)
        
        # Step 7: Generate flux summary (WASTE → FLUX/TRANSITION)
        self.flux_summary = calculate_flux_summary(self.production_plan.steps)
        print(f"⚗️ Flux summary: {self.flux_summary['total_steps_with_flux']} steps, "
              f"{self.flux_summary['total_waste_eliminated_kg_per_cm2']*1000:.1f} g/cm² waste eliminated, "
              f"${self.flux_summary['total_estimated_savings_usd_per_cm2']:.0f}/cm² savings")
        
        # Step 8: Generate visualizations (STANDARD OUTPUT)
        if generate_viz:
            self.generate_visualizations()
            self.export_visualizations_html(viz_output_dir)
        
        # Step 9: Save report
        self.save_report(save_path)
        
        print("\n✅ DESIGN PIPELINE COMPLETE")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="MetaMaterial Design System - Comprehensive metamaterial design pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python meta_material_designer.py
  python meta_material_designer.py --material graphene
  python meta_material_designer.py --material graphene --partner 1 --area 10
  python meta_material_designer.py --material-file my_material.json --auto-partner
  python meta_material_designer.py --template
        """
    )
    
    parser.add_argument(
        "--material", "-m",
        help="Base material name (from database) or path to JSON file"
    )
    parser.add_argument(
        "--material-file", "-f",
        help="Path to custom material JSON file"
    )
    parser.add_argument(
        "--partner", "-p",
        type=int,
        help="Partner index from Pareto results (1-based)"
    )
    parser.add_argument(
        "--auto-partner", "-a",
        action="store_true",
        help="Automatically select top Pareto partner"
    )
    parser.add_argument(
        "--area",
        type=float,
        default=1.0,
        help="Target production area in cm² (default: 1.0)"
    )
    parser.add_argument(
        "--output", "-o",
        default="metamaterial_report.json",
        help="Output report file path (default: metamaterial_report.json)"
    )
    parser.add_argument(
        "--viz-dir",
        default="viz_output",
        help="Visualization output directory (default: viz_output)"
    )
    parser.add_argument(
        "--no-viz",
        action="store_true",
        help="Skip visualization generation"
    )
    parser.add_argument(
        "--theta",
        type=float,
        default=1.1,
        help="Twist angle for moiré visualization (default: 1.1)"
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Generate material template JSON and exit"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available materials and exit"
    )
    
    args = parser.parse_args()
    
    designer = MetaMaterialDesigner()
    
    # Handle special commands
    if args.template:
        designer.save_material_template()
        return 0
    
    if args.list:
        print("Available materials:")
        for name in list_materials():
            mat = get_material(name)
            print(f"  {mat.name} ({mat.formula})")
        return 0
    
    # Determine material source
    material_source = args.material
    if args.material_file:
        material_source = args.material_file
    
    # Determine partner selection
    partner_idx = None
    if args.auto_partner:
        partner_idx = 0  # Top partner
    elif args.partner is not None:
        partner_idx = args.partner - 1  # Convert to 0-based
    
    # Run pipeline
    success = designer.run_full_pipeline(
        material_name=material_source,
        partner_idx=partner_idx,
        area_cm2=args.area,
        save_path=args.output,
        generate_viz=not args.no_viz,
        viz_output_dir=args.viz_dir
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())