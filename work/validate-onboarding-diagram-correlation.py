"""Validate the current SPEC-SEI-002 diagram views without network access.

Run with .venv/bin/python work/validate-onboarding-diagram-correlation.py.
This checks document consistency, not implemented provider behaviour. Browser
rendering and the semantic review recorded below are separate checks.
"""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import html
import importlib.util
import re
import struct
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import update_confluence_pages as publisher

SPEC = ROOT / 'specs/archive/SPEC-SEI-002-onboarding-solution-specification.md'
SVG = '{http://www.w3.org/2000/svg}'
PREFIX = r'(?:ONB|OFR|CERT|SPC)-(?:[A-Z]+-)*[A-Z]*'
REF = re.compile(r'\b(' + PREFIX + r')(\d+)((?:(?:/|[–-])\d+)*)')
checks = []


def normal(value):
    return ' '.join((value or '').split())


def references(value):
    result = set()
    for prefix, first, tail in REF.findall(value):
        current = int(first)
        result.add(prefix + first)
        for separator, digits in re.findall(r'([/–-])(\d+)', tail):
            stop = int(digits)
            if separator in ('–', '-'):
                result.update(prefix + str(n).zfill(len(first)) for n in range(current + 1, stop + 1))
            else:
                result.add(prefix + digits)
            current = stop
    return result


def check(name, condition, evidence):
    checks.append((name, bool(condition), evidence))


def definitions(text):
    pattern = r'^(?:\|\s*|\*\*)(' + PREFIX + r'\d+)\b'
    return set(re.findall(pattern, text, re.M))


