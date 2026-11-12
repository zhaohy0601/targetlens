# TargetLens Roadmap

## Current release: `0.1.0`

Implemented and locally testable:

- dependency-free domain contracts for targets, molecules, evidence, runs, and candidate decisions;
- provenance-preserving validation rules;
- deterministic offline planning path;
- public example and contract tests.

Not implemented in this release:

- LLM provider integration;
- ESM inference;
- AlphaFold retrieval or structure prediction;
- docking or molecular dynamics;
- virtual screening against a licensed compound collection;
- constrained molecular generation or optimization;
- production API, UI, database, or multi-agent orchestration.

## Research milestones

1. Audit existing ESM, structure, docking, literature, and license assets.
2. Freeze a reproducible target and candidate benchmark.
3. Add real target and molecule adapters with explicit unavailable states.
4. Add one structure-evaluation baseline and report failures.
5. Add one constrained optimization method and compare it with an unmodified baseline.
6. Add a model-backed Agent that chooses tools from real outputs and emits a replayable decision record.
7. Evaluate evidence fidelity, tool selection, candidate ranking, cost, latency, and failure handling.

## Thesis boundary

The thesis may study the Agent workflow, provenance contract, evidence-grounded decision record, and benchmark results. It must not claim that docking or model scores establish experimental affinity, efficacy, safety, or clinical utility.

