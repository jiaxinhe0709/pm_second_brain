"""Prepare or publish the authorised three-view onboarding set.

Uses the repository renderer, source revision banner, Change History and Draw.io
uploader. Live publication requires a merged PR and a clean source snapshot.
"""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher
import yaml

PARENT = '837610648'
DOCS = [
    ('SPEC-SEI-018', 'Onboarding Solution Summary'),
    ('SPEC-SEI-019', 'Onboarding Logical Feature Specification'),
    ('SPEC-SEI-021', 'Onboarding API Reuse Assessment'),
]
OUT = ROOT / 'work/onboarding-publication'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def install_links(revision):
    targets = {}
    for path in (ROOT / 'specs/onboarding').glob('SPEC-*.md'):
        metadata, _ = publisher.load_document(path)
        for ident, title in DOCS:
            if metadata['id'] == ident:
                targets[str(path.relative_to(ROOT))] = title
    original = publisher.storage_with_drawio

    def render(*args, **kwargs):
        storage = original(*args, **kwargs)

        def link(match):
            url, label = html.unescape(match[1]), match[2]
            marker = '/blob/' + revision + '/'
            if marker not in url:
                return match[0]
            relative = unquote(url.split(marker, 1)[1].split('#')[0])
            if relative == 'specs/onboarding/README.md':
                return f'<a href="https://confluence.sage.com/pages/viewpage.action?pageId={PARENT}">{label}</a>'
            if relative not in targets:
                return match[0]
            plain = html.unescape(re.sub('<[^>]+>', '', label))
            assert ']]>' not in plain
            return ('<ac:link><ri:page ri:space-key="DNBU" ri:content-title="'
                    + html.escape(targets[relative], quote=True)
                    + '"/><ac:plain-text-link-body><![CDATA[' + plain
                    + ']]></ac:plain-text-link-body></ac:link>')

        return re.sub(r'<a href="([^"]+)">(.*?)</a>', link, storage, flags=re.S)

    publisher.storage_with_drawio = render


