# Provider Connector architecture and API

Compact technical review set for architects. Products, authorised providers and Provider Connectors use one shared Sage e-Invoicing API contract; external platform APIs remain separate. Start with 044; use 045 for the handoff contract and capability matrix, and 046 for execution/reuse decisions. External contracts and deployed implementation coverage remain open.

**Scope: six private-provider connectors + one SPFE connector = seven logical connectors, using one shared Sage API contract.** Each private-provider connector supports existing-provider customers and customers newly onboarding; [044 §3](SPEC-SEI-044-provider-connector-architecture-summary.md#3-spain-provider-connector-scope) gives the scope and links to the setup cases.

| View | Purpose |
|---|---|
| [SPEC-SEI-044 — Architecture summary](SPEC-SEI-044-provider-connector-architecture-summary.md) | API boundaries, historical terminology, Spain scope and source authority. |
| [SPEC-SEI-045 — Logical contract](SPEC-SEI-045-provider-connector-api-logical-contract.md) | Required operation safety, proposed request/result information and platform capabilities. |
| [SPEC-SEI-046 — Sequences and reuse](SPEC-SEI-046-provider-connector-api-sequences-and-reuse-assessment.md) | Execution paths, reuse qualification and architecture gates. |

These are unpublished draft companions to SPEC-SEI-013. That file remains unchanged and remains the configured source for stable Global API page `923861402`. SPEC011, SPEC014 and SPEC017 retain public transport, shared routing and B2B Router binding ownership. Customer journeys remain in [onboarding and connectivity](../onboarding-and-connectivity/README.md). No publication configuration or existing lifecycle status changes.

## Diagrams and scenario coverage

- [Logical architecture](../../assets/diagrams/provider-connector-logical-architecture.svg) — SPEC044.
- [Operation and recovery sequence](../../assets/diagrams/provider-connector-operation-sequence.svg) — SPEC046 §1.1.
- [Acquisition and handoff sequence](../../assets/diagrams/provider-connector-inbound-sequence.svg) — SPEC046 §1.2.
- [Scenario matrix CS01–16](SPEC-SEI-045-provider-connector-api-logical-contract.md#4-scenario-coverage) — main paths, alternatives, failures, recovery and qualification evidence.

SVG, editable Draw.io and PNG assets share each diagram's filename stem. All diagrams describe proposed logical responsibilities.
