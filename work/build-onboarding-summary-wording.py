"""Build SPEC037's agreed summary flow in its existing grey visual style."""
from pathlib import Path
import importlib.util
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'onboarding-summary-scenario-selection-process'
LOGICAL = '../../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#'
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])
spec = importlib.util.spec_from_file_location('summary_renderer', ROOT / 'work/build-onboarding-scenario-diagrams.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def build():
    node, edge = renderer.node, renderer.edge
    nodes = [
        node('prerequisite', 1, 0, 'Product integrates with SXS and Tax / Connections Service', 'SPEC038 §4', 'Before customer onboarding'),
        node('request', 1, 1, 'Choose company and requested setup', 'ONB-01', 'New setup / review / add platform / change'),
        node('assess', 1, 2, 'Resolve the company’s dataset through SXS', 'ONB-10', 'Find saved connections and credentials'),
        node('identity', 1, 3, 'Check NIF and caller permission', 'ONB-02/03', 'Check certificate suitability only if required'),
        node('choice', 1, 4, 'Which checks are still needed?', 'ONB-10', kind='decision'),
        node('confirm', 0, 5, 'Reuse unchanged setup', 'ONB-11', 'Keep valid connections and evidence'),
        node('public', 1, 5, 'Check Sage access to the public platform', 'ONB-03/04', 'No public registration assumed'),
        node('private', 2, 5, 'Reuse or connect the chosen provider account', 'ONB-05', 'Add only missing Sage setup'),
        node('privatecheck', 2, 6, 'Check connection and access', 'ONB-06', 'For the requested private-platform functions'),
        node('routecheck', 1, 7, 'Confirm the change is enabled and authorised', 'ONB-07/09', 'Target ready; start agreed', 'conditional'),
        node('activation', 1, 8, 'Apply the routing change', 'ONB-07/09', 'Preserve access to earlier invoices', 'conditional'),
        node('result', 1, 9, 'Show the result for each request', 'ONB-11', 'Access / connection / routing result; pending work and who must act', 'outcome'),
    ]
    anchors = {
        'prerequisite': '4-feature-wide-functional-requirements-and-rules',
        'request': '61-onb-01-capture-requested-functions',
        'assess': '64-onb-10-assess-current-setup',
        'identity': '62-onb-02-check-business-identity-and-authority',
        'choice': '64-onb-10-assess-current-setup',
        'confirm': '612-onb-11-return-results-and-required-actions',
        'public': '65-onb-03-assess-prerequisites',
        'private': '67-onb-05-configure-private-choice',
        'privatecheck': '68-onb-06-prove-private-readiness',
        'routecheck': '69-onb-07-cut-over-new-traffic',
        'activation': '69-onb-07-cut-over-new-traffic',
        'result': '612-onb-11-return-results-and-required-actions',
    }
    tags = {
        'request': 'S01–08', 'assess': 'S01–08', 'identity': 'S01–08',
        'confirm': 'S05 / unchanged valid setup',
        'public': 'S01/S02/S04/S05/S07', 'private': 'S01/S03/S04/S05',
        'privatecheck': 'S01/S03/S04/S05', 'routecheck': 'S01/S06',
        'activation': 'S01/S06', 'result': 'S01–08',
    }
    for item in nodes:
        item['link'] = LOGICAL + anchors[item['key']]
        if item['key'] in tags:
            item['classification'] = tags[item['key']]
    positions = {
        'prerequisite': (350, 180, 500, 104),
        'request': (350, 330, 500, 104),
        'assess': (350, 480, 500, 104),
        'identity': (350, 630, 500, 104),
        'choice': (450, 780, 300, 104),
        'confirm': (60, 980, 300, 104),
        'public': (450, 980, 300, 104),
        'private': (840, 980, 300, 104),
        'privatecheck': (840, 1130, 300, 104),
        'routecheck': (350, 1410, 500, 104),
        'activation': (350, 1570, 500, 104),
        'result': (280, 1840, 640, 110),
    }
    edges = [
        edge('prerequisite', 'request'), edge('request', 'assess'),
        edge('assess', 'identity'),
        edge('identity', 'choice', points=[(600,734),(600,780)]),
        edge('choice', 'confirm', 'conditional', points=[(600,884),(600,930),(210,930),(210,980)], label='Existing Sage setup remains valid', label_pos=(60,962)),
        edge('choice', 'public', 'conditional', points=[(600,884),(600,980)], label='Public platform', label_pos=(470,962)),
        edge('choice', 'private', 'conditional', points=[(600,884),(600,930),(990,930),(990,980)], label='Private platform', label_pos=(860,962)),
        edge('private', 'privatecheck'),
        edge('confirm', 'routecheck', points=[(210,1084),(210,1290),(600,1290),(600,1410)]),
        edge('public', 'routecheck', points=[(600,1084),(600,1410)]),
        edge('privatecheck', 'routecheck', points=[(990,1234),(990,1290),(600,1290),(600,1410)]),
        edge('routecheck', 'activation', 'conditional'),
        edge('activation', 'result', 'conditional', points=[(600,1674),(600,1840)]),
        edge('public', 'result', 'conditional', points=[(600,1084),(600,1290),(250,1290),(250,1770),(600,1770),(600,1840)], label='Otherwise, keep current routing', label_pos=(35,1695)),
    ]
    path = renderer.build(
        SLUG, 'Set up Sage access to the company’s chosen platforms',
        'Read top to bottom: prepare the product, check the company’s setup, then change routing only if requested.',
        nodes, edges, spec=LOGICAL+'31-in-scope', positions=positions,
        width=1200, height=2180, lanes=[],
        legend='Solid: setup steps · Dashed: selected checks or a requested routing change',
        captions=[
            (350,1330,'Public and private checks can both apply.'),
            (350,1352,'Keep the same company dataset.'),
            (350,1390,'IF A ROUTING CHANGE IS REQUESTED'),
        ],
        boundaries=[
            'At any check: show missing information, approval, an unknown result or an unsupported choice, and who must act.',
            'Keep successful results and existing B2G (S07). Resume only affected checks; check the original request if its result is unknown.',
            'Phase 1: public-access checks. Later phase: private connections and routing changes. Private A to Private B stays disabled.',
        ])
    original = 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required'
    replacement = 'S01–S08 refer to SPEC038 scenarios. The customer and authorised accountant use the same flow.'
    svg = ET.parse(path).getroot()
    centered_captions = {
        'Public and private checks can both apply.',
        'Keep the same company dataset.',
        'IF A ROUTING CHANGE IS REQUESTED',
    }
    for text in list(svg.iter(NS+'text')):
        if text.text == original:
            text.text = replacement
        if text.text in centered_captions:
            # Leave a break in the central connector for each explanatory line.
            y = float(text.get('y'))
            background = ET.Element(NS+'rect', {
                'x': '300', 'y': str(y-17), 'width': '600',
                'height': '24', 'fill': 'white'})
            svg.insert(list(svg).index(text), background)
            text.set('x', '600')
            text.set('text-anchor', 'middle')
    path.write_text(ET.tostring(svg, encoding='unicode'))
    native = ET.parse(path.with_suffix('.drawio')).getroot()
    for cell in native.iter('mxCell'):
        if cell.get('id') == 'behaviour-legend':
            cell.set('value', replacement)
        if cell.get('id') in ('caption-0', 'caption-1', 'caption-2'):
            cell.set('style', 'text;html=0;align=center;fontSize=14;fillColor=#ffffff;')
            geometry = cell.find('mxGeometry')
            geometry.set('x', '300')
            geometry.set('width', '600')
    ET.indent(native)
    path.with_suffix('.drawio').write_text(ET.tostring(native, encoding='unicode', xml_declaration=True))
    return {'svg': str(path.relative_to(ROOT)), 'png': str(path.with_suffix('.png').relative_to(ROOT)),
            'drawio': str(path.with_suffix('.drawio').relative_to(ROOT)), 'nodes': len(nodes),
            'width': 1200, 'height': 2180, 'public_and_private_can_both_apply': True,
            'routing_after_each_successful_path': True}


if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
