#!/usr/bin/env python3
"""
Test script for the metamaterial design system
"""
import sys
sys.path.insert(0, r'D:\CQE_CMPLX\CQECMPLX-ProofValidatedSuite\EXPOSE-PAPERS')

from meta_material_system import (
    MetaMaterialDesigner,
    get_material,
    list_materials,
    run_10_fold_evaluation,
    detect_seam_candidates,
    generate_production_plan
)


def test_full_pipeline():
    """Test the complete pipeline with graphene + hBN"""
    print("="*60)
    print("TESTING FULL PIPELINE: Graphene + hBN")
    print("="*60)
    
    designer = MetaMaterialDesigner()
    
    # Step 1: Load materials
    designer.base_material = get_material("graphene")
    designer.partner = get_material("hbn")
    
    print(f"Base: {designer.base_material.name}")
    print(f"Partner: {designer.partner.name}")
    
    # Step 2: Find partners (for verification)
    all_mats = [get_material(k) for k in list_materials()]
    partners = designer.find_partners()
    
    # Verify hBN is top partner for graphene
    assert partners[0].material_b.name == "Hexagonal Boron Nitride", "hBN should be top partner"
    print("✓ Pareto partnering works - hBN is top partner for graphene")
    
    # Step 3: Run fold evaluation
    designer.fold_sequence = run_10_fold_evaluation(
        designer.base_material, 
        designer.partner
    )
    
    # Verify results
    assert designer.fold_sequence.final_tensile > 0
    assert designer.fold_sequence.final_composite > 0
    assert designer.fold_sequence.final_gluon_mass > 0
    print(f"✓ 10-fold evaluation complete")
    print(f"  Final Tensile: {designer.fold_sequence.final_tensile:.0f} MPa")
    print(f"  Final Composite: {designer.fold_sequence.final_composite:.0f} MPa")
    print(f"  Final Gluon Mass: {designer.fold_sequence.final_gluon_mass:.3f}")
    print(f"  Formation Energy: {designer.fold_sequence.total_formation_energy:.2f} eV")
    
    # Step 4: Detect seams
    designer.seam_candidates = detect_seam_candidates(
        designer.base_material,
        designer.partner,
        designer.fold_sequence
    )
    print(f"✓ Seam detection found {len(designer.seam_candidates)} candidates")
    
    # Step 6: Generate production plan
    test_area = 1.0
    designer.production_plan = generate_production_plan(
        designer.base_material,
        designer.partner,
        designer.fold_sequence,
        designer.seam_candidates,
        target_area_cm2=test_area
    )
    
    assert designer.production_plan.total_energy_joules_per_cm2 > 0
    assert designer.production_plan.estimated_cost_usd_per_cm2 > 0
    print(f"✓ Production plan generated")
    print(f"  Energy: {designer.production_plan.total_energy_joules_per_cm2/1e6:.2f} MJ/cm²")
    print(f"  Cost: ${designer.production_plan.estimated_cost_usd_per_cm2:.2f}/cm²")
    print(f"  Time: {designer.production_plan.total_time_hours:.1f} hours")
    
    # Save report
    designer.save_report("test_report.json")
    
    print("\n✅ ALL TESTS PASSED")
    return True


def test_other_combinations():
    """Test other material combinations"""
    print("\n" + "="*60)
    print("TESTING OTHER COMBINATIONS")
    print("="*60)
    
    test_pairs = [
        ("graphene", "tbg"),
        ("mos2", "hbn"),
        ("bp", "mxene"),
        ("sto", "mowse2"),
    ]
    
    for base_name, partner_name in test_pairs:
        print(f"\nTesting {base_name} + {partner_name}...")
        
        base = get_material(base_name)
        partner = get_material(partner_name)
        
        if not base or not partner:
            print(f"  ⚠ Material not found, skipping")
            continue
        
        # Quick fold evaluation
        folds = run_10_fold_evaluation(base, partner, seed=123)
        
        # Quick seam detection
        seams = detect_seam_candidates(base, partner, folds)
        
        # Quick production
        plan = generate_production_plan(base, partner, folds, seams, 1.0)
        
        print(f"  Tensile: {folds.final_tensile:.0f} MPa")
        print(f"  Composite: {folds.final_composite:.0f} MPa")
        print(f"  Gluon: {folds.final_gluon_mass:.3f}")
        print(f"  Seams: {len(seams)}")
        print(f"  Energy: {plan.total_energy_joules_per_cm2/1e6:.2f} MJ/cm²")
        print(f"  Cost: ${plan.estimated_cost_usd_per_cm2:.2f}/cm²")
        
        # Verify basic sanity
        assert folds.final_tensile > 100  # Should have reasonable strength
        assert folds.final_gluon_mass < 3.0  # Gluon mass capped
        assert plan.total_energy_joules_per_cm2 > 0
    
    print("\n✅ All combination tests passed")


def test_edge_cases():
    """Test edge cases"""
    print("\n" + "="*60)
    print("TESTING EDGE CASES")
    print("="*60)
    
    # Same material (should handle gracefully)
    base = get_material("graphene")
    partner = get_material("graphene")
    
    folds = run_10_fold_evaluation(base, partner)
    print(f"Same material (graphene+graphene): Tensile={folds.final_tensile:.0f}, Gluon={folds.final_gluon_mass:.3f}")
    
    # Materials with no oloid closure
    base = get_material("mxene")
    partner = get_material("mowse2")
    
    folds = run_10_fold_evaluation(base, partner)
    print(f"No oloid closure (mxene+mowse2): Tensile={folds.final_tensile:.0f}, Oloid={folds.folds[-1].oloid_closure}")
    
    print("✅ Edge case tests passed")


if __name__ == "__main__":
    try:
        test_full_pipeline()
        test_other_combinations()
        test_edge_cases()
        print("\n" + "="*60)
        print("ALL TESTS COMPLETED SUCCESSFULLY")
        print("="*60)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)