"""Validate and render the three onboarding and connectivity successor views; no publication calls."""

from collections import Counter
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET

import markdown
import yaml
from archive_reference_preservation import assert_preserved

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'specs/onboarding-and-connectivity'
OUT = ROOT / 'work/onboarding-and-connectivity-review'
EXPECTED = {'SPEC-SEI-037', 'SPEC-SEI-038', 'SPEC-SEI-039'}
PRESERVED = json.loads((OUT / 'source-preservation.json').read_text())
REUSED_ASSETS = {
    str(asset.relative_to(ROOT)): PRESERVED[str(asset.relative_to(ROOT))]
    for doc in SOURCE.glob('SPEC-*.md')
    for target in re.findall(r'^!\[[^\]]*\]\(([^)]+\.svg)\)', doc.read_text(), re.M)
    for suffix in ['.svg', '.drawio', '.png']
    for asset in [(doc.parent / target).resolve().with_suffix(suffix)]
}

STYLE = '\n*{box-sizing:border-box}body{margin:0;color:#243445;background:#fff;font:16px/1.55 Arial,sans-serif}\nheader{padding:18px 24px;background:#f3f6f8;border-bottom:1px solid #ccd4dc}nav{display:flex;flex-wrap:wrap;gap:20px}\na{color:#075eaa}main{max-width:1200px;margin:28px auto;padding:0 24px}h1{font-size:30px}h2{margin-top:36px}\n.table-scroll{overflow:auto;margin:18px 0}table{border-collapse:collapse;width:100%;min-width:650px;font-size:14px}\nth,td{border:1px solid #ccd4dc;vertical-align:top;text-align:left;padding:10px;overflow-wrap:anywhere}th{background:#f3f6f8}\ncode{font-size:.9em;background:#f3f6f8;overflow-wrap:anywhere}img{display:block;width:100%;height:auto;margin:20px 0}\n.notice{padding:12px;background:#fff5da;border-left:4px solid #ad7000}.toc{font-size:14px}.toc ul{padding-left:22px}\n\n.diagram{overflow-x:auto}.diagram img{min-width:1050px}\n'


STYLE += '\n.diagram{overflow:auto;max-height:720px}.diagram img{display:block;max-width:none;width:auto;min-width:0;height:auto}\n'


def render(path):
    source = path.read_text()
    body = source.split('---', 2)[2] if source.startswith('---\n') else source
    md = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code'])
    return md, md.convert(body)


def validate_links(path):
    count = 0
    for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)\)', path.read_text()):
        target = target.strip('<>')
        if '://' in target:
            continue
        relative, _, anchor = target.partition('#')
        destination = (path.parent / relative).resolve() if relative else path
        assert destination.exists(), (path.name, target)
        if anchor and destination.suffix == '.md':
            _, markup = render(destination)
            assert f'id="{anchor}"' in markup, (path.name, target, 'missing anchor')
        count += 1
    return count


def diagram_check(path):
    svg = ET.parse(path).getroot()
    assert svg.get('role') == 'img'
    width, height = float(svg.get('width')), float(svg.get('height'))
    assert not list(svg.iter('{http://www.w3.org/2000/svg}script'))
    native = ET.parse(path.with_suffix('.drawio')).getroot()
    assert native.find('.//mxGraphModel/root') is not None
    with path.with_suffix('.png').open('rb') as png:
        header = png.read(24)
    assert header[:8] == b'\x89PNG\r\n\x1a\n'
    png_width, png_height = struct.unpack('>II', header[16:24])
    assert png_width > 0 and png_height > 0
    return {'asset': path.name, 'width': int(width), 'height': int(height),
            'reused_unchanged': True, 'editable_source': True}


