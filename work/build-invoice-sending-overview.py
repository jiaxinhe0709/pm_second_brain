"""Build the SEI022 scenario overview as editable Draw.io, SVG and PNG."""
from pathlib import Path
import math
import textwrap
import xml.etree.ElementTree as ET

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-sending-end-to-end-workflow'
WIDTH, HEIGHT = 2000, 1110
SOURCE = '../../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md'

# Keep the route/copy decision visible; detailed exceptions stay in SEI023.
NODES = [
    ('draft', 80, 205, 245, 95, 'flow', 'Draft entry', 'Complete business invoice data', ''),
    ('validation', 385, 205, 285, 95, 'flow', 'Prepare and validate', 'Review and correct the draft', ''),
    ('invoice', 55, 430, 270, 125, 'flow', '1. Provide final invoice', 'Final candidate or existing issued proof', ''),
    ('ready', 385, 430, 310, 125, 'flow', '2. Confirm sending readiness', 'Authority, final validation and required files, including PDF', ''),
    ('route', 790, 420, 250, 145, 'decision', 'Recipient route?', '', ''),
    ('private', 1120, 350, 430, 115, 'flow', 'Private recipient delivery', 'Structured invoice to the recipient\'s private platform', ''),
    ('copy', 1120, 520, 430, 115, 'flow', 'Faithful copy to public', 'Separate action, coordinated with ERP issuance', ''),
    ('public', 1120, 690, 430, 115, 'flow', 'Public recipient delivery', 'Structured invoice through public platform; no extra copy', ''),
    ('results', 1640, 490, 305, 200, 'scope', 'Separate results', 'Recipient delivery, public copy and PDF delivery each keep their own result', ''),
    ('pdf', 55, 680, 640, 125, 'conditional', 'Local product generates PDF when required', 'Send to buyer via a qualified private attachment or a separate channel. Never send this PDF to the public platform.', ''),
]
EDGES = [
    ('draft', 'validation', [(325,252),(385,252)], False, '', None),
    ('validation', 'invoice', [(527,300),(527,365),(190,365),(190,430)], True, 'Conditional draft path', (260,392)),
    ('invoice', 'ready', [(325,492),(385,492)], False, '', None),
    ('ready', 'route', [(695,492),(790,492)], False, '', None),
    ('route', 'private', [(1040,492),(1070,492),(1070,407),(1120,407)], False, '', None),
    ('route', 'copy', [(1040,492),(1070,492),(1070,577),(1120,577)], False, '', None),
    ('route', 'public', [(915,565),(915,747),(1120,747)], False, 'Public route', (950,728)),
    ('private', 'results', [(1550,407),(1590,407),(1590,527),(1640,527)], True, '', None),
    ('copy', 'results', [(1550,577),(1640,577)], True, '', None),
    ('public', 'results', [(1550,747),(1590,747),(1590,650),(1640,650)], True, '', None),
]
FOOTER = [
    'One invoice for a business user or authorised accountant. Detailed rules and PDF applicability remain in SEI023 / PRD-SEI-246.',
]


