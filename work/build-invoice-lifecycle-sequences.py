"""Build short lifecycle sequences with the onboarding grey/blue notation."""
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

SPEC = '../../specs/invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md'
def build():
    sequences = []
    s = renderer.Sequence('invoice-lifecycle-fr-update-sequence',
        'Change invoice status: request and read the result',
        'Existing E-Invoice API; Spain actions and fields need confirmation',
        SPEC + '#21-existing-request-notification-and-history-read',
        ['ERP / product', 'E-Invoice API', 'Events'])
    s.note('Start with an existing invoice, dataset/platform binding and current business/action permission. Use the selected action UUID and fields.', 'LCS-R04/13; LIF-G01/04')
    s.exchange(0, 2, 'POST /internal/events/subscriptions',
        'Subscription for scoped statusupdated events', '[Existing] INT-LCS02 §1')
    s.exchange(0, 1, 'POST /datasets/{datasetId}/\ne-invoices/{e-invoiceId}/status',
        '201 Created: save operation data.id', '[Existing] INT-LCS01 §1')
    s.exchange(2, 0, 'Status-updated event: subject = invoice ID',
        'Event receipt; exact response to confirm', '[Existing] INT-LCS02 §2')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}',
        'Current status and the matching history attempt/error', '[Existing] INT-LCS02 §3; INT-ERR01')
    s.note('A completion event can report failure. Match the original attempt before recovery; a missed event uses saved history. Keep Idempotency-Key semantics and full correlation open.', 'LCS-R14; LIF-G05/06')
    sequences.append(s)

    s = renderer.Sequence('invoice-lifecycle-spain-reporting-sequence',
        'Spain event: save the fact and track each report',
        'Proposed flow; each destination has its own owner and result',
        SPEC + '#22-spain-business-event-and-independent-public-reporting',
        ['ERP / product', 'E-Invoice Service', 'Public platform', 'Private platform'])
    s.exchange(0, 1, 'Submit an authorised decision or payment fact',
        'Saved fact and required reporting work', '[Proposed] Existing POST only if confirmed')
    s.note('Select the actor, required fields, historical route, enabled scope and one sender per destination. Missing evidence holds only the affected action.', 'LCS-R04–06/10/12/13')
    f = s.start_frame('opt | Public reporting is required and its contract is confirmed')
    s.exchange(1, 2, 'CustomerInvoiceEvents OR SupplierInvoiceEvents',
        'This destination result, or outcome unknown', '[Spain] SPFE-S11/S17; body/result to confirm')
    s.end_frame(f)
    f = s.start_frame('opt | A separate private/counterparty report applies')
    s.exchange(1, 3, 'Report through the selected provider contract',
        'Independent result; identify any provider-owned report', '[Proposed] LCS-Q-PROVIDER; no endpoint supplied')
    s.end_frame(f)
    s.exchange(0, 1, 'Read invoice facts and each report result',
        'Saved view, pending work and who must act', '[Proposed] Existing GET coverage to confirm')
    s.note('Keep a known success when another destination fails. Incoming already-reported facts must not create another report. Public receipt cannot create a payment fact.', 'LCS-A08/16/17/24')
    sequences.append(s)

    s = renderer.Sequence('invoice-lifecycle-recovery-sequence',
        'Keep successful status; resolve uncertain cancellation',
        'A failed local attempt and an unknown external report are different results',
        SPEC + '#23-failed-transition-and-uncertain-cancellation',
        ['ERP / product', 'E-Invoice API', 'Reporting / operations', 'Original destination'])
    f = s.start_frame('case | Status transition is confirmed failed')
    s.exchange(0, 1, 'GET invoice and matching history',
        'Last successful status; failed attempt operationStatus = ERROR', '[Existing] INT-LCS02/05; INT-ERR01')
    s.end_frame(f)
    f = s.start_frame('case | Cancellation may have reached its destination')
    s.exchange(2, 3, 'Original CANCEL* report',
        'No reliable result: preserve outcome unknown', '[Spain proposal] LCS-09/10')
    s.exchange(2, 3, 'Check the original result through confirmed read/support',
        'Proved result, or an owned manual case', '[Proposed] LIF-G06; no lookup endpoint supplied')
    s.end_frame(f)
    s.note('Hold replacement until cancellation is resolved. Keep the original route, request and evidence. Never hide uncertainty with a new key or destination. Lifecycle Completed (209) differs from operational COMPLETED.', 'LCS-R14; LCS-A26/27; LCS-SPFE-A03')
    sequences.append(s)
    return [finish(s) for s in sequences]

if __name__ == '__main__':
    for path in build():
        print(path.relative_to(ROOT))
