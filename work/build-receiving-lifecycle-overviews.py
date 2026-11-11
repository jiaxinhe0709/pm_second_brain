"""Build concise current-view overviews; preserve predecessor process diagrams."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('feature_flow', ROOT/'work/build-onboarding-scenario-diagrams.py')
flow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(flow)
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])

def finish(path):
    old = 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required'
    new = 'Read top to bottom. Branches apply only to the selected source or required action.'
    svg = ET.parse(path).getroot()
    for text in svg.iter(NS+'text'):
        if text.text == old:
            text.text = new
    path.write_text(ET.tostring(svg, encoding='unicode'))
    native = ET.parse(path.with_suffix('.drawio')).getroot()
    for cell in native.iter('mxCell'):
        if cell.get('id') == 'behaviour-legend':
            cell.set('value', new)
    ET.indent(native)
    path.with_suffix('.drawio').write_text(ET.tostring(native, encoding='unicode', xml_declaration=True))
    return path

def receiving():
    # Retrieval is edited in Draw.io; render it without replacing local source edits.
    spec = importlib.util.spec_from_file_location(
        'retrieval_preview', ROOT / 'work/build-invoice-retrieval-overview.py')
    preview = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(preview)
    return preview.build()


def lifecycle():
    n,e=flow.node,flow.edge
    nodes=[
        n('input',0,0,'Read platform evidence or an authorised business fact','LCS-01','Existing invoice and its original source context'),
        n('verify',0,0,'Check invoice, business, actor and permission','LCS-02','Hold unknown or unauthorised work'),
        n('save',0,0,'Save evidence and apply country rules','LCS-03/04','Keep raw codes, times and correction history'),
        n('view',0,0,'Update the supported invoice facts','LCS-05/06','Delivery, decisions, payment and reports stay separate'),
        n('needed',0,0,'Is an outgoing report required?','LCS-07',kind='decision'),
        n('plan',0,0,'Select each report and its execution owner','LCS-07/08','Required fields, destination, original route and deadline'),
        n('public',0,0,'Send the required public report','LCS-09','Recipient or issuer contract; Spain fields confirmed','conditional'),
        n('private',0,0,'Send the required private report','LCS-09','Only where applicable; identify provider-owned reports','conditional'),
        n('result',0,0,'Show facts, report results and next actions','LCS-06/10','Each destination keeps its own result and action owner','outcome'),
    ]
    positions={
        'input':(400,180,600,104),'verify':(400,340,600,104),
        'save':(400,500,600,104),'view':(400,660,600,104),
        'needed':(500,820,400,104),'plan':(400,1050,600,104),
        'public':(130,1270,500,104),'private':(770,1270,500,104),
        'result':(400,1530,600,110),
    }
    edges=[
        e('input','verify',points=[(700,284),(700,340)]),
        e('verify','save',points=[(700,444),(700,500)]),
        e('save','view',points=[(700,604),(700,660)]),
        e('view','needed',points=[(700,764),(700,820)]),
        e('needed','plan','conditional',[(700,924),(700,1050)],'Yes',(720,992)),
        e('needed','result','conditional',[(500,872),(70,872),(70,1470),(700,1470),(700,1530)],'No outgoing report',(90,1000)),
        e('plan','public','conditional',[(700,1154),(700,1200),(380,1200),(380,1270)],'If required',(200,1240)),
        e('plan','private','conditional',[(700,1154),(700,1200),(1020,1200),(1020,1270)],'If required',(840,1240)),
        e('public','result',points=[(380,1374),(380,1430),(700,1430),(700,1530)]),
        e('private','result',points=[(1020,1374),(1020,1430),(700,1430),(700,1530)]),
    ]
    return finish(flow.build('invoice-lifecycle-overview-process',
        'Invoice lifecycle: show what happened and what needs action',
        'Business facts, status-change attempts and destination reporting have separate results.',
        nodes,edges,spec='../../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md',
        positions=positions,width=1400,height=1830,lanes=[],
        legend='Solid: saved evidence and results · Dashed: reporting only when applicable',
        boundaries=[
            'Unknown codes or conflicting evidence need review. Keep known facts and the last successful status when an attempt fails.',
            'A timeout keeps the external result unknown. Check the original report before unsafe replay or cancellation replacement.',
            'Public and private reports can both apply. Incoming already-reported evidence does not automatically create another report.',
        ]))

if __name__=='__main__':
    for path in [receiving(),lifecycle()]:
        print(path.relative_to(ROOT))
