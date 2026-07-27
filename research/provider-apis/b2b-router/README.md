# B2B Router API evidence

## Evidence status

Status: public developer documentation available; endpoint inventory can proceed without partner access.

Retrieved: 2026-07-27

## Official sources

| Source | URL | Use |
|---|---|---|
| Developer overview | https://docs.b2brouter.net/en/developers/overview/ | API concepts, versioning, environments, tools |
| Getting started | https://docs.b2brouter.net/en/developers/start-using-our-api/get-started/ | End-to-end account, transport, directory, invoice, and retrieval flow |
| API reference | https://developer.b2brouter.net/reference | Endpoint reference |
| Webhooks guide | https://developer.b2brouter.net/docs/webhooks_guide | State-change notification discovery |
| Directory guide | https://developer.b2brouter.net/docs/directory | Recipient and transport lookup |
| Spain VeriFactu guide | https://docs.b2brouter.net/en/developers/guides-by-country/spain/verifactu/ | Spain tax-reporting capability; not evidence of B2B routing rules |

## Confirmed public capability snapshot

| Area | Public evidence | Status |
|---|---|---|
| API style | REST with JSON-oriented guidance | Confirmed |
| Authentication | API key examples using `X-B2B-API-Key`; current reference must confirm production convention | Confirmed with validation required |
| Versioning | `X-B2B-API-Version` appears in current examples; changelog and migration guides are public | Confirmed |
| Environments | Sandbox/staging and production are documented | Confirmed |
| Accounts | Create/list/update guidance is public | Confirmed |
| Directory | Country and identifier lookup is documented | Confirmed |
| Contacts | Create and retrieve contacts | Confirmed |
| Transport configuration | Transport APIs and guides are public | Confirmed |
| Outbound invoices | Create/import and asynchronously send invoices | Confirmed |
| Invoice retrieval | List, retrieve, render/download legal document | Confirmed |
| Inbound invoices | Received-invoice concepts are public | Confirmed; exact integration flow to inventory |
| Webhooks | State-change webhook guide is public | Confirmed; guarantees to validate |
| Attachments | Upload and retrieve attachment behaviour is public | Confirmed |
| Formats | JSON mapping plus UBL, CII, Facturae and other format guidance | Confirmed |
| Tax reporting | Spain VeriFactu functionality is documented | Confirmed but separate from Phase 2 private routing |

## Initial endpoint inventory

The exact versioned reference must be captured before engineering commitment.

| Capability | Publicly documented operation |
|---|---|
| List accounts | `GET /accounts` |
| Configure transport | `POST /accounts/{ACCOUNT_ID}/transports` |
| Directory lookup | `GET /directory/{country}/{identifier}` |
| List contacts | `GET /accounts/{ACCOUNT_ID}/contacts` |
| Create contact | `POST /accounts/{ACCOUNT_ID}/contacts` |
| Create/import invoice | `POST /accounts/{ACCOUNT_ID}/invoices` |
| List invoices | `GET /accounts/{ACCOUNT_ID}/invoices` |
| Retrieve invoice | `GET /invoices/{INVOICE_ID}` |
| Render invoice format | `GET /invoices/{INVOICE_ID}/as/{document_type_code}` |
| Retrieve legal document | `GET /invoices/{INVOICE_ID}/as/legal` |
| Add attachment | `POST /invoices/{INVOICE_ID}/add_attachment` |
| Tax-report detail | `GET /tax_reports/{TAX_REPORT_ID}` |

## Product implications

- B2B Router is currently the strongest candidate for early technical discovery because its public documentation covers an end-to-end flow.
- B2B Router transport configuration must not be confused with the Sage route resource; the adapter must translate between them.
- VeriFactu/tax reporting must remain separate from the private B2B route unless the local team confirms a combined journey.
- The directory capability may provide route evidence, but it must not be treated as Spain's authoritative routing source until consultation confirms it.

## Information still required

- Authoritative Spain B2B private-platform onboarding and registration process.
- Exact sending and receiving scope for Sage's intended contract.
- Provider idempotency guarantees for account, transport, and invoice mutations.
- Webhook signing, retry schedule, event identity, and ordering guarantees.
- Rate limits and commercial transaction definitions for the intended subscription.
- Deregistration and historical invoice access behaviour.
- Data residency, retention, support, and SLA.
- OpenAPI export or other machine-readable API specification and permission to store it.

