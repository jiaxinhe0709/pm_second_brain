"""Render retrieval previews from the editable Draw.io source without changing it."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-retrieval-overview-process'


def build():
    spec = importlib.util.spec_from_file_location(
        'drawio_preview', ROOT / 'work/build-invoice-sending-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    renderer.BASE = BASE
    renderer.build()
    svg = ET.parse(BASE.with_suffix('.svg'))
    ns = '{http://www.w3.org/2000/svg}'
    # The shared preview renderer draws dashed outlines as short paths. Add the
    # source fill separately so the customer-settings colour remains visible.
    native = ET.parse(BASE.with_suffix('.drawio'))
    for obj in native.iter('object'):
        cell = obj.find('mxCell')
        style = dict(part.split('=', 1) for part in cell.get('style', '').split(';') if '=' in part)
        if style.get('dashed') != '1':
            continue
        geom = cell.find('mxGeometry')
        group = svg.find(f".//{ns}g[@id='{obj.get('id')}']")
        group.insert(0, ET.Element(ns + 'rect', {
            key: geom.get(key) for key in ('x', 'y', 'width', 'height')
        } | {'fill': style.get('fillColor', '#ffffff')}))
    svg.find('{http://www.w3.org/2000/svg}desc').text = (
        'Collect received invoices using existing onboarding access. Preserve each '
        'original or faithful copy with its source. The three Spain examples '
        'illustrate file roles; provider support remains unconfirmed.')
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')
    with pymupdf.open(BASE.with_suffix('.svg')) as image:
        with pymupdf.open('pdf', image.convert_to_pdf()) as pdf:
            pdf[0].get_pixmap(alpha=False).save(BASE.with_suffix('.png'))
    # PyMuPDF omits SVG anchor children, so add interactive links after raster QA.
    for group in svg.iter(ns + 'g'):
        if 'data-source' in group.attrib:
            group.tag = ns + 'a'
            group.set('href', group.attrib.pop('data-source'))
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')
    return BASE.with_suffix('.svg')


if __name__ == '__main__':
    build()
