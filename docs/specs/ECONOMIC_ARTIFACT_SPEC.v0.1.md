# Economic Artifact Spec v0.1

## Purpose

This specification defines the canonical economic artifacts for ContractForge.

The objective is to separate:
- source truth,
- derived settlement candidates,
- approved economic truth,
- corrective deltas,
- finalized batch state,
- and ledger commitments.

This repository treats those as distinct artifact classes. They are not interchangeable.

## Platform principles

1. **Append-only economics**
   - economic history is not rewritten after approval/finalization
   - corrections create new artifacts
2. **Deterministic identity**
   - every economically meaningful artifact should have a stable deterministic ID strategy
3. **Separated lifecycle stages**
   - compute, review, approve, finalize, and commit are distinct stages
4. **Explicit temporal semantics**
   - event time, ingest time, effective time, processing time, and finalized time are separate fields
5. **Commitment after finalization**
   - ledger anchoring attests to finalized batches; it is not the execution engine

## Canonical artifact set

### 1. SourceEvent
Raw upstream business event.

Examples:
- shipment delivered
- service dispatch completed
- usage record emitted
- entitlement consumed

Minimum fields:
- `source_event_id`
- `tenant_id`
- `source_system`
- `source_natural_key`
- `source_version`
- `event_time`
- `ingest_time`
- `payload_raw`
- `payload_normalized`
- `status`

Expected status values:
- `INGESTED`
- `REJECTED`
- `SUPERSEDED`

Deterministic identity guidance:
- hash of tenant + source system + natural key + source version

### 2. EnrichedEvent
Derived event after contract/domain enrichment.

Purpose:
- attach contract candidates
- attach dimensions and eligibility context
- preserve enrichment trace

Minimum fields:
- `enriched_event_id`
- `source_event_id`
- `effective_time`
- `contract_candidate_ids`
- `enrichment_trace`
- `status`

Expected status values:
- `ENRICHED`
- `INVALID`
- `SUPERSEDED`

### 3. Contract
Canonical agreement object.

Minimum fields:
- `contract_id`
- `tenant_id`
- `counterparty_id`
- `contract_type`
- `status`
- `effective_start`
- `effective_end`
- `governing_metadata`

Expected status values:
- `DRAFT`
- `ACTIVE`
- `SUSPENDED`
- `EXPIRED`
- `TERMINATED`

### 4. ContractAmendment
Versioned contract delta.

Minimum fields:
- `amendment_id`
- `contract_id`
- `amendment_seq`
- `effective_start`
- `effective_end`
- `retroactive_policy`
- `payload`
- `status`

Expected status values:
- `PROPOSED`
- `APPROVED`
- `WITHDRAWN`

### 5. RulesetVersion
Canonical executable or semi-executable rules version used during evaluation.

Minimum fields:
- `ruleset_version_id`
- `contract_id` or template binding
- `rules_text_hash`
- `mapping_manifest_hash`
- `schema_version_refs`
- `planner_version`
- `status`

Expected status values:
- `DRAFT`
- `RELEASE_CANDIDATE`
- `RELEASED`
- `DEPRECATED`

### 6. CandidateSettlementLine
Computed but not yet authoritative economic line.

Minimum fields:
- `candidate_line_id`
- `tenant_id`
- `contract_id`
- `ruleset_version_id`
- `charge_code`
- `charge_period_id`
- `source_event_refs`
- `quantity`
- `unit`
- `rate`
- `amount`
- `currency`
- `calculation_trace`
- `status`

Expected status values:
- `COMPUTED`
- `EXCEPTIONED`
- `SUPERSEDED`
- `VOIDED`

### 7. ReviewDecision
Approval / reject / override artifact.

Minimum fields:
- `review_decision_id`
- `candidate_line_id`
- `decision_seq`
- `decision_type`
- `override_fields`
- `reason_code`
- `decided_by`
- `decision_time`
- `status`

Expected status values:
- `RECORDED`
- `SUPERSEDED`

### 8. ApprovedSettlementLine
Authoritative settlement line.

Minimum fields:
- `approved_line_id`
- `candidate_line_id`
- `contract_id`
- `charge_code`
- `charge_period_id`
- `amount`
- `currency`
- `approval_trace`
- `status`

Expected status values:
- `APPROVED`
- `INCLUDED_IN_BATCH`
- `ADJUSTED`
- `VOIDED`

### 9. AdjustmentLine
Append-only corrective artifact.

Minimum fields:
- `adjustment_line_id`
- `adjustment_type`
- `target_ref`
- `amount`
- `currency`
- `reason_code`
- `created_by`
- `created_time`
- `status`

Expected status values:
- `ISSUED`
- `INCLUDED_IN_BATCH`
- `VOIDED`

Adjustment types should be constrained to a controlled set such as:
- `CREDIT`
- `DEBIT`
- `REVERSAL`
- `RECLASS`
- `TAX_CORRECTION`
- `FX_CORRECTION`

### 10. SettlementBatch
Sealed grouping for approval/finalization/export/commit.

Minimum fields:
- `batch_id`
- `tenant_id`
- `contract_id`
- `window_start`
- `window_end`
- `cycle_seq`
- `line_manifest_hash`
- `control_totals`
- `status`

Expected status values:
- `OPEN`
- `REVIEW`
- `FINALIZED`
- `COMMITTED`
- `EXPORTED`
- `CLOSED`

### 11. CommitmentRecord
Ledger or notarization artifact for a finalized batch.

Minimum fields:
- `commitment_id`
- `batch_id`
- `commitment_root_hash`
- `commitment_algorithm_version`
- `canonicalization_version`
- `ledger_id`
- `receipt_ref`
- `status`

Expected status values:
- `PENDING`
- `CONFIRMED`
- `FAILED`
- `SUPERSEDED`

### 12. ReconciliationRecord
Control-total and completeness artifact.

Minimum fields:
- `reconciliation_id`
- `reconciliation_type`
- `window_start`
- `window_end`
- `expected_count`
- `observed_count`
- `expected_amounts`
- `observed_amounts`
- `status`

Expected status values:
- `PASS`
- `WARN`
- `FAIL`

## Core lineage

```text
SourceEvent
  -> EnrichedEvent
  -> CandidateSettlementLine
  -> ReviewDecision
  -> ApprovedSettlementLine
  -> SettlementBatch
  -> CommitmentRecord
```

Correction lineage:

```text
ApprovedSettlementLine
  -> AdjustmentLine
  -> SettlementBatch (next cycle or next period)
  -> CommitmentRecord
```

## Invariants

1. A finalized batch is immutable in membership.
2. Commitment attaches to a specific finalized batch/cycle.
3. Approved economic truth is not rewritten in place after inclusion in a finalized batch.
4. Corrections must create explicit economic artifacts.
5. Every approved line must be traceable back to source events, ruleset version, and review/approval context.
6. Deterministic IDs should be derivable without hidden local state.
7. Multi-currency totals must not be silently co-mingled.

## Hash / proof coverage guidance

The minimum proof-bearing chain should cover:
- canonical projection of approved settlement lines
- canonical projection of adjustment lines
- batch manifest hash / Merkle root
- commitment record linking that root to the chosen ledger/notarization surface

## Relationship to schemas

The first schema tranche should cover at least:
- contract
- contract amendment
- candidate settlement line
- approved settlement line
- adjustment line
- settlement batch
