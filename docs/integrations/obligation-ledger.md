# Obligation Ledger Integration for Professional Intelligence OS

## Purpose

The Obligation Ledger is the Professional Intelligence OS layer that turns contracts, client terms, guidelines, commercial rules, restrictions, and amendment history into reviewable, enforceable, and auditable obligations.

ContractForge owns the canonical contract and obligation semantics. It does not own generic platform deployment, policy execution, workspace UX, or model routing.

## Scope

The Obligation Ledger should model:

- contractual duties;
- client or counterparty terms;
- confidentiality obligations;
- AI-use restrictions;
- billing and economic rules;
- approval requirements;
- effective-time and retroactivity;
- amendments, reversals, corrections, and restatements;
- settlement or finalization boundaries;
- evidence and dispute-oriented explanations.

## Boundary with Policy Fabric

ContractForge records what the obligation is and why it exists.

Policy Fabric compiles the obligation into executable policy overlays for runtime evaluation.

Prophet Platform calls those policies before agent, workspace, memory, model, search, or tool actions.

Model Governance Ledger and the Evidence Plane record the model/tool/policy versions, decisions, approvals, and replay pointers.

## Obligation record minimum

A Professional Intelligence OS obligation record should include:

- obligation id;
- source contract or guideline;
- source clause or section pointer;
- subject and beneficiary;
- action required, restricted, or allowed;
- affected resource classes;
- effective start/end and amendment lineage;
- jurisdiction or scope;
- approval requirement;
- policy mapping reference;
- evidence hash and replay pointer;
- finalization or dispute status.

## Initial obligation families

- confidentiality
- AI-use restriction
- billing guideline
- approval requirement
- data handling
- workspace access
- information barrier
- retention
- disclosure
- economic adjustment

## Integration with Professional Intelligence playbooks

Legal new matter intake:
- Identify client guidelines and matter-specific terms.
- Determine AI-use restrictions and confidentiality controls.
- Produce obligation review evidence before workspace creation.

Client opportunity review:
- Identify terms or restrictions tied to the client, source channel, or organization.
- Route escalations when an obligation blocks or constrains workflow execution.

Revenue integrity review:
- Compare captured work and prebill entries against contractual billing rules.
- Explain exceptions, adjustments, write-down drivers, and review gates.

Real-assets diligence:
- Capture lease, ownership, permit, service, operating, and reporting obligations.
- Bind obligations to assets and evidence sources.

## Runtime acceptance requirements

An obligation-aware workflow is not acceptable until it can:

1. resolve applicable obligations for a workspace or playbook;
2. map each obligation to a policy decision path;
3. emit evidence for obligation lookup and policy evaluation;
4. preserve effective-time and amendment lineage;
5. produce a human-readable explanation of the obligation decision;
6. support replay or audit of the decision inputs.

## Near-term implementation targets

1. Add a minimal `obligation.schema.json` aligned with platform contracts.
2. Add examples for confidentiality, AI-use restriction, billing guideline, and approval requirement.
3. Add validation that every obligation example maps to a policy-family identifier.
4. Add an integration example consumed by a `prophet-platform` playbook smoke test.