def build():
    svg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', width=str(WIDTH), height=str(HEIGHT),
        viewBox=f'0 0 {WIDTH} {HEIGHT}', role='img', attrib={'aria-label':'Single-invoice sending: private delivery and separate public copy, or public delivery; local product generates the recipient PDF'})
    ET.SubElement(svg, 'title').text = 'Invoice sending: private and public routes'
    ET.SubElement(svg, 'desc').text = 'A business user or authorised accountant sends one invoice. Private delivery and faithful public copy are independent actions; public delivery needs no extra copy. Local Product generates any required transitional PDF for the recipient only. Draft preparation remains inside a red dashed TBC boundary. ' + ' '.join(FOOTER)
    ET.SubElement(svg, 'rect', width=str(WIDTH), height=str(HEIGHT), fill='white')
    mx = ET.Element('mxfile', host='app.diagrams.net', type='device', version='24.7.17')
    diagram = ET.SubElement(mx, 'diagram', id=BASE.name, name='End-to-end sending overview')
    graph = ET.SubElement(diagram, 'mxGraphModel', page='1', pageWidth=str(WIDTH), pageHeight=str(HEIGHT))
    root = ET.SubElement(graph, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')

    def text(x, y, value, size=18, anchor='start', color='#222', key=None):
        ET.SubElement(svg, 'text', x=str(x), y=str(y), fill=color,
            attrib={'font-family':'Arial, sans-serif','font-size':str(size),'text-anchor':anchor}).text=value
        if key:
            c = ET.SubElement(root, 'mxCell', id=key, value=value, vertex='1', parent='1',
                style=f'text;html=0;align={"center" if anchor=="middle" else "left"};fontSize={size};fontColor={color};')
            ET.SubElement(c, 'mxGeometry', x=str(x-700 if anchor=='middle' else x), y=str(y-size), width=str(1400 if anchor=='middle' else WIDTH-x-55), height=str(size+10), attrib={'as':'geometry'})

    text(55,50,'Invoice sending: private and public routes',30,key='title')
    text(55,88,'Red dashed frame: TBC · Solid arrows: action flow · Grey dashed arrows: conditional handoff or independent observations',17,color='#555',key='legend')

    # Draw the red frame as explicit dash segments for consistent PNG rendering.
    parts=[]
    for (x1,y1),(x2,y2) in [((55,140),(695,140)),((695,140),(695,340)),((695,340),(55,340)),((55,340),(55,140))]:
        length=math.hypot(x2-x1,y2-y1)
        for start in range(0,int(length),18):
            end=min(start+11,length)
            parts.append(f'M {x1+(x2-x1)*start/length},{y1+(y2-y1)*start/length} L {x1+(x2-x1)*end/length},{y1+(y2-y1)*end/length}')
    ET.SubElement(svg,'path',id='draft-tbc-boundary',d=' '.join(parts),fill='none',stroke='#c62828',attrib={'stroke-width':'2.5'})
    frame=ET.SubElement(root,'mxCell',id='draft-tbc-boundary',value='',vertex='1',parent='1',
        style='rounded=0;fillColor=none;strokeColor=#c62828;strokeWidth=2.5;dashed=1;dashPattern=11 7;')
    ET.SubElement(frame,'mxGeometry',x='55',y='140',width='640',height='200',attrib={'as':'geometry'})
    text(75,178,'TBC · Draft entry, preparation and validation',21,color='#c62828',key='draft-tbc-label')
    text(850,170,'One invoice for one represented business',22,key='scope-title')
    text(850,210,'A business user or authorised accountant uses the same flow.',18,key='scope-actor')
    text(850,245,'No batch request or portfolio coordinator is required.',18,key='scope-unit')
    text(850,280,'Start with a final candidate or qualified already-issued evidence.',18,key='scope-entry')
    text(1120,325,'Private route · two independent actions',20,key='private-route-label')
    for index,(source,target,points,dashed,label,where) in enumerate(EDGES):
        attrs={'d':'M '+' L '.join(f'{x},{y}' for x,y in points),'fill':'none','stroke':'#555','stroke-width':'2'}
        # Explicit segments keep dashed SVG and raster previews consistent.
        if dashed:
            parts=[]
            for (x1,y1),(x2,y2) in zip(points,points[1:]):
                length=math.hypot(x2-x1,y2-y1)
                for start in range(0,int(length),13):
                    end=min(start+7,length)
                    parts.append(f'M {x1+(x2-x1)*start/length},{y1+(y2-y1)*start/length} L {x1+(x2-x1)*end/length},{y1+(y2-y1)*end/length}')
            attrs['d']=' '.join(parts)
        ET.SubElement(svg,'path',attrs)
        a,b=points[-2:];dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy);ux,uy=dx/length,dy/length
        ET.SubElement(svg,'path',d=f'M {b[0]},{b[1]} L {b[0]-10*ux+5*uy},{b[1]-10*uy-5*ux} L {b[0]-10*ux-5*uy},{b[1]-10*uy+5*ux} Z',fill='#555')
        c=ET.SubElement(root,'mxCell',id=f'edge-{index}',value=label,edge='1',parent='1',source=source,target=target,
            style='edgeStyle=none;strokeColor=#555555;endArrow=block;'+('dashed=1;' if dashed else ''))
        geometry=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
        ET.SubElement(geometry,'mxPoint',x=str(points[0][0]),y=str(points[0][1]),attrib={'as':'sourcePoint'})
        ET.SubElement(geometry,'mxPoint',x=str(points[-1][0]),y=str(points[-1][1]),attrib={'as':'targetPoint'})
        arr=ET.SubElement(geometry,'Array',attrib={'as':'points'})
        for x,y in points[1:-1]:ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
        if label:text(*where,label,16)

    for key,x,y,w,h,kind,title,note,refs in NODES:
        assert 0<x<x+w<WIDTH and 0<y<y+h<HEIGHT-130
        fill={'scope':'#e6e6e6','flow':'#f1f1f1','conditional':'#fafafa','decision':'#e6e6e6','recovery':'#d9d9d9'}[kind]
        link=ET.SubElement(svg,'g',id=key,attrib={'data-source':SOURCE+'#3-process-and-activity-order'})
        if kind=='decision':
            ET.SubElement(link,'path',d=f'M {x+w/2},{y} L {x+w},{y+h/2} L {x+w/2},{y+h} L {x},{y+h/2} Z',fill=fill,stroke='#555')
        else:
            ET.SubElement(link,'rect',x=str(x),y=str(y),width=str(w),height=str(h),rx=str(40 if kind=='scope' else 9),fill=fill,stroke='#555')
        title_lines=textwrap.wrap(title,24 if kind=='decision' else int(w/11))
        note_lines=textwrap.wrap(note,int((w-35)/8))
        lines_height=len(title_lines)*24+len(note_lines)*21+8+(17 if refs else 0)
        assert lines_height <= h-8, (key, lines_height, h)
        top=y+(h-lines_height)/2
        for line in title_lines:
            text(x+w/2,top+20,line,20,'middle');top+=24
        top+=4
        for line in note_lines:
            text(x+w/2,top+17,line,17,'middle','#444');top+=21
        top+=4
        if refs:text(x+w/2,top+13,refs,13,'middle','#666')
        obj=ET.SubElement(root,'object',id=key,label='\n'.join([title,note,refs]),link=SOURCE+'#3-process-and-activity-order')
        shape='rhombus;' if kind=='decision' else f'rounded=1;arcSize={80 if kind=="scope" else 12};'
        c=ET.SubElement(obj,'mxCell',vertex='1',parent='1',style=shape+f'whiteSpace=wrap;html=0;fontSize=17;spacing=12;fillColor={fill};strokeColor=#555555;')
        ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    text(55,855,'ERP owns issuance. Coordinate the required public copy with issuance, not with successful private delivery (OUT-Q03).',18,color='#444',key='issuance-note')
    text(55,885,'Unresolved route: hold dispatch. Action observations are independent; the results box is not a completion join.',18,color='#444',key='action-note')
    text(55,915,'Already-issued paths retain proof. Late-copy recovery does not redefine the normal issuance boundary.',18,color='#444',key='issued-note')
    ET.SubElement(svg,'rect',x='55',y='960',width='1890',height='90',rx='8',fill='#f5f5f5',stroke='#aaa')
    note=ET.SubElement(root,'mxCell',id='exception-note',value='If work is blocked or uncertain\nHold the affected action, preserve known results and return an owned next step. Reconcile possible external effects before repetition.',vertex='1',parent='1',style='rounded=1;whiteSpace=wrap;html=0;spacing=16;fontSize=18;align=left;fillColor=#f5f5f5;strokeColor=#aaaaaa;')
    ET.SubElement(note,'mxGeometry',x='55',y='960',width='1890',height='90',attrib={'as':'geometry'})
    text(80,993,'If work is blocked or uncertain',21)
    text(80,1028,'Hold the affected action, preserve known results and return an owned next step. Reconcile possible external effects before repetition.',18)
    for i,line in enumerate(FOOTER):text(55,1085+i*25,line,17,color='#555',key=f'footer-{i}')
    BASE.with_suffix('.svg').write_text(ET.tostring(svg,encoding='unicode'))
    ET.indent(mx)
    BASE.with_suffix('.drawio').write_text(ET.tostring(mx,encoding='unicode',xml_declaration=True))
    image=pymupdf.open(BASE.with_suffix('.svg'))
    pdf=pymupdf.open('pdf',image.convert_to_pdf())
    pdf[0].get_pixmap(alpha=False).save(BASE.with_suffix('.png'))
    print(BASE.relative_to(ROOT))


if __name__=='__main__':build()
