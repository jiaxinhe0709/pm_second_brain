"""Offline UML-style SVG and native Draw.io from one editable scene."""
from pathlib import Path
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
WIDTH = 1800
XS = [130, 515, 900, 1285, 1670]


class Sequence:
    def __init__(self, slug, title, subtitle, source, parties):
        self.slug, self.title, self.subtitle = slug, title, subtitle
        self.source, self.parties = source, parties
        self.used = set()
        self.y = 258
        self.messages, self.notes, self.frames, self.activations = [], [], [], []
        self.open_calls = {}
        self.depth = 0

    def _message(self, a, b, label, source, kind):
        self.used.update((a, b))
        width = abs(XS[b] - XS[a]) - 38 if a != b else 260
        lines = []
        for paragraph in label.split('\n'):
            lines.extend(textwrap.wrap(paragraph, max(22, int(width / 8.5))))
        y = self.y + len(lines) * 23 + 22
        self.messages.append(dict(a=a, b=b, y=y, lines=lines, source=source,
                                  kind=kind, label=label))
        self.y = y + 36
        return y

    def call(self, a, b, label, source):
        y = self._message(a, b, label, source, 'call')
        token = len(self.messages)
        self.open_calls[token] = (a, b, y)
        return token

    def reply(self, token, label, source):
        a, b, start = self.open_calls.pop(token)
        end = self._message(b, a, label, source, 'reply')
        self.activations.append((b, start, end))

    def exchange(self, a, b, label, response, source, response_source=None):
        token = self.call(a, b, label, source)
        self.reply(token, response, response_source or source)

    def note(self, text, source=''):
        # Reflow notes when unused participants are removed at write time.
        lines = textwrap.wrap(text, 110)
        height = len(lines) * 22 + (24 if source else 0) + 22
        self.notes.append((self.y, height, lines, source))
        self.y += height + 24

    def start_frame(self, label):
        top = self.y
        self.y += 60
        frame = (top, label, self.depth)
        self.depth += 1
        return frame

    def end_frame(self, frame):
        self.depth -= 1
        top, label, depth = frame
        self.frames.append((top, self.y - top, label, depth))
        self.y += 30

    def write(self, footer):
        assert not self.open_calls, self.open_calls
        used = sorted(self.used)
        xs = {party: 130 + i * 385 for i, party in enumerate(used)}
        width = 260 + (len(used) - 1) * 385
        footer_lines = [part for line in footer for part in textwrap.wrap(line, int((width - 60) / 7.8))]
        height = self.y + 65 + len(footer_lines) * 23
        svg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg',
                         width=str(width), height=str(height),
                         viewBox=f'0 0 {width} {height}', role='img',
                         attrib={'aria-label': self.title})
        ET.SubElement(svg, 'title').text = self.title
        ET.SubElement(svg, 'desc').text = (self.subtitle + '. Solid arrows are requests; '
            'dashed arrows are paired responses. Grey bars show handling intervals, not duration. '
            + ' '.join(footer))
        ET.SubElement(svg, 'rect', width=str(width), height=str(height), fill='white')
        mx = ET.Element('mxfile', host='app.diagrams.net', type='device', version='24.7.17')
        diagram = ET.SubElement(mx, 'diagram', id=self.slug, name=self.title)
        graph = ET.SubElement(diagram, 'mxGraphModel', page='1', pageWidth=str(width), pageHeight=str(height))
        root = ET.SubElement(graph, 'root')
        ET.SubElement(root, 'mxCell', id='0')
        ET.SubElement(root, 'mxCell', id='1', parent='0')
        count = 0

        def vertex(value, style, x, y, w, h, key=None, link=None):
            nonlocal count
            count += 1
            owner = root
            if link:
                owner = ET.SubElement(root, 'object', id=key or f'v{count}', label=value, link=link)
                attrs = {}
            else:
                attrs = {'id': key or f'v{count}', 'value': value}
            cell = ET.SubElement(owner, 'mxCell', **attrs, parent='1', vertex='1', style=style)
            ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), attrib={'as': 'geometry'})

        def rect(x, y, w, h, fill='white', stroke='#777777', rounded=False, key=None):
            ET.SubElement(svg, 'rect', x=str(x), y=str(y), width=str(w), height=str(h),
                          fill=fill, stroke=stroke, rx='6' if rounded else '0')
            vertex('', f'rounded={int(rounded)};arcSize=8;fillColor={fill};strokeColor={stroke};',
                   x, y, w, h, key=key)

        def text(x, y, label, size=17, grey=False, center=False, key=None):
            lines = label.split('\n')
            color = '#888888' if grey else '#222222'
            for i, line in enumerate(lines):
                ET.SubElement(svg, 'text', x=str(x), y=str(y + i * 23),
                              fill=color, attrib={'font-family': 'Arial, sans-serif',
                              'font-size': str(size), 'text-anchor': 'middle' if center else 'start'}).text = line
            w = max(len(line) for line in lines) * size * .63 + 12
            vertex(label, 'text;html=0;whiteSpace=wrap;spacing=0;verticalAlign=top;'
                   f'align={"center" if center else "left"};fontSize={size};fontColor={color};',
                   x - w / 2 if center else x, y - size, w, len(lines) * 23 + 3, key=key)

        def edge(x1, y1, x2, y2, kind, key):
            dashed = kind in ('reply', 'lifeline')
            attrs = {'d': f'M {x1},{y1} L {x2},{y2}', 'fill': 'none',
                     'stroke': '#444444', 'stroke-width': '1.6'}
            if dashed:
                attrs['stroke-dasharray'] = '7 6'
            ET.SubElement(svg, 'path', attrs)
            if kind not in ('lifeline', 'divider'):
                direction = 1 if x2 > x1 else -1
                p = f'M {x2-direction*12},{y2-6} L {x2},{y2} L {x2-direction*12},{y2+6}'
                if kind == 'call':
                    p += ' Z'
                ET.SubElement(svg, 'path', d=p, fill='#444444' if kind == 'call' else 'none',
                              stroke='#444444', attrib={'stroke-width': '1.6'})
            cell = ET.SubElement(root, 'mxCell', id=key, edge='1', parent='1',
                style='edgeStyle=none;strokeColor=#444444;strokeWidth=1.6;'
                + ('dashed=1;' if dashed else '')
                + f'endArrow={"none" if kind in ("lifeline", "divider") else "open" if kind == "reply" else "block"};'
                + ('endFill=0;' if kind == 'reply' else ''))
            geom = ET.SubElement(cell, 'mxGeometry', relative='1', attrib={'as': 'geometry'})
            ET.SubElement(geom, 'mxPoint', x=str(x1), y=str(y1), attrib={'as': 'sourcePoint'})
            ET.SubElement(geom, 'mxPoint', x=str(x2), y=str(y2), attrib={'as': 'targetPoint'})

        rect(8, 8, width - 16, height - 16, rounded=True)
        text(30, 45, self.title, 27)
        text(30, 76, self.subtitle, 17)
        text(30, 104, 'Existing = documented API / guide; To qualify = logical handoff, no confirmed Spain contract.', 14, grey=True)
        edge(8, 124, width - 8, 124, 'divider', 'header-divider')
        for i in used:
            party, x = self.parties[i], xs[i]
            edge(x, 216, x, self.y + 8, 'lifeline', f'lifeline-{i}')
            rect(x - 108, 150, 216, 66, rounded=True, key=f'participant-{i}')
            text(x, 178 if '\n' in party else 190, party, 20, center=True)
        for top, h, label, depth in self.frames:
            x = 24 + depth * 12
            rect(x, top, width - x * 2, h, fill='none')
        for i, (party, start, end) in enumerate(self.activations):
            rect(xs[party] - 8, start, 16, end - start, fill='#dddddd', key=f'activation-{i}')
        # Keep frame labels above activation bars and lifelines.
        for top, h, label, depth in self.frames:
            x = 24 + depth * 12
            rect(x, top, width - x * 2, 34, fill='#fafafa')
            text(x + 12, top + 23, label, 15)
        for y, h, lines, source in self.notes:
            rect(38, y, width - 76, h, fill='#fafafa', stroke='#aaaaaa')
            text(52, y + 24, '\n'.join(lines), 16)
            if source:
                text(52, y + h - 12, source, 12, grey=True)
        for i, msg in enumerate(self.messages, 1):
            a, b, y = msg['a'], msg['b'], msg['y']
            direction = 1 if b > a else -1
            active_a = any(p == a and start <= y <= end for p, start, end in self.activations)
            active_b = any(p == b and start <= y <= end for p, start, end in self.activations)
            xa = xs[a] + (8 * direction if active_a else 0)
            xb = xs[b] - (8 * direction if active_b else 0)
            tx = (xs[a] + xs[b]) / 2
            top = y - len(msg['lines']) * 23 - 22
            rect(min(xs[a], xs[b]) + 12, top - 18, abs(xs[b] - xs[a]) - 24,
                 y - top + 9, stroke='none')
            text(tx, top, msg['source'], 12, grey=True, center=True)
            text(tx, top + 24, '\n'.join(msg['lines']), 17, center=True, key=f'message-label-{i}')
            edge(xa, y, xb, y, msg['kind'], f'message-{i}')
        for i, line in enumerate(footer_lines):
            text(30, self.y + 48 + i * 23, line, 14, grey=True)
        vertex('Source specification', 'text;html=0;fontSize=12;align=right;',
               width - 240, height - 30, 210, 18, link=self.source)
        ET.indent(mx)
        base = ROOT / 'assets/diagrams' / self.slug
        base.with_suffix('.svg').write_text(ET.tostring(svg, encoding='unicode'))
        base.with_suffix('.drawio').write_text(ET.tostring(mx, encoding='unicode', xml_declaration=True))
        return base.with_suffix('.svg')
