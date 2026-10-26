"""Check grey source fields and blue proposals, and refresh the local preview."""
from pathlib import Path
from html.parser import HTMLParser
import html
import json
import re
import uuid

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'specs/onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md'
OUT = ROOT / 'work/onboarding-api-reference-review'
text = DOC.read_text()
meta = yaml.safe_load(text.split('---', 2)[1])
body = text.split('---', 2)[2]
assert meta['id'] == 'SPEC-SEI-040' and meta['status'] == 'draft'
assert meta['confluence']['publish'] and meta['confluence']['parent_page_id'] == '837610648'
assert {'SPEC-SEI-001', 'SPEC-SEI-039'} <= set(meta['related'])
assert not re.search(r'!\[|<svg|<img|\.drawio|```mermaid', body)
assert len(re.findall(r'^### 1\.[1-5] API-0[1-5]', body, re.M)) == 5

class Examples(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current = None
        self.blue_depth = 0
        self.blue_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'pre':
            assert 'color:#666666;' in attrs.get('style', '')
            self.current = {'text': [], 'blue_values': []}
        if self.current is not None and tag == 'span':
            assert 'color:#1565C0;' in attrs.get('style', '')
            self.blue_depth += 1
            self.blue_text = []

    def handle_data(self, data):
        if self.current is not None:
            self.current['text'].append(data)
            if self.blue_depth:
                self.blue_text.append(data)

    def handle_endtag(self, tag):
        if tag == 'span' and self.current is not None and self.blue_depth:
            self.current['blue_values'].append(json.loads(''.join(self.blue_text)))
            self.blue_depth -= 1
        if tag == 'pre':
            self.current['payload'] = json.loads(''.join(self.current['text']))
            self.blocks.append(self.current)
            self.current = None

markup = markdown.markdown(body, extensions=['tables', 'toc', 'fenced_code'])
examples = Examples()
examples.feed(markup)
assert len(examples.blocks) == 11  # Seven E-Invoice examples plus four credential/encryption examples.
filenames = ['get-accesspoints.md', 'get-dataset-accesspoints.md',
             'new-accesspoint-connection.md', 'get-accesspoint-connection.md',
             'put-accesspoint-connection.md']
contracts = []
operations = []
for filename in filenames:
    raw = (ROOT / 'context/FR API/Onboarding' / filename).read_text()
    contract = json.loads(re.search(r'```json\s*([\s\S]*?)```', raw)[1])
    path, methods = next(iter(contract['paths'].items()))
    method, operation = next(iter(methods.items()))
    assert html.escape(f'{method.upper()} {path}') in markup
    contracts.append(contract)
    operations.append(operation)

def resolve(schema, contract):
    if '$ref' not in schema:
        return schema
    value = contract
    for part in schema['$ref'][2:].split('/'):
        value = value[part]
    return resolve(value, contract)

checked = 0
def check(value, schema, contract, blue_values, require_fields, path=''):
    global checked
    checked += 1
    schema = resolve(schema, contract)
    if isinstance(value, dict):
        if require_fields:
            assert set(schema.get('required', [])) <= set(value), path
        assert set(value) <= set(schema.get('properties', {})), (path, 'unknown field')
        for name, child in value.items():
            check(child, schema['properties'][name], contract, blue_values,
                  require_fields, path + '/' + name)
    elif isinstance(value, list):
        assert len(value) >= schema.get('minItems', 0)
        assert len(value) <= schema.get('maxItems', len(value))
        for index, child in enumerate(value):
            check(child, schema['items'], contract, blue_values,
                  require_fields, path + f'/{index}')
    else:
        allowed = schema.get('type')
        if allowed:
            allowed = allowed if isinstance(allowed, list) else [allowed]
            kind = 'null' if value is None else 'string' if isinstance(value, str) else 'number'
            assert kind in allowed, (path, kind, allowed)
        # Blue values intentionally illustrate country values not yet in the contract.
        if value not in blue_values:
            if 'enum' in schema:
                assert value in schema['enum'], (path, value)
            if schema.get('format') == 'uuid':
                uuid.UUID(value)

mapping = [(0, False), (1, False), (2, True), (2, False),
           (3, False), (4, True), (4, False)]
for block, (index, request) in zip(examples.blocks, mapping):
    op = operations[index]
    schema = (op['requestBody']['content']['application/vnd.api+json']['schema'] if request
              else next(v for k, v in op['responses'].items() if k.startswith('2'))
              ['content']['application/vnd.api+json']['schema'])
    check(block['payload'], schema, contracts[index], block['blue_values'], request)
    assert set(block['blue_values']) <= {
        'ES', 'SPAIN_ADDRESS_TYPE_TBD', 'NIF_TBD',
        'B2B Router', 'Banqup (Unifiedpost)', 'EDICOM', 'SERES (Docaposte)', 'ZeroComa',
        '00000000-0000-4000-8000-000000000002',
        '00000000-0000-4000-8000-000000000101',
        '00000000-0000-4000-8000-000000000102',
        '00000000-0000-4000-8000-000000000103',
        '00000000-0000-4000-8000-000000000104',
    }

catalogue = examples.blocks[0]['payload']['data']
assert [entry['attributes']['name'] for entry in catalogue] == [
    'B2B Router', 'Banqup (Unifiedpost)', 'EDICOM', 'SERES (Docaposte)', 'ZeroComa']
assert len({entry['id'] for entry in catalogue}) == 5
saved = examples.blocks[1]['payload']['data']
assert len(saved) == 2 and saved[0]['id'] == catalogue[0]['id']
assert saved[1]['id'] == catalogue[1]['id']
assert len({entry['attributes']['connectionId'] for entry in saved}) == len(saved)
assert saved[0]['attributes']['name'] == 'B2B Router'
assert saved[0]['attributes']['connectionId'] == examples.blocks[3]['payload']['data']['id']
assert all(phrase in body for phrase in [
    'skip API-03', 'Alternative: Sage setup is missing',
    'All sample business details and UUIDs are synthetic',
    'Tax credential provider', 'B2B Router API credentials are separate',
    'No verified onboarding payload is available', 'REF-PROVIDERS', 'REF-B2BR', 'REF-ZEROCOMA'])

credential_request, credential_response, encryption_request, encryption_response = [b['payload'] for b in examples.blocks[7:]]
assert credential_request['data']['type'] == credential_response['data']['type'] == 'Connection'
credentials = credential_request['data']['attributes']['credentials']
assert credentials['type'] == 'certificate' and 'expiresBy' in credentials
assert credentials['credentialsObject']['type'] == 'personal-certificate'
assert set(credentials['credentialsObject']) == {'type', 'certificatesecret', 'password'}
for key in ['certificatesecret', 'password']:
    assert credentials['credentialsObject'][key].startswith('<')
uuid.UUID(credential_response['data']['id'])
assert set(credential_response['data']['attributes']) == {'label', 'providerId'}
assert 'expiresBy' not in credential_response['data']['attributes']
assert encryption_request['data']['type'] == encryption_response['data']['type'] == 'encrypted-certificate'
assert set(encryption_request['data']['attributes']) == {'secret'}
assert set(encryption_response['data']['attributes']) == {'encryptedSecret'}
source_extract = (ROOT / 'context/Tax API/Certificates/connections-service-certificate-guide-extract.md').read_text()
for field in ['credentials.expiresBy', 'credentials.credentialsObject.certificatesecret',
              'credentials.credentialsObject.password', 'data.attributes.encryptedSecret']:
    assert field in source_extract
assert 'certificate.credentialsObject' in body and 'source' in body
assert 'Connection-Id: &lt;credential-connection-id&gt;' in markup
assert '/datasets/{dataset_id}/connections' in body
assert '/datasets/{dataset_id}/compliance/es-anti-fraud-legislation/encryptions' in body
assert all(name in body for name in ['Sage 50', 'Sage 200', 'Sage Active', 'Sage X3', 'Despachos'])
assert 'SXS' in body and 'Product precondition' in body

companion_source = ROOT / 'specs/onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md'
companion_text = companion_source.read_text()
companion_meta = yaml.safe_load(companion_text.split('---', 2)[1])
assert meta['id'] in companion_meta['related']
known_gaps = set(re.findall(r'^\| (GAP-\d{2}) \|', companion_text, re.M))

def gap_ids(value):
    result = set()
    for first, suffix in re.findall(r'GAP-(\d{2})((?:/\d{2})*)', value):
        result.update('GAP-' + number for number in [first] + suffix.split('/')[1:])
    return result

api_alignment = []
for index in range(1, 6):
    api_id = f'API-{index:02}'
    anchor = f'api-{index:02}'
    row = next(line for line in companion_text.splitlines()
               if line.startswith(f'| [{api_id} '))
    assert f'#{anchor})' in row and f'FR-{index:02}' in row
    section = body.split(f'<a id="{anchor}"></a>', 1)[1]
    section = section.split('<a id=', 1)[0].split('\n## 2 ', 1)[0]
    assert f'FR-{index:02}' in section
    # INT-AP01/06 are guide IDs, not additional gap references.
    assert gap_ids(row) == gap_ids(section), (api_id, gap_ids(row), gap_ids(section))
    assert gap_ids(section) <= known_gaps
    api_alignment.append({'api': api_id, 'gaps': sorted(gap_ids(row))})
for source_id, page_id in [('INT-CERT01', '467063094'), ('INT-CERT02', '759615024')]:
    for content in [body, companion_text]:
        row = next(line for line in content.splitlines() if line.startswith(f'| {source_id} |'))
        assert page_id in row
assert all(name in companion_text for name in ['Sage 200', 'B2B Router', 'Despachos', 'ZeroComa'])
assert 'Private A to Private B stays disabled' in body and 'Private A to Private B stays disabled' in companion_text

links = 0
for path in [DOC, ROOT / 'specs/onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md', ROOT / 'specs/onboarding-and-connectivity/README.md']:
    width = None
    for line in path.read_text().splitlines():
        assert line == line.rstrip()
        if line.startswith('|'):
            count = len(line.split('|'))
            assert width is None or width == count, (path, line)
            width = count
        else:
            width = None
    for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)\)', path.read_text()):
        target = target.strip('<>')
        if '://' in target:
            continue
        relative, _, anchor = target.partition('#')
        destination = (path.parent / relative).resolve() if relative else path
        assert destination.exists(), target
        if anchor and destination.suffix == '.md':
            value = destination.read_text()
            value = value.split('---', 2)[2] if value.startswith('---\n') else value
            assert f'id="{anchor}"' in markdown.markdown(value, extensions=['tables', 'toc', 'fenced_code']), target
        links += 1

