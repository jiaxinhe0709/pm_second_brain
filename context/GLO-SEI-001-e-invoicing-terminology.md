---
id: GLO-SEI-001
title: E-Invoicing Terminology
type: glossary
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-28
reviewers: []
related:
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-003
  - SPEC-SEI-004
  - SPEC-SEI-005
  - SPEC-SEI-006
  - SPEC-SEI-007
  - SPEC-SEI-008
  - SPEC-SEI-009
  - SPEC-SEI-010
  - SPEC-SEI-011
  - SPEC-SEI-012
  - SPEC-SEI-013
  - SPEC-SEI-014
  - SPEC-SEI-015
  - SPEC-SEI-016
  - SPEC-SEI-018
  - SPEC-SEI-019
  - SPEC-SEI-020
  - SPEC-SEI-021
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# E-Invoicing Terminology

This is the shared writing reference for the Spain solution specs listed below. Keep it in Git with the specs, under `context/`, so reviewers and future authors use the same definitions. Short definitions inside individual specs support readers who open only one document; they must agree with this glossary.

Definitions explain the current source documents. They do not approve an architecture, legal interpretation, external API, state model or production capability. Feature-specific behaviour, evidence and open decisions remain in the owning PRD and spec. Shared terms can be used across countries; Spain rules require a separate country binding.

## How to use and maintain the glossary

- Use the preferred term in explanatory prose. Expand unfamiliar acronyms on first use, or include them in the local terms table.
- Define **exchange action** on first use when a reader may open the document on its own. Use specific phrases such as **deliver the invoice**, **submit the public copy** or **report the payment** where possible. Use **action** after the meaning is clear.
- Write a clear actor and action before naming an internal control. Use complete
  sentences in behaviour and recovery explanations. Explain necessary terms such
  as scope, commit, lease and outbox; avoid compressed chains of nouns or slashes.
  A glossary link does not replace a readable explanation in the spec.
- Qualify words with several meanings: **represented party** versus **authenticated principal**, **technical acknowledgement** versus **buyer acceptance**, and **API endpoint** versus **business outcome**.
- Preserve exact technical fields, state values, event names, headers, URLs and permanent IDs. An editorial wording change is not permission to rename a contract field or translate a raw external code.
- Add a new shared term here before copying a definition into another spec. Keep a specialised definition in the owning spec and link to it. Review both when a meaning changes.
- Identify the country, source and version when a term carries legal or network meaning. A Spain term or code must not become another country's default.
- The glossary owner coordinates wording. Domain owners decide contract meaning and resolve the open mappings below. A substantive meaning change needs the repository's normal review; document status and publication require explicit approval.

## Evidence and references