class Diagnostics(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag != 'script', 'Review preview must be static'
        if tag == 'img':
            assert attrs.get('alt') and attrs.get('src')
            self.images += 1


def main():
    OUT.mkdir(exist_ok=True)
    docs = sorted(SOURCE.glob('SPEC-*.md'))
    assert len(docs) == 3
    ids = Counter()
    for path in (ROOT / 'specs').rglob('*.md'):
        match = re.search(r'^id: (SPEC-\S+)$', path.read_text(), re.M)
        if match:
            ids[match[1]] += 1
    assert all(count == 1 for count in ids.values())
    for relative, expected in (PRESERVED | REUSED_ASSETS).items():
        assert_preserved(relative, expected)
    config = yaml.safe_load((ROOT / 'config/confluence.yml').read_text())
    assert config['publication']['current_sources']['923861399'] == 'SPEC-SEI-011'
    assert config['publication']['current_sources']['923861402'] == 'SPEC-SEI-013'
    pages = {}
    for path in docs:
        meta = yaml.safe_load(path.read_text().split('---', 2)[1])
        for field in ['id','title','type','status','owner','product','created','updated','reviewers','related','confluence']:
            assert field in meta, (path.name, field)
        assert meta['id'] in EXPECTED and meta['status'] == 'draft'
        target_ids = {'SPEC-SEI-037': '923861390', 'SPEC-SEI-038': '936509725', 'SPEC-SEI-039': '936509735'}
        assert meta['confluence']['publish'] is True
        assert meta['confluence']['page_id'] == target_ids[meta['id']]
        assert config['publication']['current_sources'][target_ids[meta['id']]] == meta['id']
        assert all('SPEC-SEI-'+n in meta['related'] for n in ['011','013','017'])
        assert '## Revision overview' in path.read_text() and '## REF Source references' in path.read_text()
        opening = path.read_text().split('## Revision overview', 1)[0]
        for label in ['Public platform (SPFE)', 'Customer connects an external private provider', 'Sage as a private platform', 'Shared controls and expansion']:
            assert label in opening, (path.name, 'missing top summary', label)
        assert all('SPEC-SEI-'+n in meta['related'] for n in ['018','019','021','034','035','036'])
        pages[path] = (meta['id']+'.html', meta['title'])
    assert {name.removesuffix('.html') for name,_ in pages.values()} == EXPECTED
    pages[SOURCE/'README.md'] = ('index.html', 'Customer onboarding and connectivity review')
    nav = ' · '.join(f'<a href="{name}">{html.escape(title)}</a>' for name,title in pages.values())
    reports=[]
    for path,(name,title) in pages.items():
        width = None
        for line in path.read_text().splitlines():
            assert line == line.rstrip(), (path.name, 'trailing whitespace')
            if line.startswith('|'):
                size=len(re.split(r'(?<!\\)\|',line))
                assert width is None or size == width, (path.name, 'table width')
                width=size
            else:
                width=None
        md,markup=render(path)

        def rewrite(match):
            attr,target=match.groups()
            if '://' in target or target.startswith('#'):
                return match.group(0)
            relative,separator,anchor=html.unescape(target).partition('#')
            destination=(path.parent/relative).resolve()
            rewritten=pages[destination][0] if destination in pages else os.path.relpath(destination,OUT)
            if separator:
                rewritten+='#'+anchor
            return f'{attr}="{html.escape(rewritten,quote=True)}"'

        markup=re.sub(r'(href|src)="([^"]+)"',rewrite,markup)
        markup=markup.replace('<table>','<div class="table-scroll"><table>').replace('</table>','</table></div>')
        markup=re.sub(r'<p>(<img [^>]+>)</p>',r'<div class="diagram">\1</div>',markup)
        document=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                  '<meta name="viewport" content="width=device-width,initial-scale=1">'
                  f'<title>{html.escape(title)}</title><style>{STYLE}</style></head><body>'
                  f'<header><nav>{nav}</nav></header><main><p class="notice">Draft design; publication authorised for the existing three onboarding pages. '
                  'Predecessor folders are archived references. Business content, IDs, lifecycle '
                  'and publication selections are preserved; relative links and reading routes changed.</p>'
                  f'{md.toc}{markup}</main></body></html>')
        diagnostics=Diagnostics()
        diagnostics.feed(document)
        (OUT/name).write_text(document)
        count=validate_links(path)
        reports.append({'source':str(path.relative_to(ROOT)), 'preview':name, 'local_links':count, 'diagrams':diagnostics.images})
    assert sum(r['diagrams'] for r in reports)==11
    reused = {
        (path.parent / target).resolve()
        for path in docs
        for target in re.findall(r'^!\[[^\]]*\]\(([^)]+\.svg)\)', path.read_text(), re.M)
    }
    assert reused == {(ROOT / p).resolve() for p in REUSED_ASSETS if p.endswith('.svg')}
    diagram_reports=[diagram_check(p) for p in sorted(reused)]
    assert len(diagram_reports)==11
    validate_links(ROOT/'specs/README.md')
    result={'result':'passed', 'documents':reports, 'diagrams':diagram_reports,
            'predecessor_business_content_preserved':True, 'eleven_existing_diagram_visuals_unchanged':True,
            'archive_relocation_record':'archive-relocation.json',
            'new_views_remain_draft_publication_authorised':True, 'top_public_private_operator_summaries':True,
            'stable_sources':{'923861390':'SPEC-SEI-037','936509725':'SPEC-SEI-038','936509735':'SPEC-SEI-039'}, 'static_preview_diagnostics':'passed',
            'implementation_tests_executed':False,
            'limits':'Document identity, metadata, local links/anchors and source preservation with explicit archive-relocation hashes; original preservation snapshot retained. Existing SVG/PNG visuals unchanged; five Draw.io source links rebased. Static HTML rendering only; browser viewport checks were not performed. No contract, legal, production or external-link qualification.'}
    (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
