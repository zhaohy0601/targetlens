from targetlens.contracts import Evidence, EvidenceKind, Molecule, Target
from targetlens.planner import DesignTask, build_plan


def test_target_and_molecule_contracts_keep_provenance_fields() -> None:
    target = Target("t1", "Example target", structure_kind="predicted")
    molecule = Molecule("m1", "CCO", "fixture")
    plan = build_plan(DesignTask(target, (molecule,)))

    assert target.structure_kind == "predicted"
    assert molecule.source == "fixture"
    assert plan[0] == "normalize_target"
    assert "evaluate_structure_compatibility" in plan


def test_evidence_kind_is_explicit() -> None:
    evidence = Evidence("e1", EvidenceKind.STRUCTURE_CALCULATION, "tool:v1", "pose score")
    assert evidence.kind.value == "structure_calculation"


def test_invalid_smiles_fixture_is_rejected() -> None:
    try:
        Molecule("m1", "C C", "fixture")
    except ValueError as error:
        assert "whitespace" in str(error)
    else:
        raise AssertionError("invalid SMILES fixture was accepted")

