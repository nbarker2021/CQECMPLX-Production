"""
Working Subset Extractor - Exact-Fit Principle

For any given task, you use exactly what the problem needs —
whether 1 tool, 3 tools, 12 tools, or all 1,024.

The full kit (1,024 objects) is what you OWN.
The working subset is what you USE — sized to the problem exactly.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum


class ComplexityTier(Enum):
    """Problem complexity determines tool capability level needed."""
    MINIMAL = 1      # Single atomic operation
    SIMPLE = 2       # Small local process  
    MIDLINE = 3      # Multi-step with feedback
    COMPLEX = 4      # Full paper / cross-paper validation
    FULL_KIT = 5     # Corpus-wide operations
    
    def typical_range(self) -> range:
        """Typical tool count for this tier."""
        ranges = {
            ComplexityTier.MINIMAL: range(1, 3),
            ComplexityTier.SIMPLE: range(3, 8),
            ComplexityTier.MIDLINE: range(8, 20),
            ComplexityTier.COMPLEX: range(20, 60),
            ComplexityTier.FULL_KIT: range(60, 1025),
        }
        return ranges.get(self, range(1, 1025))


@dataclass
class WorkingSubset:
    """The exact tools needed for a specific problem."""
    paper_id: str
    primary_tool: str
    support_tools: List[str]
    receipt_tool: str
    colors_needed: List[str]
    complexity_tier: ComplexityTier
    
    def total_tools(self) -> int:
        return 1 + len(self.support_tools) + 1
    
    def in_typical_range(self) -> bool:
        return self.total_tools() in self.complexity_tier.typical_range()
    
    def summary(self) -> str:
        return (
            f"Paper: {self.paper_id}\n"
            f"Complexity: {self.complexity_tier.name}\n"
            f"Primary: {self.primary_tool}\n"
            f"Support: {', '.join(self.support_tools) or 'none'}\n"
            f"Receipt: {self.receipt_tool}\n"
            f"Colors: {', '.join(self.colors_needed)}\n"
            f"Total tools: {self.total_tools()} "
            f"(typical for {self.complexity_tier.name}: {self.complexity_tier.typical_range().start}–{self.complexity_tier.typical_range().stop-1})"
        )


# Paper-to-subset mapping — each uses exactly what it needs
PAPER_SUBSETS = {
    "CQE-paper-00": WorkingSubset(
        paper_id="CQE-paper-00",
        primary_tool="token:C:01",
        support_tools=["loose_paper:grey_gradient:01", "pen_marker:RGB:01", "loose_paper:reading_surface:01"],
        receipt_tool="receipt_sheet:white:01",
        colors_needed=["grey_gradient", "red", "green", "blue", "white"],
        complexity_tier=ComplexityTier.SIMPLE,
    ),
    "CQE-paper-01": WorkingSubset(
        paper_id="CQE-paper-01",
        primary_tool="token:side_flip:01",
        support_tools=["token:fixed_point:01"],
        receipt_tool="sticker:closure:01",
        colors_needed=["red", "blue", "white"],
        complexity_tier=ComplexityTier.MINIMAL,
    ),
    "CQE-paper-02": WorkingSubset(
        paper_id="CQE-paper-02",
        primary_tool="token:correction:01",
        support_tools=["clear_sleeve:overlay:01"],
        receipt_tool="obligation_sheet:black:01",
        colors_needed=["black", "clear", "white"],
        complexity_tier=ComplexityTier.MINIMAL,
    ),
    "CQE-paper-03": WorkingSubset(
        paper_id="CQE-paper-03",
        primary_tool="token:triangle:01",
        support_tools=["string:rotation:01"],
        receipt_tool="proof_tree_sheet:white:01",
        colors_needed=["red", "green", "blue", "white"],
        complexity_tier=ComplexityTier.SIMPLE,
    ),
    "CQE-paper-05": WorkingSubset(
        paper_id="CQE-paper-05",
        primary_tool="token:oloid:01",
        support_tools=["loose_paper:rolling_surface:01"],
        receipt_tool="receipt_sheet:curved:01",
        colors_needed=["grey_gradient", "neon", "white"],
        complexity_tier=ComplexityTier.SIMPLE,
    ),
    "CQE-paper-07": WorkingSubset(
        paper_id="CQE-paper-07",
        primary_tool="loose_paper:lucas_base:01",
        support_tools=["clear_sleeve:correction_overlay:01"],
        receipt_tool="receipt_sheet:bridge:01",
        colors_needed=["white", "clear"],
        complexity_tier=ComplexityTier.SIMPLE,
    ),
    "CQE-paper-10": WorkingSubset(
        paper_id="CQE-paper-10",
        primary_tool="token:receipt_bead:01",
        support_tools=["string:xor_chain:01", "pen_marker:hash:01"],
        receipt_tool="receipt_sheet:master:01",
        colors_needed=["white", "black"],
        complexity_tier=ComplexityTier.MIDLINE,
    ),
    "CQE-paper-30": WorkingSubset(
        paper_id="CQE-paper-30",
        primary_tool="token:bead:01",
        support_tools=[f"token:bead:{i:02d}" for i in range(2, 32)] + [
            "string:lcr_chain:01",
            "pen_marker:root_hash:01",
            "clear_sleeve:meta_framer:01"
        ],
        receipt_tool="receipt_sheet:grand_ribbon:01",
        colors_needed=["white", "black", "clear"],
        complexity_tier=ComplexityTier.COMPLEX,
    ),
    "CQE-paper-32": WorkingSubset(
        paper_id="CQE-paper-32",
        primary_tool="superpermutation_cursor:01",
        support_tools=[
            "notebook:full_kit_manifest:01",
            "string:supervisor_cursor:01",
            "balsa_edge:superpermutation_frame:01",
            "dice:probability_boundary:01",
            "playing_card:permutation_operator:01"
        ],
        receipt_tool="receipt_sheet:supervisor:01",
        colors_needed=["red", "green", "blue", "white", "black", "clear", "grey_gradient", "neon"],
        complexity_tier=ComplexityTier.FULL_KIT,
    ),
}


def get_working_subset(paper_id: str) -> WorkingSubset:
    """Extract the exact-fit working subset for a paper."""
    if paper_id not in PAPER_SUBSETS:
        raise ValueError(f"Unknown paper: {paper_id}. Known: {sorted(PAPER_SUBSETS.keys())}")
    return PAPER_SUBSETS[paper_id]


def validate_exact_fit(subset: WorkingSubset) -> Tuple[bool, str]:
    """
    Check if subset is properly fitted to its complexity tier.
    
    Exact-fit means: tool count falls within the typical range for the tier.
    """
    in_range = subset.in_typical_range()
    tier = subset.complexity_tier
    r = tier.typical_range()
    
    if not in_range:
        return False, (
            f"Misfit: {subset.total_tools()} tools for {tier.name} "
            f"(typical range: {r.start}–{r.stop-1}). "
            f"Either tier is misclassified or subset needs adjustment."
        )
    return True, f"Exact fit: {subset.total_tools()} tools for {tier.name}"


def print_subset_for_paper(paper_id: str):
    """Print the working subset for a paper with exact-fit validation."""
    subset = get_working_subset(paper_id)
    valid, msg = validate_exact_fit(subset)
    print(f"\n{paper_id} Working Subset:")
    print("=" * 70)
    print(subset.summary())
    print("=" * 70)
    print(f"Exact-fit validation: {msg}")
    if not valid:
        print("⚠ MISFIT: Adjust tier or tool count.")


def extract_kit_objects_for_subset(subset: WorkingSubset, full_kit: dict) -> List[dict]:
    """Extract only the objects actually needed from the full kit."""
    needed = []
    
    # Primary tool
    for obj in full_kit["objects"]:
        if obj["object_id"] == subset.primary_tool:
            needed.append(obj)
            break
    
    # Support tools (allow partial matches for dynamic tool IDs like bead:02, bead:03...)
    for tool_id in subset.support_tools:
        if ':' in tool_id and tool_id.count(':') == 2:
            prefix = tool_id.rsplit(':', 1)[0]  # "token:bead"
            for obj in full_kit["objects"]:
                if obj["object_id"].startswith(prefix + ':') or obj["object_id"] == tool_id:
                    if obj not in needed:
                        needed.append(obj)
                    break
        else:
            for obj in full_kit["objects"]:
                if obj["object_id"] == tool_id:
                    needed.append(obj)
                    break
    
    # Receipt tool
    for obj in full_kit["objects"]:
        if obj["object_id"] == subset.receipt_tool:
            needed.append(obj)
            break
    
    return needed


if __name__ == "__main__":
    print("Working Subset Extractor - Exact-Fit Principle")
    print("=" * 70)
    print("Full kit: 1,024 objects (what you OWN)")
    print("Working subset: exactly what the problem needs (what you USE)")
    print("=" * 70)
    
    for paper_id in sorted(PAPER_SUBSETS.keys()):
        print_subset_for_paper(paper_id)
