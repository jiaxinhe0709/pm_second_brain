"""Create one continuous horizontal responsibility diagram from the overview model."""
from pathlib import Path
import json
import textwrap
import xml.etree.ElementTree as ET
import heapq

ROOT = Path(__file__).resolve().parents[1]
source = ROOT/'work/build-spain-end-to-end-swimlane.py'
scope = {'__file__':str(source)}
exec(compile(source.read_text().split('W, X, CW, RH, TOP, NH =',1)[0],str(source),'exec'),scope)
DETAIL = scope['MODEL']
# Add a distinct overview journey for full service exit. Both route changes and
# offboarding remain owned by SPEC-SEI-003; these IDs identify diagram nodes.
detail_by_id={n['id']:n for n in DETAIL['nodes']}
for new_id,source_id in [('END-01','EXT-01'),('END-02','EXT-02'),('END-03','EXT-05'),('END-04','EXT-04'),('END-05','EXT-07')]:
    DETAIL['nodes'].append(dict(detail_by_id[source_id],id=new_id))
# This canvas is a navigation overview. Detailed checks, states and recovery
# sequences remain in the owning specifications and the source model.
TITLES = {
    'SET-01':'Authorise the business',
    'SET-02':'Request setup through Global API',
    'SET-03':'Establish capability readiness',
    'SET-04':'Trust and certificate checks',
    'SET-05':'Public platform connection',
    'SET-07':'Return readiness and next action',
    'SET-08':'Setup recovery, when needed',
    'OUT-01':'Prepare, review and issue invoice',
    'OUT-08':'Recipient destination lookup',
    'OUT-10':'Spain UBL conversion',
    'OUT-11':'UBL validation',
    'OUT-13':'Coordinate sending the invoice',
    'OUT-14':'Recipient delivery',
    'OUT-15':'Public copy, only if required',
    'RCV-04':'Retrieve and preserve public file',
    'RCV-05':'Private invoice arrival',
    'RCV-06':'Download stored public file',
    'RCV-07':'Process received invoice',
    'RCV-11':'Invoice available in ERP',
    'LIF-03':'Record buyer decision',
    'LIF-07':'Track outcomes and reporting',
    'LIF-09':'Show status and next action',
    'EXT-01':'Request route change',
    'EXT-02':'Switch future traffic safely',
    'EXT-05':'Keep earlier records accessible',
    'END-01':'Request service exit',
    'END-02':'Coordinate exit and earlier obligations',
    'END-03':'Export records and apply retention',
    'END-04':'Confirm required disconnection',
    'END-05':'Return exit result and access terms',
}
SUMMARY_EDGES = [
    ('SET-01','SET-02','flow'),('SET-02','SET-03','flow'),
    ('SET-04','SET-03','support'),('SET-05','SET-03','support'),
    ('SET-03','SET-07','flow'),('SET-03','SET-08','support'),
    ('OUT-01','OUT-13','flow'),('OUT-08','OUT-13','support'),
    ('OUT-10','OUT-13','support'),('OUT-11','OUT-13','support'),
    ('OUT-13','OUT-14','flow'),('OUT-13','OUT-15','conditional'),
    ('RCV-04','RCV-07','flow'),('RCV-05','RCV-07','flow'),
    ('RCV-07','RCV-11','flow'),('RCV-04','RCV-06','access'),
    ('LIF-03','LIF-07','flow'),('LIF-07','LIF-09','flow'),
    ('EXT-01','EXT-02','flow'),('EXT-02','EXT-05','flow'),
    ('END-01','END-02','flow'),('END-02','END-03','flow'),
    ('END-03','END-05','flow'),('END-03','END-04','conditional'),
    ('END-04','END-05','conditional'),
]
SUMMARY_NOTES = {
    'OUT-01':'The ERP owns draft review and invoice issuance. Detailed preparation and final checks remain in SPEC-SEI-007.',
    'OUT-13':'Use a qualified recipient route. Track recipient delivery and any required public copy separately. The owning spec explains checks and recovery.',
    'OUT-14':'Deliver through the qualified public or private recipient route. This does not establish buyer acceptance.',
    'LIF-07':'Preserve separate delivery, public-copy, buyer-action and reporting evidence. Technical acknowledgement does not establish buyer acceptance.',
    'EXT-01':'Optional request to change the receiving or sending route. Full service exit is covered in the separate offboarding journey.',
    'EXT-02':'Check destination readiness and apply an approved boundary for future traffic. Earlier invoices retain their actual route and obligations.',
    'EXT-05':'Preserve permitted records and access needed for earlier invoices after a route change.',
    'END-02':'Check the authorised exit scope and assign each unfinished invoice obligation a permitted owner and channel before dependent access is released.',
    'END-03':'Provide an authorised export and apply approved retention and legal holds. Ending the service does not automatically delete invoice records.',
    'END-04':'Only perform applicable, qualified external withdrawal or deregistration actions after the relevant continuity checks. Reconcile uncertain results before declaring completion.',
    'END-05':'Report completion only when the exit checks are satisfied. Explain the approved historical-access and retention arrangements; unresolved work remains visible.',
}
ALL = dict(DETAIL,
    phases=DETAIL['phases'][:4]+[
        dict(title='5 · Change route',note='Optional route change; preserve earlier invoice obligations.'),
        dict(title='6 · Offboarding',note='Optional full service exit; preserve required records and permitted historical access.')],
    lanes=['Customer / accountant','ERP / product','Domain Service - E-Invoice Service','Domain Service - Other Services','Operations / support','Public / private platforms'],
    nodes=[dict(n,title=TITLES[n['id']],note=SUMMARY_NOTES.get(n['id'],n['note']),
                lane=4 if n['id']=='SET-08' else 5 if n['lane']==4 else n['lane'])
           for n in DETAIL['nodes'] if n['id'] in TITLES],
    edges=[dict(source=a,target=b,kind=k,label='') for a,b,k in SUMMARY_EDGES])
