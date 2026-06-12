#!/usr/bin/env python3
"""Build top-level review-facing PDFs from promoted CQECMPLX formal papers."""

from __future__ import annotations

import argparse
import json
import re
import textwrap
import unicodedata
import warnings
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from fpdf import FPDF


warnings.filterwarnings("ignore", category=DeprecationWarning)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "Papers" / "Source"
FORMAL_ROOT = ROOT / "production" / "formal-papers"
KERNEL_ROOT = ROOT / "production" / "paper-kernels" / "papers"
OUT_DIR = ROOT / "Papers" / "PDF"


REPLACEMENTS = {
    "\u2013": "-",
    "\u2014": "-",
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u2026": "...",
    "\u2192": "->",
    "\u2190": "<-",
    "\u2194": "<->",
    "\u21d2": "=>",
    "\u2208": "in",
    "\u2209": "notin",
    "\u2264": "<=",
    "\u2265": ">=",
    "\u2248": "~=",
    "\u2260": "!=",
    "\u03b5": "epsilon",
    "\u03b3": "gamma",
    "\u0393": "Gamma",
    "\u03bb": "lambda",
    "\u2212": "-",
    "\u2217": "*",
}


def clean_text(text: str) -> str:
    for src, dst in REPLACEMENTS.items():
        text = text.replace(src, dst)
    text = unicodedata.normalize("NFKD", text)
    return text.encode("latin-1", "ignore").decode("latin-1")


