"""Rebuild Spain spec diagrams with the agreed, visibly labelled responsibility groups.

Node text, activity IDs and connectors come from the canonical Draw.io files.
The mapping below assigns logical responsibilities, not approved deployments.
The two DTS diagrams retain their vertical layout and detailed role subtitles.
"""
from pathlib import Path
from html import escape, unescape
from collections import defaultdict
import ast
import copy
import heapq
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/diagrams'
SVG = 'http://www.w3.org/2000/svg'
XHTML = 'http://www.w3.org/1999/xhtml'
LABELS = ['Customer / accountant', 'ERP / product',
          'Domain Service - E-Invoice Service', 'Domain Service - Other Services',
          'Operations / support', 'Public / private platforms']
NOTE = 'Logical responsibility groups; exact service owners and implementation remain open in the owning spec.'

# Customer, ERP, E-Invoice Service, other services, Operations, platforms.
GROUPS = {
 'certificate-setup-onboarding-process': ['a1 ah2', 'a8', '', 'a2 a3 a4 a5 a6 a7', 'ah1 ah3', ''],
 'certificate-protected-use-process': ['', '', 'b1 b8', 'b2 b3 b4 b5 b6 b7 bh1 bh2', '', ''],
 'certificate-renewal-recovery-process': ['', '', '', 'c2 c3 c4 c6 c7 c8 ch1', 'c1 c5 ch2', ''],
 'onboarding-public-readiness-process': ['a8', 'a6', 'a1 a4 a5 a7', 'a2 a3', '', ''],
 'onboarding-private-route-process': ['b1', 'b7', 'b2 b4 b5 b8', 'b6', '', 'b3'],
 'offboarding-planned-exit-process': ['c1', 'c8', 'c2 c4 c5 c9', 'c6 c7', '', 'c3'],
 'offboarding-recovery-process': ['', 'd8', 'd2 d3 d5 d6', 'd4 d7', 'd1 d9', ''],
 'onboarding-failure-classification-process': ['a7', 'a6', 'a1 a2 a3 a4 a5 a8', '', 'a9', ''],
 'onboarding-uncertain-outcome-process': ['', 'b6', 'b1 b3 b4 b5', 'b2 b7', 'b8', ''],
 'ubl-preflight-correction-process': ['', 'c1 c6 c7', 'c2 c5 c8', 'c3 c4', '', ''],
 'ubl-final-validation-process': ['', '', 'd1 d2 d4 d5 d6 d7', 'd3', '', ''],
 'receiving-intake-and-delivery-process': ['', 'e8', 'e1 e2 e4 e6 e9', 'e3 e5 e7', '', ''],
 'e-invoicing-public-consultation-reconciliation': ['', 'B2', 'B1 B3 S1 S2 S3 S5 S6 S7 Q1 Q2 Q4', 'S4 Q3', '', 'X1'],
 'e-invoicing-outbound-exchange-pilot': ['B4', 'B1 B2 B3', 'S1 S3 S4 S5 S6 S7 P5', 'S2 P1 P2 P3 P4', '', 'G1 X1 X2'],
 'spain-invoice-preparation-and-outbound-flow': ['', '14 15 16 17 18 19 20 29', '21 22 23 25 26 27 28 34', '24 30 31 32 33', '', '35 36 37 38 39'],
 'lifecycle-event-derivation-process': ['', 'a7', 'a1 a2 a3 a5 a6', 'a4', 'a8', ''],
 'lifecycle-reporting-reconciliation-process': ['', 'b7', 'b1 b2 b3 b5 b6 b8', 'b4', '', ''],
 'public-platform-connector-process': ['', '', 'p1 p2 p4 gate p5 p7 p8 hold p9', 'p3 p6', 'p10', ''],
 'public-platform-recipient-lookup-process': ['', '', 'l1 l2 l4 l6 l8 l9 ready public unresolved l10', 'l3 l5 l7', '', ''],
 'global-api-access-and-route-process': ['', 'request available action', 'qualify ready authorise hold case transition known commit reconcile', 'bind check', 'admin', ''],
 'global-api-exchange-and-reconciliation-process': ['', 'request read', 'auth accept intent inbound plan known evidence derive denied reconcile', 'execute', '', ''],
}

