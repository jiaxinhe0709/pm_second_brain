# Solution specifications

Start with the feature folders. Each contains a solution summary, logical feature
specification, and sequence/reuse assessment. Their combined predecessors are
retained in the archive. Follow the folder links to their detailed rules,
inventories, decisions and acceptance mappings when needed.

## Feature reading routes

| Feature folder | Primary review set | Archived supporting baseline |
|---|---|---|
| [Customer onboarding](onboarding/README.md) | SPEC-SEI-018, 019, 021 | [SPEC-SEI-002](archive/SPEC-SEI-002-onboarding-solution-specification.md) |
| [Invoice sending](invoice-sending/README.md) | SPEC-SEI-022–024 | [SPEC-SEI-007](archive/SPEC-SEI-007-invoice-sending-solution.md) |
| [Invoice receiving, retrieval and download](invoice-receiving/README.md) | SPEC-SEI-025–027 | [SPEC-SEI-016](archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) |
| [Invoice lifecycle](invoice-lifecycle/README.md) | SPEC-SEI-028–030 | [SPEC-SEI-009](archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) |
| [Customer offboarding](offboarding/README.md) | SPEC-SEI-031–033 | [SPEC-SEI-003](archive/SPEC-SEI-003-offboarding-solution-specification.md) |

The [publication configuration](../config/confluence.yml) selects SPEC-SEI-018 for
the stable onboarding summary page, with SPEC-SEI-019 and 021 as companions. It
still selects SPEC-SEI-007, 016, 009 and 003 for the other four topics. Their folder
sets are unpublished drafts. File location does not change lifecycle or publication
state.

## Specifications without a replacement folder

These remain active. Journey-level coverage in a feature folder does not replace
their separate capability or contract scope.

| Scope | Specification |
|---|---|
| Certificate management | [SPEC-SEI-001](SPEC-SEI-001-certificate-management-solution-specification.md) |
| UBL validation and correction | [SPEC-SEI-005](SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) |
| Spain UBL mapper migration to DTS | [SPEC-SEI-008](SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) |
| Public-platform connector | [SPEC-SEI-011](SPEC-SEI-011-public-platform-connector-solution-specification.md) |
| Public recipient-information lookup | [SPEC-SEI-012](SPEC-SEI-012-consult-public-platform-for-recipient-information.md) |
| Provider API through the Global API | [SPEC-SEI-013](SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md) |
| Shared connectivity and routing | [SPEC-SEI-014](SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) |
| Invoice creation | [SPEC-SEI-015](SPEC-SEI-015-invoice-creation-solution-specification.md) |
| B2B Router adapter binding | [SPEC-SEI-017](SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md) |

## Archive coverage review

Review date: 22 October 2026. All 33 specification files were inventoried. The five
combined sources were compared with their folder sets for scenarios, activities,
rules, failure/recovery, technical detail, acceptance and source references. An ID
range or predecessor link alone does not establish replacement coverage.

**Five combined predecessors are archived as retained baselines:** SPEC-SEI-002,
003, 007, 009 and 016. Their feature folders cover the main journeys, rules,
failures and recovery. Detailed predecessor material remains accessible through
the updated links below. This follows the existing SPEC-SEI-020/021 arrangement;
it does not claim that the folder files contain every field or technical check.

Archive here is a reading-route change. These baselines remain required where a
current view cites them. Their business text, permanent IDs, lifecycle statuses
and publication settings are retained. Only relative links changed within the
moved files. The nine capabilities without replacement folders remain active.

| Archived baseline | Coverage in the feature folder | Detail retained through archive links |
|---|---|---|
| SPEC-SEI-002 | ONB-S01–08, ONB/OFR activities, recovery and compact acceptance. | [SEI019 §7](onboarding/SPEC-SEI-019-customer-onboarding-logical-feature-specification.md#7-traceability-and-supporting-artefacts) retains links to ONB/OFR interactions and records, customer/system/public field inventories, original verification mappings and release gates. Its decision register also remains in 002. |
| SPEC-SEI-007 | OUT activities, failure/recovery, public binding and compact acceptance. | [SEI023 §§4–6](invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#4-shared-controls-and-spain-binding) still uses the predecessor's invariant/requirement register, OUT-INT-01–11, OUT-D01–12, OUT-AXC-R01–07 withdrawal traceability and detailed assurance mappings. |
| SPEC-SEI-016 | Public/private acquisition, capture, receiving, saved-file access and recovery. | [SEI026 §§3–6](invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#3-process-and-activity-order) retains detailed PRI/RSD/RCV conditions and original acceptance in REF-BASE. Full interaction/data inventories, RRI/RCV/RSD controls and decision records remain in 016. |
| SPEC-SEI-009 | LCS-01–10, LCS-R01–14, reporting/recovery and compact acceptance. | [SEI029 §§4–6](invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#4-functional-requirements-and-invariants) still binds to LCS-I01–09, the destination/obligation table, detailed SPFE controls, 52-row Annex II field matrix and assurance mappings. Provider-specific lifecycle tables and interaction/data inventories remain in 009. |
| SPEC-SEI-003 | OFF-01–08, scenarios, cutoff, historical support, export and additional acceptance. | [SEI032 §2](offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md#2-state-invariants-and-workflow) retains OFF-I01–08 in 003; [§§6–7](offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md#6-requirements-and-operational-controls) explicitly retains authoritative OFF-R01–10 and OFF-A01–11 there. OFF-INT-01–10 and OFF-D01–09 also remain supporting sources for SEI033. |

This is a document-coverage review. It does not validate external contracts,
approve implementation or resolve the recorded product and engineering gates.
The [archive index](archive/README.md) identifies all nine retained sources and
distinguishes their publication settings.
