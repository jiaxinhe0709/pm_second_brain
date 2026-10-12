"""Build the scenario diagrams for SPEC-SEI-002/004 without external calls.

Use the established grey responsibility lanes and whitespace router. Generate
editable Draw.io and SVG from one description. PNGs use a local browser render.
"""
from pathlib import Path
import importlib.util
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/diagrams'
shared_spec = importlib.util.spec_from_file_location(
    'shared_diagrams', ROOT / 'work/build-shared-platform-connectivity-diagrams.py')
shared = importlib.util.module_from_spec(shared_spec)
shared_spec.loader.exec_module(shared)
WIDTH, HEIGHT = 2340, 1120
shared.WIDTH, shared.HEIGHT = WIDTH, HEIGHT
LANES = shared.LANES
LEGEND = 'Solid: shared handoff · Dashed: conditional work or recovery · Diamond: decision · Darker grey: recovery'
ONB = '../../specs/SPEC-SEI-002-onboarding-solution-specification.md'
OFR = '../../specs/SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md'


def node(key, col, lane, title, activity, note='', kind='flow'):
    return dict(key=key, col=col, lane=lane, title=title, activity=activity,
                note=note, kind=kind)


def edge(source, target, kind='flow', points=None):
    return dict(source=source, target=target, kind=kind, points=points)


