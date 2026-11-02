"""Preview, publish and verify the authorised lifecycle views from merged Git."""
import argparse
import hashlib
import html
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
from urllib.parse import quote, unquote, urlsplit
import xml.etree.ElementTree as ET

import markdown

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher

SOURCE = ROOT / 'specs/invoice-lifecycle'
PARENT, SUMMARY = '837610664', '923861398'
COUNTS = {'SPEC-SEI-028': 1, 'SPEC-SEI-029': 1, 'SPEC-SEI-030': 3, 'SPEC-SEI-041': 0}
REPO = 'jiaxinhe0709/pm_second_brain'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def documents():
    return [(path, *publisher.load_document(path)) for path in sorted(SOURCE.rglob('SPEC-*.md'))]


def install_links(revision, docs):
    targets = {str(path.relative_to(ROOT)): metadata['confluence']['title']
               for path, metadata, _ in docs}
    targets['specs/invoice-lifecycle/README.md'] = docs[0][1]['confluence']['title']
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

        def native_anchor(value):
            return ('<ac:structured-macro ac:name="anchor"><ac:parameter ac:name="">'
                    + html.escape(value, quote=True) + '</ac:parameter></ac:structured-macro>')

        def heading(match):
            if match[2] == 'Confluence page history':
                return match[0]
            token = next(headings)
            assert int(match[1]) == token['level']
            return native_anchor(token['id']) + match[0]

        storage = re.sub(r'<h([1-6])>(.*?)</h\1>', heading, storage, flags=re.S)
        assert next(headings, None) is None
        storage = re.sub(r'<a id="([^"]+)"></a>', lambda m: native_anchor(m[1]), storage)

        def link(match):
            url = html.unescape(match[1])
            if url.startswith('#'):
                title, fragment = metadata['confluence']['title'], url[1:]
            else:
                marker = '/blob/' + revision + '/'
                if marker not in url or match[2] == revision:
                    return match[0]
                relative, _, fragment = unquote(url.split(marker, 1)[1]).partition('#')
                title = targets.get(relative)
                if not title:
                    return match[0]
            destination = 'https://confluence.sage.com/display/DNBU/' + quote(title.replace(' ', '+'), safe='+')
            if fragment:
                # Verified against rendered DNBU anchors, including the E-Invoice title.
                destination += '#' + re.sub(r'[^A-Za-z0-9]', '', title) + '-' + fragment
            return '<a href="' + html.escape(destination, quote=True) + '">' + match[2] + '</a>'

        return re.sub(r'<a href="([^"]+)">(.*?)</a>', link, storage, flags=re.S)

    publisher.storage_with_drawio = render


class RenderedLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors, self.links = set(), []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('id', 'name'):
            if attrs.get(key):
                self.anchors.add(attrs[key])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])


def prepare(revision, docs):
    assert {metadata['id'] for _, metadata, _ in docs} == set(COUNTS)
    spec = importlib.util.spec_from_file_location('lifecycle_review', ROOT / 'work/prepare-invoice-lifecycle-review.py')
    review = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(review)
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
            svg = ET.parse(asset.source.with_suffix('.svg')).getroot()
            assert svg.get('role') == 'img' and svg.get('aria-label')
            assert struct.unpack('>II', asset.preview.read_bytes()[16:24]) == (
                int(svg.get('width')), int(svg.get('height')))
        storage = publisher.storage_with_drawio(metadata, body, revision,
            publisher.git_source_url(revision, path), assets, {})
        ET.fromstring('<root xmlns:ac="urn:ac" xmlns:ri="urn:ri">' + storage + '</root>')
        assert storage.count('ac:name="drawio"') == COUNTS[metadata['id']]
        assert 'change-history' in storage and 'file://' not in storage
        assert not re.search(r'<a href="(?:\.\.?/|#)', storage)


