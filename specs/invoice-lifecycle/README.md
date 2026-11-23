# Invoice lifecycle

[Lifecycle and reporting error handling — SPEC052](../error-handling/SPEC-SEI-052-invoice-lifecycle-and-reporting-error-handling.md) covers stage-specific investigation and recovery. [All stage error-handling documents](../error-handling/README.md).

Choose the view for your audience. Business stakeholders start with SPEC028; engineers start with SPEC029 and follow its contract/reuse links. The views share the same requirement IDs and source evidence. Detailed behaviour stays in its owning file so that the business summary and engineering documents cannot become separate specifications.

| Audience / reading route | File | What to use it for | Confluence |
|---|---|---|---|
| **Business — start here** | [Business summary — SPEC028](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) | Customer problem, outcomes, scope, main journey, delivery decisions and unresolved business effects. | [Open summary](https://confluence.sage.com/pages/viewpage.action?pageId=923861398) |
| **Engineering — start here** | [Logical specification — SPEC029](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) | Scenarios, exact required behaviour, exceptions, Annex II checks, safe recovery and functional acceptance. | [Open view](https://confluence.sage.com/pages/viewpage.action?pageId=937965384) |
| Engineering — contracts and mappings | [API reference — SPEC041](api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md) | Documented calls, proposed Spain action/input/XML bindings, payload examples, results and errors. | [Open view](https://confluence.sage.com/pages/viewpage.action?pageId=937965396) |
| Engineering/Architecture — reuse and decisions | [Sequence and reuse assessment — SPEC030](SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) | Interaction sequences, existing capability assessment, actual-build questions, qualification evidence and decision owners. | [Open view](https://confluence.sage.com/pages/viewpage.action?pageId=937965388) |

The business summary is a complete overview for business review. Engineering detail remains available through links. These drafts support review and planning; disputed rules and unqualified API/build coverage remain explicit. The existing [onboarding views](../onboarding-and-connectivity/README.md) use the same summary/logical/API structure.

[SPEC-SEI-029 SPFE states and reporting classifications](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#spfe-lifecycle-states) · [Draft platform mapping](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#draft-lifecycle-mapping) · [Reporting-action restrictions](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#spfe-reporting-action-restrictions).

[Supplied POST contract](<../../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>) · [API guide evidence](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>) · [Annex II comparison](<../../context/Anexo II/annex-ii-review.md>). The POST contract declares API `1.0.0`; the guides link `1.13.0`. Their build relationship and Spain support remain unconfirmed.

The existing API is the first implementation reuse candidate. A common envelope and variable attributes do not prove deployed Spain support. Keep successful invoice status, transition attempts, business facts and destination-specific reports separate. French codes, reasons and transition rules must not become Spain defaults.

[SPEC-SEI-028](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) is selected for stable Confluence page `923861398` in [the publication configuration](../../config/confluence.yml). SPEC029, SPEC030 and SPEC041 are companion views. Publication is authorised; all four remain drafts. [SPEC-SEI-009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) stays unchanged in Git; its provider tables, field ledger and LCS traceability remain supporting detail.
