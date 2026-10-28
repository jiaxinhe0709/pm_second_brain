```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Send e-invoice.",
    "version": "1.0.0",
    "contact": {
      "name": "Sage Network Accounts Team",
      "email": "email.protected@sage.com"
    },
    "license": {
      "name": "Sage Terms and Conditions",
      "url": "https://www.sage.com/en-us/legal/terms/"
    }
  },
  "externalDocs": {
    "url": "https://developer.sage.com/domain-services/",
    "description": "Sage Network e-Invoicing Service Documentation"
  },
  "servers": [
    {
      "url": "https://api.e-invoicing.sage.com",
      "description": "Production"
    },
    {
      "url": "https://api-sbx.e-invoicing.sage.com",
      "description": "Sandbox-Production"
    },
    {
      "url": "https://api-int.e-invoicing-eng.sage.com",
      "description": "Internal Sandbox"
    }
  ],
  "security": [
    {
      "m2m": []
    }
  ],
  "paths": {
    "/datasets/{datasetId}/e-invoices": {
      "post": {
        "security": [
          {
            "m2m": []
          }
        ],
        "operationId": "Send-Document",
        "summary": "Send e-invoice.",
        "parameters": [
          {
            "$ref": "#/components/parameters/traceparent"
          },
          {
            "$ref": "#/components/parameters/tracestate"
          },
          {
            "$ref": "#/components/parameters/Idempotency-Key"
          },
          {
            "$ref": "#/components/parameters/datasetId"
          }
        ],
        "requestBody": {
          "content": {
            "application/vnd.api+json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "$ref": "#/components/schemas/PostSendInvoiceRequest"
                  }
                },
                "required": [
                  "data"
                ]
              },
              "examples": {
                "post-einvoice-current-format": {
                  "summary": "Send e-invoice using current access point address format",
                  "value": {
                    "data": {
                      "type": "e-Invoice",
                      "attributes": {
                        "attachments": [
                          {
                            "filename": "invoice.xml",
                            "mimetype": "ubl-2.1/xml",
                            "filetype": "Undefined"
                          }
                        ],
                        "sender": {
                          "accessPointAddressType": "fr.siren",
                          "accessPointAddress": "025568524"
                        },
                        "recipient": {
                          "accessPointAddressType": "fr.siren",
                          "accessPointAddress": "025568524"
                        },
                        "accessPointId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "eInvoiceTypeCode": "AP_Invoice",
                        "erpInvoiceId": "string"
                      }
                    }
                  }
                },
                "post-einvoice-legal-format": {
                  "summary": "Send e-invoice using legal access point address format",
                  "value": {
                    "data": {
                      "type": "e-Invoice",
                      "attributes": {
                        "attachments": [
                          {
                            "filename": "invoice.xml",
                            "mimetype": "ubl-2.1/xml",
                            "filetype": "Undefined"
                          }
                        ],
                        "sender": {
                          "accessPointAddressType": "fr.sirensiret",
                          "accessPointAddress": "025568524_02556852400001"
                        },
                        "recipient": {
                          "accessPointAddressType": "fr.sirensiret",
                          "accessPointAddress": "025568524_02556852400001"
                        },
                        "accessPointId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "eInvoiceTypeCode": "AP_Invoice",
                        "erpInvoiceId": "string"
                      }
                    }
                  }
                },
                "post-einvoice-mixed-formats": {
                  "summary": "Send e-invoice using current and legal formats in the same request",
                  "value": {
                    "data": {
                      "type": "e-Invoice",
                      "attributes": {
                        "attachments": [
                          {
                            "filename": "invoice.xml",
                            "mimetype": "ubl-2.1/xml",
                            "filetype": "Undefined"
                          }
                        ],
                        "sender": {
                          "accessPointAddressType": "fr.siren",
                          "accessPointAddress": "025568524"
                        },
                        "recipient": {
                          "accessPointAddressType": "fr.sirensiret",
                          "accessPointAddress": "025568524_02556852400001"
                        },
                        "accessPointId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "eInvoiceTypeCode": "AP_Invoice",
                        "erpInvoiceId": "string"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/vnd.api+json": {
                "schema": {
                  "$ref": "#/components/schemas/PostSendInvoiceResponse"
                },
                "examples": {
                  "201 response example": {
                    "value": {
                      "data": {
                        "type": "e-Invoice",
                        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                        "attributes": {
                          "attachments": [
                            {
                              "filename": "invoice.xml",
                              "mimetype": "ubl-2.1/xml",
                              "filetype": "Undefined",
                              "uploadUrl": "https://example-bucket.s3.amazonaws.com/e-invoicing/documents/invoice.xml?AWSAccessKeyId=AKIA...&Expires=...&Signature=...\""
                            }
                          ],
                          "sender": {
                            "accessPointAddressType": "fr.siren",
                            "accessPointAddress": "025568524"
                          },
                          "recipient": {
                            "accessPointAddressType": "fr.siren",
                            "accessPointAddress": "025568524"
                          },
                          "accessPointId": "702dc7ac-1b25-441d-b256-1463188d42e1",
                          "eInvoiceTypeCode": "AP_Invoice",
                          "erpInvoiceId": "string",
                          "hold": false,
                          "currentStatus": {},
                          "history": [
                            {
                              "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
                              "statusCode": "00000000-0000-0000-0000-000000000001",
                              "status": "New",
                              "operationStatus": "COMPLETED",
                              "errorCode": null,
                              "statusAttributes": {},
                              "meta": {
                                "createdAt": "2024-06-12T10:20:30.4510000+00:00",
                                "createdSource": "123e4567-e89b-12d3-a456-426614174000",
                                "createdTraceId": "ccf441167c9f414e81f077c9b4f3d42e"
                              }
                            }
                          ]
                        },
                        "meta": {
                          "createdAt": "2024-05-22T15:13:45.8410000+00:00",
                          "createdSource": "sR1N7Mwqww1Ja41W9J0W3SxWnR5LQEiL",
                          "createdTraceId": "ccf441167c9f414e81f077c9b4f3d42e",
                          "modifiedAt": "2024-05-22T15:13:45.8410000+00:00",
                          "modifiedSource": "sR1N7Mwqww1Ja41W9J0W3SxWnR5LQEiL",
                          "modifiedTraceId": "ccf441167c9f414e81f077c9b4f3d42e"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/400"
          },
          "401": {
            "$ref": "#/components/responses/401"
          },
          "403": {
            "$ref": "#/components/responses/403"
          },
          "405": {
            "$ref": "#/components/responses/405"
          },
          "413": {
            "$ref": "#/components/responses/413"
          },
          "415": {
            "$ref": "#/components/responses/415"
          },
          "429": {
            "$ref": "#/components/responses/429"
          },
          "500": {
            "$ref": "#/components/responses/500"
          },
          "502": {
            "$ref": "#/components/responses/502"
          },
          "503": {
            "$ref": "#/components/responses/503"
          },
          "504": {
            "$ref": "#/components/responses/504"
          }
        },
        "tags": [
          "e-Invoicing"
        ],
        "x-codeSamples": [
          {
            "lang": "shell_curl",
            "name": "post-einvoice-current-format",
            "source": "curl --request POST \\\n  --url https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'Idempotency-Key: {Idempotency-Key}' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"recipient\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "post-einvoice-current-format",
            "source": "echo '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"recipient\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}' |  \\\n  http POST https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices \\\n  Content-Type:'application/vnd.api+json' \\\n  Idempotency-Key:'{Idempotency-Key}' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "post-einvoice-current-format",
            "source": "wget --quiet \\\n  --method POST \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --header 'Idempotency-Key: {Idempotency-Key}' \\\n  --body-data '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"recipient\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "post-einvoice-current-format",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\nxhr.setRequestHeader(\"Idempotency-Key\", \"{Idempotency-Key}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "post-einvoice-current-format",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\",\n  \"method\": \"POST\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "post-einvoice-current-format",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"POST\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/datasets/%7BdatasetId%7D/e-invoices\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "post-einvoice-current-format",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Post,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n        { \"Idempotency-Key\", \"{Idempotency-Key}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "post-einvoice-current-format",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\");\nvar request = new RestRequest(Method.POST);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddHeader(\"Idempotency-Key\", \"{Idempotency-Key}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "post-einvoice-current-format",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\",\n    'Idempotency-Key': \"{Idempotency-Key}\"\n    }\n\nconn.request(\"POST\", \"/datasets/%7BdatasetId%7D/e-invoices\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "post-einvoice-current-format",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n}\n\nresponse = requests.request(\"POST\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "post-einvoice-legal-format",
            "source": "curl --request POST \\\n  --url https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'Idempotency-Key: {Idempotency-Key}' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"recipient\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "post-einvoice-legal-format",
            "source": "echo '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"recipient\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}' |  \\\n  http POST https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices \\\n  Content-Type:'application/vnd.api+json' \\\n  Idempotency-Key:'{Idempotency-Key}' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "post-einvoice-legal-format",
            "source": "wget --quiet \\\n  --method POST \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --header 'Idempotency-Key: {Idempotency-Key}' \\\n  --body-data '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"recipient\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "post-einvoice-legal-format",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\nxhr.setRequestHeader(\"Idempotency-Key\", \"{Idempotency-Key}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "post-einvoice-legal-format",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\",\n  \"method\": \"POST\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "post-einvoice-legal-format",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"POST\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/datasets/%7BdatasetId%7D/e-invoices\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "post-einvoice-legal-format",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Post,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n        { \"Idempotency-Key\", \"{Idempotency-Key}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "post-einvoice-legal-format",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\");\nvar request = new RestRequest(Method.POST);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddHeader(\"Idempotency-Key\", \"{Idempotency-Key}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "post-einvoice-legal-format",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\",\n    'Idempotency-Key': \"{Idempotency-Key}\"\n    }\n\nconn.request(\"POST\", \"/datasets/%7BdatasetId%7D/e-invoices\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "post-einvoice-legal-format",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n}\n\nresponse = requests.request(\"POST\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "post-einvoice-mixed-formats",
            "source": "curl --request POST \\\n  --url https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'Idempotency-Key: {Idempotency-Key}' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"recipient\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "post-einvoice-mixed-formats",
            "source": "echo '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"recipient\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}' |  \\\n  http POST https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices \\\n  Content-Type:'application/vnd.api+json' \\\n  Idempotency-Key:'{Idempotency-Key}' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "post-einvoice-mixed-formats",
            "source": "wget --quiet \\\n  --method POST \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --header 'Idempotency-Key: {Idempotency-Key}' \\\n  --body-data '{\"data\":{\"type\":\"e-Invoice\",\"attributes\":{\"attachments\":[{\"filename\":\"invoice.xml\",\"mimetype\":\"ubl-2.1/xml\",\"filetype\":\"Undefined\"}],\"sender\":{\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\"},\"recipient\":{\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\"},\"accessPointId\":\"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\"eInvoiceTypeCode\":\"AP_Invoice\",\"erpInvoiceId\":\"string\"}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "post-einvoice-mixed-formats",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\nxhr.setRequestHeader(\"Idempotency-Key\", \"{Idempotency-Key}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "post-einvoice-mixed-formats",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\",\n  \"method\": \"POST\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "post-einvoice-mixed-formats",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"POST\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/datasets/%7BdatasetId%7D/e-invoices\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "post-einvoice-mixed-formats",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Post,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n        { \"Idempotency-Key\", \"{Idempotency-Key}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "post-einvoice-mixed-formats",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\");\nvar request = new RestRequest(Method.POST);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddHeader(\"Idempotency-Key\", \"{Idempotency-Key}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "post-einvoice-mixed-formats",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\",\n    'Idempotency-Key': \"{Idempotency-Key}\"\n    }\n\nconn.request(\"POST\", \"/datasets/%7BdatasetId%7D/e-invoices\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "post-einvoice-mixed-formats",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/datasets/%7BdatasetId%7D/e-invoices\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"e-Invoice\\\",\\\"attributes\\\":{\\\"attachments\\\":[{\\\"filename\\\":\\\"invoice.xml\\\",\\\"mimetype\\\":\\\"ubl-2.1/xml\\\",\\\"filetype\\\":\\\"Undefined\\\"}],\\\"sender\\\":{\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\"},\\\"recipient\\\":{\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\"},\\\"accessPointId\\\":\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"eInvoiceTypeCode\\\":\\\"AP_Invoice\\\",\\\"erpInvoiceId\\\":\\\"string\\\"}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\",\n    \"Idempotency-Key\": \"{Idempotency-Key}\"\n}\n\nresponse = requests.request(\"POST\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          }
        ]
      }
    }
  },
  "components": {
    "securitySchemes": {
      "m2m": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "A SageID JWT token (M2M token) is required to access this API."
      }
    },
    "parameters": {
      "traceparent": {
        "name": "traceparent",
        "in": "header",
        "required": false,
        "schema": {
          "type": "string",
          "examples": [
            "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"
          ],
          "description": "The traceparent header as defined by the [W3C TraceContext spec](https://www.w3.org/TR/trace-context-2/)."
        }
      },
      "tracestate": {
        "name": "tracestate",
        "in": "header",
        "required": false,
        "schema": {
          "type": "string",
          "examples": [
            "rojo=00f067aa0ba902b7"
          ]
        },
        "description": "The tracestate header as defined by the [W3C TraceContext spec](https://www.w3.org/TR/trace-context-2/)."
      },
      "Idempotency-Key": {
        "name": "Idempotency-Key",
        "in": "header",
        "required": true,
        "schema": {
          "type": "string",
          "examples": [
            "2131451c-f8c4-49f8-aa60-e0ec10be0e29"
          ]
        },
        "description": "An idempotency key as defined by the [IETF Idempotency-Key header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/)."
      },
      "datasetId": {
        "name": "datasetId",
        "in": "path",
        "required": true,
        "schema": {
          "type": "string",
          "format": "uuid"
        },
        "example": "747733f7-43d4-4bbb-8154-494c97c824bc"
      }
    },
    "schemas": {
      "PostSendInvoiceRequest": {
        "type": "object",
        "description": "JSON:API formatted upload source documents request.",
        "required": [
          "type",
          "attributes"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "e-Invoice"
            ]
          },
          "attributes": {
            "$ref": "#/components/schemas/SendInvoiceRequest"
          }
        }
      },
      "PostSendInvoiceResponse": {
        "type": "object",
        "description": "JSON:API formatted upload source documents response.",
        "properties": {
          "data": {
            "type": "object",
            "required": [
              "type",
              "id",
              "attributes",
              "meta"
            ],
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "e-Invoice"
                ]
              },
              "id": {
                "type": "string",
                "format": "uuid",
                "description": "The e-Invoice identifier generated"
              },
              "attributes": {
                "$ref": "#/components/schemas/SendInvoiceResponse"
              },
              "meta": {
                "$ref": "#/components/schemas/Assigned-Keys"
              }
            }
          }
        }
      },
      "SendInvoiceRequest": {
        "type": "object",
        "description": "JSON:API formatted upload source documents request.",
        "required": [
          "attachments",
          "sender",
          "recipient",
          "accessPointId"
        ],
        "properties": {
          "attachments": {
            "type": "array",
            "description": "The request of the source documents to be sent.",
            "items": {
              "required": [
                "filename",
                "mimetype"
              ],
              "properties": {
                "filename": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 128,
                  "examples": [
                    "invoice.xml"
                  ]
                },
                "mimetype": {
                  "type": "string",
                  "enum": [
                    "ubl-2.1/xml",
                    "application/pdf"
                  ]
                },
                "filetype": {
                  "type": "string",
                  "enum": [
                    "Undefined",
                    "UBL",
                    "Human_Readable",
                    "Original_Document",
                    "FacturX"
                  ]
                }
              }
            }
          },
          "sender": {
            "type": "object",
            "properties": {
              "accessPointAddressType": {
                "description": "The sender access point type",
                "type": [
                  "string",
                  "null"
                ],
                "enum": [
                  "fr.siren",
                  "fr.sirensiret",
                  "fr.siren_suffix",
                  "fr.sirensiret_routing"
                ]
              },
              "accessPointAddress": {
                "description": "The sender access point address. Typically a national tax ID. Current and legal formats are supported based on accessPointAddressType. Sender and recipient can use different formats in the same request.",
                "type": "string",
                "minLength": 1,
                "maxLength": 50,
                "examples": [
                  "025568524"
                ]
              }
            }
          },
          "recipient": {
            "type": "object",
            "properties": {
              "accessPointAddressType": {
                "description": "The recipient access point type",
                "type": [
                  "string",
                  "null"
                ],
                "enum": [
                  "fr.siren",
                  "fr.sirensiret",
                  "fr.siren_suffix",
                  "fr.sirensiret_routing"
                ]
              },
              "accessPointAddress": {
                "description": "A unique key to identify the **Buyer** in the Sender's ERP system. Typically a national tax ID. Current and legal formats are supported based on accessPointAddressType. Sender and recipient can use different formats in the same request.",
                "type": "string",
                "minLength": 1,
                "maxLength": 50,
                "examples": [
                  "025568524"
                ]
              }
            }
          },
          "accessPointId": {
            "description": "A unique key to identify the route destination.",
            "type": [
              "string",
              "null"
            ],
            "format": "uuid"
          },
          "eInvoiceTypeCode": {
            "type": "string",
            "enum": [
              "AP_Invoice",
              "AR_Invoice",
              "AP_CreditNote",
              "AR_CreditNote"
            ]
          },
          "erpInvoiceId": {
            "type": [
              "string",
              "null"
            ],
            "description": "ERP invoice ID"
          }
        }
      },
      "SendInvoiceResponse": {
        "type": "object",
        "description": "JSON:API formatted upload source documents response.",
        "required": [
          "documents"
        ],
        "properties": {
          "attachments": {
            "type": "array",
            "description": "The response of the source documents to be sent.",
            "items": {
              "properties": {
                "filename": {
                  "type": "string",
                  "examples": [
                    "invoice.xml"
                  ]
                },
                "mimetype": {
                  "type": "string",
                  "enum": [
                    "ubl-2.1/xml",
                    "application/pdf"
                  ]
                },
                "filetype": {
                  "type": "string",
                  "enum": [
                    "Undefined",
                    "UBL",
                    "Human_Readable",
                    "Original_Document",
                    "FacturX"
                  ]
                },
                "uploadUrl": {
                  "type": "string",
                  "examples": [
                    "https://example-bucket.s3.amazonaws.com/e-invoicing/documents/invoice.xml?AWSAccessKeyId=AKIA...&Expires=...&Signature=...\""
                  ]
                }
              }
            }
          },
          "sender": {
            "type": "object",
            "properties": {
              "accessPointAddressType": {
                "description": "The sender access point type",
                "type": [
                  "string",
                  "null"
                ],
                "enum": [
                  "fr.siren",
                  "fr.sirensiret",
                  "fr.siren_suffix",
                  "fr.sirensiret_routing"
                ]
              },
              "accessPointAddress": {
                "description": "The sender access point address. Typically a national tax ID.",
                "type": "string",
                "minLength": 1,
                "maxLength": 50,
                "examples": [
                  "025568524"
                ]
              }
            }
          },
          "recipient": {
            "type": "object",
            "properties": {
              "accessPointAddressType": {
                "description": "The recipient access point type",
                "type": [
                  "string",
                  "null"
                ],
                "enum": [
                  "fr.siren",
                  "fr.sirensiret",
                  "fr.siren_suffix",
                  "fr.sirensiret_routing"
                ]
              },
              "accessPointAddress": {
                "description": "A unique key to identify the **Buyer** in the Sender's ERP system. Typically a national tax ID.",
                "type": "string",
                "minLength": 1,
                "maxLength": 50,
                "examples": [
                  "025568524"
                ]
              }
            }
          },
          "accessPointId": {
            "description": "A unique key to identify the route destination.",
            "type": "string",
            "format": "uuid"
          },
          "eInvoiceTypeCode": {
            "type": "string",
            "enum": [
              "AP_Invoice",
              "AR_Invoice",
              "AP_CreditNote",
              "AR_CreditNote"
            ]
          },
          "erpInvoiceId": {
            "type": [
              "string",
              "null"
            ],
            "description": "ERP invoice ID"
          },
          "hold": {
            "type": "boolean",
            "description": "Indicates whether the e-invoice is on hold.",
            "examples": [
              false
            ]
          },
          "currentStatus": {
            "type": [
              "object",
              "null"
            ],
            "description": "The current status of the e-invoice"
          },
          "history": {
            "type": "array",
            "description": "The history of status changes for the e-invoice",
            "items": {
              "$ref": "#/components/schemas/invoiceHistoryItemResponse"
            }
          }
        }
      },
      "Assigned-Keys": {
        "type": "object",
        "properties": {
          "createdAt": {
            "type": "string",
            "format": "date-time",
            "description": "The ISO 8601 Coordinated Universal Time (UTC) date this resource was created.",
            "readOnly": true,
            "examples": [
              "2024-05-22T15:13:45.8410000+00:00"
            ]
          },
          "createdSource": {
            "description": "The source that created this resource (SageID clientID).",
            "type": "string",
            "examples": [
              "sR1N7Mwqww1Ja41W9J0W3SxWnR5LQEiL"
            ],
            "readOnly": true
          },
          "createdTraceId": {
            "description": "The trace identifier for distributed tracing during creation.",
            "type": [
              "string",
              "null"
            ],
            "examples": [
              "ccf441167c9f414e81f077c9b4f3d42e"
            ],
            "readOnly": true
          },
          "modifiedAt": {
            "type": [
              "string",
              "null"
            ],
            "format": "date-time",
            "description": "The ISO 8601 Coordinated Universal Time (UTC) date this resource was last modified.",
            "readOnly": true,
            "examples": [
              "2024-05-22T15:13:45.8410000+00:00"
            ]
          },
          "modifiedSource": {
            "description": "The source modified this resource (SageID clientID).",
            "type": [
              "string",
              "null"
            ],
            "examples": [
              "sR1N7Mwqww1Ja41W9J0W3SxWnR5LQEiL"
            ],
            "readOnly": true
          },
          "modifiedTraceId": {
            "description": "The trace identifier for distributed tracing during last modification.",
            "type": [
              "string",
              "null"
            ],
            "examples": [
              "ccf441167c9f414e81f077c9b4f3d42e"
            ],
            "readOnly": true
          }
        }
      },
      "invoiceHistoryItemResponse": {
        "type": "object",
        "properties": {
          "statusId": {
            "type": "string",
            "format": "uuid",
            "description": "The unique e-invoice status (internal) identifier"
          },
          "statusCode": {
            "type": "string",
            "description": "The unique e-invoice status identifier",
            "format": "uuid",
            "examples": [
              "00000000-0000-0000-0000-000000000001"
            ]
          },
          "status": {
            "type": "string",
            "description": "The e-Invoice status (string representation)",
            "examples": [
              "New"
            ]
          },
          "operationStatus": {
            "type": "string",
            "description": "The e-Invoice operation status (string representation)",
            "enum": [
              "IN_PROGRESS",
              "COMPLETED",
              "ERROR"
            ],
            "examples": [
              "COMPLETED"
            ]
          },
          "errorCode": {
            "type": [
              "string",
              "null"
            ],
            "description": "The e-Invoice error code",
            "examples": [
              null
            ]
          },
          "statusAttributes": {
            "type": "object",
            "description": "This object can have any property",
            "additionalProperties": true
          },
          "meta": {
            "type": "object",
            "properties": {
              "createdAt": {
                "type": "string",
                "format": "date-time",
                "description": "e-Invoice change status datetime",
                "examples": [
                  "2024-06-12T10:20:30.4510000+00:00"
                ]
              },
              "createdSource": {
                "type": "string",
                "format": "uuid",
                "description": "The source that created this resource (SageID clientID)",
                "examples": [
                  "123e4567-e89b-12d3-a456-426614174000"
                ]
              },
              "createdTraceId": {
                "description": "The trace identifier for distributed tracing during creation.",
                "type": [
                  "string",
                  "null"
                ],
                "examples": [
                  "ccf441167c9f414e81f077c9b4f3d42e"
                ]
              }
            }
          }
        }
      },
      "Errors-detailed": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Error-Details"
            }
          }
        }
      },
      "Error-Details": {
        "type": "object",
        "description": "Follows the [JSON:API error](https://jsonapi.org/format/#errors) convention.\n\nEvery member in an error object is optional, but all help the client by providing extra details.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "A unique identifier for this particular occurrence of the problem."
          },
          "source": {
            "type": "object",
            "description": "The source member is used to indicate which part of the request document caused the error.",
            "properties": {
              "pointer": {
                "type": "string",
                "description": "A [JSON pointer](https://www.rfc-editor.org/rfc/rfc6901) to the value in the request document that caused the error."
              },
              "parameter": {
                "type": "string",
                "description": "A string indicating which URI parameter caused the error."
              },
              "header": {
                "type": "string",
                "description": "A string indicating the name of a single request header which caused the error."
              }
            }
          },
          "title": {
            "type": "string",
            "description": "A generic description of the problem."
          },
          "detail": {
            "type": "string",
            "description": "A description specific to this occurrence of the problem."
          },
          "status": {
            "type": "number",
            "examples": [
              400
            ],
            "description": "The status member represents the HTTP status code associated with the problem. It’s very helpful when multiple errors are returned at once, as the HTTP response itself can only have one status code. However, it can also be useful for single errors, to save clients the trouble of consulting the HTTP headers, or in cases where a proxy might modify the original HTTP status code."
          },
          "links": {
            "type": "object",
            "description": "Supporting links.",
            "properties": {
              "about": {
                "type": "string",
                "format": "uri-reference",
                "description": "A link that leads to further details about this particular occurrence of the problem. When derefenced, it should return a human-readable description of the error."
              },
              "type": {
                "type": "string",
                "format": "uri-reference",
                "description": "A link that identifies the type of error that this particular error is an instance of. When derefenced, it should return a human-readable explanation of the general error."
              }
            }
          },
          "meta": {
            "type": "object",
            "description": "Additional, non-standard metadata about the error."
          }
        }
      },
      "Error-Simple": {
        "type": "object",
        "required": [
          "errors"
        ],
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "status",
                "title",
                "detail"
              ],
              "properties": {
                "status": {
                  "type": "integer",
                  "description": "The HTTP status code"
                },
                "title": {
                  "type": "string",
                  "description": "A short, human-readable summary of the problem"
                },
                "detail": {
                  "type": "string",
                  "description": "A human-readable explanation specific to this occurrence of the problem"
                }
              }
            }
          }
        }
      },
      "Error-Simple-With-Source": {
        "type": "object",
        "required": [
          "errors"
        ],
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "source",
                "status",
                "title",
                "detail"
              ],
              "properties": {
                "source": {
                  "type": "object",
                  "required": [
                    "header"
                  ],
                  "properties": {
                    "header": {
                      "type": "string",
                      "description": "The name of the request header that caused the error"
                    }
                  }
                },
                "status": {
                  "type": "integer",
                  "description": "The HTTP status code"
                },
                "title": {
                  "type": "string",
                  "description": "A short, human-readable summary of the problem"
                },
                "detail": {
                  "type": "string",
                  "description": "A human-readable explanation specific to this occurrence of the problem"
                }
              }
            }
          }
        }
      }
    },
    "responses": {
      "400": {
        "description": "Bad Request",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Errors-detailed"
            },
            "example": {
              "errors": [
                {
                  "id": "{datasetId}",
                  "source": {
                    "pointer": "path/to/invalid/field",
                    "parameter": "parameterName",
                    "header": "headerName"
                  },
                  "title": "Invalid request",
                  "detail": "{description of the issue}",
                  "status": 400,
                  "links": [],
                  "meta": {}
                }
              ]
            }
          }
        }
      },
      "401": {
        "description": "Unauthenticated",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 401,
                  "title": "Unauthenticated.",
                  "detail": "Unauthorized"
                }
              ]
            }
          }
        }
      },
      "403": {
        "description": "Forbidden",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 403,
                  "title": "Forbidden.",
                  "detail": "User is not authorized to access this resource with an explicit deny in an identity-based policy"
                }
              ]
            }
          }
        }
      },
      "405": {
        "description": "Method Not Allowed",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 405,
                  "title": "Method not allowed.",
                  "detail": "Invalid key=value pair"
                }
              ]
            }
          }
        }
      },
      "413": {
        "description": "Payload Too Large",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple-With-Source"
            },
            "example": {
              "errors": [
                {
                  "source": {
                    "header": "Content-Length"
                  },
                  "status": 413,
                  "title": "The 'Content-Length' header exceeds the maximum allowed size.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      },
      "415": {
        "description": "Unsupported Media Type",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple-With-Source"
            },
            "example": {
              "errors": [
                {
                  "source": {
                    "header": "Content-Type"
                  },
                  "status": 415,
                  "title": "The 'Content-Type' header does not contain an acceptable media type.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      },
      "429": {
        "description": "Too Many Requests",
        "headers": {
          "Retry-After": {
            "schema": {
              "type": "integer",
              "format": "duration"
            },
            "description": "Number of seconds to wait before making a follow-up request"
          }
        },
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 429,
                  "title": "Too many requests.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      },
      "500": {
        "description": "Internal Server Error",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 500,
                  "title": "Internal server error.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      },
      "502": {
        "description": "Bad Gateway",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 502,
                  "title": "Bad Gateway.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      },
      "503": {
        "description": "Service Unavailable",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 503,
                  "title": "Service unavailable.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      },
      "504": {
        "description": "Gateway Timeout",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 504,
                  "title": "Gateway timeout.",
                  "detail": "string"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```
