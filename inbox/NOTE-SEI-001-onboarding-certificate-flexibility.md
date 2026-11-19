---
id: NOTE-SEI-001
title: Onboarding certificate flexibility — meeting point to confirm
type: note
status: draft
owner: Jiaxin He
created: 2026-11-18
updated: 2026-11-18
related:
  - SPEC-SEI-001
  - SPEC-SEI-038
confluence:
  publish: false
  page_id: ""
---

# Onboarding certificate flexibility

**Unconfirmed meeting understanding. Record only; no requirement, design or implementation change authorised.** Recorded on 18 November 2026; meeting date and participants not supplied.

Initial public-platform setup may establish a relationship between a company, dataset or represented taxpayer NIF and certificate A. The meeting understanding is that this initial association should not permanently restrict that business to certificate A. The same dataset or NIF should be able to send e-invoices with another certificate where that certificate is accepted and its caller has authority for the represented taxpayer and sending action.

Confirm with the meeting participants and the certificate/public-platform owners:

- Does this mean replacing the saved certificate, keeping several eligible certificates, or selecting one for each sending action?
- Which identity owns the association: company, dataset, NIF, or a defined combination?
- What authority and credential checks apply to the alternative certificate, and does its use require a setup change or a new readiness check?

The [existing onboarding prerequisite checks](../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#65-onb-03-assess-prerequisites) distinguish the represented taxpayer, caller authority and selected credential. This is relevant context, not confirmation of the meeting point or current implementation support. Review with [SPEC-SEI-001 certificate management](../specs/SPEC-SEI-001-certificate-management-solution-specification.md) when confirmation work is authorised.

**Disposition:** Pending confirmation. No external contact, technical qualification, spec update or publication requested at this stage.
