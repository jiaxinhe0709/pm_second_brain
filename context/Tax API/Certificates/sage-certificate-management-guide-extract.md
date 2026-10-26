# Sage certificate management — reviewed extract

Source: [Sage certificate management](https://confluence.sage.com/spaces/CCLD/pages/759615024/Sage+certificate+management), page 759615024, version 6; read 26 October 2026. The user also supplied a copy. This extract omits stakeholder details, images, secrets and raw exports.

The page is marked **UNDER REVIEW**, while its narrative describes an agreed ES AFL solution. It does not establish a deployed B2B contract.

| Case | Documented mechanism |
|---|---|
| Customer's certificate | The client provisions the certificate/password in Connections Service under the designated provider. Connections Service uses the AFL encryption endpoint and stores encrypted credentials; AFL decrypts them for protected use. |
| Sage-owned seal | A dedicated provider and special credential type select one centrally stored, pre-encrypted Sage seal. Exact provider/type values are not supplied. The source chooses Secrets Manager in the Connections Service account, with AFL controlling decryption. |
| Credential selection | The client supplies the selected credential connection ID in the exact request header `Connection-Id`. This is documented for ES AFL; the B2B binding still needs confirmation. |
| Customer agreement for the Sage seal | The signed agreement for that purpose must be stored by Sage before the seal can be used. B2B eligibility and purpose require separate qualification. |
| Expiry/rotation | The design describes manual rotation and expiry monitoring. It does not supply an automated validation/readiness response contract. |

The document does not define a `certificate` property on the E-Invoice access-point APIs, a Tax certificate-readiness JSON response, or equivalence between a credential connection and an access-point connection. It does not establish that the proposed Tax Vault and the described Connections Service/AFL store are one implementation.

The linked [Connections Service API extract](connections-service-certificate-guide-extract.md) records the available certificate provisioning and internal-encryption fields.
