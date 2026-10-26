"""Small business process views for SPEC037/038; archived diagram assets stay untouched."""
from pathlib import Path
import json,textwrap,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/diagrams'
PREFIX='../../specs/onboarding-and-connectivity/'
LOGICAL=PREFIX+'SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md'
SUMMARY=PREFIX+'SPEC-SEI-037-customer-onboarding-and-connectivity-solution-summary.md'
FLOWS=[
 dict(slug='onboarding-summary-setup-process',title='Onboarding: reuse setup and return the next action',subtitle='Customer or accountant uses one journey for the selected business.',source=SUMMARY+'#6-end-to-end-workflow',nodes=[
 ('Customer / accountant','Choose the business and setup','Public, private, review or a supported change.','ONB-01','61-onb-01-capture-requested-functions',False),
 ('Sage','Check identity and permission','Check the NIF and caller separately; check a certificate only if required.','ONB-02/03','62-onb-02-check-business-identity-and-authority',False),
 ('Sage','Reuse valid existing setup','Ask only for missing, changed or out-of-date information.','ONB-10','64-onb-10-assess-current-setup',False),
 ('Sage / platform owner','Complete the selected setup checks','Public access: Phase 1. Private connection: later phase, supported providers only.','ONB-04/05/06','65-onb-03-assess-prerequisites',False),
 ('Sage → product','Show the result and next action','Return each function’s result, missing work and who must act.','ONB-11','612-onb-11-return-results-and-required-actions',False),
 ],notes=[
 'Missing approval uses ONB-12; an unknown earlier result uses ONB-08. Accountant batches use ONB-13.',
 'Connection and readiness do not activate a route. A route change needs separate permission and earlier-invoice access.',
 'Private A to Private B stays disabled. These are process steps; SPEC039 states what code/API can be reused.'
 ]),
 dict(slug='onboarding-logical-public-setup-process',title='Public setup: check Sage access',subtitle='Phase 1. Start with the business, requested public service and environment.',source=LOGICAL+'#65-onb-03-assess-prerequisites',nodes=[
 ('Customer / accountant','Choose the business and public service','Use saved information; ask only for missing or changed values.','ONB-01','61-onb-01-capture-requested-functions',False),
 ('Sage / Identity','Check the business tax ID (NIF) and permission','Identify the business and caller separately; check permission for this action.','ONB-02','62-onb-02-check-business-identity-and-authority',False),
 ('Sage','Check existing setup','Keep valid evidence. A failed lookup does not prove setup is missing.','ONB-10','64-onb-10-assess-current-setup',False),
 ('Sage / Tax Service','Check the certificate, if required','Reuse a suitable in-date certificate without exposing its private key.','ONB-03','65-onb-03-assess-prerequisites',True),
 ('Sage / public integration owner','Check that Sage can use the public service','Check that Sage supports the selected public service and can use it for this business.','ONB-03/04','66-onb-04-publish-public-readiness',False),
 ('Sage → product','Show what is ready and who must act','Name any missing check and who must act; keep other unaffected valid setup.','ONB-04/11','612-onb-11-return-results-and-required-actions',False),
 ],notes=[
 'If a check fails, return what is missing and who must act; correct it and repeat that check. Unknown effects use ONB-08.',
 'No public enrolment operation, test invoice or route activation is assumed. See §6.5–6.6 for requirements and acceptance.'
 ]),
 dict(slug='onboarding-logical-private-setup-process',title='Private setup: keep or connect the chosen provider',subtitle='Later phase only. Confirm provider support and the customer’s permission first.',source=LOGICAL+'#67-onb-05-configure-private-choice',nodes=[
 ('Customer / accountant','Choose the supported provider account','Keep the existing provider unless a supported change was requested.','ONB-01/05','67-onb-05-configure-private-choice',False),
 ('Sage','Check the NIF, permission and required certificate','Reuse the shared checks and valid existing evidence.','ONB-02/03/10','65-onb-03-assess-prerequisites',False),
 ('Sage / connection owner','Reuse or add the missing connection','Before changing routing, confirm permission and access to earlier invoices.','ONB-05','67-onb-05-configure-private-choice',False),
 ('Sage / provider','Check connection status and required access','Reuse valid results; check missing or old evidence for each address/function. A saved connection alone is insufficient.','ONB-06','68-onb-06-prove-private-readiness',False),
 ('Routing owner','Change the route only when needed','Change only the agreed work; confirm when it takes effect and keep access to earlier invoices.','ONB-07/09','69-onb-07-cut-over-new-traffic',True),
 ('Sage → product','Show setup status and who must act','Show what is ready; confirm any route change separately; name the owner of pending work.','ONB-11','612-onb-11-return-results-and-required-actions',False),
 ],notes=[
 'If setup is unchanged, keep the current route. Private A to Private B stays disabled.',
 'Failed or unknown changes use ONB-08 before repetition. Operator interconnection is a separate process; see §7.'
 ]),
 dict(slug='onboarding-logical-approval-process',title='Approval: request only the missing decision',subtitle='Use only when the selected action lacks valid approval or evidence.',source=LOGICAL+'#63-onb-12-coordinate-client-approval-and-evidence',nodes=[
 ('Sage','Check whether approval is already valid','If valid evidence already covers the action, skip a new request and continue the checks.','ONB-02/12','63-onb-12-coordinate-client-approval-and-evidence',False),
 ('Sage → eligible approver','Save and show the missing approval request','Identify the business, action and request version.','ONB-12','63-onb-12-coordinate-client-approval-and-evidence',True),
 ('Eligible approver','Approve or decline','Only the person allowed to decide may respond; an invitation proves no authority.','ONB-12','63-onb-12-coordinate-client-approval-and-evidence',True),
 ('Sage / Identity','Check the response and actual permission','Local approval alone does not establish official authority.','ONB-12/02','62-onb-02-check-business-identity-and-authority',False),
 ('Sage → product','Resume the check or return the next action','Declined, expired or missing evidence keeps only the affected work pending.','ONB-11/12','612-onb-11-return-results-and-required-actions',False),
 ],notes=[
 'Withdrawal or loss of client access stops affected future use. Check possible earlier effects under ONB-08.',
 'Approval is separate from readiness and activation. Exact request states remain in §7.'
 ]),
 dict(slug='onboarding-logical-batch-process',title='Accountant batch: keep each client independent',subtitle='Use only for a list of clients; one client does not need batch processing.',source=LOGICAL+'#613-onb-13-manage-portfolio-batch',nodes=[
 ('Authorised accountant','Select clients and requested functions','Use the current firm and actor identity.','ONB-13','613-onb-13-manage-portfolio-batch',False),
 ('Sage','Validate the request list','Reject invalid or conflicting entries before client work starts.','ONB-13','613-onb-13-manage-portfolio-batch',False),
 ('Sage','Save the list and return a receipt','A receipt confirms saved intake, not client readiness. Resume incomplete work after restart.','ONB-13/01','613-onb-13-manage-portfolio-batch',False),
 ('Sage / Identity','Check each client’s permission','Recheck before work and result access; deny unlinked clients safely.','ONB-02','62-onb-02-check-business-identity-and-authority',False),
 ('Sage','Run each allowed client’s setup','One client needing action must not stop other safe clients.','ONB-10/03–07','64-onb-10-assess-current-setup',False),
 ('Sage → product','Show permitted results and next actions','Show only clients and progress the caller may currently access.','ONB-11/13','613-onb-13-manage-portfolio-batch',False),
 ],notes=[
 'Correct or cancel only the selected authorised items; keep other completed work. Unknown effects prevent final cancellation.',
 'An unchanged repeated batch reuses its receipt. Exact states, counts and visibility rules remain in §7.'
 ]),
]
ET.register_namespace('', 'http://www.w3.org/2000/svg')

