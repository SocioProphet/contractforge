# ContractForge Boundaries

This document defines what belongs in ContractForge and what does not.

## Canonical ownership

ContractForge canonically owns:

- contract lifecycle semantics
- amendment and effective-date semantics
- retroactivity, restatement, and adjustment policy
- contractual economic artifacts
- candidate vs approved vs finalized settlement transitions
- contract-domain authoring and validation concepts
- contract-domain execution and finalization concepts
- contract-domain evidence and dispute explanation surfaces

## Explicit non-ownership

### Sociosphere owns
- workspace control
- repo inventory and topology
- workspace manifest/lock
- cross-repo governance metadata

### Policy Fabric owns
- policy authoring and validation for policy-as-code domains
- policy release packs and policy-centric governance workflows

### SocioProphet Standards Storage owns
- platform-wide normative standards that apply across multiple repos
- cross-repo storage / contract / measurement guidance
- benchmark methodology

### Prophet Platform owns
- deployable services and runtime topology
- infrastructure and platform deployment wiring
- platform-level contracts and runtime integration

### Ontogenesis / Standards Knowledge own
- ontology and semantic context packages
- RDF/OWL/JSON-LD and semantic standards work that is broader than this repo

## Placement rules

Place work in ContractForge when the change is primarily about:

- contractual obligations and amendments
- pricing/rates/charge semantics
- settlement artifact lifecycle
- adjustments, reversals, restatements
- close/finalize/commit behavior
- contract-aware authoring, planning, linting, or explanation

Do not place work in ContractForge when the change is primarily about:

- generic policy controls
- generic transport/wire protocol
- generic workspace control
- generic ontology publication
- generic platform deployment
- public website/docs not specific to contract-domain ownership

## Interaction rules

- ContractForge may consume policy from Policy Fabric, but should not re-host Policy Fabric canon.
- ContractForge may consume standards from Standards Storage, but should not duplicate platform-wide normative standards there.
- ContractForge may publish domain-specific standards upstream when they become cross-repo norms.
- ContractForge services may later be deployed through Prophet Platform, but deployment topology does not belong here.

## Anti-patterns to avoid

- turning this repo into a dumping ground for all “business logic”
- mixing policy canon and contract canon without clear ownership
- hiding runtime implementation in standards-only repos
- burying contractual economics inside umbrella public-surface repos
