# Provider connectivity

This folder retains the earlier Spain public/private connectivity review. Start customer setup reviews from [onboarding and connectivity](../../onboarding-and-connectivity/README.md), SPEC-SEI-037–039. These three unpublished drafts retain runtime sending/receiving, format and reuse analysis where cited. Business content, IDs and metadata are preserved; relative links and this reading-route guidance changed.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-034](SPEC-SEI-034-provider-connectivity-solution-summary.md) | Business problem, scope, actors, shared API direction, existing Global API diagram and material decisions. Start here. |
| [Logical Feature Specification — SPEC-SEI-035](SPEC-SEI-035-provider-connectivity-logical-feature-specification.md) | Public/private send and receive scenarios, existing PCN/B2BR processes, file roles, failures, recovery and functional acceptance. |
| [Sequence and Reuse Assessment — SPEC-SEI-036](SPEC-SEI-036-provider-connectivity-sequence-and-reuse-assessment.md) | Existing sending/receiving sequences, evidenced API operations, format differences, DTS/provider reuse and engineering gates. |

[Local review preview](../../../work/provider-connectivity-review/index.html). Diagrams are reused unchanged from 011, 013, 017, 024 and 027, with links to their existing Draw.io, SVG and PNG assets. Terminology follows the shared glossary; this folder introduces no additional service or diagram responsibility group.

This set brings three existing scopes into one review. It does not replace their detailed registers, select a provider or establish one external provider's coverage of both public and private work.

Public platform terminology comes from the original Spain catalogue, formats, WSDL/XSD and examples indexed in [context](../../../context/RES-SEI-002-spain-public-platform-technical-evidence.md), with the shared glossary for common terms. Peppol is excluded from this review.

## Retained source specifications

| Existing source | Role in the combined review |
|---|---|
| [SPEC-SEI-013 — Provider API through the Global API](../../SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md) | Shared Sage contract for products and authorised partners. |
| [SPEC-SEI-011 — Public-platform connector](../../SPEC-SEI-011-public-platform-connector-solution-specification.md) | Spain AEAT protocol, operation qualification and public response evidence. |
| [SPEC-SEI-017 — B2B Router binding](../../SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md) | Candidate private-provider contract and provider-specific gaps. |

[SPEC-SEI-014](../../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) retains shared connection and routing ownership. The existing [sending](../../invoice-sending/README.md), [receiving](../../invoice-receiving/README.md) and [lifecycle](../../invoice-lifecycle/README.md) folders retain their business behaviour. This folder assesses how those journeys use external connectivity.

All three source files remain unchanged. The [publication configuration](../../../config/confluence.yml) still selects SPEC-SEI-011 for stable Confluence page `923861399` and SPEC-SEI-013 for `923861402`. SPEC-SEI-017 has no page ID and remains unpublished. This set changes no publication selection or source document status.
