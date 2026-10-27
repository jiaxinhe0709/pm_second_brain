---
id: SPEC-SEI-025
title: Invoice Retrieval Solution Summary
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-22
updated: 2026-10-27
reviewers: []
related:
  - SPEC-SEI-016
  - SPEC-SEI-026
  - SPEC-SEI-027
  - PRD-SEI-211
  - PRD-SEI-213
  - PRD-SEI-223
  - PRD-SEI-244
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# Invoice Retrieval Solution Summary

[Logical specification](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md) · [API reuse assessment](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md) · [Feature folder](README.md)

## Revision overview

This view summarises [SPEC016](../archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md). Its RRI, PRI, RSD and RCV IDs, release scope and source-file controls remain unchanged. SPEC016 remains the selected Confluence source; these three views are unpublished drafts. Provider support and implementation coverage remain open.

## 1 Purpose and intended outcomes

**What:** obtain invoices addressed to a Spanish business, save their source files and deliver each business invoice once to the correct product. **Why:** a missed notification or product failure must not lose an invoice. **Reuse:** assess the existing E-Invoice API, records access and inbound DTS mapping before adding capabilities. REF-PRODUCT; INT-RCV01.

Product teams use this summary for scope and impact. SPEC026 owns scenarios and required behaviour; SPEC027 owns API reuse and engineering gaps.

## 2 Terms used

[Shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md): **discovery** finds an invoice reference; **capture** saves its verified source file; **stored-file access** returns saved bytes under current permission. Capture, product receipt and buyer acceptance have separate results.

## 3 Scope and actors

| Situation | Required outcome |
|---|---|
| Public platform — Phase 1 | Collect automatically. Discover invoices, then download their files. Customer refresh can accelerate the same work. SPFE-S02/S03. |
| Private platform — selected later phase | Download a file when only a notification/reference arrives. If the provider delivers complete bytes, save them without another fetch. |
| Public copy and private original | Keep both sources and prove whether they represent one business invoice. |
| Customer/accountant requests a saved file | Check current client/file permission and return the saved, labelled file. |
| Processing, product delivery or collection fails | Keep completed work; show the affected item, next action and owner. |

The business or authorised accountant requests permitted actions. The ERP displays results and confirms receipt. The E-Invoice Service coordinates collection and receiving; supporting capabilities check permission, files, mapping and records. Source platforms supply files/results; Operations resolves assigned failures. These are logical responsibilities.

Start after [onboarding](../onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules) has established the selected platform access and business mapping. Reuse the company’s SXS dataset and required credential references through qualified bindings; do not onboard the customer again here. Private rollout remains RRI-Q02. ZIP export, sending and business lifecycle actions keep their existing scope.

## 4 End-to-end workflow

![Find an invoice, save its file, and deliver it once](../../assets/diagrams/invoice-retrieval-overview-process.svg)

[Draw.io](../../assets/diagrams/invoice-retrieval-overview-process.drawio) · [PNG](../../assets/diagrams/invoice-retrieval-overview-process.png).

Public discovery and private intake join at source capture. A notification or metadata result does not complete capture. After capture, stored-file access and product processing proceed separately. SPEC026 explains the checks and safe recovery.

## 5 Reuse direction and Spain boundaries

| Existing capability / pattern | Spain work to confirm |
|---|---|
| E-Invoice subscriptions, list, detail and file download | Confirm Spain service support, identity mapping, file roles and missed-event recovery. The supplied guide proves documented operations, not a running Spain integration. |
| Shared capture, duplicate handling and records access | Qualify the actual build, current permissions, integrity, retention and recovery. |
| Existing DTS — preferred mapping candidate | Prove the selected Spain inbound format, tax/extension fields and target-product mapping. Outbound UBL support alone is insufficient. |
| Spain public collection | Bind the supplied discovery/download operations, representation and UBL profile. Keep these country rules separate. SPFE-S02/S03/S08. |

## 6 Material decisions and dependencies

| Decision | Evidence / owner |
|---|---|
| Enabled sources and access — RRI-Q01/02; RET-G01/06 | Product, Identity and Integration: supported modes, recipient permission and public contract. |
| Complete collection — RSD-G01/06/07; RET-G03 | API and Operations: page boundaries, saved progress, late arrivals and older-history recovery. |
| Correct files and mapping — RET-G04/07 | Records, Security, Format and DTS: source provenance, safety and inbound meaning. |
| Saved access and product receipt — RET-G05/09 | Records and Product: historical access, retention/holds, delivery identity and receipt. |

SPEC027 records the full gates and owners. Existing query windows, temporary links and optional renderings are API constraints; they do not set Spain retention or release scope.

## 7 Completion and assurance

Collection progress is complete only when each covered item has a saved source file and receiving classification, or an approved ignore outcome. Product processing, product receipt and source acknowledgement remain separate. PRD211 consultation also requires evidenced distribution and freshness. RSD-05/06; RCV-07; REF-PRODUCT.

Use [SPEC026 recovery](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#33-failure-and-recovery-decisions) and acceptance for failure coverage. Implementation readiness requires the selected contracts, build, mappings and operational evidence; document review cannot establish it.

## REF Source references

| REF ID | Source and version/date | Exact location | Supported claim and limit |
|---|---|---|---|
| REF-BASE | [SPEC-SEI-016](../archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md), updated 20 October 2026 | Parts 1–4; RRI/PRI/RSD/RCV controls and REF | Combined draft baseline and existing IDs; not implementation evidence. |
| REF-PRODUCT | [PRD-SEI-211](../../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md), updated 20 October 2026; [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md), updated 7 October 2026; [PRD-SEI-213](../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md) | PRD211 Phase 1, retrieval/download boundary, FR1–55; PRD223 receiving FR17–20 and DTS FR43–44; private capability boundaries | Canonical product sources with their recorded draft/discovery status. Does not approve added release scope. |
| INT-RCV01 | [Supplied FR receiving guide extract](<../../context/FR API/Receiving/receive-e-invoice-guide-extract.md>), received 22 October 2026; revision unknown | Sections 1–4; Polling, formats, and extracted data | Documented guide flow and limits; schema, build and Spain coverage unverified. |
| SPFE-S02 | [Final Order HAC/1028/2026](../../context/BOE-A-2026-20587.pdf), published 5 October 2026 | Articles 9–11, PDF pp. 9–11 | Recovery, conservation access and representation within the order's scope; no numeric Sage service objective or private API contract. |
| SPFE-S03 | [Original catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | Sections 6.4–6.7, pp. 12–15 | Public discovery, queries and downloads are distinct operations; incomplete wire semantics remain open. |
| SPFE-S08 | [Original formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), 0.1.0, 9 October 2026, BORRADOR | Section 5.1.1 p. 8; sections 5.4–5.7 pp. 14–15 | Supplied UBL 2.5 selection; query/download formats pending. Not a full activated profile. |
| REF-API | [SPEC-SEI-027](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#ref-source-references), draft 22 October 2026 | Operation sources, local changes and qualification gates | Engineering analysis and original-contract links. Proposed controls have separate authority from external sources. |
