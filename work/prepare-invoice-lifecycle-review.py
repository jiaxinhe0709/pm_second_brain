"""Validate the lifecycle draft set and generate an offline HTML review. No publish calls."""
from pathlib import Path
from collections import Counter
import hashlib
import html
import json
import os
import re
import struct
import xml.etree.ElementTree as ET

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'specs/invoice-lifecycle'
OUT = ROOT / 'work/invoice-lifecycle-review'
STYLE = '''
*{box-sizing:border-box}body{margin:0;color:#263238;background:#fff;font:16px/1.55 Arial,sans-serif}
header{padding:18px 26px;background:#f5f7f8;border-bottom:1px solid #cdd3d8}nav{display:flex;gap:24px;flex-wrap:wrap}a{color:#075eaa}
.layout{display:grid;grid-template-columns:220px minmax(0,1120px);gap:30px;max-width:1440px;margin:24px auto;padding:0 24px}
main{min-width:0}.outline{position:sticky;top:12px;align-self:start;max-height:92vh;overflow:auto;font-size:13px}.outline ul{padding-left:18px}
h1{font-size:30px}h2{margin-top:36px}h3{margin-top:30px}table{border-collapse:collapse;width:100%;margin:18px 0;font-size:14px}
th,td{border:1px solid #cdd3d8;vertical-align:top;text-align:left;padding:10px;overflow-wrap:anywhere}th{background:#f3f5f7}
code{font-size:.9em;background:#f1f3f5;overflow-wrap:anywhere}.diagram{width:100%;max-height:720px;overflow:auto;border:1px solid #b8c0c8;margin:18px 0}
.diagram img{display:block;max-width:none}p{max-width:1060px}
@media(max-width:800px){.layout{display:block}.outline{position:static;max-height:200px;margin-bottom:24px}}
'''


def rendered_markdown(path):
    text = path.read_text()
    body = text.split('---', 2)[2] if text.startswith('---\n') else text
    md = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code'])
    return md, md.convert(body)


def validate_links(path):
    for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)\)', path.read_text()):
        target = target.strip('<>')
        if '://' in target:
            continue
        relative, _, anchor = target.partition('#')
        dest = (path.parent / relative).resolve() if relative else path
        assert dest.exists(), (path, target)
        if anchor and dest.suffix == '.md':
            _, markup = rendered_markdown(dest)
            assert f'id="{anchor}"' in markup, (path, target, 'missing anchor')


