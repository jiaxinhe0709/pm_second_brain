"""Validate and render the three provider-connectivity views; no publication calls."""

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
SOURCE = ROOT / 'specs/archive/provider-connectivity'
OUT = ROOT / 'work/provider-connectivity-review'
EXPECTED = {'SPEC-SEI-034', 'SPEC-SEI-035', 'SPEC-SEI-036'}
PRESERVED = {
    'specs/SPEC-SEI-011-public-platform-connector-solution-specification.md': '63887e401c5fd15ccfd9f4059e3bb282ed19a113e299611f3e33b24501663d53',
    'specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md': '62119fde74462064e9142c4100cf4ab2c731334c19dea4f6b7063b5ed85948d2',
    'specs/SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md': '0c19466151b8aad4b1feda1e0f2e558045058da64867853c5bfe53a69785cee2',
    'config/confluence.yml': 'b9c15daf80ae4acfb080156bbdaa70059518357143732d2622a3c98566013c5b',
    'context/GLO-SEI-001-e-invoicing-terminology.md': '32323073eb2d6e7c8a675dce2657d581ef36ab2329c98c0d767636f30759e39a',
}
REUSED_ASSETS = {'assets/diagrams/global-api-exchange-and-reconciliation-process.svg': 'cabe30982232bc7d194774e3797e420049cb137a3aaca21e3cab78a9c15e9541', 'assets/diagrams/global-api-exchange-and-reconciliation-process.drawio': 'cb0b76b847ca062da23ccf23c6395bb6e4065794589206c71654e802dd9b3fcd', 'assets/diagrams/global-api-exchange-and-reconciliation-process.png': '4142b209b19ea1968d86e041f2ceb98274ee5d80346c4fba274632171cf4d3ef', 'assets/diagrams/public-platform-connector-process.svg': '5a5d8d7e687facb2cb42c5cab544655367c653417031d95e8032b32d9ffd0351', 'assets/diagrams/public-platform-connector-process.drawio': '9ece7faa59eb67da516577b39e1b9b34e4d57539db00c18e58d00e274576215c', 'assets/diagrams/public-platform-connector-process.png': '424b4bedfa06814f2deec47c676151e8f3a1114939aa3a865ea584f27c82dc3a', 'assets/diagrams/b2b-router-adapter-binding-process.svg': '00c7d85a28d63617267bd43a5ca180adbb2a45919da3847f80629649593a3564', 'assets/diagrams/b2b-router-adapter-binding-process.drawio': '704a796be7690f09bb381f5693cb803c051d739f94f66cfbbc1a5a282f2eded9', 'assets/diagrams/b2b-router-adapter-binding-process.png': '0b90bf808b64471754935a0a8814e77fe585c8f2529cf39b6ace7690883a61ee', 'assets/diagrams/invoice-sending-spain-actions-sequence.svg': '9a915d29f80437a3d4c67a5c63e0347f93319b38624749e218ced6fe027a4314', 'assets/diagrams/invoice-sending-spain-actions-sequence.drawio': '7af51d61e8b3355ab5b9e899b7ba227ca5d8eb278003b9f4c9946fabdde3037c', 'assets/diagrams/invoice-sending-spain-actions-sequence.png': '257c390ee581a02137689da382b8c0525e98ae8d3bb5352b122d40c6e25618a1', 'assets/diagrams/invoice-retrieval-spain-public-sequence.svg': '7d10d227a7f7ec5fa31d97bdf00e01114e392e203c865322b50544a44a2c6388', 'assets/diagrams/invoice-retrieval-spain-public-sequence.drawio': 'a2b0d4b88130f7eaffd03d9146b1a633f6fdfae358ead6f5d217daa37ef53098', 'assets/diagrams/invoice-retrieval-spain-public-sequence.png': '7ab071622c8b5a33330d8ee26c4de7b371cfe811c4b01961d655f33a2330fdb9', 'assets/diagrams/invoice-retrieval-fr-notification-sequence.svg': '0d60e959c12ddc2c343b8a4eb8d4ebbdf38089da796d7e9542e4d5948ae49a49', 'assets/diagrams/invoice-retrieval-fr-notification-sequence.drawio': 'a24fa0bbe71793ad697f0ca635df109d0b8396c631e72d1caab8cc71fc0e5cc0', 'assets/diagrams/invoice-retrieval-fr-notification-sequence.png': 'c439e1ce42da0b6044e2a9d2c79299c7cb07b2c7914325babef329971e45390b'}

