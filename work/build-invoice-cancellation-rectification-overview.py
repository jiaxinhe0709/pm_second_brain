"""Build the separate cancellation and rectification flows without external calls."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])
SPEC = '../../specs/SPEC-SEI-047-spfe-to-sage-einvoice-api-mapping.md#cancellation-and-rectification-flows'
loader = importlib.util.spec_from_file_location(
    'invoice_action_flow', ROOT / 'work/build-onboarding-scenario-diagrams.py')
flow = importlib.util.module_from_spec(loader)
loader.loader.exec_module(flow)


def build():
    n, e = flow.node, flow.edge
    nodes = [
        n('cancel-check', 0, 0, 'Check cancellation eligibility', 'Issuer / authorised representative',
          'Sent/pending or full customer rejection; no real operation'),
        n('cancel-request', 0, 0, 'Request cancellation of the existing invoice', 'SPEC-SEI-023 / SPEC-SEI-024',
          'Proposed Sage action; public mapping: CancelInvoice'),
        n('cancel-result', 0, 0, 'Check the original cancellation result', 'Sending: request, response and recovery',
          'A receipt or timeout does not prove cancellation'),
        n('cancel-history', 0, 0, 'Retain the evidenced result and history', 'Lifecycle: resulting cancelled state',
          'Only confirmed cancellation sets cancelled', 'outcome'),
        n('rectify-prepare', 0, 0, 'Prepare a rectifying invoice', 'ERP / SPEC-SEI-015 IC-12',
          'New number and original reference; preserve the original'),
        n('rectify-issue', 0, 0, 'Issue the new invoice in the ERP', 'SPEC-SEI-015',
          'Qualified correction type, method and invoice content'),
        n('rectify-send', 0, 0, 'Submit through the normal sending flow', 'SPEC-SEI-043 / service 01',
          'POST + upload; SendInvoice for the applicable original/copy'),
        n('rectify-track', 0, 0, 'Track the new invoice independently', 'SPEC-SEI-029',
          'Its own acceptance, rejection and payment', 'outcome'),
    ]
    links = {
        'cancel-check': '../../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#proposed-cancel-eligibility',
        'cancel-request': '../../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#24-proposed-withdrawal-interaction',
        'cancel-result': '../../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#24-proposed-withdrawal-interaction',
        'cancel-history': '../../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#proposed-spain-invoice-states',
        'rectify-prepare': '../../specs/SPEC-SEI-015-invoice-creation-solution-specification.md#proposed-rectification-modify',
        'rectify-issue': '../../specs/SPEC-SEI-015-invoice-creation-solution-specification.md#proposed-rectification-modify',
        'rectify-send': '../../specs/invoice-sending/api-reference/SPEC-SEI-043-invoice-sending-api-reference.md#contract-baseline-and-reuse-assessment',
        'rectify-track': '../../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#proposed-spain-invoice-states',
    }
    positions, edges = {}, []
    for column, prefix in enumerate(('cancel', 'rectify')):
        group = [node for node in nodes if node['key'].startswith(prefix)]
        x = 50 + column * 700
        for index, node in enumerate(group):
            node['link'] = links[node['key']]
            positions[node['key']] = (x, 210 + index * 175, 600, 104)
            if index:
                previous = group[index - 1]['key']
                edges.append(e(previous, node['key'], points=[
                    (x + 300, 210 + (index - 1) * 175 + 104),
                    (x + 300, 210 + index * 175)]))
    path = flow.build(
        'invoice-cancellation-rectification-overview',
        'Spain: cancel or correct an issued invoice',
        'Two independent flows. Full customer rejection does not automatically cancel the invoice.',
        nodes, edges, spec=SPEC, positions=positions, width=1400, height=1090, lanes=[],
        legend='Solid arrows: steps within one flow. Cards link to the owning specifications.',
        captions=[(50, 188, 'CANCEL E-INVOICE'), (750, 188, 'CORRECT INVOICE (RECTIFY)')],
        boundaries=[
            'Cancellation denied: show the reason and permitted next action. Unknown result: reconcile the original cancellation attempt.',
            'Rectification: correct the new candidate before issuance; reconcile uncertain sending without repeating successful actions.',
            'SD-CANCEL01 design input. Sage cancellation contract and Spain implementation support remain open; see SPEC-SEI-047.',
        ])
    # Replace the generic onboarding classification line in both editable and preview assets.
    note = 'Read each flow from top to bottom. Check eligibility before starting the selected action.'
    svg = ET.parse(path)
    for element in svg.getroot():
        if element.tag.endswith('text') and element.get('y') == '143':
            element.text = note
    svg.write(path, encoding='unicode')
    native = ET.parse(path.with_suffix('.drawio'))
    for cell in native.getroot().iter('mxCell'):
        if cell.get('id') == 'behaviour-legend':
            cell.set('value', note)
    ET.indent(native)
    native.write(path.with_suffix('.drawio'), encoding='unicode', xml_declaration=True)
    # Check text bounds before rendering; Arial uses Helvetica metrics in this preview.
    font = pymupdf.Font('helv')
    for anchor in svg.getroot().iter(NS + 'a'):
        box = anchor.find(NS + 'rect')
        x, y, width, height = (float(box.get(key)) for key in ('x', 'y', 'width', 'height'))
        for text in anchor.findall(NS + 'text'):
            size = float(text.get('font-size'))
            length = font.text_length(text.text or '', fontsize=size)
            tx, ty = float(text.get('x')), float(text.get('y'))
            assert x + 4 <= tx - length / 2 and tx + length / 2 <= x + width - 4, text.text
            assert y + 4 <= ty - size and ty + size * .3 <= y + height - 4, text.text
    return path


if __name__ == '__main__':
    diagram = build()
    # MuPDF skips SVG link contents. Render an equivalent group-only copy for PNG.
    raster = ET.parse(diagram)
    for anchor in raster.getroot().iter(NS + 'a'):
        anchor.tag = NS + 'g'
        anchor.attrib.clear()
    with pymupdf.open(stream=ET.tostring(raster.getroot()), filetype='svg') as document:
        document[0].get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(diagram.with_suffix('.png'))
    print(diagram.relative_to(ROOT))
