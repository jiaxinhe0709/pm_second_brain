"""Render receiving previews from Draw.io without changing its editable source."""
from pathlib import Path
from html import unescape
import copy
import importlib.util
import re
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/receiving-intake-and-delivery-process'


def plain(value):
    value = re.sub(r'<br\s*/?>', '\n', value, flags=re.I)
    return unescape(re.sub(r'<[^>]+>', '', value))


def build():
    tree = ET.parse(BASE.with_suffix('.drawio'))
    root = tree.find('.//mxGraphModel/root')
    cells = {c.get('id'): c for c in root}

    def absolute(key):
        c = cells[key]
        g = c.find('mxGeometry')
        x, y = float(g.get('x', 0)), float(g.get('y', 0))
        if c.get('parent') not in (None, '0', '1'):
            px, py = absolute(c.get('parent'))
            x, y = x + px, y + py
        return x, y

    # The shared preview renderer accepts flat cells. Flatten a temporary copy;
    # preserve Draw.io's native lane membership and HTML labels in the source.
    flattened = copy.deepcopy(tree)
    target = flattened.find('.//mxGraphModel/root')
    for c in list(target):
        c.set('value', plain(c.get('value', '')))
        if c.get('vertex') != '1':
            continue
        g = c.find('mxGeometry')
        x, y = absolute(c.get('id'))
        g.set('x', str(x))
        g.set('y', str(y))
        c.set('parent', '1')
        if c.get('id') in ('lane-1', 'lane-2', 'lane-3', 'lane-4'):
            c.set('value', '')
            c.set('style', 'fillColor=#fafafa;strokeColor=#aaaaaa;')
            strip = copy.deepcopy(c)
            strip.set('id', c.get('id') + '-strip')
            strip.set('style', 'fillColor=#e5e5e5;strokeColor=#aaaaaa;')
            strip.find('mxGeometry').set('width', '250')
            target.insert(list(target).index(c) + 1, strip)

    spec = importlib.util.spec_from_file_location(
        'receiving_preview', ROOT / 'work/build-invoice-sending-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    with tempfile.TemporaryDirectory(prefix='receiving-preview-') as folder:
        temporary = Path(folder) / BASE.name
        flattened.write(temporary.with_suffix('.drawio'), encoding='unicode')
        renderer.BASE = temporary
        renderer.build()
        svg = ET.parse(temporary.with_suffix('.svg'))
        ns = '{http://www.w3.org/2000/svg}'
        svg.find(ns + 'desc').text = (
            'Detailed action A: automatic inbound receiving after source capture. '
            'The receiving phase band is above all swimlanes. Customer/accountant '
            'has no required action. ERP/product, E-Invoice Service and Other '
            'Services handle checks, repeats, original/copy holds, conditional '
            'Phase 3 conversion and verified ERP receipt. Customer consultation '
            'is shown separately in overview frames B–E and its API sequence.')
        svg.write(BASE.with_suffix('.svg'), encoding='unicode')
        BASE.with_suffix('.png').write_bytes(temporary.with_suffix('.png').read_bytes())
    print('Receiving Draw.io source preserved; SVG and PNG previews refreshed.')


if __name__ == '__main__':
    build()
