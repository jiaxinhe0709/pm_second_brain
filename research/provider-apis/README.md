# Spain private-platform API evidence pack

## Purpose

This folder records the API evidence used to refine the Phase 2 provider PRDs. It separates confirmed public documentation from assumptions and access gaps.

## Evidence status

| Provider | Public developer documentation | Endpoint-level evidence | Current access action |
|---|---|---|---|
| B2B Router | Available | Substantial public REST documentation | Continue inventory; request commercial limits and Spain B2B-specific confirmation |
| Banqup (Unifiedpost) | Available | Public guides, explorer, recipes, and release notes | Continue inventory; developer account may be needed for credentials and some artefacts |
| EDICOM | Not located in public discovery | Not confirmed | Request partner documentation, sandbox, and technical contact |
| SERES (Docaposte) | Public product information | Public API claim but no endpoint reference located | Request API specification, sandbox, and technical contact |
| ZeroComa | Public product information | No public endpoint reference located | Request API specification, sandbox, and technical contact |

## Storage policy

- Store our analysis, source register, capability matrix, and open questions under `research/provider-apis/`.
- Store downloadable OpenAPI files, JSON schemas, Postman collections, and provider-supplied diagrams under `assets/provider-apis/` only when Sage is permitted to retain them.
- Do not store API keys, tokens, passwords, certificates, customer data, or confidential raw exports.
- Do not mirror entire documentation websites.
- Record provenance, version, retrieval date, access classification, and storage permission for every saved artefact.

## Common discovery checklist

Each provider investigation must establish:

1. product and API in scope;
2. Spain public/private platform role;
3. authentication and authorisation;
4. tenant, account, and legal-entity provisioning;
5. sandbox and production environments;
6. supported invoice directions, types, and formats;
7. recipient/network directory lookup;
8. invoice creation/import and submission;
9. inbound retrieval and/or webhook delivery;
10. lifecycle status, rejection, correction, cancellation, and payment-state operations;
11. idempotency and duplicate protection;
12. webhook authentication, ordering, replay, and retry;
13. reconciliation and authoritative state retrieval;
14. rate, payload, pagination, and attachment limits;
15. deregistration and historical invoice access;
16. API versioning, change notices, support, and SLA;
17. security, privacy, data residency, and retention.

## Related PRDs

- `PRD-SEI-201` — Spain Public and Private Platform Transition
- `PRD-SEI-202` — Spain Private Platform Connection and Routing Foundation
- `PRD-SEI-203` — Spain Private Platform Resilience and Operations
- `PRD-SEI-204` to `PRD-SEI-208` — provider integrations

