# Peppol global and UK research

This research supports two decisions: which Peppol capabilities Sage can reuse across markets, and what UK products need for existing exchange arrangements and the announced VAT e-invoicing mandate. Start with the UK policy evidence, then use the global analysis to identify shared capability and country-specific gaps.

The agreed structure separates global research from UK research. Existing PRDs and specifications remain at their current paths. Research findings are draft evidence and proposed product implications; they do not change approved requirements, document status, provider selection or production availability. Nothing in this folder is enabled for Confluence publication.

## Reading guide

| Document | Purpose |
|---|---|
| [RES-SEI-003 — Source register](RES-SEI-003-peppol-source-register.md) | Official sources, versions, exact sections, supported claims and access limits |
| [RES-SEI-004 — Governance and operating model](global/RES-SEI-004-governance-and-operating-model.md) | Actors, responsibilities and the boundary between global rules and national requirements |
| [RES-SEI-005 — Network and participant lifecycle](global/RES-SEI-005-network-and-participant-lifecycle.md) | Registration, discovery, send/receive, migration, failure and recovery |
| [RES-SEI-006 — Document profiles and validation](global/RES-SEI-006-document-profiles-and-validation.md) | BIS, PINT, syntax, process, validation artefacts and transformation qualification |
| [RES-SEI-007 — Country comparison](global/RES-SEI-007-country-comparison.md) | Authority inventory, selected country evidence and limits of global interoperability |
| [RES-SEI-008 — Operations and commercial assessment](global/RES-SEI-008-operations-and-commercial-assessment.md) | Sage capability evidence, operating options, support, security and economics |
| [RES-SEI-009 — UK policy and source evidence](uk/RES-SEI-009-policy-and-source-evidence.md) | Current public-sector context, 2029 direction and unresolved UK rules |
| [RES-SEI-010 — UK customer and product scenarios](uk/RES-SEI-010-customer-and-product-scenarios.md) | Proposed scenario extensions for customers, accountants, products and support |
| [RES-SEI-011 — UK readiness and open decisions](uk/RES-SEI-011-readiness-and-open-decisions.md) | Evidence requests, decision owners, acceptance checks and delivery sequence |

## Canonical product ownership

| Canonical document | Owning subject | Research relationship |
|---|---|---|
| [PRD-SEI-227](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md) | Shared service and country-pack boundary | Reuse shared behaviour after implementation qualification |
| [PRD-SEI-230](../../prds/PRD-SEI-230-uk-e-invoicing-compliance-pack.md) | UK product requirements | UK findings become proposed changes for review |
| [PRD-SEI-233](../../prds/PRD-SEI-233-peppol-multi-address-and-endpoint-routing.md) | Participant and endpoint routing | Owns routing requirements; research adds evidence and questions |
| [PRD-SEI-240](../../prds/PRD-SEI-240-peppol-access-point-service-readiness.md) | Earlier AP operating-model assessment | Retained as the predecessor to PRD-SEI-245 |
| [PRD-SEI-245](../../prds/PRD-SEI-245-peppol-access-point-validation-and-certification.md) | Validation and certification of the reported Sage AP | Immediate source for the AP evidence path |
| [PRD-SEI-242](../../prds/PRD-SEI-242-peppol-lifecycle-feedback.md) | Feedback, history and recovery | Owns status meanings and source-to-product mappings |
| [PRD-SEI-241](../../prds/PRD-SEI-241-ubl-validation-service.md) | Shared validation behaviour | Owns validation and correction handoff |
| [Shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md) | Shared meanings | Keep identity, authority and outcome terms aligned |

## Evidence and maintenance

Baseline checked on **15 October 2026**. Source IDs in the research refer to RES-SEI-003. “Confirmed” means supported within the named source's scope; “Proposed” means analysis for review; “Open” means evidence or a decision is missing. None of these labels proves an implementation exists.

Maintain one authoritative statement per topic. Link to the owning PRD for existing requirements and to the owning research document for new findings. Store permitted supporting artefacts under `assets/peppol/` only when needed; do not create an empty asset tree or mirror documentation sites. Do not retain credentials, private keys, personal data or confidential raw exports.

The initial pack contains evidence-backed analysis and an explicit backlog. The authority inventory is broad; the selected country comparisons are not complete national compliance packs. UK legal and technical activation remains subject to the gates in RES-SEI-011.