GROUPS = [
    ('setup',['Business request','Readiness and service checks','Result / support'],[
        ['SET-01','SET-02'],['SET-03','SET-04','SET-05'],['SET-07','SET-08']]),
    ('outbound',['ERP owns issuance','Coordinate the exchange','Independent results'],[
        ['OUT-01'],['OUT-08','OUT-10','OUT-11','OUT-13'],['OUT-14','OUT-15']]),
    ('inbound',['Invoice sources','Receive and process','ERP / customer access'],[
        ['RCV-04','RCV-05'],['RCV-07'],['RCV-06','RCV-11']]),
    ('lifecycle',['Buyer action','Lifecycle coordination','Customer view'],[
        ['LIF-03'],['LIF-07'],['LIF-09']]),
    ('route-change',['Customer request','Controlled change','Historical continuity'],[
        ['EXT-01'],['EXT-02'],['EXT-05']]),
    ('offboarding',['Exit request','Continuity and records','Controlled closure'],[
        ['END-01'],['END-02','END-03'],['END-04','END-05']])
]
PANELS=[]
for i,(slug,columns,groups) in enumerate(GROUPS):
    phase=ALL['phases'][i]
    ids={id for group in groups for id in group}
    nodes=[dict(n,col=next(j for j,g in enumerate(groups) if n['id'] in g)) for n in ALL['nodes'] if n['id'] in ids]
    edges=[e for e in ALL['edges'] if e['source'] in ids and e['target'] in ids]
    PANELS.append(dict(slug=slug,title=phase['title'],note=phase['note'],columns=columns,nodes=nodes,edges=edges))
assert len({n['id'] for p in PANELS for n in p['nodes']})==30
assert {n['spec'] for n in ALL['nodes']}=={f'SPEC-SEI-{i:03}' for i in range(1,14)}

