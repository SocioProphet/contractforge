# Temporal and Correction Policy

## Purpose

This document defines the temporal and correction policies for ContractForge. It governs how time, corrections, adjustments, restatements, and finalization interact throughout the settlement lifecycle.

## Time Dimensions

Each economic artifact in ContractForge is governed by multiple time dimensions:

- **Event Time** — when the source event occurred.
- **Ingest Time** — when the platform first received the event.
- **Effective Time** — when contractual terms actually apply.
- **Processing Time** — when a computation or validation was performed.
- **Finalization Time** — when a settlement artifact became sealed and official.

These must be treated as distinct. No single timestamp is sufficient to model contractual economics correctly.

## Period Close Rules

A settlement period may be:

- **Open** — new lines and adjustments may still be added.
- **Review** — candidate lines are under validation or approval.
- **Finalized** — batch membership is sealed.
- **Committed** — finalized batch has been anchored or otherwise formally recorded.

A finalized period must not be rewritten in place.

## Correction Modes

Corrections must use one of the following modes:

1. **Adjustment-forward**
   - Keep the original approved/finalized artifacts intact.
   - Issue new adjustment lines in a subsequent batch.
2. **Restatement cycle**
   - Create a new batch cycle for the same period.
   - Preserve the prior batch as historical fact.
3. **Prohibited correction**
   - Certain periods or commitments may forbid restatement entirely and require only external annotation or downstream financial handling.

## Default policy

The default ContractForge posture is:

- append-only artifacts,
- no in-place economic mutation after approval/finalization,
- corrections through explicit adjustment lines unless a restatement policy is explicitly permitted.

## Amendment interaction

Contract amendments may be:

- prospective,
- effective for a bounded historical window,
- or prohibited from retroactive effect.

Retroactive amendments must declare whether they produce:
- adjustment-forward behavior, or
- a formal restatement cycle.

## Reopen policy

Reopening a closed or finalized period should be rare and explicit.

If reopen is allowed:
- it must create a new cycle or controlled correction lane,
- it must preserve historical batch identity,
- and it must produce an auditable explanation trail.

## Ledger interaction

If a batch is already committed to a ledger:
- the original commitment remains historical fact,
- corrections create new adjustments or a new restatement batch,
- a new commitment record must reference the corrected cycle.

## Summary

ContractForge treats time as multi-dimensional and corrections as explicit, append-only economic actions. The platform should prefer adjustment-forward behavior, preserve finalization boundaries, and avoid rewriting history.