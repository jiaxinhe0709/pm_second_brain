"""Build editable process diagrams for SPEC-SEI-014; no external calls."""
from pathlib import Path
import heapq
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/diagrams'
SPEC = '../../specs/SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md'
LANES = ['Customer / accountant', 'ERP / product',
         'Domain Service - E-Invoice Service', 'Domain Service - Other Services',
         'Operations / support', 'Public / private platforms']
COLORS = {'flow': ('#e8e8e8', '#333333'), 'conditional': ('#f6f6f6', '#333333'),
          'recovery': ('#d7d7d7', '#333333')}
CONNECTOR_COLOR = '#555555'
LEGEND = 'Solid: main handoff · Dashed: qualification, conditional work or recovery · Darker grey cards: recovery'
WIDTH, HEIGHT = 2340, 1090


def node(key, col, lane, title, activity, note='', kind='flow'):
    return dict(key=key, col=col, lane=lane, title=title,
                activity=activity, note=note, kind=kind)


def edge(a, b, kind='flow'):
    return dict(source=a, target=b, kind=kind)


def route(e, pos):
    """Find an orthogonal path through whitespace, avoiding every activity box."""
    sx, sy, sw, sh = pos[e['source']]
    tx, ty, tw, th = pos[e['target']]
    if tx > sx:
        a, start, end, b = (sx+sw, sy+sh/2), (sx+sw+10, sy+sh/2), (tx-10, ty+th/2), (tx, ty+th/2)
    elif tx < sx:
        a, start, end, b = (sx, sy+sh/2), (sx-10, sy+sh/2), (tx+tw+10, ty+th/2), (tx+tw, ty+th/2)
    elif ty > sy:
        a, start, end, b = (sx+sw/2, sy+sh), (sx+sw/2, sy+sh+10), (tx+tw/2, ty-10), (tx+tw/2, ty)
    else:
        a, start, end, b = (sx+sw/2, sy), (sx+sw/2, sy-10), (tx+tw/2, ty+th+10), (tx+tw/2, ty+th)
    obstacles = [(x-5, y-5, x+w+5, y+h+5) for x, y, w, h in pos.values()]
    xs = sorted({220, WIDTH-20, start[0], end[0]} | {v for x, y, w, h in pos.values() for v in (x-10, x+w/2, x+w+10)})
    ys = sorted({145, HEIGHT-85, start[1], end[1]} | {v for x, y, w, h in pos.values() for v in (y-10, y+h/2, y+h+10)})
    xi, yi = {x:i for i,x in enumerate(xs)}, {y:i for i,y in enumerate(ys)}
    valid = {(i,j) for i,x in enumerate(xs) for j,y in enumerate(ys)
             if not any(l<x<r and t<y<bottom for l,t,r,bottom in obstacles)}
    def clear(p, q):
        x1,y1=p; x2,y2=q
        if x1 == x2:
            return not any(l<x1<r and max(min(y1,y2),t)<min(max(y1,y2),bottom) for l,t,r,bottom in obstacles)
        return not any(t<y1<bottom and max(min(x1,x2),l)<min(max(x1,x2),r) for l,t,r,bottom in obstacles)
    first=(xi[start[0]],yi[start[1]],0); goal=(xi[end[0]],yi[end[1]])
    heap=[(0,0,first)]; costs={first:0}; previous={}; finish=None
    while heap:
        _, g, state=heapq.heappop(heap)
        if g != costs[state]: continue
        i,j,d=state
        if (i,j)==goal: finish=state; break
        for di,dj,nd in [(1,0,1),(-1,0,1),(0,1,2),(0,-1,2)]:
            ni,nj=i+di,j+dj
            if (ni,nj) not in valid: continue
            p,q=(xs[i],ys[j]),(xs[ni],ys[nj])
            if not clear(p,q): continue
            cost=g+abs(q[0]-p[0])+abs(q[1]-p[1])+(18 if d and d!=nd else 0)
            nxt=(ni,nj,nd)
            if cost < costs.get(nxt,float('inf')):
                costs[nxt]=cost; previous[nxt]=state
                heapq.heappush(heap,(cost+abs(q[0]-end[0])+abs(q[1]-end[1]),cost,nxt))
    assert finish is not None, e
    track=[]
    while True:
        track.append((xs[finish[0]],ys[finish[1]]))
        if finish==first: break
        finish=previous[finish]
    points=[]
    for p in [a]+list(reversed(track))+[b]:
        if points and points[-1]==p: continue
        if len(points)>1:
            u,v=points[-2:]
            if u[0]==v[0]==p[0] or u[1]==v[1]==p[1]: points.pop()
        points.append(p)
    return points


