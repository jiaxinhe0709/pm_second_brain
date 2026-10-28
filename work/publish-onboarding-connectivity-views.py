"""Publish the authorised successor set to three existing pages after Git review."""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote
import xml.etree.ElementTree as ET

import markdown

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher

SOURCE = ROOT / 'specs/onboarding-and-connectivity'
OUT = ROOT / 'work/onboarding-and-connectivity-publication'
PARENT = '837610648'
PAGES = {'SPEC-SEI-037': ('923861390', 1),
         'SPEC-SEI-038': ('936509725', 2),
         'SPEC-SEI-039': ('936509735', 4)}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def install_links(revision, documents):
    targets = {str(p.relative_to(ROOT)): m['confluence']['page_id']
               for p, m, _ in documents}
    # The rendered Confluence anchor prefix omits spaces and title hyphens.
    prefixes = {m['confluence']['page_id']: re.sub(r'[\s-]+', '', m['confluence']['title'])
                for _, m, _ in documents}
    original = publisher.storage_with_drawio

    def render(metadata, body, *args, **kwargs):
        storage = original(metadata, body, *args, **kwargs)
        # Explicit named anchors retain Markdown section links after publication.
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
            name = html.escape(heading['id'], quote=True)
            return ('<ac:structured-macro ac:name="anchor">'
                    f'<ac:parameter ac:name="">{name}</ac:parameter>'
                    '</ac:structured-macro>' + match[0])
        storage = re.sub(r'<h([1-6])>(.*?)</h\1>', anchor, storage, flags=re.S)
        assert next(headings, None) is None
        # Keep earlier section links valid when a heading gains a phase suffix.
        # This also preserves the API-01–05 aliases used by the companion view.
        storage = re.sub(
            r'<a id="([^"]+)"></a>',
            lambda match: ('<ac:structured-macro ac:name="anchor">'
                           '<ac:parameter ac:name="">'
                           + html.escape(match[1], quote=True)
                           + '</ac:parameter></ac:structured-macro>'),
            storage,
        )
        def link(match):
            url = html.unescape(match[1])
            if match[2] == revision:
                return match[0]
            if url.startswith('#'):
                target = ('https://confluence.sage.com/pages/viewpage.action?pageId='
                          + metadata['confluence']['page_id'] + '#'
                          + prefixes[metadata['confluence']['page_id']] + '-' + url[1:])
                return '<a href="' + html.escape(target, quote=True) + '">' + match[2] + '</a>'
            marker = '/blob/' + revision + '/'
            if marker not in url:
                return match[0]
            relative, separator, fragment = unquote(url.split(marker, 1)[1]).partition('#')
            pid = targets.get(relative)
            if relative == 'specs/onboarding-and-connectivity/README.md':
                pid = PAGES['SPEC-SEI-037'][0]
            if not pid:
                return match[0]
            target = 'https://confluence.sage.com/pages/viewpage.action?pageId=' + pid
            if separator:
                target += '#' + prefixes[pid] + '-' + fragment
            return '<a href="' + html.escape(target, quote=True) + '">' + match[2] + '</a>'
        return re.sub(r'<a href="([^"]+)">(.*?)</a>', link, storage, flags=re.S)
    publisher.storage_with_drawio = render


