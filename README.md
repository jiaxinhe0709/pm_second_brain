# PM Second Brain

Git is the system of record for product documents. Confluence is the publishing and discovery layer.

## Working model

1. Create or update one Markdown file per PRD or feature proposal.
2. Open a pull request early and review substantive changes in GitHub.
3. Merge approved documents to `main`.
4. Publish eligible documents to Confluence after merge.

## Repository map

- `prds/` — one file per product requirements document
- `feature-proposals/` — one file per feature proposal
- `decisions/` — durable product and architecture decisions
- `research/` — customer and market evidence
- `context/` — personas, metrics, principles, glossary, and product context
- `inbox/` — ideas and feedback awaiting triage
- `assets/` — diagrams, screenshots, and attachments
- `templates/` — document starters
- `prompts/` — reusable PM assistant workflows
- `config/` — products, document types, and non-secret publishing configuration
- `schema/` — document rules and metadata schema
- `tools/` — validation and publishing utilities

## Document identity

Use a stable ID and readable filename:

```text
PRD-BILL-001-e-invoice-pipeline.md
FP-BILL-001-validation-rules.md
ADR-001-retry-policy.md
```

Do not put versions or statuses in filenames. Git records detailed versions; front matter records lifecycle status.

## Confluence

Only documents with `confluence.publish: true` are eligible for publication. Keep credentials in GitHub Actions secrets, never in this repository.

