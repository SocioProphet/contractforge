# Boundary Interfaces

This document records the explicit interfaces between ContractForge and adjacent SocioProphet repositories.

## 1. Sociosphere ↔ ContractForge

### Direction
- `sociosphere` governs and registers `contractforge`.
- `contractforge` does not own workspace topology or manifest state.

### Interface expectations
- repo registration in the canonical workspace registry
- repo role metadata
- workspace inclusion policy
- CI/ownership expectations inherited from the workspace controller

## 2. Policy Fabric ↔ ContractForge

### Direction
- Policy Fabric provides policy overlays and governance constraints.
- ContractForge consumes or references policy where contract handling requires it.

### Example boundaries
- approval policy for contract release
- data handling policy for settlement evidence
- release gating policy for finalized commitments

### Non-boundary
Policy Fabric does not become the canonical home of contractual economics.

## 3. Standards Storage ↔ ContractForge

### Direction
- Standards Storage owns broader cross-repo standards.
- ContractForge owns the product/domain implementation and repo-local canon.

### Example boundaries
- ContractForge may publish generalized contract schemas or benchmark methodology upstream when they become wider platform standards.
- Repo-local product semantics stay in ContractForge unless explicitly promoted.

## 4. Prophet Platform ↔ ContractForge

### Direction
- Prophet Platform hosts runtime/deployment topology.
- ContractForge defines the contract-domain runtime and artifact model.

### Example boundaries
- deployable APIs and services may eventually live in Prophet Platform
- canonical domain semantics remain in ContractForge

## 5. Ontogenesis / Standards Knowledge ↔ ContractForge

### Direction
- ontology and semantic publication live upstream in their respective semantic repos
- ContractForge may define domain vocabulary and export semantic companions when needed

### Example boundaries
- obligation ontology
- contract actor ontology
- settlement explanation vocabulary

## 6. Public Surface Repos ↔ ContractForge

Public-facing site/docs repos can publish operator and customer-facing documentation about ContractForge, but they do not become the canonical source for the platform itself.

## Design rule

When in doubt:
- domain canon stays in ContractForge,
- workspace canon stays in Sociosphere,
- policy canon stays in Policy Fabric,
- broad standards canon stays in Standards Storage,
- runtime/deployment canon stays in Prophet Platform.
