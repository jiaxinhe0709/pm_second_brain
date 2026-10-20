"""Build the current onboarding process diagrams without external calls.

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
OFR = '../../specs/SPEC-SEI-002-onboarding-solution-specification.md#onb-08-recovery'


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

    paths.extend(build_integrated_details())
    return paths


def build_integrated_details():
    """Keep recovery beside its parent check in the standard responsibility lanes.

    Step text and sequences retain the detailed safety decisions. Historical
    standalone recovery assets stay intact.
    """
    public = [
        node('plan',0,2,'Use the current public setup plan','ONB-01/02/10','Run missing or out-of-date checks'),
        node('identity',1,3,'Check business identity and authority','ONB-02/03','Business NIF, caller and action permission'),
        node('trust',2,3,'Check access and trust requirements','ONB-03','Certificate result or policy exception'),
        node('connection',3,5,'Check the public connection','ONB-03','Qualified reads for this function'),
        node('record',5,2,'Save public check results','ONB-04','Evidence, readiness and next check time'),
        node('result',6,1,'Show results and next actions','ONB-11','Readiness is separate from activation','outcome'),
        node('correct',2,0,'Correct the requested evidence','ONB-02/03 / OFR-03','Same business, purpose and affected check','conditional'),
        node('recover',4,2,'Resolve the blocked check','ONB-08 / OFR-02/04–08','Check the original result; retry only if safe','recovery'),
        node('case',4,4,'Review the unresolved case','OFR-07','Named owner, evidence and next action','recovery'),
    ]
    classify(public,{n['key']: ('Common' if n['key'] in ('plan','identity','trust','result')
                              else 'Scenario-specific' if n['key'] in ('connection','record')
                              else 'Conditional') for n in public})
    pub_edges = [
        edge('plan','identity',points=[(500,510),(517,510),(517,650),(535,650)]),
        edge('identity','trust',points=[(795,650),(830,650)]),
        edge('trust','connection',points=[(1090,650),(1105,650),(1105,930),(1125,930)]),
        edge('connection','record',points=[(1385,930),(1695,930),(1695,510),(1715,510)],
             label='Checks pass',label_pos=(1450,914)),
        edge('record','result',points=[(1975,510),(1992,510),(1992,370),(2010,370)]),
        edge('identity','correct','conditional',points=[(665,598),(665,300),(960,300),(960,282)],
             label='Missing identity or permission',label_pos=(690,325)),
        edge('trust','correct','conditional',points=[(960,598),(960,282)],
             label='Access or certificate problem',label_pos=(975,365)),
        edge('correct','plan','conditional',points=[(830,230),(370,230),(370,458)],
             label='Corrected: repeat the same check',label_pos=(400,215)),
        edge('correct','record','conditional',points=[(1090,230),(1845,230),(1845,458)],
             label='Pending: return required action',label_pos=(1250,215)),
        edge('trust','recover','recovery',points=[(1090,625),(1110,625),(1110,430),(1550,430),(1550,458)],
             label='Check unavailable or result unknown',label_pos=(1160,416)),
        edge('connection','recover','recovery',points=[(1385,905),(1400,905),(1400,510),(1420,510)],
             label='Read failed or result unknown',label_pos=(1140,775)),
        edge('recover','plan','conditional',points=[(1420,535),(1405,535),(1405,575),(370,575),(370,562)],
             label='Resolved: repeat the affected check',label_pos=(700,565)),
        edge('recover','record','recovery',points=[(1680,510),(1715,510)],
             label='Record this result',label_pos=(1640,445)),
        edge('recover','case','recovery',points=[(1550,562),(1550,738)],
             label='Needs review',label_pos=(1565,720)),
        edge('case','record','recovery',points=[(1680,790),(1705,790),(1705,535),(1715,535)],
             label='Return action and owner',label_pos=(1730,750)),
    ]
    pub = build('onboarding-public-readiness-process',
        'Check public setup and return readiness',
        'ONB-S01/02/04/05/07. Follow the required checks from left to right. Resolve findings at the affected step and return a result for each function.',
        public,pub_edges,height=1120,boundaries=[
            'After correction or a confirmed result, repeat the affected check. Unavailable evidence does not prove a missing certificate.',
            'Check whether the original operation ran before repeating it. Keep unresolved work on hold with a named owner.',
            'Public readiness does not activate a route. Keep other valid functions available. The matrix below links to the detailed rules.'])

    private = [
        node('plan',0,2,'Use the current private setup plan','ONB-01/02/10','Selected provider and affected check'),
        node('configure',1,3,'Add missing provider settings','ONB-05','Link the selected existing account'),
        node('checks',2,3,'Check each private function','ONB-06','Check access, trust and readiness'),
        node('external',2,5,'Check the current provider state','ONB-06','Change only if plan and contract require','conditional'),
        node('change',4,2,'Is a route change needed?','ONB-07/10',kind='decision'),
        node('activate',5,3,'Activate the authorised route','ONB-07','Current readiness, authority and version','conditional'),
        node('history',6,3,'Keep earlier invoice history','ONB-09','Keep each invoice linked to its original route'),
        node('result',6,1,'Show results and next actions','ONB-11','Readiness and activation stay separate','outcome'),
        node('correct',1,0,'Correct settings or obtain approval','ONB-05/12 / OFR-03','Same client item; current evidence','conditional'),
        node('recover',3,2,'Resolve the blocked setup or route','ONB-08 / OFR-02/04–08','Keep the original operation; stop unsafe work','recovery'),
        node('case',3,4,'Review the unresolved case','OFR-07','Named owner, evidence and next action','recovery'),
    ]
    classify(private,{n['key']: ('Common' if n['key'] in ('plan','checks','result')
                               else 'Scenario-specific' if n['key']=='configure'
                               else 'Conditional') for n in private})
    priv_edges = [
        edge('plan','configure',points=[(500,510),(517,510),(517,650),(535,650)]),
        edge('configure','checks',points=[(795,650),(830,650)]),
        edge('checks','external','conditional',points=[(940,702),(940,878)],
             label='Access and trust passed',label_pos=(760,810)),
        edge('external','checks','conditional',points=[(980,878),(980,702)],
             label='Current evidence',label_pos=(990,850)),
        edge('checks','change',points=[(1090,650),(1400,650),(1400,510),(1420,510)],
             label='Checks pass',label_pos=(1180,635)),
        edge('change','activate','conditional',points=[(1680,510),(1700,510),(1700,650),(1715,650)],
             label='Yes: supported and authorised',label_pos=(1720,585)),
        edge('change','result','conditional',points=[(1550,458),(1550,300),(2140,300),(2140,318)],
             label='No: keep the current route',label_pos=(1640,286)),
        edge('activate','history',points=[(1975,650),(2010,650)]),
        edge('history','result',points=[(2140,598),(2140,422)]),
        edge('configure','correct','conditional',points=[(645,598),(645,282)],
             label='Missing settings or approval',label_pos=(370,405)),
        edge('correct','configure','conditional',points=[(685,282),(685,598)],
             label='Corrected',label_pos=(700,440)),
        edge('correct','result','conditional',points=[(795,230),(2140,230),(2140,318)],
             label='Pending: return required action',label_pos=(1150,215)),
        edge('checks','recover','recovery',points=[(1090,625),(1105,625),(1105,510),(1125,510)],
             label='Failed or unknown',label_pos=(1120,610)),
        edge('external','recover','recovery',points=[(1090,930),(1105,930),(1105,535),(1125,535)],
             label='Result unknown',label_pos=(990,785)),
        edge('activate','recover','recovery',points=[(1845,702),(1845,720),(1300,720),(1300,562)],
             label='Conflict, unknown result or later failure',label_pos=(1430,710)),
        edge('recover','plan','conditional',points=[(1125,480),(1115,480),(1115,575),(370,575),(370,562)],
             label='Resolved: repeat the affected check',label_pos=(700,565)),
        edge('recover','result','recovery',points=[(1255,458),(1255,300),(2140,300),(2140,318)],
             label='Return the result and next action',label_pos=(990,280)),
        edge('recover','case','recovery',points=[(1255,562),(1255,738)],
             label='Needs review',label_pos=(1140,715)),
        edge('case','result','recovery',points=[(1385,790),(2310,790),(2310,370),(2270,370)],
             label='Return action and owner',label_pos=(1860,775)),
    ]
    priv = build('onboarding-private-route-process',
        'Connect a private provider; activate only when required',
        'Supported later-phase ONB-S01/03/04/05/06/07. Configure missing setup, check each function, then confirm or activate the authorised route.',
        private,priv_edges,height=1120,boundaries=[
            'Return a limitation for unsupported functions. Pending correction or an unknown result cannot establish readiness or activation.',
            'Save the intended change before execution. Check the original operation before repeating it. Return to the affected check.',
            'Keep valid services and each invoice\'s original route. Restoring a route needs a new authorised change; Private A to Private B stays blocked pending approval.'])
    return [pub,priv]

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
