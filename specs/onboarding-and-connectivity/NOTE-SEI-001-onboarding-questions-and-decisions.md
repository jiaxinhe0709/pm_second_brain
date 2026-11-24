---
id: NOTE-SEI-001
title: Onboarding questions and decisions
type: note
status: draft
owner: Jiaxin He
created: 2026-11-18
updated: 2026-11-23
related:
  - SPEC-SEI-001
  - SPEC-SEI-037
  - SPEC-SEI-038
  - SPEC-SEI-039
  - SPEC-SEI-040
confluence:
  publish: false
  page_id: ""
---

# Onboarding questions and decisions

These are the setup questions discussed on 18–19 November 2026. All 11 need confirmation. The first note records a meeting understanding; the meeting date and participants were not supplied. Recording a question does not approve a product rule or decide which service must provide it.

ERP means the customer's business software. NIF is the Spanish tax identifier. SPFE is Spain's public e-invoicing platform. The table is the source for these questions. [SPEC-SEI-039 GAP-01–08](SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#2-open-engineering-decisions) lists the technical checks still needed. The [shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md) explains other terms. This log keeps the original note's ID, NOTE-SEI-001.

## Questions and decisions

The entries add detail to [Q31 business mapping](../../work/spain-solution-review-questions.html#q31), [Q06 certificates](../../work/spain-solution-review-questions.html#q06) and [Q08 setup checks](../../work/spain-solution-review-questions.html#q08). Those questions keep their IDs and answers. [Q29 accountant batches](../../work/spain-solution-review-questions.html#q29) and [Q32 pre-registration](../../work/spain-solution-review-questions.html#q32) remain open in the workshop list.

<!-- onboarding-log-table:start -->
| ID and area | Current understanding | Question or decision needed | State | Decision or evidence | Suggested owner and next action | Affected specs or diagrams |
|---|---|---|---|---|---|---|
| <a id="q31-1"></a>Q31.1 — Company and dataset | The ERP identifies the selected company, its dataset and its NIF. | Does one dataset represent one company and NIF, several business locations, or something else? The ERP team must explain this relationship. The API teams must check that their systems support it. | Open | Discussed on 18 November. The relationship is not agreed. [R1](#r1) | ERP and Product teams: provide examples. Ask Identity and E-Invoice teams to check them. | SPEC038 business identity; SPEC039 GAP-01/02; shared-prerequisites diagram. |
| <a id="q06-1"></a>Q06.1 — Show the customer a list of certificates | Proposal: use certificate management and Connections Service to store and use certificates. The ERP shows the customer a list of certificates they are allowed to use. | Can the existing service return that list and explain what each certificate can be used for? Which checks can it provide so the Domain Service does not repeat them? | Open | The documented provider list is not a list of saved certificates. Support for this business-to-business use still needs checking. [R2](#r2) [R3](#r3) | Certificate and Connections teams: confirm the available API, returned information and supported uses. | SPEC001; SPEC039 GAP-06; SPEC040 §2; shared-prerequisites sequence. |
| <a id="q31-2"></a>Q31.2 — How datasets, NIFs and certificates relate | The business we act for and the certificate we use are separate things. | Can one dataset or NIF use several certificates? Can one certificate be used for several NIFs? We must not assume each dataset has exactly one NIF and one certificate. | Open | These relationships are not agreed. Having a certificate does not prove permission to act for a business. [R1](#r1) | ERP, Identity and Certificate teams: show the allowed relationships and how access to each business stays separate. | SPEC038 prerequisites; SPEC039 GAP-01/02/03/06. |
| <a id="q06-2"></a>Q06.2 — Use a different certificate after setup | Meeting understanding: a customer who sets up with certificate A should later be able to use another certificate, if it is accepted and authorised for the action. | Does the customer replace the saved certificate, keep several certificates, choose one each time, or use a combination? Which changes require the setup checks to run again? | Open | Recorded on 18 November. The meeting point still needs confirmation. | Product and ERP teams: agree the choices with Certificate and E-Invoice teams. Confirm which checks must run again. | SPEC038 ONB-03/10; SPEC039 GAP-06; setup/change sequences. |
| <a id="q06-3"></a>Q06.3 — Save or pass the certificate choice | Proposal: the ERP records the customer choice and passes a certificate reference through the agreed API. It does not pass the private key. | Does the choice change saved settings or apply to one action only? Can an existing API support it? The method and request fields are not agreed; do not assume POST. | Open | The Spain Anti-Fraud Legislation (ES AFL) service documents selection using `Connection-Id`. That does not confirm the same API works for B2B e-invoicing. [R2](#r2) [R3](#r3) | API, Architecture and Connections teams: check the existing API before proposing a change. | SPEC040 §2; SPEC039 GAP-06/07; supported-change sequence. |
| <a id="q06-4"></a>Q06.4 — Choose a certificate when sending | Proposal: the customer chooses a certificate that is accepted and authorised to send for the selected business NIF. | Who checks access to the dataset and NIF, permission to act, and certificate validity when sending starts? Does the customer use a saved default, choose each time, or have both options? | Open | The customer choice does not prove permission. The teams still need to agree who performs each check. [R1](#r1) [R2](#r2) | Product, ERP, Identity, Certificate and Sending teams: agree certificate selection and the checks at sending time. | SPEC038 prerequisites; SPEC001; sending SPEC023/024; sending sequence. |
| <a id="q06-5"></a>Q06.5 — Choose a certificate for automatic retrieval | If invoices are retrieved in the background, the system may need a saved certificate choice. | Can sending and retrieval use different certificates? What should happen if the saved retrieval certificate expires or can no longer be used for that business? | Open | No certificate-choice or recovery rule is agreed for retrieval. | Receiving, Product and Certificate teams: agree the saved choice, checks and recovery steps. | SPEC038 requested functions; receiving SPEC026/027; retrieval sequence. |
| <a id="q06-6"></a>Q06.6 — Choose the public-platform URL | The reviewed SPFE API files give different URLs for an electronic certificate and an electronic seal, a type of certificate used by an organisation. The URL also depends on the environment, such as test or production. | Which service chooses the URL? Changing to another certificate of the same type does not by itself mean the URL must change. | Open | The test-environment SendInvoice file defines separate certificate and seal URLs. This does not prove the software supports them or the caller has permission. [R4](#r4) | Public Integration and Certificate teams: check how certificate type and environment select the URL in the actual software. | SPEC001 CM-SPFE-R01; SPEC011 transport; public integration sequence. |
| <a id="q06-7"></a>Q06.7 — Return the certificate connection ID | The system needs to return and retain a reference that selects the certificate without exposing it. | Is that reference the certificate `Connection-Id`? How does it relate to the dataset and NIF? Is it the same as the E-Invoice platform `connectionId`, linked to it, or separate? | Open | ES AFL documents a certificate connection ID. It does not confirm that this is the E-Invoice platform connection ID. [R2](#r2) [R3](#r3) | Connections and E-Invoice API teams: provide one example from the same environment showing both IDs. | SPEC039 GAP-02/06; SPEC040 §2.3; prerequisite/setup sequences. |
| <a id="q08-1"></a>Q08.1 — Set up an account with a private platform | Each provider may use a website, an API, a manual process or a combination. Having a provider account does not mean Sage is connected to it. | For each provider, what must the customer do, what access details are needed, and how do we know setup is complete? What happens if setup stops or fails? | Open | ONB-05 already separates the provider account from the Sage connection. Each provider process still needs checking. [R1](#r1) | Provider Integration and Product teams: confirm each provider process with Architecture and Engineering. | SPEC038 ONB-05; SPEC039 GAP-02/06/08; private-setup diagram. |
| <a id="q08-2"></a>Q08.2 — Extra setup fields for a private platform | A private platform may need extra or different setup fields compared with SPFE. Check each provider separately. | Which fields are required? Which saved values can we reuse, and which must the customer enter? Flag this in the diagram. Confirm the fields against the provider API or setup instructions. | Open | Suggested on 19 November for Architecture and Engineering review. No specific fields or diagram changes are approved here. PROPOSAL: See [SPEC-SEI-046 — Private platforms integrating as connectors](../provider-connectors/SPEC-SEI-046-provider-connector-api-sequences-and-reuse-assessment.md#private-platforms-integrating-as-connectors): connector credentials and dataset permissions remain OPEN. | Architecture, Engineering and Provider Integration teams: confirm the fields and the setup step that uses them. | SPEC038 ONB-05; SPEC039 GAP-02/08; private-setup diagram. |
<!-- onboarding-log-table:end -->

## Diagram note to consider

For Q08.2, place this concise annotation beside **ONB-05 — Configure private choice** when the diagram is next revised:

> Private-platform setup: This provider may need extra or different setup fields compared with SPFE. Architecture and Engineering must confirm the fields. See Q08.2 in NOTE-SEI-001.

Wait for answers about certificate choice and team responsibilities before changing the other diagrams. Sending and receiving diagrams should link to this discussion where they use the same certificate rules.

## Evidence and decision handling

- **Open:** we still need an answer. **Proposed answer:** an answer has been suggested but not agreed. **Partly answered:** we have an answer or evidence for only part of the question. **Decision recorded:** record who agreed, when, the source and what they agreed. An agreed decision does not mean the software is built or tested.
- The owner column suggests who to ask. Owners and due dates still need agreement. Do not present a meeting note as a confirmed decision.
- Edit this table, then run `python3 tools/render_onboarding_question_log.py` to update the HTML. Keep one answer here. The HTML displays it and links back to it. Existing workshop and GAP IDs keep their meaning.

## Source references

<a id="r1"></a>
**R1 — Product and engineering context:** [SPEC038 prerequisites](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#65-onb-03-assess-prerequisites), [ONB-05](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#67-onb-05-configure-private-choice) and [SPEC039 GAP register](SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#2-open-engineering-decisions), repository drafts. These drafts describe the current proposal and checks still needed. They do not confirm the new choices or prove that the software is ready for production.

<a id="r2"></a>
**R2 — Choosing a certificate:** [Sage certificate management reviewed extract](../../context/Tax%20API/Certificates/sage-certificate-management-guide-extract.md), original Confluence page 759615024 v6, read 26 October 2026, credential-selection row. Describes certificate selection using `Connection-Id` for ES AFL, the Spain Anti-Fraud Legislation service. We still need to check B2B e-invoicing use and what is running today.

<a id="r3"></a>
**R3 — Find a provider and upload a certificate:** [AEAT upload reviewed extract](../../context/Tax%20API/Certificates/aeat-certificate-upload-guide-extract.md), guide received 27 October 2026; The original version and URL were not supplied. Sections “Obtain provider ID for Spain AEAT”, “Upload certificate” and “Source conflicts and limits” separate finding a provider from uploading a certificate. B2B use and the relationship between connection IDs still need confirmation.

<a id="r4"></a>
**R4 — Certificate types and URLs:** [Original SendInvoice WSDL](../../context/WSDL%20servicios%20web%20-%20PRE_23_11_26/SendInvoice.wsdl), reviewed local test release labelled 23 November 2026, `wsdl:documentation` access text and `SendInvoiceCertPort` / `SendInvoiceSealPort` addresses. The [manifest](../../assets/regulatory/spain/spfe/source-manifest.json) selects this baseline; [RES-SEI-002 release review](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026) records the missing evidence. Defined URLs do not prove certificate acceptance, permission to act for a business, or working software.
