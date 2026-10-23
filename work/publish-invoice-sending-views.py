"""Publish the authorised sending views from a merged, clean Git snapshot."""

import argparse
import hashlib
import html
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, unquote, urlsplit
import xml.etree.ElementTree as ET

import markdown

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher

SOURCE = ROOT / 'specs/invoice-sending'
OUT = ROOT / 'work/invoice-sending-publication'
PARENT = '837610656'
SUMMARY = '923861395'
COUNTS = {'SPEC-SEI-022': 1, 'SPEC-SEI-023': 1, 'SPEC-SEI-024': 3}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def documents():
    return [(path, *publisher.load_document(path)) for path in sorted(SOURCE.glob('SPEC-*.md'))]


def install_links(revision, docs):
    targets = {str(path.relative_to(ROOT)): metadata['confluence']['title']
               for path, metadata, _ in docs}
    targets['specs/invoice-sending/README.md'] = docs[0][1]['confluence']['title']
    original = publisher.storage_with_drawio

    def render(metadata, body, *args, **kwargs):
        storage = original(metadata, body, *args, **kwargs)
        md = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code'])
        md.convert(body)

        def flatten(tokens):
            for token in tokens:
                yield token
                yield from flatten(token['children'])

        headings = iter(flatten(md.toc_tokens))

        def anchor(match):
            if match[2] == 'Confluence page history':
                return match[0]
            heading = next(headings)
            assert int(match[1]) == heading['level']
            return ('<ac:structured-macro ac:name="anchor"><ac:parameter ac:name="">'
                    + html.escape(heading['id'], quote=True)
                    + '</ac:parameter></ac:structured-macro>' + match[0])

        storage = re.sub(r'<h([1-6])>(.*?)</h\1>', anchor, storage, flags=re.S)
        assert next(headings, None) is None

        def link(match):
            url = html.unescape(match[1])
            fragment = ''
            if url.startswith('#'):
                title = metadata['confluence']['title']
                fragment = url[1:]
            else:
                marker = '/blob/' + revision + '/'
                if marker not in url or match[2] == revision:
                    return match[0]
                relative, _, fragment = unquote(url.split(marker, 1)[1]).partition('#')
                title = targets.get(relative)
                if not title:
                    return match[0]
            target = 'https://confluence.sage.com/display/DNBU/' + quote(title.replace(' ', '+'), safe='+')
            if fragment:
                target += '#' + re.sub(r'\s+', '', title) + '-' + fragment
            return '<a href="' + html.escape(target, quote=True) + '">' + match[2] + '</a>'

        return re.sub(r'<a href="([^"]+)">(.*?)</a>', link, storage, flags=re.S)

    publisher.storage_with_drawio = render


