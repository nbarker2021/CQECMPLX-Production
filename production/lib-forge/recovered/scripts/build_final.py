#!/usr/bin/env python3
"""Generate all 33 papers + Final Formal Paper from MASTER spec."""
import sys
from pathlib import Path

sys.path.insert(0, '/d/CQE_CMPLX/CQECMPLX-Production/lib-forge')

# Import as modules
import part1_constants as P1
import part2_steps as P2
import part3_data as P3
import part4_functions as P4

# Inject data into the function module's namespace
P4.VERIFIED_THEOREMS = P1.VERIFIED_THEOREMS
P4.PAPER_F_STEPS = P2.PAPER_F_STEPS
P4.PAPER_THEOREMS = P3.PAPER_THEOREMS
P4.VERIFICATION_COMMANDS = P3.VERIFICATION_COMMANDS
P4.CUMULATIVE_KIT = P3.CUMULATIVE_KIT

if __name__ == "__main__":
    print("Generating all papers...")
    output_dir = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/papers_output')
    output_dir.mkdir(parents=True, exist_ok=True)

    all_papers = sorted(P2.PAPER_F_STEPS.keys())
    print(f"Total papers to generate: {len(all_papers)}")

    for paper_id in all_papers:
        content = P4.generate_paper(paper_id)
        out_path = output_dir / f"{paper_id}.md"
        out_path.write_text(content)
        print(f"  Generated: {out_path.name}")

    # Final formal paper
    final_content = P4.generate_final_formal_paper()
    final_path = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/FINAL_FORMAL_PAPER.md')
    final_path.write_text(final_content)
    print(f"\nFinal formal paper generated: {final_path}")
    print(f"\nAll {len(all_papers)} papers + FINAL_FORMAL_PAPER.md generated!")
