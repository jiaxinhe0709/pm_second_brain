"""Build the combined onboarding swimlane; render previews from its Draw.io source.

Use --build-source to regenerate the initial editable layout. Without that flag,
render the maintained Draw.io source only. Native activities belong to swimlanes.
"""
from pathlib import Path
import argparse
import copy
import importlib.util
import tempfile
import xml.etree.ElementTree as ET

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/onboarding-and-connectivity-swimlane'
DOC = '../../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md'
WIDTH, HEIGHT = 3260, 1530
GREEN, PURPLE, GREY = '#e5f4f0', '#f0eafa', '#fafafa'
ANCHORS = {
    '01': '61-onb-01-capture-requested-functions',
    '02': '62-onb-02-check-business-identity-and-authority',
    '03': '65-onb-03-assess-prerequisites',
    '04': '66-onb-04-publish-public-readiness',
    '05': '67-onb-05-configure-private-choice',
    '06': '68-onb-06-prove-private-readiness',
    '07': '69-onb-07-cut-over-new-traffic',
    '08': '610-onb-08-reconcile-and-recover',
    '10': '64-onb-10-assess-current-setup',
    '11': '612-onb-11-return-results-and-required-actions',
}
LANES = [
    ('customer', 'Customer / accountant', 230, 160),
    ('erp', 'ERP / product', 400, 190),
    ('einvoice', 'Domain Service\nE-Invoice Service', 590, 380),
    ('other', 'Domain Service\nOther Services', 980, 180),
    ('platform', 'Public / private platforms', 1170, 160),
]


