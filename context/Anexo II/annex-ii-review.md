# Annex II lifecycle field comparison

Reviewed 22 October 2026 for SPEC-SEI-028–030. This is a source-reading aid, not a new legal requirement or executed API test.

| Source | Identity and limit |
|---|---|
| SPFE-S22 | [Supplied original PDF](<A2-Proyecto-OM-FE 21-10-26.pdf>), 15 pages. Filename date: 21 October 2026. PDF creation/modification metadata: 20 October 2026. No formal release version, public download provenance or supersession notice supplied. |
| Snapshot hash | SHA-256 `a28dc3dae7a8c149fff5bb7099305bfd1486554c2b505507cdd0ae0452bccf0b`. Identifies local bytes; does not establish authority. |
| Legal baseline | SPFE-S02, [final Order HAC/1028/2026](../BOE-A-2026-20587.pdf), published 5 October 2026; Annex II pp. 35–42, field tables pp. 36–42. [Official publication](https://www.boe.es/eli/es/o/2026/10/02/hac1028) checked 22 October. |
| Comparison baseline | [Original field ledger](../../assets/regulatory/spain/spfe/field-traceability.json), all 52 AXII rows with original BOE XML locators and cells. |
| Searchable source | [Supplement Spanish text](../../assets/regulatory/spain/spfe/lifecycle-annex-supplement.es.txt). Original PDF layout controls table interpretation. |

## Result and method

No material change was found in the reviewed event codes, actor split, 52 field/group occurrences, source names, descriptions, cardinalities, literal UBL paths or L1 reasons. The comparison checked the ordered 52 cardinalities from PDF pp. 4–14 against the AXII ledger. It matched every field name, description and nonempty literal path within the corresponding message pages after removing PDF wrapping/whitespace and normalising the ordinal `7.ª` / `7ª`. Source spelling and path defects remain preserved in the originals.

Table layout and continued rows were inspected in the rendered PDF. This is not byte equality, complete XML-schema conformance, a legal supersession finding or proof of complete ERP/API mappings. The snapshot contains no revised service response catalogue, reporting calendar, production endpoint or error dictionary.

| Exact code / actor | Supplement pages | Field/group rows | Final BOE pages | Result |
|---|---|---|---|---|
| `PAYMENT` / recipient | 4–6 | 11 | 36–37 | Required payment and due dates; conditional receipt dates and corrected/negative indicators retained. |
| `CANCELPAYMENT` / recipient | 6 | 4 | 37 | Invoice-reference fields retained. |
| `REJECTION` / recipient | 7 | 7 | 38–39 | Rejection date, L1 reason and invoice group retained. |
| `CANCELREJECTION` / recipient | 8 | 4 | 38–39 | Invoice-reference fields retained. |
| `SETTLEMENT` / issuer | 9–10 | 10 | 39–40 | Required collection date; conditional due date, financing and receipt fields retained. |
| `CANCELSETTLEMENT` / issuer | 11 | 4 | 40 | Invoice-reference fields retained. |
| `DEFAULT` / issuer | 12–13 | 8 | 41–42 | Required due date in EffectiveDate; conditional receipt dates retained. |
| `CANCELDEFAULT` / issuer | 14 | 4 | 42 | Invoice-reference fields retained. |
| L1 rejection reasons | 15 | Code list | 42 | `01` commercial rejection; `02` private consumption/not related to business activity. |

## Open implementation evidence

| Evidence gap | Consequence and accountable role |
|---|---|
| Literal PAYMENT ShipmentDate path on p. 5 includes missing/repeated separators | Format/public-integration owner must obtain a validated schema/path decision; do not silently fix the source. SPFE-Q16; LIF-G04. |
| `CorrectedInvoice`, `NegativeAmountInvoice` and `FinancingArrangement` specify source selectors but not a complete executable indicator contract | Spain/API/DTS owners must qualify actual serialization, values and fixtures. A generic prepaid wire field is not established. |
| Cancellation seller-name rows carry `++` while adjacent invoice identifiers carry `+` | Format owner must qualify actual XML hierarchy; table levels are not complete schema evidence. |
| WSDLs transport opaque UBL attachments; complete event business formats remain pending in SPFE-S08 | Public connector/API owners must qualify full envelope, schema, per-item outcomes, errors, correlation and safe correction/reconciliation. SPFE-Q16/17. |
| Public legal fields differ from French status attributes | Lifecycle/API and Spain owners must qualify country identifiers, actor rules, dates and reasons before enabling reuse. French UUIDs and reasons cannot stand in for Annex II codes. |

The [logical lifecycle view](../../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) uses this review beside SPFE-S02/S03. The [API assessment](../../specs/invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) owns implementation reuse gates. The original SPEC-SEI-009 and field ledger remain unchanged.
