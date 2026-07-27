# Banqup (Unifiedpost) API evidence

## Evidence status

Status: public API documentation, explorer, recipes, and release notes are available. A developer account may be required for credentials and some integration artefacts.

Retrieved: 2026-07-27

## Official sources

| Source | URL | Use |
|---|---|---|
| API documentation | https://docs.btx.banqup.com/ | Guides and product-area navigation |
| API recipes | https://docs.btx.banqup.com/docs/recipes/overview | End-to-end authorisation and invoice flows |
| Developer portal | https://dev.btx.banqup.com/ | App registration and credentials |
| API explorer | https://docs.btx.banqup.com/api-explorer | Endpoint discovery |
| Release notes | https://docs.btx.banqup.com/release-notes | Version and change monitoring |

## Confirmed public capability snapshot

| Area | Public evidence | Status |
|---|---|---|
| Developer portal | App credentials can be created and revoked | Confirmed |
| Authorisation | App access token and OAuth 2.0 authorisation-code recipes are published | Confirmed |
| API domains | Foundation, Invoicing, Payments, Identity, Workspace, Network, Extensions, Product, and Tax explorers | Confirmed |
| Sales invoices | Upload, validate, and send sales invoice recipe | Confirmed |
| Purchase invoices | Purchase-invoice processing recipe | Confirmed |
| Documents | Document-focused guides and recipes | Confirmed |
| Workspaces/entities | Space and entity identifiers are part of the public integration model | Confirmed |
| Network connections | Connection identifiers are referenced publicly | Confirmed; semantics require inventory |
| Release management | Public release notes | Confirmed |

## Initial journey inventory

| Journey | Publicly documented steps |
|---|---|
| Grant permissions | Banqup user grants application permissions |
| Create credentials | Developer creates/revokes application credentials |
| Obtain access token | Application exchanges credentials for access |
| Delegated authorisation | OAuth 2.0 authorisation-code flow |
| Process sales invoice | Upload, validate, and send |
| Process purchase invoice | Retrieve and perform supported workflow actions |

Exact endpoints, request schemas, scopes, webhook guarantees, and Spain-specific network behaviour must be extracted from the explorer before engineering commitment.

## Product implications

- The Banqup permission model may require explicit customer consent in the Sage onboarding journey.
- Space, entity, plugin-interface, and connection identifiers need mapping to Sage customer, legal entity, adapter connection, and route concepts.
- Banqup's broad platform API must be narrowed to the Spain e-invoicing product boundary; payments and unrelated workspace functions are outside Phase 2 unless separately approved.

## Information still required

- Exact Banqup/Unifiedpost product and contractual API for Spain private-platform connectivity.
- Spain-supported invoice types, formats, directions, and lifecycle states.
- Production and sandbox base URLs and tenant-provisioning process.
- Required OAuth scopes and consent/administrator roles.
- Inbound notification mechanism and webhook security/delivery guarantees.
- Idempotency behaviour, rate limits, pagination, and payload/attachment limits.
- Network directory and routing semantics.
- Reconciliation, deregistration, historical access, retention, and SLA.
- Downloadable OpenAPI/Postman artefacts and permission to retain them.