def layout(panel,width=1660):
    label=190;left=label+30;journey_gap=90
    cw=(width-left-30-journey_gap*(len(panel['phases'])-1))/len(panel['columns']);boxw=cw-32;gap=20
    column_lefts=[left+col*cw+journey_gap*next(i for i,p in enumerate(panel['phases']) if p['start']<=col<p['start']+p['count']) for col in range(len(panel['columns']))]
    phase_bounds=[(column_lefts[p['start']],p['count']*cw) for p in panel['phases']]
    node_sizes={n['id']: max(84, len(textwrap.wrap(n['title'],int(boxw/7.7)))*19+42) for n in panel['nodes']}
    lane_tops=[];lane_heights=[];pos={};y=226
    for lane in range(len(ALL['lanes'])):
        cells=[[n for n in panel['nodes'] if n['lane']==lane and n['col']==col] for col in range(len(panel['columns']))]
        h=max(125,max((sum(node_sizes[n['id']]+gap for n in cell) for cell in cells),default=0)+35)
        lane_tops.append(y);lane_heights.append(h)
        for col,cell in enumerate(cells):
            ny=y+38
            for n in cell:
                pos[n['id']]=(column_lefts[col]+16,ny,boxw,node_sizes[n['id']]);ny+=node_sizes[n['id']]+gap
        y+=h
    return dict(width=width,height=y+44,left=left,cw=cw,tops=lane_tops,heights=lane_heights,pos=pos,column_lefts=column_lefts,phase_bounds=phase_bounds,journey_gap=journey_gap)

def ports(source,target):
    sx,sy,sw,sh=source;tx,ty,tw,th=target
    if tx>sx+1:return (sx+sw,sy+sh/2),(sx+sw+10,sy+sh/2),(tx-10,ty+th/2),(tx,ty+th/2)
    if tx<sx-1:return (sx,sy+sh/2),(sx-10,sy+sh/2),(tx+tw+10,ty+th/2),(tx+tw,ty+th/2)
    if ty>sy:return (sx+sw/2,sy+sh),(sx+sw/2,sy+sh+10),(tx+tw/2,ty-10),(tx+tw/2,ty)
    return (sx+sw/2,sy),(sx+sw/2,sy-10),(tx+tw/2,ty+th+10),(tx+tw/2,ty+th)

def route(edge,view):
    positions=view['pos'];a,start,end,b=ports(positions[edge['source']],positions[edge['target']])
    obstacles=[(x-5,y-5,x+w+5,y+h+5) for x,y,w,h in positions.values()]
    xs=sorted({view['left']+4,view['width']-12,start[0],end[0]} | {q for x,y,w,h in positions.values() for q in [x-10,x+w/2,x+w+10]})
    ys=sorted({218,view['height']-22,start[1],end[1]} | {q for x,y,w,h in positions.values() for q in [y-10,y+h/2,y+h+10]})
    xi={x:i for i,x in enumerate(xs)};yi={y:i for i,y in enumerate(ys)}
    valid={(i,j) for i,x in enumerate(xs) for j,y in enumerate(ys) if not any(l<x<r and t<y<bot for l,t,r,bot in obstacles)}
    def clear(p,q):
        x1,y1=p;x2,y2=q
        if x1==x2:return not any(l<x1<r and max(min(y1,y2),t)<min(max(y1,y2),bot) for l,t,r,bot in obstacles)
        return not any(t<y1<bot and max(min(x1,x2),l)<min(max(x1,x2),r) for l,t,r,bot in obstacles)
    first=(xi[start[0]],yi[start[1]],0);goal=(xi[end[0]],yi[end[1]])
    heap=[(0,0,first)];cost={first:0};previous={};finish=None
    while heap:
        _,g,state=heapq.heappop(heap)
        if g!=cost.get(state):continue
        i,j,d=state
        if (i,j)==goal:finish=state;break
        for di,dj,nd in [(1,0,1),(-1,0,1),(0,1,2),(0,-1,2)]:
            ni,nj=i+di,j+dj
            if (ni,nj) not in valid:continue
            p=(xs[i],ys[j]);q=(xs[ni],ys[nj])
            if not clear(p,q):continue
            ng=g+abs(q[0]-p[0])+abs(q[1]-p[1])+(18 if d and d!=nd else 0)
            nxt=(ni,nj,nd)
            if ng<cost.get(nxt,float('inf')):
                cost[nxt]=ng;previous[nxt]=state
                heapq.heappush(heap,(ng+abs(q[0]-end[0])+abs(q[1]-end[1]),ng,nxt))
    assert finish is not None,edge
    track=[]
    while True:
        track.append((xs[finish[0]],ys[finish[1]]))
        if finish==first:break
        finish=previous[finish]
    points=[a]+list(reversed(track))+[b]
    compact=[]
    for p in points:
        if compact and compact[-1]==p:continue
        if len(compact)>1:
            u,v=compact[-2:]
            if (u[0]==v[0]==p[0]) or (u[1]==v[1]==p[1]):compact.pop()
        compact.append(p)
    return compact

