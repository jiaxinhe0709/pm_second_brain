"""Prepare and validate the separate SPEC-SEI-021 offline review. No publication."""
from collections import Counter
from pathlib import Path
import hashlib
import html
import importlib.util
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

SOURCE = ROOT / 'specs/onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md'
OUT = ROOT / 'work/onboarding-sequence-review'
STYLE = '''
*{box-sizing:border-box}body{margin:0;background:white;color:#263238;font:16px/1.55 Arial,sans-serif}
header{padding:18px 24px;background:#f7f8f9;border-bottom:1px solid #d8dde2}nav{display:flex;gap:24px;flex-wrap:wrap}
a{color:#075eaa}.layout{display:grid;grid-template-columns:235px minmax(0,1160px);gap:28px;max-width:1480px;margin:24px auto;padding:0 24px}
main{min-width:0}.outline{position:sticky;top:12px;align-self:start;font-size:13px;max-height:92vh;overflow:auto}.outline ul{padding-left:17px}
h1{font-size:29px}h2{margin-top:36px}h3{margin-top:30px}table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px}
th,td{border:1px solid #d8dde2;text-align:left;vertical-align:top;padding:10px;overflow-wrap:anywhere}th{background:#f3f5f7}
code{background:#f1f3f5;overflow-wrap:anywhere;font-size:.9em}p{max-width:1080px}
.diagram{width:100%;height:640px;overflow:auto;border:1px solid #b8c0c8;margin:16px 0}.diagram img{display:block;max-width:none}
@media(max-width:800px){.layout{display:block}.outline{position:static;max-height:230px;margin-bottom:24px}}
'''


def validate_links(path):
    errors = []
    text = path.read_text()
    for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)\)', text):
        target = target.strip('<>')
        if '://' in target:
            continue
        relative, _, anchor = target.partition('#')
        dest = (path.parent / relative).resolve() if relative else path
        if not dest.exists():
            errors.append(f'{path.name}: missing {target}')
        elif anchor and dest.suffix == '.md':
            rendered = markdown.markdown(dest.read_text(), extensions=['toc','tables'])
            if f'id="{anchor}"' not in rendered:
                errors.append(f'{path.name}: missing anchor {target}')
    assert not errors, '\n'.join(errors)


