"""Build a customer-action overview using the existing onboarding renderer."""
from pathlib import Path
import html
import importlib.util
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'offboarding-and-switch-customer-actions'
spec = importlib.util.spec_from_file_location('onboarding_renderer', ROOT / 'work/build-onboarding-scenario-diagrams.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])
LOGICAL = '../../specs/offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md'
def scenario_rows():
    """Use the logical specification as the sole scenario statement."""
    source = (ROOT / 'specs/offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md').read_text()
    return [[cell.strip() for cell in line.strip('|').split('|')]
            for line in source.splitlines() if line.startswith('| OFF-S')]


def build_settings():
    n, e = renderer.node, renderer.edge
    target = '../../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#e-invoicing-settings-intended-interaction'
    nodes = [
        n('settings',0,0,'Open E-invoicing settings','Customer entry point','Review the selected business or authorised client'),
        n('connect',0,0,'Connect or add a platform','Customer action','Keep existing valid setup'),
        n('switch',0,0,'Switch platform','Customer action','Change future sending or receipt'),
        n('disconnect',0,0,'Disconnect or stop a service','Customer action','No new platform is assumed'),
        n('connectwork',0,0,'Set up and check Sage access','Onboarding','Reuse a valid account and connection'),
        n('switchwork',0,0,'Check new setup and end selected old services','Onboarding + routing + offboarding','One customer request; keep earlier work accounted for'),
        n('disconnectwork',0,0,'End selected access or services safely','Offboarding','Keep earlier work and records accounted for'),
        n('result',0,0,'Return the result and next actions to settings','Shared result','Show progress, pending work and who must act next','outcome'),
    ]
    pos={'settings':(500,180,600,104),'connect':(60,430,460,104),'switch':(570,430,460,104),'disconnect':(1080,430,460,104),
         'connectwork':(60,610,460,104),'switchwork':(570,610,460,104),'disconnectwork':(1080,610,460,104),'result':(480,900,640,110)}
    edges=[]
    for key,cx in [('connect',290),('switch',800),('disconnect',1310)]:
        edges.append(e('settings',key,points=[(800,284),(800,350),(cx,350),(cx,430)] if cx!=800 else [(800,284),(800,430)]))
        edges.append(e(key,key+'work',points=[(cx,534),(cx,610)]))
        edges.append(e(key+'work','result',points=[(cx,714),(cx,820),(800,820),(800,900)] if cx!=800 else [(800,714),(800,900)]))
    path=renderer.build('e-invoicing-settings-actions','Manage e-invoicing in settings',
        'The customer chooses an action in one place. Sage coordinates the work behind that request.',
        nodes,edges,spec=target,positions=pos,width=1600,height=1230,lanes=[],
        legend='Solid: customer action and coordinated work',
        boundaries=['A switch is one request. Do not ask the customer to complete separate onboarding and offboarding journeys.',
                    'Show only actions supported for this business, caller, country and platform. Settings do not enable a disabled switch.',
                    'Before confirmation, explain what changes, what remains, when it starts and how earlier invoices will be handled.'])
    svg=ET.parse(path).getroot()
    old='Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required'
    replacement='Intended interaction; detailed screen design and implementation remain to confirm.'
    for t in svg.iter(NS+'text'):
        if t.text==old: t.text=replacement
    path.write_text(ET.tostring(svg,encoding='unicode'))
    native=ET.parse(path.with_suffix('.drawio'))
    for c in native.iter('mxCell'):
        if c.get('id')=='behaviour-legend': c.set('value',replacement)
    native.write(path.with_suffix('.drawio'),encoding='unicode',xml_declaration=True)
    fragment='<div class="offboarding-actions" style="overflow-x:auto">'+path.read_text()+'</div>'
    path.with_suffix('.html').write_text(fragment)
    return fragment


def build():
    n, e = renderer.node, renderer.edge
    nodes = [
        n('request',0,0,'Choose an action in E-invoicing settings','OFF-01','Switch platform or Disconnect or stop a service'),
        n('risk',0,0,'Urgent incident?','OFF-S10',kind='decision'),
        n('contain',0,0,'Stop unsafe access or processing','OFF-S10 / OFF-08','Name who will recover affected work','recovery'),
        n('scope',0,0,'Confirm permission and what will change','OFF-01/02 · OFF-S07/08','Identify businesses, clients, addresses, directions, environments and services'),
        n('choice',0,0,'What changes?','Sage coordinates the required steps',kind='decision'),
        n('switch',0,0,'SWITCH: change the invoice platform','OFF-S02–05','Use onboarding to check the new setup','conditional'),
        n('offboard',0,0,'OFFBOARD: end selected access or services','OFF-S01/06–09','The invoice platform may remain in use'),
        n('switchcase',0,0,'Public to private; private to public or private','Only changes approved and checked for release','Sage product access may continue','conditional'),
        n('offboardcase',0,0,'Stop a connection, product or all Sage services','OFF-02','Stopping Sage access is not SPFE deregistration'),
        n('ready',0,0,'Check that the new platform can be used','OFF-03 + onboarding','Reuse onboarding APIs for setup; confirm Spain support','conditional'),
        n('closure',0,0,'Business ceased trading?','OFF-S09',kind='decision'),
        n('cessation',0,0,'Check closure evidence','OFF-S09 / G3','Decide if invoices must still be received','conditional'),
        n('continuity',0,0,'Check how work continues','OFF-S01/06 / G3','Confirm the access method'),
        n('cutover',0,0,'Change platform and confirm the result','OFF-04','End old-provider services only where permitted','conditional'),
        n('stop',0,0,'Stop new work in the selected Sage services','OFF-04','Keep someone responsible for earlier invoices'),
        n('history',0,0,'Finish earlier work or agree who takes it over','OFF-05/06/07','Remove access safely; hand over records or keep them accessible'),
        n('result',0,0,'Show each result and any remaining action','OFF-08 / completion','New invoices, access, contracts, earlier work and records','outcome'),
    ]
    positions = {
        'request':(500,180,600,104), 'risk':(640,340,320,104),
        'contain':(1170,340,380,104), 'scope':(480,540,640,104),
        'choice':(640,730,320,104),
        'switch':(100,950,600,104), 'offboard':(900,950,600,104),
        'switchcase':(100,1110,600,104), 'offboardcase':(900,1110,600,104),
        'ready':(100,1270,600,104), 'closure':(1030,1270,340,104),
        'cessation':(900,1470,280,104), 'continuity':(1220,1470,280,104),
        'cutover':(100,1660,600,104), 'stop':(900,1660,600,104),
        'history':(480,1930,640,104), 'result':(480,2100,640,110),
    }
    edges = [
        e('request','risk',points=[(800,284),(800,340)]),
        e('risk','contain','recovery',points=[(960,392),(1170,392)],label='Yes',label_pos=(1020,377)),
        e('risk','scope',points=[(800,444),(800,540)],label='No',label_pos=(825,493)),
        e('contain','scope','recovery',points=[(1360,444),(1360,490),(1140,490),(1140,592),(1120,592)],label='If a switch or exit is requested',label_pos=(1170,470)),
        e('scope','choice',points=[(800,644),(800,730)]),
        e('choice','switch','conditional',points=[(800,834),(800,900),(400,900),(400,950)]),
        e('choice','offboard',points=[(800,834),(800,900),(1200,900),(1200,950)]),
        e('switch','switchcase','conditional',points=[(400,1054),(400,1110)]),
        e('switchcase','ready','conditional',points=[(400,1214),(400,1270)]),
        e('ready','cutover','conditional',points=[(400,1374),(400,1660)]),
        e('offboard','offboardcase',points=[(1200,1054),(1200,1110)]),
        e('offboardcase','closure',points=[(1200,1214),(1200,1270)]),
        e('closure','cessation','conditional',points=[(1200,1374),(1200,1420),(1040,1420),(1040,1470)],label='Yes',label_pos=(960,1447)),
        e('closure','continuity',points=[(1200,1374),(1200,1420),(1360,1420),(1360,1470)],label='No',label_pos=(1380,1447)),
        e('cessation','stop','conditional',points=[(1040,1574),(1040,1610),(1200,1610),(1200,1660)]),
        e('continuity','stop',points=[(1360,1574),(1360,1610),(1200,1610),(1200,1660)]),
        e('cutover','history','conditional',points=[(400,1764),(400,1860),(800,1860),(800,1930)]),
        e('stop','history',points=[(1200,1764),(1200,1860),(800,1860),(800,1930)]),
        e('history','result',points=[(800,2034),(800,2100)]),
    ]
    anchors = {key:'2-state-invariants-and-workflow' for key in positions}
    for key in ('request','risk','contain','scope','choice','switch','offboard','switchcase','offboardcase','closure','cessation','continuity'):
        anchors[key] = 'customer-action-scenarios' if key not in ('scope','choice') else 'classification-and-scope'
    anchors['result']='7-assurance-and-traceability'
    for item in nodes:
        item['link']=LOGICAL+'#'+anchors[item['key']]
    path = renderer.build(SLUG, 'Switch platforms or end access and services',
        'Check what the customer wants to change, who can approve it, and how new and earlier invoices will be handled.',
        nodes, edges, spec=LOGICAL, positions=positions, width=1600, height=2430, lanes=[],
        legend='Solid: planned offboarding / shared controls · Dashed: switch, exception or recovery',
        captions=[(1170,292,'Act before setup or handover if access is unsafe'),
                  (1170,515,'Otherwise, continue the incident recovery work.'),
                  (100,865,'Sage coordinates both paths behind one Switch platform request.'),
                  (100,1490,'New platform not ready? Hold the switch.'),
                  (100,1515,'Closure evidence missing? Hold the exit.'),
                  (100,1540,'Keep safe, permitted work available.')],
        boundaries=[
            'Only an authorised incident responder may stop unsafe access. This does not complete a switch or customer exit.',
            'Every path keeps evidence and names who will finish earlier work. SPEC032 §1 defines customer scenarios OFF-S01–10.',
            'A listed scenario does not confirm feature availability. Private-to-private switching remains disabled in current onboarding scope.',
        ])
    svg = ET.parse(path).getroot()
    old = 'Common: shared behaviour · Scenario-specific: selected path · Conditional: only when required'
    new = 'A change can affect part or all of the setup. Business closure and urgent incidents need different checks.'
    for text in svg.iter(NS+'text'):
        if text.text == old:
            text.text = new
    path.write_text(ET.tostring(svg, encoding='unicode'))
    native = ET.parse(path.with_suffix('.drawio'))
    for cell in native.iter('mxCell'):
        if cell.get('id') == 'behaviour-legend':
            cell.set('value', new)
    native.write(path.with_suffix('.drawio'), encoding='unicode', xml_declaration=True)
    svg_text = path.read_text()
    fragment = '<div class="offboarding-actions" style="overflow-x:auto">' + svg_text + '</div>'
    path.with_suffix('.html').write_text(fragment)
    rows = ''.join('<tr>' + ''.join('<td>'+html.escape(v)+'</td>' for v in row) + '</tr>' for row in scenario_rows())
    preview = ROOT / 'work/offboarding-review/customer-actions.html'
    preview.parent.mkdir(exist_ok=True)
    preview.write_text('''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Switch or offboard</title><style>
    *{box-sizing:border-box}body{margin:0;font:16px/1.5 Arial,sans-serif;color:#222}main{max-width:1260px;margin:auto;padding:24px}h1{font-size:28px}table{border-collapse:collapse;width:100%;min-width:850px}th,td{padding:12px;border:1px solid #bbb;text-align:left;vertical-align:top}th{background:#eee}.table-scroll{overflow-x:auto}a{color:#075eaa}
    </style></head><body><main><h1>Customer actions: switching and offboarding</h1><p>A switch changes the platform used to send or receive new invoices. Offboarding ends selected access or services. The customer starts one switch request; Sage coordinates new setup and any old-service exit. Earlier work still needs someone responsible for it.</p>'''
    + build_settings() + '<h2>Switching and offboarding: detailed checks</h2>' + fragment + '<p>Switch setup uses existing onboarding APIs where suitable. <a href="SPEC-SEI-033.html#how-the-onboarding-apis-support-a-platform-switch">Read the API mapping and Spain checks</a>.</p><h2>Scenarios by customer action</h2><p>This table is generated from the customer scenarios in SPEC032 §1. Engineering must still confirm how each provider supports the required steps. Private-to-private switching remains disabled in current onboarding scope.</p><div class="table-scroll"><table><thead><tr><th>ID</th><th>Customer action</th><th>Category</th><th>Required result</th><th>Failure or recovery</th></tr></thead><tbody>'
    + rows + '</tbody></table></div><p>Source: <a href="../../specs/offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md">SPEC-SEI-032</a>; onboarding ownership: SPEC-SEI-037–039. No publication or status change.</p></main></body></html>')
    print(path.relative_to(ROOT))
    print(preview.relative_to(ROOT))


if __name__ == '__main__':
    build()
