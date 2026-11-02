# Invoice receiving

Use the same three reading views and detailed API reference as [onboarding](../onboarding-and-connectivity/README.md). These drafts are based on SPEC016 and the supplied `/context` evidence. Publication was authorised on 2 November 2026; lifecycle status remains draft.

**View is required for public and private platforms. SPFE user download is required; private user download is TBD.** [SPEC026 §1](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#1-purpose-actors-and-boundary) owns this product decision. Backend source-file acquisition is a separate action.

**Which API does what?** **Query e-invoices** supplies the invoice list (RET-API-01). **Retrieve e-invoice** supplies one invoice's details, status history and attachment download links (RET-API-02). Downloading an attachment follows a returned link as part of this flow. RET-API-03 documents that file-transfer step; it is not a third Sage invoice endpoint. Query can also return attachment links. See [the API comparison and flow](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#1-existing-product-facing-calls). Spain implementation coverage still needs qualification.

**How do new SPFE invoices reach the list?** Sage must initiate discovery and file pulls using the supplied contracts; no SPFE webhook or WebSocket interface is established. [SPEC027 §3.1](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#31-query-coverage-and-recovery) compares France notifications, the scheduled baseline and the proposed refresh when a customer opens a stale list. Architecture must determine cadence, rate limits and execution; the customer-view trigger remains a proposal.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-025](SPEC-SEI-025-invoice-retrieval-solution-summary.md) | Business outcome, scope, actors and step-by-step walkthrough. Start here. |
| [Logical Feature Specification — SPEC-SEI-026](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md) | Existing intake, retrieval, receiving and file-access scenarios, rules, failures and functional acceptance. |
| [Sequence and Reuse Assessment — SPEC-SEI-027](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md) | Existing API calls, grey/blue sequences, Spain public/private changes, product impact and engineering gates. |
| [API Reuse and Spain Changes — SPEC-SEI-042](api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md) | Request/response fields and examples, public SOAP bindings, proposed changes and missing contracts. |

[Supplied API guide evidence](<../../context/FR API/Receiving/receive-e-invoice-guide-extract.md>) — first used for France; Spain support still needs confirmation.

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