| Preferred term | Definition and usage boundary |
|---|---|
| Source evidence baseline | The original files used to establish external requirements and contract facts for a stated scope/version. For the Spain public platform, use the original sources in [RES-SEI-002](RES-SEI-002-spain-public-platform-technical-evidence.md#ref-source-references). The final published regulation governs legal requirements; technical files establish only their stated facts. Missing or conflicting evidence remains an open gate. |
| REF source reference | A source ID with its original-file link, version/date, exact article/section/page or contract element, supported claims and limits. Product requirements and proposed Sage controls retain separate authority. An English summary or extraction is a reading aid, not a replacement source. |
| Confirmed in supplied evidence | A fact stated in a supplied source, within that source's status and limits. This does not mean that an implementation supports it or that a live service accepted it. Source, field-mapping and implementation coverage are separate checks. |

## Identity, access and authority

| Preferred term | Definition and usage boundary |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. The two terms describe the same business context in these specs; neither is a tenant ID or network address. |
| Tenant | The customer account boundary used to keep one customer's data and access separate from another's. A tenant may contain several legal entities. The Network dataset guide uses the exact field `tenantId` as the subsequent `datasetId`; that API usage does not establish product-tenant or legal-entity cardinality. See **FR API dataset / Network dataset** below. |
| Represented party | The business or person on whose behalf an action is performed; also called the **business principal** in delegation context. It is separate from the authenticated identity making the request. |
| Authenticated principal | The trusted identity of a person, application or service making a request. Authentication establishes that identity; a separate authority check establishes what it may do for a represented party. Avoid unqualified “principal” in prose. |
| Actor / delegate | An actor performs an action. A delegate is an actor authorised to act for a represented party within a stated scope and period. A delegate and its authenticated application may have different identities. |
| Authentication | Checking the identity of the caller or communicating service. A successful login or certificate check does not establish customer authority. |
| Authority / authority grant | Permission to perform a specific action for a represented party within a defined scope and period, supported by effective evidence. An API permission alone does not establish legal representation. |
| Direct customer | The represented business acting through its authorised owner, administrator or service. Use this term for the business pathway; **consumer** identifies an application using the API. |
| Client relationship | The current link between an accountant firm and a client workspace or business for approved product access. It is checked separately from the actor's firm role and delegated authority. |
| Approval evidence / approver | Approval evidence records an eligible actor's decision for a named business, purpose, scope and request or plan version. The approver is the actor permitted to make that decision. A recorded approval is separate from verified effective authority; terms acceptance, delegation, route change and signing remain distinct purposes. |
| Internal invoice approval | A business workflow decision that permits a specified next step for a named invoice revision. An authorised business actor or delegate may make the decision. It is separate from effective authority, issuance, technical receipt, buyer acceptance and statutory reporting. Product policy defines whether a manual decision or an authorised automatic rule is permitted. |
| Accounting handoff | An authorised transfer of invoice information or files to an accountant or accounting software. Its result is separate from supplier-to-buyer delivery, source capture, technical acknowledgement, buyer acceptance and bookkeeping completion. |
| Consent | Qualify the specific decision and evidence when this word appears in a source or user journey. Do not use a generic consent flag as service-terms acceptance, effective delegated authority, route-change approval or signing permission. Country policy defines the accepted mechanism for each purpose. |
| Entitlement | Commercial or product permission to use a feature. It is checked separately from identity, authority and technical readiness. |
| Portfolio / portfolio item | An accountant's set of client businesses; one client's separately scoped work item. Clients do not share authority, credentials or outcomes merely because they belong to one portfolio. |
| Batch / batch receipt | A batch groups separately scoped requests for processing. A batch receipt confirms durable acceptance of its request manifest. Batch coordination states do not establish item authority, readiness or activation. |
| Consumer | A product application or partner service using an API or service contract. Consumer readiness does not grant access to every customer or operation. |
| Provider / partner / operator | A provider supplies an invoice-network capability. A partner may instead be a delegate or product integrator. An operator operates a platform or network capability. Identify the actual role; these labels do not confer authority or execution rights. |
| Environment | The separately controlled context, such as test or production, in which an operation runs. Credentials, records, authority bindings and readiness must match it. |
| NIF / apoderamiento | Spain tax identifier; power of attorney. These are separate identity and representation concepts, governed by the selected Spain action and evidence. NIF does not encode a France-style establishment suffix. Separately identified permanent establishments and dataset mapping need the country rules and sources in [SPEC-SEI-020 section 4.4](../specs/archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md#44-spain-nif-establishments-and-dataset-mapping). |
| SIREN / SIRET | French legal-unit and establishment identifiers. SIRET contains the legal unit’s SIREN plus an establishment identifier. Several addresses/establishments can therefore refer to the same legal unit. These meanings do not establish Sage dataset cardinality. See INSEE sources in [SPEC-SEI-020 REF](../specs/archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md#ref-source-references). |

## Services, connections and routing

| Preferred term | Definition and usage boundary |
|---|---|
| SXS | The small experience service that manages the product's `datasetId` / `tenantId`, as clarified by the user on 26 October 2026. Its exact interface, business/client mapping and deployment support need owner confirmation. It does not establish one dataset per NIF or replace action permission. |
| Public platform | Preferred prose name for Spain's public e-invoicing platform in these specs. **Public solution**, **public electronic invoicing solution** and **SPFE** are source aliases in this context. This does not make other AEAT services interchangeable with it. |
| AEAT | The Spain tax authority identified in the source specs. AEAT names the authority; public platform names the e-invoicing service being used. Avoid using “AEAT API” without naming the qualified capability. |
| Private platform | An invoice platform other than the public platform, used under its qualified capability, contract and customer authority. Its readiness does not remove independent public-copy or reporting requirements. |
| E-Invoicing Global API / Global API | The proposed common API contract for products and authorised partners in SPEC-SEI-013. “Global API” is the short form. Existing implementation coverage remains unverified. |
| Sage Global e-Invoicing Platform | The broader set of shared invoicing capabilities described in the supplied Public Platform API Integration PRD. The Global API is its access contract; the public platform connector is one integration responsibility within it. The names do not establish deployment boundaries or production readiness. |
| API / contract profile | Application programming interface: the operations and data a service exposes to callers. A contract profile fixes the selected operation, protocol/schema, environment and safety rules; it is separate from an invoice or trust profile. |
| Provider API | The Sage-owned provider-facing capabilities proposed within the Global API. Use **provider-owned API** for an external provider's own interface. The terms describe different contract owners. |
| Domain Services / E-Invoice Service | Domain Services is the broader group of business services, including an E-Invoice Service, Tax Service and other domain services. The E-Invoice Service coordinates invoice journeys and uses the capabilities assigned to other services. In these specs, the older singular label **Domain Service** describes the logical owner of the feature being discussed. Actual capability ownership, service contracts and deployment coverage remain design and qualification questions. |
| Diagram responsibility groups | Use the same main lane names: **Customer / accountant**, **ERP / product**, **Domain Service - E-Invoice Service**, **Domain Service - Other Services**, **Operations / support**, and **Public / private platforms**. The E-Invoice Service coordinates invoice journeys. Other Services covers supporting responsibilities such as identity, certificates, connections, transformation and records, subject to the owning spec's service-ownership gates. Operations covers people performing support, release or recovery work; automatic processing and record storage remain with their logical service owners. A diagram may omit groups with no activity. A short subtitle may distinguish roles within one group, such as DTS API and DTS mapper. These labels group logical responsibilities; they do not approve deployed service boundaries. |
| DTS | Document Transformation Service, the existing Sage transformation reuse candidate. Each selected input/output pair, mapping, rule pack, build and operational path needs qualification. DTS does not by itself provide legal issuance, signing, invoice transport or permanent archiving. |
| Tax Service / Tax Vault / Connections Service / AFL | Service names retained from certificate source evidence. AFL refers to the Spain anti-fraud implementation in that evidence. Do not treat the proposed Tax Vault and the described Connections Service/AFL credential path as one proven implementation; actual ownership and B2B fitness remain SPEC-SEI-001 qualification questions. |
| Public platform connector | The logical protocol-access and operation-evidence responsibility in SPEC-SEI-011. It executes a qualified public operation; the feature service owns its business interpretation. |
| Recipient lookup | Finding and qualifying evidence of a recipient's receiving destination. It is separate from discovering invoices already received, validating tax identity or changing a customer's route. No central AEAT recipient-directory API is proven by this name. |
| Capability | A supported function, such as receiving invoices or signing them. Each operation used to provide it needs qualification for the selected scope. |
| Integration role | The capacity in which Sage uses an interface: customer-provider integration or platform interconnection. The role selects qualified contracts and controls; it does not grant customer authority. A capability qualified for one role is not automatically ready for the other. |
| Private-platform interconnection | Exchange between participating private platform operators. It is separate from connecting a customer's ERP to its provider or changing that customer's provider. The Spain operator request period is one month, subject to the specific queue exception in RD 238/2026 Article 9; [SPEC-SEI-038 operator handoff](../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#67-onb-05-configure-private-choice), traced to PRD-SEI-221 FR20, defines the onboarding handoff and source limits. ONB-R25 means the requested/confirmed effective boundary, not operator interconnection. |
| Connection | Configuration for communicating with a platform or provider. A configured connection is separate from external registration, readiness and route activation. |
| Existing E-Invoice API | The shared Sage API whose supplied onboarding contracts cover datasets, access points and connections. It was first used for France. Its name does not limit it to France or prove that Spain support is already implemented. `FR-01–05` are retained evidence IDs, not the API name. |
| E-Invoice API dataset / Network dataset (previously FR API dataset) | A resource identified by `datasetId` in the [existing onboarding contracts](<FR API/Onboarding/get-dataset-accesspoints.md>). Connections can contain multiple addresses. Guides recommend one dataset/official registration per legal entity wherever possible; the integrating product owns intended mapping, subject to supported constraints. Enforced entity cardinality remains unverified. The [dataset guide](<FR API/Onboarding/network-onboarding-create-dataset-guide-extract.md#review-clarification-dataset-entity-and-address-scope>) uses returned `tenantId` as `datasetId`; its differing `data.id` needs clarification. Multiple addresses sharing one SIREN do not prove multiple legal entities. Distinct-SIREN/NIF, accountant, product/Tax and channel mappings remain SPEC-SEI-021 GAP-01. |
| Network partner account | The account that owns API-created datasets in the supplied dataset guide. It can manage many legal-entity datasets with one M2M credential set; a different partner account receives `403 Forbidden`. This technical boundary does not establish an accountant firm's client relationships or authority. Native Sage channels are not automatically linked. See the [guide's ownership and channel statements](<FR API/Onboarding/network-onboarding-create-dataset-guide-extract.md#ownership-and-access>). |
| E-Invoice API access point and connection (previously FR API) | `accessPointId` identifies the service route; `connectionId` identifies the dataset’s connection. The [supplied guide](<FR API/Onboarding/access-point-guides-evidence-extract.md#int-ap01-connect-and-channel-selection>) describes one connection per dataset/access point and several address entries within it. Dataset-level and address-level CONNECTED have different scopes; neither alone proves business authority or route activation. Preserve exact source results and qualify Spain mappings in SPEC-SEI-021. |
| Connection reference — qualify by source | E-Invoice API `connectionId` identifies an `AccessPointConnection`; Tax certificate upload returns `data.id` for a `Connection` selected through ES AFL `Connection-Id`. Their different documented purposes do not prove separate ID namespaces. Whether IDs are shared, mapped or independent remains [SPEC039 GAP-06](../specs/onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#4-open-engineering-decisions). Retain source context and do not substitute IDs before contract confirmation. |
| Address ownership (Network guide) | A technical assignment of an e-invoicing address to a product dataset or active provider route. The [ownership guide](<FR API/Onboarding/access-point-guides-evidence-extract.md#int-ap04-address-ownership-transfer>) describes takeover through connect, subject to provider/version and conflict qualification. This is separate from legal ownership of the business and authority to act for it. The integrating product owns intended address/dataset/client mapping within supported platform and country constraints. |
| Onboarding | The setup workflow owned by the E-Invoice Service. It establishes or confirms selected functions through Sage. It can connect an existing service, add a function or coordinate an authorised platform change. It does not imply a separate onboarding service, first-time external registration or active invoice exchange. |
| Onboarding component | A proposed internal component of the E-Invoice Service that could implement setup and recovery coordination. Its need and implementation remain open. The term does not establish a separate API or deployment. |
| Common / scenario-specific / conditional behaviour | Diagram and specification labels. Common names shared behaviour; scenario-specific names work selected for the customer's situation and requested outcome; conditional names work performed only when required and permitted. Common checks can return no further work. These labels do not prove implementation reuse or replace country/provider rules. |
| Registration | External enrolment or recorded configuration under the selected provider contract. A local connection record does not prove registration or receiving reachability. |
| Readiness | The current result of capability checks for a stated legal entity, actor, environment and route/profile, with evidence, limitations and a recheck condition. Readiness is separate from authority, route activation and invoice outcomes. |
| Route | The time-bound selection of platform and connection for a defined invoice scope and direction. A ready connection does not activate a route or rewrite earlier invoice plans. |
| Entry point | The published receiving destination for a legal entity. It need not be a raw URL. Publication does not by itself prove operational eligibility for a particular invoice. |
| FR sending routing address | The `sender` or `recipient` address in the supplied FR sending API guide, using `accessPointAddressType` and `accessPointAddress`. These identify network routing roles, separately from seller and buyer in the invoice. The sender belongs to the calling dataset; self-billing routes buyer to seller. This guide does not establish Spain address types or document-code mappings. See [sending evidence](<FR API/Sending/send-e-invoice-guide-extract.md>). |
| Direction | Business direction relative to the represented legal entity: outbound when it is the issuer, inbound when it is the recipient. API call direction, push/pull and network origin are separate concepts. |
| Cutover / rollback | Cutover changes future work to a qualified route or capability at an agreed boundary. Rollback is a controlled change back; after an external effect it needs its own checks and evidence. Earlier work keeps its actual history. |
| Rotation | Preparing replacement trust material and switching future eligible operations to it. Cutover is the switch boundary, rather than the whole replacement lifecycle. |
| Historical continuity | Keeping the permitted access, evidence, responsible actors and channels needed to complete work on earlier invoices after a route change or service exit. It does not give a former provider indefinite authority. |

## Invoices, representations and rules

| Preferred term | Definition and usage boundary |
|---|---|
| ERP | Enterprise resource planning or business software that owns invoice data and issuance. Domain services may prepare a representation but do not silently issue or change the legal invoice. |
| Issued invoice | The invoice whose business identity and final revision have been recorded by the issuing product under its controls. A successful draft check does not establish issuance. |
| Business invoice creation / representation generation | The ERP prepares and issues the business invoice. Representation generation creates an electronic file from an identified source revision. A generated file or validation pass does not establish issuance. SPEC-SEI-015 owns the Spain creation handoff. |
| Seller / buyer / material issuer | Seller supplies the goods or services; buyer receives the supply; material issuer prepares and issues the document in practice. Buyer-issued invoices preserve seller and buyer in their normal invoice fields. Material issuer, legally obligated supplier and authenticated caller are separate roles; country rules qualify their authority and identifier binding. |
| Corrective invoice / correction method | A separate invoice that rectifies earlier invoice facts. In the selected Spain public profile, method `I` means correction by difference and `S` means correction by substitution. New document amounts and referenced original amounts have different meanings. Exact field bindings and permitted procedures belong to SPEC-SEI-015 and its qualified country pack. |
| Replacement of simplified invoices | Spain type `388` in the final public-platform order's L1 list. This scenario is separate from corrective substitution method `S`; do not use “replacement” alone when both meanings are possible. |
| Unique invoice code | Spain composite invoice identity using the qualified issuer NIF, series/number and issue date. Encoding and issuer-role mapping require the selected country contract. It is separate from a Sage invoice ID, request-idempotency key, operation ID and DTS task ID. Knowledge of a code does not grant access. |
| REGI | Fixed property code identifying a Spain invoice-line regime entry. The entry's value contains the regime code; REGI is not itself the regime value. Cardinality, national tax qualifier and permitted codes belong to the selected Spain profile. |
| Representation | A specific file or data form of an invoice. Preserve its role, source, version and integrity evidence. Different representations may carry the same business meaning without having identical bytes. |
| Transitional PDF companion | A readable PDF accompanying the structured invoice under the selected country transition rule. In this Spain sending scope, the local product generates it and qualifies delivery to the recipient. It is distinct from a faithful public copy, a Factur-X hybrid and the structured invoice. See [the product rule](../prds/PRD-SEI-246-spain-invoice-preparation-and-outbound-flow.md#transitional-pdf-product-rule). |
| Recovered source file / original | The exact bytes obtained from a source, kept with their source and role. “Original” must identify which source it refers to. A retrieved public copy is not relabelled as the private-route original. |
| Retrieval / file acquisition | Obtaining the actual invoice file from its source. Discovery, a query result or a notification records availability but does not by itself establish durable source-file capture. A qualified source can deliver the complete file or require a separate fetch. |
| Source-file download / stored-file download | A source-file download transfers a file from an external source. A stored-file download returns already captured bytes to an authorised actor. Qualify which operation is meant. Neither operation alone proves product receipt, buyer acceptance or completed conservation. |
| Notification-only intake | A saved source event, metadata or file reference that requires later file acquisition. It cannot stand in for the actual invoice bytes, a verified capture receipt or business delivery. Acknowledgement meaning follows the qualified source contract. |
| Faithful public copy / public copy | The separately classified public-platform copy of an invoice exchanged through another route, where the applicable Spain policy requires it. “Faithful copy” is a source short form. Exact syntax and acceptance still require the selected contract/profile evidence. Preserve role `PUBLIC_COPY`. |
| Canonical representation | The shared internal data form used by Sage products. It is derived from a source invoice and does not replace its original bytes or become the legal system of record by its name alone. |
| Canonical event | A Sage interpretation of a source fact under a versioned mapping. It is separate from the exact raw source event and from a derived customer status. |
| Exchange action | One separately tracked action to deliver an invoice, submit a public copy, or report an invoice event. Each action has its own result. For example, invoice delivery can succeed while public-copy submission still needs attention. |
| UBL / XML / CII | Universal Business Language; Extensible Markup Language, the file syntax used for UBL; Cross Industry Invoice, another structured invoice format. A standard's existence does not establish acceptance by a Spain route. |
| Profile | The selected constraints for a syntax, country, route and document type. Qualify **invoice profile**, **trust profile** or **contract profile** where needed; these are not interchangeable. |
| Rule pack | Versioned executable rules and resources used to apply or check a selected profile or policy. It is not the entire country pack or the deployed service build. |
| Country pack / country binding | A country pack contains versioned local identity, routing, format, trust or reporting rules. A country binding selects those rules and the required adapters for a shared capability. Spain rules do not become shared defaults. |
| Capability bundle | The proposed fixed set of input, document type, mapper, syntax/profile/rules and output versions for one transformation scope in SPEC-SEI-008. It includes more than a rule pack. |
| Mapper / transformation | Mapping code applies defined conversion rules. A transformation is an operation converting source data to a target representation. Support in one direction does not qualify the reverse direction. |
| Semantic preservation / parity | Semantic preservation keeps required business meaning during conversion. Parity checks whether the required old and new behaviour matches. Neither necessarily requires byte-identical output. |
| Preflight / final validation | A preflight is an advisory draft or preview check. Final validation checks the exact final representation and current rules before dispatch. A draft pass cannot authorise changed final bytes. |
| XSD / EN 16931 / BIS / CIUS | XML Schema Definition checks XML structure; EN 16931 defines a European invoice model; Business Interoperability Specifications and Core Invoice Usage Specifications add more specific rules. Keep the exact selected versions and country/route acceptance gates. |

## Evidence, outcomes and recovery

| Preferred term | Definition and usage boundary |
|---|---|
| Business outcome / API endpoint | A business outcome is an observable result or handoff in a feature journey. An API endpoint is an addressable service operation. Use “outcome” for summary result tables. |
| Operation acceptance / durable receipt | Confirmation that a service has saved an operation through its agreed recoverable acceptance boundary. It does not prove external execution, delivery, buyer acceptance or payment. |
| Technical acknowledgement | A response with the meaning defined by the selected source contract and milestone. Identify what it acknowledges: API intake, transport, platform receipt, product receipt or event delivery. It does not establish buyer acceptance. |
| Recipient delivery / product receipt | Recipient delivery records evidence at the external destination's stated level. Product receipt records the Sage product's intake of a delivery. Neither is automatically buyer acceptance or completed accounting. |
| Buyer acceptance / commercial decision | An authorised buyer decision concerning the invoice. Preserve source, actor, meaning and country rule. A presumed acceptance view is labelled as derived and is not an invented explicit buyer event. |
| Payment information / reporting outcome | Payment information records an evidenced payment fact. Reporting outcome records the separate transmission/result of a required report. A saved payment fact does not prove that its report reached the required destination. |
| Raw event / derived status | A raw event preserves the source code, meaning, actor, times and integrity evidence. Derived status is a rebuildable interpretation under a versioned rule. Preserve separate processing, validation, delivery, commercial, payment and reporting dimensions. |
| Lifecycle transition attempt / latest successful status | A transition attempt requests a status change. In the [supplied lifecycle outcome note](<FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md#int-lcs05-transition-outcome-note>), a failed attempt remains in history with `operationStatus = ERROR`; the invoice keeps its latest successful status. Attempt processing, business facts and each destination's reporting outcome remain separate. A transport timeout can still leave an external effect unknown. |
| Operational COMPLETED / lifecycle Completed | Operational `COMPLETED` means the status-transition attempt succeeded in the supplied lifecycle note. French lifecycle Completed is numeric `209`, UUID `00000000-0000-0000-0000-140000000000`, for information supplied after suspension. Neither term alone establishes payment or completion of all required reports. |
| Source observation | A record of an invoice or event arriving or being retrieved from a particular source. Several observations may relate to one business invoice without being the same source file. |
| Idempotency | Repeating the same logical request adds no effect within the contract's defined scope and retention window. The contract binds request identity and input and defines conflict handling. It does not promise exactly-once transport. |
| Duplicate detection | Recognising repeated observations, events or invoice candidates under defined identity/equivalence rules. It is separate from request idempotency; changed content under the same identity requires conflict handling. |
| Reconciliation | Check the original operation against an authoritative source to establish what happened before deciding the next action. Preserve original identity, input and context. |
| Outcome unknown | An external effect may have happened but reliable evidence is missing. It is a recovery condition, separate from confirmed failure or success; it does not permit a fresh mutation or automatic fallback. |
| External mutation | An operation that changes another system. Retry safety depends on the qualified operation contract and transmission evidence, rather than the error name alone. |
| Durable intent / outbox | A durable intent saves request identity and input before a possible external effect. An outbox saves an event or delivery intent waiting to be sent. Sending a notification does not prove business processing. |
| Durable | Saved through the agreed recovery boundary so the record survives a process restart or worker failure. Long-term retention and disaster-recovery targets are separate policies. |
| Immutable / append-only | Immutable means a saved record cannot be changed. Append-only means later information is added as another record. Neither means indefinite retention or exemption from approved deletion policy. |
| Provenance / evidence package | Provenance records where data came from and the versions, checks and changes producing a result. An evidence package groups references needed to verify a specific operation. |
| Digest / hash / correlation | A digest or hash is a calculated content fingerprint. Correlation is a reference linking requests and results. A correlation ID is not proof of authority or content equality. |
| Snapshot / pinned version | A snapshot preserves the evidence and policy used for a decision. A pinned version is fixed for one operation. Later upgrades do not silently change historical bindings. |
| Checkpoint / watermark | A checkpoint saves retrieval progress after the required durable classification. A watermark indicates a covered source position or time under the collection contract. It is not automatically the latest timestamp observed or a processing-success claim. |
| Freshness / coverage | Freshness says whether evidence is current enough for a use. Coverage says what a source answer includes. An empty response, stale result or source outage is not proof of global absence. |
| Negative caching | Temporarily reusing an absence observation for the same scope under approved freshness and coverage rules. It does not turn incomplete source coverage into proven absence. |
| Lease / execution claim | A time-limited, scoped right for one worker to perform work. Replacement workers must prevent stale commits; having a work reference alone is not execution authority. |
| Retry budget / backoff / jitter / circuit breaker | A retry budget limits attempts and elapsed time; backoff waits between attempts; jitter varies that wait. A circuit breaker temporarily stops calls after defined failures. These controls do not establish retry safety or change invoice routing. |
| Processing attempt / FR processing outcome | One handling attempt for an invoice or status change in the [supplied FR error guide](<FR API/Shared/invoice-flow-error-handling-guide-extract.md>). Its history item uses `operationStatus` and nullable `errorCode`; `currentStatus` has neither. `ERROR` is final for that attempt. A later platform retry needs qualified correlation and its own evidenced result. Processing completion does not prove invoice delivery, buyer acceptance or completion of every obligation. This meaning is source-specific, not an AEAT state model. |
| Quarantine | Restricted storage and a held processing state until an authorised owner resolves a trust, content, identity or routing problem. Conservation access requires its separately approved safe-access policy. |
| Conservation / retention / legal hold | Conservation keeps invoices available for the required records period. Retention is the policy for keeping a data class. A legal hold prevents deletion where required. DTS staging expiry is separate from invoice conservation. |
| Gate / qualification | A gate is a condition, decision or evidence check required before proceeding. Qualification establishes that a selected capability meets its stated scope. Both require an owner and evidence; a candidate name is not a passed gate. |
| Contract | The agreed inputs, outputs, behaviour and responsibilities between services or parties. A logical proposed contract is separate from an approved deployed interface. |
| Scope / commit / conformance | Scope states which customer, legal entity, environment, capability, action and objects an operation covers. A commit finishes saving the related records through an agreed recovery boundary. Conformance is evidence that a consumer or service follows the selected contract. Explain the relevant scope and saved result in prose rather than using these words as unexplained shorthand. |

## Trust and operational abbreviations

| Term | Meaning and limit |
|---|---|
| Certificate / signature / seal | A certificate binds an identity to public-key information. A signature or seal is a cryptographic result for specific bytes. Possession of a certificate or a raw signature does not by itself establish a qualified electronic signature or authority to act. |
| Trust material / material version | A certificate, chain, protected key reference or external validation identity; one saved version of that material. Renewal creates a new version and preserves required earlier evidence. |
| Custody / protected operation | Custody is the approved holding and use of protected material. A protected operation uses a key inside that boundary. **Custody** can refer to retained invoice files in records context; name the object and owner. |
| QTSP / QES | Qualified trust service provider; qualified electronic signature. Preserve the selected qualified service and legal/evidence gates rather than assuming every certificate operation qualifies. |
| PKI / HSM / CA / mTLS | Public key infrastructure; hardware security module; certificate authority; mutual transport authentication using certificates at both ends. These are distinct trust, custody, issuer and communication concepts. |
| AP / MLR / MLS | Access point; Message Level Response; Message Level Status, as used in the Peppol lifecycle sources. Actual message availability and meaning require the selected process/provider contract. |
| Task / transformation ID | In DTS, the task is a separate progress reference pointing to a transformation. Preserve the documented task identifier, `TransformationId` and ownership; do not substitute an invoice or event ID. |
| SQS / DLQ / redrive | Amazon Simple Queue Service; dead-letter queue for messages that could not be processed; controlled replay of those messages. Redrive keeps original identity and safe execution rules. |
| NAS / JWT / IAM | The authorisation service named NAS in the DTS sources; JSON Web Token; identity and access management. The NAS name does not establish its complete protocol. |
| CDK / MIME type | Cloud Development Kit for deployment; a label identifying a file format. Neither proves the content or capability is valid. |
| B2B / B2G / B2C | Business to business; business to government; business to consumer. Different transaction scope and service/network rules apply. International trade between businesses is still B2B, but the label alone does not establish inclusion in a domestic mandate. B2G or tax-submission capability is not automatically qualified B2B invoice exchange. |
| SLA / RTO / RPO | Service-level agreement; target time to restore service; maximum acceptable loss of recent data. Exact targets require approval and measurement. |
| RACI / LFS | Responsible, accountable, consulted and informed; Logical Feature Specification, Part 2 of these specs. |

## Reuse vocabulary

Use these four classifications consistently. Scope exclusions may say **Out of scope**; that is not a reuse-readiness claim.

| Classification | Meaning |
|---|---|
| Reusable unchanged | The proposed design pattern can stay the same. This does not claim that an existing implementation is unchanged or production-ready. |
| Reusable with country binding | Shared behaviour needs approved country/network/provider rules or adapters. Identify the binding and owner. |
| Country-specific | The behaviour belongs to the named country's rules. In this set, the country is Spain; it must not become another country's default. |
| Unknown | Implementation fitness or coverage needs evidence. Name the existing implementation reuse candidate, local changes, gaps, owner and required evidence separately. |

An **existing implementation reuse candidate** is an identified service or build being assessed. A **proposed design pattern** is an approach that may be implemented or reused. They are different claims. DTS remains the preferred transformation candidate where relevant, subject to its selected scope being qualified.

## Review coverage and remaining contract questions

The terminology review covers SPEC-SEI-001 through SPEC-SEI-016, including archived predecessors. Use [SPEC-SEI-016](../specs/archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) for current receiving, retrieval and download design. SPEC-SEI-006 and SPEC-SEI-010 remain linked below as historical review sources. Current onboarding and recovery design is in [SPEC-SEI-002](../specs/archive/SPEC-SEI-002-onboarding-solution-specification.md); the SPEC-SEI-004 row is also an archived review source. The review checks repeated definitions, service names, roles, outcome wording, reuse labels and terms used in behaviour, contracts and acceptance coverage. It is not an implementation test or a new regulatory validation.

| Source spec | Terminology focus |
|---|---|
| [SPEC-SEI-001 — Certificate management](../specs/SPEC-SEI-001-certificate-management-solution-specification.md) | Represented party versus authenticated principal; trust readiness, custody, rotation and source aliases. |
| [SPEC-SEI-002 — Onboarding](../specs/archive/SPEC-SEI-002-onboarding-solution-specification.md) | Readiness versus registration and activation; connection, entry point and cutover. |
| [SPEC-SEI-003 — Offboarding](../specs/archive/SPEC-SEI-003-offboarding-solution-specification.md) | Cutover, historical continuity and data disposition. |
| [SPEC-SEI-004 — Onboarding recovery](../specs/archive/SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md) | Unknown outcome, retry safety and reconciliation. |
| [SPEC-SEI-005 — UBL validation](../specs/SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) | Profile versus rule pack; preflight versus final validation. |
| [SPEC-SEI-006 — Inbound receiving](../specs/archive/SPEC-SEI-006-invoice-receiving-solution.md) | Source observation, canonical representation, product receipt and technical acknowledgement. |
| [SPEC-SEI-007 — Preparation and outbound](../specs/archive/SPEC-SEI-007-invoice-sending-solution.md) | Issuance, exchange actions, faithful public copy and final route evidence. |
| [SPEC-SEI-008 — Mapper migration to DTS](../specs/SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) | DTS, mapper, transformation, task, capability bundle and migration cutover. |
| [SPEC-SEI-009 — Invoice lifecycle](../specs/archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) | Raw event, canonical event, derived status and independent outcome dimensions. |
| [SPEC-SEI-010 — Retrieval, storage and download](../specs/archive/SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md) | Source original versus public copy; checkpoint, conservation and reuse classification. |
| [SPEC-SEI-011 — Public connector](../specs/SPEC-SEI-011-public-platform-connector-solution-specification.md) | Qualified operation, connection, contract profile and public transport responsibility. |
| [SPEC-SEI-012 — Recipient lookup](../specs/SPEC-SEI-012-consult-public-platform-for-recipient-information.md) | Recipient destination versus received-invoice discovery; coverage, freshness and unresolved absence. |
| [SPEC-SEI-013 — Provider capabilities through Global API](../specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md) | Authenticated principal, Provider API ownership, durable receipt and action execution. |

| [SPEC-SEI-014 — Shared connectivity and routing](../specs/SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) | Integration role, contract qualification, setup result, scoped platform change and historical continuity. |
| [SPEC-SEI-015 — Invoice creation](../specs/SPEC-SEI-015-invoice-creation-solution-specification.md) | Business creation versus representation generation; material issuer; corrective method versus simplified-invoice replacement; qualified unique invoice code and regime entries. |
| [SPEC-SEI-016 — Receiving, retrieval and download](../specs/archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) | One receiving feature; file acquisition versus notification-only intake; source-file download versus authorised stored-file download; qualified provider and country reuse. |

| Remaining question | Owner and boundary |
|---|---|
| How do existing `principal` fields map to represented-party and authenticated-caller identities? | Identity/Trust/API owners must confirm each actual schema and mapping. This review distinguishes prose meanings without renaming contract fields; SPEC-SEI-001 G1/G9/G11 and SPEC-SEI-013 GPA-Q02/Q03 retain the relevant decisions. |
| Which real components correspond to Domain Service, Tax Vault, Connections Service/AFL and other logical owners? | Architecture and domain owners must establish actual service/build boundaries. Names in the glossary do not merge them or close SPEC-SEI-001 G1/G9 and SPEC-SEI-013 GPA-Q01/Q02. |
| What does each external acceptance, acknowledgement or raw status actually prove? | Provider/public-platform and lifecycle owners must qualify each contract, namespace and country mapping. Keep raw codes and existing evidence gates; do not standardise external values through an editorial replacement. |