def build(slug, title, description, nodes, edges, spec=ONB):
    pos = {n['key']: (240 + n['col'] * 295, 178 + n['lane'] * 140, 260, 104)
           for n in nodes}
    assert len(pos) == len(nodes)
    for x, y, w, h in pos.values():
        assert x + w < WIDTH and y + h < 1000
    paths = [e['points'] or shared.route(e, pos) for e in edges]
    svg = ET.Element('svg', {
        'xmlns': 'http://www.w3.org/2000/svg', 'width': str(WIDTH),
        'height': str(HEIGHT), 'viewBox': f'0 0 {WIDTH} {HEIGHT}',
        'role': 'img', 'aria-label': title})
    ET.SubElement(svg, 'title').text = title
    ET.SubElement(svg, 'desc').text = description
    ET.SubElement(svg, 'rect', width=str(WIDTH), height=str(HEIGHT), fill='white')

    def text(x, y, value, size=15, anchor='start', parent=svg, color='#222222'):
        ET.SubElement(parent, 'text', {
            'x': str(x), 'y': str(y), 'font-family': 'Arial, sans-serif',
            'font-size': str(size), 'text-anchor': anchor, 'fill': color}).text = value

    text(28, 35, title, 24)
    for i, line in enumerate(textwrap.wrap(description, 190)):
        text(28, 65 + i * 20, line)
    text(28, 120, 'Proposed design · ' + LEGEND, 14)
    for i, lane in enumerate(LANES):
        y = 160 + i * 140
        ET.SubElement(svg, 'rect', x='20', y=str(y), width=str(WIDTH - 40),
                      height='140', fill='#fafafa', stroke='#aaaaaa')
        ET.SubElement(svg, 'rect', x='20', y=str(y), width='200',
                      height='140', fill='#e5e5e5', stroke='#aaaaaa')
        lines = textwrap.wrap(lane, 23)
        for j, line in enumerate(lines):
            text(120, y + 75 - (len(lines) - 1) * 10 + j * 20,
                 line, 15, 'middle')
    for e, points in zip(edges, paths):
        attrs = {'d': 'M ' + ' L '.join(f'{x:g},{y:g}' for x, y in points),
                 'fill': 'none', 'stroke': '#555555', 'stroke-width': '1.8'}
        if e['kind'] != 'flow':
            attrs['stroke-dasharray'] = '6 4'
        ET.SubElement(svg, 'path', attrs)
        a, b = points[-2:]
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = (dx * dx + dy * dy) ** .5
        ux, uy = dx / length, dy / length
        ET.SubElement(svg, 'path', {
            'd': f'M {b[0]},{b[1]} L {b[0]-8*ux+4*uy},{b[1]-8*uy-4*ux} '
                 f'L {b[0]-8*ux-4*uy},{b[1]-8*uy+4*ux} Z', 'fill': '#555555'})
    for n in nodes:
        x, y, w, h = pos[n['key']]
        fill = {'flow': '#e8e8e8', 'conditional': '#f6f6f6',
                'decision': '#e8e8e8', 'recovery': '#d7d7d7',
                'outcome': '#ffffff'}[n['kind']]
        a = ET.SubElement(svg, 'a', {'href': spec,
                         'aria-label': n['activity'] + ' ' + n['title']})
        ET.SubElement(a, 'title').text = n['note'] or n['title']
        if n['kind'] == 'decision':
            ET.SubElement(a, 'path', {
                'd': f'M {x+w/2},{y} L {x+w},{y+h/2} L {x+w/2},{y+h} L {x},{y+h/2} Z',
                'fill': fill, 'stroke': '#333333', 'stroke-width': '1.5'})
        else:
            attrs = {'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h),
                     'rx': '42' if n['kind'] == 'outcome' else '8',
                     'fill': fill, 'stroke': '#333333', 'stroke-width': '1.5'}
            if n['kind'] in ('conditional', 'recovery'):
                attrs['stroke-dasharray'] = '6 4'
            ET.SubElement(a, 'rect', attrs)
        lines = textwrap.wrap(n['title'], 29 if n['kind'] != 'decision' else 18)
        assert len(lines) <= 2, n
        if n['kind'] == 'decision':
            for j, line in enumerate(lines):
                text(x+w/2, y+42+j*18, line, 14, 'middle', a)
            text(x+w/2, y+78, n['activity'], 11, 'middle', a, '#555555')
        else:
            for j, line in enumerate(lines):
                text(x+w/2, y+26+j*19, line, 15, 'middle', a)
            text(x+w/2, y+72, n['note'], 12, 'middle', a, '#444444')
            text(x+w/2, y+92, n['activity'], 11, 'middle', a, '#555555')
    boundaries = [
        'Logical responsibility groups; actual service ownership, API fields and provider interfaces require qualification.',
        'Connection checks and readiness do not activate a route. Phase gates and supported scope apply to every branch.',
        'Preserve valid unaffected services. Reconcile possible external effects before repeating a change or reporting activation.']
    for i, value in enumerate(boundaries):
        text(28, 1030+i*24, value, 14)
    base = OUT / slug
    base.with_suffix('.svg').write_text(ET.tostring(svg, encoding='unicode'))

    mx = ET.Element('mxfile', host='app.diagrams.net', type='device', version='24.7.17')
    diagram = ET.SubElement(mx, 'diagram', id=slug, name=title)
    graph = ET.SubElement(diagram, 'mxGraphModel', page='1',
                         pageWidth=str(WIDTH), pageHeight=str(HEIGHT))
    root = ET.SubElement(graph, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')

    def cell(key, value, style, x, y, w, h):
        c = ET.SubElement(root, 'mxCell', id=key, value=value, style=style,
                          vertex='1', parent='1')
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w),
                      height=str(h), attrib={'as': 'geometry'})

    cell('title', title+'\n'+description, 'text;whiteSpace=wrap;html=0;align=left;fontSize=20;',
         28, 12, WIDTH-56, 95)
    cell('legend', 'Proposed design · '+LEGEND, 'text;html=0;align=left;fontSize=14;',
         28, 104, WIDTH-56, 36)
    for i, lane in enumerate(LANES):
        cell(f'lane-{i}', lane,
             'swimlane;horizontal=0;noLabel=1;startSize=200;html=0;fillColor=#e5e5e5;'
             'swimlaneFillColor=#fafafa;strokeColor=#aaaaaa;', 20, 160+i*140, WIDTH-40, 140)
        cell(f'lane-label-{i}', '\n'.join(textwrap.wrap(lane, 23)),
             'text;html=0;align=center;verticalAlign=middle;fontSize=15;',
             30, 160+i*140, 180, 140)
    for n in nodes:
        shape = {'decision': 'rhombus;', 'outcome': 'rounded=1;arcSize=80;'}
        fill = {'flow': '#e8e8e8', 'conditional': '#f6f6f6',
                'decision': '#e8e8e8', 'recovery': '#d7d7d7', 'outcome': '#ffffff'}[n['kind']]
        style = shape.get(n['kind'], 'rounded=1;') + (
            f'whiteSpace=wrap;html=0;fontSize=15;fillColor={fill};strokeColor=#333333;spacing=8;')
        if n['kind'] in ('conditional', 'recovery'):
            style += 'dashed=1;'
        obj = ET.SubElement(root, 'object', id=n['key'], link=spec,
                            label=n['title']+'\n'+n['note']+'\n'+n['activity'], tooltip=n['note'])
        c = ET.SubElement(obj, 'mxCell', vertex='1', parent='1', style=style)
        x, y, w, h = pos[n['key']]
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w),
                      height=str(h), attrib={'as': 'geometry'})
    for i, (e, points) in enumerate(zip(edges, paths)):
        sx, sy, sw, sh = pos[e['source']]
        tx, ty, tw, th = pos[e['target']]
        style = (f'edgeStyle=none;endArrow=block;strokeColor=#555555;'
                 f'exitX={(points[0][0]-sx)/sw};exitY={(points[0][1]-sy)/sh};'
                 f'entryX={(points[-1][0]-tx)/tw};entryY={(points[-1][1]-ty)/th};')
        if e['kind'] != 'flow':
            style += 'dashed=1;'
        c = ET.SubElement(root, 'mxCell', id=f'edge-{i}', source=e['source'],
                          target=e['target'], edge='1', parent='1', style=style)
        g = ET.SubElement(c, 'mxGeometry', relative='1', attrib={'as': 'geometry'})
        points_array = ET.SubElement(g, 'Array', attrib={'as': 'points'})
        for x, y in points[1:-1]:
            ET.SubElement(points_array, 'mxPoint', x=str(x), y=str(y))
    cell('boundary', '\n'.join(boundaries), 'text;html=0;align=left;fontSize=14;',
         28, 1010, WIDTH-56, 96)
    ET.indent(mx)
    base.with_suffix('.drawio').write_text(ET.tostring(mx, encoding='unicode', xml_declaration=True))
    return base.with_suffix('.svg')


