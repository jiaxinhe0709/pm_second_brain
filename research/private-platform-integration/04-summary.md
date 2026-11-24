---
id: RES-SEI-014
title: Private-platform connector integration — summary for Jiaxin
type: research
status: draft
owner: Samu Coco
product: spain-e-invoicing
created: 2026-11-23
updated: 2026-11-23
related:
  - RES-SEI-013
confluence:
  publish: false
  page_id: ""
---

# PROPOSAL — Summary for Jiaxin

**Assumption:** B2B Router, SERES, Banqup and ZeroComa integrate with Sage through the existing connector role. All classifications and next steps below are PROPOSAL, not decisions.

Sage has code-evidenced authentication, connector invoice submission/upload, retrieval, status/history, notifications and UBL/Factur-X processing. Missing or unqualified areas include external admission, business mapping, delivery/recovery guarantees, Spain profiles and cancellation effects; production readiness is not established. Much of the proposal reuses these surfaces, with optional extensions where platforms use different patterns.

The effort classes below are provisional: **Document existing** describes EXISTING surfaces; **Small change** extends an existing surface; **New capability** covers proposed behaviour whose implementation is only SPECIFIED or OPEN. OPEN scope can change the classification. Confidence concerns platform-pattern evidence: High = DOCUMENTED; Medium = INFERRED, not delivery certainty.

| Change | Type | Platforms | Confidence |
|---|---|---|---|
| P01 Credential profile | Document existing; New capability option | All; API-key option for B2B Router | High: B2B Router/Banqup/ZeroComa; SERES auth unknown |
| P02 Business IDs and stable external references | Small change; Spain mapping OPEN | All | High: documented account models; Medium: SERES NIF/ZeroComa CIF |
| P03 Async receipts, correlation and recovery | Small change; guarantees OPEN | All | High: B2B Router/Banqup; Medium: SERES/ZeroComa |
| P04 Signed notifications, subscriptions and replay | New capability for unproven guarantees | All | High: B2B Router/Banqup/ZeroComa; Medium: SERES |
| P05 Status dictionary and attribute mappings | Document existing; Spain meanings OPEN | All | High: documented outcomes; Medium: inferred invoice/tracking lists |
| P06 Structured errors and next actions | Small change | All; source mappings initially B2B Router/Banqup | High: B2B Router/Banqup; other catalogues unknown |
| P07 Document profiles and conversion options | Document existing; New capability option | B2B Router/ZeroComa: conversions; Banqup: UBL/PDF; SERES provisional | High: documented formats; Medium: SERES broader formats |
| P08 Versioned connector sandbox/conformance pack | New capability where partner enablement is OPEN | All | High: B2B Router/Banqup/ZeroComa; Medium: SERES |
| P09 Cancellation/correction action contract | New capability for qualified external actions | B2B Router/Banqup; others questions | High: limited documented workflows; Spain semantics OPEN |

**Options, not recommendations:** P01 API-key support is a **costly alternative; cheaper option = platforms use our existing auth**. P07 Facturae/standalone-CII conversion is a **costly alternative; cheaper option = platforms send UBL**, subject to profile qualification. No cost estimate is established.

**Top three questions for Jiaxin**

1. **J01:** Which invoice, work-retrieval and result actions will each connector own, and for which businesses?
2. **J02:** Who grants credentials and authority, and how do platform accounts/NIFs map to Sage datasets and connections?
3. **J03:** Which subscriptions, acknowledgement, retry/replay and recovery guarantees can Sage expose to external connectors?

**PROPOSAL — Next step after agreement:** Prepare platform questions on B2B Router's authoritative statuses/replay; SERES's API, auth and identifiers; Banqup's Spain scope/listener security; and ZeroComa's Swagger, file profiles, statuses and errors. Request sample payloads and sandbox contracts. Keep SPFE claims/dates unverified and separate from current capabilities.

Source: [RES-SEI-013 — Gap matrix](03-gap-matrix.md), the only analysis input.