def build_source():
    mx = ET.Element('mxfile', host='app.diagrams.net', type='device', version='24.7.17')
    page = ET.SubElement(mx, 'diagram', id=BASE.name, name='Customer onboarding and connectivity — detailed swimlane')
    model = ET.SubElement(page, 'mxGraphModel', page='1', pageWidth=str(WIDTH), pageHeight=str(HEIGHT), grid='1', gridSize='10')
    root = ET.SubElement(model, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')
    lane_y = {key: y for key, _, y, _ in LANES}
    nodes, edges = [], []

    def cell(key, label, x, y, w, h, style, parent='1', link=None):
        container = root
        attrs = {'id': key, 'value': label, 'vertex': '1', 'parent': parent, 'style': style}
        if link:
            container = ET.SubElement(root, 'object', id=key, label=label, link=link)
            attrs.pop('id')
            attrs.pop('value')
        c = ET.SubElement(container, 'mxCell', attrs)
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), attrib={'as': 'geometry'})
        return c

    def text(key, label, x, y, w, h, size=17, align='left'):
        return cell(key, label, x, y, w, h, f'text;html=0;whiteSpace=wrap;align={align};fontSize={size};spacing=2;')

    text('title', 'Set up Sage access to the company’s chosen platforms', 28, 15, 3200, 42, 28)
    text('subtitle', 'Follow the ERP / product row from left to right. Each stage requests its checks below and uses their results before continuing.', 28, 65, 3200, 30, 19)
    cell('precondition', 'BEFORE CUSTOMER ONBOARDING · SXS and Tax / Connections Service product integrations are available. SPEC038 §4.',
         240, 115, 2980, 40, f'fillColor={GREY};strokeColor=#bdbdbd;whiteSpace=wrap;html=0;fontSize=17;')
    for key, label, y, h in LANES:
        cell('lane-' + key, label, 20, y, 3220, h,
             f'swimlane;horizontal=0;noLabel=1;startSize=210;html=0;fillColor=#e5e5e5;swimlaneFillColor={GREY};strokeColor=#bdbdbd;')
        cell('lane-' + key + '-label', label, 8, 0, 194, h,
             'text;html=0;whiteSpace=wrap;align=center;fontSize=18;', parent='lane-' + key)
    for i, (x, w, label) in enumerate([
        (240, 600, '1 · REVIEW SETUP AND CHOOSE ACTION'),
        (870, 480, '2 · COMPLETE SHARED CHECKS'),
        (1380, 1050, '3 · COMPLETE PLATFORM SETUP AND CONFIRM ACCESS'),
        (2460, 760, '4 · CONFIRM PLATFORM USE AND SHOW RESULTS'),
    ], 1):
        cell('stage-' + str(i), label, x, 180, w, 40,
             'fillColor=#d8d8d8;strokeColor=none;html=0;whiteSpace=wrap;fontSize=17;')

    def node(key, lane, x, y, title, detail, ids, w=280, h=110, decision=False, optional=False, terminal=False):
        label = title + ('\n\n' + detail if detail else '') + '\n' + ids
        color = GREEN if lane in ('customer', 'erp') else PURPLE
        style = 'rhombus;' if decision else 'rounded=1;arcSize=18;'
        if terminal:
            style = 'rounded=1;arcSize=100;'
        style += f'html=0;whiteSpace=wrap;align=center;fontSize=17;spacing=8;fillColor={color};strokeColor=#555555;strokeWidth=1.5;'
        if optional:
            style += 'dashed=1;dashPattern=6 4;'
        nodes.append((key, label, x-20, y-lane_y[lane], w, h, style, 'lane-'+lane,
                      DOC + '#' + ANCHORS[ids.split('-')[1].split('/')[0]]))

    def edge(key, source, target, start, end, points=(), dashed=False):
        edges.append((key, source, target, start, end, points, dashed))

    # The ERP row carries the journey. Supporting checks return within their stage.
    node('select-business', 'customer', 240, 260, 'Select the business or client', 'Use the existing selection', 'ONB-01', w=270)
    node('choose-action', 'customer', 560, 250, 'Choose the requested action', 'After setup review;\nconfirm functions and environment', 'ONB-01', w=270, h=130)
    node('review-current', 'erp', 240, 435, 'Review current e-invoicing setup', 'Check view permission and SXS mapping; show permitted saved setup', 'ONB-10/11', w=590)
    node('assess-saved', 'einvoice', 400, 650, 'Assess permitted saved setup', 'Qualified lookup; unavailable\ndoes not mean missing setup', 'ONB-10', w=300)
    node('shared-request', 'erp', 910, 435, 'Complete shared checks', 'For the confirmed business/client,\nrequested functions and environment', 'ONB-01/03', w=360)
    node('assess-shared', 'einvoice', 910, 650, 'Assess required shared checks', 'Reuse matching current evidence;\nkeep caller and business distinct', 'ONB-02/03', w=360)
    node('check-shared', 'other', 910, 1015, 'Check shared prerequisites', 'NIF, authority and required credential;\nkeep the checks independent', 'ONB-02/03', w=360)
    node('platform-setup', 'erp', 1410, 435, 'Complete platform setup and confirm access', 'Public and/or private functions · Reuse valid setup; complete only missing, changed or expired work', 'ONB-04/05/06/10', w=990)
    node('public-access', 'einvoice', 1410, 650, 'Confirm or establish\nSage public access', 'Reuse valid evidence;\nqualified checks only for gaps', 'ONB-04/10', w=300, h=130)
    node('private-account', 'einvoice', 1770, 650, 'Account on chosen\nprivate platform?', '', 'ONB-05/10', w=280, decision=True)
    node('private-setup', 'einvoice', 2100, 650, 'Set up or reuse Sage connection', 'Confirmed account;\ncomplete only missing setup', 'ONB-05/10', w=300)
    node('private-access', 'einvoice', 2100, 820, 'Confirm private access', 'Reuse current evidence;\ncheck only missing or stale items', 'ONB-06/10', w=300)
    node('provider-onboarding', 'platform', 1770, 1195, 'Complete provider onboarding', 'No account: qualified process\nor handoff for this business/client', 'ONB-05', w=280, optional=True)
    node('platform-use', 'customer', 2460, 260, 'Start or change\nplatform use?', '', 'ONB-07', w=300, decision=True)
    node('confirm-use', 'customer', 2810, 250, 'Confirm the platform\nchoice and start', 'Enabled scope;\ncurrent permission and readiness', 'ONB-07', w=300, h=130, optional=True)
    node('show-results', 'erp', 2460, 435, 'Show results and next actions', 'Setup / readiness / platform use;\nnext action and owner', 'ONB-11', w=300, terminal=True)
    node('submit-use', 'erp', 2810, 435, 'Submit confirmed platform use', 'Agreed scope and effective start', 'ONB-07', w=300, optional=True)
    node('apply-use', 'other', 2810, 1015, 'Start or change platform use', 'Apply authorised selection;\nkeep earlier-invoice access', 'ONB-07/09', w=300, optional=True)

    edge('select-review', 'select-business', 'review-current', (.5, 1), (135/590, 0))
    edge('request-saved', 'review-current', 'assess-saved', (.5, 1), (.45, 0))
    edge('return-saved', 'assess-saved', 'review-current', (.55, 0), (325/590, 1))
    edge('review-action', 'review-current', 'choose-action', (455/590, 0), (.5, 1))
    edge('action-shared', 'choose-action', 'shared-request', (1, .5), (.5, 0), [(1090, 315)])
    edge('request-shared', 'shared-request', 'assess-shared', (.44, 1), (.44, 0))
    edge('return-shared', 'assess-shared', 'shared-request', (.56, 0), (.56, 1))
    edge('request-prerequisites', 'assess-shared', 'check-shared', (.44, 1), (.44, 0))
    edge('return-prerequisites', 'check-shared', 'assess-shared', (.56, 0), (.56, 1))
    edge('shared-platform', 'shared-request', 'platform-setup', (1, .5), (0, .5))
    edge('request-public', 'platform-setup', 'public-access', (150/990, 1), (.5, 0), dashed=True)
    edge('return-public', 'public-access', 'platform-setup', (.9, 0), (270/990, 1))
    edge('request-private', 'platform-setup', 'private-account', (500/990, 1), (.5, 0), dashed=True)
    edge('account-yes', 'private-account', 'private-setup', (1, .5), (0, .5), dashed=True)
    edge('account-no', 'private-account', 'provider-onboarding', (.5, 1), (.5, 0), dashed=True)
    edge('onboarding-complete', 'provider-onboarding', 'private-setup', (1, .5), (0, .5), [(2080, 1250), (2080, 705)], dashed=True)
    edge('private-setup-access', 'private-setup', 'private-access', (.5, 1), (.5, 0))
    edge('return-private', 'private-access', 'platform-setup', (1, .5), (980/990, 1), [(2420, 875), (2420, 570), (2390, 570)])
    edge('platform-use-decision', 'platform-setup', 'platform-use', (1, .5), (0, .5), [(2440, 490), (2440, 315)])
    edge('use-yes', 'platform-use', 'confirm-use', (1, .5), (0, .5), dashed=True)
    edge('use-no', 'platform-use', 'show-results', (.5, 1), (.5, 0), dashed=True)
    edge('confirm-submit', 'confirm-use', 'submit-use', (.5, 1), (.5, 0), dashed=True)
    edge('submit-apply', 'submit-use', 'apply-use', (.5, 1), (.5, 0), dashed=True)
    edge('apply-results', 'apply-use', 'show-results', (0, .5), (1, .5), [(2780, 1070), (2780, 490)])
    for key, source, target, start, end, points, dashed in edges:
        style = ('edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;endFill=1;'
                 'strokeColor=#555555;strokeWidth=1.5;'
                 f'exitX={start[0]};exitY={start[1]};exitPerimeter=0;'
                 f'entryX={end[0]};entryY={end[1]};entryPerimeter=0;')
        if dashed:
            style += 'dashed=1;dashPattern=6 4;'
        c = ET.SubElement(root, 'mxCell', id=key, source=source, target=target, edge='1', parent='1', style=style)
        g = ET.SubElement(c, 'mxGeometry', relative='1', attrib={'as': 'geometry'})
        if points:
            array = ET.SubElement(g, 'Array', attrib={'as': 'points'})
            for x, y in points:
                ET.SubElement(array, 'mxPoint', x=str(x), y=str(y))
    for args in nodes:
        key, label, x, y, w, h, style, parent, link = args
        cell(key, label, x, y, w, h, style, parent, link)

    for key, label, x, y, w, h in [
        ('request-saved-label', 'Request', 440, 585, 80, 25),
        ('return-saved-label', 'Result', 580, 585, 80, 25),
        ('request-shared-label', 'Request', 970, 585, 85, 25),
        ('return-shared-label', 'Result', 1135, 585, 85, 25),
        ('request-prerequisites-label', 'Request', 970, 875, 85, 25),
        ('return-prerequisites-label', 'Result', 1135, 875, 85, 25),
        ('shared-pass-label', 'Checks passed', 1275, 445, 130, 30),
        ('public-label', 'Public functions', 1410, 595, 140, 30),
        ('public-result-label', 'Result', 1695, 595, 70, 30),
        ('private-label', 'Private functions', 1925, 595, 160, 30),
        ('account-yes-label', 'Yes', 2050, 665, 50, 25),
        ('account-no-label', 'No · new account needed', 1925, 1115, 140, 55),
        ('onboarding-label', 'Onboarding confirmed', 2090, 1180, 260, 25),
        ('private-result-label', 'Result', 2330, 785, 70, 25),
        ('use-yes-label', 'Yes', 2765, 280, 45, 25),
        ('use-no-label', 'No · setup only', 2625, 395, 160, 25),
    ]:
        text(key, label, x, y, w, h, 16)
    text('setup-only-rule', 'Setup only preserves the current selection.\nIf none exists, setup alone activates none.', 2490, 650, 270, 120, 18)
    cell('recovery-note', 'IF ANY STEP FAILS OR REMAINS PENDING · Stop dependent work. Keep independent successful results. Show the limitation, next action and owner. Resume only affected work; check unknown effects before retrying. ONB-08/11.',
         240, 1360, 2980, 60, f'fillColor={GREY};strokeColor=#bdbdbd;whiteSpace=wrap;html=0;align=left;spacing=12;fontSize=18;')
    text('legend', 'Green: customer and ERP steps · Purple: setup and checks · Solid: normal work, requests and results · Dashed: conditional work.', 28, 1440, 3200, 30, 17)
    text('ownership', 'Proposed responsibilities; implementation coverage remains open in SPEC039. Colours do not show readiness or implementation. Phase 1: public access; phases 2–3 add private setup and enabled changes.', 28, 1475, 3200, 30, 16)
    ET.indent(mx)
    BASE.with_suffix('.drawio').write_text(ET.tostring(mx, encoding='unicode', xml_declaration=True) + '\n')


