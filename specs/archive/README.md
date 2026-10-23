# Archived specifications

Start new reviews from the [feature reading routes](../README.md). Archived files
preserve permanent IDs and earlier analysis. Some remain required supporting
references; archive location does not mean that all their detail was copied into a
successor or that their lifecycle status changed.

## Earlier onboarding and provider-connectivity views

Start current reviews from [customer onboarding and connectivity](../onboarding-and-connectivity/README.md),
SPEC-SEI-037–039. These two folders retain the predecessor views and cited analysis.
Business content, permanent IDs and metadata are preserved. Relative links and
reading-route guidance changed; lifecycle and publication selections did not.

| Retained folder | Supporting scope |
|---|---|
| [Onboarding](onboarding/README.md): SPEC-SEI-018, 019, 021 | Earlier customer scenarios, rules, acceptance and API reuse analysis. Current Confluence sources are SPEC-SEI-037–039. |
| [Provider connectivity](provider-connectivity/README.md): SPEC-SEI-034–036 | Earlier connectivity review, runtime sending/receiving, file formats and reuse evidence. Cited runtime detail remains required. |

## Combined baselines for the feature folders

The feature folders are the main review route. These five files retain supporting
rules, inventories, decisions and acceptance detail cited by the new views. Their
business content and metadata are preserved; relative links were adjusted for the
moves. They remain required references where cited.

| Retained baseline | Current feature views |
|---|---|
| [SPEC-SEI-002 — Customer onboarding](SPEC-SEI-002-onboarding-solution-specification.md) | [Onboarding and connectivity](../onboarding-and-connectivity/README.md): SPEC-SEI-037–039; earlier [018/019/021](onboarding/README.md) remain supporting views. |
| [SPEC-SEI-003 — Customer offboarding](SPEC-SEI-003-offboarding-solution-specification.md) | [Offboarding](../offboarding/README.md): SPEC-SEI-031–033. |
| [SPEC-SEI-007 — Invoice sending](SPEC-SEI-007-invoice-sending-solution.md) | [Sending](../invoice-sending/README.md): SPEC-SEI-022–024. |
| [SPEC-SEI-009 — Invoice lifecycle](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) | [Lifecycle](../invoice-lifecycle/README.md): SPEC-SEI-028–030. |
| [SPEC-SEI-016 — Receiving, retrieval and download](SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) | [Receiving](../invoice-receiving/README.md): SPEC-SEI-025–027. |

The [coverage review](../README.md#archive-coverage-review) records the journey
coverage and the detailed material that each folder still uses from its baseline.

## Earlier consolidated sources

| Preserved source | Current reading route and retained detail |
|---|---|
| [SPEC-SEI-004 — Onboarding failure and reconciliation](SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md) | [Onboarding and connectivity](../onboarding-and-connectivity/README.md). OFR recovery controls remain in [SPEC-SEI-002](SPEC-SEI-002-onboarding-solution-specification.md#onb-08-recovery), the retained SPEC-SEI-019 and current SPEC-SEI-038. |
| [SPEC-SEI-006 — Invoice receiving](SPEC-SEI-006-invoice-receiving-solution.md) | [Receiving folder](../invoice-receiving/README.md). [SPEC-SEI-016](SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) retains the combined RCV receiving, validation, duplicate, product-delivery and recovery controls. |
| [SPEC-SEI-010 — Public retrieval and download](SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md) | [Receiving folder](../invoice-receiving/README.md). SPEC-SEI-016 retains RSD discovery, capture, covered progress, stored-file access and records controls. |
| [SPEC-SEI-020 — Onboarding API reuse assessment](SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md) | [SPEC-SEI-039](../onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md) is the current engineering view; [021](onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md) is its retained predecessor. Detailed API-A01–16 checks, source conflicts and earlier analysis remain here. |

Existing historical links can continue to point to these four earlier sources.

## Publication boundary

The four earlier consolidated sources have publication disabled. Their lifecycle
statuses and historical page IDs are retained. SPEC-SEI-004, 006 and 010 are not selected in
`publication.current_sources` in [config/confluence.yml](../../config/confluence.yml).
SPEC-SEI-020 has no Confluence page ID.

The stable onboarding page `923861390` selects **SPEC-SEI-037**, with SPEC-SEI-038
and 039 as companion sources. The archived 018/019/021 retain their historical page IDs;
the source-selection guard prevents them from overwriting the successor pages. SPEC-SEI-002 remains a retained Git supporting source.
SPEC-SEI-003, 007, 009 and 016 remain selected for their existing stable pages;
their folder sets remain unpublished. The five relocated baselines retain their
existing publication flags and page IDs. Archive location does not disable
publication. The archive move did not change lifecycle or publication state. Subsequent authorised
publication selects 037–039 for the three existing onboarding pages; lifecycle statuses remain unchanged.