def slug(text: str) -> str:
    text = clean_text(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "paper"


def paper_sort_key(paper_id: str) -> tuple[float, str]:
    match = re.search(r"(\d+(?:\.\d+)?)", paper_id)
    if not match:
        return (9999.0, paper_id)
    return (float(match.group(1)), paper_id)


@dataclass
class PaperInput:
    paper_id: str
    title: str
    formal_path: Path
    source_label: str
    manifest_path: Path | None
    verifier_paths: list[Path]
    receipt_paths: list[Path]


class ReviewPDF(FPDF):
    def __init__(self, title: str, paper_id: str):
        super().__init__(unit="in", format="Letter")
        self.title = clean_text(title)
        self.paper_id = clean_text(paper_id)
        self.set_auto_page_break(auto=True, margin=0.65)
        self.set_margins(0.72, 0.72, 0.72)

    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_font("Times", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 0.2, f"{self.paper_id} - {self.title}", 0, 1, "R")
        self.ln(0.08)
        self.set_text_color(0, 0, 0)

    def footer(self) -> None:
        self.set_y(-0.45)
        self.set_font("Times", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 0.2, f"Review draft - page {self.page_no()}", 0, 0, "C")
        self.set_text_color(0, 0, 0)

    def title_page(self, paper: PaperInput, manifest: dict | None) -> None:
        self.add_page()
        self.set_font("Times", "B", 22)
        self.multi_cell(0, 0.35, clean_text(paper.title), align="C")
        self.ln(0.18)
        self.set_font("Times", "", 12)
        self.cell(0, 0.25, clean_text(paper.paper_id), 0, 1, "C")
        self.cell(0, 0.25, "CQECMPLX Formal Paper Series", 0, 1, "C")
        self.cell(0, 0.25, f"Review-facing PDF built {date.today().isoformat()}", 0, 1, "C")
        self.ln(0.5)
        self.set_font("Times", "B", 12)
        self.cell(0, 0.25, "Construction Basis", 0, 1)
        self.set_font("Times", "", 10)
        thesis = (manifest or {}).get("central_thesis")
        if thesis:
            self.multi_cell(0, 0.22, clean_text(thesis))
            self.ln(0.12)
        self.multi_cell(
            0,
            0.22,
            clean_text(
                "This PDF is the clean paper artifact. Source extracts, kernels, "
                "receipts, tool notes, workbook material, and package bindings are "
                "used as construction evidence; they are not treated as separate "
                "review-facing papers."
            ),
        )
        self.ln(0.25)
        self.set_font("Times", "B", 11)
        self.cell(0, 0.25, "Evidence Inputs", 0, 1)
        self.set_font("Times", "", 9)
        for line in evidence_lines(paper, manifest):
            self.wrapped_line(clean_text(f"- {line}"), height=0.2, width=92)
        self.add_page()

    def heading(self, text: str, level: int) -> None:
        self.ln(0.08 if level > 1 else 0.18)
        sizes = {1: 17, 2: 14, 3: 12}
        self.set_font("Times", "B", sizes.get(level, 11))
        self.multi_cell(0, 0.28, clean_text(text))
        self.ln(0.04)

    def paragraph(self, text: str) -> None:
        self.set_font("Times", "", 10.4)
        self.wrapped_line(clean_text(text), height=0.205, width=96)
        self.ln(0.04)

    def bullet(self, text: str) -> None:
        self.set_font("Times", "", 10)
        wrapped = textwrap.wrap(
            clean_text(text),
            width=92,
            break_long_words=True,
            break_on_hyphens=True,
        ) or [""]
        self.set_x(self.l_margin)
        self.cell(0.18, 0.2, "-")
        self.multi_cell(0, 0.2, wrapped[0])
        for rest in wrapped[1:]:
            self.set_x(self.l_margin)
            self.cell(0.18, 0.2, "")
            self.multi_cell(0, 0.2, rest)
        self.ln(0.02)

    def code_block(self, text: str) -> None:
        self.set_font("Courier", "", 8.2)
        self.set_fill_color(245, 245, 245)
        for raw in clean_text(text).splitlines() or [""]:
            for line in textwrap.wrap(
                raw,
                width=96,
                replace_whitespace=False,
                break_long_words=True,
                break_on_hyphens=True,
            ) or [""]:
                self.set_x(self.l_margin)
                self.multi_cell(0, 0.17, line, fill=True)
        self.ln(0.08)

    def wrapped_line(self, text: str, height: float, width: int) -> None:
        wrapped = textwrap.wrap(
            clean_text(text),
            width=width,
            break_long_words=True,
            break_on_hyphens=True,
        ) or [""]
        for line in wrapped:
            self.set_x(self.l_margin)
            self.multi_cell(0, height, line)


def read_manifest(paper_id: str) -> dict | None:
    if "." in paper_id:
        return None
    path = KERNEL_ROOT / paper_id / "paper_kernel_manifest.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_lines(paper: PaperInput, manifest: dict | None) -> list[str]:
    lines = [f"{paper.source_label}: {paper.formal_path.relative_to(ROOT)}"]
    if paper.manifest_path:
        lines.append(f"paper kernel manifest: {paper.manifest_path.relative_to(ROOT)}")
    for path in paper.verifier_paths:
        lines.append(f"verifier: {path.relative_to(ROOT)}")
    for path in paper.receipt_paths:
        status = receipt_status(path)
        suffix = f" ({status})" if status else ""
        lines.append(f"receipt: {path.relative_to(ROOT)}{suffix}")
    for key, row in (manifest or {}).get("sources", {}).items():
        if row.get("present"):
            lines.append(f"{key}: {row.get('path')}")
    return lines


def receipt_status(path: Path) -> str:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return ""
    status = payload.get("status") or payload.get("verdict")
    theorem = payload.get("theorem") or payload.get("paper")
    if status and theorem:
        return f"{theorem}: {status}"
    return str(status or "")


def discover_papers(selected: list[str] | None = None) -> list[PaperInput]:
    papers_by_id: dict[str, PaperInput] = {}

    for source_path in sorted(SOURCE_ROOT.glob("CQE-paper-*.md")):
        paper_id = source_path.stem
        if selected and paper_id not in selected:
            continue
        raw = source_path.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", raw, flags=re.MULTILINE)
        title = title_match.group(1).strip() if title_match else paper_id
        manifest_path = KERNEL_ROOT / paper_id / "paper_kernel_manifest.json"
        papers_by_id[paper_id] = PaperInput(
            paper_id=paper_id,
            title=title,
            formal_path=source_path,
            source_label="top-level review source",
            manifest_path=manifest_path if manifest_path.exists() else None,
            verifier_paths=[],
            receipt_paths=[],
        )

    for formal_path in sorted(FORMAL_ROOT.glob("CQE-paper-*/FORMAL_PAPER.md")):
        paper_id = formal_path.parent.name
        if paper_id in papers_by_id:
            continue
        if selected and paper_id not in selected:
            continue
        raw = formal_path.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", raw, flags=re.MULTILINE)
        title = title_match.group(1).strip() if title_match else paper_id
        manifest_path = KERNEL_ROOT / paper_id / "paper_kernel_manifest.json"
        papers_by_id[paper_id] = (
            PaperInput(
                paper_id=paper_id,
                title=title,
                formal_path=formal_path,
                source_label="promoted formal paper",
                manifest_path=manifest_path if manifest_path.exists() else None,
                verifier_paths=sorted(formal_path.parent.glob("verify_*.py")),
                receipt_paths=sorted(formal_path.parent.glob("*.json")),
            )
        )

    for body_path in sorted((ROOT / "production" / "papers").glob("CQE-paper-*/PAPER-BODY.md")):
        paper_id = body_path.parent.name
        if paper_id in papers_by_id:
            continue
        if selected and paper_id not in selected:
            continue
        raw = body_path.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", raw, flags=re.MULTILINE)
        title = title_match.group(1).strip() if title_match else paper_id
        manifest_path = KERNEL_ROOT / paper_id / "paper_kernel_manifest.json"
        papers_by_id[paper_id] = PaperInput(
            paper_id=paper_id,
            title=title,
            formal_path=body_path,
            source_label="production paper body pending rewrite",
            manifest_path=manifest_path if manifest_path.exists() else None,
            verifier_paths=[],
            receipt_paths=sorted((ROOT / "production" / "proof-receipts" / paper_id).glob("**/*.json")),
        )

    return [
        papers_by_id[paper_id]
        for paper_id in sorted(papers_by_id, key=paper_sort_key)
    ]


def render_markdown(pdf: ReviewPDF, markdown: str) -> None:
    paragraph: list[str] = []
    code: list[str] = []
    in_code = False

    def flush_paragraph() -> None:
        if paragraph:
            pdf.paragraph(" ".join(part.strip() for part in paragraph))
            paragraph.clear()

    def flush_code() -> None:
        if code:
            pdf.code_block("\n".join(code))
            code.clear()

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_paragraph()
                in_code = True
            continue
        if in_code:
            code.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            continue
        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            pdf.heading(heading.group(2), len(heading.group(1)))
            continue
        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if bullet or numbered:
            flush_paragraph()
            pdf.bullet((bullet or numbered).group(1))
            continue
        paragraph.append(line)

    flush_paragraph()
    flush_code()


def build_pdf(paper: PaperInput, out_dir: Path) -> Path:
    manifest = read_manifest(paper.paper_id)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{paper.paper_id}_{slug(paper.title)}.pdf"
    pdf = ReviewPDF(paper.title, paper.paper_id)
    pdf.title_page(paper, manifest)
    render_markdown(pdf, paper.formal_path.read_text(encoding="utf-8"))
    pdf.output(str(out_path))
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper", action="append", help="Paper id, e.g. CQE-paper-11")
    parser.add_argument("--out", default=str(OUT_DIR), help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.out)
    papers = discover_papers(args.paper)
    if not papers:
        raise SystemExit("No promoted formal papers found.")

    if not args.paper:
        out_dir.mkdir(parents=True, exist_ok=True)
        for stale in out_dir.glob("CQE-paper-*.pdf"):
            stale.unlink()

    built = []
    for paper in papers:
        path = build_pdf(paper, out_dir)
        built.append(
            {
                "paper": paper.paper_id,
                "title": paper.title,
                "pdf": str(path.relative_to(ROOT)),
                "bytes": path.stat().st_size,
            }
        )
        print(f"built {path}")

    manifest = {
        "built_on": date.today().isoformat(),
        "paper_count": len(built),
        "outputs": built,
    }
    manifest_path = out_dir / "review_pdf_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"manifest {manifest_path}")


if __name__ == "__main__":
    main()
