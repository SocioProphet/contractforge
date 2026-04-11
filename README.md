# ContractForge

ContractForge is the canonical SocioProphet repository for **contract lifecycle, contractual economics, settlement artifacts, adjustments, and ledger-anchored finalization**.

This repository exists because contracts are **not** the same thing as policy, ontology, transport, or generic platform runtime.

ContractForge is the home for:

- contract lifecycle and amendment semantics
- effective-time and retroactivity rules
- economic artifact definitions
- candidate vs approved vs finalized settlement behavior
- adjustment, reversal, and restatement semantics
- contract-aware authoring, linting, planning, and execution surfaces
- batch finalization and commitment boundaries
- evidence and dispute-oriented explanation surfaces for contractual outcomes

## What ContractForge is not

ContractForge is **not**:

- the workspace controller (`SocioProphet/sociosphere`)
- the generic runtime/deployment hub (`SocioProphet/prophet-platform`)
- the generic policy control repository (`SocioProphet/policy-fabric`)
- the cross-platform standards authority for storage/contracts/measurement (`SocioProphet/socioprophet-standards-storage`)
- the ontology supply-chain home (`SocioProphet/ontogenesis`)

## Initial repository structure

- `docs/ARCHITECTURE.md` — platform architecture and role in the wider stack
- `docs/BOUNDARIES.md` — explicit repo boundary and ownership rules
- `docs/ECONOMIC_ARTIFACT_SPEC.md` — canonical economic artifact model
- `docs/TEMPORAL_AND_CORRECTION_POLICY.md` — timing, close, restatement, and adjustment policy
- `schemas/README.md` — schema strategy and expected contract families

## Relationship to the wider SocioProphet stack

- **Sociosphere** registers ContractForge as a managed workspace component and enforces repo-role boundaries.
- **Policy Fabric** provides policy overlays and governance constraints that may restrict contract authoring, release, approval, and data-handling behavior.
- **SocioProphet Standards Storage** is the upstream normative home for cross-repo standards and interoperability contracts that ContractForge may consume or publish into.
- **Prophet Platform** is the runtime/deployment hub that can host ContractForge services once implementation begins.
- **Ontogenesis / Standards Knowledge** can carry ontology and semantic companion materials where appropriate.

## Current status

This repository is intentionally seeded as a **clean canonical home** before large code drops. The immediate goal is to freeze the architecture, economic artifact model, and temporal/correction semantics so later implementation work lands into a stable boundary.

## License

MIT
