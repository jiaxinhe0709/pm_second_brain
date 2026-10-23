# Invoice lifecycle

Three unpublished draft views based on the unchanged SPEC-SEI-009, four supplied French lifecycle guides, the transition-outcome note and the new Annex II snapshot.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-028](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) | Business outcomes, scope, reuse direction and material decisions. Start here. |
| [Logical Feature Specification — SPEC-SEI-029](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) | Scenarios, LCS rules, Spain events, failure/recovery and acceptance. |
| [Sequence and Reuse Assessment — SPEC-SEI-030](SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) | Existing French API patterns, Spain field gaps, sequences and qualification gates. |

[Local review preview](../../work/invoice-lifecycle-review/index.html) · [French guide evidence](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>) · [Annex II comparison](<../../context/Anexo II/annex-ii-review.md>).

The existing API is the first implementation reuse candidate. A common envelope and variable attributes do not prove deployed Spain support. Keep successful invoice status, transition attempts, business facts and destination-specific reports separate. French codes, reasons and transition rules must not become Spain defaults.

The combined predecessor is retained in [the archive](../archive/README.md). Its
linked detail remains part of this review set; its lifecycle and publication
settings are unchanged.

[SPEC-SEI-009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) remains unchanged and selected for stable Confluence page `923861398` in [the publication configuration](../../config/confluence.yml). Its detailed provider tables, field ledger links and LCS traceability remain available. These companions preserve existing IDs and add only the stated controls and checks. No publication, status change or second Confluence page is authorised by this draft set.
