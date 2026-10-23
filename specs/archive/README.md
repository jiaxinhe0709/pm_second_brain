# Archived specifications

Start new reviews from the [feature reading routes](../README.md). Archived files
preserve permanent IDs and earlier analysis. Some remain required supporting
references; archive location does not mean that all their detail was copied into a
successor or that their lifecycle status changed.

## Combined baselines for the feature folders

The feature folders are the main review route. These five files retain supporting
rules, inventories, decisions and acceptance detail cited by the new views. Their
business content and metadata are preserved; relative links were adjusted for the
moves. They remain required references where cited.

| Retained baseline | Current feature views |
|---|---|
| [SPEC-SEI-002 — Customer onboarding](SPEC-SEI-002-onboarding-solution-specification.md) | [Onboarding](../onboarding/README.md): SPEC-SEI-018, 019 and 021. |
| [SPEC-SEI-003 — Customer offboarding](SPEC-SEI-003-offboarding-solution-specification.md) | [Offboarding](../offboarding/README.md): SPEC-SEI-031–033. |
| [SPEC-SEI-007 — Invoice sending](SPEC-SEI-007-invoice-sending-solution.md) | [Sending](../invoice-sending/README.md): SPEC-SEI-022–024. |
| [SPEC-SEI-009 — Invoice lifecycle](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) | [Lifecycle](../invoice-lifecycle/README.md): SPEC-SEI-028–030. |
| [SPEC-SEI-016 — Receiving, retrieval and download](SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) | [Receiving](../invoice-receiving/README.md): SPEC-SEI-025–027. |

The [coverage review](../README.md#archive-coverage-review) records the journey
coverage and the detailed material that each folder still uses from its baseline.

## Earlier consolidated sources

| Preserved source | Current reading route and retained detail |
|---|---|
| [SPEC-SEI-004 — Onboarding failure and reconciliation](SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md) | [Onboarding folder](../onboarding/README.md). OFR recovery controls are integrated into [SPEC-SEI-002](SPEC-SEI-002-onboarding-solution-specification.md#onb-08-recovery) and developed in SPEC-SEI-019. |
| [SPEC-SEI-006 — Invoice receiving](SPEC-SEI-006-invoice-receiving-solution.md) | [Receiving folder](../invoice-receiving/README.md). [SPEC-SEI-016](SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) retains the combined RCV receiving, validation, duplicate, product-delivery and recovery controls. |
| [SPEC-SEI-010 — Public retrieval and download](SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md) | [Receiving folder](../invoice-receiving/README.md). SPEC-SEI-016 retains RSD discovery, capture, covered progress, stored-file access and records controls. |
| [SPEC-SEI-020 — Onboarding API reuse assessment](SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md) | [SPEC-SEI-021](../onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md) is the main engineering view. Detailed API-A01–16 checks, source conflicts and earlier analysis remain supporting references here. |

Existing historical links can continue to point to these four earlier sources.

## Publication boundary

The four earlier consolidated sources have publication disabled. Their lifecycle
statuses and historical page IDs are retained. SPEC-SEI-004, 006 and 010 are not selected in
`publication.current_sources` in [config/confluence.yml](../../config/confluence.yml).
SPEC-SEI-020 has no Confluence page ID.

The stable onboarding page `923861390` selects **SPEC-SEI-018**, with SPEC-SEI-019
and 021 as companion sources. SPEC-SEI-002 remains a retained Git supporting source.
SPEC-SEI-003, 007, 009 and 016 remain selected for their existing stable pages;
their folder sets remain unpublished. The five relocated baselines retain their
existing publication flags and page IDs. Archive location does not disable
publication. No live page, lifecycle status or publication setting changed in this
tidy-up.
