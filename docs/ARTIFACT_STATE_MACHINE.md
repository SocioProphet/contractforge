# Artifact State Machine

This document defines the first-pass state machine for ContractForge economic artifacts.

## Core flow

```text
SourceEvent
  -> EnrichedEvent
  -> CandidateSettlementLine
  -> ReviewDecision
  -> ApprovedSettlementLine
  -> SettlementBatch
  -> CommitmentRecord
```

## SourceEvent

States:
- `INGESTED`
- `REJECTED`
- `SUPERSEDED`

Rules:
- source corrections produce a new event version rather than mutating an existing event in place

## EnrichedEvent

States:
- `ENRICHED`
- `INVALID`
- `SUPERSEDED`

Rules:
- enrichment is derived state and may be recomputed when inputs or reference data change

## CandidateSettlementLine

States:
- `COMPUTED`
- `EXCEPTIONED`
- `SUPERSEDED`
- `VOIDED`

Rules:
- candidate lines are not authoritative economic truth
- they may be replaced by later recomputation before approval/finalization

## ReviewDecision

States:
- `RECORDED`
- `SUPERSEDED`

Rules:
- review/override logic should not mutate candidate line economics directly; it should produce explicit review artifacts

## ApprovedSettlementLine

States:
- `APPROVED`
- `INCLUDED_IN_BATCH`
- `ADJUSTED`
- `VOIDED`

Rules:
- once included in a finalized batch, the line must not be rewritten in place
- later corrections happen through explicit adjustment or restatement behavior

## AdjustmentLine

States:
- `ISSUED`
- `INCLUDED_IN_BATCH`
- `VOIDED`

Rules:
- adjustment lines are append-only correction artifacts

## SettlementBatch

States:
- `OPEN`
- `REVIEW`
- `FINALIZED`
- `COMMITTED`
- `EXPORTED`
- `CLOSED`

Rules:
- batch membership may change only before finalization
- once finalized, membership is sealed
- if later correction is required, create adjustment-forward behavior or a new batch cycle

## CommitmentRecord

States:
- `PENDING`
- `CONFIRMED`
- `FAILED`
- `SUPERSEDED`

Rules:
- commitment records represent notarization/anchoring, not business-logic execution
- a committed batch remains historical fact even when a later correcting batch exists

## Default global invariant

ContractForge prefers:
- append-only economic history,
- explicit adjustments,
- explicit restatement cycles,
- and no in-place mutation of finalized economic truth.
