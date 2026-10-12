"""Build the onboarding sequences and the separate sending preview.

SVG and editable Draw.io use the same scene. Local Chromium renders PNGs and
checks text bounds. All provider calls and service allocations remain logical.
"""
from pathlib import Path
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/diagrams'
W = 1800
XS = [135 + i * 255 for i in range(7)]
FONT = 'Arial, sans-serif'


class Sequence:
    def __init__(self, slug, title, subtitle, source, participants):
        self.slug, self.title, self.subtitle, self.source = slug, title, subtitle, source
        self.participants = participants
        self.scene, self.messages, self.frames = [], [], []
        self.y = 290
        self.frame_depth = 0

    def band(self, title):
        self.y += 12
        self.scene.append(('band', 28, self.y, W - 56, 36, title))
        self.y += 125

    def msg(self, a, b, title, ref='', kind='call'):
        self.messages.append((a, b, self.y, title, ref, kind))
        self.y += 90

    def note(self, a, b, text, ref='', kind='note'):
        x = XS[a] - 105
        width = XS[b] - XS[a] + 210
        lines = textwrap.wrap(text, max(22, int((width - 28) / 8.5)))
        h = 24 + len(lines) * 23 + (22 if ref else 0)
        self.scene.append((kind, x, self.y - 40, width, h, text, ref))
        self.y += h + 55

    def start_frame(self, label):
        top = self.y - 48
        self.y += 70
        depth = self.frame_depth
        self.frame_depth += 1
        return (top, label, depth)

    def end_frame(self, frame):
        top, label, depth = frame
        self.frame_depth -= 1
        x = 24 + depth * 16
        self.frames.append((x, top, W - 2 * x, self.y - top - 28, label))
        self.y += 16

    def divider(self, label):
        self.scene.append(('divider', 25, self.y - 30, W - 50, 30, label))
        self.y += 80

    def write(self, notes):
        bottom = self.y + 5
        h = int(bottom + 178)
        svg = ET.Element('svg', {'xmlns': 'http://www.w3.org/2000/svg',
            'width': str(W), 'height': str(h), 'viewBox': f'0 0 {W} {h}',
            'role': 'img', 'aria-label': self.title})
        ET.SubElement(svg, 'title').text = self.title
        ET.SubElement(svg, 'desc').text = self.subtitle + ' ' + ' '.join(notes)
        ET.SubElement(svg, 'rect', width=str(W), height=str(h), fill='white')
        mx = ET.Element('mxfile', host='app.diagrams.net', type='device', version='24.7.17')
        d = ET.SubElement(mx, 'diagram', id=self.slug, name=self.title)
        g = ET.SubElement(d, 'mxGraphModel', page='1', pageWidth=str(W), pageHeight=str(h))
        r = ET.SubElement(g, 'root')
        ET.SubElement(r, 'mxCell', id='0')
        ET.SubElement(r, 'mxCell', id='1', parent='0')
        count = 0

        def cell(value, style, x, y, width, height, key=None, link=None):
            nonlocal count
            count += 1
            owner = r
            ident = key or f'cell-{count}'
            if link:
                owner = ET.SubElement(r, 'object', id=ident, label=value, link=link)
                attrs = {}
            else:
                attrs = {'id': ident, 'value': value}
            c = ET.SubElement(owner, 'mxCell', **attrs, parent='1', vertex='1', style=style)
            ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(width),
                          height=str(height), attrib={'as': 'geometry'})

        def text(x, y, value, size=17, color='#222222', center=False, key=None):
            lines = value.split('\n')
            width = max(12, max(len(v) for v in lines) * size * .58 + 12)
            for j, line in enumerate(lines):
                ET.SubElement(svg, 'text', {'x': str(x), 'y': str(y + j * (size + 5)),
                    'font-family': FONT, 'font-size': str(size), 'fill': color,
                    'text-anchor': 'middle' if center else 'start'}).text = line
            cell(value, f'text;html=0;whiteSpace=wrap;align={"center" if center else "left"};'
                 f'verticalAlign=top;fontSize={size};fontColor={color};spacing=0;',
                 x - width / 2 if center else x, y - size, width,
                 len(lines) * (size + 5) + 5, key=key)

        def rect(x, y, width, height, fill='#f6f6f6', stroke='#aaaaaa', dashed=False):
            attrs = dict(x=str(x), y=str(y), width=str(width), height=str(height),
                         fill=fill, stroke=stroke, rx='4')
            if dashed:
                attrs['stroke-dasharray'] = '6 4'
            ET.SubElement(svg, 'rect', attrs)
            cell('', f'rounded=1;arcSize=6;fillColor={fill};strokeColor={stroke};'
                 + ('dashed=1;' if dashed else ''), x, y, width, height)

        def edge(points, kind='call', key=None):
            nonlocal count
            color = '#555555'
            attrs = {'d': 'M ' + ' L '.join(f'{x},{y}' for x, y in points),
                     'fill': 'none', 'stroke': color, 'stroke-width': '1.8'}
            if kind in ('reply', 'lifeline'):
                attrs['stroke-dasharray'] = '6 5'
            ET.SubElement(svg, 'path', attrs)
            if kind != 'lifeline':
                a, b = points[-2:]
                dx, dy = b[0] - a[0], b[1] - a[1]
                length = (dx * dx + dy * dy) ** .5
                ux, uy = dx / length, dy / length
                p1 = (b[0] - 10 * ux + 5 * uy, b[1] - 10 * uy - 5 * ux)
                p2 = (b[0] - 10 * ux - 5 * uy, b[1] - 10 * uy + 5 * ux)
                arrow = f'M {p1[0]},{p1[1]} L {b[0]},{b[1]} L {p2[0]},{p2[1]}'
                if kind == 'call':
                    arrow += ' Z'
                ET.SubElement(svg, 'path', {'d': arrow, 'fill': color if kind == 'call' else 'none',
                    'stroke': color, 'stroke-width': '1.8'})
            count += 1
            c = ET.SubElement(r, 'mxCell', id=key or f'edge-{count}', edge='1', parent='1',
                style='edgeStyle=none;rounded=0;strokeColor=#555555;'
                + ('endArrow=none;dashed=1;' if kind == 'lifeline' else
                   f'endArrow={"block" if kind == "call" else "open"};'
                   + ('dashed=1;' if kind == 'reply' else '')))
            geom = ET.SubElement(c, 'mxGeometry', relative='1', attrib={'as': 'geometry'})
            ET.SubElement(geom, 'mxPoint', x=str(points[0][0]), y=str(points[0][1]), attrib={'as': 'sourcePoint'})
            ET.SubElement(geom, 'mxPoint', x=str(points[-1][0]), y=str(points[-1][1]), attrib={'as': 'targetPoint'})
            array = ET.SubElement(geom, 'Array', attrib={'as': 'points'})
            for x, y in points[1:-1]:
                ET.SubElement(array, 'mxPoint', x=str(x), y=str(y))

        text(28, 42, self.title, 28)
        text(28, 75, self.subtitle, 17)
        text(28, 105, 'Proposed logical sequence · Participants are responsibility groups; actual service placement and contracts remain open.', 15, '#555555')
        text(28, 132, 'Solid filled arrow: request · Dashed open arrow: response · Solid open arrow: notification · Time runs down.', 15, '#555555')
        if self.slug.startswith('spain-onboarding-'):
            text(28, 149, 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required · opt: optional group · alt: alternatives', 12, '#555555')
        for x, y, width, height, label in self.frames:
            rect(x, y, width, height, 'none', '#777777')
        for i, (x, name) in enumerate(zip(XS, self.participants)):
            edge([(x, 246), (x, bottom)], 'lifeline', key=f'participant-{i}-lifeline')
            rect(x - 113, 158, 226, 88, '#e8e8e8', '#555555')
            lines = name.split('\n')
            text(x, 184, '\n'.join(lines), 15, center=True, key=f'participant-{i}-label')
        # Frame headers cover lifelines so lines cannot cross their wording.
        for x, y, width, height, label in self.frames:
            rect(x, y, width, 31, '#f1f1f1', '#777777')
            text(x + 12, y + 22, label, 15)
        for entry in self.scene:
            kind, x, y, width, height, label, *extra = entry
            if kind == 'band':
                rect(x, y, width, height, '#444444', '#444444')
                text(x + 12, y + 25, label, 18, '#ffffff')
            elif kind == 'divider':
                edge([(x, y), (x + width, y)], 'lifeline')
                rect(x + 6, y + 5, width - 12, 29, 'white', 'none')
                text(x + 14, y + 25, label, 15)
            else:
                rect(x, y, width, height, '#f7f7f7' if kind == 'note' else '#ededed', '#888888', dashed=kind == 'exception')
                lines = textwrap.wrap(label, max(22, int((width - 28) / 8.5)))
                text(x + 14, y + 25, '\n'.join(lines), 17)
                if extra and extra[0]:
                    text(x + 14, y + height - 12, extra[0], 12, '#666666')
        for n, (a, b, y, title, ref, kind) in enumerate(self.messages, 1):
            xa, xb = XS[a], XS[b]
            width = abs(xb - xa) - 28
            label = f'{n:02d}  {title}'
            if a == b:
                points = [(xa, y), (xa + 90, y), (xa + 90, y + 22), (xa, y + 22)]
                lines = textwrap.wrap(label, 44)
                assert len(lines) <= 2, label
                text(xa + 16, y - 42, '\n'.join(lines), 17)
                if ref:
                    text(xa + 16, y - 12, ref, 12, '#666666')
            else:
                points = [(xa, y), (xb, y)]
                lines = textwrap.wrap(label, max(22, int(width / 8.5)))
                assert len(lines) <= 2, (label, lines)
                # Message labels sit on white backing above, never on the arrow.
                tx = (xa + xb) / 2
                ty = y - 18 - (len(lines) - 1) * 22 - (17 if ref else 0)
                rect(min(xa, xb) + 8, ty - 18, abs(xb - xa) - 16,
                     len(lines) * 22 + (17 if ref else 0) + 4, 'white', 'none')
                text(tx, ty, '\n'.join(lines), 17, center=True)
                if ref:
                    text(tx, y - 12, ref, 12, '#666666', center=True)
            edge(points, kind, key=f'message-{n:02d}')
        rect(24, bottom + 18, W - 48, 144, '#f4f4f4', '#aaaaaa')
        text(40, bottom + 43, 'Scope and interpretation', 17)
        for i, note in enumerate(notes):
            text(40, bottom + 70 + i * 24, note, 15, '#444444')
        cell('Source specification', 'text;html=0;align=right;fontSize=12;',
             W - 240, bottom + 140, 190, 20, link=self.source)
        ET.indent(mx)
        base = OUT / self.slug
        base.with_suffix('.svg').write_text(ET.tostring(svg, encoding='unicode'))
        base.with_suffix('.drawio').write_text(ET.tostring(mx, encoding='unicode', xml_declaration=True))
        return base.with_suffix('.svg')


def onboarding_participants(private=False):
    return [
        'ERP / product', 'Global API\nProduct-facing contract',
        'Domain Service -\nE-Invoice Service\nSetup coordination',
        'Domain Service -\nOther Services\nIdentity / policy',
        'Domain Service -\nOther Services\nTax / certificate capability',
        'Domain Service -\nOther Services\nConnection / route / adapters',
        'Public / private platforms\n' + ('Private provider' if private else 'Public platform')]


def setup_start(s):
    s.band('1 · Common · Capture requested functions; acknowledge saved request')
    s.msg(0, 1, 'Capture requested functions', 'ONB-01 · ONB-INT-01')
    s.msg(1, 2, 'Pass authenticated, scoped request', 'Tenant access and supported capability')
    s.note(2, 3, 'Save the work item, request key and input digest. A repeated key with the same input returns the existing item; changed input conflicts.', 'ONB-01 · ONB-D01')
    s.msg(2, 1, 'Return saved item and version', 'Receipt; checks may remain pending', 'reply')
    s.msg(1, 0, 'Acknowledge request receipt', 'Receipt is not readiness', 'reply')
    s.band('2 · Common · Check business identity and authority; assess current setup')
    s.msg(2, 3, 'Check business identity and authority', 'ONB-02 · ONB-INT-02')
    s.msg(3, 2, 'Return NIF and authority evidence', 'Business NIF; caller identity; scoped grant', 'reply')
    s.note(2, 4, 'If authority is missing, expired or unknown, stop affected checks. Save the reason and required action. Return the scoped result through ONB-11.', 'ONB-02 · Main path below assumes authority passed', 'exception')
    s.msg(2, 5, 'Assess current setup', 'ONB-10 · ONB-INT-10')
    s.msg(5, 2, 'Return versions, freshness and gaps', 'Customer statements are not proof', 'reply')
    s.note(2, 5, 'Record the per-function plan. Reuse only valid matching evidence. A failed or incomplete lookup remains unknown; it does not prove no existing setup. Valid unchanged functions need no new external work.', 'ONB-10 · ONB-D10')


def access_and_trust(s, activity):
    s.band('3 · Common · Check access and trust requirements')
    s.msg(2, 3, 'Check access and trust requirements', f'{activity} · ONB-INT-03 · Resolve policy')
    s.msg(3, 2, 'Return credential requirements', 'Actor, purpose, environment, policy version', 'reply')
    s.note(2, 5, 'NOT_REQUIRED needs approved policy evidence. UNDETERMINED blocks dependent work. Keep business NIF, caller authentication and action authority separate. Evaluate each access or signing purpose separately.', f'{activity} · ONB-D02/03')
    f = s.start_frame('opt · Conditional · Certificate required; obtain current readiness or refresh missing/stale evidence')
    s.msg(2, 4, 'Check required certificate readiness', f'{activity} · ONB-INT-03 · SPEC-001 CERT-05')
    s.note(3, 5, 'The qualified Tax/certificate capability resolves authorised existing references and validates suitability. Confirm the subject or authorised representative, purpose, role, environment, source/material version, validity and effective grant. It owns certificate controls; E-Invoice Service receives no key bytes.', 'SPEC-001 CERT-03/04/05 · Source and execution owner require ONB-Q06')
    s.msg(4, 2, 'Return scoped readiness and reference', 'Evidence, source/version, recheck, action owner', 'reply')
    a = s.start_frame('alt · Conditional · Valid existing certificate / confirmed problem / unavailable or ambiguous evidence')
    s.note(2, 5, 'Valid existing certificate: reuse its protected reference and current scoped decision. No repeat upload. This decision does not perform authentication or sign an invoice.', f'{activity} · ONB-D04')
    s.divider('Confirmed missing, expired, revoked or unsuitable required certificate')
    s.note(2, 5, 'Hold dependent work. Return the confirmed reason and correction owner through ONB-11. The approved SPEC-001 process supplies replacement or corrected evidence. Recheck the affected parent gate.', 'ONB-08 · SPEC-004 OFR-03/08 · No automatic signer change', 'exception')
    s.divider('Unavailable, stale, ambiguous or unqualified source contract')
    s.note(2, 5, 'Keep readiness unconfirmed. Do not infer missing material or request another upload. SPEC-004 permits only qualified safe-read retry or owned escalation. Resume this check after reliable evidence returns.', 'ONB-08 · SPEC-004 OFR-02/04/07/08 · No mutation inferred', 'exception')
    s.end_frame(a)
    s.end_frame(f)
    s.note(2, 5, 'The main path continues only when the verified business NIF, required certificate readiness and effective action authority pass. Failed or unknown checks return owned actions; independently valid functions remain intact.', f'{activity} · Credential checks precede dependent platform operations')


def setup_result(s, private=False):
    s.band('5 · Common · Return results and required actions')
    s.note(2, 5, 'Save check results, evidence, limitations, recheck conditions and next action owner before notification. Keep setup, readiness and independently evidenced activation separate.', ('ONB-06' if private else 'ONB-04') + ' · ONB-D03 / ONB-D11')
    s.msg(2, 1, 'Publish saved item change', 'ONB-INT-09 · Repeats can occur', 'event')
    s.msg(1, 0, 'Notify product if supported', 'Notification transport remains proposed', 'event')
    s.note(0, 2, 'The ERP can read the result after receipt, on notification or after a missed notification. Each read rechecks access; a notification is not the result itself.', 'ONB-11 · ONB-INT-11')
    s.msg(0, 1, 'Get current work-item result', 'Item reference / version')
    s.msg(1, 2, 'Read authorised current result', 'ONB-11 · ONB-INT-11')
    s.msg(2, 1, 'Return results and required actions', 'ONB-11 · Each function; activation separate', 'reply')
    s.msg(1, 0, 'Show result and action owner', 'Readiness does not mean active exchange', 'reply')


def onboarding():
    s = Sequence('spain-onboarding-public-setup-sequence',
        'Spain onboarding · Connect an existing public service',
        'ONB-S02 example · Public detail: ONB-S01/02/04/05/07 · Shared checks, certificate readiness and authoritative result.',
        '../../specs/SPEC-SEI-002-onboarding-solution-specification.md', onboarding_participants())
    setup_start(s)
    access_and_trust(s, 'ONB-03')
    s.band('4 · Scenario-specific · Check public setup requirements; record public check results')
    f = s.start_frame('opt · Conditional · Run only missing or stale public checks supported by the selected contract')
    s.msg(2, 5, 'Check the public connection', 'ONB-03 · ONB-INT-04')
    s.msg(5, 6, 'Read required capability evidence', 'Only if a qualified external read exists')
    s.msg(6, 5, 'Return observed evidence or read error', 'Source and meaning from selected contract', 'reply')
    s.msg(5, 2, 'Return check result and evidence', 'Failed read is not external absence', 'reply')
    s.end_frame(f)
    s.note(2, 5, 'Record public check results before calculating readiness. An uncertain read returns a limitation. This example creates no registration, receiving-point publication or route activation.', 'ONB-04 · ONB-08 when recovery is required')
    setup_result(s)
    return s.write([
        'Logical asynchronous example for external checks; direct requests may finish synchronously when every check is local.',
        'This example uses qualified reads. It creates no external registration, receiving-point publication or route activation.',
        'If another qualified journey can cause an external effect, ONB-08 / SPEC-SEI-004 reconcile the original operation first.',
        'Source: SPEC-SEI-002; timing pattern: PRD-SEI-101/104. Actual API mapping, policy and service ownership remain open.'])


def onboarding_private():
    s = Sequence('spain-onboarding-private-setup-sequence',
        'Spain onboarding · Connect a private provider',
        'ONB-S03 example · Private detail: ONB-S01/03/04/05/06/07 · Account binding, shared trust checks and conditional activation.',
        '../../specs/SPEC-SEI-002-onboarding-solution-specification.md', onboarding_participants(private=True))
    setup_start(s)
    s.band('2a · Scenario-specific · Configure missing provider settings')
    f = s.start_frame('opt · Conditional · Selected private function needs account binding or missing configuration')
    s.msg(2, 5, 'Configure missing provider settings', 'ONB-05 · ONB-INT-05')
    s.msg(5, 2, 'Return configuration and version', 'Existing account; no activation implied', 'reply')
    s.note(2, 5, 'Bind the existing provider account with permission. Keep the provider unless a supported change was requested. New enrolment, subscription or publication needs a contract requirement and separate authority; configure only missing settings.', 'ONB-05 · External changes require saved intent and recovery controls')
    s.end_frame(f)
    access_and_trust(s, 'ONB-06')
    s.band('4 · Scenario-specific · Check private functions; activate only when required')
    f = s.start_frame('opt · Conditional · Run only required missing or stale provider checks')
    s.msg(2, 5, 'Check selected private functions', 'ONB-06 · ONB-INT-06')
    s.msg(5, 6, 'Observe required provider state', 'Qualified sending / receiving / status contract')
    s.msg(6, 5, 'Return observed state or uncertainty', 'Source, version and freshness', 'reply')
    s.msg(5, 2, 'Return per-function check results', 'Configuration does not prove readiness', 'reply')
    s.note(2, 5, 'Inspect current entry-point evidence first. Publish or change only when the plan and contract require it, after saving original intent and operation identity. A possible effect uses ONB-08 / SPEC-004; do not repeat it blindly.', 'ONB-06 · ONB-D06 · A qualified mutation is a separate operation', 'exception')
    s.end_frame(f)
    a = s.start_frame('alt · Conditional · Valid unchanged route / required authorised activation / failed or unknown checks')
    s.note(2, 5, 'Valid unchanged route: retain its current version and evidence. Return the result without a route commit or external change.', 'ONB-10/11 · Confirmation shortcut')
    s.divider('Required initial activation or supported platform change; all prerequisite checks passed')
    s.msg(2, 3, 'Recheck change authority', 'ONB-07 · ONB-INT-02 · Exact scope/time')
    s.msg(3, 2, 'Return current authority decision', 'Unknown or denied stops activation', 'reply')
    s.note(2, 5, 'Continue only with current readiness, qualified external observations, effective authority, the expected route version and an approved boundary. Private A to Private B stays gated by SPEC-014 and the product decision.', 'ONB-07 · SPEC-014 SPC-04')
    s.msg(2, 5, 'Activate the authorised route', 'ONB-07 · ONB-INT-07 · Version and boundary')
    s.msg(5, 2, 'Return observed activation or conflict', 'No activation claim without owning evidence', 'reply')
    s.note(2, 5, 'Keep earlier invoice context and in-flight bindings. Release old access and dependencies only at separate approved gates. A post-cutover failure opens an owned restoration case.', 'ONB-09 · SPEC-014 SPC-08')
    s.divider('Failed or unknown checks, conflict or possible external effect')
    s.note(2, 5, 'Hold unsafe dependent work and return the owner and next action. Preserve independently valid functions. SPEC-004 resolves the original operation and resumes its exact parent gate; recovered success cannot commit a route.', 'ONB-08 · SPEC-004 OFR-01–08', 'exception')
    s.end_frame(a)
    setup_result(s, private=True)
    return s.write([
        'Logical responsibility groups; connector, certificate, records and Routing allocations require owner qualification.',
        'Shared behaviour does not prove implementation reuse. Provider and Spain rules remain selected contract bindings.',
        'Readiness, route activation and invoice outcomes are separate. Signing and use-time rechecks belong to runtime features.',
        'Source: SPEC-SEI-002; recovery: SPEC-SEI-004; protected-source readiness: SPEC-SEI-001. No endpoint is approved here.'])


def sending():
    s = Sequence('spain-invoice-sending-independent-actions-sequence',
        'Spain sending · Recipient delivery and required public copy',
        'One issued invoice · Eligible private recipient route · Example: recipient delivery confirmed; public-copy response lost.',
        '../../specs/SPEC-SEI-007-invoice-sending-solution.md', [
        'ERP / product\nOwns issued invoice', 'Global API\nProduct-facing contract', 'Domain Service -\nE-Invoice Service\nExchange responsibility',
        'Domain Service -\nOther Services\nPolicy / lookup / prepare', 'Domain Service -\nOther Services\nQualified adapters',
        'Public / private platforms\nPrivate recipient platform', 'Public / private platforms\nPublic platform'])
    s.note(0, 3, 'Precondition: the ERP has issued the invoice and frozen its business identity and revision. A draft check cannot authorise sending changed final data.', 'OUT-05/06 · Draft preparation is outside this sequence')
    s.band('1 · Accept exact issued data; qualify the final route and representation')
    s.msg(0, 1, 'Submit exact issued invoice revision', 'OUT-07 · OUT-INT-04')
    s.msg(1, 2, 'Pass scoped final submission', 'Issued identity, revision, input digest and key')
    s.note(2, 3, 'Save final intent and stable exchange identity. Same key and input resume the existing exchange; changed input conflicts. Request receipt is not delivery.', 'OUT-07 · OUT-D01 / OUT-D02')
    s.msg(2, 1, 'Return saved exchange reference', 'Logical intake receipt; not external success', 'reply')
    s.msg(1, 0, 'Return exchange reference and state', 'API transport and exact fields remain open', 'reply')
    s.msg(2, 3, 'Recheck final authority and rules', 'OUT-08 · OUT-INT-02/03')
    s.msg(3, 2, 'Return current checks and obligations', 'Includes conditional public-copy requirement', 'reply')
    s.msg(2, 3, 'Confirm recipient destination', 'OUT-09 · OUT-INT-05')
    s.msg(3, 2, 'Return PRIVATE_READY with evidence', 'Selected scenario; current eligible route', 'reply')
    s.note(2, 4, 'Failed, stale or ambiguous lookup holds dispatch. It cannot select the public recipient route. Final validation or policy failure also stops external actions.', 'OUT-08/09 · Issued-content issues go to ERP resolution', 'exception')
    s.note(2, 4, 'Freeze the qualified plan and route version. Record delivery and PUBLIC_COPY as separate actions, with their own destinations, identities and dependencies.', 'OUT-10 · OUT-INT-06 · Copy exists only if Spain policy requires it')
    s.msg(2, 3, 'Prepare final action representations', 'OUT-11 · OUT-INT-07')
    s.note(3, 4, 'Qualify DTS where transformation is needed. Validate final bytes after transformation; sign or seal only when required. Protected-operation uncertainty must reconcile before repetition.', 'OUT-11 · DTS is a reuse candidate, not proven coverage')
    s.msg(3, 2, 'Return exact bytes, hashes and evidence', 'Preparation failure leaves actions unsubmitted', 'reply')
    s.note(2, 4, 'Save final artefact references and send intent. Before each transmission, save its attempt, payload hash, target, contract version and original correlation.', 'OUT-11/12 · OUT-D06 / OUT-D07')
    s.band('2 · Execute separate actions; expose each result without waiting for the other')
    f = s.start_frame('par · Eligible independent actions; recorded plan dependencies govern dispatch; no assumed order or synchronous join')
    s.msg(2, 4, 'Dispatch recipient delivery action', 'OUT-12 · OUT-INT-08 · Delivery operation ID')
    s.msg(4, 5, 'Deliver planned invoice representation', 'Qualified private-recipient contract')
    s.msg(5, 4, 'Return confirmed delivery evidence', 'Meaning must match this contract milestone', 'reply')
    s.msg(4, 2, 'Return delivery evidence', 'OUT-13 · Delivery action only', 'reply')
    s.note(2, 4, 'Save the recipient result and publish the committed change. Recipient delivery can be visible while the separate public copy is still pending.', 'OUT-13/14 · OUT-INT-10')
    s.divider('Separate operand · Required public-copy action; diagram position does not impose a dependency on delivery')
    s.msg(2, 4, 'Dispatch required PUBLIC_COPY action', 'OUT-12 · OUT-INT-08 · Separate operation ID')
    s.msg(4, 6, 'Submit planned public-copy representation', 'Qualified public-copy contract')
    s.note(4, 6, 'Example exception: no reliable response arrives after possible transmission. The public-copy outcome is unknown; this is not confirmed rejection.', 'OUT-13 · Lost-response scenario', 'exception')
    s.msg(4, 2, 'Return OUTCOME_UNKNOWN for copy', 'Preserve original operation and correlation', 'reply')
    s.note(2, 4, 'Save the unknown copy outcome and publish the partial result. Keep confirmed recipient delivery. Do not resend it or blindly repeat the copy.', 'OUT-13 · OUT-A07 / OUT-A08', 'exception')
    s.end_frame(f)
    s.band('3 · Reconcile only the unknown action; keep independent evidence visible')
    s.msg(2, 4, 'Reconcile original public-copy action', 'OUT-13 · OUT-INT-09')
    s.msg(4, 6, 'Query original operation outcome', 'Only where the selected contract supports it')
    s.msg(6, 4, 'Return authoritative copy evidence', 'Example: confirms the original copy submission', 'reply')
    s.msg(4, 2, 'Return evidenced original outcome', 'No new copy submission', 'reply')
    s.note(2, 4, 'Record the original outcome once and publish the committed change. If no reliable observation is available, retain unknown and open an owned operations case.', 'OUT-13 · OUT-INT-10')
    s.msg(2, 1, 'Publish saved action-result change', 'At least once; consumer deduplicates', 'event')
    s.msg(1, 0, 'Notify or expose current results', 'OUT-14/15 · Authorised read repairs missed updates', 'event')
    s.note(0, 2, 'Show recipient delivery and public-copy progress separately, with evidence and required actions. API receipt, transport acknowledgement and buyer acceptance have different meanings.', 'OUT-14/15 · Lifecycle spec owns later business outcomes')
    return s.write([
        'Selected logical scenario: private recipient delivery plus a required public copy. Public recipient delivery is another scenario.',
        'The par frame shows independent work, not proof of simultaneous transport. The plan defines permitted dependencies and timing.',
        'Spain route and copy rules require qualification. No endpoints, provider query support, deployment boundaries or deadlines are approved.',
        'Source: SPEC-SEI-007; Global API handoff: SPEC-SEI-013. Reconcile an unknown action without repeating a completed action.'])


def render(paths):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': W, 'height': 1000}, device_scale_factor=1)
        page.route('http://**/*', lambda route: route.abort())
        page.route('https://**/*', lambda route: route.abort())
        for path in paths:
            page.goto(path.as_uri())
            failures = page.evaluate('''() => {
                const s=document.querySelector('svg'), v=s.viewBox.baseVal;
                return Array.from(s.querySelectorAll('text')).flatMap(t=>{
                    const b=t.getBBox();
                    return b.x<0 || b.y<0 || b.x+b.width>v.width || b.y+b.height>v.height
                        ? [t.textContent] : [];
                });
            }''')
            assert not failures, (path.name, failures)
            page.locator('svg').screenshot(path=str(path.with_suffix('.png')))
            # Keep visual QA slices outside the repository.
            height = int(ET.parse(path).getroot().get('height'))
            page.set_viewport_size({'width': W, 'height': height})
            for j, y in enumerate(range(0, height, 1000)):
                page.screenshot(path=f'/tmp/{path.stem}-qa-{j}.png',
                    clip={'x': 0, 'y': y, 'width': W, 'height': min(1000, height-y)})
            page.set_viewport_size({'width': 480, 'height': 800})
            page.goto('about:blank')
            page.set_content('<div style="width:100%;overflow-x:auto">'+path.read_text()+'</div>')
            assert page.locator('div').evaluate('(e)=>e.scrollWidth>e.clientWidth')
            page.set_viewport_size({'width': W, 'height': 1000})
            print(f'{path.name}: XML valid, text in bounds, PNG rendered, narrow view scrolls')
        browser.close()


def preview(paths):
    cards = []
    for path in paths:
        title = ET.parse(path).getroot().find('{http://www.w3.org/2000/svg}title').text
        cards.append(f'<section><h2>{title}</h2><p><a href="{path.stem}.drawio">Editable Draw.io</a> · '
                     f'<a href="{path.name}">SVG</a> · <a href="{path.stem}.png">PNG</a></p>'
                     '<div class="sequence-scroll">'+path.read_text()+'</div></section>')
    (OUT / 'spain-onboarding-and-sending-sequence-preview.html').write_text(
        '<div class="spain-sequence-preview"><style>'
        '.spain-sequence-preview{font-family:Arial,sans-serif;color:#222;padding:20px;background:#fff}'
        '.spain-sequence-preview section{margin:28px 0;border:1px solid #ccc;padding:16px}'
        '.spain-sequence-preview .sequence-scroll{overflow-x:auto;width:100%}'
        '.spain-sequence-preview svg{display:block;max-width:none}'
        '</style><h1>Spain onboarding and sending · Sequence diagram trials</h1>'
        '<p>The onboarding sequences support SPEC-SEI-002 and its process diagrams. The sending sequence remains a separate review preview. '
        'Scroll horizontally to inspect the participants.</p>'+''.join(cards)+'</div>')


if __name__ == '__main__':
    paths = [onboarding(), onboarding_private(), sending()]
    render(paths)
    preview(paths)