def build(slug, title, description, nodes, edges):
    pos={n['key']:(240+n['col']*295, 186+n['lane']*135, 260, 84) for n in nodes}
    assert len(pos)==len(nodes)
    paths=[route(e,pos) for e in edges]
    svg=ET.Element('svg', {'xmlns':'http://www.w3.org/2000/svg', 'width':str(WIDTH), 'height':str(HEIGHT),
                          'viewBox':f'0 0 {WIDTH} {HEIGHT}', 'role':'img', 'aria-label':title})
    ET.SubElement(svg,'title').text=title
    ET.SubElement(svg,'desc').text=description
    ET.SubElement(svg,'rect',{'width':str(WIDTH),'height':str(HEIGHT),'fill':'white'})
    def text(x,y,value,size=15,anchor='start',parent=svg,color='#222222'):
        ET.SubElement(parent,'text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif',
                                     'font-size':str(size),'text-anchor':anchor,'fill':color}).text=value
    text(28,35,title,23)
    for i,line in enumerate(textwrap.wrap(description,190)): text(28,65+i*20,line,15)
    text(28,120,'Proposed design · '+LEGEND,14)
    for i,lane in enumerate(LANES):
        y=160+i*135
        ET.SubElement(svg,'rect',{'x':'20','y':str(y),'width':str(WIDTH-40),'height':'135',
                                 'fill':'#fafafa','stroke':'#aaaaaa'})
        ET.SubElement(svg,'rect',{'x':'20','y':str(y),'width':'200','height':'135',
                                 'fill':'#e5e5e5','stroke':'#aaaaaa'})
        lines = textwrap.wrap(lane,23)
        for j,line in enumerate(lines): text(120,y+135/2-(len(lines)-1)*10+5+j*20,line,15,'middle')
    for e,points in zip(edges,paths):
        color=CONNECTOR_COLOR
        attrs={'d':'M '+' L '.join(f'{x:g},{y:g}' for x,y in points),'fill':'none','stroke':color,'stroke-width':'1.8'}
        if e['kind']!='flow': attrs['stroke-dasharray']='6 4'
        ET.SubElement(svg,'path',attrs)
        a,b=points[-2:]; dx,dy=b[0]-a[0],b[1]-a[1]; length=(dx*dx+dy*dy)**.5; ux,uy=dx/length,dy/length
        ET.SubElement(svg,'path',{'d':f'M {b[0]},{b[1]} L {b[0]-8*ux+4*uy},{b[1]-8*uy-4*ux} L {b[0]-8*ux-4*uy},{b[1]-8*uy+4*ux} Z','fill':color})
    for n in nodes:
        x,y,w,h=pos[n['key']]; fill,color=COLORS[n['kind']]
        a=ET.SubElement(svg,'a',{'href':SPEC,'aria-label':n['activity']+' '+n['title']})
        ET.SubElement(a,'title').text=n['note'] or n['title']
        ET.SubElement(a,'rect',{'x':str(x),'y':str(y),'width':str(w),'height':str(h),'rx':'8',
                               'fill':fill,'stroke':color,'stroke-width':'1.5'})
        lines=textwrap.wrap(n['title'],31)
        assert len(lines)<=3, n
        for i,line in enumerate(lines): text(x+w/2,y+23+i*18,line,15,'middle',a)
        text(x+w/2,y+h-10,n['activity'],12,'middle',a,color)
    text(28,1002,'Logical responsibility groups; actual service ownership and external contracts require qualification.',14)
    text(28,1026,'Readiness does not activate a route. Earlier invoices retain original context and require current permitted access.',14)
    text(28,1050,'SPEC-SEI-014 · Country rules and operator eligibility remain separate from shared connectivity.',14)
    base=OUT/slug; base.with_suffix('.svg').write_text(ET.tostring(svg,encoding='unicode'))
    mx=ET.Element('mxfile',{'host':'app.diagrams.net','type':'device','version':'24.7.17'})
    diagram=ET.SubElement(mx,'diagram',{'id':slug,'name':title})
    graph=ET.SubElement(diagram,'mxGraphModel',{'page':'1','pageWidth':str(WIDTH),'pageHeight':str(HEIGHT)})
    root=ET.SubElement(graph,'root'); ET.SubElement(root,'mxCell',{'id':'0'}); ET.SubElement(root,'mxCell',{'id':'1','parent':'0'})
    def cell(key,value,style,x,y,w,h):
        c=ET.SubElement(root,'mxCell',{'id':key,'value':value,'style':style,'vertex':'1','parent':'1'})
        ET.SubElement(c,'mxGeometry',{'x':str(x),'y':str(y),'width':str(w),'height':str(h),'as':'geometry'})
    cell('title',title+'\n'+description,'text;whiteSpace=wrap;html=0;align=left;fontSize=20;',28,12,WIDTH-56,95)
    cell('legend',LEGEND,'text;html=0;align=left;fontSize=14;',28,104,WIDTH-56,36)
    for i,lane in enumerate(LANES):
        cell(f'lane-{i}',lane,'swimlane;horizontal=0;noLabel=1;startSize=200;whiteSpace=wrap;html=0;fontSize=15;fillColor=#e5e5e5;swimlaneFillColor=#fafafa;strokeColor=#aaaaaa;',20,160+i*135,WIDTH-40,135)
        cell(f'lane-{i}-label','\n'.join(textwrap.wrap(lane,23)),'text;html=0;align=center;verticalAlign=middle;fontSize=15;spacing=0;',30,160+i*135,180,135)
    for n in nodes:
        obj=ET.SubElement(root,'object',{'id':n['key'],'label':n['title']+'\n'+n['activity'],'tooltip':n['note'],'link':SPEC})
        fill,color=COLORS[n['kind']]
        c=ET.SubElement(obj,'mxCell',{'vertex':'1','parent':'1','style':f'rounded=1;whiteSpace=wrap;html=0;fontSize=15;fillColor={fill};strokeColor={color};spacing=8;'})
        x,y,w,h=pos[n['key']]; ET.SubElement(c,'mxGeometry',{'x':str(x),'y':str(y),'width':str(w),'height':str(h),'as':'geometry'})
    for i,(e,points) in enumerate(zip(edges,paths)):
        sx,sy,sw,sh=pos[e['source']]; tx,ty,tw,th=pos[e['target']]; color=CONNECTOR_COLOR
        style=f'edgeStyle=none;endArrow=block;strokeColor={color};exitX={(points[0][0]-sx)/sw};exitY={(points[0][1]-sy)/sh};entryX={(points[-1][0]-tx)/tw};entryY={(points[-1][1]-ty)/th};'
        if e['kind']!='flow': style+='dashed=1;'
        c=ET.SubElement(root,'mxCell',{'id':f'edge-{i}','source':e['source'],'target':e['target'],'edge':'1','parent':'1','style':style})
        g=ET.SubElement(c,'mxGeometry',{'relative':'1','as':'geometry'}); array=ET.SubElement(g,'Array',{'as':'points'})
        for x,y in points[1:-1]: ET.SubElement(array,'mxPoint',{'x':str(x),'y':str(y)})
    cell('boundary','Proposed logical responsibilities. Readiness does not activate a route; preserve original history and current permitted access.','text;whiteSpace=wrap;html=0;align=left;fontSize=14;',28,990,WIDTH-56,70)
    ET.indent(mx); base.with_suffix('.drawio').write_text(ET.tostring(mx,encoding='unicode',xml_declaration=True))
    print(slug,len(nodes),'activities')


