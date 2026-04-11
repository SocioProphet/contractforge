# ContractForge Repo Role

## Canonical role

`contractforge` is the canonical SocioProphet repository for **contract lifecycle, contractual economics, settlement semantics, adjustments, reversals, restatements, and ledger-anchored finalization**.

This repository should be treated as the primary home for:

- contract-domain architecture
- contract-domain schemas and examples
- economic artifact definitions
- temporal and correction policy
- contract authoring / validation / planning concepts
- contract-domain execution and finalization concepts
- dispute and explanation surfaces for contractual outcomes

## Relationship to adjacent repositories

### Workspace control
`SocioProphet/sociosphere` remains the canonical workspace controller. It owns repo topology, manifest/lock state, registry, and workspace policy. `contractforge` should be registered there, but it must not absorb workspace-control responsibilities.

### Runtime and deployment
`SocioProphet/prophet-platform` remains the runtime and deployment hub. If ContractForge services are implemented, deployment topology and platform runtime concerns belong there, not here.

### Policy
`SocioProphet/policy-fabric` remains the policy-as-code and policy-control repository. ContractForge may consume policy or publish contract-policy integration notes, but it does not replace Policy Fabric.

### Standards
`SocioProphet/socioprophet-standards-storage` remains the upstream standards and decision package for cross-repo storage, contracts, and measurement guidance. ContractForge can publish broader standards upstream when they become platform-wide.

### Ontology and semantics
`SocioProphet/ontogenesis` and `SocioProphet/socioprophet-standards-knowledge` remain the semantic and ontology companions. ContractForge may reference them, but does not subsume their role.

## Anti-goals

ContractForge should not become:

- a generic policy repo
- a generic standards repo
- a generic ontology repo
- a public-surface marketing/docs umbrella
- a workspace controller
- a platform deployment monorepo

## Placement test

A change belongs in ContractForge when the primary question is:

- how a contract is defined, amended, interpreted, executed, adjusted, finalized, or disputed.

A change probably does **not** belong here when the primary question is:

- how the whole workspace is governed,
- how all platform services are deployed,
- how generic policy is authored,
- or how generic ontology/knowledge structures are published.