def prepare():
    OUT.mkdir(exist_ok=True)
    metadata, body = publisher.load_document(SOURCE)
    assert metadata['id'] == 'SPEC-SEI-021' and metadata['status'] == 'draft'
    assert 'SPEC-SEI-020' in metadata['related']
    assert metadata['confluence']['publish'] is False and not metadata['confluence']['page_id']
    publisher.validate_no_manual_history(body, SOURCE)
    md = markdown.Markdown(extensions=['tables','toc','fenced_code'])
    rendered = md.convert(body)

    def local_link(match):
        attr, target = match[1], html.unescape(match[2])
        if '://' in target or target.startswith('#'):
            return match[0]
        relative, _, anchor = target.partition('#')
        dest = (SOURCE.parent / relative).resolve()
        if dest.name.startswith(('SPEC-SEI-018-', 'SPEC-SEI-019-', 'SPEC-SEI-020-')):
            target = '../onboarding-api-review/' + dest.name[:12] + '.html'
        else:
            target = dest.as_uri()
        if anchor:
            target += '#' + anchor
        return attr + '="' + html.escape(target, quote=True) + '"'

    rendered = re.sub(r'(href|src)="([^"]+)"', local_link, rendered)
    rendered = re.sub(r'<img ([^>]*src="[^"]+\.svg"[^>]*)\s*/?>',
                      r'<div class="diagram"><img \1></div>', rendered)
    page = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>SPEC-SEI-021 — Onboarding sequence review</title><style>' + STYLE + '</style></head><body>'
            '<header><p>Local review · Main engineering view · SPEC020 retained in the archive</p>'
            '<nav><a href="../onboarding-api-review/SPEC-SEI-020.html">Archived SPEC020 reference</a>'
            '<a href="../onboarding-api-review/index.html">Existing onboarding views</a></nav></header>'
            '<div class="layout"><aside class="outline"><strong>Contents</strong>' + md.toc
            + '</aside><main>' + rendered + '</main></div></body></html>')
    (OUT / 'SPEC-SEI-021.html').write_text(page)
    assets = publisher.drawio_assets(SOURCE, body)
    assert len(assets) == 5
    storage = publisher.storage_with_drawio(metadata, body, 'local-review', None, assets, {})
    assert storage.count('ac:name="drawio"') == 5 and 'change-history' in storage
    (OUT / 'SPEC-SEI-021.proposed.storage.xml').write_text(storage)

    for path in (SOURCE, ROOT / 'specs/onboarding/README.md'):
        validate_links(path)
        width = None
        for line in path.read_text().splitlines() + ['']:
            assert line == line.rstrip(), (path, 'trailing whitespace')
            if line.startswith('|'):
                count = len(re.split(r'(?<!\\)\|', line))
                width = count if width is None else width
                assert count == width, (path, line)
            else:
                width = None
    ids = re.findall(r'\bid="([^"]+)"', rendered)
    assert not [key for key, count in Counter(ids).items() if count > 1]
    for i in range(1,9):
        assert f'ONB-S{i:02}' in body and f'GAP-{i:02}' in body
    acceptance = body.split('## 5 Acceptance coverage')[1].split('## REF')[0]
    present = set()
    for group in re.findall(r'\| (API-A[\d/]+) \|', acceptance):
        present.update(int(n) for n in group.replace('API-A','').split('/'))
    assert present == set(range(1,17)), present

    views = json.loads((OUT / 'sequences.json').read_text())['views']
    source_digests = json.loads((ROOT / 'work/onboarding-api-review/source-snapshots.json').read_text())
    for item in source_digests:
        assert hashlib.sha256((ROOT / item['file']).read_bytes()).hexdigest() == item['sha256']
    archive_spec = importlib.util.spec_from_file_location('onboarding_archive', ROOT / 'work/onboarding-archive-validation.py')
    archive_module = importlib.util.module_from_spec(archive_spec)
    archive_spec.loader.exec_module(archive_module)
    archive_validation = archive_module.validate_archive()
    for view in views:
        assert view['request_response_pairs'] == view['activation_bars']
        assert f'id="{view["anchor"]}"' in rendered
        for target in view['references']:
            assert f'id="{target}"' in rendered
        editable = ET.parse(ROOT / view['drawio'])
        cells = editable.findall('.//mxCell')
        values = [c.get('value','') for c in cells]
        labels = [''.join(value.splitlines()) for value in values]
        for op in view['operations']:
            assert op['method'] + ' ' + op['path'] in labels
            assert any(value.startswith(op['code'] + ' ') for value in values)
            assert op['operation_id'] in body
        for effect in view['conditional_effects']:
            assert any(gate < effect['y'] for gate in view['pre_dispatch_gates'])
        svg = ET.parse(ROOT / view['svg']).getroot()
        png = (ROOT / view['png']).read_bytes()
        assert struct.unpack('>II', png[16:24]) == (int(svg.get('width')), int(svg.get('height')))
        assert editable.getroot().tag == 'mxfile'
        assert any(obj.get('link','').startswith('../../specs/onboarding/SPEC-SEI-021-') for obj in editable.findall('.//object'))
    config = yaml.safe_load((ROOT / 'config/confluence.yml').read_text())
    assert config['publication']['current_sources']['923861390'] == 'SPEC-SEI-002'
    predecessor = ROOT / archive_validation['archive_location']
    pre_body = publisher.load_document(predecessor)[1]
    main_words = len(body.partition('## REF Source references')[0].split())
    total_words, old_words = len(body.split()), len(pre_body.split())
    assert 1500 <= main_words <= 2000
    report = {
        'result':'pass', 'source_id':'SPEC-SEI-021', 'live_publication':False,
        'main_reading_words':main_words, 'total_body_words':total_words,
        'predecessor_body_words':old_words,
        'archived_020_analysis_unchanged':True, 'business_rules_and_acceptance_018_019_unchanged':True,
        'publication_configuration_unchanged':True, 'stable_page_source':'SPEC-SEI-002',
        'archive_validation':archive_validation,
        'checks':['Metadata and unique successor ID', 'Local links, anchors and tables',
                  'All eight scenario and gap IDs; all sixteen acceptance IDs',
                  'Five editable Draw.io macros and SVG/PNG companions',
                  'Documented method/path/success responses and operation IDs',
                  'Shared-reference targets and pre-dispatch mutation gates',
                  'Source contract hashes unchanged', 'Authorised archive retained analysis and business rules'],
    }
    (OUT / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    prepare()
