"""Render source-choice previews without changing the editable Draw.io file."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/receiving-source-selection-process'


def build():
    spec = importlib.util.spec_from_file_location(
        'source_choice_preview', ROOT / 'work/build-invoice-sending-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    renderer.BASE = BASE
    renderer.build()
    svg = ET.parse(BASE.with_suffix('.svg'))
    ns = '{http://www.w3.org/2000/svg}'
    for obj in ET.parse(BASE.with_suffix('.drawio')).iter('object'):
        cell = obj.find('mxCell')
        style = dict(part.split('=', 1) for part in cell.get('style', '').split(';') if '=' in part)
        if style.get('dashed') == '1':
            geom = cell.find('mxGeometry')
            group = svg.find(f".//{ns}g[@id='{obj.get('id')}']")
            group.insert(0, ET.Element(ns + 'rect', {
                key: geom.get(key) for key in ('x', 'y', 'width', 'height')
            } | {'fill': style.get('fillColor', '#ffffff')}))
    svg.find(ns + 'desc').text = (
        'Before receiving, use the company’s authorised setup to obtain a public '
        'original, private original or public copy. Four plain-English routes '
        'include private-download failure, whose automatic recovery rules remain '
        'open. Safe copy access does not release ERP delivery without the original. '
        'Saved files continue at receiving step 1.')
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')
    with pymupdf.open(BASE.with_suffix('.svg')) as source:
        with pymupdf.open('pdf', source.convert_to_pdf()) as pdf:
            pdf[0].get_pixmap(alpha=False).save(BASE.with_suffix('.png'))
    for group in svg.iter(ns + 'g'):
        if 'data-source' in group.attrib:
            group.tag = ns + 'a'
            group.set('href', group.attrib.pop('data-source'))
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')


if __name__ == '__main__':
    build()
