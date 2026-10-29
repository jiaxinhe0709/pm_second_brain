# Invoice lifecycle

Use the same reading structure as [onboarding and connectivity](../onboarding-and-connectivity/README.md): three specification views and a separate API reference. These drafts use SPEC009, the supplied lifecycle guides, status POST OpenAPI and Spain source evidence.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-028](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) | Business outcomes, scope, reuse direction and material decisions. Start here. |
| [Logical Feature Specification — SPEC-SEI-029](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) | Scenarios, LCS rules, Spain events, failure/recovery and acceptance. |
| [Sequence and Reuse Assessment — SPEC-SEI-030](SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) | Reuse sequences, country-pack/architecture assessment, product impact and the authoritative LIF-G01–08 register. |
| [API Reuse and Spain Changes — SPEC-SEI-041](api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md) | Existing calls, proposed SPFE action/field mappings, Spain payload examples and headers/errors. |

[Supplied POST contract](<../../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>) · [API guide evidence](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>) · [Annex II comparison](<../../context/Anexo II/annex-ii-review.md>). The POST contract declares API `1.0.0`; the guides link `1.13.0`. Their build relationship and Spain support remain unconfirmed.

The existing API is the first implementation reuse candidate. A common envelope and variable attributes do not prove deployed Spain support. Keep successful invoice status, transition attempts, business facts and destination-specific reports separate. French codes, reasons and transition rules must not become Spain defaults.

[SPEC-SEI-009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) remains unchanged and selected for stable Confluence page `923861398` in [the publication configuration](../../config/confluence.yml). Its provider tables, field ledger and LCS traceability remain part of this review set. SPEC028–030 and SPEC041 are unpublished drafts; no status or publication change is authorised.