def build(flow):
 width=1040;start=165;step=154;box_x=110;box_w=820;box_h=112
 foot_y=start+len(flow['nodes'])*step+12
 notes=[]
 for line in flow['notes']:notes.extend(textwrap.wrap(line,126))
 height=foot_y+len(notes)*22+45
 svg=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(width),height=str(height),viewBox=f'0 0 {width} {height}',role='img',attrib={'aria-label':flow['title']})
 ET.SubElement(svg,'title').text=flow['title'];ET.SubElement(svg,'desc').text=flow['subtitle']+' Main steps only. Detailed requirements and exceptions stay in SPEC038.'
 ET.SubElement(svg,'rect',x='8',y='8',width=str(width-16),height=str(height-16),rx='8',fill='white',stroke='#777777')
 native=ET.Element('mxfile',host='app.diagrams.net',type='device',version='24.7.17');diagram=ET.SubElement(native,'diagram',id=flow['slug'],name=flow['title']);graph=ET.SubElement(diagram,'mxGraphModel',page='1',pageWidth=str(width),pageHeight=str(height));root=ET.SubElement(graph,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
 def cell(key,value,x,y,w,h,style,link=None):
  parent=root
  if link:parent=ET.SubElement(root,'object',id=key,label=value,link=link);attrs={}
  else:attrs={'id':key,'value':value}
  c=ET.SubElement(parent,'mxCell',**attrs,parent='1',vertex='1',style=style);ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
 def text(x,y,value,size=17,anchor='start',color='#343434',parent=svg):
  ET.SubElement(parent,'text',x=str(x),y=str(y),fill=color,attrib={'font-family':'Arial, sans-serif','font-size':str(size),'text-anchor':anchor}).text=value
 text(32,47,flow['title'],25);text(32,81,flow['subtitle'],16)
 text(32,116,'Main steps in order. Dashed box: only when required. These are process roles, not service deployments.',14,color='#626262')
 cell('heading',flow['title']+'\n'+flow['subtitle'],32,22,width-64,72,'text;html=0;whiteSpace=wrap;align=left;fontSize=21;')
 cell('legend','Main steps in order. Dashed box: only when required. Process roles, not service deployments.',32,100,width-64,27,'text;html=0;align=left;fontSize=14;fontColor=#626262;')
 for i,(actor,title,note,activity,anchor,optional) in enumerate(flow['nodes']):
  y=start+i*step;link=LOGICAL+'#'+anchor
  group=ET.SubElement(svg,'a',href=link,attrib={'aria-label':activity+' '+title})
  attrs=dict(x=str(box_x),y=str(y),width=str(box_w),height=str(box_h),rx='38' if i==len(flow['nodes'])-1 else '8',fill='#fafafa' if optional else '#f1f1f1',stroke='#626262')
  if optional:attrs['stroke-dasharray']='7 5'
  ET.SubElement(group,'rect',attrs)
  text(width/2,y+24,actor+' · '+activity,14,anchor='middle',color='#626262',parent=group)
  text(width/2,y+53,f'{i+1}. '+title,20,anchor='middle',parent=group)
  lines=textwrap.wrap(note,99);assert len(lines)<=2,(flow['slug'],title)
  for j,line in enumerate(lines):text(width/2,y+78+j*19,line,15,anchor='middle',parent=group)
  style='rounded=1;whiteSpace=wrap;html=0;fillColor=#f1f1f1;strokeColor=#626262;fontSize=18;spacing=12;'+('dashed=1;' if optional else '')
  cell('step-'+str(i+1),actor+' · '+activity+'\n'+str(i+1)+'. '+title+'\n'+note,box_x,y,box_w,box_h,style,link)
  if i<len(flow['nodes'])-1:
   x=width/2;sy=y+box_h;ty=y+step-9
   ET.SubElement(svg,'path',d=f'M {x} {sy} L {x} {ty}',fill='none',stroke='#626262',attrib={'stroke-width':'1.8'})
   ET.SubElement(svg,'path',d=f'M {x-6} {ty-8} L {x} {ty} L {x+6} {ty-8}',fill='none',stroke='#626262',attrib={'stroke-width':'1.8'})
   e=ET.SubElement(root,'mxCell',id='edge-'+str(i+1),parent='1',edge='1',style='edgeStyle=none;strokeColor=#626262;endArrow=open;endFill=0;');geo=ET.SubElement(e,'mxGeometry',relative='1',attrib={'as':'geometry'});ET.SubElement(geo,'mxPoint',x=str(x),y=str(sy),attrib={'as':'sourcePoint'});ET.SubElement(geo,'mxPoint',x=str(x),y=str(ty),attrib={'as':'targetPoint'})
 for j,line in enumerate(notes):text(32,foot_y+j*22,line,14,color='#626262')
 cell('notes','\n'.join(notes),32,foot_y-15,width-64,len(notes)*22+10,'text;html=0;whiteSpace=wrap;align=left;fontSize=14;fontColor=#626262;')
 # One canonical document link is retained separately from the per-activity links.
 cell('source','Source specification',width-210,height-30,180,20,'text;html=0;fontSize=12;align=right;',flow['source'])
 path=OUT/(flow['slug']+'.svg');path.write_text(ET.tostring(svg,encoding='unicode'));ET.indent(native);path.with_suffix('.drawio').write_text(ET.tostring(native,encoding='unicode',xml_declaration=True))
 return {'svg':str(path.relative_to(ROOT)),'png':str(path.with_suffix('.png').relative_to(ROOT)),'drawio':str(path.with_suffix('.drawio').relative_to(ROOT)),'nodes':len(flow['nodes']),'width':width,'height':height,'title':flow['title']}
if __name__=='__main__':
 import importlib.util
 spec=importlib.util.spec_from_file_location('summary_wording',ROOT/'work/build-onboarding-summary-wording.py')
 summary_wording=importlib.util.module_from_spec(spec);spec.loader.exec_module(summary_wording)
 spec=importlib.util.spec_from_file_location('logical_swimlanes',ROOT/'work/build-onboarding-clear-swimlanes.py')
 logical_swimlanes=importlib.util.module_from_spec(spec);spec.loader.exec_module(logical_swimlanes)
 # Retain SPEC037's branching layout and SPEC038's original responsibility lanes.
 reports=[summary_wording.build()]+logical_swimlanes.build_all()
 (ROOT/'work/onboarding-clarity-review/simple-processes.json').write_text(json.dumps({'diagrams':reports,'publication_performed':False},indent=2)+'\n')
 print(json.dumps(reports,indent=2))
