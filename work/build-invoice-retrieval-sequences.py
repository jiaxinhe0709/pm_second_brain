"""Build short receiving sequences with the onboarding grey/blue notation."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'work' / filename)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded
renderer = module('feature_sequence_renderer', 'onboarding-sequence-renderer.py')
palette = module('feature_sequence_colours', 'recolour-onboarding-sequences.py')

def finish(sequence):
    path = sequence.write([
        'Solid: request. Dashed: result. Grey bars show handling, not elapsed time.',
        'Blue: Spain binding or proposed work to confirm; it does not mean a new API or proven implementation.',
    ])
    palette.apply_colours(path)
    svg = ET.parse(path).getroot()
    native = ET.parse(path.with_suffix('.drawio')).getroot()
    for item in svg.iter():
        if item.text == 'Existing FR API / flow':
            item.text = 'Existing E-Invoice API / flow'
    for cell in native.iter('mxCell'):
        if cell.get('value') == 'Existing FR API / flow':
            cell.set('value', 'Existing E-Invoice API / flow')
    path.write_text(ET.tostring(svg, encoding='unicode'))
    ET.indent(native)
    path.with_suffix('.drawio').write_text(ET.tostring(native, encoding='unicode', xml_declaration=True))
    return path

SPEC = '../../specs/invoice-receiving/SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md'
def build():
    sequences = []
    s = renderer.Sequence('invoice-retrieval-fr-notification-sequence',
        'Receive an invoice: event, details and file',
        'Existing source-capture pattern; saved-file access needs separate qualification',
        SPEC + '#21-existing-notifications-details-and-files',
        ['ERP / product', 'E-Invoice API', 'Events', 'File source', 'Records'])
    s.note('Start with the authorised company dataset and platform connection. Check the event source and client scope before using its invoice ID.', 'RSD-01; RET-G01/02')
    s.exchange(0, 2, 'POST /internal/events/subscriptions',
        'Subscription result; save the selected scope', '[Existing] INT-RCV01 §1')
    s.exchange(2, 0, 'Received event: subject = invoice ID',
        'Event receipt; exact response to confirm', '[Existing] INT-RCV01 §2')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}',
        'Invoice details and each attachment downloadUrl', '[Existing] INT-RCV01 §3.1')
    s.exchange(0, 3, 'GET {downloadUrl} for each required file',
        'File bytes; no Sage bearer header', '[Existing] INT-RCV01 §4')
    s.exchange(0, 4, 'Save and verify source bytes, role and hash',
        'Saved file reference, or incomplete capture', '[Proposed] RSD-04; RET-G04/05')
    s.note('Listing can recover missed events. An error event needs its own action. Saved bytes do not prove product receipt or buyer acceptance.', 'INT-ERR01; RCV-01–09')
    sequences.append(s)

    s = renderer.Sequence('invoice-retrieval-spain-public-sequence',
        'Public collection: find, download and save invoices',
        'Phase 1: required SPFE collection; view and user download follow capture',
        SPEC + '#22-spain-public-discovery-and-separate-file-recovery',
        ['E-Invoice Service', 'Public platform', 'Records / receiving'])
    s.note('Automatic collection is the baseline. A customer refresh joins the same work. Check recipient permission before protected calls.', 'RSD-01/02; SPFE-S02 Articles 9–11')
    s.exchange(0, 1, 'GetRegisteredInvoice / QUERYBYFILTER',
        'Presentation-date results and continuation evidence', '[Spain] SPFE-S03/S15; RET-G06')
    f = s.start_frame('opt | Invoice identity or final status needs consultation')
    s.exchange(0, 1, 'GetInvoices / QUERYBYID',
        'Invoice identity/status metadata', '[Spain] SPFE-S03/S14')
    s.end_frame(f)
    s.exchange(0, 1, 'DownloadInvoicesByLOC OR DownloadInvoicesByID',
        'Files and separate item failures', '[Spain] SPFE-S03/S12/S13')
    s.exchange(0, 2, 'Save source files and receiving classification',
        'Saved results; incomplete items keep progress pending', '[Proposed] RSD-04–06')
    s.note('Commit only the covered items with saved source/classification or approved ignore results. Preserve SECUENCE_ID; exact continuation, authority and business formats still need confirmation.', 'RET-G03/06; SPFE-S08')
    sequences.append(s)

    s = renderer.Sequence('invoice-retrieval-file-recovery-sequence',
        'Recover a file link or read a saved file',
        'Required user download for public and private platforms',
        SPEC + '#23-expired-links-interrupted-capture-and-stored-file-access',
        ['ERP / product', 'E-Invoice API', 'File source', 'Records'])
    f = s.start_frame('case | Required file is missing; link expiry is confirmed')
    s.exchange(0, 1, 'GET existing invoice details',
        'Fresh link for the same required file role', '[Existing] INT-RCV01 §3.1')
    s.exchange(0, 2, 'GET {fresh downloadUrl}; no Sage bearer',
        'Complete bytes, or file still pending', '[Existing] INT-RCV01 §4')
    s.exchange(0, 3, 'Verify and save the missing file',
        'Saved receipt, or content conflict to resolve', '[Proposed] RSD-04; RET-G04/05')
    s.end_frame(f)
    f = s.start_frame('case | Public or private customer requests a saved file')
    s.exchange(0, 3, 'Check current permission and read saved bytes',
        'Labelled file and audit result, or denial/incident', '[Proposed] RSD-07/09; no endpoint supplied')
    s.end_frame(f)
    s.note('Not every 403 means expiry. Verify renewed content and retain good files. Saved reads do not refetch or generate Factur-X; mapping/product failure has its own recovery.', 'RRI-A03/05/06; RET-G04/05/08')
    sequences.append(s)

    sequences.append(view_download_sequence())
    return [finish(s) for s in sequences]


def view_download_sequence():
    """Build this view separately when the other receiving sequences are unchanged."""
    s = renderer.Sequence('invoice-retrieval-view-download-sequence',
        'Customer: view list, open invoice and download file',
        'The ERP uses existing calls; Spain coverage still needs qualification.',
        SPEC + '#24-required-view-and-user-download',
        ['Customer /\naccountant', 'ERP / product', 'Domain Service -\nE-Invoice Service', 'File source /\nrecords'])
    s.note('Customer consultation covers sent and received invoices. ERP calls the E-Invoice Service through the shared Query/Retrieve API. Reuse the NIF/business dataset binding and existing certificate/authority setup; the GETs use a Sage ID M2M token. Recheck current user/client permission. Automatic receiving is inbound only.', 'SPEC026 §2; RSD-07; RET-G01/03/05')
    f = s.start_frame('case | View invoice list — business level')
    request = s.call(0, 1, 'View invoice list', '[Proposed] SPEC026 §2')
    s.exchange(1, 2, 'GET /datasets/{datasetId}/e-invoices',
        'Permitted sent/received list, status, attachment count and qualified links.next paging',
        '[Existing] INT-RCV02; RET-API-01')
    s.reply(request, 'Invoice list and collection result; keep empty, failed and incomplete results distinct',
        '[Proposed] RSD-07; RET-G03/05')
    s.end_frame(f)
    f = s.start_frame('case | Select and open invoice — one invoice')
    request = s.call(0, 1, 'Select and open invoice', '[Proposed] SPEC026 §2')
    s.exchange(1, 2, 'GET /datasets/{datasetId}/e-invoices/{e-invoiceId}',
        'Selected invoice details, history, attachment count and included descriptors/URLs',
        '[Existing] INT-RCV03; RET-API-02')
    s.reply(request, 'Permitted invoice content and file choices, or reason content is unavailable',
        '[Proposed] RSD-07; RET-G01/08')
    s.end_frame(f)
    s.note('Keep the selected ID and business context; qualify the list-to-detail ID under RET-G01. Metadata alone is not a complete view. Retrieve includeAttachments defaults to true. With false, descriptors and URL/Factur-X generation are omitted, but availableAttachments is retained. A positive count does not itself return file choices or links.', 'INT-RCV03, snapshot 13 November; RET-API-01/02')
    f = s.start_frame('opt | Download file — one attachment')
    request = s.call(0, 1, 'Download file; get file choices first if omitted', '[Proposed] SPEC026 §2')
    links = s.start_frame('opt | Attachment choices/links omitted, or link expiry confirmed')
    s.exchange(1, 2, 'GET /datasets/{datasetId}/e-invoices/{e-invoiceId}?includeAttachments=true',
        'Attachment count, file choices and current download URLs',
        '[Existing] INT-RCV03; RET-API-02')
    s.end_frame(links)
    s.exchange(1, 3, 'GET {downloadUrl} for the selected saved file',
        'Labelled bytes, or an access/file problem',
        '[Spain] Reuse INT-RCV01 §4; RET-G04/05',
        response_source='[Proposed] RSD-07; RET-API-03')
    s.reply(request, 'Selected file, or denial/file problem with a safe next action',
        '[Proposed] RSD-07; RET-G04/05/10')
    s.end_frame(f)
    s.note('Apply file access, role, safety and integrity checks. A zero attachment count is distinct from omitted descriptors. Qualify readable content and SPFE inbound freshness. Safe saved access can continue during source outage or pending inbound ERP delivery, including an authorised faithful copy. Viewing/download does not create buyer acceptance.', 'REF-SCOPE/COPY-POLICY; RET-G04/05/08/10')
    return s

if __name__ == '__main__':
    for path in build():
        print(path.relative_to(ROOT))