def render():
    """Flatten native lane membership only in a temporary renderer input."""
    source = ET.parse(BASE.with_suffix('.drawio'))
    root = source.find('.//mxGraphModel/root')
    cells = {item.get('id'): item.find('mxCell') if item.tag == 'object' else item for item in root}

    def absolute(key):
        c = cells[key]
        g = c.find('mxGeometry')
        x, y = float(g.get('x', 0)), float(g.get('y', 0))
        if c.get('parent') not in (None, '0', '1'):
            px, py = absolute(c.get('parent'))
            x, y = x+px, y+py
        return x, y

    flattened = copy.deepcopy(source)
    target = flattened.find('.//mxGraphModel/root')
    for item in list(target):
        c = item.find('mxCell') if item.tag == 'object' else item
        if c.get('vertex') != '1':
            continue
        g = c.find('mxGeometry')
        x, y = absolute(item.get('id'))
        g.set('x', str(x))
        g.set('y', str(y))
        c.set('parent', '1')
        if item.get('id') in {'lane-' + lane[0] for lane in LANES}:
            c.set('value', '')
            c.set('style', f'fillColor={GREY};strokeColor=#bdbdbd;')
            strip = copy.deepcopy(c)
            strip.set('id', item.get('id') + '-strip')
            strip.set('style', 'fillColor=#e5e5e5;strokeColor=#bdbdbd;')
            strip.find('mxGeometry').set('width', '210')
            target.insert(list(target).index(item) + 1, strip)

    spec = importlib.util.spec_from_file_location('drawio_preview', ROOT / 'work/build-invoice-sending-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    with tempfile.TemporaryDirectory(prefix='onboarding-preview-') as folder:
        temporary = Path(folder) / BASE.name
        flattened.write(temporary.with_suffix('.drawio'), encoding='unicode')
        renderer.BASE = temporary
        renderer.build()
        svg = ET.parse(temporary.with_suffix('.svg'))
    ns = '{http://www.w3.org/2000/svg}'
    model = source.find('.//mxGraphModel')
    width, height = model.get('pageWidth'), model.get('pageHeight')
    svg.getroot().attrib.update(width=width, height=height, viewBox=f'0 0 {width} {height}')
    svg.find(ns + 'rect').attrib.update(x='0', y='0', width=width, height=height)
    svg.find(ns + 'desc').text = (
        'Detailed customer onboarding swimlane. Four stage bands: review setup and choose action; '
        'complete shared checks; complete public and/or private platform setup and confirm access; '
        'confirm platform use and show results. Native lanes distinguish customer/accountant, '
        'ERP/product, E-Invoice Service, Other Services and external platforms. Both public and '
        'private results return to the ERP platform-setup stage before the common platform-use decision. '
        'Setup alone does not activate a platform. Existing setup and '
        'matching current evidence are reused. Each platform requires its own readiness checks. '
        'Failed or pending steps use the shared recovery note and ONB-08/11. Responsibilities are proposed; implementation '
        'coverage and external contracts remain subject to SPEC039 qualification.')
    # The shared renderer uses rectangular outlines for ellipses and unfilled dashed
    # outlines. Restore those source styles before rasterisation and link activation.
    for item in root:
        c = item.find('mxCell') if item.tag == 'object' else item
        if c.get('vertex') != '1':
            continue
        style = c.get('style', '')
        s = dict(part.split('=', 1) for part in style.split(';') if '=' in part)
        group = svg.find(f".//{ns}g[@id='{item.get('id')}']")
        if group is None:
            continue
        g = c.find('mxGeometry')
        x, y = absolute(item.get('id'))
        w, h = float(g.get('width')), float(g.get('height'))
        if style.startswith('ellipse;'):
            group.remove(group[0])
            group.insert(0, ET.Element(ns + 'ellipse', cx=str(x+w/2), cy=str(y+h/2), rx=str(w/2), ry=str(h/2), fill=s.get('fillColor'), stroke=s.get('strokeColor')))
        elif s.get('dashed') == '1':
            group.insert(0, ET.Element(ns + 'rect', x=str(x), y=str(y), width=str(w), height=str(h), fill=s.get('fillColor', 'white')))
    ET.indent(svg)
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')
    with pymupdf.open(BASE.with_suffix('.svg')) as image:
        with pymupdf.open('pdf', image.convert_to_pdf()) as pdf:
            pdf[0].get_pixmap(alpha=False).save(BASE.with_suffix('.png'))
    for group in svg.iter(ns + 'g'):
        if 'data-source' in group.attrib:
            group.tag = ns + 'a'
            group.set('href', group.attrib.pop('data-source'))
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')
    print('Native swimlane source preserved; SVG and PNG previews refreshed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-source', action='store_true')
    args = parser.parse_args()
    if args.build_source:
        build_source()
    render()
