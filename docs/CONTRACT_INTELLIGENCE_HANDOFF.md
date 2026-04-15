# Contract Intelligence Handoff

## Purpose

This document captures the current contract-intelligence build state across repositories so the work is portable without relying on chat history.

## Canonical repository roles

### `SocioProphet/contractforge`

Owns:

- contract-domain canon
- parser architecture
- contract-domain schema family
- pattern-pack examples and domain-facing examples

### `SocioProphet/socioprophet-standards-storage`

Owns:

- cross-repo interface standard
- JSON schema families for shared structural contracts
- Avro wire-adjacent payload contracts for TriTRPC Path-A posture
- benchmark workloads and benchmark fixtures

### `SocioProphet/api-contracts`

Owns:

- developer-facing / compatibility transport IDLs
- shared application-facing service package definitions

### `SocioProphet/TriTRPC`

Owns:

- normative transport / wire protocol posture
- fixture determinism and transport verification

## Frozen naming

- family: `contract_intelligence`
- protobuf package: `socioprophet.contract_intelligence.v1`
- logical services:
  - `ContractIntelligenceService`
  - `ContractIntelligenceQueryService`
  - `ContractIntelligenceEvaluationService`

## Landed files in ContractForge

### Docs

- `docs/CONTRACT_INTELLIGENCE_MODEL.md`
- `docs/CONTRACT_PARSER_ARCHITECTURE.md`
- `docs/CONTRACT_INTELLIGENCE_HANDOFF.md`

### Contract-domain schemas

- `schemas/contract-domain/contract-clause.schema.json`
- `schemas/contract-domain/contract-obligation.schema.json`
- `schemas/contract-domain/contract-right.schema.json`
- `schemas/contract-domain/contract-prohibition.schema.json`
- `schemas/contract-domain/contract-exception.schema.json`
- `schemas/contract-domain/contract-term-window.schema.json`
- `schemas/contract-domain/contract-interpretation-evidence.schema.json`
- `schemas/contract-domain/contract-pattern-pack.schema.json`

### Example pattern packs

- `examples/pattern-packs/privacy-data-processing-v0.1.json`

## Landed files in Standards Storage

### Interface standard

- `docs/standards/interfaces/tritrpc-contract-intelligence.md`

### JSON schemas

- `schemas/json/contract-intelligence/document-artifact.schema.json`
- `schemas/json/contract-intelligence/profile-resolution.schema.json`
- `schemas/json/contract-intelligence/reviewer-feedback.schema.json`
- `schemas/json/contract-intelligence/benchmark-case.schema.json`
- `schemas/json/contract-intelligence/evaluation-report.schema.json`

### Avro schemas

- `schemas/avro/contract-intelligence/document-artifact.avsc`
- `schemas/avro/contract-intelligence/profile-resolution.avsc`
- `schemas/avro/contract-intelligence/contract-clause.avsc`
- `schemas/avro/contract-intelligence/contract-obligation.avsc`
- `schemas/avro/contract-intelligence/reviewer-feedback.avsc`
- `schemas/avro/contract-intelligence/benchmark-case.avsc`
- `schemas/avro/contract-intelligence/evaluation-report.avsc`

### Benchmarks and fixtures

- `benchmarks/workloads/contract-intelligence-routing.yaml`
- `benchmarks/workloads/contract-intelligence-extraction.yaml`
- `benchmarks/fixtures/contract-intelligence/privacy-data-processing-case-001.txt`
- `benchmarks/fixtures/contract-intelligence/privacy-data-processing-case-001.json`

## Landed files in API Contracts

- `proto/socioprophet/contract_intelligence/v1/types.proto`
- `proto/socioprophet/contract_intelligence/v1/service.proto`
- `proto/socioprophet/contract_intelligence/v1/query.proto`
- `proto/socioprophet/contract_intelligence/v1/evaluation.proto`

## Architectural decisions captured

1. **Contract intelligence is staged**.
   Parsing is not a single opaque pass. It is modeled over source artifacts, profile resolution, structural extraction, semantic extraction, interpretation evidence, and downstream projection.

2. **Routing is first-class**.
   Language, jurisdiction, domain, subdomain, and pack selection are explicit artifacts and benchmarked surfaces.

3. **TriTRPC is the transport authority**.
   The stable transport/wire posture is upstream in `SocioProphet/TriTRPC`.

4. **Avro is the wire-adjacent Path-A payload posture**.
   The Avro family in standards storage is the canonical wire-adjacent payload set for contract intelligence.

5. **Protobuf is compatibility-facing unless proven otherwise**.
   The `api-contracts` protobuf files are useful, but they should be reconciled against the Avro/JSON canonical contracts instead of treated as an independent truth surface.

6. **Pattern packs and model packs are distinct**.
   They must be versioned and benchmarked separately.

7. **Ambiguity is first-class**.
   The system must support ambiguous, conflicting, or underdetermined interpretations instead of forcing a single answer.

## Known remaining gap

The main remaining normalization gap is the compatibility layer in `SocioProphet/api-contracts`.

The protobuf files exist, but they still require a deliberate reconciliation pass against:

- the interface standard in standards storage,
- the canonical JSON contracts,
- the Avro wire-adjacent payload contracts aligned to TriTRPC Path-A.

## Recommended completion checklist

A repo-level completion pass should verify:

- JSON schema family present and coherent
- Avro family present for transport-critical payloads
- benchmark workloads present
- at least one golden lane fixture present
- protobuf compatibility layer reconciled
- TriTRPC linkage explicitly documented
- generated bindings / build verification run where applicable

## Current status

This handoff captures the current state sufficiently that chat history is no longer required to understand:

- ownership boundaries,
- canonical naming,
- landed schemas,
- benchmark posture,
- and the remaining transport normalization task.
