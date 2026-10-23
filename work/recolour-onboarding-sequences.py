"""Apply reuse colours and a header legend to the five SPEC021 sequences."""
from pathlib import Path
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / 'specs/onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md'
OUT = ROOT / 'work/onboarding-colour-review'
GREY, BLUE = '#626262', '#1565C0'
PAINT_KEYS = {'fontColor', 'strokeColor', 'fillColor'}
SVG = 'http://www.w3.org/2000/svg'
HEADER_NOTE = 'Existing = documented API / guide; To qualify = logical handoff, no confirmed Spain contract.'
ET.register_namespace('', SVG)


def signature(node, native=False, ignore_legend=False):
    """Ignore paint and formatting whitespace; retain every other property."""
    attrs = dict(node.attrib)
    if native:
        if 'style' in attrs:
            attrs['style'] = ';'.join(
                item for item in attrs['style'].split(';')
                if item and item.split('=', 1)[0] not in PAINT_KEYS)
    else:
        attrs = {key: value for key, value in attrs.items() if key not in {'fill', 'stroke'}}
    children = [child for child in node if not (ignore_legend and (
        child.get('id', '').startswith('reuse-legend-')
        or child.get('value') == HEADER_NOTE
        or (child.tag.rsplit('}', 1)[-1] == 'text' and child.text == HEADER_NOTE)))]
    return (node.tag, tuple(sorted(attrs.items())), (node.text or '').strip(),
            tuple(signature(child, native, ignore_legend) for child in children))


def add_legend(svg, native):
    graph = native.find('.//root')
    for parent in (svg, graph):
        for child in list(parent):
            if (child.get('id', '').startswith('reuse-legend-')
                    or child.get('value') == HEADER_NOTE
                    or (child.tag.rsplit('}', 1)[-1] == 'text' and child.text == HEADER_NOTE)):
                parent.remove(child)
    for name, x, colour, label in (
        ('grey', 30, GREY, 'Existing FR API / flow'),
        ('blue', 340, BLUE, 'Spain adaptation / proposed work'),
    ):
        key = f'reuse-legend-{name}'
        ET.SubElement(svg, f'{{{SVG}}}rect', id=key + '-swatch', x=str(x), y='91',
                      width='13', height='13', fill=colour)
        ET.SubElement(svg, f'{{{SVG}}}text', id=key + '-label', x=str(x + 23), y='103',
                      fill=colour, attrib={'font-family': 'Arial, sans-serif',
                                          'font-size': '14'}).text = label
        swatch = ET.SubElement(graph, 'mxCell', id=key + '-swatch', value='',
                              parent='1', vertex='1',
                              style=f'rounded=0;fillColor={colour};strokeColor=none;')
        ET.SubElement(swatch, 'mxGeometry', x=str(x), y='91', width='13', height='13',
                      attrib={'as': 'geometry'})
        text = ET.SubElement(graph, 'mxCell', id=key + '-label', value=label,
                            parent='1', vertex='1', style=(
                                'text;html=0;whiteSpace=wrap;spacing=0;verticalAlign=top;'
                                f'align=left;fontSize=14;fontColor={colour};'))
        ET.SubElement(text, 'mxGeometry', x=str(x + 23), y='89', width='260' if name == 'grey' else '440', height='24',
                      attrib={'as': 'geometry'})


def set_paint(cell, key, value):
    cell.set('style', re.sub(rf'(^|;){key}=[^;]*',
                            lambda match: match[1] + key + '=' + value,
                            cell.get('style', '')))


def geometry(cell):
    geo = cell.find('mxGeometry')
    return tuple(float(geo.get(key, 0)) for key in ('x', 'y', 'width', 'height'))