def path(points):return 'M '+' L '.join(f'{x:g},{y:g}' for x,y in points)

COMBINED = dict(slug='overview', title='End-to-end responsibility overview', note='Setup → outbound → inbound → lifecycle → route change → offboarding is a reading order; sending and receiving are independent, and later journeys are optional.', columns=[], nodes=[], edges=[], phases=[])
for panel in PANELS:
    offset=len(COMBINED['columns'])
    phase_notes = [
        'Authorise a business and establish readiness for the selected capability.',
        'ERP owns issuance. Recipient delivery and a required public copy have separate results.',
        'Public and private sources converge. Saved-file download does not wait for ERP processing.',
        'Track evidence and buyer actions. Technical acknowledgement does not mean buyer acceptance.',
        'Change future traffic while preserving permitted work and records for earlier invoices.',
        'Leave the service safely. Export and retention are separate from closing access.',
    ]
    COMBINED['phases'].append(dict(title=panel['title'], note=phase_notes[len(COMBINED['phases'])], start=offset, count=len(panel['columns'])))
    COMBINED['columns'].extend(panel['columns'])
    COMBINED['nodes'].extend(dict(n,col=n['col']+offset) for n in panel['nodes'])
    COMBINED['edges'].extend(panel['edges'])

for panel in [COMBINED]:
    view=layout(panel, width=220+len(panel['columns'])*285+30+90*(len(panel['phases'])-1));panel['exportLayout']=view
    points={f"{e['source']}:{e['target']}":route(e,view) for e in panel['edges']}
    panel['routes']=points
    w,h=view['width'],view['height']
    svg=ET.Element('svg',{'xmlns':'http://www.w3.org/2000/svg','width':str(w),'height':str(h),'viewBox':f'0 0 {w} {h}','role':'img','aria-label':panel['title']})
    ET.SubElement(svg,'title').text=panel['title']
    ET.SubElement(svg,'desc').text=panel['note']+' Six horizontal responsibility lanes. Domain Services includes E-Invoice Service and other named services, such as Tax Service. Each activity opens its owning spec. Exact service ownership of supporting capabilities remains open.'
    ET.SubElement(svg,'rect',{'width':str(w),'height':str(h),'fill':'#ffffff'})
    def text(x,y,value,size=15,anchor='start',parent=svg,color='#222222'):
        ET.SubElement(parent,'text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif','font-size':str(size),'font-weight':'400','text-anchor':anchor,'fill':color}).text=value
    text(30,36,'Spain e-invoicing · '+panel['title'],23)
    text(30,65,panel['note'],15)
    text(30,89,'Read left to right · Solid: main handoff · Dashed: supporting capability / conditional action · Dotted: independent download',14)
    text(30,111,'Domain Services includes E-Invoice Service and other named services, such as Tax Service. Supporting-service ownership remains to be confirmed in the specs.',14)
    for col,title in enumerate(panel['columns']):
        text(view['column_lefts'][col]+view['cw']/2,213,title,15,'middle')
    for i,lane in enumerate(ALL['lanes']):
        y=view['tops'][i];lh=view['heights'][i]
        ET.SubElement(svg,'rect',{'x':'25','y':str(y),'width':str(w-50),'height':str(lh),'fill':'#fafafa' if i%2==0 else '#f1f1f1','stroke':'#c7c7c7'})
        ET.SubElement(svg,'path',{'d':f'M {view["left"]-4},{y} L {view["left"]-4},{y+lh}','stroke':'#c7c7c7'})
        for j,line in enumerate(textwrap.wrap(lane,22)):text(38,y+30+j*20,line,15)
    for i,(phase,(px,pw)) in enumerate(zip(panel['phases'],view['phase_bounds'])):
        if i:
            ET.SubElement(svg,'rect',{'x':str(px-view['journey_gap']),'y':'118','width':str(view['journey_gap']),'height':str(h-148),'fill':'#ffffff'})
        ET.SubElement(svg,'rect',{'x':str(px),'y':'118','width':str(pw),'height':str(h-162),'fill':'none','stroke':'#888888','stroke-width':'1.6','data-journey':str(i+1)})
        ET.SubElement(svg,'rect',{'x':str(px),'y':'118','width':str(pw),'height':'72','fill':'#444444'})
        text(px+16,146,phase['title'],23,color='#ffffff')
        text(px+16,173,phase['note'],15,color='#ffffff')
        for lane,y in zip(ALL['lanes'],view['tops']):
            text(px+12,y+15,lane,12,color='#555555')
    for e in panel['edges']:
        pts=points[f"{e['source']}:{e['target']}"]
        attrs={'d':path(pts),'fill':'none','stroke':'#555555','stroke-width':'1.6'}
        if e['kind']!='flow':attrs['stroke-dasharray']='2 4' if e['kind']=='access' else '6 4'
        ET.SubElement(svg,'path',attrs)
        a,b=pts[-2:];dx=b[0]-a[0];dy=b[1]-a[1];l=(dx*dx+dy*dy)**.5;ux=dx/l;uy=dy/l
        ET.SubElement(svg,'path',{'d':path([b,(b[0]-8*ux+4*uy,b[1]-8*uy-4*ux),(b[0]-8*ux-4*uy,b[1]-8*uy+4*ux)])+' Z','fill':'#555555'})
    for n in panel['nodes']:
        x,y,bw,bh=view['pos'][n['id']]
        a=ET.SubElement(svg,'a',{'href':n['relative'],'aria-label':n['title']+' '+n['spec']})
        ET.SubElement(a,'title').text=n['note'] or n['spec']
        attr={'x':str(x),'y':str(y),'width':str(bw),'height':str(bh),'rx':'7','fill':'#ffffff','stroke':'#555555','stroke-width':'1.3'}
        if n['id'] in ['SET-08','OUT-15','OUT-17']:attr['stroke-dasharray']='5 3'
        ET.SubElement(a,'rect',attr)
        for j,line in enumerate(textwrap.wrap(n['title'],int(bw/7.7))):text(x+bw/2,y+24+j*19,line,15,'middle',a)
        text(x+bw/2,y+bh-14,n['spec'],13,'middle',a)
    base=ROOT/'assets/diagrams/spain-end-to-end-responsibility-overview'
    base.with_suffix('.svg').write_text(ET.tostring(svg,encoding='unicode'))
    mx=ET.Element('mxfile',{'host':'app.diagrams.net','type':'device','version':'24.7.17'})
    diag=ET.SubElement(mx,'diagram',{'id':base.name,'name':panel['title']})
    graph=ET.SubElement(diag,'mxGraphModel',{'page':'1','pageWidth':str(w),'pageHeight':str(h),'grid':'1','gridSize':'10'})
    root=ET.SubElement(graph,'root');ET.SubElement(root,'mxCell',{'id':'0'});ET.SubElement(root,'mxCell',{'id':'1','parent':'0'})
    def cell(id,label,style,x,y,cw,ch):
        c=ET.SubElement(root,'mxCell',{'id':id,'value':label,'style':style,'parent':'1','vertex':'1'});ET.SubElement(c,'mxGeometry',{'x':str(x),'y':str(y),'width':str(cw),'height':str(ch),'as':'geometry'})
    cell('title','Spain e-invoicing · '+panel['title']+'\n'+panel['note'],'text;html=0;align=left;fontSize=20;',30,14,w-60,100)
    for i,lane in enumerate(ALL['lanes']):
        cell(f'lane-{i}',lane,f'swimlane;horizontal=0;noLabel=1;startSize={view["left"]-29};fillColor={"#fafafa" if i%2==0 else "#f1f1f1"};swimlaneFillColor={"#fafafa" if i%2==0 else "#f1f1f1"};strokeColor=#c7c7c7;fontSize=15;whiteSpace=wrap;html=0;',25,view['tops'][i],w-50,view['heights'][i])
        cell(f'lane-{i}-label','\n'.join(textwrap.wrap(lane,22)),'text;html=0;align=left;verticalAlign=top;fontSize=15;whiteSpace=wrap;spacing=0;',38,view['tops'][i]+14,view['left']-54,96)
    for i,(phase,(px,pw)) in enumerate(zip(panel['phases'],view['phase_bounds'])):
        if i:cell(f'journey-gap-{i}','','rounded=0;fillColor=#ffffff;strokeColor=none;',px-view['journey_gap'],118,view['journey_gap'],h-148)
        cell(f'journey-frame-{i}','','rounded=0;fillColor=none;strokeColor=#888888;strokeWidth=1.6;',px,118,pw,h-162)
        cell(f'phase-{i}','','rounded=0;fillColor=#444444;strokeColor=none;',px,118,pw,72)
        cell(f'phase-{i}-title',phase['title'],'text;html=0;align=left;fontColor=#ffffff;fontSize=23;spacing=0;',px+16,126,pw-32,32)
        cell(f'phase-{i}-note',phase['note'],'text;html=0;align=left;fontColor=#ffffff;fontSize=15;spacing=0;',px+16,157,pw-32,26)
        for j,(lane,y) in enumerate(zip(ALL['lanes'],view['tops'])):cell(f'phase-{i}-lane-{j}',lane,'text;html=0;align=left;fontColor=#555555;fontSize=12;spacing=0;',px+12,y+1,pw-24,18)
    for col,title in enumerate(panel['columns']):cell(f'column-{col}',title,'text;html=0;align=center;fontSize=15;',view['column_lefts'][col],195,view['cw'],26)
    for n in panel['nodes']:
        obj=ET.SubElement(root,'object',{'id':n['id'],'label':n['title']+'\n'+n['spec'],'link':n['relative'],'tooltip':n['note']})
        style='rounded=1;arcSize=8;whiteSpace=wrap;html=0;fillColor=#ffffff;strokeColor=#555555;fontSize=15;spacing=8;'
        if n['id'] in ['SET-08','OUT-15','OUT-17']:style+='dashed=1;'
        c=ET.SubElement(obj,'mxCell',{'vertex':'1','parent':'1','style':style})
        x,y,bw,bh=view['pos'][n['id']];ET.SubElement(c,'mxGeometry',{'x':str(x),'y':str(y),'width':str(bw),'height':str(bh),'as':'geometry'})
    for i,e in enumerate(panel['edges']):
        pts=points[f"{e['source']}:{e['target']}"];sx,sy,sw,sh=view['pos'][e['source']];tx,ty,tw,th=view['pos'][e['target']]
        style=f'edgeStyle=none;rounded=0;endArrow=block;strokeColor=#555555;strokeWidth=1.6;exitX={(pts[0][0]-sx)/sw};exitY={(pts[0][1]-sy)/sh};entryX={(pts[-1][0]-tx)/tw};entryY={(pts[-1][1]-ty)/th};'
        if e['kind']!='flow':style+='dashed=1;dashPattern='+('2 4;' if e['kind']=='access' else '6 4;')
        c=ET.SubElement(root,'mxCell',{'id':f'edge-{i}','source':e['source'],'target':e['target'],'edge':'1','parent':'1','style':style})
        g=ET.SubElement(c,'mxGeometry',{'relative':'1','as':'geometry'});arr=ET.SubElement(g,'Array',{'as':'points'})
        for px,py in pts[1:-1]:ET.SubElement(arr,'mxPoint',{'x':str(px),'y':str(py)})
    ET.indent(mx);base.with_suffix('.drawio').write_text(ET.tostring(mx,encoding='unicode',xml_declaration=True))
    # Native exports must never put an unrelated box under a connector.
    for e in panel['edges']:
        pts=points[f"{e['source']}:{e['target']}"]
        for a,b in zip(pts,pts[1:]):
            for id,(x,y,bw,bh) in view['pos'].items():
                if id in [e['source'],e['target']]:continue
                assert not (a[0]==b[0] and x<a[0]<x+bw and max(min(a[1],b[1]),y)<min(max(a[1],b[1]),y+bh)),(e,id)
                assert not (a[1]==b[1] and y<a[1]<y+bh and max(min(a[0],b[0]),x)<min(max(a[0],b[0]),x+bw)),(e,id)
    print(panel['title'],len(panel['nodes']),'linked activities',f'{w} × {h}')
