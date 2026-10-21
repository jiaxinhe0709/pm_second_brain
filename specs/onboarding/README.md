# Customer onboarding

Use this folder to review onboarding through three complementary views. All three specifications are unpublished drafts.

| Read | Purpose |
|---|---|
| [Solution Summary](SPEC-SEI-018-customer-onboarding-solution-summary.md) | Understand the end-to-end outcome, scope, workflow, responsibilities and material decisions. Start here. |
| [Logical Feature Specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) | Review required behaviour, activity rules, failures, recovery and acceptance scenarios. |
| [API Design and Reuse Assessment](SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md) | Review the five supplied FR operations, API-labelled sequences, Spain changes and implementation evidence gaps. |

## Product requirements and original specification

The existing PRDs remain the product requirements sources. This landing page adds navigation; it does not replace or duplicate them.

| Source | Scope |
|---|---|
| [PRD-SEI-101 Public platform onboarding](../../prds/PRD-SEI-101-public-platform-onboarding.md) | Phase 1 public readiness. |
| [PRD-SEI-104 Accountant and single-client onboarding](../../prds/PRD-SEI-104-accountant-and-single-client-onboarding.md) | Direct and delegated access, client isolation and portfolio work. |
| [PRD-SEI-107 Onboarding failure recovery](../../prds/PRD-SEI-107-public-onboarding-failure-recovery.md) | Correction, safe retry, reconciliation and manual recovery. |
| [PRD-SEI-222 Customer onboarding and migration](../../prds/PRD-SEI-222-customer-onboarding-entry-point-migration.md) | Private setup, authorised route changes and historical continuity. |
| [Original SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md) | Unchanged combined specification. Retains detailed technical analysis, field inventories, decision records and original acceptance coverage. |

## Directory and publication boundary

This is the onboarding pilot for a feature-folder structure. Shared diagrams stay in [assets/diagrams](../../assets/diagrams/); shared terminology and source evidence stay in [context](../../context/). Other feature directories are unchanged.

SPEC-SEI-018, SPEC-SEI-019 and SPEC-SEI-020 keep their own permanent document IDs. Existing ONB and OFR behaviour IDs retain their meanings. Each document explains its relationship to SPEC-SEI-002 in its Revision overview. The [FR source contracts](<../../context/FR API/Onboarding/>) remain unchanged evidence inputs.

The stable onboarding Confluence page `923861390` still selects **SPEC-SEI-002** in [the publication configuration](../../config/confluence.yml). None of the three companions is selected for publication.

## Confluence presentation

Present three sibling pages under the existing onboarding feature/PRD page (`837610648`). Keep the README as local navigation; do not create another Confluence page merely for the directory.

| Confluence view | Git source | Proposed page handling |
|---|---|---|
| Onboarding Solution Summary | SPEC-SEI-018 | Reuse the existing specification page `923861390`, preserving its URL/history. |
| Onboarding Logical Feature Specification | SPEC-SEI-019 | Create one sibling under the same parent; record its returned page ID. |
| Onboarding API Design and Reuse Assessment | SPEC-SEI-020 | Create one sibling under the same parent; record its returned page ID. |

Each view links to the other two. Logical behaviour stays in 019; API allocation and FR reuse evidence stay in 020. Draw.io viewers provide full-size diagrams. Per-operation headings on the API page provide contents links without creating a page for every endpoint.

The [local preview](../../work/onboarding-api-review/index.html) shows this structure; the [publication plan](../../work/onboarding-api-review/publication-plan.json) records intended targets without changing live configuration. Sources must complete repository review and merge before publication. Before a live update, reconcile existing child titles/IDs, resolve companion links to their Confluence pages, then update the selected-source map together with publication metadata. Preserve SPEC-SEI-002 unchanged. This plan does not itself publish or change document status.
