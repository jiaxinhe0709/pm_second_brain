"""Generate SVG and PNG previews from the manually maintained Draw.io overview.

Supports the text, rounded rectangles, diamond and straight connectors used here.
The Draw.io file is the source; this script never writes it.
Run from any directory with the repository Python environment.
"""
from pathlib import Path
import math
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-sending-end-to-end-workflow'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def tag(name):
    return '{' + NS + '}' + name

def build():
    document = ET.parse(BASE.with_suffix('.drawio'))
    cells = {}
    for item in document.find('.//mxGraphModel/root'):
        cell = item.find('mxCell') if item.tag == 'object' else item
        if cell is None:
            continue
        key = item.get('id')
        style = dict(part.split('=', 1) for part in cell.get('style', '').split(';') if '=' in part)
        geom = cell.find('mxGeometry')
        cells[key] = dict(key=key, cell=cell, style=style, geom=geom,
                          label=item.get('label', cell.get('value', '')),
                          link=item.get('link'),
                          x=float(geom.get('x', 0)) if geom is not None else 0,
                          y=float(geom.get('y', 0)) if geom is not None else 0,
                          w=float(geom.get('width', 0)) if geom is not None else 0,
                          h=float(geom.get('height', 0)) if geom is not None else 0)
    vertices = [c for c in cells.values() if c['cell'].get('vertex') == '1' and c['cell'].get('parent') == '1']
    left = math.floor(min(c['x'] for c in vertices) - 20)
    top = math.floor(min(c['y'] for c in vertices) - 20)
    right = math.ceil(max(c['x'] + c['w'] for c in vertices) + 20)
    bottom = math.ceil(max(c['y'] + c['h'] for c in vertices) + 20)
    width, height = right-left, bottom-top
    svg = ET.Element(tag('svg'), width=str(width), height=str(height), viewBox=f'{left} {top} {width} {height}',
                     role='img', attrib={'aria-label': cells['title']['label']})
    ET.SubElement(svg, tag('title')).text = cells['title']['label']
    ET.SubElement(svg, tag('desc')).text = 'Preview generated from the editable Draw.io source. Private delivery and public copy keep separate results. The local product generates any required recipient PDF. A final handoff links to central lifecycle tracking for sent invoices.'
    ET.SubElement(svg, tag('rect'), x=str(left), y=str(top), width=str(width), height=str(height), fill='white')
    font = pymupdf.Font('helv')

    def element(parent, kind, **attrs):
        return ET.SubElement(parent, tag(kind), {k.replace('_', '-'): str(v) for k,v in attrs.items()})

    def text(parent, c, box=None, edge=False):
        style = c['style']
        value = c['label'].strip('\n')
        if not value:
            return
        x,y,w,h = box or (c['x'], c['y'], c['w'], c['h'])
        size = float(style.get('fontSize', 11 if edge else 17))
        spacing = float(style.get('spacing', 2))
        wrap = style.get('whiteSpace') == 'wrap'
        lines = []
        for paragraph in value.split('\n'):
            if not paragraph or not wrap:
                lines.append(paragraph)
                continue
            line = ''
            for word in paragraph.split():
                candidate = (line + ' ' + word).strip()
                if line and font.text_length(candidate, fontsize=size) > w-2*spacing:
                    lines.append(line)
                    line = word
                else:
                    line = candidate
            lines.append(line)
        line_height = size*1.2
        total = len(lines)*line_height
        if not edge and wrap and total > h:
            print(f'Label extends beyond source shape: {c["key"]} ({total:.1f}px in {h}px)')
        align = style.get('align', 'center')
        anchor = {'left':'start', 'center':'middle', 'right':'end'}[align]
        tx = x+spacing if align == 'left' else x+w-spacing if align == 'right' else x+w/2
        ty = y+(h-total)/2+size
        group = element(parent, 'g', fill=style.get('fontColor', '#000000'), font_family='Helvetica',
                        font_size=size, text_anchor=anchor)
        if edge:
            bgwidth = max(font.text_length(s, fontsize=size) for s in lines)+4
            element(group, 'rect', x=x+w/2-bgwidth/2, y=y+(h-total)/2, width=bgwidth, height=total, fill='white')
        for line in lines:
            element(group, 'text', x=tx, y=ty, fill=style.get('fontColor', '#000000'), font_family='Arial', font_size=size, text_anchor=anchor).text = line
            ty += line_height

    def boundary(c, toward, fx=None, fy=None):
        x,y,w,h = c['x'],c['y'],c['w'],c['h']
        if fx is not None:
            return (x+w*float(fx), y+h*float(fy))
        cx,cy = x+w/2,y+h/2
        dx,dy = toward[0]-cx,toward[1]-cy
        if dx == 0 and dy == 0:
            return cx,cy
        if 'rhombus' in c['cell'].get('style',''):
            scale = 1/(abs(dx)/(w/2)+abs(dy)/(h/2))
        else:
            scale = min(w/2/abs(dx) if dx else math.inf, h/2/abs(dy) if dy else math.inf)
        return cx+dx*scale,cy+dy*scale

    def dashed_path(points, dash=3, gap=3):
        parts = []
        for a,b in zip(points, points[1:]):
            length = math.dist(a,b)
            if not length:
                continue
            start = 0
            while start < length:
                end = min(start+dash, length)
                p = (a[0]+(b[0]-a[0])*start/length, a[1]+(b[1]-a[1])*start/length)
                q = (a[0]+(b[0]-a[0])*end/length, a[1]+(b[1]-a[1])*end/length)
                parts.append(f'M {p[0]},{p[1]} L {q[0]},{q[1]}')
                start += dash+gap
        return ' '.join(parts)

    def point(geom, name):
        el = geom.find(f"mxPoint[@as='{name}']")
        return (float(el.get('x',0)),float(el.get('y',0))) if el is not None else (0,0)

    def midpoint(points, relative):
        lengths = [math.dist(a,b) for a,b in zip(points, points[1:])]
        distance = (relative+1)/2*sum(lengths)
        for i,length in enumerate(lengths):
            if distance <= length or i == len(lengths)-1:
                a,b = points[i:i+2]
                ratio = distance/length if length else 0
                return a[0]+(b[0]-a[0])*ratio, a[1]+(b[1]-a[1])*ratio
            distance -= length

    # Preserve source drawing order: frame, connectors, nodes and notes.
    paths = {}
    for c in cells.values():
        cell,s,g = c['cell'],c['style'],c['geom']
        if cell.get('edge') == '1':
            waypoints = [(float(p.get('x',0)),float(p.get('y',0))) for p in g.findall("Array[@as='points']/mxPoint")]
            source = cells.get(cell.get('source'))
            target = cells.get(cell.get('target'))
            center = lambda n: (n['x']+n['w']/2,n['y']+n['h']/2)
            start = boundary(source, waypoints[0] if waypoints else center(target),s.get('exitX'),s.get('exitY')) if source else point(g,'sourcePoint')
            end = boundary(target, waypoints[-1] if waypoints else start,s.get('entryX'),s.get('entryY')) if target else point(g,'targetPoint')
            points = [start]+waypoints+[end]
            paths[c['key']] = points
            group = element(svg, 'g', id=c['key'])
            attrs = dict(d='M '+' L '.join(f'{x},{y}' for x,y in points), fill='none', stroke=s.get('strokeColor','#555555'), stroke_width=s.get('strokeWidth',1))
            if s.get('dashed') == '1':
                attrs['d'] = dashed_path(points)
            element(group,'path',**attrs)
            a,b = points[-2:]
            length = math.dist(a,b)
            dx,dy = (b[0]-a[0])/length,(b[1]-a[1])/length
            element(group,'path', d=f'M {b[0]},{b[1]} L {b[0]-7*dx-3*dy},{b[1]-7*dy+3*dx} L {b[0]-7*dx+3*dy},{b[1]-7*dy-3*dx} Z',fill=s.get('strokeColor','#555555'))
            if c['label']:
                x,y = midpoint(points,float(g.get('x',0)))
                ox,oy = point(g,'offset')
                text(group,c,(x+ox-150,y+oy-10,300,20),edge=True)
        elif cell.get('vertex') == '1' and cell.get('parent') == '1':
            group = element(svg, 'g', id=c['key'])
            if c['link']:
                group.set('data-source', c['link'])
            x,y,w,h = c['x'],c['y'],c['w'],c['h']
            rawstyle = cell.get('style','')
            if not rawstyle.startswith('text;'):
                attrs = dict(fill=s.get('fillColor','#ffffff'),stroke=s.get('strokeColor','#000000'),stroke_width=s.get('strokeWidth',1))
                if 'rhombus' in rawstyle:
                    element(group,'path',d=f'M {x+w/2},{y} L {x+w},{y+h/2} L {x+w/2},{y+h} L {x},{y+h/2} Z',**attrs)
                else:
                    radius = min(w,h)*float(s.get('arcSize',20))/200 if s.get('rounded')=='1' else 0
                    if s.get('dashed') == '1':
                        dash,gap = map(float,s.get('dashPattern','3 3').split())
                        element(group,'path',d=dashed_path([(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)],dash,gap),**attrs)
                    else:
                        element(group,'rect',x=x,y=y,width=w,height=h,rx=radius,**attrs)
            text(group,c)
        elif cell.get('vertex') == '1' and cell.get('parent') in paths:
            x,y = midpoint(paths[cell.get('parent')],c['x'])
            ox,oy = point(g,'offset')
            text(svg,c,(x+ox-150,y+oy-10,300,20),edge=True)
    svg_path = BASE.with_suffix('.svg')
    ET.indent(svg)
    svg_path.write_text(ET.tostring(svg, encoding='unicode')+'\n')
    image = pymupdf.open(svg_path)
    pdf = pymupdf.open('pdf',image.convert_to_pdf())
    pdf[0].get_pixmap(alpha=False).save(BASE.with_suffix('.png'))
    print(f'Generated SVG and PNG: {width} x {height}; Draw.io source unchanged.')

if __name__ == '__main__':
    build()