def load_module(relative, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


metadata, body = publisher.load_document(SPEC)
assets = publisher.drawio_assets(SPEC, body)
views = {}
defined = definitions(body)
for relative in ['specs/SPEC-SEI-001-certificate-management-solution-specification.md',
                 'specs/SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md']:
    defined |= definitions((ROOT / relative).read_text())

for asset in assets:
    editable = ET.parse(asset.source).getroot()
    svg = ET.parse(asset.source.with_suffix('.svg')).getroot()
    objects = list(editable.iter('object'))
    cells = list(editable.iter('mxCell'))
    edges = [cell for cell in cells if cell.get('edge') == '1']
    visible = ' '.join(t.text or '' for t in svg.iter(SVG + 'text'))
    all_text = visible + ' ' + (svg.findtext(SVG + 'desc') or '')
    nodes = {obj.get('id'): obj for obj in objects}
    graph = defaultdict(set)
    labels = {}
    for edge in edges:
        if edge.get('source'):
            graph[edge.get('source')].add(edge.get('target'))
            label_id = 'edge-label-' + edge.get('id').split('-')[-1]
            label = editable.find(".//mxCell[@id='" + label_id + "']")
            labels[edge.get('source'), edge.get('target')] = label.get('value', '') if label is not None else ''
    views[asset.name] = dict(asset=asset, svg=svg, editable=editable, nodes=nodes,
                             graph=graph, labels=labels, text=all_text, refs=references(all_text))
    unknown = references(all_text) - defined
    check(asset.name + ': activity and contract references', not unknown,
          'Every ONB/OFR/CERT/SPC reference has a definition. Missing: ' + ', '.join(sorted(unknown)))
    png = asset.preview.read_bytes()
    png_size = struct.unpack('>II', png[16:24]) if png.startswith(b'\x89PNG\r\n\x1a\n') else None
    check(asset.name + ': companion dimensions',
          png_size == (asset.diagram_width, asset.diagram_height),
          f'SVG and PNG dimensions: {asset.diagram_width} × {asset.diagram_height}.')
    if 'sequence' not in asset.name:
        anchors = list(svg.findall(SVG + 'a'))
        equivalent = len(anchors) == len(objects)
        for obj, anchor in zip(objects, anchors):
            drawn = ' '.join(t.text or '' for t in anchor.findall(SVG + 'text'))
            equivalent &= normal(obj.get('label')) == normal(drawn)
            equivalent &= obj.get('link') == anchor.get('href')
        check(asset.name + ': editable and SVG labels', equivalent,
              'Activity wording, IDs and links match between Draw.io and SVG.')
        dangling = [(e.get('source'), e.get('target')) for e in edges
                    if e.get('source') not in nodes or e.get('target') not in nodes]
        check(asset.name + ': connected endpoints', not dangling,
              'Every process connector refers to existing activities.')
        decisions = [obj.get('id') for obj in objects
                     if 'rhombus;' in obj.find('mxCell').get('style', '')]
        check(asset.name + ': decision alternatives',
              all(len(graph[key]) >= 2 for key in decisions),
              'Every decision has at least two alternatives. The overview permits multiple selected work paths.')
    else:
        editable_text = ' '.join(cell.get('value', '') for cell in cells
                                 if cell.get('style', '').startswith('text;'))
        check(asset.name + ': editable and SVG text',
              Counter(editable_text.split()) == Counter(visible.split()),
              'All rendered sequence wording and references match the editable source.')

names = ['onboarding-scenario-selection-process', 'onboarding-public-readiness-process',
         'onboarding-private-route-process', 'onboarding-client-approval-process',
         'onboarding-portfolio-batch-process', 'spain-onboarding-public-setup-sequence',
         'spain-onboarding-private-setup-sequence']
check('Active view set', set(views) == set(names), 'Five process views and two technical sequence views.')


def direct(name, source, target):
    return target in views[name]['graph'][source]


def path(name, start, end, avoid=()):
    pending, seen = [start], set(avoid)
    while pending:
        node = pending.pop()
        if node in seen:
            continue
        if node == end:
            return True
        seen.add(node)
        pending.extend(views[name]['graph'][node])
    return False


overview, public, private, approval, portfolio, public_sequence, private_sequence = names
for name, source, target in [(public, 'correct', 'record'), (private, 'correct', 'result'),
                             (approval, 'present', 'result')]:
    check(name + ': pending action is visible', direct(name, source, target)
          and 'Pending' in views[name]['labels'][source, target],
          'A pending correction or approval can return ONB-11 without waiting for completion; ONB-A30/35/38.')
check('Public recovery returns to its parent checks',
      direct(public, 'recover', 'plan') and direct(public, 'correct', 'plan')
      and 'Resolved' in views[public]['labels']['recover', 'plan'],
      'Correction and resolution recheck the saved public gate; ONB-03/08 and OFR-I10.')
check('Private recovery cannot bypass readiness and route decisions',
      direct(private, 'recover', 'plan') and 'Resolved' in views[private]['labels']['recover', 'plan']
      and not path(private, 'recover', 'activate', ['plan', 'checks', 'change']),
      'Every route activation after recovery requires the parent checks; ONB-07/08 and OFR-I10.')
check('Private unchanged-route shortcut',
      direct(private, 'change', 'result') and direct(private, 'change', 'activate')
      and direct(overview, 'private', 'result'),
      'Overview and private detail both permit an unchanged route without activation; ONB-R12, ONB-10/11.')
check('Approval verification precedes resumption',
      not path(approval, 'present', 'resume', ['verify', 'effective'])
      and direct(approval, 'evidence', 'resume'),
      'New responses require evidence and effective-authority checks; valid current evidence can skip a new request; ONB-A30/31.')
approval_recovery = views[approval]['nodes']['recover'].get('label', '')
check('Withdrawal does not invent an unknown external effect',
      'only possible unknown effects' in approval_recovery,
      'Withdrawal stops affected new use. Reconciliation applies only to a possible unknown effect; ONB-A33.')
portfolio_recovery = views[portfolio]['nodes']['recover']
recovery_y = float(portfolio_recovery.find('mxCell/mxGeometry').get('y'))
check('Original-effect observation stays with the query owner',
      580 <= recovery_y < 720 and 'Query owner' in portfolio_recovery.get('label', ''),
      'Portfolio observation uses Other Services. Operations receives assigned manual cases; ONB-R15/OFR-R11 and OFR-INT-05/06.')
check('Portfolio items use the same onboarding journey',
      direct(portfolio, 'permitted', 'run') and references(views[portfolio]['nodes']['run'].get('label', ''))
      >= {'ONB-03', 'ONB-04', 'ONB-05', 'ONB-06', 'ONB-07', 'ONB-10'},
      'Each authorised client selects public/private work independently; ONB-A35.')
check('Portfolio cancellation keeps uncertain work separate',
      direct(portfolio, 'hold', 'recover') and direct(portfolio, 'hold', 'aggregate')
      and 'No uncertain effect' in views[portfolio]['labels']['hold', 'aggregate']
      and 'Unresolved effects keep cancellation incomplete' in views[portfolio]['text'],
      'Progress can report an unresolved item; the diagram does not claim final cancellation; ONB-A35/OFR-A08.')

# Inspect sequence authoring scenes without writing or rendering any assets.
sequence_module = load_module('work/build-spain-sequence-diagrams.py', 'correlation_sequences')
sequence_module.Sequence.write = lambda scene, notes: scene
public_scene, private_scene = sequence_module.onboarding(), sequence_module.onboarding_private()
check('Sequences share the same request, authority and assessment prefix',
      [(a, b, title, ref, kind) for a, b, y, title, ref, kind in public_scene.messages[:8]]
      == [(a, b, title, ref, kind) for a, b, y, title, ref, kind in private_scene.messages[:8]],
      'Both sequences use ONB-01 → ONB-02 → ONB-10, matching the overview.')
for name, scene, activity in [(public_sequence, public_scene, 'ONB-03'),
                               (private_sequence, private_scene, 'ONB-06')]:
    refs = [ref for a, b, y, title, ref, kind in scene.messages if title == 'Check required certificate readiness']
    check(name + ': certificate dependency',
          len(refs) == 1 and activity in refs[0] and 'CERT-05' in refs[0],
          f'{activity} consumes SPEC-SEI-001 CERT-05; NIF, authority and certificate decisions remain separate.')
    source_scene_labels = [normal(entry[5]) for entry in scene.scene]
    check(name + ': generated scene matches visible notes',
          all(label in normal(views[name]['text']) for label in source_scene_labels),
          'The checked sequence image contains the current scene notes and alternative outcomes.')
    scene_owners = [participant.replace('\n', ' ') for participant in scene.participants]
    check(name + ': responsibility groups',
          all(any(participant.startswith(prefix) for prefix in ['ERP / product', 'Global API',
              'Domain Service -', 'Public / private platforms']) for participant in scene_owners),
          'Sequence participants match the process responsibility groups; physical deployment remains open.')
check('Public process and sequence do not activate routes',
      not (views[public]['refs'] & {'ONB-05', 'ONB-06', 'ONB-07', 'ONB-09'})
      and not any(title == 'Activate the authorised route' for a, b, y, title, ref, kind in public_scene.messages),
      'Public setup establishes readiness only; ONB-I02 and ONB-R18.')
check('Private sequence establishes trust before provider observations',
      next(y for a, b, y, title, ref, kind in private_scene.messages if title == 'Check required certificate readiness')
      < next(y for a, b, y, title, ref, kind in private_scene.messages if title == 'Observe required provider state')
      and 'Access and trust passed' in views[private]['labels']['checks', 'external'],
      'The detail uses the same access/trust guard before external checks as the private sequence.')
check('Both sequences preserve original-effect reconciliation rules',
      all('empty or failed query is not proof of absence' in views[name]['text']
          and 'Proven absence permits retry only under the qualified contract' in views[name]['text']
          for name in [public_sequence, private_sequence]),
      'The same business, environment and original operation are used; OFR-05/06 and OFR-I03.')
check('Both sequences read the saved authoritative result',
      all(any(title == 'Get current work-item result' and kind == 'call'
              for a, b, y, title, ref, kind in scene.messages) for scene in [public_scene, private_scene]),
      'Receipt and notification are separate from the per-function result; ONB-11/INT-11.')

# Introductions replace the former reading matrices. Their activity references
# must belong to the view or a declared parent/dependency. The graph, guard and
# detailed-rule checks above remain unchanged.
images = list(re.finditer(r'!\[[^\]]*\]\(([^)]+\.svg)\)', body))
for index, match in enumerate(images):
    introduction = body[:match.start()].rstrip().rsplit('\n\n', 1)[-1]
    following = body[match.end():].lstrip().split('\n\n', 2)
    companion_links, next_block = following[:2]
    name = Path(match.group(1)).stem
    intro_refs = references(introduction)
    inherited = {'ONB-08'} if name == overview else set()
    if name == public:
        inherited.add('CERT-05')
    unmatched = intro_refs - views[name]['refs'] - inherited
    check(name + ': introduction correlation',
          20 <= len(introduction.split()) <= 100 and bool(intro_refs)
          and not unmatched and not introduction.startswith(('|', '#', '**'))
          and '.drawio)' in companion_links and not next_block.startswith('|'),
          'A short introduction precedes the diagram; its activity IDs match the view '
          'or its named dependency. Companion links remain; no reading matrix follows. '
          'Unmatched: ' + ', '.join(sorted(unmatched)))

correlation_rows = []
for number in range(1, 14):
    activity = 'ONB-' + str(number).zfill(2)
    cells = []
    for name in names:
        if activity in views[name]['refs']:
            value = 'Shown'
        elif name == portfolio and activity == 'ONB-09':
            value = 'Via private setup'
        elif name in (public_sequence, private_sequence) and activity in ('ONB-12', 'ONB-13'):
            value = 'Parent approval / item flow'
        else:
            value = 'Outside this view'
        cells.append('<td>' + value + '</td>')
    correlation_rows.append('<tr><th>' + activity + '</th>' + ''.join(cells) + '</tr>')

findings = [
    ('Pending correction visibility', 'Public/private correction paths returned only after correction.',
     'Added ONB-11 pending-action branches; completion still requires the affected check.'),
    ('Pending approval visibility', 'The approval diagram returned a result only after a response or later failure.',
     'Added a pending-action return while waiting. Verification still precedes resumption.'),
    ('Observation responsibility', 'Portfolio original-effect observation appeared in Operations/support.',
     'Moved it to the query-owner responsibility group; manual cases still go to Operations.'),
    ('Withdrawal condition', 'The diagram wording could imply every withdrawal requires reconciliation.',
     'Stop new use for every effective withdrawal; reconcile only possible unknown effects.'),
    ('Shared sequence references', 'A shared protected-operation note used both public and private parent IDs.',
     'Use ONB-03/08 in the public sequence and ONB-06/08 in the private sequence.'),
]
rows = ''.join('<tr><td>' + ('Pass' if passed else 'FAIL') + '</td><td>' + html.escape(name)
               + '</td><td>' + html.escape(evidence) + '</td></tr>' for name, passed, evidence in checks)
finding_rows = ''.join('<tr><td>' + html.escape(name) + '</td><td>' + html.escape(before)
                       + '</td><td>' + html.escape(after) + '</td></tr>' for name, before, after in findings)
failed = [name for name, passed, evidence in checks if not passed]
result = ('Pass' if not failed else 'FAIL') + f': {len(checks)-len(failed)}/{len(checks)} checks'
fingerprint = hashlib.sha256(SPEC.read_bytes()).hexdigest()
style = 'body{font:15px/1.5 Arial;color:#172b4d;margin:24px}main{max-width:1500px}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px}th,td{padding:9px;border:1px solid #ccd1d8;text-align:left;vertical-align:top}th{background:#f4f5f7}.limit{background:#fff7d6;padding:12px}a{color:#0052cc}'
report = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Onboarding diagram correlation validation</title><style>' + style + '</style></head><body><main><h1>Onboarding diagram correlation validation</h1><p><strong>' + result + '</strong>. Current local SPEC-SEI-002, 20 October 2026.</p><p><a href="../specs/archive/SPEC-SEI-002-onboarding-solution-specification.md">Canonical spec</a> · <a href="onboarding-integrated-diagrams-preview.html">Diagrams and introductions</a> · <a href="onboarding-consolidation-validation.html">Preservation checks</a></p><p class="limit">This validates consistency across the seven document views, their introductions and the detailed ONB/OFR rules. The seven former matrix checks now validate introduction scope and placement; all graph, guard, recovery and rule checks remain. Semantic review covers the listed conditions and outcomes. It does not execute product/provider behaviour, approve service boundaries or close implementation gates. Visual rendering is checked separately.</p><h2>Findings corrected</h2><table><thead><tr><th>Concern</th><th>Before</th><th>Correction</th></tr></thead><tbody>' + finding_rows + '</tbody></table><h2>Activity correlation</h2><p>Shown means the view explicitly references the activity. Parent/delegated coverage is named. Views have different purposes; they do not need identical node sets.</p><div class="scroll"><table><thead><tr><th>Activity</th><th>Overview</th><th>Public process</th><th>Private process</th><th>Approval</th><th>Portfolio</th><th>Public sequence</th><th>Private sequence</th></tr></thead><tbody>' + ''.join(correlation_rows) + '</tbody></table></div><h2>Checks</h2><table><thead><tr><th>Result</th><th>Check</th><th>Evidence and rule</th></tr></thead><tbody>' + rows + '</tbody></table></main></body></html>'
report = report.replace('<h2>Findings corrected</h2>', '<p>Spec SHA-256: <code>' + fingerprint
                        + '</code>. Rerun the validator after source changes.</p><h2>Findings corrected</h2>')
(ROOT / 'work/onboarding-diagram-correlation-validation.html').write_text(report)
print(result)
for name in failed:
    print('FAIL:', name)
sys.exit(bool(failed))