def prepare(revision):
    OUT.mkdir(exist_ok=True)
    install_links(revision)
    records = []
    documents = []
    for ident, title in DOCS:
        path = next((ROOT / 'specs/onboarding').glob(ident + '-*.md'))
        metadata, body = publisher.load_document(path)
        assert metadata['status'] == 'draft'
        assert metadata['confluence']['title'] == title
        target = publisher.validate_publication(metadata, path, True)
        publisher.validate_no_manual_history(body, path)
        assets = publisher.drawio_assets(path, body)
        source = publisher.git_source_url(revision, path)
        storage = publisher.storage_with_drawio(metadata, body, revision, source, assets, {})
        assert storage.count('ac:name="drawio"') == len(assets)
        assert 'change-history' in storage and 'ri:content-title="Onboarding' in storage
        assert 'file://' not in storage
        (OUT / (ident + '.storage.xml')).write_text(storage)
        records.append({'source_id': ident, 'file': str(path.relative_to(ROOT)),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'title': title, 'target': target, 'editable_diagrams': len(assets)})
        documents.append((path, metadata, body))
    assert [x['editable_diagrams'] for x in records] == [1, 4, 5]
    manifest = {'mode': 'prepared', 'parent_page_id': PARENT, 'git_revision': revision,
                'lifecycle_status': 'draft', 'pages': records,
                'retained_git_reference': 'SPEC-SEI-020', 'live_publication': False}
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return documents, manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--refresh', action='store_true', help='Update the recorded existing pages')
    parser.add_argument('--merged-pr', type=int)
    parser.add_argument('--env-from', type=Path)
    args = parser.parse_args()
    revision = git('rev-parse', 'HEAD')
    documents, manifest = prepare(revision)
    if not args.live:
        print(json.dumps(manifest, indent=2))
        return
    assert args.merged_pr, 'A merged review PR is required'
    review = json.loads(subprocess.check_output(
        ['gh', 'pr', 'view', str(args.merged_pr), '--repo', 'jiaxinhe0709/pm_second_brain',
         '--json', 'state,mergedAt,mergeCommit,url'], text=True))
    assert review['state'] == 'MERGED' and review['mergedAt']
    merge_sha = review['mergeCommit']['oid']
    subprocess.run(['git', 'merge-base', '--is-ancestor', revision, merge_sha], cwd=ROOT, check=True)
    protected = ['specs/onboarding', 'specs/archive', 'assets/diagrams', 'context', 'config/confluence.yml']
    assert not git('status', '--porcelain', '--', *protected), 'Publication sources must be committed'
    publisher.load_workspace_env(args.env_from or Path(__file__))
    client = publisher.confluence_client()
    parent = client.get_page_by_id(PARENT, expand='version')
    assert parent['title'] == 'Public Platform - Onboarding'
    if args.refresh:
        previous = json.loads((OUT / 'receipt.json').read_text())
        versions = {item['page_id']: item['version'] for item in previous['results']}
        for _, metadata, _ in documents:
            pid = metadata['confluence']['page_id']
            assert pid and pid in versions, 'Refresh requires a recorded page'
            page = client.get_page_by_id(pid, expand='version,body.storage,ancestors')
            assert str(page['ancestors'][-1]['id']) == PARENT
            assert page['title'] == metadata['confluence']['title']
            assert page['version']['number'] == versions[pid], 'Page changed since last verification; reconcile first'
            assert not re.search('manual[ -]discussion', page['body']['storage']['value'], re.I)
    else:
        summary = client.get_page_by_id('923861390', expand='version,body.storage,ancestors')
        assert str(summary['ancestors'][-1]['id']) == PARENT
        assert summary['version']['number'] == 10, 'Summary changed since preflight; reconcile first'
        assert not re.search('manual[ -]discussion', summary['body']['storage']['value'], re.I)
        for _, metadata, _ in documents:
            found = client.get_page_by_title('DNBU', metadata['confluence']['title'])
            assert not found, 'A target title already exists; reconcile its page ID first'
    manifest['review'] = review
    manifest['parent_version_before'] = parent['version']['number']
    manifest['results'] = []
    for path, metadata, body in documents:
        result = publisher.update_document(client, path, metadata, body, revision, True, True)
        print(result, flush=True)
        match = re.search(r'page=(\d+)', result)
        assert match
        pid = match[1]
        page = client.get_page_by_id(pid, expand='body.storage,version,ancestors')
        assert page['title'] == metadata['confluence']['title']
        assert str(page['ancestors'][-1]['id']) == PARENT
        saved = page['body']['storage']['value']
        assert metadata['id'] in saved and revision in saved and 'change-history' in saved
        expected = len(publisher.drawio_assets(path, body))
        assert saved.count('ac:name="drawio"') == expected
        attachments = client.get_attachments_from_content(pid, limit=500)
        names = {item['title'] for item in attachments['results']}
        for asset in publisher.drawio_assets(path, body):
            assert asset.name in names and asset.name + '.png' in names
        if not metadata['confluence']['page_id']:
            path.write_text(path.read_text().replace('  page_id: ""', f'  page_id: "{pid}"', 1))
            config_path = ROOT / 'config/confluence.yml'
            config_path.write_text(config_path.read_text() + f'    "{pid}": {metadata["id"]}\n')
        manifest['results'].append({'source_id': metadata['id'], 'page_id': pid,
                                    'title': page['title'], 'version': page['version']['number'],
                                    'editable_diagrams': expected, 'verified': True,
                                    'url': f'https://confluence.sage.com/pages/viewpage.action?pageId={pid}'})
        (OUT / 'receipt.json').write_text(json.dumps(manifest, indent=2) + '\n')
    after = client.get_page_by_id(PARENT, expand='version')
    assert after['version']['number'] == parent['version']['number'], 'Parent unexpectedly changed'
    manifest.update(mode='published', live_publication=True, parent_content_unchanged=True)
    (OUT / 'receipt.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(manifest['results'], indent=2))


if __name__ == '__main__':
    main()
