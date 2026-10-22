"""Verify the authorised archive move without changing source documents."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher


def normalized_body(text, path):
    def link(match):
        target = match[1].strip('<>')
        if '://' in target:
            return match[0]
        relative, separator, fragment = target.partition('#')
        destination = (path.parent / relative).resolve() if relative else path
        value = 'SELF' if destination == path else str(destination.relative_to(ROOT))
        return '](' + value + ('#' + fragment if separator else '') + ')'
    return re.sub(r'\]\((<[^>]+>|[^\s)]+)\)', link, text)


def business_rows(path):
    body = publisher.load_document(path)[1]
    return '\n'.join(line.replace('SEI020', 'SEI021') for line in body.splitlines()
                     if (line.startswith('|') and re.match(r'\|\s*(?:ONB|OFR)-(?:SPFE-|NFR|R|A)', line))
                     or line.startswith('**ONB-R15'))


def validate_archive():
    baseline = json.loads((ROOT / 'work/onboarding-sequence-review/archive-baseline.json').read_text())
    archived = ROOT / baseline['retained_path']
    assert not (ROOT / baseline['former_path']).exists()
    metadata, body = publisher.load_document(archived)
    assert metadata['id'] == 'SPEC-SEI-020' and metadata['status'] == 'draft'
    assert metadata['confluence']['publish'] is False and not metadata['confluence']['page_id']
    assert 'SPEC-SEI-021' in metadata['related']
    retained, notices = re.subn(r'^> \*\*Archived supporting reference\.\*\*[^\n]*\n\n', '', body, flags=re.M)
    assert notices == 1
    digest = hashlib.sha256(normalized_body(retained, archived).encode()).hexdigest()
    assert digest == baseline['technical_body_normalized_sha256'], 'Archived analysis changed beyond links/notice'
    for path, digest in baseline['business_rows_sha256'].items():
        assert hashlib.sha256(business_rows(ROOT / path).encode()).hexdigest() == digest, path
    for path, digest in baseline['immutable_sha256'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    return {
        'archive_location': baseline['retained_path'],
        'archived_020_analysis_unchanged': True,
        'business_rules_and_acceptance_018_019_unchanged': True,
        'publication_configuration_unchanged': True,
        'lifecycle_status_preserved': 'draft',
        'active_review_set': ['SPEC-SEI-018', 'SPEC-SEI-019', 'SPEC-SEI-021'],
        'immutable_sha256': baseline['immutable_sha256'],
    }


if __name__ == '__main__':
    print(json.dumps(validate_archive(), indent=2))
