# Contract Intelligence Evaluations

## Purpose

This document defines the initial evaluation posture for ContractForge contract intelligence.

The evaluation surface must measure more than raw extraction accuracy. It must also test routing, structure, ambiguity handling, replayability, and governance behavior.

## Evaluation families

### 1. Profile resolution

Measures correctness of routing across:

- language
- jurisdiction / region
- domain
- subdomain
- schema pack selection
- pattern pack selection
- model pack selection

### 2. Structural parsing

Measures correctness of:

- section extraction
- clause segmentation
- definition detection
- schedule / exhibit detection
- cross-reference detection
- table recognition
- amendment reference detection

### 3. Semantic extraction

Measures correctness of:

- obligation extraction
- prohibition extraction
- rights extraction
- exception capture
- condition capture
- trigger capture
- timeframe extraction
- actor / counterparty / beneficiary extraction
- defined-term dependency resolution

### 4. Ambiguity handling

Measures whether the system correctly surfaces:

- contradictory clauses
- multiple plausible interpretations
- unresolved references
- low-confidence outputs requiring review

### 5. Replay and governance

Measures:

- deterministic or bounded-repeat replay behavior
- idempotent command behavior where applicable
- event emission completeness
- feedback application correctness
- pack-promotion control behavior

## Recommended benchmark slices

At minimum, the benchmark corpus should include slices for:

- modal obligations (`shall`, `must`, `will`)
- prohibitions (`shall not`, `may not`, `must not`)
- conditional clauses (`if`, `unless`, `provided that`)
- temporal clauses (`within 30 days`, `effective on`, `annually`)
- amendment chains
- cross-reference-heavy clauses
- definition-dependent clauses
- tables and schedules
- OCR or formatting damage
- deliberate ambiguity and contradiction cases

## Evaluation artifacts

The evaluation layer should produce:

- benchmark cases
- benchmark suites
- evaluation reports
- regression comparison reports
- promotion recommendations

## Error buckets

Evaluation reports should bucket failures at least into:

- routing failure
- structure boundary failure
- clause typing failure
- semantic role failure
- exception/condition loss
- timeframe loss
- ambiguity suppression
- provenance/explanation failure
- replay divergence

## Promotion posture

Pattern packs and model packs MUST be promoted independently.

A regression in rule-driven extraction is not equivalent to a regression in learned-model behavior.

## Minimal initial metrics

### Routing metrics

- accuracy by profile dimension
- confusion matrix by domain/subdomain

### Structural metrics

- span overlap / boundary F1
- clause typing accuracy
- cross-reference extraction accuracy

### Semantic metrics

- exact-match and partial-match F1 for actor/action/object
- obligation / prohibition / right classification accuracy
- exception and condition recall
- timeframe extraction accuracy

### Governance metrics

- replay consistency rate
- feedback propagation correctness
- event emission completeness

## Reviewer integration

The benchmark process should support reviewer adjudication for:

- ambiguous cases
- low-confidence cases
- disagreements between pattern-pack and model-pack outputs

## Initial recommendation

ContractForge should treat evaluations as a first-class product surface and maintain:

- benchmark fixtures
- regression baselines
- comparison reports per pack version
- explicit promotion criteria

## Status

This document defines **v0.1** of the ContractForge contract-intelligence evaluation posture.