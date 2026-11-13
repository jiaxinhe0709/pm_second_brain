# Invoice receiving

The customer can consult **sent and received** e-invoices through **Customer ↔ ERP ↔ Domain Service – E-Invoice Service**, using the existing E-Invoice API. [SPEC026 §2](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#customer-list-open-and-download) owns that read journey. Automatic collection and processing in this folder apply to received invoices; sending keeps its own workflow.

Use the same three reading views and detailed API reference as [onboarding](../onboarding-and-connectivity/README.md). These drafts are based on SPEC016 and the supplied `/context` evidence. Publication was authorised on 2 November 2026; lifecycle status remains draft.

**View and user download are required for all enabled public and private platforms, including the Sage offering.** [SPEC026 §1](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#1-purpose-actors-and-boundary) owns this product decision. Backend source-file acquisition is a separate action.

**Which API does what?** The ERP calls the Domain Service through the shared API. **Query e-invoices** supplies the business’s authorised sent/received list (RET-API-01). **Retrieve e-invoice** supplies one invoice's details, history, attachment count and links when included (RET-API-02). Downloading an attachment follows a returned link as part of this flow. RET-API-03 documents that file-transfer step; it is not a third Sage invoice endpoint. Query can also return attachment links. See [the API comparison and flow](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#1-existing-product-facing-calls). Spain implementation coverage still needs qualification.

**How do new SPFE invoices reach the list?** Sage must initiate discovery and file pulls using the supplied contracts; no SPFE webhook or WebSocket interface is established. [SPEC027 §3.1](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#31-query-coverage-and-recovery) compares France notifications, the scheduled baseline and the proposed refresh when a customer opens a stale list. Architecture must determine cadence, rate limits and execution; the customer-view trigger remains a proposal.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-025](SPEC-SEI-025-invoice-retrieval-solution-summary.md) | Start here: one presentation overview with five framed actions A–E, their scope and links to detail. |
| [Logical Feature Specification — SPEC-SEI-026](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md) | Required behaviour for receiving and consultation; the supporting swimlane expands A. E links to the lifecycle owner. |
| [Sequence and Reuse Assessment — SPEC-SEI-027](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md) | Supporting sequences: B–D customer Query/Retrieve/download, plus source collection and file recovery; reuse and engineering gates. |
| [API Reuse and Spain Changes — SPEC-SEI-042](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md) | Request/response fields and examples, public SOAP bindings, proposed changes and missing contracts. |

**Where do we get the invoice?** Read the [plain-English source-choice flow in SPEC026](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#choose-source-and-get-invoice) before receiving step 1. It covers public originals, private originals, copy-only access and failed private downloads.

**After opening an invoice:** the customer can choose **Download file** or [**Review and take action — SPEC029**](../invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#review-and-take-action). The lifecycle view owns enabled actions and their results. Use [SPEC042’s source lists](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#document-types-and-status-values) for exact invoice types, status codes and their separate meanings.

[Supplied API guide and REST snapshot evidence](<../../context/FR API/Receiving/receive-e-invoice-guide-extract.md#query-and-retrieve-openapi-snapshots>) — the 13 November Query/Retrieve text includes attachment count, legal address and `includeAttachments` updates. [Earlier snapshots and current hashes](<../../context/FR API/Receiving/openapi-source-snapshots.json>) are preserved. Spain support still needs confirmation.

The combined predecessor is retained in [the archive](../archive/README.md). Its
linked detail remains part of this review set; its lifecycle and publication
settings are unchanged.

## Current sources

| Source | Scope |
|---|---|
| [SPEC-SEI-016 Invoice receiving, retrieval and download](../archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) | Retained archived baseline. Contains full interaction/data inventories, decisions and original acceptance traceability. |
| [PRD-SEI-211 Public platform invoice consultation](../../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md) | Public consultation and retrieval requirements. |
| [PRD-SEI-223 Interoperability, routing and transformation](../../prds/PRD-SEI-223-interoperability-routing-transformation.md) | Shared exchange and receiving requirements. |
| [PRD-SEI-213 Private platform connectivity](../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md) | Private connectivity requirements. |
| [PRD-SEI-244 E-invoicing process flow](../../prds/PRD-SEI-244-e-invoicing-process-flow-specification.md) | Inbound business process boundary. |

The folder name covers receiving, retrieval and download. Source intake, product availability, technical acknowledgement and buyer acceptance retain their separate meanings. Shared diagrams stay in [assets/diagrams](../../assets/diagrams/); terminology and source evidence stay in [context](../../context/).

The companions retain existing RRI, PRI, RSD and RCV meanings. Their Revision overviews identify the split, unchanged areas and open decisions. The API guide supplies reuse evidence; it does not prove Spain coverage. Phase 1 is SPFE; Phase 2 adds external private providers; Phase 3 covers the Sage offering. Labels do not establish provider readiness.

SPEC-SEI-016 remains unchanged. SPEC-SEI-025 is selected for stable Confluence page `933331276` in [the publication configuration](../../config/confluence.yml). SPEC026, SPEC027 and SPEC042 are distinct detail pages under the same public consultation parent (`837610662`); creation is authorised where no matching page exists. This README is local navigation.

## Confluence reading views

Confluence views: [Summary](https://confluence.sage.com/pages/viewpage.action?pageId=933331276) · [Required behaviour](https://confluence.sage.com/pages/viewpage.action?pageId=943980648) · [Sequences and reuse](https://confluence.sage.com/pages/viewpage.action?pageId=943980652) · [API reference](https://confluence.sage.com/pages/viewpage.action?pageId=943980662)