def apply_colours(svg_path):
    svg_path = Path(svg_path)
    native_path = svg_path.with_suffix('.drawio')
    svg = ET.parse(svg_path).getroot()
    native = ET.parse(native_path).getroot()
    before_svg, before_native = signature(svg), signature(native, True)
    process_svg = signature(svg, ignore_legend=True)
    process_native = signature(native, True, ignore_legend=True)
    cells = list(native.iter('mxCell'))
    by_id = {cell.get('id'): cell for cell in cells if cell.get('id')}
    messages = {}
    for key, cell in by_id.items():
        if not re.fullmatch(r'message-\d+', key):
            continue
        label = by_id[key.replace('message-', 'message-label-')]
        source_y = geometry(label)[1] - 19
        source = [item for item in cells if 'fontSize=12;' in item.get('style', '')
                  and item.find('mxGeometry') is not None
                  and geometry(item)[1] == source_y]
        assert len(source) == 1, (svg_path.name, key, source)
        arrow_y = float(cell.find('mxGeometry/mxPoint').get('y'))
        messages[arrow_y] = {'key': key, 'source': source[0], 'label': label,
                             'source_baseline': source_y + 12}
    colours = {}
    for cell in cells:
        if not cell.get('id', '').startswith('activation-'):
            continue
        _, start, _, duration = geometry(cell)
        request, response = messages[start], messages[start + duration]
        colour = GREY if request['source'].get('value', '').startswith('[Existing') else BLUE
        colours[start] = colours[start + duration] = colour
    assert set(colours) == set(messages), 'Every request and return must have a handling interval'
    bands = [(info['source_baseline'], y, colours[y]) for y, info in messages.items()]
    text_colours = {}
    for y, info in messages.items():
        for item in (by_id[info['key']], info['label'], info['source']):
            text_colours[id(item)] = colours[y]

    frames = []
    for cell in cells:
        label = cell.get('value', '')
        if not label.startswith(('ref |', 'opt |')):
            continue
        # These frames select existing discovery and observation behaviour.
        existing = label.startswith((
            'opt | A supported service choice', 'opt | Known connection needs detail',
            'opt | Known authorised dataset', 'opt | Known connection; qualified safe detail read'))
        colour = GREY if existing else BLUE
        x, y, _, _ = geometry(cell)
        frames.append((x - 12, y - 8, colour))
        text_colours[id(cell)] = colour

    for cell in cells:
        colour = text_colours.get(id(cell), GREY)
        cell_style = cell.get('style', '')
        if 'fontColor=' in cell_style:
            set_paint(cell, 'fontColor', colour)
        if 'strokeColor=' in cell_style and 'strokeColor=none' not in cell_style:
            set_paint(cell, 'strokeColor', colour)
        # Participant boxes, lifelines and handling bars remain neutral.
        if cell.find('mxGeometry') is not None:
            x, y, _, height = geometry(cell)
            for fx, fy, frame_colour in frames:
                if (x, y) == (fx, fy):
                    set_paint(cell, 'strokeColor', frame_colour)
                    if height == 34:
                        set_paint(cell, 'fillColor', '#EFF6FF' if frame_colour == BLUE else '#FAFAFA')

    for element in svg:
        tag = element.tag.rsplit('}', 1)[-1]
        if element.get('stroke') not in (None, 'none'):
            element.set('stroke', GREY)
        if tag == 'text':
            x, y = float(element.get('x')), float(element.get('y'))
            colour = next((c for start, end, c in bands if start <= y <= end), GREY)
            for fx, fy, frame_colour in frames:
                if (x, y) == (fx + 12, fy + 23):
                    colour = frame_colour
            element.set('fill', colour)
        elif tag == 'path':
            points = [float(number) for number in re.findall(r'-?\d+(?:\.\d+)?', element.get('d', ''))]
            ys = points[1::2]
            colour = GREY
            if ys and max(ys) - min(ys) <= 12:
                colour = next((colours[y] for y in ys if y in colours), GREY)
            element.set('stroke', colour)
            if element.get('fill') not in (None, 'none'):
                element.set('fill', colour)
        elif tag == 'rect':
            x, y = float(element.get('x', 0)), float(element.get('y', 0))
            for fx, fy, colour in frames:
                if (x, y) == (fx, fy):
                    element.set('stroke', colour)
                    if float(element.get('height', 0)) == 34:
                        element.set('fill', '#EFF6FF' if colour == BLUE else '#FAFAFA')
    assert signature(svg) == before_svg, 'SVG content or geometry changed'
    assert signature(native, True) == before_native, 'Draw.io content, links or geometry changed'
    add_legend(svg, native)
    assert signature(svg, ignore_legend=True) == process_svg, 'SVG process changed'
    assert signature(native, True, ignore_legend=True) == process_native, 'Draw.io process changed'
    svg_path.write_text(ET.tostring(svg, encoding='unicode'))
    ET.indent(native)
    native_path.write_text(ET.tostring(native, encoding='unicode', xml_declaration=True))
    return {'svg': str(svg_path.relative_to(ROOT)), 'process_content_and_geometry_preserved': True,
            'header_legend_added': True,
            'request_response_pairs': len(messages) // 2,
            'grey_messages': [messages[y]['key'] for y in sorted(messages) if colours[y] == GREY],
            'blue_messages': [messages[y]['key'] for y in sorted(messages) if colours[y] == BLUE]}


def main():
    protected = list((ROOT / 'specs/onboarding').glob('*.md'))
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
    paths = [(SPEC.parent / target).resolve() for target in re.findall(r'^!\[[^\]]*\]\(([^)]+\.svg)\)', SPEC.read_text(), re.M)]
    assert len(paths) == 5 and all(path.name.startswith('onboarding-reuse-') for path in paths)
    report = [apply_colours(path) for path in paths]
    assert all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == value for p, value in hashes.items())
    OUT.mkdir(exist_ok=True)
    nav = ''.join(f'<a href="#diagram-{i}">{html.escape(ET.parse(p).getroot().find("{http://www.w3.org/2000/svg}title").text)}</a>' for i, p in enumerate(paths))
    diagrams = ''.join(f'<section id="diagram-{i}"><div class="diagram">{p.read_text()}</div></section>' for i, p in enumerate(paths))
    (OUT / 'index.html').write_text('''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SPEC021 diagram colour review</title>
<style>body{margin:0;font:16px/1.5 Arial,sans-serif;color:#444;background:#f5f5f5}main{max-width:1480px;margin:24px auto;padding:0 20px}h1{font-size:27px}nav{display:flex;flex-wrap:wrap;gap:20px}a{color:#1565c0}section{margin:28px 0}.diagram{overflow:auto;border:1px solid #ccc;background:white}.diagram svg{display:block;max-width:none}.grey{color:#626262}.blue{color:#1565c0}</style></head><body><main>
<h1>SPEC021: diagram colour review</h1><p><strong class="grey">Grey: existing FR calls and flow.</strong> <strong class="blue">Blue: Spain adaptations and proposed work.</strong></p>
<p>Each diagram includes the colour legend. Process wording, layout, arrows and call order are preserved. Participants and handling bars remain neutral. Existing calls still require Spain qualification.</p><nav>''' + nav + '</nav>' + diagrams + '</main></body></html>')
    (OUT / 'validation.json').write_text(json.dumps({'markdown_unchanged': hashes, 'diagrams': report, 'published': False}, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
