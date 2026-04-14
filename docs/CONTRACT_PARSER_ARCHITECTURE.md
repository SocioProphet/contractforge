# Contract Parser Architecture

## Purpose

This document defines the initial architecture for the ContractForge **contract parser**.

The parser is treated as a governed, staged compiler / interpreter over contractual documents rather than as a single opaque extraction pass.

## Architectural goals

The contract parser must:

- preserve replayability over document and pack versions
- separate routing, structure, semantics, and explanation into explicit stages
- support language / jurisdiction / domain / subdomain specialization
- emit evidence-rich artifacts suitable for review and dispute handling
- support both rules/pattern packs and learned model packs
- integrate cleanly with upstream query, command, and evaluation standards

## Non-goals

The parser is not:

- the transport contract authority
- the benchmark authority
- the generic runtime deployment layer
- the generic ontology publication lane

## Processing topology

### Stage A — Ingest and canonicalize

Input formats may include PDF, DOCX, HTML, text, OCR outputs, or upstream artifact references.

Outputs:

- canonical text
- content hash
- normalization log
- structural spans where available
- source provenance references

### Stage B — Resolve processing profile

The parser MUST resolve and persist a processing profile before semantic extraction.

Profile dimensions:

- language
- jurisdiction / region
- domain
- subdomain
- selected schema pack
- selected pattern pack
- selected model pack

This stage is explicit to prevent silent routing drift.

### Stage C — Structural parse

The parser derives an intermediate structural representation containing:

- sections
- clauses
- definitions
- schedules
- exhibits
- tables
- signature blocks
- cross-references
- amendment references

The output of this stage is **StructureIR**.

### Stage D — Semantic extraction

The parser derives a semantic representation containing:

- obligations
- prohibitions
- rights
- conditions
- exceptions
- triggers
- timeframes
- actors / counterparties / beneficiaries
- defined-term dependencies

The output of this stage is **SemanticIR**.

### Stage E — Interpretation evidence

The parser emits explanation and review artifacts such as:

- supporting spans
- contradicting spans
- rule hits
- pattern hits
- model scores
- ambiguity markers
- unresolved references
- reviewer state

The output of this stage is **InterpretationEvidenceIR**.

### Stage F — Downstream projection

When required, semantic artifacts may be projected into downstream ContractForge flows such as:

- settlement-relevant obligations
- effective-window artifacts
- adjustment triggers
- finalization constraints
- approval gates

This stage is downstream of interpretation and must not be conflated with parsing.

## Pack architecture

The parser operates over three independent pack families.

### Schema packs

Schema packs define the structural contracts for parser artifacts.

### Pattern packs

Pattern packs define:

- lexicons
- rule groups
- normalizers
- precedence rules
- routing hints
- extraction templates

Pattern packs are the modern equivalent of domain-specific annotator collections.

### Model packs

Model packs contain learned components used for:

- profile resolution
- structural classification
- semantic extraction
- ranking
- ambiguity handling

Pattern packs and model packs MUST be versioned and evaluated independently.

## Artifact boundaries

The parser should emit distinct artifact families instead of a single mixed payload.

### Structural artifacts

- `ContractClause`
- `ContractDefinition`
- `ContractSchedule`
- `ContractCrossReference`

### Semantic artifacts

- `ContractObligation`
- `ContractRight`
- `ContractProhibition`
- `ContractException`
- `ContractTermWindow`

### Explanation artifacts

- `ContractInterpretationEvidence`
- `ContractReviewRecord`
- `ContractAmbiguityRecord`

## Control-plane and query-plane integration

The parser should integrate with a CQRS-like posture:

- command plane for ingest, parse, extract, feedback, recompute
- query plane for retrieval of artifacts by id/version/profile/story/time window
- evaluation plane for benchmark execution, comparison, replay, and promotion

The canonical shared interfaces are defined upstream.

## Ambiguity handling

Ambiguity is a required feature, not an error condition.

The parser must be able to represent:

- multiple plausible interpretations
- conflicting clauses
- unresolved references
- low-confidence extracts requiring review

## Minimal internal modules

A first implementation should separate these modules:

1. `ingest`
2. `profile_resolver`
3. `structure_parser`
4. `semantic_extractor`
5. `evidence_builder`
6. `feedback_adapter`
7. `benchmark_runner`

## Recommended repository-local deliverables

- parser architecture docs
- contract-domain schema family
- test fixtures for routing, structure, and semantic extraction
- pattern-pack examples by domain/subdomain
- evaluation reports and regression baselines

## Initial implementation order

1. lock architecture and schemas
2. add upstream interface and benchmark contracts
3. add transport bindings
4. land routing fixtures and structural fixtures
5. land semantic extraction fixtures
6. begin runtime implementation

## Status

This document defines **v0.1** of the ContractForge parser architecture.