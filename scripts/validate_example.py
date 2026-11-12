"""Validate the public example without external services or model weights."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from targetlens.contracts import Molecule, Target
from targetlens.planner import DesignTask, build_plan


def main() -> None:
    payload = json.loads((ROOT / "examples/minimal_task.json").read_text(encoding="utf-8"))
    target = Target(**payload["target"])
    molecules = tuple(Molecule(**item) for item in payload["molecules"])
    plan = build_plan(DesignTask(target, molecules, payload["objective"]))
    print("TargetLens example is valid")
    print(" -> ".join(plan))


if __name__ == "__main__":
    main()

