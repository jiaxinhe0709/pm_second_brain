"""Publish 040 beneath Onboarding from a merged source; keep 039 links aligned."""
import argparse
import hashlib
import html
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher

spec = importlib.util.spec_from_file_location('onboarding_links', ROOT / 'work/publish-onboarding-connectivity-views.py')
links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(links)
FOLDER = ROOT / 'specs/onboarding-and-connectivity'
OUT = ROOT / 'work/onboarding-api-reference-publication'
PARENT = '837610648'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--merged-pr', type=int)
    parser.add_argument('--env-from', type=Path)
    parser.add_argument('--expected-parent-version', type=int)
    parser.add_argument('--expected-child-version', type=int)
    args = parser.parse_args()
    revision = git('rev-parse', 'HEAD')
    paths = sorted(FOLDER.glob('SPEC-*.md')) + sorted((FOLDER / 'api-reference').glob('SPEC-*.md'))
    documents = [(path, *publisher.load_document(path)) for path in paths]
    selected = [item for item in documents if item[1]['id'] in {'SPEC-SEI-039', 'SPEC-SEI-040'}]
    assert len(selected) == 2
    child = next(item for item in selected if item[1]['id'] == 'SPEC-SEI-040')
    assert child[1]['confluence']['parent_page_id'] == PARENT
    creating = not child[1]['confluence']['page_id']
    links.install_links(revision, documents)
    render = publisher.storage_with_drawio
    def with_explicit_anchors(*values, **kwargs):
        value = render(*values, **kwargs)
        return re.sub(r'<p><a id="(api-\d{2})"></a></p>',
            lambda m: '<ac:structured-macro ac:name="anchor"><ac:parameter ac:name="">'
            + m[1] + '</ac:parameter></ac:structured-macro>', value)
    publisher.storage_with_drawio = with_explicit_anchors
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for path, meta, body in selected:
        assert meta['status'] == 'draft'
        publisher.validate_publication(meta, path, creating)
        assets = publisher.drawio_assets(path, body)
        storage = publisher.storage_with_drawio(meta, body, revision,
                    publisher.git_source_url(revision, path), assets, {})
        ET.fromstring('<root xmlns:ac="urn:ac" xmlns:ri="urn:ri">' + storage + '</root>')
        assert 'change-history' in storage and revision in storage and 'file://' not in storage
        assert not re.search(r'<a href="(?:\.\.?/|#)', storage)
        if meta['id'] == 'SPEC-SEI-040':
            assert storage.count('ac:name="html"') == 11
            assert all('>' + f'api-{i:02}' + '</ac:parameter>' in storage for i in range(1, 6))
            assert '#666666' in storage and '#1565C0' in storage
        (OUT / (meta['id'] + '.storage.xml')).write_text(storage)
        records.append({'id': meta['id'], 'path': str(path.relative_to(ROOT)),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    receipt = {'revision': revision, 'creating_child': creating, 'sources': records,
               'live_publication': False, 'results': []}
    (OUT / 'plan.json').write_text(json.dumps(receipt, indent=2) + '\n')
    if not args.live:
        print(json.dumps(receipt, indent=2))
        return
    assert args.merged_pr and args.expected_parent_version
    review = json.loads(subprocess.check_output(['gh', 'pr', 'view', str(args.merged_pr),
        '--repo', 'jiaxinhe0709/pm_second_brain', '--json', 'state,mergeCommit,url'], text=True))
    assert review['state'] == 'MERGED' and review['mergeCommit']['oid'] == revision
    assert not git('status', '--porcelain', '--', 'specs', 'context', 'config/confluence.yml')
    publisher.load_workspace_env(args.env_from or ROOT / 'tools/update_confluence_pages.py')
    client = publisher.confluence_client()
    client.timeout = 30
    parent = client.get_page_by_id(PARENT, expand='version,body.storage,ancestors')
    assert parent['version']['number'] == args.expected_parent_version, 'Reconcile a changed parent first'
    assert not re.search('manual[ -]discussion', parent['body']['storage']['value'], re.I)
    if not creating:
        assert args.expected_child_version
        existing = client.get_page_by_id(child[1]['confluence']['page_id'], expand='version')
        assert existing['version']['number'] == args.expected_child_version, 'Reconcile a changed child first'
    jobs = [child]
    for path, meta, body in jobs:
        result = publisher.update_document(client, path, meta, body, revision, True, creating)
        saved = client.get_page_by_title('DNBU', meta['confluence']['title'], expand='version,body.storage,ancestors')
        pid = str(saved['id'])
        receipt['results'].append({'id': meta['id'], 'page_id': pid, 'result': result,
                                   'version': saved['version']['number']})
        (OUT / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        if creating:
            # Stamp the creation with the same source revision in native history.
            client.update_page(pid, saved['title'], saved['body']['storage']['value'],
                parent_id=PARENT, representation='storage',
                version_comment=publisher.publication_version_comment(meta, revision))
            saved = client.get_page_by_id(pid, expand='version,body.storage,ancestors')
        actual = saved['body']['storage']['value']
        expected_parent = meta['confluence']['parent_page_id']
        assert str(saved['ancestors'][-1]['id']) == expected_parent
        assert revision in actual and meta['id'] in actual and 'change-history' in actual
        if meta['id'] == 'SPEC-SEI-040':
            assert actual.count('ac:name="html"') == 11
            assert '#666666' in actual and '#1565C0' in actual
        receipt['results'][-1].update(version=saved['version']['number'], verified=True,
            url='https://confluence.sage.com/pages/viewpage.action?pageId=' + pid)
    assert client.get_page_by_id(PARENT, expand='version')['version']['number'] == args.expected_parent_version
    receipt.update(live_publication=True, review=review)
    (OUT / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))

if __name__ == '__main__':
    main()
