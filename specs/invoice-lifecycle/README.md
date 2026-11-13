# Invoice lifecycle

Use the same reading structure as [onboarding and connectivity](../onboarding-and-connectivity/README.md): three specification views and a separate API reference. These drafts use SPEC009, the supplied lifecycle guides, status POST OpenAPI and Spain source evidence.

| Read | Purpose | Confluence |
|---|---|---|
| [Solution Summary — SPEC-SEI-028](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) | Business outcomes, scope, reuse direction and material decisions. Start here. | [Open summary](https://confluence.sage.com/pages/viewpage.action?pageId=923861398) |
| [Logical Feature Specification — SPEC-SEI-029](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) | Scenarios, LCS rules, SPFE states and reporting classifications, draft platform mapping, restrictions and acceptance. | [Open view](https://confluence.sage.com/pages/viewpage.action?pageId=937965384) |
| [Sequence and Reuse Assessment — SPEC-SEI-030](SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) | Reuse sequences, country-pack/architecture assessment, product impact and the authoritative LIF-G01–08 register. | [Open view](https://confluence.sage.com/pages/viewpage.action?pageId=937965388) |
| [API Reuse and Spain Changes — SPEC-SEI-041](api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md) | Existing calls, proposed SPFE action/field mappings, Spain payload examples and headers/errors. | [Open view](https://confluence.sage.com/pages/viewpage.action?pageId=937965396) |

[SPEC-SEI-029 SPFE states and reporting classifications](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#spfe-lifecycle-states) · [Draft platform mapping](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#draft-lifecycle-mapping) · [Reporting-action restrictions](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#spfe-reporting-action-restrictions).

[Supplied POST contract](<../../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>) · [API guide evidence](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>) · [Annex II comparison](<../../context/Anexo II/annex-ii-review.md>). The POST contract declares API `1.0.0`; the guides link `1.13.0`. Their build relationship and Spain support remain unconfirmed.

The existing API is the first implementation reuse candidate. A common envelope and variable attributes do not prove deployed Spain support. Keep successful invoice status, transition attempts, business facts and destination-specific reports separate. French codes, reasons and transition rules must not become Spain defaults.

[SPEC-SEI-028](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) is selected for stable Confluence page `923861398` in [the publication configuration](../../config/confluence.yml). SPEC029, SPEC030 and SPEC041 are companion views. Publication is authorised; all four remain drafts. [SPEC-SEI-009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) stays unchanged in Git; its provider tables, field ledger and LCS traceability remain supporting detail.
