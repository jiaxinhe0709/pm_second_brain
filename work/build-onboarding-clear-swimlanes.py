"""Main paths and key controls in the original swimlanes; detailed exceptions stay below."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET
from onboarding_swimlane_routes import finish

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('renderer',ROOT/'work/build-onboarding-scenario-diagrams.py')
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
node,edge=d.node,d.edge
DOC='../../specs/onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#'
ANCHORS={
 'ONB-01':'61-onb-01-capture-requested-functions','ONB-02':'62-onb-02-check-business-identity-and-authority',
 'ONB-12':'63-onb-12-coordinate-client-approval-and-evidence','ONB-10':'64-onb-10-assess-current-setup',
 'ONB-03':'65-onb-03-assess-prerequisites','ONB-04':'66-onb-04-publish-public-readiness',
 'ONB-05':'67-onb-05-configure-private-choice','ONB-06':'68-onb-06-prove-private-readiness',
 'ONB-07':'69-onb-07-cut-over-new-traffic','ONB-08':'610-onb-08-reconcile-and-recover',
 'ONB-11':'612-onb-11-return-results-and-required-actions','ONB-13':'613-onb-13-manage-portfolio-batch',
}

def add_controls(slug,nodes,edges):
 if slug=='onboarding-public-setup-swimlane':
  nodes.extend([
   node('correct',2,0,'Correct information or approval','ONB-02/12','Repeat only the affected check','conditional'),
   node('recover',3,2,'Check the original result','ONB-08','Resume safely or return next action','recovery')])
  edges.extend([
   edge('checks','correct','conditional',points=[(950,598),(950,282)],label='Missing information or approval',label_pos=(965,385)),
   edge('correct','checks','conditional',points=[(890,282),(890,598)],label='Corrected',label_pos=(805,420)),
   edge('checks','recover','recovery',points=[(1060,625),(1070,625),(1070,535),(1080,535)],label='Result unknown',label_pos=(1080,610)),
   edge('public','recover','recovery',points=[(1210,878),(1210,562)],label='Failed or unknown',label_pos=(1225,790)),
   edge('recover','save','recovery',points=[(1340,510),(1360,510)])])
 elif slug=='onboarding-private-setup-swimlane':
  nodes.extend([
   node('correct',2,0,'Correct settings or approval','ONB-05/12','Repeat only the affected check','conditional'),
   node('recover',5,2,'Check the original result','ONB-08','Pause affected work; repeat only if safe','recovery')])
  edges.extend([
   edge('setup','correct','conditional',points=[(950,598),(950,282)],label='Missing settings or approval',label_pos=(965,385)),
   edge('correct','setup','conditional',points=[(890,282),(890,598)],label='Corrected',label_pos=(805,420)),
   edge('provider','recover','recovery',points=[(1340,955),(1620,955),(1620,535),(1640,535)],label='Failed or unknown',label_pos=(1400,980)),
   edge('activate','recover','recovery',points=[(1770,598),(1770,562)],label='Failed or unknown',label_pos=(1785,585)),
   edge('recover','result','recovery',points=[(1770,458),(1770,370),(1920,370)],label='Result and next action',label_pos=(1785,355))])
  next(e for e in edges if (e['source'],e['target'])==('activate','result'))['points']=[(1900,650),(2100,650),(2100,422)]
 elif slug=='onboarding-client-approval-swimlane':
  nodes.extend([
   node('withdraw',3,2,'Approval or client access ends','ONB-12/02','Withdrawal or loss of role','conditional'),
   node('stop',4,2,'Stop affected future use','ONB-12/08','Check unknown earlier effects','recovery')])
  edges.extend([
   edge('withdraw','stop','recovery',points=[(1340,510),(1360,510)]),
   edge('stop','result','recovery',points=[(1490,458),(1490,370),(1920,370)],label='Return required action',label_pos=(1510,355))])
  next(e for e in edges if (e['source'],e['target'])==('reply','permission'))['points']=[(1340,230),(1630,230),(1630,585),(1490,585),(1490,598)]
  e=next(e for e in edges if (e['source'],e['target'])==('permission','resume'))
  e['points']=[(1620,650),(1650,650),(1650,562)];e['label_pos']=(1665,630)
  next(e for e in edges if (e['source'],e['target'])==('resume','result'))['points']=[(1900,510),(2100,510),(2100,422)]
 elif slug=='onboarding-accountant-batch-swimlane':
  nodes.extend([
   node('correct',4,0,'Correct the affected client','ONB-13/12','Other safe client items continue','conditional'),
   node('cancel',0,2,'Cancel selected pending work','ONB-13','Resolve effects before completion','conditional')])
  edges.extend([
   edge('run','correct','conditional',points=[(1530,458),(1530,282)],label='Client action required',label_pos=(1545,300)),
   edge('correct','run','conditional',points=[(1450,282),(1450,458)],label='Corrected: recheck',label_pos=(1320,420)),
   edge('cancel','result','conditional',points=[(370,562),(370,840),(1770,840),(1770,422)],label='Cancelled or action required',label_pos=(1050,865))])

def build(slug,title,description,nodes,edges,lanes,original,rows,notes):
 add_controls(slug,nodes,edges)
 width=240+280*max(n['col'] for n in nodes)+300
 lane_bottom=160+140*lanes;height=lane_bottom+430
 positions={n['key']:(240+n['col']*280,178+n['lane']*140,260,104) for n in nodes}
 for n in nodes:n['link']=DOC+ANCHORS[n['activity'].split('/')[0]]
 d.shared.WIDTH,d.shared.HEIGHT=width,height
 for e in edges:e['points']=e['points'] or d.shared.route(e,positions)
 path=d.build(slug,title,description,nodes,edges,spec=DOC+'6-feature-activities',positions=positions,
              width=width,height=height,lanes=d.LANES[:lanes],boundaries=notes,
              legend='Solid: main path · Dashed: alternative or correction · Darker grey: recovery · Details: table below')
 finish(path,edges)
 svg=ET.parse(path).getroot();ns='{http://www.w3.org/2000/svg}'
 ET.register_namespace('',ns[1:-1])
 # The common/scenario classification adds no decision in this overview.
 for e in list(svg):
  if e.tag==ns+'text' and e.get('y')=='143':
   e.text='Read the main path from left to right. Swimlanes show proposed roles; Engineering must confirm service ownership.'
 native=ET.parse(path.with_suffix('.drawio')).getroot();root=native.find('.//root')
 for e in native.iter('mxCell'):
  if e.get('id')=='behaviour-legend':
   e.set('value','Read the main path from left to right. Proposed roles; Engineering must confirm service ownership.')
 def txt(x,y,value,size=14,bold=False):
  attrs={'x':str(x),'y':str(y),'font-family':'Arial, sans-serif','font-size':str(size),'fill':'#333333'}
  if bold:attrs['font-weight']='bold'
  ET.SubElement(svg,ns+'text',attrs).text=value
 def cell(key,value,x,y,w,h,bold=False):
  c=ET.SubElement(root,'mxCell',id=key,value=value,parent='1',vertex='1',
    style='text;html=0;whiteSpace=wrap;align=left;verticalAlign=middle;fontSize=14;spacing=8;'+('fontStyle=1;' if bold else ''))
  ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
 txt(28,lane_bottom+32,'Additional checks and next actions',18,True)
 cell('exception-title','Additional checks and next actions',28,lane_bottom+10,width-56,30,True)
 top=lane_bottom+48;columns=[28,410,740];widths=[382,330,width-768]
 ET.SubElement(svg,ns+'rect',x='20',y=str(top),width=str(width-40),height=str(32+52*len(rows)),fill='#fafafa',stroke='#aaaaaa')
 for i,heading in enumerate(['When','Who acts','Next action']):
  txt(columns[i]+8,top+22,heading,14,True);cell('exception-heading-'+str(i),heading,columns[i],top,widths[i],32,True)
 for i,row in enumerate(rows):
  y=top+32+i*52
  ET.SubElement(svg,ns+'path',d=f'M 20,{y} L {width-20},{y}',stroke='#cccccc',fill='none')
  for j,value in enumerate(row):
   txt(columns[j]+8,y+30,value,14)
   cell(f'exception-{i}-{j}',value,columns[j],y,widths[j],52)
 path.write_text(ET.tostring(svg,encoding='unicode'))
 ET.indent(native);path.with_suffix('.drawio').write_text(ET.tostring(native,encoding='unicode',xml_declaration=True))
 original_root=ET.parse(ROOT/f'assets/diagrams/{original}.drawio')
 old_lanes=[e.get('value') for e in original_root.iter('mxCell') if e.get('id','').startswith('lane-label')]
 current_lanes=[e.get('value') for e in native.iter('mxCell') if e.get('id','').startswith('lane-label')]
 assert old_lanes==current_lanes
 return dict(svg=str(path.relative_to(ROOT)),png=str(path.with_suffix('.png').relative_to(ROOT)),
   drawio=str(path.with_suffix('.drawio').relative_to(ROOT)),nodes=len(nodes),connections=len(edges),
   original_nodes=len(list(original_root.iter('object'))),original_lanes_preserved=True,swimlanes=lanes,
   width=width,height=height,title=title,exception_rows=len(rows),key_controls_shown=True)

def build_all():
 reports=[]
 public=[
  node('choose',0,0,'1. Choose business and service','ONB-01','Customer or authorised accountant'),
  node('reuse',1,2,'2. Reuse SXS dataset and setup','ONB-10','Use the resolved company dataset'),
  node('checks',2,3,'3. Check identity and access','ONB-02/03','NIF, permission; Tax credential if needed'),
  node('public',3,5,'4. Check public service access','ONB-03','Use supported checks for this function'),
  node('save',4,2,'5. Save public check results','ONB-04','Save readiness and evidence'),
  node('result',5,1,'6. Show result and next action','ONB-11','Per function; no route activation','outcome'),
 ]
 reports.append(build('onboarding-public-setup-swimlane','Public onboarding: setup, correction and recovery',
  'Before setup: product integrates SXS and Tax Connections Service. Phase 1 checks public access.',public,
  [edge(a,b) for a,b in [('choose','reuse'),('reuse','checks'),('checks','public'),('public','save'),('save','result')]],
  6,'onboarding-public-readiness-process',[
   ('Information or approval is missing','Customer / accountant','Correct it, then repeat the affected check. ONB-02/03/12.'),
   ('A check fails or its result is unknown','E-Invoice owner','Check the original result. Repeat only when safe. ONB-08.'),
   ('The case cannot be resolved','Operations / support','Keep affected work pending; show its owner and next action. ONB-08/11.'),
  ],[
   'Check the business NIF, caller and permission separately. Use a suitable in-date certificate only where required.',
   'No public enrolment call, test invoice or route activation is assumed. A failed lookup does not prove missing setup.',
   'Keep other valid functions available. Full rules and acceptance checks remain in SPEC038 §7.'
  ]))
 private=[
  node('choose',0,0,'1. Choose provider and account','ONB-01','Supported later-phase provider only'),
  node('reuse',1,2,'2. Reuse SXS dataset and setup','ONB-02/10','Keep the SXS dataset and provider'),
  node('setup',2,3,'3. Connect and check access','ONB-05/06','Tax / Connections credential if needed'),
  node('provider',3,5,'4. Check provider status','ONB-06','Continue only when all checks pass'),
  node('change',4,2,'Change the route?','ONB-07',kind='decision'),
  node('activate',5,3,'5. Activate; keep earlier access','ONB-07/09','Only when supported and authorised','conditional'),
  node('result',6,1,'6. Show result and next action','ONB-11','Separate readiness from activation','outcome'),
 ]
 edges=[edge(a,b) for a,b in [('choose','reuse'),('reuse','setup'),('setup','provider'),('provider','change')]]
 edges += [edge('change','activate','conditional',label='Yes',label_pos=(1630,590)),
  edge('change','result','conditional',points=[(1490,458),(1490,300),(2050,300),(2050,318)],label='No: keep current route',label_pos=(1660,285)),edge('activate','result')]
 reports.append(build('onboarding-private-setup-swimlane','Private onboarding: setup, recovery and route decision',
  'Before setup: product integrates SXS and Tax Connections Service. Later phase; keep the chosen provider.',private,edges,
  6,'onboarding-private-route-process',[
   ('Settings or approval is missing','Customer / accountant','Correct it, then repeat the affected check. ONB-05/12.'),
   ('A change fails or has an unknown result','E-Invoice owner','Check earlier effects before repetition or an activation claim. ONB-08.'),
   ('The case cannot be resolved','Operations / support','Keep affected work pending; show its owner and next action. ONB-08/11.'),
   ('A call can redirect traffic','Customer + routing owner','Before the call: confirm permission, readiness and earlier-invoice access.'),
  ],[
   'A saved connection alone does not prove readiness. Confirm the agreed start point before a route change.',
   'Keep earlier invoices linked to their original route. Private A to Private B stays disabled.',
   'Operator interconnection is separate from customer setup. Full rules and acceptance checks remain in SPEC038 §7.'
  ]))
 approval=[
  node('valid',0,3,'Approval valid?','ONB-02/12',kind='decision'),
  node('request',1,2,'1. Save the approval request','ONB-12','Business, action and request version'),
  node('show',2,1,'2. Show the requested decision','ONB-12/11','Ask an eligible approver'),
  node('reply',3,0,'3. Approve or decline','ONB-12','Respond to the current request'),
  node('permission',4,3,'Approved and allowed?','ONB-02/12',kind='decision'),
  node('resume',5,2,'4. Resume the affected check','ONB-12','Recheck permission and access'),
  node('result',6,1,'5. Show result and next action','ONB-11','Approval alone is not readiness','outcome'),
 ]
 edges=[edge('valid','request','conditional',label='No',label_pos=(510,590)),
  edge('valid','resume',points=[(370,702),(370,735),(1770,735),(1770,562)],label='Yes: reuse current evidence',label_pos=(900,760)),
  edge('request','show'),edge('show','reply'),edge('reply','permission'),
  edge('permission','resume',label='Yes',label_pos=(1630,590)),
  edge('permission','result','conditional',points=[(1490,702),(1490,715),(2200,715),(2200,395),(2180,395)],label='No or unknown',label_pos=(1900,705)),edge('resume','result')]
 reports.append(build('onboarding-client-approval-swimlane','Approval: reuse, request or withdraw',
  'Reuse valid approval, request a missing decision, or stop affected use when approval ends.',approval,edges,
  4,'onboarding-client-approval-process',[
   ('Waiting, declined, expired or stale','Product + approver','Keep affected work pending; show the required action. ONB-12/11.'),
   ('Information changes','Customer / accountant','Correct it; make a new request only when allowed. ONB-12.'),
   ('Approval or client access ends','E-Invoice owner','Stop affected future use; resolve unknown earlier effects. ONB-12/08.'),
  ],[
   'Check the response and actual official authority separately. A local approval response alone proves neither.',
   'Keep other permitted functions available. Approval does not prove readiness or activate a route.',
   'Request states, approvers and evidence checks remain in SPEC038 §6.3 and §7.'
  ]))
 batch=[
  node('choose',0,0,'1. Choose clients and functions','ONB-13','Current firm and accountant identity'),
  node('valid',1,2,'Valid request list?','ONB-13',kind='decision'),
  node('reject',1,1,'Reject invalid list','ONB-13','Do not start client work','outcome'),
  node('save',2,2,'2. Save list and return receipt','ONB-13/01','Resume unfinished items after restart'),
  node('access',3,3,'Client work allowed?','ONB-02',kind='decision'),
  node('run',4,2,'3. Run each client setup','ONB-10/03–07','Recheck before protected actions'),
  node('result',5,1,'4. Show permitted results','ONB-13/11','Keep each client result separate','outcome'),
 ]
 edges=[edge('choose','valid'),edge('valid','reject','conditional',label='No',label_pos=(675,445)),
  edge('valid','save',label='Yes',label_pos=(790,445)),edge('save','access'),
  edge('access','run',label='Yes',label_pos=(1350,590)),edge('run','result'),
  edge('access','result','conditional',points=[(1210,702),(1210,735),(1900,735),(1900,370),(1900,370)],label='No: return action or denial',label_pos=(1420,760))]
 # Enter the outcome from its right side; avoid a zero-length final segment.
 edges[-1]['points']=[(1210,702),(1210,735),(1920,735),(1920,370),(1900,370)]
 reports.append(build('onboarding-accountant-batch-swimlane','Accountant batch: setup, correction and cancellation',
  'Save the request list, then check and process each client independently.',batch,edges,
  5,'onboarding-portfolio-batch-process',[
   ('One client needs action','Customer / accountant','Correct only that client; other safe clients can continue. ONB-13/12.'),
   ('The accountant cancels selected work','E-Invoice owner','Stop permitted pending steps; retain completed work. ONB-13.'),
   ('An earlier effect is unknown','E-Invoice owner','Resolve it before completing cancellation. ONB-08.'),
   ('Permission or client access ends','Identity + product','Stop affected work and access; show only permitted progress. ONB-02/13.'),
  ],[
   'A receipt proves saved intake, not readiness. Reuse unchanged requests without duplicate effects.',
   'Check permission for each client before work and result access. One client must not expose or fail another.',
   'Batch states, counts, visibility and full acceptance checks remain in SPEC038 §7.'
  ]))
 return reports

if __name__=='__main__':
 import json
 print(json.dumps(build_all(),indent=2))
