# Economic Artifact Spec

## Purpose

This document defines the canonical **economic artifact model** for contract lifecycle, settlement, and ledger anchoring. It sets the structure for representing contractual events, obligations, amendments, settlements, adjustments, reversals, and finalization.

## Economic Artifacts

1. **SourceEvent**
   - Raw, upstream business events like service completion or item dispatch. Defines a natural key and timestamp.
2. **EnrichedEvent**
   - Source events enriched with contract data (e.g., customer, terms) for validation.
3. **Contract**
   - A formal agreement, containing obligations, terms, and effective dates.
4. **CandidateSettlementLine**
   - A proposed settlement record before approval or finalization.
5. **ApprovedSettlementLine**
   - An approved settlement record that can be invoiced or recorded.
6. **AdjustmentLine**
   - Corrections or changes to previously approved settlement lines.
7. **SettlementBatch**
   - A batch of finalized settlement lines, marked for ledger anchoring.
8. **CommitmentRecord**
   - Final, anchored record of a settlement batch committed to the ledger.

## Artifact Relationships

These artifacts flow through the system as follows:

- **SourceEvent** → **EnrichedEvent** → **CandidateSettlementLine** → **ApprovedSettlementLine** → **SettlementBatch** → **CommitmentRecord**.

The adjustment flow is a corrective loop:

- **ApprovedSettlementLine** → **AdjustmentLine** → **ApprovedSettlementLine**.

## Temporal and Versioning Rules

- Every artifact is time-bound with an `event_time`, `ingest_time`, `effective_time`, and `processing_time`.
- **Versioning** is handled through amendments or adjustments. Artifacts are not rewritten; instead, new versions are created (e.g., `SourceEvent v2` for corrected data).

## Summary

This document defines how economic artifacts are structured, their temporal semantics, and how they interact with each other in the settlement lifecycle.

## Next Steps

- Implement the model in code.
- Integrate with existing services in the SocioProphet stack (e.g., `sociosphere`, `prophet-platform`).