# Reuse the checked-in overview router without executing its diagram generator.
module = ast.parse((ROOT / 'work/build-spain-continuous-horizontal.py').read_text())
router = ast.Module(body=[n for n in module.body if isinstance(n, ast.FunctionDef) and n.name in ('ports', 'route')], type_ignores=[])
scope = {'heapq': heapq}
exec(compile(router, '<overview-router>', 'exec'), scope)
route = scope['route']

def style(value):
    return dict(item.split('=', 1) for item in value.split(';') if '=' in item)

def set_style(cell, **values):
    original = cell.get('style', '')
    flags = [item for item in original.split(';') if item and '=' not in item]
    current = style(original)
    current.update({k: str(v) for k, v in values.items()})
    cell.set('style', ';'.join(flags + [k + '=' + v for k, v in current.items()]) + ';')

def geometry(cell):
    g = cell.find('mxGeometry')
    return tuple(float(g.get(k, '0')) for k in ('x', 'y', 'width', 'height'))

def fmt(number):
    return f'{number:g}'

def plain(value):
    return unescape(re.sub('<[^>]+>', ' ', value)).strip()

def label_html(label, subtitle=''):
    main = escape(label).replace(' - ', ' -<br>')
    return '<b>' + main + '</b>' + ('<br><span style="font-size:12px">' + escape(subtitle) + '</span>' if subtitle else '')

def cell(root, id, value, x, y, w, h, styling):
    c = ET.SubElement(root, 'mxCell', id=id, value=value, style=styling, vertex='1', parent='1')
    ET.SubElement(c, 'mxGeometry', x=fmt(x), y=fmt(y), width=fmt(w), height=fmt(h), attrib={'as': 'geometry'})
    return c

def html_text(svg, x, y, w, h, value, size=14, align='center', inset=10):
    foreign = ET.SubElement(svg, 'foreignObject', x=fmt(x + inset), y=fmt(y + inset), width=fmt(w - 2 * inset), height=fmt(h - 2 * inset))
    div = ET.SubElement(foreign, 'div', {'xmlns': XHTML, 'style': f'font-family:Arial,sans-serif;font-size:{size}px;line-height:1.18;color:#222;box-sizing:border-box;width:100%;height:100%;display:flex;align-items:center;justify-content:{"center" if align == "center" else "flex-start"};text-align:{align};overflow:visible;'})
    inner = ET.SubElement(div, 'div', {'class': 'diagram-text', 'style': 'max-width:100%;overflow-wrap:break-word;'})
    # Existing Draw.io labels are simple HTML; preserve their formatting and words.
    fragment = value.replace('&nbsp;', '&#160;').replace('<br>', '<br/>').replace('<BR>', '<br/>')
    fragment = re.sub(r'&(?!#\d+;|#x[0-9a-fA-F]+;|amp;|lt;|gt;|quot;|apos;)', '&amp;', fragment)
    try:
        parsed = ET.fromstring('<div xmlns="' + XHTML + '">' + fragment + '</div>')
        inner.text = parsed.text
        for child in parsed:
            for item in child.iter():item.tag=item.tag.split('}')[-1]
            inner.append(child)
    except ET.ParseError:
        inner.text = plain(value)
    return foreign

