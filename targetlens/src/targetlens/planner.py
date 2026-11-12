"""Offline task planner used before real model and scientific tool adapters exist."""

from __future__ import annotations

from dataclasses import dataclass

from .contracts import Molecule, Target


@dataclass(frozen=True)
class DesignTask:
    target: Target
    molecules: tuple[Molecule, ...] = ()
    objective: str = "prioritize candidates for a protein target"


def build_plan(task: DesignTask) -> tuple[str, ...]:
    """Return a deterministic plan; this is not an LLM or scientific prediction."""

    steps = ["normalize_target", "collect_target_evidence"]
    if task.molecules:
        steps.extend(["standardize_candidates", "evaluate_structure_compatibility"])
    else:
        steps.append("retrieve_or_import_candidates")
    steps.extend(["review_literature_and_computational_evidence", "write_decision_record"])
    return tuple(steps)

