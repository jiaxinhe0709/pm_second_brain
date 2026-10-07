---
id: PRD-SEI-233
title: E-Invoicing — Peppol Multi-Address and Endpoint Routing
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-10-07
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-223
  - PRD-SEI-231
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: "866152236"
  title: E-Invoicing — Peppol Multi-Address and Endpoint Routing
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Peppol Multi-Address and Endpoint Routing

An **exchange action** is one separately tracked action, such as delivering an invoice, submitting a public copy or reporting an invoice event. Each action has its own result. See the [shared definition](../context/GLO-SEI-001-e-invoicing-terminology.md#invoices-representations-and-rules).

## Decision summary

Interpret “multiple Access Point addresses” as a Peppol addressing and discovery requirement, while keeping three concepts separate:

| Concept | Meaning |
|---|---|
| Peppol participant address | Scheme-qualified business/network identifier used for discovery, commonly represented as `scheme::value` and as an invoice `EndpointID` according to the applicable BIS |
| SMP service endpoint | Technical URL plus transport/certificate metadata returned for a participant, document type and process |
| Access Point provider | Certified service-provider organisation operating the sending or receiving connection |

The platform must support multiple participant addresses and one or more discovered service endpoints. It must not assume a SIREN/SIRET, invoice `EndpointID`, SMP URL, Access Point provider or Sage tenant is the same thing.

## Address discovery and immutable route selection

<!-- confluence-html-macro:start -->
<div class="eip-route" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eip-route *{box-sizing:border-box}.eip-route .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eip-route svg{display:block;width:100%;max-width:1100px;height:auto;min-width:760px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eip-route .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eip-route .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eip-route .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eip-route .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eip-route .title{fill:#172b4d;font-size:10px;font-weight:700}.eip-route .copy{fill:#42526e;font-size:8.5px}.eip-route .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eip-route .path{fill:none;stroke:#00875a;stroke-width:2}.eip-route .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eip-route .arrow{fill:#00875a}.eip-route .arrow-g{fill:#6b778c}.eip-route .notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;min-width:0;margin-top:10px}.eip-route .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eip-route .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Resolve the receiver from a scheme-qualified participant address and capability metadata; then freeze the selected execution route with the invoice exchange action.</p>
  <svg viewBox="0 0 1100 570" role="img" aria-label="A buyer legal entity has zero or more Peppol participant addresses, each with a scheme, value, country, purpose and validity. A sending system selects the intended participant address, document type and process, then performs DNS/SML and SMP discovery. SMP returns one or more technical endpoints with transport profile, certificate, service availability and effective metadata. A governed selection policy chooses an eligible endpoint and binds the sending Access Point provider, Peppol network, recipient participant, receiving endpoint and evidence version into an immutable execution route. Failed or ambiguous delivery is reconciled before trying another endpoint.">
    <text x="32" y="30" class="label">BUSINESS DESTINATION</text><text x="338" y="30" class="label">PEPPOL DISCOVERY</text><text x="748" y="30" class="label">EXECUTION</text>
    <rect x="32" y="62" width="240" height="92" rx="10" class="main"/><text x="52" y="91" class="title">Buyer legal entity / establishment</text><text x="52" y="112" class="copy">country identity and business role</text><text x="52" y="132" class="copy">not itself the Access Point or SMP URL</text>
    <path d="M152 154 V192" class="path"/><polygon points="152,192 146,182 158,182" class="arrow"/>
    <rect x="32" y="194" width="240" height="152" rx="10" class="finish"/><text x="52" y="223" class="title">Peppol participant addresses [0..n]</text><text x="52" y="246" class="copy">A — scheme::value • purpose • validity</text><text x="52" y="269" class="copy">B — scheme::value • purpose • validity</text><text x="52" y="292" class="copy">C — scheme::value • purpose • validity</text><text x="52" y="319" class="copy">Explicit association to legal entity/context</text><text x="52" y="336" class="copy">No value-only match or silent merge</text>
    <path d="M272 270 H330" class="path"/><polygon points="330,270 320,264 320,276" class="arrow"/>
    <rect x="332" y="194" width="226" height="152" rx="10" class="main"/><text x="352" y="223" class="title">Discovery key</text><text x="352" y="246" class="copy">participant scheme + value</text><text x="352" y="269" class="copy">document type identifier</text><text x="352" y="292" class="copy">process identifier</text><text x="352" y="315" class="copy">environment + discovery time</text><text x="352" y="336" class="copy">SML/DNS → authoritative SMP</text>
    <path d="M558 270 H616" class="path"/><polygon points="616,270 606,264 606,276" class="arrow"/>
    <rect x="618" y="154" width="270" height="232" rx="10" class="main"/><text x="638" y="183" class="title">SMP service metadata</text><text x="638" y="208" class="copy">Process + ServiceEndpointList</text><text x="638" y="236" class="copy">Endpoint 1 — URL • transport • certificate</text><text x="638" y="264" class="copy">Endpoint 2 — URL • transport • certificate</text><text x="638" y="292" class="copy">… one or more eligible endpoints</text><text x="638" y="322" class="copy">service activation/expiry • description</text><text x="638" y="346" class="copy">metadata source/version/freshness</text><text x="638" y="370" class="copy">capability is process/document-specific</text>
    <path d="M888 270 H938" class="path"/><polygon points="938,270 928,264 928,276" class="arrow"/>
    <rect x="940" y="194" width="126" height="152" rx="10" class="finish"/><text x="958" y="223" class="title">Selected route</text><text x="958" y="246" class="copy">sending AP role</text><text x="958" y="266" class="copy">Peppol network</text><text x="958" y="286" class="copy">participant</text><text x="958" y="306" class="copy">endpoint URL</text><text x="958" y="326" class="copy">evidence version</text>
    <rect x="332" y="62" width="556" height="62" rx="10" class="optional"/><text x="352" y="89" class="title">Selection policy</text><text x="352" y="108" class="copy">approved transport • current certificate • effective service • country/BIS rules • deterministic tie-break • no blind fallback</text>
    <path d="M753 124 V154" class="path-opt"/><polygon points="753,154 747,144 759,144" class="arrow-g"/>
    <path d="M1003 346 V404" class="path-opt"/><polygon points="1003,404 997,394 1009,394" class="arrow-g"/>
    <rect x="618" y="404" width="448" height="92" rx="10" class="warn"/><text x="638" y="433" class="title">Ambiguous delivery / endpoint change</text><text x="638" y="454" class="copy">Reconcile the selected route and external message identity first.</text><text x="638" y="474" class="copy">Another discovered endpoint is not an automatic retry target.</text>
    <rect x="32" y="404" width="526" height="92" rx="10" class="optional"/><text x="52" y="433" class="title">Immutable route evidence</text><text x="52" y="454" class="copy">participant address • document/process • SMP source/freshness • endpoint/certificate</text><text x="52" y="474" class="copy">sending/receiving provider roles • adapter/config • correlation • selection reason</text>
    <rect x="204" y="526" width="692" height="28" rx="14" class="finish"/><text x="303" y="545" class="title">New metadata affects eligible new work; historical invoice exchange actions retain the route used</text>
  </svg>
  <div class="notes"><div class="note"><strong>Multiple addresses are valid input</strong>Purpose, country, document/process capability and validity determine which address is eligible.</div><div class="note"><strong>SMP may return multiple endpoints</strong>Each is a technical URL for a transport profile—not the participant identifier or provider name.</div><div class="note"><strong>Fallback is a mutation decision</strong>After a possible send, reconcile before selecting another endpoint to prevent duplicates.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Required distinctions

| Do not collapse | Why |
|---|---|
| Country identifier ↔ Peppol participant address | A participant address is scheme-qualified and used in transport discovery; a legal/tax identity may be associated but is not universally interchangeable |
| Business-document `EndpointID` ↔ transport Participant Identifier | Peppol policy notes that their relationship is not a reliable universal rule; the sending context must bind them explicitly |
| Participant Identifier ↔ SMP technical URL | One identifies the receiver in discovery; the other is a process/transport-specific service endpoint |
| Sending AP ↔ receiving AP | Four-corner exchange allows different providers |
| Network ↔ provider ↔ Sage adapter | Peppol is the network/rules; the provider operates an AP; Sage owns its provider boundary/configuration |

## Actual participant-scheme terms before reusable routing

The shared router must be derived from real scheme-qualified country addresses. The following are **active entries in OpenPeppol Participant Identifier Schemes v9.7 (2026-07-02)**; active list status means registrable in the network, not that a country mandates or approves that scheme for every invoice, direction, profile or participant.

| Country/context | Scheme ID and official term | Illustrative participant form | Country-specific interpretation required |
|---|---|---|---|
| France | `0002` — `FR:SIRENE` | `0002::<9-digit SIREN>` or an eligible 14-digit SIRET form under the v9.7 scheme rules | Decide whether the legal unit or establishment is the intended receiver; do not discard subject level |
| France | `0009` — `FR:SIRET` | `0009::<14-digit SIRET>` | Bind the exact establishment and supported document/process |
| France | `9957` — `FR:VAT` | `9957::<French VAT number>` | VAT identity reused as a network address remains a separate scheme-qualified binding |
| Spain | `9920` — `ES:VAT` | `9920::<Spanish VAT/NIF value permitted by scheme rules>` | Peppol availability does not establish the universal route under Spain's public/private statutory topology |
| Germany | `0246` — `DE:GEBA` | `0246::DE#########[-#####][.sub-address]` | German Electronic Business Address can include W-IdNr, distinguishing feature and self-published sub-address; country rollout/usage policy applies |
| Germany B2G | `0204` — `DE:LWID` / Peppol-Leitweg-ID | `0204::<Leitweg-ID>` | Public-sector routing identity; never infer for ordinary B2B |
| Germany / eligible context | `9930` — `DE:VAT` | `9930::<German VAT number>` | VAT participant scheme; exact B2B eligibility and capability must be discovered |
| International / eligible context | `0088` — `GLN` | `0088::<13-digit GLN>` | Not Germany-specific; use only where the participant is registered and country/profile policy permits it |
| Ireland | `9935` — `IE:VAT` | `9935::<Irish VAT number>` | Active Peppol scheme; future domestic B2B mandate binding remains country-owned |
| United Kingdom | `9932` — `GB:VAT` | `9932::<UK VAT number>` | Active Peppol scheme; the future UK mandate's participant/profile rules remain open |

The reusable routing contract begins only after those source terms are retained:

| Actual country/network term | Reusable field or behaviour |
|---|---|
| Scheme ID and value | `participantScheme`, raw/display value and normalized value; uniqueness includes the scheme |
| Legal unit, establishment, VAT registration or sub-address meaning | Explicit subject reference, purpose, direction and no value-only merge |
| Registrable/active/deprecated/removed state | Code-list version, verification time, effective interval and prospective blocking |
| Registered document type and process | Capability-specific lookup; an address is not globally reachable for every document |
| SML/DNS and authoritative SMP result | Discovery source, lookup time, returned endpoint set and freshness |
| Technical endpoint, transport and certificate | Deterministic selection plus immutable execution-route evidence |
| Country mandate/profile eligibility | Country-pack decision kept outside the generic Peppol resolver |

## Requirements and acceptance

| ID | Requirement / acceptance |
|---|---|
| PA-FR1 | Store participant addresses as scheme + value + legal-entity association + purpose/direction + country + effective interval + status/evidence. |
| PA-FR2 | Support 0..n participant addresses for one legal entity/context without value-only deduplication or an ungoverned “primary” flag. |
| PA-FR3 | Resolve capability using participant, document type, process, environment and effective time; retain authoritative discovery source and freshness. |
| PA-FR4 | Parse one or more SMP service endpoints and validate transport profile, certificate, activation/expiry and country/BIS eligibility before selection. |
| PA-FR5 | Produce a deterministic, explainable selected route that binds network, sending/receiving provider roles, Sage adapter/config, participant and technical endpoint. |
| PA-FR6 | Freeze the selected route with the invoice exchange action; metadata refresh changes only eligible new work. |
| PA-FR7 | Following a timeout after possible transmission, reconcile by external identity before switching endpoints or providers. |
| PA-FR8 | Load participant schemes from a versioned OpenPeppol code list and apply country/profile eligibility separately; deprecated or removed entries affect eligible new work without rewriting history. |
| PA-AC1 | Given two participant addresses where only one supports the required invoice document/process, then discovery selects that address and records why. |
| PA-AC2 | Given SMP returns two transport endpoints, then only an approved eligible endpoint is selected and both candidates/evidence remain explainable. |
| PA-AC3 | Given an endpoint/certificate changes after dispatch, then historical status/recovery uses the original route while a new invoice can use refreshed metadata. |
| PA-AC4 | Given the same character sequence appears under two participant schemes, then the two addresses remain distinct and discovery never merges them by value alone. |
| PA-AC5 | Given an active Peppol scheme exists for a country but the selected country pack has not approved it for the document/process, then route selection remains blocked or undetermined rather than treating list presence as mandate eligibility. |

## Evidence and open gates

| Evidence | Finding | Impact |
|---|---|---|
| [Peppol SMP 1.4](https://docs.peppol.eu/edelivery/smp/Peppol-EDN-Service-Metadata-Publishing-1.4.0-2025-02-06.pdf), 2025-02-06 | A process has a `ServiceEndpointList` with one or more endpoints; an endpoint is a technical URL with transport metadata | Confirms multi-endpoint model and process/document-specific discovery |
| [Peppol Policy for use of Identifiers 4.4](https://docs.peppol.eu/edelivery/policies/Peppol-EDN-Policy-for-use-of-identifiers-4.4.0-2025-02-06.pdf), 2025-02-06 | Business-document parties/`EndpointID` and transport Participant Identifiers can relate, but no reliable universal linking rule exists | Requires explicit association and preserved discovery context |
| [Peppol MLS specification](https://docs.peppol.eu/edelivery/specs/mls/v1.0.0/mls/spec/), accessed 2026-08-12 | Some Peppol cases explicitly support participants with multiple service providers and providers with multiple Access Points | Prevents single-provider/single-AP assumptions; exact applicability must follow the selected BIS/process |
| [OpenPeppol Participant Identifier Schemes v9.7](https://docs.peppol.eu/edelivery/codelists/v9.7/Peppol%20Code%20Lists%20-%20Participant%20identifier%20schemes%20v9.7.html), 2026-07-02 | Confirms active country and international scheme terms including `0002`, `0009`, `9957`, `9920`, `0246`, `0204`, `9930`, `0088`, `9935` and `9932` | Supplies actual scheme vocabulary and version/state; does not supply national mandate eligibility |

Open gates: approved participant-identifier schemes per country; whether one legal entity, establishment or product context owns each address; address priority/purpose UX; discovery cache/freshness policy; multiple-provider commercial model; transport selection; certificate rollover; and operational reconciliation rules.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-12 | Initial child discovery PRD; clarified “Access Point address” as Peppol participant and service-endpoint concerns | User clarification and official Peppol specifications |
| 2026-08-12 | Published as a child of commonality page `866150169` | User publication approval |
| 2026-08-12 | Attached selection and recovery connectors to node boundaries, removed through-node routing and made the diagram responsive | Confluence visual review |
| 2026-08-25 | Added the actual v9.7 participant-scheme catalogue for France, Spain, Germany, Ireland and the UK, then derived the reusable routing fields and tests | User request; OpenPeppol eDEC v9.7 |