if __name__=='__main__':
    build('shared-platform-connection-qualification-process','Check a platform connection without changing the active route',
          'Use one foundation for customer-provider integration and platform interconnection. Check each role and capability separately; return setup results and required actions.',[
        node('request',0,0,'Request platform setup','SPC-01'),
        node('api',1,1,'Submit the authorised setup request','SPC-01'),
        node('scope',2,2,'Check business permission and role','SPC-01'),
        node('configure',3,3,'Save the connection and contract settings','SPC-02'),
        node('qualify',4,3,'Check each required function','SPC-03'),
        node('observe',4,5,'Provide evidence for the checks','SPC-03',kind='conditional'),
        node('result',5,2,'Return setup results and next actions','SPC-03','Passed, failed and unknown checks; no route activation.'),
        node('display',6,1,'Show checks and remaining steps','SPC-03'),
        node('recover',5,4,'Resolve missing or uncertain evidence','SPC-07','Reconcile possible external effects before unsafe repeat.',kind='recovery')],
        [edge('request','api'),edge('api','scope'),edge('scope','configure'),edge('configure','qualify'),
         edge('qualify','observe','conditional'),edge('observe','qualify','conditional'),edge('qualify','result'),
         edge('result','display'),edge('qualify','recover','recovery'),edge('recover','qualify','recovery')])
    build('shared-platform-route-and-continuity-process','Change the platform for future invoices; keep earlier invoice context',
          'Only an explicit authorised change activates a qualified route. Resolve and bind new work through the shared foundation; retain permitted historical actors and channels.',[
        node('request',0,0,'Request an invoicing platform change','SPC-04'),
        node('intent',1,1,'Confirm direction and effective time','SPC-04'),
        node('prepare',2,2,'Coordinate the authorised platform change','SPC-04'),
        node('checks',2,3,'Recheck settings, permission and readiness','SPC-03',kind='conditional'),
        node('external',2,5,'Confirm required external changes','SPC-04',kind='conditional'),
        node('commit',3,3,'Save the approved route version','SPC-04'),
        node('resolve',4,3,'Select one route for new work','SPC-05'),
        node('bind',5,2,'Save invoice context and the action owner','SPC-06'),
        node('execute',5,5,'Perform each approved invoice action','SPC-06','Invoice delivery, public copy and reports retain independent outcomes.'),
        node('history',6,3,'Keep permitted earlier invoice context','SPC-08','Earlier invoices retain their original route/operator and current permitted actor/channel.',kind='conditional'),
        node('recover',3,4,'Check uncertain outcomes before retrying','SPC-07',kind='recovery')],
        [edge('request','intent'),edge('intent','prepare'),edge('prepare','checks','conditional'),
         edge('checks','external','conditional'),edge('external','commit'),edge('commit','resolve'),
         edge('resolve','bind'),edge('bind','execute'),edge('commit','history','conditional'),
         edge('external','recover','recovery'),edge('resolve','recover','recovery'),edge('recover','prepare','recovery')])
