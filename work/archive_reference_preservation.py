"""Check original preservation hashes across the authorised folder relocation."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / 'work/onboarding-and-connectivity-review/archive-relocation.json'
PUBLICATION = ROOT / 'work/onboarding-and-connectivity-review/publication-changes.json'


def assert_preserved(relative, expected):
    receipt = json.loads(RECEIPT.read_text()) if RECEIPT.exists() else {}
    change = receipt.get('files', {}).get(relative)
    if change and change['before_sha256'] == expected:
        target = change['retained_path']
        digest = change['after_sha256']
    else:
        target, digest = relative, expected
    publication = json.loads(PUBLICATION.read_text()) if PUBLICATION.exists() else {}
    approved = publication.get('files', {}).get(target)
    if approved and approved['before_sha256'] == digest:
        digest = approved['after_sha256']
    assert hashlib.sha256((ROOT / target).read_bytes()).hexdigest() == digest, (
        relative, 'source changed beyond recorded archive relocation')
