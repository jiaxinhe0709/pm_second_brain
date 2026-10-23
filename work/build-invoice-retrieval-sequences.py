"""Build retrieval companion sequences; preserve existing diagrams and source specs."""
from pathlib import Path
import importlib.util
import math
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('retrieval_sequence_renderer', ROOT / 'work/onboarding-sequence-renderer.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
SPEC = '../../specs/invoice-receiving/SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md'


def build():
    sequences = []
    s = renderer.Sequence('invoice-retrieval-fr-notification-sequence',
        'FR notification and invoice-file capture',
        'Guide-evidenced calls; capture integration and Spain support remain to qualify',
        SPEC + '#21-fr-notification-detail-and-file-capture',
        ['ERP / product', 'E-Invoice API', 'Events', 'File source', 'Records'])
    s.note('Precondition: qualified dataset/address connection, current represented-business/action authority and correct access point/environment. A notification is not captured invoice bytes.', 'INT-RCV01 prerequisites; RRI-R02; RET-G01')
    s.exchange(0, 2, 'POST /internal/events/subscriptions',
        '201: subscription result; schema/casing to confirm', '[Existing] INT-RCV01 section 1')
    s.exchange(2, 0, 'Received webhook: subject = e-invoice ID',
        'Event receipt only; response contract to qualify', '[Existing] INT-RCV01 section 2', '[To qualify] RET-G02')
    s.note('Authenticate and check event scope. Correlate errors to the relevant history attempt. Follow INT-ERR01 platform retry/support actions; do not repeat capture to repair notification failure. Only qualified file-ready work continues below.', 'INT-RCV01 section 2; INT-ERR01; RET-G02')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}',
        '200: details, attachment roles and short-lived downloadUrl', '[Existing] INT-RCV01 section 3.1')
    f = s.start_frame('loop | Each required qualified source-file role')
    s.exchange(0, 3, 'GET {downloadUrl}; no Sage Authorization header',
        '200: actual file bytes; failure keeps capture incomplete', '[Existing] INT-RCV01 section 4')
    s.exchange(0, 4, 'Capture exact bytes, source role and integrity evidence',
        'Verified capture receipt, or incomplete/restricted state', '[To qualify] RSD-04; RET-G04/05')
    s.end_frame(f)
    s.note('List discovery can replace the webhook trigger. File capture does not establish canonical mapping, product consumption, source acknowledgement or buyer acceptance.', 'RRI-R02; RCV-01-09; RET-API-A02/03/04')
    sequences.append(s)

    s = renderer.Sequence('invoice-retrieval-spain-public-sequence',
        'Spain public discovery and separate file recovery',
        'Supplied PRE transport; business formats, authority and complete coverage remain gated',
        SPEC + '#22-spain-public-discovery-and-separate-file-recovery',
        ['ERP / product', 'E-Invoice Service', 'Public platform', 'Records'])
    s.note('A qualified automatic schedule is the public collection baseline. Optional refresh joins scoped work. Check current recipient authority, environment and source binding before protected calls.', 'RSD-01/02; SPFE-S02 Articles 9-11')
    s.exchange(0, 1, 'Optional refresh for the represented business',
        'Current scoped work and result; physical API to qualify', '[To qualify] RRI-Q02; no new endpoint implied')
    s.exchange(1, 2, 'GetRegisteredInvoice / QUERYBYFILTER',
        'Presentation-date results; qualified continuation evidence', '[Existing transport] SPFE-S03/S15; [To qualify] RET-G06')
    f = s.start_frame('opt | Identity or final-state consultation is required')
    s.exchange(1, 2, 'GetInvoices / QUERYBYID',
        'Scoped identity/status metadata; not invoice-file capture', '[Existing transport] SPFE-S03/S14')
    s.end_frame(f)
    f = s.start_frame('loop | Every covered item; locator OR identity recovery')
    s.exchange(1, 2, 'DownloadInvoicesByLOC OR DownloadInvoicesByID',
        'Invoice bytes with separate per-item success/failure', '[Existing transport] SPFE-S03/S12/S13; RET-G06')
    s.exchange(1, 3, 'Capture exact source, role and context',
        'Verified source reference/hash, or incomplete/restricted state', '[To qualify] RSD-04; RET-G05')
    s.end_frame(f)
    s.note('Receiving saves classification or pending handoff. Commit covered progress only when every item has source plus durable classification, or an approved ignore outcome. Pending handoff or failed download keeps the boundary incomplete.', 'RSD-05/06; RCV-01-09; RET-G03/09')
    s.note('SECUENCE_ID spelling is preserved. Query/download business formats remain pending in the supplied formats PDF; a WSDL operation is not complete schema or production-readiness evidence.', 'SPFE-S03/S08; RET-API-A06')
    sequences.append(s)

    s = renderer.Sequence('invoice-retrieval-file-recovery-sequence',
        'Expired-link recovery and independent stored-file access',
        'Keep invoice/file identity; temporary source links are separate from records access',
        SPEC + '#23-expired-links-interrupted-capture-and-stored-file-access',
        ['ERP / product', 'E-Invoice API', 'File source', 'Records'])
    f = s.start_frame('opt | Capture is incomplete and the original link has expired')
    s.exchange(0, 2, 'GET {original downloadUrl}',
        '403: classify against the actual expiry/error contract', '[Existing] INT-RCV01 section 4')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}',
        '200: fresh link for the same intended source-file role', '[Existing] INT-RCV01 section 3.1; [To qualify] binding')
    s.exchange(0, 2, 'GET {fresh downloadUrl}; no Sage bearer header',
        '200: complete bytes; failure keeps capture incomplete', '[Existing] INT-RCV01 section 4')
    s.exchange(0, 3, 'Verify/capture bytes under the existing item identity',
        'Verified receipt or incomplete/conflict state; no second invoice', '[To qualify] RSD-04; RET-G04/05')
    s.end_frame(f)
    s.note('Do not assume every 403 is expiry or that renewal proves byte immutability. Verify source role/content binding. Discard capability URLs; retain saved file references and integrity evidence.', 'RRI-A03/06; RET-G04')
    f = s.start_frame('opt | A customer requests an already captured file')
    s.exchange(0, 3, 'Read selected saved file under current action authority',
        'Labelled safe bytes and audited result, or owned denial/failure', '[To qualify] RSD-07/09; no physical endpoint supplied')
    s.end_frame(f)
    s.note('Mapping or ERP failure does not undo verified capture or permitted conservation access. This saved read neither calls the source nor requests format=facturx, creates another invoice or asserts buyer acceptance.', 'RRI-A05; RCV-A23; RET-API-A05/08')
    sequences.append(s)

    paths = []
    for s in sequences:
        assert len(s.messages) == 2 * len(s.activations)
        paths.append(s.write([
            'Solid arrows: requests. Dashed arrows: paired responses. Grey bars: handling, not elapsed time.',
            'Existing: supplied guide/transport evidence. To qualify: logical handoff or missing contract; no deployment decision.',
        ]))
    return paths


if __name__ == '__main__':
    import pymupdf
    for path in build():
        svg = ET.parse(path).getroot()
        # Expand dashed segments for the local rasterizer; keep source SVG editable.
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
        pdf = pymupdf.open('pdf', doc.convert_to_pdf())
        pdf[0].get_pixmap(alpha=False).save(path.with_suffix('.png'))
        print(path.name, svg.get('width'), svg.get('height'))