def prepare(revision):
    OUT.mkdir(exist_ok=True)
    documents = [(p, *publisher.load_document(p)) for p in sorted(SOURCE.glob('SPEC-*.md'))]
    assert {m['id'] for _, m, _ in documents} == set(PAGES)
    install_links(revision, documents)
    records = []
    for path, metadata, body in documents:
        pid, diagrams = PAGES[metadata['id']]
        target = publisher.validate_publication(metadata, path, False)
        assert target['page_id'] == pid and target['parent_page_id'] == PARENT
        assert metadata['status'] == 'draft'
        publisher.validate_no_manual_history(body, path)
        assets = publisher.drawio_assets(path, body)
        assert len(assets) == diagrams
        storage = publisher.storage_with_drawio(metadata, body, revision,
                  publisher.git_source_url(revision, path), assets, {})
        ET.fromstring('<root xmlns:ac="urn:ac" xmlns:ri="urn:ri">' + storage + '</root>')
        assert storage.count('ac:name="drawio"') == diagrams
        assert 'change-history' in storage and 'file://' not in storage
        assert not re.search(r'<a href="(?:\.\.?/|#)', storage)
        (OUT / (metadata['id'] + '.storage.xml')).write_text(storage)
        records.append({'source_id': metadata['id'], 'file': str(path.relative_to(ROOT)),
                        'page_id': pid, 'title': target['title'],
                        'editable_diagrams': diagrams,
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest = {'git_revision': revision, 'pages': records, 'live_publication': False}
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return documents, manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--merged-pr', type=int)
    parser.add_argument('--env-from', type=Path)
    args = parser.parse_args()
    revision = git('rev-parse', 'HEAD')
    documents, manifest = prepare(revision)
    if not args.live:
        print(json.dumps(manifest, indent=2))
        return
    assert args.merged_pr, 'A merged review PR is required'
    review = json.loads(subprocess.check_output(['gh', 'pr', 'view', str(args.merged_pr),
        '--repo', 'jiaxinhe0709/pm_second_brain', '--json', 'state,mergedAt,mergeCommit,url'], text=True))
    assert review['state'] == 'MERGED' and review['mergedAt']
    assert review['mergeCommit']['oid'] == revision, 'Publish from the verified merged snapshot'
    assert not git('status', '--porcelain', '--', 'specs', 'assets/diagrams', 'context', 'config/confluence.yml')
    publisher.load_workspace_env(args.env_from or Path(__file__))
    client = publisher.confluence_client()
    preflight = json.loads((OUT / 'preflight.json').read_text())
    versions = {p['page_id']: p['version'] for p in preflight['pages']}
    parent_version = client.get_page_by_id(PARENT, expand='version')['version']['number']
    # Check all three pages before the first write.
    for _, metadata, _ in documents:
        pid = metadata['confluence']['page_id']
        page = client.get_page_by_id(pid, expand='version,body.storage,ancestors')
        assert page['version']['number'] == versions[pid], 'Page changed since preflight; reconcile first'
        assert str(page['ancestors'][-1]['id']) == PARENT
        assert not re.search('manual[ -]discussion', page['body']['storage']['value'], re.I)
        collision = client.get_page_by_title('DNBU', metadata['confluence']['title'])
        assert not collision or str(collision['id']) == pid, 'New title belongs to another page'
    manifest.update(review=review, results=[])
    for path, metadata, body in documents:
        pid = metadata['confluence']['page_id']
        page = client.get_page_by_id(pid, expand='version')
        assert page['version']['number'] == versions[pid]
        print(publisher.update_document(client, path, metadata, body, revision, True, False), flush=True)
        saved = client.get_page_by_id(pid, expand='version,body.storage,ancestors')
        storage = saved['body']['storage']['value']
        assert saved['title'] == metadata['confluence']['title']
        assert str(saved['ancestors'][-1]['id']) == PARENT
        assert metadata['id'] in storage and revision in storage and 'change-history' in storage
        assert saved['version']['number'] == versions[pid] + 1
        assert storage.count('ac:name="drawio"') == PAGES[metadata['id']][1]
        names = {a['title'] for a in client.get_attachments_from_content(pid, limit=500)['results']}
        for asset in publisher.drawio_assets(path, body):
            assert asset.name in names and asset.name + '.png' in names
        manifest['results'].append({'source_id': metadata['id'], 'page_id': pid,
            'title': saved['title'], 'version': saved['version']['number'],
            'editable_diagrams': PAGES[metadata['id']][1], 'verified': True})
        (OUT / 'receipt.json').write_text(json.dumps(manifest, indent=2) + '\n')
    assert client.get_page_by_id(PARENT, expand='version')['version']['number'] == parent_version
    from verify_onboarding_connectivity_publication import verify
    verification = verify(client, revision)
    (OUT / 'verification.json').write_text(json.dumps(verification, indent=2) + '\n')
    manifest.update(live_publication=True, parent_content_unchanged=True)
    (OUT / 'receipt.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(manifest['results'], indent=2))


if __name__ == '__main__':
    main()