def compare_annex():
    import pymupdf
    annex = ROOT / 'context/Anexo II/A2-Proyecto-OM-FE 21-10-26.pdf'
    pdf = pymupdf.open(annex)
    ledger = json.loads((ROOT / 'assets/regulatory/spain/spfe/field-traceability.json').read_text())
    rows = [row for row in ledger['rows'] if row['annex'] == 'II']
    cards = re.findall(r'\b[01]\.\.1\b', ''.join(pdf[i].get_text() for i in range(3, len(pdf))))
    assert len(rows) == 52 and cards == [row['cardinality'] for row in rows]
    pages = {'PAYMENT': (4, 6), 'CANCELPAYMENT': (6, 6), 'REJECTION': (7, 7),
             'CANCELREJECTION': (8, 8), 'SETTLEMENT': (9, 10), 'CANCELSETTLEMENT': (11, 11),
             'DEFAULT': (12, 13), 'CANCELDEFAULT': (14, 14)}
    def normalise(text):
        return re.sub(r'\s+', '', text).replace('7.ª', '7ª')
    checked = []
    for row in rows:
        start, end = pages[row['message']]
        source = normalise(''.join(pdf[i].get_text() for i in range(start-1, end)))
        for field in ['source_name', 'source_description', 'source_ubl_path', 'semantic_type']:
            assert normalise(row[field]) in source, (row['trace_id'], field)
        checked.append({'trace_id': row['trace_id'], 'source_pages': [start, end],
                        'cardinality': row['cardinality'], 'result': 'source text matched'})
    codes = re.findall(r'ResponseCode:\s*([A-Z]+)', ''.join(pdf[i].get_text() for i in range(3, len(pdf))))
    assert codes == list(pages)
    result = {'source': 'SPFE-S22', 'sha256': hashlib.sha256(annex.read_bytes()).hexdigest(),
              'baseline': 'SPFE-S02 AXII rows in original field ledger', 'codes': codes,
              'field_group_count': len(rows), 'checks': ['52 ordered cardinalities',
              'field names, descriptions, literal paths and semantic type in message page ranges'],
              'normalisation': 'PDF wrapping/whitespace and ordinal 7.ª / 7ª only',
              'limits': 'Page-range text matching plus recorded visual review; not byte/schema/implementation equivalence.',
              'rows': checked, 'implementation_tests_executed': False}
    (OUT / 'annex-comparison.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    OUT.mkdir(exist_ok=True)
    docs = sorted(SOURCE.glob('SPEC-*.md'))
    assert len(docs) == 3
    repo_ids = Counter()
    for path in (ROOT / 'specs').rglob('*.md'):
        match = re.search(r'^id: (SPEC-\S+)$', path.read_text(), re.M)
        if match:
            repo_ids[match[1]] += 1
    cards = []
    for path in docs:
        metadata = yaml.safe_load(path.read_text().split('---', 2)[1])
        ident = metadata['id']
        assert repo_ids[ident] == 1
        for field in ['id','title','type','status','owner','created','updated','product','related','confluence']:
            assert field in metadata, (path, field)
        assert metadata['status'] == 'draft' and metadata['confluence']['publish'] is False
        assert not metadata['confluence']['page_id'] and 'SPEC-SEI-009' in metadata['related']
        assert '## Revision overview' in path.read_text() and '## REF Source references' in path.read_text()
        assert not re.search(r'^#+ .*?(change log|revision history)', path.read_text(), re.I | re.M)
        width = None
        for line in path.read_text().splitlines():
            assert line == line.rstrip(), (path, 'trailing whitespace')
            if line.startswith('|'):
                count = len(re.split(r'(?<!\\)\|', line))
                assert width is None or count == width, (path, 'table width', line)
                width = count
            else:
                width = None
        md, markup = rendered_markdown(path)
        def resolve(match):
            attr, target = match[1], html.unescape(match[2])
            if '://' in target or target.startswith('#'):
                return match[0]
            relative, _, anchor = target.partition('#')
            dest = (path.parent / relative).resolve()
            if dest in docs:
                result = dest.name[:12] + '.html'
            else:
                result = os.path.relpath(dest, OUT)
            if anchor:
                result += '#' + anchor
            return attr + '="' + html.escape(result, quote=True) + '"'
        markup = re.sub(r'(href|src)="([^"]+)"', resolve, markup)
        markup = re.sub(r'<img ([^>]*src="[^"]+\.svg"[^>]*)\s*/?>', r'<div class="diagram"><img \1></div>', markup)
        page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            + '<title>' + html.escape(metadata['title']) + '</title><style>' + STYLE + '</style></head><body>'
            + '<header><p>Invoice lifecycle · Unpublished draft · Local review</p><nav><a href="index.html">All lifecycle views</a>'
            + '<a href="../../specs/archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md">Retained SPEC-SEI-009</a></nav></header>'
            + '<div class="layout"><aside class="outline">' + md.toc + '</aside><main>' + markup + '</main></div></body></html>')
        (OUT / (ident + '.html')).write_text(page)
        cards.append(f'<li><a href="{ident}.html">{html.escape(metadata["title"])}</a></li>')
    (OUT / 'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        + '<title>Invoice lifecycle review</title><style>' + STYLE + '</style></head><body><header><h1>Invoice lifecycle</h1>'
        + '<p>Three unpublished draft views. SPEC-SEI-009 is retained in the archive; publication settings are unchanged.</p></header><main style="padding:24px;max-width:1100px">'
        + '<ol>' + ''.join(cards) + '</ol><p>Document checks do not prove implementation readiness. Each engineering gap retains its owner and evidence gate.</p></main></body></html>')
    files = docs + [SOURCE / 'README.md', ROOT / 'README.md', ROOT / 'context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md', ROOT / 'context/Anexo II/annex-ii-review.md']
    for path in files:
        validate_links(path)
    diagrams = sorted((ROOT / 'assets/diagrams').glob('invoice-lifecycle-*-sequence.svg'))
    assert len(diagrams) == 3
    for path in diagrams:
        svg = ET.parse(path).getroot()
        assert svg.get('role') == 'img' and svg.get('aria-label')
        ET.parse(path.with_suffix('.drawio'))
        data = path.with_suffix('.png').read_bytes()
        assert struct.unpack('>II', data[16:24]) == (int(svg.get('width')), int(svg.get('height')))
        if path.name.endswith('-sequence.svg'):
            assert 'stroke-dasharray' in path.read_text()
    initial_hashes = json.loads((OUT / 'source-hashes.json').read_text())
    # Preserve the original source-hash receipt. This move changed links only.
    archived_baseline = 'specs/archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md'
    for name, digest in initial_hashes.items():
        if name == 'specs/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md':
            assert digest == '296a77e85ef437be8b6555812b130a2c7591e9b8a21b068d882db7ffb8833c8e', 'Unexpected original baseline'
            name, digest = archived_baseline, 'ab9dd6b7878c57ed117cba7d6f2390f042165f5af771e667ad15c9e12c092929'
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, (name, 'source changed')
    source_hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in ['specs/archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md','config/confluence.yml']}
    comparison = compare_annex()
    report = {'mode':'local-review-only','documents':[p.name for p in docs], 'checks': ['metadata and unique IDs','unpublished drafts','revision and source references','local links and anchors','table structure','SVG/Draw.io XML and PNG dimensions', 'source/config/field-ledger unchanged since task snapshot', 'Annex II 52-field source comparison'], 'source_hashes':source_hashes, 'annex_field_group_count':comparison['field_group_count'], 'implementation_tests_executed':False}
    (OUT / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