def verify(client, revision, docs, results):
    rendered, records = {}, []
    by_id = {metadata['id']: (path, metadata, body) for path, metadata, body in docs}
    for result in results:
        path, metadata, body = by_id[result['source_id']]
        page = client.get_page_by_id(result['page_id'], expand='version,body.storage,body.view,ancestors')
        storage = page['body']['storage']['value']
        assert result['source_id'] in storage and revision in storage
        assert result['source_id'] in page['version'].get('message', '')
        assert revision[:12] in page['version'].get('message', '')
        assert storage.count('ac:name="drawio"') == COUNTS[result['source_id']]
        assert 'change-history' in storage and 'Lifecycle status:</strong> draft' in storage
        assert str(page['ancestors'][-1]['id']) == PARENT
        view = RenderedLinks()
        view.feed(page['body']['view']['value'])
        rendered[page['title']] = view
        attachments = {item['title']: item for item in
            client.get_attachments_from_content(result['page_id'], limit=500, expand='version')['results']}
        verified = []
        for asset in publisher.drawio_assets(path, body):
            for name, local in [(asset.name, asset.source), (asset.name + '.png', asset.preview)]:
                item = attachments[name]
                remote = client.get(item['_links']['download'], not_json_response=True)
                if isinstance(remote, str):
                    remote = remote.encode()
                assert hashlib.sha256(remote).digest() == hashlib.sha256(local.read_bytes()).digest(), name
                verified.append(name)
        records.append(dict(result, version=page['version']['number'], verified_attachments=verified))
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
            'rendered_section_links_checked': checked, 'browser_inspection': 'not available'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--merged-pr', type=int)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('--receipt', type=Path, default=Path('/private/tmp/invoice-lifecycle-publication.json'))
    args = parser.parse_args()
    assert not (args.live and args.verify_only)
    docs, revision = documents(), git('rev-parse', 'HEAD')
    saved = json.loads(args.receipt.read_text()) if args.receipt.exists() else {}
    if args.verify_only:
        revision = saved['git_revision']
    install_links(revision, docs)
    prepare(revision, docs)
    publisher.load_workspace_env(ROOT / 'tools/update_confluence_pages.py')
    client = publisher.confluence_client()
    client.timeout = 30
    if args.verify_only:
        result = verify(client, revision, docs, saved['results'])
        saved['verification'] = result
        args.receipt.write_text(json.dumps(saved, indent=2) + '\n')
        print(json.dumps(result, indent=2))
        return
    parent = client.get_page_by_id(PARENT, expand='version')
    summary = client.get_page_by_id(SUMMARY, expand='version,body.storage,ancestors')
    assert str(summary['ancestors'][-1]['id']) == PARENT
    assert not re.search(r'manual[ -]discussion', summary['body']['storage']['value'], re.I)
    if not args.live:
        for path, metadata, body in docs:
            collision = client.get_page_by_title('DNBU', metadata['confluence']['title'])
            assert not collision or str(collision['id']) == metadata['confluence']['page_id']
            print(publisher.update_document(client, path, metadata, body, revision, False, True))
        plan = {'summary_version': summary['version']['number'], 'parent_version': parent['version']['number'],
                'predecessor_sha256': hashlib.sha256((ROOT / 'specs/archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md').read_bytes()).hexdigest()}
        args.receipt.write_text(json.dumps({'preflight': plan}, indent=2) + '\n')
        return
    assert args.merged_pr, 'Publish only after a merged review PR'
    pr = json.loads(subprocess.check_output(['gh', 'pr', 'view', str(args.merged_pr),
        '--repo', REPO, '--json', 'state,mergeCommit,url'], text=True))
    assert pr['state'] == 'MERGED' and pr['mergeCommit']['oid'] == revision
    assert not git('status', '--porcelain', '--', 'specs', 'assets/diagrams', 'context', 'config/confluence.yml')
    assert summary['version']['number'] == saved['preflight']['summary_version']
    assert parent['version']['number'] == saved['preflight']['parent_version']
    assert hashlib.sha256((ROOT / 'specs/archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md').read_bytes()).hexdigest() == saved['preflight']['predecessor_sha256']
    saved.update(git_revision=revision, review_pr=pr['url'], results=[])
    args.receipt.write_text(json.dumps(saved, indent=2) + '\n')
    for path, metadata, body in docs[1:] + docs[:1]:
        result = publisher.update_document(client, path, metadata, body, revision, True, True)
        page_id = re.search(r'page=(\d+)', result)[1]
        page = client.get_page_by_id(page_id, expand='version,body.storage')
        if metadata['id'] not in page['version'].get('message', ''):
            client.update_page(page_id=page_id, title=metadata['confluence']['title'],
                body=page['body']['storage']['value'], parent_id=PARENT, representation='storage',
                version_comment=publisher.publication_version_comment(metadata, revision), always_update=True)
        saved['results'].append({'source_id': metadata['id'], 'page_id': page_id,
            'file': str(path.relative_to(ROOT)), 'title': metadata['confluence']['title']})
        args.receipt.write_text(json.dumps(saved, indent=2) + '\n')
        print(result, flush=True)
    saved['verification'] = verify(client, revision, docs, saved['results'])
    assert client.get_page_by_id(PARENT, expand='version')['version']['number'] == parent['version']['number']
    args.receipt.write_text(json.dumps(saved, indent=2) + '\n')
    print(json.dumps(saved['verification'], indent=2))


if __name__ == '__main__':
    main()
