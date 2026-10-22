"""Validate and prepare local onboarding pages and Confluence storage previews.

This performs no network calls and does not enable publication or change sources.
Run with .venv/bin/python work/prepare-onboarding-api-review.py.
"""
from pathlib import Path
from collections import Counter
import hashlib
import html
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher

OUT = ROOT / 'work/onboarding-api-review'
SPECS = ROOT / 'specs/onboarding'
DOCS = [
    ('SPEC-SEI-018', 'SPEC-SEI-018-customer-onboarding-solution-summary.md', 'Solution Summary'),
    ('SPEC-SEI-019', 'SPEC-SEI-019-customer-onboarding-logical-feature-specification.md', 'Logical Feature Specification'),
    ('SPEC-SEI-020', 'SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md', 'API Reuse Assessment'),
]
TITLES = {name: 'Onboarding ' + title for _, name, title in DOCS}
EXPECTED_FR = {
    'get-accesspoints.md': ('abd8cc2b4430ebca7ccbbf957acce8a8c26eb3d86f61e15b0f3fc00a1bb75e5f', 'GET', '/accesspoints'),
    'get-dataset-accesspoints.md': ('e0c2849a0d30b06945be4943232f20415f077db3c21c110fa62fd70d6632448f', 'GET', '/datasets/{datasetId}/accesspoints'),
    'new-accesspoint-connection.md': ('aa4c3db90b2878977705bb1a6877bb91a6a911f26f8fb0c0d1116a8f9a116194', 'POST', '/connectors/{accessPointId}/datasets/{datasetId}/connect'),
    'get-accesspoint-connection.md': ('0616501ddc3046fbe4facd2186466029bb9249a87b63424c7249ff9ee990808c', 'GET', '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/'),
    'put-accesspoint-connection.md': ('bf0fc7a8fcbdf236905b4ff7116be60df8c0305ac62ee32fa80eb2efa588d92f', 'PUT', '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/'),
}
STYLE = '''
*{box-sizing:border-box}body{margin:0;color:#263238;background:#fff;font:16px/1.55 Arial,sans-serif}
header{padding:20px 30px;border-bottom:1px solid #d8dde2;background:#f7f8f9}header p{margin:6px 0}
a{color:#075eaa}nav{display:flex;gap:22px;flex-wrap:wrap}main{max-width:1160px;margin:28px auto;padding:0 24px}
.layout{display:grid;grid-template-columns:260px minmax(0,1160px);gap:28px;max-width:1500px;margin:24px auto;padding:0 24px}
.layout main{margin:0;padding:0;min-width:0}.outline{position:sticky;top:12px;align-self:start;max-height:92vh;overflow:auto;font-size:13px}
.outline ul{padding-left:17px}.outline>div>ul{padding-left:0;list-style:none}h1{font-size:30px}h2{margin-top:36px}h3{margin-top:28px}
table{border-collapse:collapse;width:100%;font-size:14px;margin:16px 0}th,td{border:1px solid #d8dde2;padding:10px;vertical-align:top;text-align:left;overflow-wrap:anywhere}th{background:#f3f5f7}
th:first-child,td:first-child{min-width:90px}code{background:#f1f3f5;padding:2px 3px;overflow-wrap:anywhere;font-size:.9em}p{max-width:1020px}
.diagram{width:100%;height:640px;overflow:auto;border:1px solid #b8c0c8;margin:16px 0;background:white}.diagram img{display:block;max-width:none}
.meta{font-size:13px;color:#4e5963}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.card{padding:20px;border:1px solid #d8dde2;border-radius:6px}
@media(max-width:800px){.layout{display:block}.outline{position:static;max-height:260px;margin-bottom:24px}.cards{grid-template-columns:1fr}main{padding:0 16px}}
'''


def nav():
    return '<nav><a href="index.html">Feature landing</a>' + ''.join(
        f'<a href="{ident}.html">{title}</a>' for ident, _, title in DOCS) + '</nav>'


def shell(title, content):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title><style>{STYLE}</style></head><body>'
            '<header><p class="meta">Local Confluence presentation preview · Unpublished drafts · Live pages unchanged</p>'
            + nav() + '</header>' + content + '</body></html>')


