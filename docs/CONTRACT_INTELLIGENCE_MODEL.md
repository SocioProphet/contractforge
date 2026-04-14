# Contract Intelligence Model

## Purpose

This document defines the **contract-domain model** for contract intelligence in ContractForge.

It formalizes contract parsing and extraction as a staged **compiler / interpretation pipeline**, rather than a single opaque parser pass.

This model exists to support:

- contract-aware authoring and linting,
- obligation and amendment interpretation,
- evidence-oriented explanation,
- integration with temporal, correction, and finalization semantics,
- future execution and settlement projections where contractual meaning feeds downstream economic artifacts.

---

## Boundary

This document is a **contract-domain canon**.

It does not define platform-wide transport or benchmark authority.
Those concerns belong upstream.

This document also does not attempt to redefine generic ontology, generic policy, or generic deployment wiring.

---

## High-level model

Contract intelligence is modeled as a staged transformation pipeline over versioned artifacts.

The core idea is:

1. ingest a source document,
2. resolve the applicable processing profile,
3. derive structural boundaries,
4. derive contract semantics,
5. attach explanation / evidence,
6. optionally project contract meaning into execution-relevant artifacts.

This staging is deliberate.
It prevents the system from collapsing routing, structure, semantics, and explanation into one opaque score.

---

## Canonical stages

### Stage 0 — SourceDocumentArtifact

Represents the canonicalized source document.

Properties:

- source bytes or stable source reference
- canonical text
- content hash
- normalization log
- layout anchors where available
- document-level metadata

Purpose:

- provides the immutable input base for replay,
- separates ingestion concerns from interpretation concerns.

### Stage 1 — ProfileResolution

Represents the chosen routing decision.

Profile dimensions:

- language
- jurisdiction
- region where needed
- domain
- subdomain
- selected schema pack
- selected pattern pack
- selected model pack

Purpose:

- makes routing a first-class, inspectable artifact,
- supports domain-specific collections similar to historical annotator packs,
- enables explicit benchmark coverage for profile resolution.

### Stage 2 — StructureIR

Represents structural parsing output.

Expected artifact families:

- sections
- clauses
- definitions
- schedules
- exhibits
- tables
- signature blocks
- amendment references
- cross-references

Purpose:

- isolates structural parsing quality from semantic extraction quality,
- provides stable clause and definition anchors for downstream interpretation.

### Stage 3 — SemanticIR

Represents extracted contractual meaning.

Expected semantic outputs:

- obligations
- prohibitions
- rights
- exceptions
- conditions
- triggers
- timeframes
- actors
- counterparties
- beneficiaries
- defined-term dependencies

Purpose:

- expresses contract meaning in machine-tractable form,
- supports downstream reasoning without flattening all interpretation into raw spans.

### Stage 4 — InterpretationEvidenceIR

Represents explanation, ambiguity, and evidence.

Expected fields and concepts:

- supporting spans
- contradicting spans
- rule hits
- pattern hits
- model scores
- ambiguity flags
- unresolved references
- reviewer state

Purpose:

- makes explanation first-class,
- supports dispute-oriented review,
- allows multiple plausible interpretations to be surfaced explicitly.

### Stage 5 — ExecutionProjectionIR

Represents downstream projections of contract meaning into execution-relevant artifacts when needed.

Examples:

- settlement-relevant obligations
- payment or rate application hooks
- effective windows
- adjustment / reversal triggers
- approval requirements
- finalization constraints

Purpose:

- bridges contract interpretation to economic or operational consequences,
- keeps execution projections downstream of interpretation rather than mixed into parsing.

---

## Core domain entities

The following entities are first-class in the contract intelligence model.

### ContractClause

Represents a structurally identified clause or clause-like unit.

Key properties:

- clause id
- document reference
- section path
- clause type
- text span
- cross-reference links
- provenance

### ContractObligation

Represents an extracted obligation.

Key properties:

