"""Build SPEC037's summary flow with customer settings and setup colour groups."""
from pathlib import Path
import importlib.util
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'onboarding-summary-scenario-selection-process'
LOGICAL = '../../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#'
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])
SETTINGS_FILL = '#E6F4F1'
SETUP_FILL = '#F0EBFA'
SETTINGS_NODES = {'start', 'select', 'assess', 'pending', 'request', 'result'}
spec = importlib.util.spec_from_file_location('summary_renderer', ROOT / 'work/build-onboarding-scenario-diagrams.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def build():
    node, edge = renderer.node, renderer.edge
    nodes = [
        node('start', 1, 0, 'Open E-invoicing settings or guided onboarding', 'SPEC038 §1', 'In the business’s or accountant’s Sage product', 'outcome'),
        node('select', 1, 1, 'Select the business or client', 'ONB-01/02', 'Use the existing selection where available'),
        node('assess', 1, 2, 'Review current e-invoicing setup', 'ONB-10', 'Sage loads saved setup through SXS; customer reviews'),
        node('pending', 2, 2, 'E · Show pending result or limitation', 'ONB-08/10/11', 'Next action and owner; no duplicate setup', 'recovery'),
        node('request', 1, 3, 'Choose the requested action', 'ONB-01', 'Review / Connect or add a platform / Switch platform'),
        node('identity', 1, 4, 'Complete the applicable shared checks', 'ONB-02/03', 'NIF, action permission; certificate only if required'),
        node('choice', 1, 4, 'Which platform setup applies?', 'ONB-10', kind='decision'),
        node('public', 0, 5, 'Confirm or establish Sage public access', 'ONB-03/04', 'Reuse valid evidence; no public registration assumed'),
        node('private', 2, 5, 'Account on chosen private platform?', 'ONB-05', 'Assess the chosen platform, not any previous provider', 'decision'),
        node('privateexisting', 2, 6, 'Connect existing account to Sage', 'ONB-05', 'Reuse a valid Sage connection if present'),
        node('privatenew', 3, 6, 'Complete provider onboarding, then connect', 'ONB-05', 'Complete required provider and Sage setup'),
        node('privatecheck', 2, 6, 'Confirm private access', 'ONB-06', 'For requested functions; reuse valid evidence'),
        node('usechoice', 1, 7, 'Start or change platform use?', 'ONB-07', 'Only if included in the customer request', 'decision'),
        node('routecheck', 1, 8, 'Confirm the platform choice and start', 'ONB-07', 'Enabled, authorised and ready; sending / receiving', 'conditional'),
        node('activation', 1, 9, 'Start or change platform use', 'ONB-07/09', 'Agreed start and scope; keep earlier-invoice access', 'conditional'),
        node('result', 1, 10, 'Show results and next actions', 'ONB-11', 'Setup / readiness / platform use; next action and owner', 'outcome'),
    ]
    anchors = {
        'start': '1-purpose-and-authority',
        'select': '61-onb-01-capture-requested-functions',
        'request': '61-onb-01-capture-requested-functions',
        'assess': '64-onb-10-assess-current-setup',
        'pending': '610-onb-08-reconcile-and-recover',
        'identity': '62-onb-02-check-business-identity-and-authority',
        'choice': '64-onb-10-assess-current-setup',
        'public': '65-onb-03-assess-prerequisites',
        'private': '67-onb-05-configure-private-choice',
        'privateexisting': '67-onb-05-configure-private-choice',
        'privatenew': '67-onb-05-configure-private-choice',
        'privatecheck': '68-onb-06-prove-private-readiness',
        'usechoice': '69-onb-07-cut-over-new-traffic',
        'routecheck': '69-onb-07-cut-over-new-traffic',
        'activation': '69-onb-07-cut-over-new-traffic',
        'result': '612-onb-11-return-results-and-required-actions',
    }
    tags = {
        'select': 'S01–08', 'request': 'S01–08', 'assess': 'S01–08',
        'pending': 'S01–08', 'identity': 'S01–08',
        'public': 'S01/S02/S04/S05/S06/S07',
        'private': 'S01/S03/S04/S05/S06/S07',
        'privateexisting': 'Existing account', 'privatenew': 'No account on chosen platform',
        'privatecheck': 'S01/S03/S04/S05/S06/S07',
        'usechoice': 'Requested scope', 'routecheck': 'Requested scope',
        'activation': 'Requested scope', 'result': 'S01–08',
    }
    for item in nodes:
        item['link'] = LOGICAL + anchors[item['key']]
        if item['key'] in tags:
            item['classification'] = tags[item['key']]
    positions = {
        'start': (350, 310, 500, 104),
        'select': (350, 460, 500, 104),
        'assess': (350, 610, 500, 104),
        'pending': (1000, 610, 390, 104),
        'request': (350, 760, 500, 104),
        'identity': (350, 910, 500, 104),
        'choice': (400, 1060, 400, 104),
        'public': (70, 1260, 440, 104),
        'private': (650, 1260, 440, 104),
        'privateexisting': (530, 1460, 330, 104),
        'privatenew': (910, 1460, 420, 104),
        'privatecheck': (650, 1710, 440, 104),
        'usechoice': (400, 2040, 400, 104),
        'routecheck': (350, 2200, 500, 104),
        'activation': (350, 2360, 500, 104),
        'result': (280, 2620, 640, 110),
    }
    edges = [
        edge('start', 'select'), edge('select', 'assess'),
        edge('assess', 'request'), edge('request', 'identity'),
        edge('assess', 'pending', 'recovery',
             points=[(850,662),(1000,662)],
             label='Lookup unavailable', label_pos=(865,643)),
        edge('identity', 'choice', points=[(600,1014),(600,1060)]),
        edge('choice', 'public', 'conditional', points=[(600,1164),(600,1210),(290,1210),(290,1260)], label='Public functions', label_pos=(80,1242)),
        edge('choice', 'private', 'conditional', points=[(600,1164),(600,1210),(870,1210),(870,1260)], label='Private functions', label_pos=(660,1242)),
        edge('private', 'privateexisting', 'conditional', points=[(870,1364),(870,1410),(695,1410),(695,1460)], label='Yes — existing account', label_pos=(540,1442)),
        edge('private', 'privatenew', 'conditional', points=[(870,1364),(870,1410),(1120,1410),(1120,1460)], label='No — new account needed', label_pos=(920,1442)),
        edge('privateexisting', 'privatecheck', points=[(695,1564),(695,1640),(870,1640),(870,1710)]),
        edge('privatenew', 'privatecheck', points=[(1120,1564),(1120,1640),(870,1640),(870,1710)]),
        edge('public', 'usechoice', points=[(290,1364),(290,1880),(600,1880),(600,2040)]),
        edge('privatecheck', 'usechoice', points=[(870,1814),(870,1880),(600,1880),(600,2040)]),
        edge('usechoice', 'routecheck', 'conditional', points=[(600,2144),(600,2200)], label='Yes', label_pos=(620,2178)),
        edge('usechoice', 'result', 'conditional', points=[(800,2092),(970,2092),(970,2560),(600,2560),(600,2620)], label='No — setup only', label_pos=(995,2110)),
        edge('routecheck', 'activation', 'conditional'),
        edge('activation', 'result', 'conditional', points=[(600,2464),(600,2620)]),
    ]
    path = renderer.build(
        SLUG, 'Set up Sage access to the company’s chosen platforms',
        'Select the business, review current setup, choose the action, then complete the required checks.',
        nodes, edges, spec=LOGICAL+'31-in-scope', positions=positions,
        width=1440, height=2900, lanes=[],
        legend='Solid: setup steps · Dashed: conditional work or exception · E: same exception result · Folded note: precondition',
        captions=[
            (300,1920,'Both paths can apply; keep results per function.'),
            (300,1943,'Reuse valid setup; complete only missing, changed or expired work.'),
            (300,1966,'Keep valid B2G setup and independent successful results.'),
            (300,2005,'ONLY IF INCLUDED IN THIS REQUEST'),
        ],
        boundaries=[
            'E: stop dependent work; show the limitation or pending evidence, next action and owner. Resume only affected work.',
            'Setup only: keep any existing platform selection unchanged. If none exists, setup alone activates none.',
            'Phase 1: public access. Phases 2–3 add private setup and enabled platform changes. Private A to Private B stays disabled.',
        ])
    original = 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required'
    replacement = 'S01–S08 refer to SPEC038 scenarios. The customer and authorised accountant use the same flow.'
    svg = ET.parse(path).getroot()
    # Colour adds activity meaning; shapes and connectors retain their semantics.
    for item, anchor in zip(nodes, svg.findall(NS+'a')):
        anchor.set('id', item['key'])
        shape = anchor.find(NS+'rect')
        if shape is None:
            shape = anchor.find(NS+'path')
        shape.set('fill', SETTINGS_FILL if item['key'] in SETTINGS_NODES else SETUP_FILL)
    colour_legend = [
        (28, SETTINGS_FILL, 'Customer settings'),
        (220, SETUP_FILL, 'Setup and checks'),
        (420, '#fafafa', 'Product precondition'),
    ]
    for x, fill, label in colour_legend:
        ET.SubElement(svg, NS+'rect', {
            'x': str(x), 'y': '154', 'width': '16', 'height': '14',
            'fill': fill, 'stroke': '#777777'})
        ET.SubElement(svg, NS+'text', {
            'x': str(x+24), 'y': '166', 'font-family': 'Arial, sans-serif',
            'font-size': '13', 'fill': '#333333'}).text = label
    colour_limit = 'Colour shows activity type, not readiness or implementation.'
    ET.SubElement(svg, NS+'text', {
        'x': '650', 'y': '166', 'font-family': 'Arial, sans-serif',
        'font-size': '12', 'fill': '#555555'}).text = colour_limit
    group_labels = [
        ('settings-entry', 350, 299, 'CUSTOMER SETTINGS'),
        ('setup-checks', 350, 899, 'SETUP AND CHECKS'),
        ('settings-result', 280, 2608, 'CUSTOMER SETTINGS'),
    ]
    for _, x, y, label in group_labels:
        ET.SubElement(svg, NS+'text', {
            'x': str(x), 'y': str(y), 'font-family': 'Arial, sans-serif',
            'font-size': '12', 'font-weight': 'bold', 'fill': '#444444'}).text = label
    precondition = ET.SubElement(svg, NS+'a', {
        'href': LOGICAL+'4-feature-wide-functional-requirements-and-rules',
        'aria-label': 'Product precondition: integrations available before customer onboarding'})
    ET.SubElement(precondition, NS+'path', {
        'd': 'M 250,180 H 930 L 950,200 V 270 H 250 Z M 930,180 V 200 H 950',
        'fill': '#fafafa', 'stroke': '#777777', 'stroke-width': '1.5'})
    note_lines = [
        ('PRODUCT PRECONDITION', 202, 13),
        ('SXS and Tax / Connections Service integration is available.', 227, 15),
        ('Before customer onboarding · SPEC038 §4', 252, 12),
    ]
    for value, y, size in note_lines:
        ET.SubElement(precondition, NS+'text', {
            'x': '600', 'y': str(y), 'font-family': 'Arial, sans-serif',
            'font-size': str(size), 'text-anchor': 'middle', 'fill': '#444444'}).text = value
    centered_captions = {
        'Both paths can apply; keep results per function.',
        'Reuse valid setup; complete only missing, changed or expired work.',
        'Keep valid B2G setup and independent successful results.',
        'ONLY IF INCLUDED IN THIS REQUEST',
    }
    for text in list(svg.iter(NS+'text')):
        if text.text == original:
            text.text = replacement
        if text.text in centered_captions:
            # Leave a break in the central connector for each explanatory line.
            y = float(text.get('y'))
            background = ET.Element(NS+'rect', {
                'x': '250', 'y': str(y-17), 'width': '700',
                'height': '24', 'fill': 'white'})
            svg.insert(list(svg).index(text), background)
            text.set('x', '600')
            text.set('text-anchor', 'middle')
    native = ET.parse(path.with_suffix('.drawio')).getroot()
    root = native.find('.//mxGraphModel/root')
    node_by_key = {item['key']: item for item in nodes}
    for obj in native.iter('object'):
        item = node_by_key[obj.get('id')]
        if item['kind'] == 'decision':
            # Decision notes are tooltips in SVG; keep the editable label identical.
            obj.set('label', item['title']+'\n\n'+renderer.activity_label(item))
        fill = SETTINGS_FILL if obj.get('id') in SETTINGS_NODES else SETUP_FILL
        cell = obj.find('mxCell')
        style = cell.get('style')
        parts = [part for part in style.split(';') if part and not part.startswith('fillColor=')]
        cell.set('style', ';'.join(parts) + ';fillColor=' + fill + ';')

    def label_cell(key, value, x, y, width, height, style):
        cell = ET.SubElement(root, 'mxCell', {
            'id': key, 'value': value, 'style': style, 'vertex': '1', 'parent': '1'})
        ET.SubElement(cell, 'mxGeometry', {
            'x': str(x), 'y': str(y), 'width': str(width), 'height': str(height), 'as': 'geometry'})

    for i, (x, fill, label) in enumerate(colour_legend):
        label_cell(f'colour-swatch-{i}', '', x, 154, 16, 14,
                   f'rounded=0;html=0;fillColor={fill};strokeColor=#777777;')
        label_cell(f'colour-label-{i}', label, x+24, 150, 185, 22,
                   'text;html=0;align=left;fontSize=13;fontColor=#333333;')
    label_cell('colour-limit', colour_limit, 650, 150, 530, 22,
               'text;html=0;align=left;fontSize=12;fontColor=#555555;')
    for key, x, y, label in group_labels:
        label_cell('group-'+key, label, x, y-16, 210, 22,
                   'text;html=0;align=left;fontSize=12;fontStyle=1;fontColor=#444444;')
    note = ET.SubElement(root, 'object', {
        'id': 'product-precondition',
        'link': LOGICAL+'4-feature-wide-functional-requirements-and-rules',
        'label': '\n'.join(value for value, _, _ in note_lines)})
    cell = ET.SubElement(note, 'mxCell', {
        'vertex': '1', 'parent': '1',
        'style': 'shape=note;size=20;whiteSpace=wrap;html=0;align=center;'
                 'fontSize=14;fillColor=#fafafa;strokeColor=#777777;spacing=8;'})
    ET.SubElement(cell, 'mxGeometry', {
        'x': '250', 'y': '180', 'width': '700', 'height': '90', 'as': 'geometry'})
    for cell in native.iter('mxCell'):
        if cell.get('id') == 'behaviour-legend':
            cell.set('value', replacement)
        if cell.get('id') in ('caption-0', 'caption-1', 'caption-2', 'caption-3'):
            cell.set('style', 'text;html=0;align=center;fontSize=14;fillColor=#ffffff;')
            geometry = cell.find('mxGeometry')
            geometry.set('x', '250')
            geometry.set('width', '700')
    # Repeated E symbols reference one exception outcome, rather than adding work.
    # Store the common target in both editable and SVG metadata for correlation checks.
    exception_cases = [
        ('request', 900, 812, 'Unsupported choice'),
        ('identity', 900, 962, 'Failed or pending shared check'),
        ('public', 555, 1312, 'Failed or unknown public access'),
        ('private', 1140, 1312, 'Account status on the chosen platform is unconfirmed'),
        ('privateexisting', 885, 1512, 'Existing-account Sage connection failed or uncertain'),
        ('privatenew', 1380, 1512, 'Provider onboarding unavailable, incomplete or connection uncertain'),
        ('privatecheck', 1140, 1762, 'Failed or unknown private access'),
        ('routecheck', 900, 2252, 'Platform choice, authority, readiness or start not confirmed'),
        ('activation', 900, 2412, 'Platform use result unknown'),
    ]
    for source, cx, cy, reason in exception_cases:
        key = 'exception-'+source
        target = ET.SubElement(svg, NS+'a', {
            'id': key, 'href': LOGICAL+'610-onb-08-reconcile-and-recover',
            'data-exception-target': 'pending', 'aria-label': reason+'; return exception result E'})
        ET.SubElement(target, NS+'title').text = reason+' → E · Show pending result or limitation'
        ET.SubElement(target, NS+'circle', {
            'cx': str(cx), 'cy': str(cy), 'r': '14', 'fill': SETTINGS_FILL,
            'stroke': '#555555', 'stroke-width': '1.5'})
        ET.SubElement(target, NS+'text', {
            'x': str(cx), 'y': str(cy+4), 'font-family': 'Arial, sans-serif',
            'font-size': '12', 'text-anchor': 'middle', 'fill': '#333333'}).text = 'E'
        x, y, w, h = positions[source]
        end = cx-14
        ET.SubElement(svg, NS+'path', {
            'd': f'M {x+w},{cy} H {end}', 'fill': 'none', 'stroke': '#555555',
            'stroke-width': '1.8', 'stroke-dasharray': '6 4'})
        ET.SubElement(svg, NS+'path', {
            'd': f'M {end},{cy} L {end-8},{cy-4} L {end-8},{cy+4} Z', 'fill': '#555555'})
        obj = ET.SubElement(root, 'object', {
            'id': key, 'label': 'E', 'link': LOGICAL+'610-onb-08-reconcile-and-recover',
            'exception_target': 'pending', 'tooltip': reason+' → E · Show pending result or limitation'})
        cell = ET.SubElement(obj, 'mxCell', {
            'vertex': '1', 'parent': '1',
            'style': f'ellipse;html=0;fontSize=12;align=center;fillColor={SETTINGS_FILL};strokeColor=#555555;'})
        ET.SubElement(cell, 'mxGeometry', {
            'x': str(cx-14), 'y': str(cy-14), 'width': '28', 'height': '28', 'as': 'geometry'})
        line = ET.SubElement(root, 'mxCell', {
            'id': 'edge-'+key, 'source': source, 'target': key, 'edge': '1', 'parent': '1',
            'style': 'edgeStyle=none;endArrow=block;strokeColor=#555555;dashed=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;'})
        ET.SubElement(line, 'mxGeometry', {'relative': '1', 'as': 'geometry'})
    exception_notes = [
        'Every E reference returns the affected work here.',
        'Missing input / authority, unsupported or unknown.',
        'Keep independent successful results.',
        'Resume only affected work.',
        'Reconcile uncertain changes before retry.',
    ]
    for i, value in enumerate(exception_notes):
        y = 746+i*22
        ET.SubElement(svg, NS+'text', {
            'x': '1000', 'y': str(y), 'font-family': 'Arial, sans-serif',
            'font-size': '12', 'fill': '#444444'}).text = value
        label_cell('exception-note-'+str(i), value, 1000, y-16, 400, 22,
                   'text;html=0;align=left;fontSize=12;fontColor=#444444;')
    path.write_text(ET.tostring(svg, encoding='unicode'))
    ET.indent(native)
    path.with_suffix('.drawio').write_text(ET.tostring(native, encoding='unicode', xml_declaration=True))
    return {'svg': str(path.relative_to(ROOT)), 'png': str(path.with_suffix('.png').relative_to(ROOT)),
            'drawio': str(path.with_suffix('.drawio').relative_to(ROOT)), 'nodes': len(nodes),
            'width': 1440, 'height': 2900, 'public_and_private_can_both_apply': True,
            'precondition_outside_flow': True,
            'customer_action_after_setup_review': True,
            'colour_groups': {'customer_settings': SETTINGS_FILL, 'setup_and_checks': SETUP_FILL},
            'platform_use_decision_after_each_applicable_path': True,
            'setup_only_exit_after_each_applicable_path': True,
            'unchanged_setup_is_shared_behaviour': True,
            'private_existing_and_new_accounts_explicit': True,
            'exception_references': len(exception_cases)}


if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
