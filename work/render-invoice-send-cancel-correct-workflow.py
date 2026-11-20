"""Render the separate proposal Draw.io file; never replace the original workflow."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-send-cancel-correct-workflow'


def build():
    spec = importlib.util.spec_from_file_location(
        'invoice_sending_preview', ROOT / 'work/build-invoice-sending-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    renderer.BASE = BASE
    renderer.build()
    # The reused renderer describes the original sending diagram by default.
    svg = ET.parse(BASE.with_suffix('.svg'))
    svg.find('{http://www.w3.org/2000/svg}desc').text = (
        'Separate proposal copied from invoice-sending-end-to-end-workflow.drawio. '
        'The customer chooses Send, Correct or Cancel. Correction creates a new '
        'invoice and joins existing sending step 1. Cancellation checks the earlier '
        'submission, state, reason and authority, then records its independent result. '
        'Full customer rejection does not automatically cancel an invoice. '
        'The existing sending steps, route branches and independent results are retained. '
        'Sage cancellation contracts and Spain implementation support remain unqualified.')
    svg.write(BASE.with_suffix('.svg'), encoding='unicode')


if __name__ == '__main__':
    build()
