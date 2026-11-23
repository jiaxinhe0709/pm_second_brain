"""Render retrieval previews from the editable Draw.io source without changing it."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-retrieval-overview-process'


def build(base=BASE, description=None):
    spec = importlib.util.spec_from_file_location(
        'drawio_preview', ROOT / 'work/build-invoice-sending-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    renderer.BASE = base
    renderer.build()
    svg = ET.parse(base.with_suffix('.svg'))
    ns = '{http://www.w3.org/2000/svg}'
    # The shared preview renderer draws dashed outlines as short paths. Add the
    # source fill separately so linked dashed shapes retain their background.
    native = ET.parse(base.with_suffix('.drawio'))
    page = native.find('.//mxGraphModel')
    width, height = page.get('pageWidth'), page.get('pageHeight')
    svg.getroot().attrib.update(width=width, height=height,
                                viewBox=f'0 0 {width} {height}')
    background = svg.getroot().find(ns + 'rect')
    background.attrib.update(x='0', y='0', width=width, height=height)
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
    svg.find('{http://www.w3.org/2000/svg}desc').text = description or (
        'Five actions: receive invoice, view invoice list, select and open invoice, '
        'download file, and review and take action. Invoices are received automatically. '
        'Users can view saved invoices after access and safety checks, even if ERP '
        'delivery is not complete. If the original is not saved, choose a permitted '
        'public source or recipient-side private connection and obtain the original. '
        'An authorised faithful copy preserves view/download access and public-file '
        'evidence while original retrieval is pending. It does not complete ERP intake. '
        'No source, denied access and failed retrieval keep original recovery open. '
        'Check the recipient account and receiving connection; the customer restores '
        'access and the receiving provider checks delivery. Ask the sender for the '
        'existing original or destination evidence only if delivery is unresolved. '
        'R returns a retrieved file to source '
        'and role checks before delivery; its relationship to any saved copy must '
        'be proved. From the opened invoice, users can download a file '
        'or review and take action. Download is optional. Buyer actions when only a copy '
        'is available remain an open decision in SPEC026. The ERP uses Query e-invoices '
        'and Retrieve e-invoice for lists, details and file links. The file source sends '
        'the selected file through its downloadUrl. Pale green shows customer actions '
        'and ERP steps. Pale purple shows getting, checking and processing invoice files. '
        'White or light grey shows notes and what is needed before starting. Colours '
        'do not show whether a function is ready or built. E marks a problem or pending '
        'result. Matching S markers link checked saved files to the invoice list.')
    svg.write(base.with_suffix('.svg'), encoding='unicode')
    with pymupdf.open(base.with_suffix('.svg')) as image:
        with pymupdf.open('pdf', image.convert_to_pdf()) as pdf:
            pdf[0].get_pixmap(alpha=False).save(base.with_suffix('.png'))
    # PyMuPDF omits SVG anchor children, so add interactive links after raster QA.
    for group in svg.iter(ns + 'g'):
        if 'data-source' in group.attrib:
            group.tag = ns + 'a'
            group.set('href', group.attrib.pop('data-source'))
    svg.write(base.with_suffix('.svg'), encoding='unicode')
    return base.with_suffix('.svg')


if __name__ == '__main__':
    build()
