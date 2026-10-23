"""Verify saved source attribution, macros and rendered companion section links."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = {'923861390': ('SPEC-SEI-037', 1),
         '936509725': ('SPEC-SEI-038', 4),
         '936509735': ('SPEC-SEI-039', 6)}


class RenderedLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.anchors.add(attrs['id'])
        if tag == 'a':
            if attrs.get('name'):
                self.anchors.add(attrs['name'])
            if attrs.get('href'):
                self.links.append(attrs['href'])


def verify(client, revision):
    rendered, records = {}, []
    for pid, (ident, count) in PAGES.items():
        page = client.get_page_by_id(pid, expand='version,body.storage,body.view,ancestors')
        storage = page['body']['storage']['value']
        view = RenderedLinks()
        view.feed(page['body']['view']['value'])
        rendered[pid] = view
        assert ident in storage and revision in storage
        assert ident in page['version'].get('message', '')
        assert revision[:12] in page['version'].get('message', '')
        assert storage.count('ac:name="drawio"') == count
        assert 'change-history' in storage and 'Lifecycle status:</strong> draft' in storage
        assert str(page['ancestors'][-1]['id']) == '837610648'
        records.append({'source_id': ident, 'page_id': pid, 'title': page['title'],
                        'version': page['version']['number'], 'editable_diagrams': count,
                        'version_comment': page['version'].get('message')})
    checked = 0
    for pid, view in rendered.items():
        for href in view.links:
            parts = urlsplit(href)
            if parts.netloc not in {'', 'confluence.sage.com'}:
                continue
            destination = parse_qs(parts.query).get('pageId', [''])[0]
            if destination not in rendered or not parts.fragment:
                continue
            fragment = unquote(parts.fragment)
            assert fragment in rendered[destination].anchors, (pid, destination, fragment)
            checked += 1
    assert checked > 0, 'No rendered section links were checked'
    return {'result': 'passed', 'git_revision': revision, 'pages': records,
            'rendered_section_links_checked': checked,
            'source_ids_revision_comments_draft_status_history_and_parent': 'passed',
            'browser_viewport_inspection': 'not performed'}
