"""Small, dependency-free domain contracts for reproducible design records."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from typing import Any


class EvidenceKind(StrEnum):
    EXPERIMENTAL = "experimental"
    DATABASE = "database"
    LITERATURE = "literature"
    MODEL_PREDICTION = "model_prediction"
    STRUCTURE_CALCULATION = "structure_calculation"
    AGENT_INFERENCE = "agent_inference"


def _require(value: str, field_name: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} must not be empty")
    return value


@dataclass(frozen=True)
class Target:
    target_id: str
    name: str
    organism: str | None = None
    sequence: str | None = None
    structure_ref: str | None = None
    structure_kind: str | None = None

    def __post_init__(self) -> None:
        _require(self.target_id, "target_id")
        _require(self.name, "name")
        if self.structure_kind and self.structure_kind not in {"experimental", "predicted"}:
            raise ValueError("structure_kind must be experimental or predicted")


@dataclass(frozen=True)
class Molecule:
    molecule_id: str
    smiles: str
    source: str
    parent_id: str | None = None
    generation_method: str | None = None

    def __post_init__(self) -> None:
        _require(self.molecule_id, "molecule_id")
        _require(self.smiles, "smiles")
        _require(self.source, "source")
        if any(char.isspace() for char in self.smiles):
            raise ValueError("smiles must not contain whitespace")


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    kind: EvidenceKind
    source: str
    claim: str
    locator: str | None = None
    status: str = "unreviewed"

    def __post_init__(self) -> None:
        _require(self.evidence_id, "evidence_id")
        _require(self.source, "source")
        _require(self.claim, "claim")


@dataclass(frozen=True)
class AnalysisRun:
    run_id: str
    tool: str
    version: str
    input_hash: str
    parameters: dict[str, Any] = field(default_factory=dict)
    status: str = "completed"

    def __post_init__(self) -> None:
        _require(self.run_id, "run_id")
        _require(self.tool, "tool")
        _require(self.version, "version")
        _require(self.input_hash, "input_hash")


@dataclass(frozen=True)
class CandidateDecision:
    molecule_id: str
    decision: str
    reasons: tuple[str, ...] = ()
    evidence_ids: tuple[str, ...] = ()
    analysis_run_ids: tuple[str, ...] = ()
    uncertainty: str | None = None

    def __post_init__(self) -> None:
        _require(self.molecule_id, "molecule_id")
        if self.decision not in {"include", "exclude", "review"}:
            raise ValueError("decision must be include, exclude, or review")


def to_dict(value: Any) -> dict[str, Any]:
    """Serialize a contract without hiding provenance fields."""

    result = asdict(value)
    for key, item in list(result.items()):
        if isinstance(item, StrEnum):
            result[key] = item.value
    return result

