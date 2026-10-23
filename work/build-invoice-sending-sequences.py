"""Build the sending companion diagrams without changing existing assets."""
from pathlib import Path
import importlib.util
import math
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sending_sequence_renderer', ROOT / 'work/onboarding-sequence-renderer.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
SPEC = '../../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md'


def build():
    sequences = []
    s = renderer.Sequence('invoice-sending-fr-submission-sequence',
        'FR submission and observation', 'Existing guide flow; Spain contracts and implementation remain to qualify',
        SPEC + '#21-documented-fr-submission-and-observation',
        ['ERP / product', 'E-Invoice API', 'File upload', 'Events'])
    s.note('Precondition: current business/action authority, qualified CONNECTED setup and approved final files. HTTP intake is separate from processing, delivery and buyer acceptance.', 'OUT-08/11/12; INT-SND01 prerequisites')
    s.exchange(0, 3, 'POST /internal/events/subscriptions', 'Subscription result; success code/schema not supplied', '[Existing] INT-SND01 step 1')
    s.exchange(0, 1, 'POST /datasets/{datasetId}/e-invoices', '201 Created: e-invoice ID and uploadUrl per file', '[Existing] INT-SND01 step 2')
    f = s.start_frame('loop | Each required file in the qualified manifest')
    s.exchange(0, 2, 'PUT {uploadUrl}: exact binary file', '200 OK: upload result', '[Existing] INT-SND01 step 3')
    s.end_frame(f)
    s.note('Upload completion remains to qualify. INT-ERR01 says notification follows attempt handling; ERROR is final for that attempt. Follow platform retry ownership, not a fresh product POST.', 'INT-SND01; INT-ERR01; SND-G04/05')
    s.exchange(3, 0, 'Status-updated webhook; subject = e-invoice ID', 'Webhook receipt; exact response contract to qualify', '[Existing] INT-SND01 step 4', '[To qualify] SND-G05')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}', '200 OK: currentStatus and history; retain actual meaning', '[Existing] INT-SND01 step 5')
    sequences.append(s)

    s = renderer.Sequence('invoice-sending-spain-actions-sequence',
        'Spain final plan and independent actions', 'Proposed logical handoffs; OUT-Q03 must prove issuance/copy coordination',
        SPEC + '#22-spain-final-plan-and-independent-actions',
        ['ERP / product', 'E-Invoice Service', 'Public platform', 'Private platform'])
    s.exchange(0, 1, 'Final candidate: stable identity, revision and business scope', 'Qualified plan or owned hold; no issuance on a failed check', '[To qualify] OUT-07–11; SND-G01/03/06')
    s.note('Complete current authority/approval, recipient eligibility, final-byte validation and trust. Freeze independent action identities before external execution.', 'OUT-08–11; OUT-Q01/03')
    f = s.start_frame('alt | Qualified private route with a required public copy')
    parallel = s.start_frame('par | Independent copy and recipient actions; no shared completion')
    g = s.start_frame('ref | Logical ERP issuance + copy boundary; no physical atomicity claim')
    s.note('ERP issuance and copy transmission must meet the qualified boundary together. The call below shows public transport, not an approved scheduling or issuance API.', 'OUT-06/12; OUT-Q03; SPFE-S02 Article 4')
    s.exchange(1, 2, 'SendInvoice: qualified faithful-copy Invoice attachment', 'Transport / request / item result; copy action evidence', '[Existing transport] SPFE-S16; [To qualify] Spain binding')
    s.end_frame(g)
    s.exchange(1, 3, 'Deliver exact invoice on the frozen recipient route', 'Independent recipient-delivery result or outcome unknown', '[To qualify] OUT-12/13; SND-G02/04')
    s.end_frame(parallel)
    s.end_frame(f)
    f = s.start_frame('else | Proven no private entry point; qualified public recipient route')
    s.note('Retain ERP issuance evidence for the qualified public-original path. This branch does not invoke the Article 4 private-issuance copy boundary.', 'OUT-06/07/12; SND-G01/06')
    s.exchange(1, 2, 'SendInvoice: qualified public original / interconnection action', 'Independent recipient-action result; no redundant public copy', '[Existing transport] SPFE-S16; OUT-09/12; SPFE-S02')
    s.end_frame(f)
    s.note('The ref frame states a coordination obligation, not call timing. Private delivery success is not the copy trigger. Failed/stale/ambiguous lookup holds dispatch; reconcile each unknown action against its original context.', 'OUT-SPFE-R01; SPFE-S02 Article 4; OUT-09/13')
    sequences.append(s)

    s = renderer.Sequence('invoice-sending-recovery-sequence',
        'Uncertain action: observe before repetition', 'Preserve the original business, route, input and action identity',
        SPEC + '#23-missing-or-uncertain-result',
        ['ERP / product', 'E-Invoice API', 'Original platform', 'Operations'])
    f = s.start_frame('opt | The Sage e-invoice ID is known')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}', '200 detail or failed read; neither proves global absence', '[Existing] INT-SND01 step 5')
    s.end_frame(f)
    s.note('If the POST response was lost and the ID is unknown, this guide supplies no discovery-by-key operation. Preserve the request; do not create another invoice.', 'OUT-13; SND-G04')
    s.exchange(1, 2, 'Observe the original action using its qualified correlation', 'Proven success, qualified absence or unresolved evidence', '[To qualify] OUT-13; SND-G04/05')
    s.exchange(1, 3, 'Assign unresolved evidence and safe next action', 'Owned hold; assignment is not external completion', '[To qualify] OUT-13/15; SND-G04')
    s.note('Record confirmed success once. Retry proven absence only under the selected safe contract and current authority. Retain completed delivery while a public copy remains unknown.', 'OUT-A07/08/16; no new retry API is implied')
    sequences.append(s)

    paths = []
    for s in sequences:
        assert len(s.messages) == 2 * len(s.activations)
        paths.append(s.write([
            'Solid arrows: requests. Dashed arrows: paired responses. Grey bars: handling, not elapsed time.',
            'Existing labels identify supplied evidence; To qualify labels do not define new endpoints or deployed service boundaries.',
        ]))
    return paths


if __name__ == '__main__':
    import pymupdf
    paths = build()
    for path in paths:
        svg = ET.parse(path).getroot()
        # The local SVG rasterizer does not honour stroke-dasharray consistently.
        # Expand the straight dashed strokes for raster input only; keep SVG editable.
        for edge in svg.iter('{http://www.w3.org/2000/svg}path'):
            if 'stroke-dasharray' not in edge.attrib:
                continue
            points = edge.get('d').replace('M ', '').replace(' L ', ',').split(',')
            x1, y1, x2, y2 = map(float, points)
            length = math.hypot(x2-x1, y2-y1)
            parts = []
            for start in range(0, int(length), 13):
                end = min(start+7, length)
                parts.append(f'M {x1+(x2-x1)*start/length},{y1+(y2-y1)*start/length} L {x1+(x2-x1)*end/length},{y1+(y2-y1)*end/length}')
            edge.set('d', ' '.join(parts))
            del edge.attrib['stroke-dasharray']
        doc = pymupdf.open(stream=ET.tostring(svg), filetype='svg')
        page = doc.convert_to_pdf()
        pdf = pymupdf.open('pdf', page)
        pdf[0].get_pixmap(alpha=False).save(path.with_suffix('.png'))
        print(path.name, svg.get('width'), svg.get('height'))