def shape(svg, box, styling):
    x, y, w, h = box
    s = style(styling)
    attributes = {'fill': s.get('fillColor', '#fff'), 'stroke': s.get('strokeColor', '#444'), 'stroke-width': s.get('strokeWidth', '2')}
    if s.get('dashed') == '1':
        attributes['stroke-dasharray'] = s.get('dashPattern', '7 5')
    if 'ellipse;' in styling or s.get('shape')=='ellipse':
        ET.SubElement(svg, 'ellipse', cx=fmt(x+w/2), cy=fmt(y+h/2), rx=fmt(w/2), ry=fmt(h/2), attrib=attributes)
    elif 'rhombus;' in styling or s.get('shape')=='rhombus':
        ET.SubElement(svg, 'polygon', points=f'{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}', attrib=attributes)
    elif s.get('shape') in ('hexagon', 'parallelogram', 'trapezoid', 'octagon'):
        points = ([(x+22,y),(x+w-22,y),(x+w,y+h/2),(x+w-22,y+h),(x+22,y+h),(x,y+h/2)] if s['shape']=='hexagon' else [(x+22,y),(x+w,y),(x+w-22,y+h),(x,y+h)] if s['shape']=='parallelogram' else [(x+22,y),(x+w-22,y),(x+w,y+h),(x,y+h)] if s['shape']=='trapezoid' else [(x+18,y),(x+w-18,y),(x+w,y+18),(x+w,y+h-18),(x+w-18,y+h),(x+18,y+h),(x,y+h-18),(x,y+18)])
        ET.SubElement(svg, 'polygon', points=' '.join(f'{a},{b}' for a,b in points), attrib=attributes)
    elif s.get('shape')=='cylinder':
        path=f'M {x},{y+12} C {x},{y-4} {x+w},{y-4} {x+w},{y+12} L {x+w},{y+h-12} C {x+w},{y+h+4} {x},{y+h+4} {x},{y+h-12} Z'
        ET.SubElement(svg,'path',d=path,attrib=attributes)
        ET.SubElement(svg,'path',d=f'M {x},{y+12} C {x},{y+28} {x+w},{y+28} {x+w},{y+12}',fill='none',stroke=attributes['stroke'],attrib={'stroke-width':attributes['stroke-width']})
    elif s.get('shape')=='document':
        ET.SubElement(svg,'path',d=f'M {x},{y} L {x+w},{y} L {x+w},{y+h-12} C {x+w*.75},{y+h-32} {x+w*.25},{y+h+8} {x},{y+h-12} Z',attrib=attributes)
    else:
        ET.SubElement(svg, 'rect', x=fmt(x), y=fmt(y), width=fmt(w), height=fmt(h), rx='8' if s.get('rounded')=='1' else '0', attrib=attributes)

