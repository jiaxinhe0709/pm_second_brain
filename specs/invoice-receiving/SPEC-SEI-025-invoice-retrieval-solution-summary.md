---
id: SPEC-SEI-025
title: Invoice Retrieval Solution Summary
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-22
updated: 2026-11-13
reviewers: []
related:
  - SPEC-SEI-016
  - SPEC-SEI-026
  - SPEC-SEI-027
  - SPEC-SEI-042
  - PRD-SEI-211
  - PRD-SEI-213
  - PRD-SEI-223
  - PRD-SEI-244
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610662"
  page_id: "933331276"
  layout: two_left_sidebar
  toc: true
---

# Invoice Retrieval Solution Summary

[Logical specification](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md) · [API reuse assessment](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md) · [API calls and Spain changes](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md) · [Feature folder](README.md)

Confluence views: [Summary](https://confluence.sage.com/pages/viewpage.action?pageId=933331276) · [Required behaviour](https://confluence.sage.com/pages/viewpage.action?pageId=943980648) · [Sequences and reuse](https://confluence.sage.com/pages/viewpage.action?pageId=943980652) · [API reference](https://confluence.sage.com/pages/viewpage.action?pageId=943980662)

## Revision overview

This view summarises [SPEC016](../archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md). Its RRI, PRI, RSD and RCV IDs and source-file controls remain unchanged. The 11 November 2026 scope decision requires public/private view and user download, replacing the earlier private-download TBD. SPEC016 stays unchanged. Following publication approval on 2 November 2026, SPEC025 is the selected source for its stable Confluence page; SPEC026, SPEC027 and SPEC042 supply distinct detail views. All retain draft status. Provider support and implementation coverage remain open. REF-SCOPE.

## 1 Purpose and intended outcomes

**What:** let a customer or authorised accountant consult the business’s sent and received e-invoices through the ERP and download available files. Automatic collection and receiving cover inbound files from public (SPFE) and private platforms. **Why:** users need access to invoices even when collection or product processing has a problem. **Reuse:** assess the existing E-Invoice list, detail and file calls, and records access before adding capabilities; assess DTS for the conversion scope in SPEC026 RCV-06. REF-PRODUCT; REF-SCOPE; INT-RCV01.

SPEC026 owns scenarios and required behaviour; SPEC027 owns reuse and engineering gaps; SPEC042 supplies API fields, examples and Spain changes.

## 2 Terms used

[Shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md): **view** shows permitted invoice information or a readable representation; **source-file download** obtains bytes from a platform; **stored-file download** returns captured bytes to the user. Both view and user download are required across enabled platforms under SPEC026 §1. Viewing, capture, product receipt and buyer acceptance have separate results.

## 3 Scope and actors

| Situation | Required outcome |
|---|---|
| SPFE public platform — Phase 1 | **View and user download required.** Sage initiates discovery and file pulls; the supplied evidence establishes no SPFE webhook or WebSocket interface. Automatic collection requires Sage to trigger these calls. The scheduled baseline and proposed refresh when a stale list opens are assessed in [SPEC027 §3.1](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#31-query-coverage-and-recovery). SPFE-S03; REF-PRODUCT/API. |
| External private providers — Phase 2 | **View and user download required.** Qualify provider intake and saved-file access. Complete supplied bytes avoid another source fetch. REF-SCOPE. |
| Sage private-platform offering — Phase 3 | **View and user download required.** Qualify shared reuse, provider/service-chain support and operator readiness. REF-SCOPE. |
| Public copy and private original | Keep both sources and prove whether they represent one business invoice. |
| Customer/accountant views the list, opens an invoice and chooses a file to download | Follow the [SPEC026 §2 customer journey](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#customer-list-open-and-download). The ERP checks current access for each action and keeps original, public-copy and derived labels clear. |
| Processing, product delivery or collection fails | Keep completed work; show the affected item, next action and owner. |

The customer or authorised accountant selects a business/client and consults its sent and received invoices. The ERP calls the Domain Service – E-Invoice Service through the existing E-Invoice API, then displays returned lists, selected-invoice details and file choices. Its separate receiving work saves delivered invoices and confirms receipt. The E-Invoice Service coordinates collection and receiving; supporting capabilities check permission, files, mapping and records. Source platforms supply files/results; Operations resolves assigned failures. These are logical responsibilities.

Start after [onboarding](../onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules) has established the selected platform access and business mapping. Reuse the company’s SXS dataset and required credential references through qualified bindings. RRI-Q02 still gates provider rollout; RET-G10 qualifies required private user download. ZIP export, sending and business lifecycle actions keep their existing scope.

## 4 End-to-end workflow

![Five actions: receive, list, open, download, and review and take action](../../assets/diagrams/invoice-retrieval-overview-process.svg)

[Presentation overview — Draw.io](../../assets/diagrams/invoice-retrieval-overview-process.drawio) · [PNG](../../assets/diagrams/invoice-retrieval-overview-process.png).

Use this overview for the business presentation. **Receive invoice** is automatic inbound work. The other stages show the customer journey. From **Select and open invoice**, the customer can choose **Download file** or **Review and take action**. Download is not required before a decision. The dashed feed starts after safe capture; it does not require completed ERP delivery. Sent invoices are also available through the shared read API. The diagram legend defines the colours and **E** (exception) and **S** (saved-content handoff) markers. [SPEC042’s source lists](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#document-types-and-status-values) distinguish document types, API type values and status codes.

| Action | Purpose / detailed owner |
|---|---|
| **Receive invoice** — automatic, inbound only | Source collection/intake feeds the captured file into receiving. Record the received file → identify the invoice and label its file role → validate/convert only under RCV-06 → deliver and confirm. [SPEC026 §3 receiving swimlane](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#3-process-and-activity-order) owns the detailed steps, holds and recovery. RSD-01–06; PRI-01–04; RCV-01–09. |
| **View invoice list** — business level | ERP requests the business’s authorised sent/received list from the E-Invoice Service using Query e-invoices and displays the result. [SPEC026 §2 customer journey](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#customer-list-open-and-download) owns the outcome and exceptions; RET-API-01 supplies the call. |
| **Select and open invoice** — one invoice | ERP requests the selected invoice through Retrieve e-invoice, then displays permitted details and available files. Keep the selected ID and business context. SPEC026 §2; RET-API-02. |
| **Download file** — one attachment, optional | Obtain file choices/links when needed, then follow the selected saved-file URL. [SPEC042 RET-API-03](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#ret-api-03) describes transfer and recovery; it is not a third Sage invoice endpoint. RSD-07. |
| **Review and take action** — one invoice decision | [SPEC029](../invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#review-and-take-action) owns acceptance, rejection, payment and other enabled actions, with independent report results. [SPEC041](../invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#12-documented-status-inputs) owns exact documented command UUIDs and input fields. |

Before receiving step 1, use the [SPEC026 source-choice flow](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#choose-source-and-get-invoice): get the public original, private original or permitted public copy. It also shows the open recovery decision when private download fails. Use the [Spain public UBL copy-indicator table](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#spain-copy-indicator) to read the original/copy flag. The [three Spain original/copy scenarios](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#spain-original-and-faithful-copy-scenarios) govern file roles. A safe, authorised faithful copy can be consulted while ERP delivery waits for the original. Optional readable-file generation does not replace the source. REF-COPY-POLICY.

Use the supporting [SPEC026 receiving swimlane](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#3-process-and-activity-order), [SPEC027 list/open/download sequence](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#24-required-view-and-user-download) and [SPEC029 review and action flow](../invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#3-activity-order-and-process-support). Accounting/import choices and cancellation remain linked journeys; ERP receipt alone does not complete them. Provider/build qualification remains open.

## 5 Reuse direction and Spain boundaries

| Existing capability / pattern | Spain work to confirm |
|---|---|
| E-Invoice list/detail and file download; optional notifications | Confirm public/private view and saved-file download support, identity, file roles and missed-event recovery. The guide proves documented operations, not a running Spain integration. |
| Shared capture, duplicate handling and records access | Qualify the actual build, current permissions, integrity, retention and recovery. |
| Existing DTS — Phase 3 format conversion only | Follow [SPEC026 RCV-06](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#32-receiving-handoff). Prove the selected non-UBL 2.5 input, UBL 2.5 output, tax/extension fields and recovery. Existing outbound support alone does not prove this conversion. REF-DTS-SCOPE. |
| Spain public collection | Bind the supplied discovery/download operations, representation and UBL profile. Keep these country rules separate. SPFE-S02/S03/S08. |

## 6 Material decisions and dependencies

| Decision | Evidence / owner |
|---|---|
| Enabled sources and access — RRI-Q01/02; RET-G01/06 | Product, Identity and Integration: supported modes, recipient permission and public contract. |
| Complete collection — RSD-G01/06/07; RET-G03 | Architecture, API and Operations, with Product freshness input: pull schedule, source/API limits, proposed list-open refresh, page boundaries and gap recovery. |
| Correct files and mapping — RET-G04/07 | Records, Security and Format: source, safety and invoice meaning. DTS joins only for the conversion defined in RCV-06. |
| Saved access and product receipt — RET-G05/09 | Records and Product: historical access, retention/holds, delivery identity and receipt. |
| Private user download — RRI-Q02; RET-G10 | Records, API and provider integration, with Product/Compliance: prove private saved-file access, roles, permissions and recovery before enablement. Required scope is settled in SPEC026 §1. |
| Copy-only policy — selected; recovery qualification open | Product aligns the canonical PRD with REF-COPY-POLICY. Integration/Identity qualify public recovery triggers; Receiving/Records qualify later-original equivalence. See [SPEC026 §3.4 decisions](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#34-process-review-proposal); RET-G01/04/07/09/10 remain open. |

SPEC027 records the full gates and owners. Existing query windows, temporary links and optional renderings are API constraints; they do not set Spain retention or release scope.

## 7 Completion and assurance

Collection progress is complete only when each covered item has a saved source file and receiving classification, or an approved ignore outcome. Product processing, product receipt and source acknowledgement remain separate. PRD211 consultation also requires evidenced distribution and freshness. RSD-05/06; RCV-07; REF-PRODUCT.

Use [SPEC026 recovery](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#33-failure-and-recovery-decisions) and acceptance for failure coverage. Implementation readiness requires the selected contracts, build, mappings and operational evidence; document review cannot establish it.

## REF Source references

| REF ID | Source and version/date | Exact location | Supported claim and limit |
|---|---|---|---|
| REF-SCOPE | [SPEC026 scope and customer journey](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#customer-list-open-and-download), user direction, 11 and 13 November 2026 | §§1–2; REF-SCOPE | Public/private view and user download required. Customer sent/received list → selected invoice → optional file download through the ERP and Domain Service. Product direction, not a legal or implementation claim. |
| REF-DTS-SCOPE | [SPEC026 RCV-06](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#32-receiving-handoff), user direction, 13 November 2026 | Conversion scope and acceptance; REF-DTS-SCOPE | Phase 3 conversion of received formats other than UBL 2.5. Product decision; actual input/output mapping and build remain unqualified. |
| REF-COPY-POLICY | [SPEC026 selected copy-only policy](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#34-process-review-proposal), user direction, 13 November 2026 | Selected policy and acceptance coverage; REF-COPY-POLICY | Authorised faithful-copy view/download can proceed; ERP delivery waits for the original. Product decision; recovery triggers and implementation qualification remain open. |
| REF-BASE | [SPEC-SEI-016](../archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md), updated 20 October 2026 | Parts 1–4; RRI/PRI/RSD/RCV controls and REF | Combined draft baseline and existing IDs; not implementation evidence. |
| REF-PRODUCT | [PRD-SEI-211](../../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md), updated 20 October 2026; [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md), updated 7 October 2026; [PRD-SEI-213](../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md) | PRD211 Phase 1, retrieval/download boundary, FR1–55; PRD223 receiving FR17–20 and DTS FR43–44; private capability boundaries | Canonical product sources with their recorded draft/discovery status. Does not approve added release scope. |
| INT-RCV01 | [Supplied FR receiving guide extract](<../../context/FR API/Receiving/receive-e-invoice-guide-extract.md>), received 22 October 2026; revision unknown | Sections 1–4; Polling, formats, and extracted data | Documented guide flow and limits; schema, build and Spain coverage unverified. |
| SPFE-S02 | [Final Order HAC/1028/2026](../../context/BOE-A-2026-20587.pdf), published 5 October 2026 | Articles 3(4), 4(1)–(3), 5(2)/(5), PDF pp. 6–8; Articles 9–11, pp. 9–11 | Original/faithful-copy distinction, public exchange and copy duties; recovery, conservation access and representation. No private-provider API contract or implementation proof. |
| SPFE-S03 | [Original catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | Sections 6.4–6.7, pp. 12–15 | Public discovery, queries and downloads are distinct operations; incomplete wire semantics remain open. |
| SPFE-S08 | [Original formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), 0.1.0, 9 October 2026, BORRADOR | Section 5.1.1 p. 8; sections 5.4–5.7 pp. 14–15 | Supplied UBL 2.5 selection; query/download formats pending. Not a full activated profile. |
| REF-API | [SPEC027](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#ref-source-references) and [SPEC042](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#ref-source-references), drafts, updated 13 November 2026 | Operation sources, request/response examples, local changes and qualification gates | Engineering analysis and original-contract links. Proposed controls have separate authority from external sources. |
