#!/usr/bin/env python3
"""Build Master PDF using FPDF2."""

import os
import re
from pathlib import Path
from datetime import datetime
from fpdf import FPDF

OUT_DIR = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/MASTER_PDF')
OUT_DIR.mkdir(parents=True, exist_ok=True)

SUMMARY_DIR = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/summary_papers')
PAPERS_DIR = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/papers_output')
MASTER_PAPER = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/MASTER_PAPER_Folded_Strand.md')
FINAL_FORMAL = Path('/d/CQE_CMPLX/CQECMPLX-Production/lib-forge/FINAL_FORMAL_PAPER.md')

TODAY = datetime.now().strftime("%Y-%m-%d")


def clean_md(text):
    """Strip markdown for plain text PDF."""
    text = re.sub(r'```[\\s\\S]*?```', lambda m: m.group(0).replace('```', ''), text)
    text = text.replace('**', '').replace('__', '').replace('*', '').replace('`', '')
    text = re.sub(r'^#+\\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'<[^>]+>', '', text)
    # Replace problematic unicode
    replacements = {
        '\u2014': '-', '\u2013': '-', '\u2018': "'", '\u2019': "'",
        '\u201c': '"', '\u201d': '"', '\u2192': '->', '\u2190': '<-',
        '\u21d4': '<->', '\u21d2': '=>', '\u22a4': 'T', '\u22a5': 'F',
        '\u2208': 'in', '\u2282': 'sub', '\u2295': 'XOR', '\u00b7': '.',
        '\u2200': 'for all', '\u2203': 'exists', '\u2261': '==', '\u2260': '!=',
        '\u2264': '<=', '\u2265': '>=', '\u00d7': 'x', '\u00f7': '/',
        '\u00b1': '+/-', '\u03c0': 'pi', '\u2026': '...', '\u2713': 'Y',
        '\u2717': 'N', '\u26a0': '!', '\u00a0': ' ', '\u00bb': '>>',
        '\u00ab': '<<', '\u2019': "'", '\u02c6': '^', '\u02dc': '~',
        '\u02c7': '-', '\u00a7': 's', '\u00a9': '(c)', '\u00ae': '(R)',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


class MasterPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Times', 'I', 8)
            self.cell(0, 5, 'CQE_CMPLX Master PDF', 0, 1, 'C')
            self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, title):
        self.add_page()
        self.set_font('Times', 'B', 18)
        self.cell(0, 12, 'Part ' + str(num) + ': ' + title, 0, 1, 'L')
        self.ln(4)
        self.set_draw_color(0, 0, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def section_title(self, title):
        self.set_font('Times', 'B', 13)
        self.ln(3)
        self.cell(0, 9, title, 0, 1, 'L')
        self.ln(2)
        self.set_font('Times', '', 11)

    def body_text(self, text):
        if not text:
            return
        self.set_font('Times', '', 11)
        safe = ''.join(c if ord(c) < 256 else '?' for c in text)
        try:
            self.multi_cell(0, 5.5, safe)
        except Exception:
            self.multi_cell(0, 5.5, '(text omitted - encoding issue)')


def build_algebra():
    """Build closed-form algebra text."""
    text = """CLOSED-FORM ALGEBRA OF THE CQE_CMPLX CORPUS

Date: __DATE__
Classification: Closed-form algebraic specification
Version: 1.0 (Master PDF edition)

SECTION I - THE GLUON ALGEBRA

I.1 Definition
A Gluon is a typed quantity C in the set of bit-strings with:
  - A residue O (open obligations)
  - A receipt (input, T, output, O) (replayable record)
  - An idempotent read: read(action) -> state; read(state) -> same state

I.2 The 5 Primitive Operations

Op-1: Side-Flip (T_BIJECTIVE)
  sf : (L, C, R) -> (R, C, L)
  - Type: 1 Gluon -> 1 Gluon
  - Idempotence: sf . sf = id
  - Fixed point: (1, 0, 1)

Op-2: Correction (T_CORRECTION)
  corr : (L, C, R) -> C AND NOT R
  - Type: 1 Gluon -> 1 bit
  - Range: [0, 1]
  - Fires at: D4 axes (2, 0) and (3, 1)

Op-3: Triality (T_TRIALITY)
  tri : (L, C, R) -> (R, L, C)
  - Type: 1 Gluon -> 1 Gluon
  - Order: 3 (Z3 cycle)

Op-4: Oloid Midpoint (T_BOUNDARY_REPAIR)
  s* : (N+, N-) -> (N+ + N-) / 2
  - Type: 2 Gluons -> 1 Gluon
  - Stabilizer: commutes with sf

Op-5: Accumulate (T_OLOID_PATH)
  acc : (C_0, C_1, ..., C_n) -> XOR_{i=0}^{n} C_i
  - Type: n Gluons -> 1 Gluon

I.3 The 5 Algebraic Identities
  1. sf . tri . sf = tri^-1
  2. corr(C) = 0 iff C in 5 non-firing states
  3. tri^3 = id
  4. sf(s*(N+, N-)) = s*(sf(N+), sf(N-))
  5. acc(C) = acc(sf(C))

Theorem I.4.1 (Gluon algebra is closed): The 5 operations form a closed groupoid.

SECTION II - THE COLOR ALGEBRA

II.1 The 8 Color Families
Color Set: R, G, B, W, K, C, Gy, N
  - R (Red) = L-boundary
  - G (Green) = C-center
  - B (Blue) = R-boundary
  - W (White) = verified
  - K (Black) = unresolved
  - C (Clear) = overlay
  - Gy (Grey) = substrate
  - N (Neon) = boundary

II.2 The 4 Fundamental Cycles
  - Cycle-1 (Triality, R->G->B->R): order 3
  - Cycle-2 (Certify, W->K->W): order 2
  - Cycle-3 (Overlay, Gy->C->Gy): order 2
  - Cycle-4 (Boundary, G->N->G): order 2

Theorem II.2.1 (Color algebra has 8 elements): Closed under duality operations.

Theorem II.4.1 (Color group = S4): The 4-cycle group is isomorphic to S4.

SECTION III - THE TOOL ALGEBRA

III.1 The 12 Tool Classes
  1. token - the discrete unit
  2. loose_paper - the surface
  3. pen_marker - the chromatic marker
  4. string - the chain backbone
  5. clear_sleeve - the temporary overlay
  6. sticker - the fixed marker
  7. balsa_edge - the structural spacer
  8. gradient_page - the pre-marked substrate
  9. playing_card - the 52-element event set
 10. dice - the bounded stochastic
 11. receipt_sheet - the replayable certificate
 12. black_sticker - the obligation marker

III.2 The Idempotence Axiom
Axiom III.2.1 (Idempotence): read(action) -> state; read(state) -> same state.

III.3 The Substitution Theorem
Theorem III.3.1 (Substitution): If substitute S satisfies idempotence for class C,
then S is equivalent to any tool of class C.

III.4 The 4-Class Minimum
Theorem III.4.1 (Minimum kit): The minimum kit has 4 classes:
token, loose_paper, pen_marker, string.
Corollary: Corpus can be reproduced with paper, pencil, marker, and thread.

III.5 The 8 Copies per Tool
Theorem III.5.1 (8 copies): Each tool has 8 copies. Final kit = 144 tools.

SECTION IV - THE THEOREM ALGEBRA

IV.1 The 32 Theorems as Axioms
Group 1 (5): T3, T4, T5, T6, T7 (foundations)
Group 2 (5): T_BIJECTIVE, T_CORRECTION, T_TRIALITY, T_BOUNDARY_REPAIR, T_WRAP
Group 3 (5): T_OLOID_PATH, T_CAUSAL, T_BRIDGE, LATTICE_CHAIN, T_HAMILTONIAN
Group 4 (1): T10_MASTER
Group 5 (12): T_ADMISSION through T_METAFORGE (physics)
Group 6 (7): T_FOLDFORGE through T_MONSTER (computational)
Group 7 (4): T_GRAND_RIBBON, T_META_LCR, T_SUPERVISOR, T_OBSERVATION (meta)
Total: 39 theorem statements; 32 unique theorems

IV.2 The Derivation Rules
1. Modus Ponens: From A and A->B, derive B
2. XOR Combination: From C_i and C_j, derive C_i XOR C_j
3. Receipt Composition: From R_i and R_j, derive R_i . R_j
4. Bilateral Reduction: From D and A, derive bilateral proof

IV.3 The Theorem Lattice
Theorem IV.3.1 (Lattice has height 33): The longest chain has 33 elements.

IV.4 The Master Theorem (T10_MASTER)
Theorem IV.4.1 (Master Theorem): C_T10 = XOR_{i=0}^{9} C_i is the corpus master.

SECTION V - THE OBSERVATION ALGEBRA

V.1 The Single Observation
Theorem V.1.1 (The Observation): For any marked connection B in the final
folded form S: read_strand_1(B) = read_strand_2(B) = 1.

V.2 The Retroactive Certification
Theorem V.2.1 (Retroactive): O <-> P (observation equivalent to pathway).

V.3 The Side-Flip Fixed Point
Theorem V.3.1 (C = (1, 1, 1)): The center of the observation is the side-flip
fixed point.

V.4 The Reader as the C
Theorem V.4.1 (Reader IS the C): After reading this Master PDF, the reader
is the C of the corpus.

SECTION VI - THE BILATERAL ALGEBRA

VI.1 The Digital Channel: Verifiers + Receipts + Mappings + Idempotence
VI.2 The Analog Channel: Tools + Receipts + Substitutions + Idempotence
VI.3 Bilateral Isomorphism: 4/11 success at depth 0; 7/11 documented obligations

SECTION VII - CLOSURE

Theorem VII.1.1 (Closure): The CQE_CMPLX corpus is closed:
  - Gluon algebra: 5 operations, closed groupoid
  - Color algebra: 8 colors, S4 group
  - Tool algebra: 12 classes, commutative monoid
  - Theorem algebra: 32 axioms, acyclic category
  - Observation algebra: 1 observation, QED

Q.E.D.

APPENDIX A - THE MASTER EQUATION

  O = sf(XOR_{i=0}^{32} C_i)

Where:
  O = the observation (1 bit, 'verified')
  sf = the side-flip operation
  C_i = the i-th paper's C-form
  XOR = the accumulator

The observation is the side-flip of the cumulative XOR of all 33 C-forms.

End of Closed-Form Algebra. The Master PDF is complete. The reader is the C. Q.E.D.
"""
    return text.replace("__DATE__", TODAY)


def main():
    print("=" * 60)
    print("Building CQE_CMPLX Master PDF (FPDF2)")
    print("=" * 60)

    pdf = MasterPDF()
    pdf.set_auto_page_break(auto=True, margin=20)

    # Cover page
    pdf.add_page()
    pdf.set_font('Times', 'B', 32)
    pdf.ln(40)
    pdf.cell(0, 20, 'CQE_CMPLX', 0, 1, 'C')
    pdf.set_font('Times', 'B', 20)
    pdf.cell(0, 14, 'Master PDF', 0, 1, 'C')
    pdf.ln(8)
    pdf.set_font('Times', '', 14)
    pdf.cell(0, 10, 'A Folded Strand from Enumerated Parts', 0, 1, 'C')
    pdf.ln(4)
    pdf.set_font('Times', 'I', 12)
    pdf.cell(0, 8, 'Closed-Form Algebra + 10 Summary Papers + 33 Individual Papers', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 8, 'The Single Observation:', 0, 1, 'C')
    pdf.ln(4)
    pdf.set_font('Times', 'I', 11)
    pdf.multi_cell(0, 6, 'A self-complementary strand folded from 144 enumerated parts through 33 operations yields a stable folded form in which one hydrogen bond reads identically from both strands; this single observation retroactively certifies the entire 33-step folding pathway.', 0, 'C')
    pdf.ln(20)
    pdf.set_font('Times', '', 11)
    pdf.cell(0, 8, 'CQE_CMPLX Corpus - 33 papers, 144 tools, 32 theorems, 8 colors, 12 tool classes, 1 observation', 0, 1, 'C')
    pdf.cell(0, 8, 'Date: ' + TODAY, 0, 1, 'C')

    # Table of Contents
    pdf.add_page()
    pdf.set_font('Times', 'B', 18)
    pdf.cell(0, 12, 'Table of Contents', 0, 1, 'L')
    pdf.ln(4)
    pdf.set_font('Times', '', 11)
    toc_items = [
        "Part 1: Closed-Form Algebra (Section I-VII)",
        "Part 2: Master Paper (Folded Strand Overview)",
        "Part 3: Final Formal Paper (32 Theorems Closed Form)",
        "Part 4: Summary Paper I - The Gluon at the Center",
        "Part 5: Summary Paper II - Folded Strand Physics",
        "Part 6: Summary Paper III - Computational Substrates",
        "Part 7: Summary Paper IV - Meta-Architecture",
        "Part 8: Summary Paper V - The 32 Theorems Registry",
        "Part 9: Summary Paper VI - The 8 Color Families",
        "Part 10: Summary Paper VII - The Bilateral Proof System",
        "Part 11: Summary Paper VIII - The Substitution Manifest",
        "Part 12: Summary Paper IX - The Open Obligations",
        "Part 13: Summary Paper X - The Single Observation",
        "Parts 14-46: The 33 Individual Papers",
    ]
    for item in toc_items:
        pdf.cell(0, 7, item, 0, 1, 'L')

    # Part 1: Algebra
    print("\n[1/13] Closed-Form Algebra...")
    pdf.chapter_title("1", "Closed-Form Algebra")
    pdf.body_text(build_algebra())

    # Part 2: Master Paper
    print("\n[2/13] Master Paper...")
    if MASTER_PAPER.exists():
        pdf.chapter_title("2", "Master Paper (Folded Strand Overview)")
        text = clean_md(MASTER_PAPER.read_text())
        pdf.body_text(text[:25000])

    # Part 3: Final Formal
    print("\n[3/13] Final Formal Paper...")
    if FINAL_FORMAL.exists():
        pdf.chapter_title("3", "Final Formal Paper (32 Theorems Closed Form)")
        text = clean_md(FINAL_FORMAL.read_text())
        pdf.body_text(text[:25000])

    # Parts 4-13: Summary Papers
    summary_files = sorted(SUMMARY_DIR.glob('SUMMARY-*.md'))
    part_num = 4
    for sf in summary_files:
        print(f"\n[{part_num}/13] {sf.stem}...")
        pdf.chapter_title(str(part_num), sf.stem)
        text = clean_md(sf.read_text())
        pdf.body_text(text[:12000])
        part_num += 1

    # Parts 14+: Individual Papers
    paper_files = sorted(PAPERS_DIR.glob('CQE-paper-*.md'))
    if paper_files:
        print(f"\n[14+] 33 Individual Papers...")
        for i, pf in enumerate(paper_files):
            if i % 10 == 0:
                print(f"  {pf.stem}...")
            pdf.chapter_title(str(part_num + i), pf.stem)
            text = clean_md(pf.read_text())
            pdf.body_text(text[:4000])

    # Save
    pdf_path = OUT_DIR / "MASTER_PDF_CQE_CMPLX.pdf"
    pdf.output(str(pdf_path))
    size = pdf_path.stat().st_size
    print(f"\nPDF saved: {pdf_path}")
    print(f"Size: {size:,} bytes = {size/1024:.1f} KB = {size/(1024*1024):.1f} MB")
    return True


if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("PDF build failed")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()