assert 'CERT-04/05' in body and 'SPEC001 G1/G9/G10' in body
assert all(word in body for word in ['READY', 'EXPIRING', 'ACTION_REQUIRED',
                                     'BLOCKED', 'UNDETERMINED', 'NOT_REQUIRED'])
assert 'existing connect contract has no certificate field' in body
OUT.mkdir(exist_ok=True)
companion = next((ROOT / 'work/onboarding-concise-review').glob('SPEC-SEI-039-*.html'), companion_source)
def rewrite(match):
    attr, target = match.groups()
    if '://' in target or target.startswith('#'):
        return match[0]
    relative, sep, anchor = html.unescape(target).partition('#')
    destination = (DOC.parent / relative).resolve()
    if destination.name.startswith('SPEC-SEI-039-'):
        destination = companion
    return f'{attr}="{html.escape(str(destination) + (sep + anchor if sep else ""), quote=True)}"'

markup = re.sub(r'(href|src)="([^"]+)"', rewrite, markup)
markup = markup.replace('<table>', '<div class="scroll"><table>').replace('</table>', '</table></div>')
style = '*{box-sizing:border-box}body{font:16px/1.55 Arial;color:#333;margin:30px auto;padding:0 24px;max-width:1100px}h1{font-size:28px}h2{margin-top:36px}h3{margin-top:30px}.scroll{overflow:auto}table{border-collapse:collapse;min-width:650px;width:100%;font-size:14px}td,th{padding:10px;border:1px solid #ccc;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#f5f5f5}pre{font-size:14px;line-height:1.45}pre code{color:inherit}code{font-size:.9em;overflow-wrap:anywhere}a{color:#075eaa}'
preview = OUT / 'SPEC-SEI-040.html'
preview.write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>040 request-response comparison</title><style>{style}</style><body>{markup}</body></html>')
for parent in [ROOT / 'work/onboarding-concise-review', ROOT / 'work/onboarding-clarity-review', ROOT / 'work/onboarding-and-connectivity-review']:
    for page in parent.glob('SPEC-SEI-039*.html'):
        page.write_text(page.read_text().replace(str(DOC), str(preview)))
report = {'result': 'passed', 'e_invoice_response_extracts': 5, 'e_invoice_request_body_examples': 2,
          'credential_and_internal_encryption_examples': 4,
          'grey_source_field_checks': checked, 'blue_values_are_proposals': True,
          'certificate_management': 'documented ES AFL fields; B2B binding and validation response unconfirmed',
          'SXS_Tax_precondition_and_product_list': True,
          'private_provider_candidates': [entry['attributes']['name'] for entry in catalogue],
          'worked_cases': ['Sage 200 / B2B Router', 'Despachos / ZeroComa', 'Sage 50 / public platform'],
          'sample_ids_are_synthetic': True,
          'multiple_connections_example': len(saved),
          '039_040_api_and_gap_alignment': api_alignment,
          'certificate_source_ids_aligned': True,
          'local_links_and_anchors': links, 'diagrams': 0, 'published': False}
(OUT / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
