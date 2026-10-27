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
    n, e = flow.node, flow.edge
    nodes = [
        n('authority',0,0,'Check company, source and permission','RSD-01 / PRI-01','Reuse existing onboarding setup'),
        n('source',0,0,'Which source supplied the item?','RSD-03 / PRI-02',kind='decision'),
        n('public',0,0,'Find invoices by presentation date','RSD-03','Public platform: automatic collection'),
        n('private',0,0,'Read private notification or supplied files','PRI-02','A notification alone does not contain the invoice'),
        n('files',0,0,'Obtain the required source files','RSD-03 / PRI-03','Download missing files; reuse complete supplied bytes'),
        n('capture',0,0,'Verify and save files and item results','RSD-04/05','Exact bytes, roles, hashes and receiving state'),
        n('progress',0,0,'Save covered collection progress','RSD-06 / PRI-04','Only when every covered item is accounted for','outcome'),
        n('process',0,0,'Check and map the invoice','RCV-02–07','Recipient, safety, duplicates, profile and meaning'),
        n('savedread',0,0,'Read a saved file when requested','RSD-07/09','Current client/file permission; saved safe bytes','conditional'),
        n('product',0,0,'Deliver once and confirm product receipt','RCV-07','Keep pending delivery and who must act visible','outcome'),
    ]
    positions = {
        'authority':(460,180,480,104), 'source':(550,340,300,104),
        'public':(120,540,480,104), 'private':(800,540,480,104),
        'files':(460,760,480,104), 'capture':(460,930,480,104),
        'progress':(40,1160,360,110), 'process':(460,1160,480,104),
        'savedread':(1000,1160,360,104), 'product':(460,1340,480,110),
    }
    edges = [
        e('authority','source',points=[(700,284),(700,340)]),
        e('source','public','conditional',[(700,444),(700,480),(360,480),(360,540)],'Public platform',(160,520)),
        e('source','private','conditional',[(700,444),(700,480),(1040,480),(1040,540)],'Private platform',(840,520)),
        e('public','files',points=[(360,644),(360,700),(700,700),(700,760)]),
        e('private','files',points=[(1040,644),(1040,700),(700,700),(700,760)]),
        e('files','capture',points=[(700,864),(700,930)]),
        e('capture','process',points=[(700,1034),(700,1160)]),
        e('capture','progress',points=[(460,982),(220,982),(220,1160)]),
        e('capture','savedread','conditional',[(940,982),(1180,982),(1180,1160)]),
        e('process','product',points=[(700,1264),(700,1340)]),
    ]
    return finish(flow.build('invoice-retrieval-overview-process',
        'Receive invoices: find the file, save it and deliver once',
        'Phase 1: public collection. Private intake follows its selected later-phase scope.',
        nodes,edges,spec='../../specs/invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md',
        positions=positions,width=1400,height=1660,lanes=[],
        legend='Solid: main steps · Dashed: selected source or a requested saved-file read',
        boundaries=[
            'A missing file or pending receiving handoff cannot complete collection progress. Partial capture keeps its recovery owner.',
            'Mapping or product failure preserves saved source files and independently permitted access. Recover only affected work.',
            'Source acknowledgement uses its confirmed contract milestone. Buyer acceptance and payment reports belong to lifecycle.',
        ]))

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