- obligation id
- clause reference
- obligation type
- actor
- counterparty
- beneficiary
- action
- object
- condition
- exception
- trigger
- timeframe
- effective window
- confidence
- provenance

### ContractRight

Represents an extracted right or entitlement.

Key properties mirror obligations where relevant, but the semantic posture is entitlement rather than required action.

### ContractProhibition

Represents a prohibited action or forbidden state.

### ContractException

Represents a carve-out, override, or narrowing condition affecting another semantic artifact.

### ContractTermWindow

Represents temporal semantics such as:

- effective date
- retroactive window
- expiry
- renewal window
- notice period
- cure period

### ContractInterpretationEvidence

Represents the explanation and evidence surface supporting an extracted semantic artifact.

---

## Pattern packs and model packs

Contract intelligence MUST support independent versioning of:

- schema packs
- pattern packs
- model packs

### Pattern packs

Pattern packs are the modern equivalent of domain-specific annotator collections.
They may contain:

- lexicons
- rule groups
- normalizers
- precedence rules
- extraction templates
- routing hints

Pattern packs SHOULD be specialized by:

- language
- jurisdiction
- domain
- subdomain

### Model packs

Model packs contain learned components used in routing, structure extraction, semantic extraction, ranking, or ambiguity handling.

Pattern packs and model packs MUST be evaluated separately.
A regression in a rule pack is not the same class of failure as a regression in a learned model.

---

## Ambiguity posture

Contracts frequently contain:

- undefined or circular references,
- amendments that modify prior terms partially,
- conflicting clauses,
- scope ambiguity,
- formatting damage,
- schedule/table dependence,
- implicit actor/action relations.

The model MUST therefore support:

- multiple candidate interpretations,
- explicit ambiguity markers,
- unresolved references,
- reviewer adjudication.

A compliant implementation SHOULD NOT force a single answer when the evidence supports multiple plausible readings.

---

## Relationship to ContractForge architecture

This model aligns to the internal ContractForge layers as follows:

- **Domain model layer**: clauses, obligations, rights, prohibitions, term windows
- **Economic artifact layer**: downstream execution projections where contractual meaning affects settlement artifacts
- **Temporal and correction layer**: effective windows, retroactivity, reopen/restatement implications
- **Authoring / compiler layer**: routing, parsing, linting, explain plans, extraction orchestration
- **Execution / finalization layer**: downstream use of extracted meaning in governed execution flows

---

## Initial schema families implied by this model

The following schema documents SHOULD be created in `schemas/`:

- `contract-clause.schema.json`
- `contract-obligation.schema.json`
- `contract-right.schema.json`
- `contract-prohibition.schema.json`
- `contract-exception.schema.json`
- `contract-term-window.schema.json`
- `contract-interpretation-evidence.schema.json`
- `contract-pattern-pack.schema.json`

---

## Evaluation alignment

The contract intelligence model SHOULD be evaluated against at least the following harness families:

- routing / profile resolution
- structure extraction
- semantic extraction
- ambiguity handling
- replay and idempotency
- governance and feedback propagation
- pack-regression comparison

Recommended benchmark slices include:

- modal obligations
- prohibitions
- conditional clauses
- temporal clauses
- amendment chains
- cross-reference-heavy clauses
- definition-dependent clauses
- tables and schedules
- OCR / formatting damage
- deliberate ambiguity and contradictory interpretation cases

---

## Initial implementation posture

The initial implementation SHOULD be specification-first.

Recommended order:

1. freeze this model,
2. define schema families,
3. define interface and evaluation standards upstream,
4. define typed bindings in shared API-contract repos,
5. only then begin runtime parser/compiler implementation.

---

## Anti-patterns to avoid

- treating all parsing outcomes as one undifferentiated JSON blob
- hiding routing decisions inside opaque model code
- mixing contract-domain canon with platform transport canon
- coupling pattern-pack promotion and model-pack promotion into a single uncontrolled process
- forcing single-answer outputs for genuinely ambiguous clauses
- projecting settlement or execution artifacts before contract meaning is represented explicitly
