# ContractForge Architecture

## Purpose

ContractForge is the canonical repository for contractual economics in the SocioProphet stack.

Its job is to define and eventually implement the layers required to move from:

1. contractual terms,
2. source events and evidence,
3. governed computation,
4. approval and exception handling,
5. finalized settlement artifacts,
6. and optional ledger anchoring.

## Placement in the wider stack

### Upstream / adjacent repos

- **SocioProphet/sociosphere**
  - workspace controller and canonical repo-role governance
  - owns manifest, lock, topology, and workspace policy
- **SocioProphet/policy-fabric**
  - policy authoring and policy-as-code governance
  - may constrain contract approval, release, and handling behavior
- **SocioProphet/socioprophet-standards-storage**
  - cross-repo standards authority for storage, data contracts, and measurement
  - ContractForge may publish normative cross-repo standards there when they are broader than this repo
- **SocioProphet/prophet-platform**
  - runtime and deployment hub
  - eventual host for ContractForge services where appropriate
- **SocioProphet/ontogenesis** and **SocioProphet/socioprophet-standards-knowledge**
  - semantic and ontology companion lanes

## Internal architecture layers

### 1. Domain model layer
Defines:
- contracts
- amendments
- obligations
- charge families
- periods
- approvals
- adjustments
- commitments

### 2. Economic artifact layer
Defines canonical artifacts such as:
- source events
- enriched events
- candidate settlement lines
- approved settlement lines
- adjustment lines
- settlement batches
- commitment records

### 3. Temporal and correction layer
Defines:
- event time
- ingest time
- effective time
- processing time
- finalization time
- reopen, restatement, and adjustment policy

### 4. Authoring / compiler layer
Expected future ownership:
- contract-aware rule and lifecycle authoring
- linting
- explain plans
- planning and execution preparation

### 5. Execution / finalization layer
Expected future ownership:
- batch or microbatch settlement execution
- exception handling and approval pathways
- batch sealing and control totals
- optional ledger anchoring

## Non-goals

This repository is not intended to become:
- a generic workspace controller
- a generic policy system
- a generic ontology warehouse
- a generic platform deployment repo

## Initial implementation posture

The first work in this repository should be specification-first:

1. architecture
2. boundaries
3. economic artifact model
4. temporal and correction policy
5. schema families
6. then code
