# Schemas

This directory is reserved for ContractForge schema families.

## Intended schema areas

- contract lifecycle schemas
- amendment and effective-window schemas
- economic artifact schemas
- settlement and batch schemas
- adjustment and reversal schemas
- commitment and proof schemas
- explanation / evidence reference schemas

## Format posture

ContractForge may use multiple schema forms depending on the interface and artifact type:

- JSON Schema for structural contracts and API-facing objects
- Avro where event-stream compatibility is needed
- JSON-LD or RDF/OWL companions only when semantic publication is necessary and canonical ownership is clear

## Boundary rule

Schemas that become wider cross-repo platform standards may need to be published or mirrored upstream into `SocioProphet/socioprophet-standards-storage`.

This repository remains the canonical home for the contract-domain product model itself.
