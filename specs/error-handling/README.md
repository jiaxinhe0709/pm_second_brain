# Error handling and operational support

Start with [SPEC048 — Shared error handling and operational support](SPEC-SEI-048-shared-error-handling-and-operational-support.md). It owns proposed search, diagnostic history, version visibility, portal actions and bulk controls. Stage documents identify the additional evidence, safe next action, owner and acceptance coverage. Functional rules and external code catalogues stay in their existing owning specs.

## Stage documents

| Stage | Error-handling document | Functional owner |
|---|---|---|
| Onboarding and connection/configuration changes | [SPEC004 — Onboarding failure and reconciliation](../SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md#operational-investigation-and-recovery) | SPEC038/039; certificate controls in SPEC001 |
| Transformation and validation | [SPEC049 — Transformation and validation error handling](SPEC-SEI-049-transformation-and-validation-error-handling.md) | SPEC005/008/015 |
| Invoice sending, including cancellation requests | [SPEC050 — Invoice sending error handling](SPEC-SEI-050-invoice-sending-error-handling.md) | SPEC023/024/043 |
| Invoice receiving, retrieval, download and ERP handoff | [SPEC051 — Invoice receiving and retrieval error handling](SPEC-SEI-051-invoice-receiving-and-retrieval-error-handling.md) | SPEC026/027/042 |
| Invoice lifecycle and reporting | [SPEC052 — Invoice lifecycle and reporting error handling](SPEC-SEI-052-invoice-lifecycle-and-reporting-error-handling.md) | SPEC029/030/041 |
| Offboarding, disconnection and exit recovery | [SPEC053 — Customer offboarding error handling](SPEC-SEI-053-customer-offboarding-error-handling.md) | SPEC032/033 |

## Existing epic and feature-plan coverage

[PRD107 — onboarding recovery](../../prds/PRD-SEI-107-public-onboarding-failure-recovery.md#functional-requirements), [PRD215 — shared resilience](../../prds/PRD-SEI-215-resilience-recovery-reconciliation-structured-review.md#overview) and [PRD225 — operational support](../../prds/PRD-SEI-225-operations-resilience-support-reconciliation.md#functional-requirements) already establish the requirement areas. The earlier ERP use-case list repeats credential, validation, platform and service failures through ON, company MCS, CII, CIL, SIR and SIL. The new stakeholder note makes investigation, historical search, versions and self-service/bulk recovery explicit. [SPEC048 §3](SPEC-SEI-048-shared-error-handling-and-operational-support.md#3-stakeholder-request-coverage) maps those requests without copying raw notes.

All new documents are unpublished drafts. SPEC004 keeps its existing identity and publication metadata; local edits do not publish it. No release capability, endpoint, retention period or automatic replay permission is approved by this split.