STYLE = '\n*{box-sizing:border-box}body{margin:0;color:#243445;background:#fff;font:16px/1.55 Arial,sans-serif}\nheader{padding:18px 24px;background:#f3f6f8;border-bottom:1px solid #ccd4dc}nav{display:flex;flex-wrap:wrap;gap:20px}\na{color:#075eaa}main{max-width:1200px;margin:28px auto;padding:0 24px}h1{font-size:30px}h2{margin-top:36px}\n.table-scroll{overflow:auto;margin:18px 0}table{border-collapse:collapse;width:100%;min-width:650px;font-size:14px}\nth,td{border:1px solid #ccd4dc;vertical-align:top;text-align:left;padding:10px;overflow-wrap:anywhere}th{background:#f3f6f8}\ncode{font-size:.9em;background:#f3f6f8;overflow-wrap:anywhere}img{display:block;width:100%;height:auto;margin:20px 0}\n.notice{padding:12px;background:#fff5da;border-left:4px solid #ad7000}.toc{font-size:14px}.toc ul{padding-left:22px}\n\n.diagram{overflow-x:auto}.diagram img{min-width:1050px}\n'


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
        assert meta['confluence']['publish'] is False and not meta['confluence']['page_id']
        assert all('SPEC-SEI-'+n in meta['related'] for n in ['011','013','017'])
        assert '## Revision overview' in path.read_text() and '## REF Source references' in path.read_text()
        pages[path] = (meta['id']+'.html', meta['title'])
    assert {name.removesuffix('.html') for name,_ in pages.values()} == EXPECTED
    pages[SOURCE/'README.md'] = ('index.html', 'Provider connectivity review')
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
                  f'<header><nav>{nav}</nav></header><main><p class="notice">Unpublished design proposal. '
                  'Specs 011, 013 and 017 and current Confluence sources remain unchanged.</p>'
                  f'{md.toc}{markup}</main></body></html>')
        diagnostics=Diagnostics()
        diagnostics.feed(document)
        (OUT/name).write_text(document)
        count=validate_links(path)
        reports.append({'source':str(path.relative_to(ROOT)), 'preview':name, 'local_links':count, 'diagrams':diagnostics.images})
    assert sum(r['diagrams'] for r in reports)==6
    reused = {
        (path.parent / target).resolve()
        for path in docs
        for target in re.findall(r'^!\[[^\]]*\]\(([^)]+\.svg)\)', path.read_text(), re.M)
    }
    assert reused == {(ROOT / p).resolve() for p in REUSED_ASSETS if p.endswith('.svg')}
    diagram_reports=[diagram_check(p) for p in sorted(reused)]
    assert len(diagram_reports)==6
    validate_links(ROOT/'specs/README.md')
    result={'result':'passed', 'documents':reports, 'diagrams':diagram_reports,
            'source_specs_and_publication_unchanged':True, 'six_existing_diagrams_reused_unchanged':True,
            'new_views_unpublished_drafts':True, 'static_preview_diagnostics':'passed',
            'implementation_tests_executed':False,
            'limits':'Document identity, metadata, local links/anchors, source preservation, unchanged source diagram hashes and asset XML/PNG checks. Existing source diagrams reused without regeneration. Headless Chrome could not launch under the current sandbox; browser viewport checks are not claimed. No contract, legal, production or external-link qualification.'}
    (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