def build_all():
    paths = []
    paths.append(build('onboarding-scenario-selection-process',
        'Review current setup and choose the requested journey',
        'ONB-S01–08 share identity, authority, current-setup assessment and per-function results. Existing platform use does not prove Sage access or active exchange.', [
        node('request', 0, 0, 'Choose functions to use in Sage', 'ONB-01', 'Business and desired outcome'),
        node('api', 1, 1, 'Submit setup through the API', 'ONB-01', 'Scoped product request'),
        node('subject', 1, 3, 'Check business and permission', 'ONB-02', 'Caller and represented party'),
        node('assess', 2, 2, 'Review current setup', 'ONB-10', 'Declared and observed facts'),
        node('read', 2, 3, 'Read settings and valid checks', 'ONB-10', 'No setup changes', 'conditional'),
        node('choice', 3, 2, 'What work is needed?', 'ONB-10', kind='decision'),
        node('confirm', 4, 1, 'Unchanged: confirm setup', 'ONB-11', 'Current valid evidence', 'outcome'),
        node('missing', 4, 3, 'Missing: configure and check', 'ONB-03–06', 'Selected supported functions', 'conditional'),
        node('change', 4, 0, 'Change: authorise activation', 'ONB-07/09', 'Qualified scope and boundary', 'conditional'),
        node('hold', 4, 4, 'Explain limitation or unknown', 'ONB-08/11', 'Owner and safe next action', 'recovery'),
        node('result', 6, 1, 'Return results to the ERP', 'ONB-11', 'Readiness and activation apart', 'outcome')], [
        edge('request', 'api'), edge('api', 'subject'), edge('subject', 'assess'),
        edge('assess', 'read', 'conditional'), edge('read', 'assess', 'conditional'),
        edge('assess', 'choice'), edge('choice', 'confirm'),
        edge('choice', 'missing', 'conditional'), edge('choice', 'change', 'conditional'),
        edge('choice', 'hold', 'recovery'), edge('confirm', 'result'),
        edge('missing', 'result'), edge('change', 'result'), edge('hold', 'result', 'recovery')]))

    paths.append(build('onboarding-existing-provider-connection-process',
        'Connect the current private provider to Sage',
        'ONB-S03 keeps the existing provider. Bind the authorised account and qualify each function; initial Sage route activation may still be needed. ONB-S01 adds only contract-required new enrolment.', [
        node('request', 0, 0, 'Keep provider and connect Sage', 'ONB-01', 'Selected sending or receiving'),
        node('api', 1, 1, 'Submit the connection request', 'ONB-01', 'Common Global API contract'),
        node('identity', 1, 3, 'Check business and permission', 'ONB-02', 'Per function and environment'),
        node('assess', 2, 2, 'Identify existing account', 'ONB-10', 'Observe setup and gaps'),
        node('configure', 3, 3, 'Bind missing Sage settings', 'ONB-05', 'No duplicate enrolment'),
        node('qualify', 4, 3, 'Check each selected function', 'ONB-06', 'Transport, authority, profile'),
        node('external', 4, 5, 'Observe required provider state', 'ONB-06', 'Publish only if required', 'conditional'),
        node('activate', 5, 2, 'Confirm or activate Sage route', 'ONB-07', 'Explicit authority if needed', 'conditional'),
        node('result', 6, 1, 'Show per-function ERP results', 'ONB-11', 'Current provider retained', 'outcome'),
        node('recover', 5, 4, 'Resolve the affected setup', 'ONB-08', 'No provider substitution', 'recovery')], [
        edge('request', 'api'), edge('api', 'identity'), edge('identity', 'assess'),
        edge('assess', 'configure'), edge('configure', 'qualify'),
        edge('qualify', 'external', 'conditional'), edge('external', 'qualify', 'conditional'),
        edge('qualify', 'activate'), edge('activate', 'result'),
        edge('qualify', 'recover', 'recovery'), edge('recover', 'result', 'recovery')]))

    paths.append(build('onboarding-combined-platform-setup-process',
        'Connect public and private functions independently',
        'ONB-S04 records which platform handles each function. Shared identity does not share readiness; invoice delivery, public copies and reports have distinct execution owners and results.', [
        node('request', 0, 0, 'Choose public/private functions', 'ONB-01', 'Keep or extend current setup'),
        node('api', 1, 1, 'Submit the scoped setup', 'ONB-01', 'Functions and directions'),
        node('identity', 1, 3, 'Check business and permission', 'ONB-02', 'Authority for each action'),
        node('assess', 2, 2, 'Map functions and their owners', 'ONB-10', 'Observe current configuration'),
        node('public', 3, 3, 'Check public prerequisites', 'ONB-03', 'Qualified connector and trust'),
        node('private', 3, 2, 'Coordinate private setup', 'ONB-05/06', 'Existing account and gaps'),
        node('pubready', 4, 2, 'Record public readiness', 'ONB-04', 'No route activation'),
        node('privready', 4, 3, 'Record private function checks', 'ONB-06', 'Each direction separate'),
        node('external', 4, 5, 'Observe private service state', 'ONB-06', 'Qualified provider contract', 'conditional'),
        node('activation', 5, 3, 'Confirm authorised private route', 'ONB-07', 'Activate only if needed', 'conditional'),
        node('result', 6, 1, 'Return separate function results', 'ONB-11', 'Show limitations and owners', 'outcome'),
        node('recover', 5, 4, 'Hold only dependent work', 'ONB-08', 'Preserve valid services', 'recovery')], [
        edge('request', 'api'), edge('api', 'identity'), edge('identity', 'assess'),
        edge('assess', 'public'), edge('assess', 'private'),
        edge('public', 'pubready', points=[(1385, 650), (1410, 650), (1410, 510), (1420, 510)]),
        edge('private', 'privready', points=[(1255, 562), (1255, 580), (1550, 580), (1550, 598)]),
        edge('privready', 'external', 'conditional'),
        edge('external', 'privready', 'conditional'), edge('pubready', 'result'), edge('privready', 'activation'),
        edge('activation', 'result'), edge('pubready', 'recover', 'recovery'),
        edge('privready', 'recover', 'recovery'), edge('recover', 'result', 'recovery')]))

    paths.append(build('onboarding-existing-sage-setup-process',
        'Confirm existing Sage setup or add missing functions',
        'ONB-S05 confirms valid unchanged setup without an external mutation. Missing or stale checks apply only to affected functions; any new activation needs its own authority and evidence.', [
        node('request', 0, 0, 'Review setup or add a function', 'ONB-01', 'Explicit requested outcome'),
        node('api', 1, 1, 'Submit review through the API', 'ONB-01', 'Business and environment'),
        node('identity', 1, 3, 'Recheck current permission', 'ONB-02', 'No inherited authority'),
        node('assess', 2, 2, 'Read setup and evidence', 'ONB-10', 'Settings, versions, freshness'),
        node('choice', 3, 2, 'Any missing work?', 'ONB-10', kind='decision'),
        node('confirm', 4, 1, 'No: confirm existing setup', 'ONB-11', 'Zero external mutations', 'outcome'),
        node('checks', 4, 3, 'Yes: check affected functions', 'ONB-03–06', 'Reuse valid unchanged checks', 'conditional'),
        node('activate', 5, 2, 'Activate only requested scope', 'ONB-07', 'If supported and authorised', 'conditional'),
        node('recover', 5, 4, 'Resolve stale or unknown facts', 'ONB-08', 'Do not infer deregistration', 'recovery'),
        node('result', 6, 1, 'Return current function results', 'ONB-11', 'Unchanged functions preserved', 'outcome')], [
        edge('request', 'api'), edge('api', 'identity'), edge('identity', 'assess'),
        edge('assess', 'choice'), edge('choice', 'confirm'),
        edge('choice', 'checks', 'conditional'), edge('confirm', 'result'),
        edge('checks', 'activate', 'conditional'), edge('activate', 'result'),
        edge('checks', 'result'), edge('checks', 'recover', 'recovery'),
        edge('recover', 'result', 'recovery')]))

    paths.append(build('onboarding-service-continuity-recovery-process',
        'Recover the affected function and preserve valid services',
        'All ONB-S01–08 journeys use one recovery model. Before external effects keep the previous safe arrangement; possible receiving-point changes require observation and a scoped hold if unsafe.', [
        node('capture', 0, 2, 'Capture operation and pre-state', 'OFR-01', 'Parent scenario and checkpoint'),
        node('classify', 1, 2, 'Classify fault and repeat safety', 'OFR-02', 'Exact provider, role and scope'),
        node('scope', 2, 3, 'Preserve or hold affected scope', 'OFR-02/INT-08', 'Connection/Routing decides'),
        node('correct', 3, 0, 'Correct only affected evidence', 'OFR-03', 'New input or plan revision', 'conditional'),
        node('safe', 3, 3, 'Retry only proven safe work', 'OFR-04', 'Original identity and budget', 'conditional'),
        node('hold', 3, 2, 'Hold possible external effect', 'OFR-05', 'No conflicting repeat', 'recovery'),
        node('observe', 4, 5, 'Observe the original effect', 'OFR-06', 'Reliable source and evidence', 'conditional'),
        node('escalate', 4, 4, 'Own unresolved or unsafe work', 'OFR-07', 'Evidence and next action', 'recovery'),
        node('resume', 5, 2, 'Recheck parent after resolution', 'OFR-08', 'Activation stays separate'),
        node('result', 6, 1, 'Show per-function ERP results', 'ONB-11', 'Readiness and activation apart', 'outcome')], [
        edge('capture', 'classify'), edge('classify', 'scope'),
        edge('scope', 'correct', 'conditional'), edge('scope', 'safe', 'conditional'),
        edge('scope', 'hold', 'recovery'),
        edge('correct', 'resume', points=[(1385, 230), (1700, 230), (1700, 510), (1715, 510)]),
        edge('safe', 'resume', points=[(1385, 650), (1700, 650), (1700, 510), (1715, 510)]),
        edge('hold', 'observe', 'conditional', [(1385, 510), (1395, 510), (1395, 860), (1550, 860), (1550, 878)]),
        edge('observe', 'resume', points=[(1680, 930), (1695, 930), (1695, 510), (1715, 510)]),
        edge('observe', 'escalate', 'recovery'), edge('escalate', 'result', 'recovery'),
        edge('resume', 'result')], spec=OFR))
    return paths


