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


def edge(source, target, kind='flow', points=None, label='', label_pos=None):
    return dict(source=source, target=target, kind=kind, points=points,
                label=label, label_pos=label_pos)


def classify(nodes, mapping):
    """Label behaviour without changing shapes or connector meanings."""
    for n in nodes:
        n['classification'] = mapping[n['key']]


def activity_label(n):
    return n['activity'] + (' · ' + n['classification'] if n.get('classification') else '')


def build(slug, title, description, nodes, edges, spec=ONB, *,
          positions=None, width=WIDTH, height=HEIGHT, lanes=LANES,
          boundaries=None, captions=(), legend=LEGEND):
    if spec == OFR:
        classify(nodes, {n['key']: ('Conditional' if n['kind'] in ('conditional', 'recovery')
                                  else 'Common') for n in nodes})
    pos = positions or {
        n['key']: (240 + n['col'] * 295, 178 + n['lane'] * 140, 260, 104)
        for n in nodes}
    assert len(pos) == len(nodes)
    for x, y, w, h in pos.values():
        assert 0 < x and 0 < y and x + w < width and y + h < height - 120
    shared.WIDTH, shared.HEIGHT = width, height
    paths = [e['points'] or shared.route(e, pos) for e in edges]
    svg = ET.Element('svg', {
        'xmlns': 'http://www.w3.org/2000/svg', 'width': str(width),
        'height': str(height), 'viewBox': f'0 0 {width} {height}',
        'role': 'img', 'aria-label': title})
    ET.SubElement(svg, 'title').text = title
    ET.SubElement(svg, 'desc').text = description
    ET.SubElement(svg, 'rect', width=str(width), height=str(height), fill='white')

    def text(x, y, value, size=15, anchor='start', parent=svg, color='#222222'):
        ET.SubElement(parent, 'text', {
            'x': str(x), 'y': str(y), 'font-family': 'Arial, sans-serif',
            'font-size': str(size), 'text-anchor': anchor, 'fill': color}).text = value

    text(28, 35, title, 24)
    for i, line in enumerate(textwrap.wrap(description, int(width / 12))):
        text(28, 65 + i * 20, line)
    text(28, 120, 'Proposed design · ' + legend, 14)
    behaviour_legend = 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required'
    text(28, 143, behaviour_legend, 13)
    for i, lane in enumerate(lanes):
        y = 160 + i * 140
        ET.SubElement(svg, 'rect', x='20', y=str(y), width=str(width - 40),
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
        a = ET.SubElement(svg, 'a', {'href': n.get('link', spec),
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
        lines = textwrap.wrap(n['title'], int(w / 9) if n['kind'] != 'decision' else int(w / 14))
        assert len(lines) <= 2, n
        if n['kind'] == 'decision':
            for j, line in enumerate(lines):
                text(x+w/2, y+42+j*18, line, 14, 'middle', a)
            text(x+w/2, y+78, activity_label(n), 11, 'middle', a, '#555555')
        else:
            for j, line in enumerate(lines):
                text(x+w/2, y+26+j*19, line, 15, 'middle', a)
            text(x+w/2, y+72, n['note'], 12, 'middle', a, '#444444')
            text(x+w/2, y+92, activity_label(n), 11, 'middle', a, '#555555')
    for e in edges:
        if e['label']:
            text(*e['label_pos'], e['label'], 13)
    for x, y, value in captions:
        text(x, y, value, 14)
    boundaries = boundaries or [
        'Logical responsibility groups; actual service ownership, API fields and provider interfaces require qualification.',
        'Connection checks and readiness do not activate a route. Phase gates and supported scope apply to every branch.',
        'Preserve valid unaffected services. Reconcile possible external effects before repeating a change or reporting activation.']
    for i, value in enumerate(boundaries):
        text(28, height-90+i*24, value, 14)
    base = OUT / slug
    base.with_suffix('.svg').write_text(ET.tostring(svg, encoding='unicode'))

    mx = ET.Element('mxfile', host='app.diagrams.net', type='device', version='24.7.17')
    diagram = ET.SubElement(mx, 'diagram', id=slug, name=title)
    graph = ET.SubElement(diagram, 'mxGraphModel', page='1',
                         pageWidth=str(width), pageHeight=str(height))
    root = ET.SubElement(graph, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')

    def cell(key, value, style, x, y, w, h):
        c = ET.SubElement(root, 'mxCell', id=key, value=value, style=style,
                          vertex='1', parent='1')
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w),
                      height=str(h), attrib={'as': 'geometry'})

    cell('title', title+'\n'+description, 'text;whiteSpace=wrap;html=0;align=left;fontSize=20;',
         28, 12, width-56, 95)
    cell('legend', 'Proposed design · '+legend, 'text;html=0;align=left;fontSize=14;',
         28, 104, width-56, 22)
    cell('behaviour-legend', behaviour_legend, 'text;html=0;align=left;fontSize=13;',
         28, 130, width-56, 24)
    for i, lane in enumerate(lanes):
        cell(f'lane-{i}', lane,
             'swimlane;horizontal=0;noLabel=1;startSize=200;html=0;fillColor=#e5e5e5;'
             'swimlaneFillColor=#fafafa;strokeColor=#aaaaaa;', 20, 160+i*140, width-40, 140)
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
        obj = ET.SubElement(root, 'object', id=n['key'], link=n.get('link', spec),
                            label=n['title']+'\n'+n['note']+'\n'+activity_label(n), tooltip=n['note'])
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
        if e['label']:
            lx, ly = e['label_pos']
            cell(f'edge-label-{i}', e['label'],
                 'text;html=0;align=left;fontSize=13;', lx, ly-16, 260, 22)
    for i, (x, y, value) in enumerate(captions):
        cell(f'caption-{i}', value, 'text;html=0;align=left;fontSize=14;',
             x, y-18, width-x-20, 24)
    cell('boundary', '\n'.join(boundaries), 'text;html=0;align=left;fontSize=14;',
         28, height-110, width-56, 96)
    ET.indent(mx)
    base.with_suffix('.drawio').write_text(ET.tostring(mx, encoding='unicode', xml_declaration=True))
    return base.with_suffix('.svg')


def build_all():
    """Build the three diagrams used by the current onboarding spec."""
    paths = []
    overview_nodes = [
        node('request', 0, 0, 'Capture requested functions', 'ONB-01', 'Business and desired outcome'),
        node('identity', 0, 0, 'Check business identity and authority', 'ONB-02', 'Business NIF; caller; action grant'),
        node('assess', 0, 0, 'Assess current setup', 'ONB-10', 'Reuse only valid matching evidence'),
        node('choice', 0, 0, 'What work is needed?', 'ONB-10', kind='decision'),
        node('confirm', 0, 0, 'Confirm valid existing setup', 'ONB-11', 'S05 and valid unchanged functions'),
        node('public', 0, 0, 'Check public setup requirements', 'ONB-03', 'Public · S01/02/04/05/07'),
        node('pubresult', 0, 0, 'Record public check results', 'ONB-04', 'Readiness; no route activation'),
        node('private', 0, 0, 'Configure and check private setup', 'ONB-05/06', 'Private · S01/03/04/05/06/07'),
        node('activation', 0, 0, 'Activate or change the route', 'ONB-07/09', 'If required; keep earlier invoice context', 'conditional'),
        node('hold', 0, 0, 'Explain limitation or uncertainty', 'ONB-08/11', 'S08 and affected work; owned action', 'recovery'),
        node('result', 0, 0, 'Return results and required actions', 'ONB-11', 'Setup, readiness and activation are separate', 'outcome')]
    classify(overview_nodes, {**dict.fromkeys(['request', 'identity', 'assess', 'choice', 'result'], 'Common'),
        **dict.fromkeys(['confirm', 'public', 'pubresult', 'private'], 'Scenario-specific'),
        **dict.fromkeys(['activation', 'hold'], 'Conditional')})
    for n in overview_nodes:
        if n['key'] in ('public', 'pubresult'):
            n['link'] = 'onboarding-public-readiness-process.svg'
        elif n['key'] in ('private', 'activation'):
            n['link'] = 'onboarding-private-route-process.svg'
        elif n['key'] == 'hold':
            n['link'] = OFR
    positions = {
        'request': (40, 165, 280, 104), 'identity': (430, 165, 280, 104),
        'assess': (830, 165, 280, 104), 'choice': (830, 305, 280, 104),
        'confirm': (40, 510, 280, 104), 'public': (380, 510, 280, 104),
        'pubresult': (380, 670, 280, 104), 'private': (720, 510, 280, 104),
        'activation': (720, 670, 280, 104), 'hold': (1060, 510, 280, 104),
        'result': (630, 900, 460, 104)}
    overview_edges = [edge('request', 'identity'), edge('identity', 'assess'), edge('assess', 'choice')]
    for key, centre in [('confirm', 180), ('public', 520), ('private', 860), ('hold', 1200)]:
        overview_edges.append(edge('choice', key, 'recovery' if key == 'hold' else 'conditional',
                                   [(970, 409), (970, 455), (centre, 455), (centre, 510)]))
    overview_edges += [edge('public', 'pubresult'), edge('private', 'activation', 'conditional'),
        edge('private', 'result', 'conditional', [(1000, 562), (1020, 562), (1020, 840), (860, 840), (860, 900)],
             'No route change needed', (1040, 750))]
    for key, centre, bottom in [('confirm', 180, 614), ('pubresult', 520, 774),
                                ('activation', 860, 774), ('hold', 1200, 614)]:
        overview_edges.append(edge(key, 'result', 'recovery' if key == 'hold' else 'flow',
                                   [(centre, bottom), (centre, 840), (860, 840), (860, 900)]
                                   if centre != 860 else [(860, bottom), (860, 900)]))
    paths.append(build('onboarding-scenario-selection-process',
        'Set up, connect or review e-invoicing through Sage',
        'ONB-S01–08 use one journey. Choose the work for each requested function. Public and private functions can both apply.',
        overview_nodes, overview_edges, positions=positions, width=1440, height=1140, lanes=(),
        legend='Solid: work or result · Dashed: selected or conditional work · Darker grey: limitation or recovery',
        captions=[(28, 430, 'Use each required branch. These columns show work paths, not service responsibilities.'),
                  (40, 490, 'Valid setup'), (380, 490, 'Public'),
                  (720, 490, 'Private'), (1060, 490, 'Needs action'),
                  (28, 875, 'Return a result for each function, including partial results and remaining actions.')],
        boundaries=[
            'Phase 1 checks public readiness. Later-phase private work requires qualified contracts and approved scope.',
            'Activation requires current readiness, explicit authority and an approved effective boundary.',
            'Preserve valid unaffected functions. Invoice features enforce required public-copy and reporting dependencies.']))

    # The detail diagrams start after the common request, authority and setup assessment.
    # Empty customer lanes are omitted. The shared service lane names remain unchanged.
    detail_lanes = LANES[1:]
    public_nodes = [
        node('plan', 0, 1, 'Use the assessed public setup plan', 'ONB-10', 'Common ONB-01/02 already complete'),
        node('evidence', 1, 2, 'Check business identity and authority', 'ONB-03', 'Recheck affected ONB-02 evidence'),
        node('trust', 2, 2, 'Check access and trust requirements', 'ONB-03', 'Certificate readiness or NOT_REQUIRED'),
        node('connector', 3, 2, 'Check the public connection', 'ONB-03', 'Qualified capability and environment'),
        node('external', 3, 4, 'Observe required public evidence', 'ONB-03', 'Only approved external operations', 'conditional'),
        node('ready', 4, 1, 'Required checks passed?', 'ONB-03', kind='decision'),
        node('record', 5, 1, 'Record public check results', 'ONB-04', 'Readiness and recheck conditions'),
        node('action', 4, 3, 'Own missing or unknown checks', 'ONB-08/11', 'Reconcile possible external effects', 'recovery'),
        node('result', 6, 0, 'Return results and required actions', 'ONB-11', 'Each client and function separate', 'outcome')]
    classify(public_nodes, {**dict.fromkeys(['plan', 'evidence', 'trust', 'ready', 'result'], 'Common'),
        **dict.fromkeys(['connector', 'record'], 'Scenario-specific'),
        **dict.fromkeys(['external', 'action'], 'Conditional')})
    paths.append(build('onboarding-public-readiness-process',
        'Check public setup and return the readiness result',
        'Public detail for ONB-S01/02/04/05/07. Run only missing or stale checks from the assessed plan. Public readiness does not activate invoice exchange.',
        public_nodes, [edge('plan', 'evidence'), edge('evidence', 'trust'), edge('trust', 'connector'),
        edge('connector', 'external', 'conditional'), edge('external', 'connector', 'conditional'),
        edge('connector', 'ready'), edge('ready', 'record', label='Yes', label_pos=(1690, 349)),
        edge('ready', 'action', 'recovery', label='No / unknown', label_pos=(1570, 574)),
        edge('action', 'record', 'recovery'), edge('record', 'result')],
        lanes=detail_lanes, height=980,
        boundaries=[
            'ONB-01/02/10 establish the request, authority and current setup. Existing public or B2G use does not prove Sage B2B access.',
            'Keep exact readiness states. Return failed and unknown checks with actions; an uncertain external effect uses SPEC-SEI-004.',
            'Check certificate policy, then required readiness through qualified Tax/certificate references. Unknown lookup does not mean missing.']))

    private_nodes = [
        node('plan', 0, 1, 'Use the assessed private setup plan', 'ONB-10', 'Provider, scope and customer choice'),
        node('configure', 1, 2, 'Configure missing provider settings', 'ONB-05', 'Bind existing account where selected'),
        node('checks', 2, 2, 'Check access and trust requirements', 'ONB-06', 'Certificate readiness; each function'),
        node('external', 2, 4, 'Observe required provider state', 'ONB-06', 'Publish only if plan requires it', 'conditional'),
        node('ready', 3, 1, 'Required checks passed?', 'ONB-06', kind='decision'),
        node('change', 4, 1, 'Route change needed?', 'ONB-10/07', kind='decision'),
        node('activate', 5, 2, 'Activate the authorised route', 'ONB-07', 'Recheck authority and boundary', 'conditional'),
        node('history', 6, 2, 'Keep earlier invoice context', 'ONB-09', 'Release only at separate gates'),
        node('action', 3, 3, 'Resolve only the affected scope', 'ONB-08', 'Hold unsafe work; keep valid services', 'recovery'),
        node('result', 6, 0, 'Return results and required actions', 'ONB-11', 'Readiness and activation separate', 'outcome')]
    classify(private_nodes, {**dict.fromkeys(['plan', 'checks', 'ready', 'result'], 'Common'),
        'configure': 'Scenario-specific', **dict.fromkeys(['external', 'change', 'activate', 'history', 'action'], 'Conditional')})
    paths.append(build('onboarding-private-route-process',
        'Connect a private provider; activate or change only when required',
        'Private detail for supported functions in ONB-S01/03/04/05/06/07. Keep the selected existing provider unless a change is requested. Qualified setup comes before authorised activation.',
        private_nodes, [edge('plan', 'configure'), edge('configure', 'checks'),
        edge('checks', 'external', 'conditional'), edge('external', 'checks', 'conditional'),
        edge('checks', 'ready'), edge('ready', 'change', label='Yes', label_pos=(1395, 349)),
        edge('ready', 'action', 'recovery', label='No / unknown', label_pos=(1275, 574)),
        edge('change', 'activate', 'conditional', [(1680, 370), (1700, 370), (1700, 510), (1715, 510)],
             'Yes: approved change', (1725, 438)),
        edge('change', 'result', 'conditional', [(1550, 318), (1550, 290), (1990, 290), (1990, 230), (2010, 230)],
             'No: return current evidence', (1640, 274)),
        edge('activate', 'history'), edge('history', 'result'),
        edge('action', 'result', 'recovery',
             [(1385, 650), (2310, 650), (2310, 230), (2270, 230)],
             'Return the required action', (1970, 632))], lanes=detail_lanes, height=980,
        boundaries=[
            'ONB-01/02/10 already establish the request, authority and current setup. Reuse valid evidence; create only missing settings.',
            'Later-phase work only. New enrolment or publication needs a contract requirement; initial Sage activation needs explicit authority.',
            'Private A → Private B remains gated by SPEC-SEI-014. Reconcile uncertain effects; preserve invoice origins and historical access.']))
    return paths


def build_recovery():
    """Regenerate the separate recovery spec asset only when explicitly needed."""
    return build('onboarding-service-continuity-recovery-process',
        'Recover the affected function and preserve valid services',
        'All ONB-S01–08 journeys use one recovery model. Before external effects keep the previous safe arrangement; possible receiving-point changes require observation and a scoped hold if unsafe.', [
        node('capture', 0, 2, 'Capture operation and pre-state', 'OFR-01', 'Parent scenario and checkpoint'),
        node('classify', 1, 2, 'Classify fault and repeat safety', 'OFR-02', 'NIF, certificate and grant separate'),
        node('scope', 2, 3, 'Preserve or hold affected scope', 'OFR-02/INT-08', 'Connection/Routing decides'),
        node('correct', 3, 0, 'Correct only affected evidence', 'OFR-03', 'SPEC-001 owns certificate correction', 'conditional'),
        node('safe', 3, 3, 'Retry only proven safe work', 'OFR-04', 'Original identity and budget', 'conditional'),
        node('hold', 3, 2, 'Hold possible external effect', 'OFR-05', 'No conflicting repeat', 'recovery'),
        node('observe', 4, 5, 'Observe the original effect', 'OFR-06', 'Reliable source and evidence', 'conditional'),
        node('escalate', 4, 4, 'Own unresolved or unsafe work', 'OFR-07', 'Evidence and next action', 'recovery'),
        node('resume', 5, 2, 'Recheck parent after resolution', 'OFR-08', 'Exact ONB-02/03/05/06/07/10 gate'),
        node('result', 6, 1, 'Return results and required actions', 'ONB-11', 'Readiness and activation apart', 'outcome')], [
        edge('capture', 'classify'), edge('classify', 'scope'),
        edge('scope', 'correct', 'conditional'), edge('scope', 'safe', 'conditional'),
        edge('scope', 'hold', 'recovery'),
        edge('correct', 'resume', points=[(1385, 230), (1700, 230), (1700, 510), (1715, 510)]),
        edge('safe', 'resume', points=[(1385, 650), (1700, 650), (1700, 510), (1715, 510)]),
        edge('hold', 'observe', 'conditional', [(1385, 510), (1395, 510), (1395, 860), (1550, 860), (1550, 878)]),
        edge('observe', 'resume', points=[(1680, 930), (1695, 930), (1695, 510), (1715, 510)]),
        edge('observe', 'escalate', 'recovery'), edge('escalate', 'result', 'recovery'),
        edge('resume', 'result')], spec=OFR)


def render_pngs(paths):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': WIDTH, 'height': HEIGHT}, device_scale_factor=1)
        page.route('http://**/*', lambda route: route.abort())
        page.route('https://**/*', lambda route: route.abort())
        for svg in paths:
            dimensions = ET.parse(svg).getroot().attrib
            page.set_viewport_size({'width': int(dimensions['width']), 'height': int(dimensions['height'])})
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
