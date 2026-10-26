"""Keep SPEC037's original branching layout; change labels and current-source links only."""
from pathlib import Path
import copy
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/diagrams'
ORIGINAL = OUT / 'onboarding-scenario-selection-process.svg'
SLUG = 'onboarding-summary-scenario-selection-process'
LOGICAL = '../../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#'
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])

# Order and IDs match the original SVG and editable Draw.io source.
NODES = [
 ('request', 'Choose the requested setup', 'Business and required functions', '61-onb-01-capture-requested-functions'),
 ('identity', 'Check the NIF and permission', 'Check the business and caller separately', '62-onb-02-check-business-identity-and-authority'),
 ('assess', 'Check existing setup', 'Reuse valid checks for the same work', '64-onb-10-assess-current-setup'),
 ('choice', 'Which work is needed?', '', '64-onb-10-assess-current-setup'),
 ('confirm', 'Keep valid existing setup', 'S05 and other unchanged valid setup', '612-onb-11-return-results-and-required-actions'),
 ('public', 'Check public access', 'Check required access and certificate', '65-onb-03-assess-prerequisites'),
 ('pubresult', 'Record public setup results', 'Show readiness; do not activate a route', '66-onb-04-publish-public-readiness'),
 ('private', 'Set up and check private access', 'Reuse or connect the chosen account', '67-onb-05-configure-private-choice'),
 ('activation', 'Activate or change the route', 'If needed; keep earlier-invoice access', '69-onb-07-cut-over-new-traffic'),
 ('hold', 'Explain the problem and next action', 'S08 or affected work; name who must act', '610-onb-08-reconcile-and-recover'),
 ('result', 'Show results and next actions', 'Report setup, readiness and route activation separately', '612-onb-11-return-results-and-required-actions'),
]

REPLACEMENTS = {
 'ONB-S01–08 use one journey. Choose the work for each requested function. Public and private functions can both apply.':
 'ONB-S01–08: choose the work needed for each requested function. Both public and private setup may be needed.',
 'Proposed design · Solid: work or result · Dashed: selected or conditional work · Darker grey: limitation or recovery':
 'Proposed flow · Solid: step or result · Dashed: only when needed · Darker grey: problem or recovery',
 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required':
 'Common: used across cases · Scenario-specific: selected case · Conditional: only when needed',
 'Use each required branch. These columns show work paths, not service responsibilities.':
 'Follow each branch needed for the request. Columns show work; they do not assign service ownership.',
 'Return a result for each function, including partial results and remaining actions.':
 'Show a result for each function: completed checks, unfinished work and who must act.',
 'Phase 1 checks public readiness. Later-phase private work requires qualified contracts and approved scope.':
 'Phase 1 checks public access. Later-phase private setup needs confirmed contracts and approved scope.',
 'Activation requires current readiness, explicit authority and an approved effective boundary.':
 'Activate a route only after checks pass, permission is confirmed and the start point is agreed.',
 'Preserve valid unaffected functions. Invoice features enforce required public-copy and reporting dependencies.':
 'Keep other valid functions. Invoice features check any required public copy and reporting before use.',
}

def shapes(root):
 return [(e.tag, dict(e.attrib)) for e in root.iter() if e.tag in {NS+'rect', NS+'path', NS+'polygon', NS+'line', NS+'ellipse'}]

def build():
 original = ET.parse(ORIGINAL).getroot()
 svg = copy.deepcopy(original)
 native_original = ET.parse(ORIGINAL.with_suffix('.drawio')).getroot()
 native = copy.deepcopy(native_original)
 for root in [svg, native]:
  for element in root.iter():
   for old, new in REPLACEMENTS.items():
    if element.text:
     element.text = element.text.replace(old, new)
    for attr in ['value', 'label', 'tooltip']:
     if element.get(attr):
      element.set(attr, element.get(attr).replace(old, new))
 groups = svg.findall(NS+'a')
 assert len(groups) == len(NODES) == 11
 for group, (key, title, note, anchor) in zip(groups, NODES):
  obj = next(e for e in native.iter('object') if e.get('id') == key)
  activity = obj.get('label').split('\n')[-1]
  group.set('href', LOGICAL+anchor)
  group.set('aria-label', activity.split(' · ')[0]+' '+title)
  group.find(NS+'title').text = note or title
  texts = group.findall(NS+'text')
  title_nodes = [e for e in texts if e.get('font-size') in {'14','15'}]
  template = copy.deepcopy(title_nodes[0])
  start_y = float(template.get('y'))
  for e in title_nodes:
   group.remove(e)
  lines = textwrap.wrap(title, 20 if key == 'choice' else (49 if key == 'result' else 31))
  assert len(lines) <= 2, (key, lines)
  for i, line in enumerate(lines):
   e = copy.deepcopy(template)
   e.set('y', str(start_y + i*19))
   e.text = line
   group.append(e)
  for e in texts:
   if e.get('font-size') == '12':
    e.text = note
  obj.set('link', LOGICAL+anchor)
  obj.set('label', '\n'.join([title, note, activity]))
  obj.set('tooltip', note)
 assert shapes(svg) == shapes(original), 'Original shapes and connectors must stay identical'
 def geometry(root):
  return [ET.tostring(e) for e in root.iter('mxGeometry')]
 assert geometry(native) == geometry(native_original), 'Editable layout must stay identical'
 path = OUT/(SLUG+'.svg')
 path.write_text(ET.tostring(svg, encoding='unicode'))
 ET.indent(native)
 path.with_suffix('.drawio').write_text(ET.tostring(native, encoding='unicode', xml_declaration=True))
 return dict(svg=str(path.relative_to(ROOT)), png=str(path.with_suffix('.png').relative_to(ROOT)),
             drawio=str(path.with_suffix('.drawio').relative_to(ROOT)), nodes=11,
             width=1440, height=1140, title=svg.find(NS+'title').text,
             original_layout_preserved=True)

if __name__ == '__main__':
 print(build())