def render_pngs(paths):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': WIDTH, 'height': HEIGHT}, device_scale_factor=1)
        page.route('http://**/*', lambda route: route.abort())
        page.route('https://**/*', lambda route: route.abort())
        for svg in paths:
            page.goto(svg.as_uri())
            failures = page.evaluate('''() => Array.from(document.querySelectorAll('svg a')).flatMap(a => {
                const shape=a.querySelector('rect,path').getBBox();
                return Array.from(a.querySelectorAll('text')).flatMap(t => {
                    const b=t.getBBox();
                    return b.x<shape.x+2 || b.x+b.width>shape.x+shape.width-2 ||
                           b.y<shape.y+2 || b.y+b.height>shape.y+shape.height-2
                           ? [t.textContent] : [];
                });
            })''')
            assert not failures, (svg.stem, failures)
            page.locator('svg').screenshot(path=str(svg.with_suffix('.png')))
            page.set_viewport_size({'width': 480, 'height': 800})
            page.goto('about:blank')
            page.set_content('<div style="width:100%;overflow-x:auto">'+svg.read_text()+'</div>')
            assert page.locator('div').evaluate('(e) => e.scrollWidth > e.clientWidth')
            page.set_viewport_size({'width': WIDTH, 'height': HEIGHT})
            print(svg.stem + ': rendered; text fits; narrow view scrolls')
        browser.close()


if __name__ == '__main__':
    render_pngs(build_all())
