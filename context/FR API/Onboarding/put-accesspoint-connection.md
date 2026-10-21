```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Update access point connection.",
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
    "/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/": {
      "put": {
        "security": [
          {
            "m2m": []
          }
        ],
        "operationId": "Put-AccessPoint-Connection",
        "summary": "Update access point connection.",
        "parameters": [
          {
            "$ref": "#/components/parameters/traceparent"
          },
          {
            "$ref": "#/components/parameters/tracestate"
          },
          {
            "$ref": "#/components/parameters/datasetId"
          },
          {
            "$ref": "#/components/parameters/accessPointId"
          },
          {
            "$ref": "#/components/parameters/connectionId"
          }
        ],
        "requestBody": {
          "content": {
            "application/vnd.api+json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "$ref": "#/components/schemas/PutAccessPointConnectionRequest"
                  }
                },
                "required": [
                  "data"
                ]
              },
              "examples": {
                "update-address-effective+end-dates": {
                  "summary": "Update an existing access point address (effectiveDate / endDate only)",
                  "value": {
                    "data": {
                      "type": "AccessPointConnection",
                      "attributes": {
                        "accessPointAddresses": [
                          {
                            "action": "update",
                            "accessPointAddressType": "fr.siren",
                            "accessPointAddress": "025568524",
                            "effectiveDate": "2025/11/01",
                            "endDate": "2027/01/01"
                          }
                        ]
                      }
                    }
                  }
                },
                "update-address-only-effective-date": {
                  "summary": "Update an existing access point address (only effectiveDate)",
                  "value": {
                    "data": {
                      "type": "AccessPointConnection",
                      "attributes": {
                        "accessPointAddresses": [
                          {
                            "action": "update",
                            "accessPointAddressType": "fr.siren",
                            "accessPointAddress": "025568524",
                            "effectiveDate": "2025/11/01"
                          }
                        ]
                      }
                    }
                  }
                },
                "update-address-only-end-date": {
                  "summary": "Update an existing access point address (only endDate)",
                  "value": {
                    "data": {
                      "type": "AccessPointConnection",
                      "attributes": {
                        "accessPointAddresses": [
                          {
                            "action": "update",
                            "accessPointAddressType": "fr.siren",
                            "accessPointAddress": "025568524",
                            "endDate": "2026/08/30"
                          }
                        ]
                      }
                    }
                  }
                },
                "mixed-actions-success": {
                  "summary": "Add a new address and update an existing address in the same request",
                  "value": {
                    "data": {
                      "type": "AccessPointConnection",
                      "attributes": {
                        "accessPointAddresses": [
                          {
                            "action": "add",
                            "accessPointAddressType": "fr.sirensiret",
                            "accessPointAddress": "02556852400001",
                            "effectiveDate": "2026/07/30",
                            "usage": [
                              "SEND"
                            ]
                          },
                          {
                            "action": "update",
                            "accessPointAddressType": "fr.siren",
                            "accessPointAddress": "025568524",
                            "effectiveDate": "2026/07/30",
                            "endDate": "2026/08/30"
                          }
                        ]
                      }
                    }
                  }
                },
                "mixed-actions-with-legal-format": {
                  "summary": "Add and update addresses using legal formats in the same request",
                  "value": {
                    "data": {
                      "type": "AccessPointConnection",
                      "attributes": {
                        "accessPointAddresses": [
                          {
                            "action": "add",
                            "accessPointAddressType": "fr.sirensiret",
                            "accessPointAddress": "02556852400002",
                            "effectiveDate": "2026/07/30",
                            "usage": [
                              "SEND"
                            ]
                          },
                          {
                            "action": "update",
                            "accessPointAddressType": "fr.sirensiret",
                            "accessPointAddress": "025568524_02556852400001",
                            "effectiveDate": "2026/07/30",
                            "endDate": "2026/08/30"
                          }
                        ]
                      }
                    }
                  }
                },
                "mixed-actions-with-mixed-format": {
                  "summary": "Add and update addresses using legal and current formats in the same request",
                  "value": {
                    "data": {
                      "type": "AccessPointConnection",
                      "attributes": {
                        "accessPointAddresses": [
                          {
                            "action": "add",
                            "accessPointAddressType": "fr.siren_suffix",
                            "accessPointAddress": "025568524SUFFIX-01",
                            "effectiveDate": "2026/07/30",
                            "usage": [
                              "SEND"
                            ]
                          },
                          {
                            "action": "update",
                            "accessPointAddressType": "fr.sirensiret",
                            "accessPointAddress": "025568524_02556852400001",
                            "effectiveDate": "2026/07/30",
                            "endDate": "2026/08/30"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/vnd.api+json": {
                "schema": {
                  "$ref": "#/components/schemas/PutAccessPointConnectionResponse"
                },
                "examples": {
                  "200 response example": {
                    "value": {
                      "data": {
                        "type": "AccessPointConnection",
                        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                        "attributes": {
                          "accessPointAddresses": [
                            {
                              "action": "add",
                              "mandateNumber": "123456789_234098678_20250630_01",
                              "accessPointAddressType": "fr.siren",
                              "accessPointAddress": "025568524",
                              "effectiveDate": "2025/10/25",
                              "endDate": "2026/10/25",
                              "status": "IN_PROGRESS",
                              "errorCode": "string"
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
          "404": {
            "$ref": "#/components/responses/404"
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
          "Onboarding"
        ],
        "x-codeSamples": [
          {
            "lang": "shell_curl",
            "name": "update-address-effective+end-dates",
            "source": "curl --request PUT \\\n  --url https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2025/11/01\",\"endDate\":\"2027/01/01\"}]}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "update-address-effective+end-dates",
            "source": "echo '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2025/11/01\",\"endDate\":\"2027/01/01\"}]}}}' |  \\\n  http PUT https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  Content-Type:'application/vnd.api+json' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "update-address-effective+end-dates",
            "source": "wget --quiet \\\n  --method PUT \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --body-data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2025/11/01\",\"endDate\":\"2027/01/01\"}]}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "update-address-effective+end-dates",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "update-address-effective+end-dates",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"method\": \"PUT\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "update-address-effective+end-dates",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"PUT\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "update-address-effective+end-dates",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Put,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "update-address-effective+end-dates",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nvar request = new RestRequest(Method.PUT);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "update-address-effective+end-dates",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\"\n    }\n\nconn.request(\"PUT\", \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "update-address-effective+end-dates",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\",\\\"endDate\\\":\\\"2027/01/01\\\"}]}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n}\n\nresponse = requests.request(\"PUT\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "update-address-only-effective-date",
            "source": "curl --request PUT \\\n  --url https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2025/11/01\"}]}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "update-address-only-effective-date",
            "source": "echo '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2025/11/01\"}]}}}' |  \\\n  http PUT https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  Content-Type:'application/vnd.api+json' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "update-address-only-effective-date",
            "source": "wget --quiet \\\n  --method PUT \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --body-data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2025/11/01\"}]}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "update-address-only-effective-date",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "update-address-only-effective-date",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"method\": \"PUT\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "update-address-only-effective-date",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"PUT\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "update-address-only-effective-date",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Put,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "update-address-only-effective-date",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nvar request = new RestRequest(Method.PUT);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "update-address-only-effective-date",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\"\n    }\n\nconn.request(\"PUT\", \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "update-address-only-effective-date",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2025/11/01\\\"}]}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n}\n\nresponse = requests.request(\"PUT\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "update-address-only-end-date",
            "source": "curl --request PUT \\\n  --url https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"endDate\":\"2026/08/30\"}]}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "update-address-only-end-date",
            "source": "echo '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"endDate\":\"2026/08/30\"}]}}}' |  \\\n  http PUT https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  Content-Type:'application/vnd.api+json' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "update-address-only-end-date",
            "source": "wget --quiet \\\n  --method PUT \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --body-data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"endDate\":\"2026/08/30\"}]}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "update-address-only-end-date",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "update-address-only-end-date",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"method\": \"PUT\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "update-address-only-end-date",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"PUT\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "update-address-only-end-date",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Put,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "update-address-only-end-date",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nvar request = new RestRequest(Method.PUT);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "update-address-only-end-date",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\"\n    }\n\nconn.request(\"PUT\", \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "update-address-only-end-date",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n}\n\nresponse = requests.request(\"PUT\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "mixed-actions-success",
            "source": "curl --request PUT \\\n  --url https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"02556852400001\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "mixed-actions-success",
            "source": "echo '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"02556852400001\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}' |  \\\n  http PUT https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  Content-Type:'application/vnd.api+json' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "mixed-actions-success",
            "source": "wget --quiet \\\n  --method PUT \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --body-data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"02556852400001\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.siren\",\"accessPointAddress\":\"025568524\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "mixed-actions-success",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "mixed-actions-success",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"method\": \"PUT\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "mixed-actions-success",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"PUT\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "mixed-actions-success",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Put,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "mixed-actions-success",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nvar request = new RestRequest(Method.PUT);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "mixed-actions-success",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\"\n    }\n\nconn.request(\"PUT\", \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "mixed-actions-success",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.siren\\\",\\\"accessPointAddress\\\":\\\"025568524\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n}\n\nresponse = requests.request(\"PUT\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "mixed-actions-with-legal-format",
            "source": "curl --request PUT \\\n  --url https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"02556852400002\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "mixed-actions-with-legal-format",
            "source": "echo '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"02556852400002\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}' |  \\\n  http PUT https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  Content-Type:'application/vnd.api+json' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "mixed-actions-with-legal-format",
            "source": "wget --quiet \\\n  --method PUT \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --body-data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"02556852400002\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "mixed-actions-with-legal-format",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "mixed-actions-with-legal-format",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"method\": \"PUT\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "mixed-actions-with-legal-format",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"PUT\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "mixed-actions-with-legal-format",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Put,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "mixed-actions-with-legal-format",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nvar request = new RestRequest(Method.PUT);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "mixed-actions-with-legal-format",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\"\n    }\n\nconn.request(\"PUT\", \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "mixed-actions-with-legal-format",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"02556852400002\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n}\n\nresponse = requests.request(\"PUT\", url, data=payload, headers=headers)\n\nprint(response.text)",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_curl",
            "name": "mixed-actions-with-mixed-format",
            "source": "curl --request PUT \\\n  --url https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.siren_suffix\",\"accessPointAddress\":\"025568524SUFFIX-01\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_httpie",
            "name": "mixed-actions-with-mixed-format",
            "source": "echo '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.siren_suffix\",\"accessPointAddress\":\"025568524SUFFIX-01\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}' |  \\\n  http PUT https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/ \\\n  Content-Type:'application/vnd.api+json' \\\n  traceparent:'{traceparent}' \\\n  tracestate:'{tracestate}'",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "shell_wget",
            "name": "mixed-actions-with-mixed-format",
            "source": "wget --quiet \\\n  --method PUT \\\n  --header 'Content-Type: application/vnd.api+json' \\\n  --header 'traceparent: {traceparent}' \\\n  --header 'tracestate: {tracestate}' \\\n  --body-data '{\"data\":{\"type\":\"AccessPointConnection\",\"attributes\":{\"accessPointAddresses\":[{\"action\":\"add\",\"accessPointAddressType\":\"fr.siren_suffix\",\"accessPointAddress\":\"025568524SUFFIX-01\",\"effectiveDate\":\"2026/07/30\",\"usage\":[\"SEND\"]},{\"action\":\"update\",\"accessPointAddressType\":\"fr.sirensiret\",\"accessPointAddress\":\"025568524_02556852400001\",\"effectiveDate\":\"2026/07/30\",\"endDate\":\"2026/08/30\"}]}}}' \\\n  --output-document \\\n  - https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_xhr",
            "name": "mixed-actions-with-mixed-format",
            "source": "const data = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\";\n\nconst xhr = new XMLHttpRequest();\nxhr.withCredentials = true;\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nxhr.setRequestHeader(\"Content-Type\", \"application/vnd.api+json\");\nxhr.setRequestHeader(\"traceparent\", \"{traceparent}\");\nxhr.setRequestHeader(\"tracestate\", \"{tracestate}\");\n\nxhr.send(data);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "javascript_jquery",
            "name": "mixed-actions-with-mixed-format",
            "source": "const settings = {\n  \"async\": true,\n  \"crossDomain\": true,\n  \"url\": \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"method\": \"PUT\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  },\n  \"data\": \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n};\n\n$.ajax(settings).done(function (response) {\n  console.log(response);\n});",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "node_native",
            "name": "mixed-actions-with-mixed-format",
            "source": "const http = require(\"https\");\n\nconst options = {\n  \"method\": \"PUT\",\n  \"hostname\": \"api.e-invoicing.sage.com\",\n  \"port\": null,\n  \"path\": \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\",\n  \"headers\": {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n  }\n};\n\nconst req = http.request(options, function (res) {\n  const chunks = [];\n\n  res.on(\"data\", function (chunk) {\n    chunks.push(chunk);\n  });\n\n  res.on(\"end\", function () {\n    const body = Buffer.concat(chunks);\n    console.log(body.toString());\n  });\n});\n\nreq.write(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\");\nreq.end();",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_httpclient",
            "name": "mixed-actions-with-mixed-format",
            "source": "var client = new HttpClient();\nvar request = new HttpRequestMessage\n{\n    Method = HttpMethod.Put,\n    RequestUri = new Uri(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"),\n    Headers =\n    {\n        { \"traceparent\", \"{traceparent}\" },\n        { \"tracestate\", \"{tracestate}\" },\n    },\n    Content = new StringContent(\"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\")\n    {\n        Headers =\n        {\n            ContentType = new MediaTypeHeaderValue(\"application/vnd.api+json\")\n        }\n    }\n};\nusing (var response = await client.SendAsync(request))\n{\n    response.EnsureSuccessStatusCode();\n    var body = await response.Content.ReadAsStringAsync();\n    Console.WriteLine(body);\n}",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "csharp_restsharp",
            "name": "mixed-actions-with-mixed-format",
            "source": "var client = new RestClient(\"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\");\nvar request = new RestRequest(Method.PUT);\nrequest.AddHeader(\"Content-Type\", \"application/vnd.api+json\");\nrequest.AddHeader(\"traceparent\", \"{traceparent}\");\nrequest.AddHeader(\"tracestate\", \"{tracestate}\");\nrequest.AddParameter(\"application/vnd.api+json\", \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_python3",
            "name": "mixed-actions-with-mixed-format",
            "source": "import http.client\n\nconn = http.client.HTTPSConnection(\"api.e-invoicing.sage.com\")\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\n\nheaders = {\n    'Content-Type': \"application/vnd.api+json\",\n    'traceparent': \"{traceparent}\",\n    'tracestate': \"{tracestate}\"\n    }\n\nconn.request(\"PUT\", \"/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\", payload, headers)\n\nres = conn.getresponse()\ndata = res.read()\n\nprint(data.decode(\"utf-8\"))",
            "mimeType": "application/vnd.api+json",
            "isAutoGenerated": true
          },
          {
            "lang": "python_requests",
            "name": "mixed-actions-with-mixed-format",
            "source": "import requests\n\nurl = \"https://api.e-invoicing.sage.com/connectors/%7BaccessPointId%7D/datasets/%7BdatasetId%7D/connections/%7BconnectionId%7D/\"\n\npayload = \"{\\\"data\\\":{\\\"type\\\":\\\"AccessPointConnection\\\",\\\"attributes\\\":{\\\"accessPointAddresses\\\":[{\\\"action\\\":\\\"add\\\",\\\"accessPointAddressType\\\":\\\"fr.siren_suffix\\\",\\\"accessPointAddress\\\":\\\"025568524SUFFIX-01\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"usage\\\":[\\\"SEND\\\"]},{\\\"action\\\":\\\"update\\\",\\\"accessPointAddressType\\\":\\\"fr.sirensiret\\\",\\\"accessPointAddress\\\":\\\"025568524_02556852400001\\\",\\\"effectiveDate\\\":\\\"2026/07/30\\\",\\\"endDate\\\":\\\"2026/08/30\\\"}]}}}\"\nheaders = {\n    \"Content-Type\": \"application/vnd.api+json\",\n    \"traceparent\": \"{traceparent}\",\n    \"tracestate\": \"{tracestate}\"\n}\n\nresponse = requests.request(\"PUT\", url, data=payload, headers=headers)\n\nprint(response.text)",
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
      "datasetId": {
        "name": "datasetId",
        "in": "path",
        "required": true,
        "schema": {
          "type": "string",
          "format": "uuid"
        },
        "example": "747733f7-43d4-4bbb-8154-494c97c824bc"
      },
      "accessPointId": {
        "name": "accessPointId",
        "in": "path",
        "description": "The e-invoicing access point identifier.",
        "required": true,
        "schema": {
          "type": "string",
          "format": "uuid",
          "examples": [
            "69a7eb0a-ac7e-4203-a765-a23b86601459"
          ]
        }
      },
      "connectionId": {
        "name": "connectionId",
        "in": "path",
        "description": "The e-invoicing access point connection identifier.",
        "required": true,
        "schema": {
          "type": "string",
          "format": "uuid",
          "examples": [
            "69a7eb0a-ac7e-4203-a765-a23b86601459"
          ]
        }
      }
    },
    "schemas": {
      "PutAccessPointConnectionRequest": {
        "type": "object",
        "required": [
          "type"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "AccessPointConnection"
            ]
          },
          "attributes": {
            "$ref": "#/components/schemas/UpdateAccessPointConnectionRequest"
          }
        }
      },
      "PutAccessPointConnectionResponse": {
        "type": "object",
        "description": "JSON:API formatted access point connection update response.",
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
                  "AccessPointConnection"
                ]
              },
              "id": {
                "type": "string",
                "format": "uuid",
                "description": "Id of the connection"
              },
              "attributes": {
                "$ref": "#/components/schemas/UpdateAccessPointConnectionResponse"
              },
              "meta": {
                "$ref": "#/components/schemas/Assigned-Keys"
              }
            }
          }
        }
      },
      "UpdateAccessPointConnectionRequest": {
        "type": "object",
        "properties": {
          "companyName": {
            "type": "string",
            "maximum": 128,
            "examples": [
              "Company A"
            ]
          },
          "companyAddress": {
            "type": "string",
            "maximum": 128,
            "examples": [
              "1234 Main St, City, Country"
            ]
          },
          "companyPostalCode": {
            "type": "string",
            "maximum": 32,
            "examples": [
              12345
            ]
          },
          "companyCountryCode": {
            "type": "string",
            "maximum": 3,
            "examples": [
              "FR"
            ]
          },
          "user": {
            "type": "object",
            "properties": {
              "firstName": {
                "type": "string",
                "maximum": 64,
                "examples": [
                  "John"
                ]
              },
              "lastName": {
                "type": "string",
                "maximum": 128,
                "examples": [
                  "Doe"
                ]
              },
              "jobTitle": {
                "type": "string",
                "maximum": 128,
                "examples": [
                  "Finance Manager"
                ]
              },
              "emailAddress": {
                "type": "string",
                "maximum": 128,
                "format": "email",
                "examples": [
                  "john.doe@sage.com"
                ]
              },
              "clientIPAddress": {
                "oneOf": [
                  {
                    "type": "string",
                    "maximum": 128,
                    "format": "ipv4"
                  },
                  {
                    "type": "string",
                    "maximum": 128,
                    "format": "ipv6"
                  }
                ],
                "examples": [
                  "183.342.1.1"
                ]
              }
            }
          },
          "accessPointAddresses": {
            "type": "array",
            "minItems": 1,
            "description": "All accessPointAddress values in this array must share the same base SIREN prefix.\nRequests mixing different base SIREN prefixes are rejected with 400 Bad Request.\nCurrent and legal formats can be mixed in the same request.\n",
            "items": {
              "type": "object",
              "required": [
                "action",
                "accessPointAddressType",
                "accessPointAddress"
              ],
              "properties": {
                "action": {
                  "type": "string",
                  "enum": [
                    "add",
                    "update"
                  ],
                  "description": "Action to perform on the access point address\nadd: add a new access point address connection\nupdate: update an existing access point address connection (only effectiveDate, endDate can be updated)\n"
                },
                "accessPointAddressType": {
                  "description": "The recipient access point type",
                  "type": "string",
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
                  "maxLength": 114,
                  "examples": [
                    "025568524",
                    "02556852400001",
                    "025568524_02556852400001",
                    "025568524SUFFIX-01",
                    "025568524_SUFFIX-01",
                    "02556852400001ROUTING",
                    "025568524_02556852400001_ROUTING"
                  ]
                },
                "effectiveDate": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "format": "YYYY/MM/DD",
                  "maximum": 50,
                  "description": "Indicate when the access point connection is effective.\nNOTE: The minimum date must be today + 1 day.\n",
                  "examples": [
                    "2025/10/25"
                  ]
                },
                "endDate": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "format": "YYYY/MM/DD",
                  "maximum": 50,
                  "description": "Indicate when the access point connection ends.\nNOTE: The end date must be greater than the effective date.\n",
                  "examples": [
                    "2026/10/25"
                  ]
                },
                "usage": {
                  "type": [
                    "array",
                    "null"
                  ],
                  "description": "The permitted operations for this access point address.\nIf null (or not present), all operations are allowed (send, receive, e-reporting).\nOnly one value can be specified at a time.\nOnly allowed if the action = \"add\"\n",
                  "maxItems": 1,
                  "items": {
                    "type": "string",
                    "enum": [
                      "SEND",
                      "EREPORTING"
                    ]
                  },
                  "examples": [
                    null,
                    [
                      "SEND"
                    ],
                    [
                      "EREPORTING"
                    ]
                  ]
                }
              }
            }
          }
        }
      },
      "UpdateAccessPointConnectionResponse": {
        "type": "object",
        "properties": {
          "accessPointAddresses": {
            "type": "array",
            "description": "All accessPointAddress values in this array must share the same base SIREN prefix.\nRequests mixing different base SIREN prefixes are rejected with 400 Bad Request.\n",
            "items": {
              "properties": {
                "action": {
                  "type": "string",
                  "enum": [
                    "add",
                    "update"
                  ],
                  "description": "Action to perform on the access point address\nadd: add a new access point address connection\nupdate: update an existing access point address connection (only effectiveDate, endDate can be updated)\n",
                  "examples": [
                    "add",
                    "update"
                  ]
                },
                "mandateNumber": {
                  "type": "string",
                  "description": "Is a value generated per Opt-in-form based on SIREN (specific for France).\nFormat of a Mandate number = SIREN + PDP reference + onboaridng date + unique sequential number 01,02\n",
                  "maxLength": 50,
                  "examples": [
                    "123456789_234098678_20250630_01"
                  ]
                },
                "accessPointAddressType": {
                  "description": "The recipient access point type",
                  "type": "string",
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
                },
                "effectiveDate": {
                  "type": "string",
                  "format": "YYYY/MM/DD",
                  "description": "Indicate when the access point connection is effective.\nNOTE: The minimum date must be today + 1 day.\n",
                  "examples": [
                    "2025/10/25"
                  ]
                },
                "endDate": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "format": "YYYY/MM/DD",
                  "description": "Indicate when the access point connection ends.\nNOTE: The end date must be greater than the effective date.\n",
                  "examples": [
                    "2026/10/25"
                  ]
                },
                "status": {
                  "type": "string",
                  "enum": [
                    "IN_PROGRESS",
                    "RETRYING",
                    "CONNECTED",
                    "DISCONNECTED",
                    "ERROR"
                  ]
                },
                "errorCode": {
                  "type": [
                    "string",
                    "null"
                  ]
                }
              }
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
      "404": {
        "description": "Not Found",
        "content": {
          "application/vnd.api+json": {
            "schema": {
              "$ref": "#/components/schemas/Error-Simple"
            },
            "example": {
              "errors": [
                {
                  "status": 404,
                  "title": "Not found",
                  "detail": "string"
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