def page_link(match):
    target, label = html.unescape(match[1]), match[2]
    name = target.split('#')[0].split('/')[-1]
    if name not in TITLES:
        return match[0]
    # Native title-based links can resolve after child-page creation. Section
    # navigation uses the destination's native table of contents.
    plain = html.unescape(re.sub('<[^>]+>', '', label))
    assert ']]>' not in plain
    return ('<ac:link><ri:page ri:space-key="DNBU" ri:content-title="'
            + html.escape(TITLES[name], quote=True)
            + '"/><ac:plain-text-link-body><![CDATA[' + plain
            + ']]></ac:plain-text-link-body></ac:link>')


def prepare():
    OUT.mkdir(exist_ok=True)
    plan = {'mode': 'local-preview-only', 'parent_page_id': '837610648',
            'current_source_unchanged': {'923861390': 'SPEC-SEI-002'},
            'publication_preconditions': ['Repository review and merge',
                'Approved live publication scope', 'Reconcile existing child titles and IDs',
                'Resolve native companion links and update selected sources atomically'],
            'pages': []}
    for ident, name, title in DOCS:
        plan['pages'].append({'source_id': ident, 'source': str((SPECS / name).relative_to(ROOT)),
            'title': TITLES[name], 'target_page_id': '923861390' if ident == 'SPEC-SEI-018' else '',
            'action': 'reuse-existing-page' if ident == 'SPEC-SEI-018' else 'create-sibling-after-title-check',
            'parent_page_id': '837610648', 'publish_enabled': False})
    (OUT / 'publication-plan.json').write_text(json.dumps(plan, indent=2) + '\n')

    snapshots = []
    for name, (digest, method, route) in EXPECTED_FR.items():
        p = ROOT / 'context/FR API/Onboarding' / name
        assert hashlib.sha256(p.read_bytes()).hexdigest() == digest, p
        doc = json.loads(re.search(r'```json\s*(.*?)\s*```', p.read_text(), re.S)[1])
        op = doc['paths'][route][method.lower()]
        snapshots.append({'file': str(p.relative_to(ROOT)), 'sha256': digest,
            'info_version': doc['info']['version'], 'reviewed': '2026-10-21',
            'method': method, 'path': route, 'operation_id': op['operationId'],
            'response_codes': list(op['responses']),
            'reuse_direction': 'reuse-fr-api-with-spain-country-pack',
            'implementation_qualification': 'unknown'})
    (OUT / 'source-snapshots.json').write_text(json.dumps(snapshots, indent=2) + '\n')

    preview_files = {name: ident + '.html' for ident, name, _ in DOCS}
    for ident, name, title in DOCS:
        p = SPECS / name
        metadata, body = publisher.load_document(p)
        assert metadata['id'] == ident and metadata['status'] == 'draft'
        assert metadata['confluence']['publish'] is False
        assert metadata['confluence']['page_id'] == ''
        assets = publisher.drawio_assets(p, body)
        storage = publisher.storage_with_drawio(metadata, body, 'local-review', None, assets, {})
        storage = re.sub(r'<a href="([^"]+)">(.*?)</a>', page_link, storage, flags=re.S)
        if assets:
            assert '<ac:structured-macro ac:name="drawio"' in storage
        assert '<ri:page ri:space-key="DNBU"' in storage
        assert 'change-history' in storage
        (OUT / f'{ident}.proposed.storage.xml').write_text(storage)
        md = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code'])
        rendered = md.convert(body)

        def local_href(m):
            attribute, target = m[1], html.unescape(m[2])
            if '://' in target or target.startswith('#'):
                return m[0]
            relative, _, anchor = target.partition('#')
            dest = (p.parent / relative).resolve()
            if dest.parent == SPECS and dest.name in preview_files:
                target = preview_files[dest.name] + ('#' + anchor if anchor else '')
            elif dest == SPECS / 'README.md':
                target = 'index.html'
            else:
                target = dest.as_uri() + ('#' + anchor if anchor else '')
            return f'{attribute}="{html.escape(target, quote=True)}"'

        rendered = re.sub(r'(href|src)="([^"]+)"', local_href, rendered)
        rendered = re.sub(r'<img ([^>]*src="[^"]+\.svg"[^>]*)\s*/?>',
                          r'<div class="diagram"><img \1></div>', rendered)
        document = ('<div class="layout"><aside class="outline"><strong>Contents</strong>'
                    + md.toc + '</aside><main>' + rendered + '</main></div>')
        (OUT / f'{ident}.html').write_text(shell(title, document))

    cards = ''.join(f'<article class="card"><h2><a href="{ident}.html">{title}</a></h2><p>{ident}</p>'
                    + f'<p>{description}</p></article>'
                    for (ident, _, title), description in zip(DOCS, [
                        'Outcome, scope, workflow and material decisions.',
                        'Required behaviour, process diagrams and acceptance.',
                        'Existing FR coverage, Spain tailoring by platform and reuse gaps.']))
    landing = ('<main><h1>Customer onboarding</h1><p>Three sibling views under the existing onboarding feature/PRD page. '
               'Choose a view for your review.</p><div class="cards">' + cards + '</div>'
               '<h2>Planned Confluence structure</h2><ul><li>Existing onboarding feature/PRD page (837610648)<ul>'
               '<li>Solution Summary — reuse page 923861390</li><li>Logical Feature Specification — new sibling</li>'
               '<li>API Reuse Assessment — new sibling</li></ul></li></ul>'
               '<p>The original SPEC-SEI-002 file is unchanged and remains the selected live source. '
               'These local pages do not perform publication.</p><p><a href="publication-plan.json">Publication plan</a> · '
               '<a href="source-snapshots.json">FR source snapshot identities</a></p></main>')
    (OUT / 'index.html').write_text(shell('Customer onboarding review', landing))

    issues = []
    documents = [SPECS / 'README.md'] + [SPECS / name for _, name, _ in DOCS] + [ROOT / 'context/GLO-SEI-001-e-invoicing-terminology.md']
    for p in documents:
        text = p.read_text()
        for line in text.splitlines():
            assert line == line.rstrip(), (p, 'trailing whitespace')
        for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)\)', text):
            target = target.strip('<>')
            if '://' in target:
                continue
            relative, _, anchor = target.partition('#')
            dest = (p.parent / relative).resolve() if relative else p
            if not dest.exists():
                issues.append(f'{p.name}: missing {target}')
            elif anchor and dest.suffix == '.md':
                rendered = markdown.markdown(dest.read_text(), extensions=['toc', 'tables'])
                if f'id="{anchor}"' not in rendered:
                    issues.append(f'{p.name}: missing anchor {target}')
        count = None
        for line in text.splitlines() + ['']:
            if line.startswith('|'):
                width = len(re.split(r'(?<!\\)\|', line))
                if count is None:
                    count = width
                if count != width:
                    issues.append(f'{p.name}: malformed table row')
            else:
                count = None
        ids = re.findall(r'\bid="([^"]+)"', markdown.markdown(text, extensions=['toc', 'tables']))
        assert not [i for i, c in Counter(ids).items() if c > 1], (p, 'duplicate HTML anchor')
    for original, digest in [
        ('specs/SPEC-SEI-002-onboarding-solution-specification.md', '30d01d97be12d9122fee5715236ff8c6451a57bad34f6c2215a1a8b2495e4093'),
        ('config/confluence.yml', '62bc03e3ff1203d85bf30d9f3ba9f6f967737abc5c4520a08ad2fcbafb9824d5')]:
        assert hashlib.sha256((ROOT / original).read_bytes()).hexdigest() == digest, original
    api_path = SPECS / DOCS[2][1]
    assets = []
    for _, name, _ in DOCS:
        document_path = SPECS / name
        assets.extend(publisher.drawio_assets(document_path, publisher.load_document(document_path)[1]))
    for asset in assets:
        editable = ET.parse(asset.source)
        root = ET.parse(asset.source.with_suffix('.svg')).getroot()
        png = asset.preview.read_bytes()
        assert struct.unpack('>II', png[16:24]) == (int(root.get('width')), int(root.get('height')))
        assert editable.getroot().tag == 'mxfile'
    api_body = api_path.read_text()
    for item in snapshots:
        assert item['path'] in api_body and item['operation_id'] in api_body
    assert not issues, '\n'.join(issues)
    report = {'result': 'pass', 'network_calls': 0, 'live_publication': False,
              'checks': ['Local links and anchors', 'Table structure', 'Unique heading anchors',
                         'Draft/publication metadata', 'All five supplied method/path/operation IDs',
                         'FR source hashes unchanged', 'Referenced editable SVG/PNG diagram companions',
                         'Offline Confluence storage with native companion links',
                         'Original specification and publication configuration unchanged']}
    (OUT / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    prepare()
