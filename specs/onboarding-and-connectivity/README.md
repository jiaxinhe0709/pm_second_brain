# Customer onboarding and connectivity

This is the primary review set for customer onboarding and connection setup. Read 037 for the quick overview, 038 for the customer paths and 039 for API reuse and Spain changes. The predecessor folders are retained under `specs/archive/`.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-037](SPEC-SEI-037-customer-onboarding-and-connectivity-solution-summary.md) | Outcomes, public/private/Sage scope, responsibilities, phases and material decisions. |
| [Logical Feature Specification — SPEC-SEI-038](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md) | Simple public/private paths; conditional approval/recovery/batches. Exact rules, acceptance, states and operator timing are linked in its reference section. |
| [Sequence and Reuse Assessment — SPEC-SEI-039](SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md) | Existing E-Invoice API calls, setup sequences, Spain changes, per-call reuse recommendations and owner checks. |

[Public setup diagram](../../assets/diagrams/onboarding-public-setup-swimlane.svg) · [Private setup diagram](../../assets/diagrams/onboarding-private-setup-swimlane.svg).

## Scope and retained detail

Public onboarding remains Phase 1 readiness. External private connections and the Sage private-platform service require their existing scope, contract and activation gates. Sage branding does not identify the legal operator. Customer authority, connection readiness, route activation and operator readiness remain separate results.

The existing ONB-S01–08, ONB/OFR activities and relevant acceptance IDs retain their meanings. The summary shows the main choices. Logical diagrams show the main path and key correction and recovery branches; tables hold further actions. The five engineering sequences show API calls and data. Detailed rules and conditional diagrams remain linked; all archived sources and assets are unchanged. Public service names and identifiers come from the original [context source baseline](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md). Peppol is excluded.

Runtime invoice execution stays in the sending, receiving and lifecycle sets. [011](../SPEC-SEI-011-public-platform-connector-solution-specification.md), [013](../SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md), [014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) and [017](../SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md) retain public execution, Global API, shared routing and provider contracts. Existing DTS remains the preferred transformation candidate, subject to checks in the invoice feature where invoice work requires it.

## Predecessors and publication

All six predecessors retain their business content, permanent IDs and metadata. Their archive move changes relative links and reading-route guidance. Publication of these drafts is authorised for the existing three onboarding pages. No lifecycle status changes. The selected sources are 037–039; archived sources cannot overwrite those pages.

| New view | Retained predecessors | Approved stable-page source |
|---|---|---|
| SPEC-SEI-037 | [018](../archive/onboarding/SPEC-SEI-018-customer-onboarding-solution-summary.md) and [034](../archive/provider-connectivity/SPEC-SEI-034-provider-connectivity-solution-summary.md) | Onboarding summary page `923861390` selects SPEC-SEI-037. |
| SPEC-SEI-038 | [019](../archive/onboarding/SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) and [035](../archive/provider-connectivity/SPEC-SEI-035-provider-connectivity-logical-feature-specification.md) | Logical page `936509725` selects SPEC-SEI-038. |
| SPEC-SEI-039 | [021](../archive/onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md) and [036](../archive/provider-connectivity/SPEC-SEI-036-provider-connectivity-sequence-and-reuse-assessment.md) | Engineering page `936509735` selects SPEC-SEI-039. |

See [publication configuration](../../config/confluence.yml). Existing public connector page `923861399` still selects 011 and Global API page `923861402` still selects 013. A separate Git successor does not require another Confluence page.

The logical view records an inherited source conflict: 019 uses ONB-R25 for two different statements. The new set preserves the original effective-boundary meaning from 002 and references PRD-SEI-221 FR20 for operator handoff. The source-qualified mapping in SPEC-SEI-038 §7 resolves cross-document traceability; the archived behaviour is unchanged.
