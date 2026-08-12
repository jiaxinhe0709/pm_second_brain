---
id: PRD-SEI-231
title: E-Invoicing — Country Identifiers, Tenancy and Delegated Accountants
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-08-12
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-223
  - PRD-SEI-226
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: "866152234"
  title: E-Invoicing — Country Identifiers, Tenancy and Delegated Accountants
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Country Identifiers, Tenancy and Delegated Accountants

## Decision summary

Model Sage access context, legal identity, tax identity, network address and delegated authority as separate, related records. Do not attach country identifiers directly to `tenantId` or `datasetId`, and do not treat a credential as proof that an accountant may act for every client or operation.

For France, the corrected cardinality is: an accountant portfolio may contain many client **SIRENs**; each legal unit has one SIREN and may have many establishment **SIRETs**. A SIRET contains the SIREN plus an establishment-specific NIC. [French official guidance](https://entreprendre.service-public.gouv.fr/vosdroits/F32135) gives the example `1 SIREN + 3 SIRETs` for one head office and two shops.

This is a discovery contract, not an approved physical schema or API.

## Identity and authority map

<!-- confluence-html-macro:start -->
<div class="eii-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eii-map *{box-sizing:border-box}.eii-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eii-map svg{display:block;width:1100px;height:590px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eii-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eii-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eii-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eii-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eii-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eii-map .copy{fill:#42526e;font-size:8.5px}.eii-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eii-map .path{fill:none;stroke:#00875a;stroke-width:2}.eii-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eii-map .arrow{fill:#00875a}.eii-map .arrow-g{fill:#6b778c}.eii-map .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eii-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eii-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">One internal access context can reference several legal entities; each legal entity can carry country identities, establishments and network addresses. Delegation is an explicit scoped edge.</p>
  <svg viewBox="0 0 1100 590" role="img" aria-label="Two onboarding paths lead to a common identity graph. A direct client is authorised for one or more workspaces. An accountant firm and its users have explicit delegated authority to selected client workspaces only. A workspace contains tenant and dataset access context, which references a legal entity but is not embedded in the official identifier. The French example shows one client legal unit with one SIREN and multiple SIRETs for establishments. Tax identifiers, Peppol participant addresses and credentials remain separate records. Every action binds actor, authority, client legal entity, capability, country, direction and effective time.">
    <text x="32" y="30" class="label">ACCESS PATH</text><text x="392" y="30" class="label">SAGE CONTEXT</text><text x="738" y="30" class="label">LEGAL / COUNTRY / NETWORK IDENTITY</text>
    <rect x="32" y="62" width="220" height="78" rx="10" class="main"/><text x="52" y="91" class="title">Direct client</text><text x="52" y="112" class="copy">Owner/admin acts for own business</text><text x="52" y="128" class="copy">interactive or bounded bulk operations</text>
    <rect x="32" y="190" width="220" height="98" rx="10" class="main"/><text x="52" y="219" class="title">Accountant firm + authorised user</text><text x="52" y="240" class="copy">Portfolio may contain many client SIRENs</text><text x="52" y="258" class="copy">batch is execution mode, not authority</text><text x="52" y="276" class="copy">no implicit access to another client</text>
    <path d="M252 101 H330 V168 H392" class="path"/><polygon points="392,168 382,162 382,174" class="arrow"/>
    <path d="M252 238 H300" class="path-opt"/><polygon points="300,238 290,232 290,244" class="arrow-g"/>
    <rect x="302" y="198" width="220" height="80" rx="10" class="optional"/><text x="322" y="226" class="title">Delegated authority grant</text><text x="322" y="247" class="copy">client • capability • direction • country</text><text x="322" y="264" class="copy">effective interval • evidence • revocation</text>
    <path d="M412 198 V178" class="path-opt"/><polygon points="412,178 406,188 418,188" class="arrow-g"/>
    <rect x="392" y="128" width="220" height="100" rx="10" class="main"/><text x="412" y="157" class="title">Workspace / access context</text><text x="412" y="178" class="copy">tenantId • datasetId? • product/account</text><text x="412" y="196" class="copy">internal references and permissions</text><text x="412" y="214" class="copy">dataset meaning/cardinality is an open gate</text>
    <path d="M612 178 H680" class="path"/><polygon points="680,178 670,172 670,184" class="arrow"/>
    <rect x="682" y="128" width="210" height="100" rx="10" class="main"/><text x="702" y="157" class="title">Client legal entity</text><text x="702" y="178" class="copy">stable Sage entity reference</text><text x="702" y="196" class="copy">country establishment and tax context</text><text x="702" y="214" class="copy">one workspace may reference 1..n by policy</text>
    <path d="M787 228 V274" class="path"/><polygon points="787,274 781,264 793,264" class="arrow"/>
    <rect x="620" y="276" width="334" height="130" rx="10" class="finish"/><text x="640" y="305" class="title">France identity example</text><text x="640" y="327" class="copy">Legal unit — one SIREN (9 digits)</text><text x="640" y="349" class="copy">├─ Head office — SIRET A (SIREN + NIC)</text><text x="640" y="371" class="copy">├─ Establishment — SIRET B</text><text x="640" y="393" class="copy">└─ Establishment — SIRET C</text>
    <rect x="302" y="330" width="248" height="76" rx="10" class="optional"/><text x="322" y="359" class="title">Tax identities</text><text x="322" y="380" class="copy">NIF / VAT / country registration</text><text x="322" y="397" class="copy">scheme + value + country + validity</text>
    <rect x="302" y="442" width="248" height="76" rx="10" class="optional"/><text x="322" y="471" class="title">Peppol participant addresses</text><text x="322" y="492" class="copy">scheme + value • 0..n per entity/context</text><text x="322" y="509" class="copy">discovery identity, not provider company</text>
    <rect x="620" y="442" width="334" height="76" rx="10" class="warn"/><text x="640" y="471" class="title">Credential / certificate reference</text><text x="640" y="492" class="copy">proves authentication; does not itself prove authority</text><text x="640" y="509" class="copy">custody • purpose • environment • expiry • rotation</text>
    <path d="M682 208 H582 V368 H550" class="path-opt"/><polygon points="550,368 560,362 560,374" class="arrow-g"/>
    <path d="M682 218 H580 V480 H550" class="path-opt"/><polygon points="550,480 560,474 560,486" class="arrow-g"/>
    <path d="M787 406 V442" class="path-opt"/><polygon points="787,442 781,432 793,432" class="arrow-g"/>
    <rect x="180" y="542" width="740" height="30" rx="15" class="finish"/><text x="276" y="562" class="title">Action context = actor + authority + client entity + identifier + capability + direction + effective time</text>
  </svg>
  <div class="notes"><div class="note"><strong>No identifier stuffing</strong>Internal IDs reference identity records; they do not become part of SIREN, SIRET, NIF or a Peppol address.</div><div class="note"><strong>Authority is narrower than access</strong>A login, API key or certificate never grants portfolio-wide rights by implication.</div><div class="note"><strong>Batch preserves isolation</strong>Every item is authorised, processed, evidenced and failed independently for its client entity.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Persona and processing differences

| Concern | Direct client | Accountant / portfolio |
|---|---|---|
| Authority | Own-business role and approved product access | Explicit relationship to each client plus capability-specific representation evidence |
| Cardinality | One or more workspaces/legal entities according to product model | Many client workspaces/legal entities; no transitive access |
| Processing | Interactive or bounded bulk | Async batch may improve scale, but each record has its own outcome and idempotency key |
| Credential | Client, Sage or provider credential according to approved route | Firm/user credential may authenticate; authority must still be proven per client and operation |
| Visibility | Own invoices, statuses and evidence | Only authorised client, direction, period and operations; portfolio aggregate must not leak item data |

The earlier draft `POST /api/v1/es/onboarding/profile` and `/batch` paths are useful scenario sketches only. Endpoint names, `202` behaviour and certificate ownership are not approved by this PRD.

## Business rules

| ID | Rule |
|---|---|
| BR1 | Store every external identifier as `scheme + value + issuing country/authority + subject level + validity`; never infer its type from length alone. |
| BR2 | Bind official identities to a Sage legal-entity reference through versioned associations; `tenantId` and `datasetId` remain internal access/context identifiers. |
| BR3 | A French legal unit has one SIREN and can have multiple establishment SIRETs; an accountant portfolio can contain multiple client SIRENs. |
| BR4 | A Peppol participant address is a network/discovery identity. It may reuse a national identifier value, but its scheme and role remain explicit. |
| BR5 | Delegated authority must identify principal/client, delegate, permitted capability, direction, country, effective interval, source evidence and revocation state. |
| BR6 | Credential possession proves authentication only; execution requires both a valid credential reference and a valid authority decision. |
| BR7 | Submission, consultation/retrieval, correction, payment reporting and onboarding are separately authorisable capabilities. |
| BR8 | Batch acceptance is not client success. Each record receives an isolated result, correlation, retry policy and audit trail. |

## Requirements and acceptance

| ID | Requirement / acceptance |
|---|---|
| ID-FR1 | The platform must resolve `tenantId → workspace/access context → Sage legal entity → country identity` without embedding the official identifier in an internal ID. |
| ID-FR2 | The model must support one legal entity to many establishments and many country/network identifiers, with effective dates and no silent overwrite. |
| ID-FR3 | The model must support an accountant firm and authorised users acting for many client legal entities while denying unlinked clients. |
| ID-FR4 | Every operation must evaluate actor, client entity, authority grant, capability, direction, credential and effective time before external mutation or protected retrieval. |
| ID-FR5 | Batch execution must authorise and isolate each item, permit partial success, prevent cross-client idempotency collisions and return per-item customer-safe outcomes. |
| ID-AC1 | Given one SIREN with three active establishments, when identity is resolved, then all three SIRETs remain distinct and traceable to the same legal unit. |
| ID-AC2 | Given an accountant can submit for client A but cannot consult for client A or access client B, when those actions are attempted, then only the authorised submission proceeds and both other actions are denied with audit. |
| ID-AC3 | Given the same tax identifier appears in two schemes or countries, when it is stored, then the scheme/country prevents collision and no identity is merged automatically. |

## Evidence and open gates

| Evidence | Finding | Status / impact |
|---|---|---|
| [French government SIREN/SIRET guidance](https://entreprendre.service-public.gouv.fr/vosdroits/F32135), verified 2025-01-30 | SIREN uniquely identifies the enterprise/legal unit; SIRET identifies each establishment and is SIREN + NIC | Confirmed hierarchy; drives BR3 and ID-AC1 |
| [AEAT VERI*FACTU delegation FAQ](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/cuestiones-generales-cumplimiento-delegacion.html), accessed 2026-08-12 | Third-party/self-billing submission can require registered power; social-collaboration representation uses specified forms and distinguishes professional/software-provider paths | Official but specific to RRSIF/VERI*FACTU; do not generalise to every Spanish e-invoice operation |
| [AEAT social-collaboration FAQ](https://sede.agenciatributaria.gob.es/Sede/colaborar-agencia-tributaria/colaboracion-social-presentacion-declaraciones/preguntas-frecuentes-sobre-colaboracion-social.html), accessed 2026-08-12 | Social collaboration is procedure-bounded and does not automatically confer broader intervention or receipt rights | Supports capability-specific authority, not a universal master-certificate rule |
| [Accountant & Single Client — Domain Services Team](https://confluence.sage.com/spaces/DNBU/pages/848078252/Accountant+Single+Client), supplied research | Proposes direct and batch paths, asymmetric send/retrieve authority and strict client isolation | Internal discovery input; exact APIs, `SENDING_ONLY` rule and SPFE applicability require Spanish legal/product validation |

Open gates: define the product meaning/cardinality of `datasetId`; approve the legal-entity/workspace model; obtain country identifier catalogs; confirm Spanish authority per operation; choose credential custody; and validate accountant/direct journeys with security, privacy and users.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-12 | Initial child discovery PRD; corrected SIREN/SIRET cardinality and combined identity, tenancy, Peppol address and accountant-delegation analysis | User feedback, supplied research and official French/Spanish sources |
| 2026-08-12 | Published as a child of commonality page `866150169` | User publication approval |
