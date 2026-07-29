# PRD-SEI-201 Spain use-case evidence

## Source

| Attribute | Value |
|---|---|
| Source | `eInvoicing Spain Use Cases.pptx` |
| Source date | May 2026 |
| Supplied | 2026-07-29 |
| Evidence type | Internal discovery material |
| Confidence | Business scenarios are useful; regulatory and technical claims require validation |
| Used by | PRD-SEI-201, PRD-SEI-202, PRD-SEI-203 and relevant lifecycle/onboarding work |

The raw presentation is not copied into the repository. This note records the product scenarios and decisions it informs.

## Use cases identified

| ID | Use case | Business flow | Product implication | Evidence limitation |
|---|---|---|---|---|
| UC1 | Public → Public default flow | Issuer submits UBL to public platform; receiver retrieves and reports invoice/payment status | Public retrieval, lifecycle status, payment status, notifications | No-push and four-day auto-acceptance claims require official confirmation |
| UC2 | Public → Private | Issuer submits to public; receiver's private platform retrieves relevant invoices | Platform identification and detection/notification | Claim that no central directory exists and proposed UBL endpoint field require confirmation |
| UC3 | Multiple platforms for one company | Company may use more than one private platform and select a target per invoice | Multiple connections and potential per-invoice selection | Conflicts with current Phase 2 non-goal; priority and regulatory mechanics open |
| UC4 | Private-platform format transformation | Private platform transforms UBL to/from Facturae, EDIFACT or other formats and sends a trusted UBL copy to public | Preserve original/transformed documents and avoid data loss | Exact transformation responsibility and supported formats require provider/regulatory evidence |
| UC5 | Invoice retrieval | Public invoices are retrieved through periodic, trigger-based or configurable polling | Shared batching, rate limiting, alerts and pending-invoice visibility | Polling model, frequency and auto-acceptance window require confirmation |
| UC6 | Dual-channel delivery | E-invoice and human-readable PDF are delivered in parallel during transition | Correlate channels and prevent duplicate business processing | Legal duration, channel obligations and synchronisation rules require confirmation |
| UC7 | Corrections/adjustments | Rejection or later credit note/corrective invoice resolves an error | Document linkage and clear accepted-but-corrected lifecycle | Exact correction/status rules require local-team confirmation |
| UC8 | Accountant cross-product visibility | Accountant retrieves client invoices/lifecycle using delegated authorisation/certificate | Delegation, multi-certificate UX, cross-product identity and synchronisation | Credential ownership, authorisation and duplication controls remain open |

## Implications for Phase 2

### Directly aligned

- multiple public/private connections for a legal entity;
- independent inbound/outbound route capability;
- public → private reachability and retrieval responsibility;
- invoice/network context and lifecycle continuity;
- resilience for polling, missed events, duplicates and ambiguous state.

### Dependencies or adjacent scope

- format transformation belongs in provider/canonical-document capability and data-preservation analysis;
- polling/status/payment behaviour belongs in public lifecycle and resilience work;
- correction/credit-note linkage belongs in invoice lifecycle requirements;
- accountant visibility belongs in identity, authorisation, certificate and cross-product access.

### Scope decisions required

1. Does Phase 2 support more than one private connection per legal entity?
2. Does Phase 2 allow a default provider plus per-invoice override?
3. What authoritative data identifies the receiver's platform?
4. Which platform is responsible for retrieving public invoices for a private receiver?
5. Which format is canonical and which original/transformed artefacts must be retained?
6. Which regulatory claims in the presentation are confirmed by official sources?

## Research actions

- Validate public-platform polling, notification and acceptance timing with the Spain local team and official specification.
- Validate route/directory and endpoint-field claims.
- Obtain provider-specific transformation, format and trusted-copy behaviour.
- Define correction, rejection and payment-status ownership across route changes.
- Define accountant delegation and certificate ownership separately from platform connection credentials.
