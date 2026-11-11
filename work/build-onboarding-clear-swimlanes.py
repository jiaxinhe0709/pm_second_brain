"""Main paths and key controls in the original swimlanes; detailed exceptions stay below."""
from pathlib import Path
import importlib.util
import re
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
   edge('checks','correct','conditional',label='Missing input / approval'),
   edge('correct','request','conditional',label='Corrected: resume request'),
   edge('checks','recover','recovery',label='Unknown check result'),
   edge('public','recover','recovery',label='Failed / unknown'),
   edge('recover','save','recovery')])
 elif slug=='onboarding-private-setup-swimlane':
  nodes.extend([
   node('correct',2,0,'Correct settings or approval','ONB-05/12','Repeat only the affected check','conditional'),
   node('recover',6,2,'Check the original result','ONB-08','Pause affected work; repeat only if safe','recovery')])
  edges.extend([
   edge('setup','correct','conditional',label='Missing input / approval'),
   edge('correct','request','conditional',label='Corrected: resume request'),
   edge('account','recover','recovery',label='Account status unknown'),
   edge('onboard','recover','recovery',label='Incomplete / unknown'),
   edge('provider','recover','recovery',label='Failed / unknown'),
   edge('activate','recover','recovery',label='Failed / unknown'),
   edge('recover','result','recovery',label='Result and next action')])
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
 primary=slug in {'onboarding-shared-prerequisites-swimlane','onboarding-public-setup-swimlane','onboarding-private-setup-swimlane'}
 if not primary:add_controls(slug,nodes,edges)
 if primary:
  # Keep exception rules in the table. Give the main handoffs their own gutters.
  if slug=='onboarding-private-setup-swimlane':
   columns={'choose':0,'load':0,'account':1,'onboard':1,
            'request':2,'setup':2,'progress':3,'track':3,'provider':3,
            'change':4,'confirm':5,'activate':5,'result':6}
   for n in nodes:n['col']=columns[n['key']]
  step,node_width,lane_height=350,280,180
  width=240+step*max(n['col'] for n in nodes)+node_width+80
  lane_bottom=160+lane_height*lanes
  height=lane_bottom+max(440,((48+32+52*len(rows)+150+19)//20)*20)
  positions={n['key']:(240+n['col']*step,200+n['lane']*lane_height,node_width,104) for n in nodes}
  for e in edges:e['points']=None;e['label_pos']=None
 else:
  lane_height=140
  width=240+280*max(n['col'] for n in nodes)+300
  lane_bottom=160+140*lanes;height=lane_bottom+430
  positions={n['key']:(240+n['col']*280,178+n['lane']*140,260,104) for n in nodes}
 if primary:
  for n in nodes:n['title']=re.sub(r'^\d+\.\s*','',n['title'])
 for n in nodes:n['link']=DOC+ANCHORS[n['activity'].split('/')[0]]
 if primary and slug=='onboarding-private-setup-swimlane':
  ax,ay,aw,ah=positions['account'];rx,ry,rw,rh=positions['request']
  ox,oy,ow,oh=positions['onboard'];cx,cy,cw,ch=positions['change']
  fx,fy,fw,fh=positions['confirm'];zx,zy,zw,zh=positions['result']
  routes={
   ('account','request'): ([(ax+aw,ay+ah/2),(ax+aw+30,ay+ah/2),(ax+aw+30,ry+rh/2),(rx,ry+rh/2)],'Yes: existing account',(ax+aw+42,ay+ah/2-14)),
   ('account','onboard'): ([(ax+aw/2,ay+ah),(ox+ow/2,oy)],'No: new account needed',(ax+aw/2-190,oy-180)),
   ('onboard','request'): ([(ox+ow,oy+oh/2),(ax+aw+30,oy+oh/2),(ax+aw+30,ry+rh/2),(rx,ry+rh/2)],'Onboarding confirmed',(ax+aw+42,oy-180)),
   ('change','confirm'): ([(cx+cw,cy+ch/2),(cx+cw+30,cy+ch/2),(cx+cw+30,fy+fh/2),(fx,fy+fh/2)],'Yes — requested',(cx+cw+42,cy+ch/2-14)),
   ('change','result'): ([(cx+cw,cy+ch/2),(zx-40,cy+ch/2),(zx-40,zy+zh/2),(zx,zy+zh/2)],'No — setup only',(cx+cw+230,cy+ch/2-14)),
  }
  for e in edges:
   if (e['source'],e['target']) in routes:
    e['points'],e['label'],e['label_pos']=routes[e['source'],e['target']]
 d.shared.WIDTH,d.shared.HEIGHT=width,height
 for e in edges:e['points']=e['points'] or d.shared.route(e,positions)
 # Keep labels outside activity boxes after adding product request handoffs.
 occupied=list(positions.values())
 for e in edges:
  if e['label'] and e['label_pos'] is not None:
   x,y=e['label_pos'];occupied.append((x,y-16,len(e['label'])*6.6+12,22))
 for e in edges:
  if not e['label'] or e['label_pos'] is not None:continue
  tw=len(e['label'])*6.6+12
  candidates=[]
  for a,b in zip(e['points'],e['points'][1:]):
   mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
   if a[1]==b[1]:candidates.extend([(mx-tw/2,my-10),(mx-tw/2,my+24)])
   else:candidates.extend([(mx+12,my),(mx-tw-12,my)])
  # Tight adjacent lanes may need the label in the neighbouring whitespace.
  for a,b in zip(e['points'],e['points'][1:]):
   mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
   for dy in (-28,28,-48,48,-70,70):
    candidates.extend([(mx+12,my+dy),(mx-tw-12,my+dy),(mx-tw/2,my+dy)])
  for x,y in candidates:
   if x<225 or x+tw>width-20 or y<165 or y>lane_bottom:continue
   if any(x<X+W and x+tw>X and y-16<Y+H and y+4>Y for X,Y,W,H in occupied):continue
   e['label_pos']=(x,y);occupied.append((x,y-16,tw,22));break
  if e['label_pos'] is None:raise ValueError(('No label space',slug,e))
 path=d.build(slug,title,description,nodes,edges,spec=DOC+'6-feature-activities',positions=positions,
              width=width,height=height,lanes=d.LANES[:lanes],boundaries=notes,
              legend=('Solid: main path · Dashed: selected account or platform-use path · Exceptions: table below' if primary else
                      'Solid: main path · Dashed: alternative or correction · Darker grey: recovery · Details: table below'))
 finish(path,edges)
 svg=ET.parse(path).getroot();ns='{http://www.w3.org/2000/svg}'
 ET.register_namespace('',ns[1:-1])
 if primary:
  # The shared renderer uses 140px lanes. Expand only these three current views.
  for element in svg:
   if element.tag==ns+'rect' and element.get('height')=='140':
    old_y=float(element.get('y'));index=round((old_y-160)/140)
    element.set('y',str(160+index*lane_height));element.set('height',str(lane_height))
   if element.tag==ns+'text' and element.get('x')=='120':
    old_y=float(element.get('y'));index=int((old_y-160)//140)
    if 0<=index<lanes:element.set('y',str(old_y+index*(lane_height-140)+(lane_height-140)/2))
 # The common/scenario classification adds no decision in this overview.
 for e in list(svg):
  if e.tag==ns+'text' and e.get('y')=='143':
   e.text='Follow the solid arrows through the main path. Swimlanes show proposed roles; Engineering must confirm service ownership.'
 native=ET.parse(path.with_suffix('.drawio')).getroot();root=native.find('.//root')
 for e in native.iter('mxCell'):
  if primary and (e.get('id','').startswith('lane-') or e.get('id','').startswith('lane-label-')):
   index=int(e.get('id').rsplit('-',1)[1]);geometry=e.find('mxGeometry')
   geometry.set('y',str(160+index*lane_height));geometry.set('height',str(lane_height))
  if e.get('id')=='behaviour-legend':
   e.set('value','Follow the solid arrows through the main path. Proposed roles; Engineering must confirm service ownership.')
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
 original_root=ET.parse(ROOT/f'assets/diagrams/{original}.drawio') if original else None
 if original_root is not None:
  old_lanes=[e.get('value') for e in original_root.iter('mxCell') if e.get('id','').startswith('lane-label')]
  current_lanes=[e.get('value') for e in native.iter('mxCell') if e.get('id','').startswith('lane-label')]
  assert old_lanes==current_lanes
 return dict(svg=str(path.relative_to(ROOT)),png=str(path.with_suffix('.png').relative_to(ROOT)),
   drawio=str(path.with_suffix('.drawio').relative_to(ROOT)),nodes=len(nodes),connections=len(edges),
   original_nodes=len(list(original_root.iter('object'))) if original_root is not None else None,
   original_lanes_preserved=True if original else None,swimlanes=lanes,
   exception_detail_in_table=primary,lane_height=lane_height,
   width=width,height=height,title=title,exception_rows=len(rows),key_controls_shown=True)

def build_shared():
 nodes=[
  node('choose',0,0,'Select the business or client','ONB-01','Use the existing selection if available'),
  node('load',0,1,'Request current setup','ONB-10','Resolve mapping via product / SXS first'),
  node('dataset',1,2,'Assess permitted saved setup','ONB-10','Use the confirmed business/client mapping'),
  node('show',1,1,'Show current e-invoicing setup','ONB-10/11','Permitted setup; readiness is separate'),
  node('action',2,0,'Choose the requested action','ONB-01','Review / connect or add / enabled switch'),
  node('request',2,1,'Request shared checks','ONB-01/03','Business/client, functions and environment'),
  node('coordinate',2,2,'Coordinate required checks','ONB-02/03','Keep the caller and business distinct'),
  node('identity',2,3,'3. Check NIF and permission','ONB-02','Check business and caller separately'),
  node('credential',3,3,'4. Check required credential','ONB-03','Skip if the selected function needs none'),
  node('collect',4,2,'Return shared check results','ONB-03/11','Passed checks or missing item and owner'),
  node('result',4,1,'5. Show shared check result','ONB-11','Pass: continue public/private setup','outcome'),
 ]
 return build('onboarding-shared-prerequisites-swimlane',
  'Shared onboarding checks: company, permission and credentials',
  'Phases 1–3. Before customer setup: product integrations with SXS and Tax / Connections Service are available.',
  nodes,[edge(a,b) for a,b in [('choose','load'),('load','dataset'),('dataset','show'),('show','action'),('action','request'),('request','coordinate'),('coordinate','identity'),('identity','credential'),('credential','collect'),('collect','result')]],
  4,None,[
   ('Company mapping is missing','Product / SXS owner','Confirm it is missing, then complete qualified setup. ONB-10.'),
   ('Information or approval is missing','Customer / accountant','Correct it, then repeat the affected check. ONB-02/12.'),
   ('Required certificate is missing or unsuitable','Tax / credential owner','Use the qualified correction or provisioning path. ONB-03.'),
   ('Lookup fails or an earlier result is unknown','E-Invoice owner','Keep pending with an owner; check the original result. ONB-08/11.'),
  ],[
   'Continue the selected public or private checks only after the required shared checks pass. No route activation occurs here.',
   'Reuse valid evidence for the business, action and environment. An unavailable lookup does not prove missing setup.',
   'Open: Spain resource mapping and Tax / E-Invoice ID relationships require owner confirmation. SPEC039 GAP-01/02/06.',
  ])

def build_all(primary_only=False):
 reports=[build_shared()]
 public=[
  node('choose',0,0,'Review requested public functions','ONB-01','Use the selected business/client context'),
  node('load',0,1,'Load current public setup','ONB-10','Discover only missing service/setup details'),
  node('reuse',1,2,'2. Reuse SXS dataset and setup','ONB-10','Use the resolved company dataset'),
  node('request',1,1,'Request public access check','ONB-03/04','Selected business, action and environment'),
  node('coordinate',2,2,'Coordinate public access check','ONB-03/04','Reuse matching current evidence'),
  node('checks',2,3,'3. Check identity and access','ONB-02/03','NIF, permission; Tax credential if needed'),
  node('public',3,5,'4. Check public service access','ONB-03','Use supported checks for this function'),
  node('save',4,2,'5. Save public check results','ONB-04','Save readiness and evidence'),
  node('result',5,1,'Show result and next action','ONB-11','Readiness / pending / owner; use separate','outcome'),
 ]
 reports.append(build('onboarding-public-setup-swimlane','Public onboarding: setup, correction and recovery',
  'Before setup: product integrates SXS and Tax Connections Service. Phase 1 checks public access.',public,
  [edge(a,b) for a,b in [('choose','load'),('load','reuse'),('reuse','request'),('request','coordinate'),('coordinate','checks'),('checks','public'),('public','save'),('save','result')]],
  6,'onboarding-public-readiness-process',[
   ('Information or approval is missing','Customer / accountant','Correct it, then repeat the affected check. ONB-02/03/12.'),
   ('A check fails or its result is unknown','E-Invoice owner','Check the original result. Repeat only when safe. ONB-08.'),
   ('The case cannot be resolved','Operations / support','Keep affected work pending; show its owner and next action. ONB-08/11.'),
  ],[
   'Check the business NIF, caller and permission separately. Use a suitable in-date certificate only where required.',
   'No public enrolment call or test invoice is assumed. Results return to the common ONB-07 platform-use decision; setup alone activates nothing.',
   'Keep other valid functions available. Full rules and acceptance checks remain in SPEC038 §7.'
  ]))
 private=[
  node('choose',0,0,'Choose the private platform','ONB-01','For selected business or accountant client'),
  node('load',0,1,'Load current private setup','ONB-10','Use confirmed SXS mapping and service ID'),
  node('request',2,1,'Submit connection setup','ONB-05','Confirmed account; submit only missing work'),
  node('account',1,2,'Account on chosen platform?','ONB-05/10',kind='decision'),
  node('onboard',2,5,'Complete provider onboarding','ONB-05','No account: qualified process or handoff'),
  node('setup',2,3,'Set up or reuse Sage connection','ONB-05','Keep valid setup; add only missing work'),
  node('progress',3,1,'Read setup progress','ONB-06/11','Keep request and returned connection refs'),
  node('track',3,2,'Confirm private access','ONB-06','Assess required evidence for each function'),
  node('provider',3,5,'Provide access evidence','ONB-06','Qualified platform checks or current evidence'),
  node('change',4,2,'Start or change platform use?','ONB-07',kind='decision'),
  node('confirm',5,1,'Submit confirmed platform use','ONB-07','Requested scope and agreed start only','conditional'),
  node('activate',5,3,'Start or change platform use','ONB-07/09','Enabled, authorised; keep earlier access','conditional'),
  node('result',6,1,'6. Show result and next action','ONB-11','Separate readiness from activation','outcome'),
 ]
 edges=[edge(a,b) for a,b in [('choose','load'),('load','account'),('request','setup'),('setup','progress'),('progress','track'),('track','provider'),('provider','change')]]
 edges += [edge('account','request','conditional',label='Yes: existing account'),
  edge('account','onboard','conditional',label='No: new account needed'),
  edge('onboard','request','conditional',points=[(1060,930),(1070,930),(1070,440),(930,440),(930,422)],label='Onboarding confirmed',label_pos=(1080,800)),
  edge('change','confirm','conditional',points=[(1490,458),(1490,430),(1770,430),(1770,422)],label='Yes: requested and enabled',label_pos=(1490,453)),edge('confirm','activate','conditional'),
  edge('change','result','conditional',points=[(1490,562),(1490,585),(1910,585),(1910,370),(1920,370)],label='No — setup only',label_pos=(1640,574)),edge('activate','result')]
 reports.append(build('onboarding-private-setup-swimlane','Private onboarding: setup, recovery and platform use',
  'Use the selected business/client and chosen provider. Existing and new accounts both need qualified Sage access.',private,edges,
  6,'onboarding-private-route-process',[
   ('Settings or approval is missing','Customer / accountant','Correct it, then repeat the affected check. ONB-05/12.'),
   ('Account or onboarding status is unconfirmed','Product / provider owner','Keep pending; obtain evidence before connection. Do not create a duplicate account. ONB-05/08.'),
   ('A change fails or has an unknown result','E-Invoice owner','Check earlier effects before repetition or an activation claim. ONB-08.'),
   ('The case cannot be resolved','Operations / support','Keep affected work pending; show its owner and next action. ONB-08/11.'),
   ('A call can redirect traffic','Customer + routing owner','Before the call: confirm permission, readiness and earlier-invoice access.'),
  ],[
   'Reuse valid setup and evidence; complete only affected work. Setup only preserves any selection; if none exists, it activates none.',
   'Keep earlier invoices linked to their original route. Private A to Private B stays disabled.',
   'Operator interconnection is separate from customer setup. Full rules and acceptance checks remain in SPEC038 §7.'
  ]))
 if primary_only:return reports
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
 import argparse,json
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--shared-only',action='store_true',help='Build only the shared prerequisites diagram.')
 parser.add_argument('--primary-only',action='store_true',help='Build only the three inline SPEC038 diagrams.')
 args=parser.parse_args()
 print(json.dumps([build_shared()] if args.shared_only else build_all(primary_only=args.primary_only),indent=2))
