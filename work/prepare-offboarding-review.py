"""Validate and render the local offboarding review set. No publication calls."""

from collections import Counter
import hashlib
import html
import json
import os
from pathlib import Path
import re

import markdown
import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'specs/offboarding'
OUT = ROOT / 'work/offboarding-review'
BASELINE = ROOT / 'specs/archive/SPEC-SEI-003-offboarding-solution-specification.md'
# Fingerprint after the verified archive move; only relative links changed.
BASELINE_HASH = 'fd7ac66dc16374144c0fb9634cf2a2f109fdb1813c79541778ebf4dd6bf85dc3'
EXPECTED_IDS = {'SPEC-SEI-031', 'SPEC-SEI-032', 'SPEC-SEI-033'}
STYLE = '''
*{box-sizing:border-box}body{margin:0;color:#243445;background:#fff;font:16px/1.55 Arial,sans-serif}
header{padding:18px 24px;background:#f3f6f8;border-bottom:1px solid #ccd4dc}nav{display:flex;flex-wrap:wrap;gap:20px}
a{color:#075eaa}main{max-width:1200px;margin:28px auto;padding:0 24px}h1{font-size:30px}h2{margin-top:36px}
.table-scroll{overflow:auto;margin:18px 0}table{border-collapse:collapse;width:100%;min-width:650px;font-size:14px}
th,td{border:1px solid #ccd4dc;vertical-align:top;text-align:left;padding:10px;overflow-wrap:anywhere}th{background:#f3f6f8}
code{font-size:.9em;background:#f3f6f8;overflow-wrap:anywhere}img{display:block;width:100%;height:auto;margin:20px 0}
.notice{padding:12px;background:#fff5da;border-left:4px solid #ad7000}.toc{font-size:14px}.toc ul{padding-left:22px}
'''


def render(path):
    text = path.read_text()
    body = text.split('---', 2)[2] if text.startswith('---\n') else text
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


def main():
    docs = sorted(SOURCE.glob('SPEC-*.md'))
    assert len(docs) == 3
    ids = Counter()
    for path in (ROOT / 'specs').rglob('*.md'):
        match = re.search(r'^id: (SPEC-\S+)$', path.read_text(), re.M)
        if match:
            ids[match[1]] += 1
    actual_hash = hashlib.sha256(BASELINE.read_bytes()).hexdigest()
    assert actual_hash == BASELINE_HASH, 'Baseline changed since this review began'
    config = yaml.safe_load((ROOT / 'config/confluence.yml').read_text())
    assert config['publication']['current_sources']['923861391'] == 'SPEC-SEI-003'
    pages = {}
    for path in docs:
        metadata = yaml.safe_load(path.read_text().split('---', 2)[1])
        for field in ['id', 'title', 'type', 'status', 'owner', 'product', 'created',
                      'updated', 'reviewers', 'related', 'confluence']:
            assert field in metadata, (path.name, field)
        assert metadata['id'] in EXPECTED_IDS and ids[metadata['id']] == 1
        assert metadata['status'] == 'draft'
        assert metadata['confluence']['publish'] is False
        assert metadata['confluence']['page_id'] == ''
        assert 'SPEC-SEI-003' in metadata['related']
        assert '## Revision overview' in path.read_text()
        assert '## REF Source references' in path.read_text()
        pages[path] = (metadata['id'] + '.html', metadata['title'])
    assert {name.removesuffix('.html') for name, _ in pages.values()} == EXPECTED_IDS
    pages[SOURCE / 'README.md'] = ('index.html', 'Customer offboarding review')
    OUT.mkdir(exist_ok=True)
    nav = ' · '.join(f'<a href="{name}">{html.escape(title)}</a>'
                     for name, title in pages.values())
    reports = []
    for path, (name, title) in pages.items():
        link_count = validate_links(path)
        md, markup = render(path)

        def rewrite(match):
            attr, target = match.groups()
            if '://' in target or target.startswith('#'):
                return match.group(0)
            relative, separator, anchor = html.unescape(target).partition('#')
            destination = (path.parent / relative).resolve()
            rewritten = pages[destination][0] if destination in pages else os.path.relpath(destination, OUT)
            if separator:
                rewritten += '#' + anchor
            return f'{attr}="{html.escape(rewritten, quote=True)}"'

        markup = re.sub(r'(href|src)="([^"]+)"', rewrite, markup)
        markup = markup.replace('<table>', '<div class="table-scroll"><table>')
        markup = markup.replace('</table>', '</table></div>')
        document = ('<!doctype html><html lang="en"><meta charset="utf-8">'
                    '<meta name="viewport" content="width=device-width,initial-scale=1">'
                    f'<title>{html.escape(title)}</title><style>{STYLE}</style>'
                    f'<header><nav>{nav}</nav></header><main>'
                    '<p class="notice">Unpublished draft. Proposed periods need approval. '
                    'SPEC-SEI-003 is retained in the archive and remains the selected Confluence source.</p>'
                    f'{md.toc}{markup}</main></html>')
        (OUT / name).write_text(document)
        reports.append({'source': str(path.relative_to(ROOT)), 'local_links_checked': link_count,
                        'preview': name})
    result = {'result': 'passed', 'documents': reports, 'baseline_sha256': actual_hash,
              'baseline_unchanged': True, 'selected_confluence_source': 'SPEC-SEI-003',
              'new_documents_unpublished_drafts': True,
              'implementation_tests_executed': False,
              'limits': 'Metadata, identity, local file/anchor links, source preservation and HTML generation only. '
                        'No external-link, browser, contract, legal-applicability or implementation validation.'}
    (OUT / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