def rebuild(name, assignments):
    file = OUT / (name + '.drawio')
    tree = ET.parse(file)
    oldroot = tree.find('.//mxGraphModel/root')
    oldsvg = ET.parse(file.with_suffix('.svg')).getroot()
    cells = {c.get('id'): c for c in oldroot.findall('mxCell') if c.get('edge')!='1'}
    selected = {id: lane for lane, ids in enumerate(assignments) for id in ids.split()}
    assert all(id in cells for id in selected), name
    original_edges = [copy.deepcopy(c) for c in oldroot.findall('mxCell') if c.get('edge')=='1']
    for edge in original_edges:
        if edge.get('id') in cells:
            edge.set('id', 'connector-' + edge.get('id'))
    referenced = {id for e in original_edges for id in (e.get('source'),e.get('target')) if id}
    assert referenced <= selected.keys(), (name, referenced-selected.keys())
    # Two existing external-exchange frames have labelled subcards.
    children = {'G1': ['X1','X2']} if name=='e-invoicing-outbound-exchange-pilot' else {'35':['36','37','38','39']} if name=='spain-invoice-preparation-and-outbound-flow' else {}
    nested = {id for ids in children.values() for id in ids}
    nodes = {id: copy.deepcopy(cells[id]) for id in selected}
    if name=='spain-invoice-preparation-and-outbound-flow':
        nodes['35'].set('value', '12  Independent external obligations')
        set_style(nodes['35'], verticalAlign='top', spacingTop='10', fontSize='14', html='1', whiteSpace='wrap')
        for e in original_edges:
            if not e.get('source'): e.set('source', '35')
            if not e.get('target'): e.set('target', '35')
    groups = defaultdict(list)
    for id in selected:
        if id not in nested: groups[selected[id]].append(id)
    width = float(tree.find('.//mxGraphModel').get('pageWidth'))
    left = 290
    pos = {}
    lane_boxes = {}
    y = 170
    for lane in sorted(groups):
        rows = []
        row_heights = []
        placements = {}
        for id in sorted(groups[lane], key=lambda i: (geometry(nodes[i])[0], geometry(nodes[i])[1], i)):
            x, old_y, w, h = geometry(nodes[id])
            if id not in children:
                h = max(h, 110 if 'rhombus;' in nodes[id].get('style','') else 100)
            row = next((i for i, boxes in enumerate(rows) if all(x+w+24 <= a or x >= b+24 for a,b in boxes)), len(rows))
            if row == len(rows): rows.append([]); row_heights.append(0)
            rows[row].append((x,x+w));row_heights[row]=max(row_heights[row],h)
            placements[id]=(x,w,h,row)
        height = sum(row_heights) + max(0,len(rows)-1)*30 + 64
        lane_boxes[lane] = (25,y,width-50,height)
        for id,(x,w,h,row) in placements.items():
            ny = y+32+sum(row_heights[:row])+30*row
            pos[id]=(x,ny,w,h)
            if id in children:
                old_x,old_y,_,_=geometry(cells[id])
                for child in children[id]:
                    cx,cy,cw,ch=geometry(cells[child]);pos[child]=(cx+x-old_x,cy+ny-old_y,cw,ch)
        y += height + 14
    height = y+104
    model = tree.find('.//mxGraphModel')
    model.set('pageWidth',fmt(width));model.set('pageHeight',fmt(height));model.set('dx',fmt(width));model.set('dy',fmt(height))
    root = ET.Element('root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
    model.remove(oldroot);model.append(root)
    title_node = oldsvg.find('{' + SVG + '}title')
    title = title_node.text if title_node is not None else tree.find('diagram').get('name')
    subtitle = NOTE
    svg = ET.Element('svg', xmlns=SVG, width=fmt(width), height=fmt(height), viewBox=f'0 0 {width:g} {height:g}', role='img', attrib={'aria-label':title})
    ET.SubElement(svg,'title').text=title
    desc=oldsvg.find('{' + SVG + '}desc')
    ET.SubElement(svg,'desc').text=(desc.text if desc is not None else '')+' '+NOTE
    ET.SubElement(svg,'rect',width=fmt(width),height=fmt(height),fill='white')
    cell(root,'title',title,25,15,width-50,42,'text;html=1;align=left;fontSize=26;fontStyle=1;')
    cell(root,'subtitle',NOTE,25,58,width-50,30,'text;html=1;align=left;fontSize=14;')
    html_text(svg,25,15,width-50,42,'<b>'+escape(title)+'</b>',26,'left',0)
    html_text(svg,25,58,width-50,30,escape(NOTE),14,'left',0)
    phases = [copy.deepcopy(c) for id,c in cells.items() if id.startswith('phase') and c.get('vertex')=='1']
    if name=='spain-invoice-preparation-and-outbound-flow':
        phase_names=['DRAFT PREPARATION','ERP ISSUANCE & FINAL CHECKS','ROUTING & EXCHANGE','OUTCOMES']
        phases=[copy.deepcopy(cells[str(i)]) for i in range(2,6)]
        for c,label in zip(phases,phase_names): c.set('value',label)
    for c in phases:
        set_style(c,html='1',fontSize='12',fontStyle='1')
        root.append(c);box=geometry(c);shape(svg,box,c.get('style',''));html_text(svg,*box,c.get('value',''),12,inset=2)
    for lane,box in lane_boxes.items():
        x,ly,w,lh=box
        c=cell(root,f'lane-{lane}',LABELS[lane],*box,'shape=swimlane;horizontal=0;startSize=250;noLabel=1;fillColor=#e5e5e5;swimlaneFillColor=#fafafa;strokeColor=#aaaaaa;')
        cell(root,f'lane-{lane}-label',label_html(LABELS[lane]),x,ly,250,lh,'text;html=1;fontSize=15;align=center;verticalAlign=middle;whiteSpace=wrap;spacing=16;strokeColor=none;fillColor=none;')
        ET.SubElement(svg,'rect',x=fmt(x),y=fmt(ly),width=fmt(w),height=fmt(lh),fill='#fafafa',stroke='#aaa')
        ET.SubElement(svg,'rect',x=fmt(x),y=fmt(ly),width='250',height=fmt(lh),fill='#e5e5e5',stroke='#aaa')
        html_text(svg,x,ly,250,lh,label_html(LABELS[lane]),15,inset=16)
    # Draw group frames behind their internal arrows and activity boxes.
    for id in children:
        c=nodes[id];x,ny,w,h=pos[id]
        g=c.find('mxGeometry');g.set('x',fmt(x));g.set('y',fmt(ny))
        root.append(c);shape(svg,pos[id],c.get('style',''))
        html_text(svg,x,ny,w,42,c.get('value',''),13,inset=6)
    view={'pos':{id:box for id,box in pos.items() if id not in nested},'left':left,'width':width,'height':height}
    label_boxes=[]
    for e in original_edges:
        sid,tid=e.get('source'),e.get('target')
        if sid in nested or tid in nested:
            # Internal branches stay inside their original external-exchange frame.
            frame = next(id for id,ids in children.items() if sid in ids or tid in ids)
            ox,oy,_,_=geometry(cells[frame]);nx,ny,_,_=pos[frame]
            geo=e.find('mxGeometry')
            for point in geo.iter('mxPoint'):
                if point.get('x') is not None:point.set('x',fmt(float(point.get('x'))+nx-ox))
                if point.get('y') is not None:point.set('y',fmt(float(point.get('y'))+ny-oy))
            source_point = geo.find("mxPoint[@as='sourcePoint']")
            target_point = geo.find("mxPoint[@as='targetPoint']")
            a,b=scope['ports'](pos[sid],pos[tid])[::3]
            if source_point is not None:a=(float(source_point.get('x')),float(source_point.get('y')))
            if target_point is not None:b=(float(target_point.get('x')),float(target_point.get('y')))
            points=[a]+[(float(p.get('x')),float(p.get('y'))) for p in geo.findall("Array/mxPoint")]+[b]
        else:
            points=route({'source':sid,'target':tid},view)
            geo=e.find('mxGeometry');geo.clear();geo.set('relative','1');geo.set('as','geometry')
            array=ET.SubElement(geo,'Array',attrib={'as':'points'})
            for px,py in points[1:-1]:ET.SubElement(array,'mxPoint',x=fmt(px),y=fmt(py))
        sx,sy,sw,sh=pos[sid];tx,ty,tw,th=pos[tid]
        set_style(e,edgeStyle='none',exitX=(points[0][0]-sx)/sw,exitY=(points[0][1]-sy)/sh,entryX=(points[-1][0]-tx)/tw,entryY=(points[-1][1]-ty)/th,exitPerimeter='0',entryPerimeter='0')
        root.append(e)
        dashed='dashed=1' in e.get('style','')
        attrs={'d':'M '+' L '.join(f'{px:g},{py:g}' for px,py in points),'fill':'none','stroke':'#555','stroke-width':'2'}
        if dashed:attrs['stroke-dasharray']='7 5'
        ET.SubElement(svg,'path',attrs)
        a,b=points[-2:];dx=b[0]-a[0];dy=b[1]-a[1];length=(dx*dx+dy*dy)**.5
        if length:
            ux,uy=dx/length,dy/length
            ET.SubElement(svg,'polygon',points=f'{b[0]},{b[1]} {b[0]-9*ux+4*uy},{b[1]-9*uy-4*ux} {b[0]-9*ux-4*uy},{b[1]-9*uy+4*ux}',fill='#555')
        label=e.get('workflowLabel', e.get('value',''))
        if label:
            lw=min(360,max(30,len(plain(label))*5.5+8));lh=22
            candidates=[]
            for a,b in sorted(zip(points,points[1:]),key=lambda pair: -(abs(pair[1][0]-pair[0][0])+abs(pair[1][1]-pair[0][1]))):
                for fraction in (.5,.25,.75):
                    px=a[0]+(b[0]-a[0])*fraction;py=a[1]+(b[1]-a[1])*fraction
                    if a[1]==b[1]:candidates.extend([(px-lw/2,py-lh-5,lw,lh),(px-lw/2,py+5,lw,lh)])
                    else:candidates.extend([(px+7,py-lh/2,lw,lh),(px-lw-7,py-lh/2,lw,lh)])
            obstacles=[box for id,box in pos.items() if id not in children]+label_boxes
            def clear(box):
                x,ly,w,lh=box
                return x>=275 and x+w<=width-15 and all(x+w+3<=a or x>=a+bw+3 or ly+lh+3<=b or ly>=b+bh+3 for a,b,bw,bh in obstacles)
            chosen=next((box for box in candidates if clear(box)),None)
            if chosen is None:
                # Use the clear padding above or below nearby activities.
                for a,b in zip(points,points[1:]):
                    px=(a[0]+b[0])/2
                    for _,ny,_,nh in pos.values():
                        candidates.extend([(px-lw/2,ny-lh-6,lw,lh),(px-lw/2,ny+nh+6,lw,lh)])
                chosen=next((box for box in candidates if clear(box)),None)
            assert chosen is not None,(name,'No free connector label position',label)
            lx,ly,_,_=chosen;label_boxes.append(chosen)
            ET.SubElement(svg,'rect',x=fmt(lx),y=fmt(ly),width=fmt(lw),height=fmt(lh),fill='white')
            html_text(svg,*chosen,label,11,inset=0)
            # Store the same explicit edge-label position for the Draw.io viewer.
            label_id='label-'+e.get('id')
            cell(root,label_id,label,*chosen,'text;html=1;fontSize=11;align=center;verticalAlign=middle;whiteSpace=wrap;fillColor=#ffffff;strokeColor=none;')
            e.set('value','')
            e.set('workflowLabel',label)
    for id,c in nodes.items():
        if id in children:continue
        x,ny,w,h=pos[id]
        g=c.find('mxGeometry');g.set('x',fmt(x));g.set('y',fmt(ny));g.set('width',fmt(w));g.set('height',fmt(h))
        if id not in children:set_style(c,html='1',whiteSpace='wrap',fontSize='14',fontFamily='Arial')
        root.append(c)
        shape(svg,pos[id],c.get('style',''))
        html_text(svg,*pos[id],c.get('value',''),14,inset=18 if 'rhombus;' in c.get('style','') else 12)
    footer=cells.get('footer')
    footer_text=footer.get('value','') if footer is not None else (desc.text if desc is not None else '')
    if name=='spain-invoice-preparation-and-outbound-flow':
        footer_text='Record each action asynchronously; acknowledgement is not buyer acceptance. Alternatives for delivery; copy is a separate conditional duty.'
    cell(root,'footer',footer_text,25,height-75,width-50,58,'text;html=1;fontSize=13;align=left;whiteSpace=wrap;')
    html_text(svg,25,height-75,width-50,58,escape(plain(footer_text)),13,'left',0)
    ET.register_namespace('xhtml',XHTML)
    tree.write(file,encoding='utf-8',xml_declaration=True)
    file.with_suffix('.svg').write_text(ET.tostring(svg,encoding='unicode'))
    print(name, 'labelled lanes='+str(len(lane_boxes)), 'nodes='+str(len(nodes)), 'edges='+str(len(original_edges)))

def vertical_headers(name, headings):
    file=OUT/(name+'.drawio');tree=ET.parse(file);root=tree.find('.//mxGraphModel/root')
    svg_tree=ET.parse(file.with_suffix('.svg'));svg=svg_tree.getroot()
    for index,(label,subtitle) in enumerate(headings):
        lane=next(c for c in root.findall('mxCell') if c.get('id')=='lane'+str(index))
        lane.set('value',label);set_style(lane,noLabel='1',startSize='60')
        x,y,w,h=geometry(lane)
        existing=next((c for c in root.findall('mxCell') if c.get('id')=='lane'+str(index)+'-label'),None)
        if existing is not None:root.remove(existing)
        cell(root,'lane'+str(index)+'-label',label_html(label,subtitle),x,y,w,60,'text;html=1;fontSize=14;align=center;verticalAlign=middle;whiteSpace=wrap;spacing=4;strokeColor=none;fillColor=none;')
        # Replace the original single-line SVG header, retaining the whole process layout.
        for child in list(svg):
            if child.tag.split('}')[-1]=='foreignObject' and abs(float(child.get('x','-1'))-(x+3))<.1 and abs(float(child.get('y','-1'))-(y+3))<.1:
                svg.remove(child)
            if child.tag=='{'+SVG+'}text' and child.get('x') and x<=float(child.get('x'))<=x+w and y<=float(child.get('y','0'))<=y+60:
                svg.remove(child)
            if child.tag=='{'+SVG+'}rect' and float(child.get('x','-1'))==x and float(child.get('y','-1'))==y and float(child.get('height','0'))==45:
                child.set('height','60')
        html_text(svg,x,y,w,60,label_html(label,subtitle),14,inset=3)
    ET.register_namespace('',SVG);ET.register_namespace('xhtml',XHTML)
    tree.write(file,encoding='utf-8',xml_declaration=True);svg_tree.write(file.with_suffix('.svg'),encoding='utf-8',xml_declaration=True)
    print(name,'explicit vertical headers='+str(len(headings)))

if __name__=='__main__':
    for name,groups in GROUPS.items():rebuild(name,groups)
    vertical_headers('spain-ubl-dts-generation-process',[(LABELS[2],'Generation consumer / records'),(LABELS[3],'DTS API / orchestration'),(LABELS[3],'DTS mapper / validation')])
    vertical_headers('spain-ubl-dts-migration-process',[(LABELS[4],'Spain / consumer owners'),(LABELS[3],'DTS engineering / QA'),(LABELS[4],'DTS release / operations')])