def prepare(revision, docs):
    OUT.mkdir(exist_ok=True)
    assert {metadata['id'] for _, metadata, _ in docs} == set(COUNTS)
    spec = importlib.util.spec_from_file_location('sending_review', ROOT / 'work/prepare-invoice-sending-review.py')
    review = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(review)
    records = []
    for path, metadata, body in docs:
        assert metadata['status'] == 'draft'
        target = publisher.validate_publication(metadata, path, True)
        assert target['parent_page_id'] == PARENT
        publisher.validate_no_manual_history(body, path)
        review.validate_links(path)
        assets = publisher.drawio_assets(path, body)
        assert len(assets) == COUNTS[metadata['id']]
        for asset in assets:
            ET.parse(asset.source)
            ET.parse(asset.source.with_suffix('.svg'))
            assert asset.preview.read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
        storage = publisher.storage_with_drawio(metadata, body, revision,
                    publisher.git_source_url(revision, path), assets, {})
        ET.fromstring('<root xmlns:ac="urn:ac" xmlns:ri="urn:ri">' + storage + '</root>')
        assert storage.count('ac:name="drawio"') == len(assets)
        assert 'change-history' in storage and 'file://' not in storage
        assert not re.search(r'<a href="(?:\.\.?/|#)', storage)
        (OUT / (metadata['id'] + '.storage.xml')).write_text(storage)
        records.append({'source_id': metadata['id'], 'file': str(path.relative_to(ROOT)),
                        'target': target, 'editable_diagrams': len(assets),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    baseline = ROOT / 'specs/archive/SPEC-SEI-007-invoice-sending-solution.md'
    return {'git_revision': revision, 'parent_page_id': PARENT, 'pages': records,
            'retained_predecessor_sha256': hashlib.sha256(baseline.read_bytes()).hexdigest(),
            'lifecycle_status': 'draft', 'live_publication': False}


class RenderedLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.anchors.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.anchors.add(attrs['name'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])


def verify(client, revision, results):
    rendered = {}
    records = []
    for result in results:
        page = client.get_page_by_id(result['page_id'], expand='version,body.storage,body.view,ancestors')
        storage = page['body']['storage']['value']
        view = RenderedLinks()
        view.feed(page['body']['view']['value'])
        rendered[page['title']] = view
        assert result['source_id'] in storage and revision in storage
        assert result['source_id'] in page['version'].get('message', '')
        assert revision[:12] in page['version'].get('message', '')
        assert storage.count('ac:name="drawio"') == COUNTS[result['source_id']]
        assert 'change-history' in storage and 'Lifecycle status:</strong> draft' in storage
        assert str(page['ancestors'][-1]['id']) == PARENT
        attachments = {x['title'] for x in client.get_attachments_from_content(result['page_id'], limit=500)['results']}
        path = ROOT / result['file']
        _, body = publisher.load_document(path)
        for asset in publisher.drawio_assets(path, body):
            assert asset.name in attachments and asset.name + '.png' in attachments
        records.append({'source_id': result['source_id'], 'page_id': result['page_id'],
                        'title': page['title'], 'version': page['version']['number'],
                        'editable_diagrams': COUNTS[result['source_id']]})
    checked = 0
    for title, view in rendered.items():
        for href in view.links:
            parts = urlsplit(href)
            if parts.netloc not in {'', 'confluence.sage.com'}:
                continue
            destination = unquote(parts.path.removeprefix('/display/DNBU/')).replace('+', ' ')
            if destination not in rendered or not parts.fragment:
                continue
            assert unquote(parts.fragment) in rendered[destination].anchors, (title, destination, parts.fragment)
            checked += 1
    assert checked > 0
    return {'result': 'passed', 'git_revision': revision, 'pages': records,
            'rendered_section_links_checked': checked,
            'checks': ['source IDs and Git revision', 'draft lifecycle', 'native Change History',
                       'editable diagrams and PNG attachments', 'parent hierarchy', 'rendered companion section links'],
            'browser_viewport_inspection': 'not performed'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--merged-pr', type=int)
    parser.add_argument('--env-from', type=Path)
    args = parser.parse_args()
    revision = git('rev-parse', 'HEAD')
    docs = documents()
    install_links(revision, docs)
    manifest = prepare(revision, docs)
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if not args.live:
        print(json.dumps(manifest, indent=2))
        return
    assert args.merged_pr, 'Publish only after the review PR is merged'
    review = json.loads(subprocess.check_output(['gh', 'pr', 'view', str(args.merged_pr),
        '--repo', 'jiaxinhe0709/pm_second_brain', '--json', 'state,mergedAt,mergeCommit,url'], text=True))
    assert review['state'] == 'MERGED' and review['mergeCommit']['oid'] == revision
    assert not git('status', '--porcelain', '--', 'specs', 'assets/diagrams', 'context', 'config/confluence.yml')
    publisher.load_workspace_env(args.env_from or Path(__file__))
    client = publisher.confluence_client()
    client.timeout = 30
    preflight = json.loads((OUT / 'preflight.json').read_text())
    parent = client.get_page_by_id(PARENT, expand='version')
    summary = client.get_page_by_id(SUMMARY, expand='version,body.storage,ancestors')
    assert parent['version']['number'] == preflight[0]['version']
    assert summary['version']['number'] == preflight[1]['version']
    assert str(summary['ancestors'][-1]['id']) == PARENT
    assert not re.search('manual[ -]discussion', summary['body']['storage']['value'], re.I)
    existing_children = list(client.get_page_child_by_type(PARENT, type='page', start=0, limit=100))
    assert {str(x['id']) for x in existing_children} == {SUMMARY}
    for _, metadata, _ in docs:
        collision = client.get_page_by_title('DNBU', metadata['confluence']['title'])
        assert not collision or str(collision['id']) == metadata['confluence']['page_id']
    manifest.update(review=review, results=[])
    # Create companions first, then update the existing summary and its navigation.
    for path, metadata, body in docs[1:] + docs[:1]:
        result = publisher.update_document(client, path, metadata, body, revision, True, True)
        print(result, flush=True)
        pid = re.search(r'page=(\d+)', result)[1]
        manifest['results'].append({'source_id': metadata['id'], 'page_id': pid,
            'file': str(path.relative_to(ROOT)), 'title': metadata['confluence']['title']})
        (OUT / 'receipt.json').write_text(json.dumps(manifest, indent=2) + '\n')
    verification = verify(client, revision, manifest['results'])
    assert client.get_page_by_id(PARENT, expand='version')['version']['number'] == parent['version']['number']
    assert {str(x['id']) for x in client.get_page_child_by_type(PARENT, type='page', start=0, limit=100)} == {x['page_id'] for x in manifest['results']}
    (OUT / 'verification.json').write_text(json.dumps(verification, indent=2) + '\n')
    manifest.update(live_publication=True, parent_content_unchanged=True, verification='passed')
    (OUT / 'receipt.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(verification, indent=2))


if __name__ == '__main__':
    main()
