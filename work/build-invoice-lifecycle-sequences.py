"""Build local lifecycle sequence assets using the repository's editable renderer."""
from pathlib import Path
import importlib.util
import math
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('lifecycle_sequence_renderer', ROOT / 'work/onboarding-sequence-renderer.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
SOURCE = '../../specs/invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md'


def build():
    sequences = []
    s = renderer.Sequence('invoice-lifecycle-fr-update-sequence',
        'French lifecycle request, completion and history',
        'Guide-evidenced product calls; selected build and Spain coverage remain unqualified',
        SOURCE + '#21-french-request-notification-and-history-read',
        ['ERP / product', 'E-Invoice API', 'Notifications'])
    s.note('Precondition: connected dataset, existing invoice at the selected access point, correct environment and current represented-business/action authority. Country-specific commands still need qualification.', 'INT-LCS01/02; LCS-R04/13; LIF-G01/04')
    s.exchange(0, 2, 'POST /internal/events/subscriptions',
        '201: subscription for scoped statusupdated events', '[Guide] INT-LCS02 section 1')
    s.exchange(0, 1, 'POST /datasets/{datasetId}/\ne-invoices/{e-invoiceId}/status',
        '201 Created: operation data.id and echoed status attributes', '[Guide] INT-LCS01 section 1')
    s.note('POST statusCode is a UUID. The request uses e-InvoiceStatus and the matching statusAttributes shape. Preserve the required Idempotency-Key; its scope/retention/replay semantics need qualification.', 'INT-LCS01; LIF-G04/06')
    s.exchange(2, 0, 'statusupdated notification; subject = invoice ID',
        'Webhook receipt; authentication and receipt response to qualify', '[Guide] INT-LCS02 section 2', '[To qualify] LIF-G05')
    s.note('Finished processing can mean ERROR. Notification data.id is a workflow-status UUID, not proven operation correlation. Do not assume delivery order or successful business/reporting completion.', 'INT-LCS02/05; LIF-G05')
    s.exchange(0, 1, 'GET /datasets/{datasetId}/\ne-invoices/{e-invoiceId}',
        'Read currentStatus and correlated history outcome/error', '[Guide] INT-LCS02 section 3; INT-ERR01')
    s.note('Missed notification: recover saved history under the qualified read strategy. External evidence not yet captured needs a separate source consultation. Full history schema and correlation remain open.', 'LCS-A10/15/26; LIF-G02/05/06')
    sequences.append(s)

    s = renderer.Sequence('invoice-lifecycle-spain-reporting-sequence',
        'Spain event and independent destination reports',
        'Proposed responsibility sequence; public SOAP transport is evidenced, country payloads remain gated',
        SOURCE + '#22-spain-business-event-and-independent-public-reporting',
        ['ERP / product', 'Lifecycle / country rules', 'Public connector', 'AEAT SPFE', 'Private platform'])
    s.exchange(0, 1, 'Submit an authorised Spain business event',
        'Saved fact and separately tracked reporting obligations', '[Proposed] LCS-02-08; existing POST only if qualified')
    s.note('Select event, actor, fields, legal applicability, historical channel and each reporting owner. The lifecycle/country lane is a logical responsibility, not a new deployment. Missing evidence holds the affected report.', 'LCS-R04-06/10/12/13; LIF-G04/07/08')
    f = s.start_frame('opt | Public reporting applies and the selected contract is qualified')
    call = s.call(1, 2, 'Execute one saved public obligation', '[Proposed] LCS-09; LIF-G04/06')
    s.exchange(2, 3, 'CustomerInvoiceEvents OR SupplierInvoiceEvents',
        'Raw transport and business/item result at its actual evidence level', '[PRE transport] SPFE-S11/S17; [To qualify] business schema')
    s.reply(call, 'Record this public destination result or outcome unknown', '[Proposed] LCS-09/10; no inferred business fact')
    s.end_frame(f)
    f = s.start_frame('opt | A separate issuer/counterparty report is required')
    s.exchange(1, 4, 'Execute through the selected private contract',
        'Independent result; correlate a provider-owned report', '[To qualify] LCS-Q-PROVIDER; no endpoint supplied')
    s.end_frame(f)
    s.exchange(0, 1, 'Read fact, current dimensions and each report result',
        'Authorised view with evidence age, owner and safe next action', '[Proposed] LCS-06; existing GET coverage to qualify')
    s.note('An earlier success remains complete if another destination fails. Public admission is not new payment/acceptance evidence. Incoming already-reported facts cannot create a reporting loop.', 'LCS-A08/16/17/24; SPFE-S02 Article 8')
    sequences.append(s)

    s = renderer.Sequence('invoice-lifecycle-recovery-sequence',
        'Failed attempt and uncertain cancellation recovery',
        'Keep successful status, attempt results and destination reporting outcomes distinct',
        SOURCE + '#23-failed-transition-and-uncertain-cancellation',
        ['ERP / product', 'E-Invoice API', 'Reporting / operations', 'Original destination'])
    f = s.start_frame('case | A transition is confirmed failed')
    s.exchange(0, 1, 'GET existing invoice and correlated history',
        'Last successful currentStatus; failed history operationStatus = ERROR', '[Guide] INT-LCS02/05; INT-ERR01')
    s.note('Expose the failed attempt and an owned corrective action. Lifecycle Completed (209) differs from operational COMPLETED. A saved business fact remains when only its report fails.', 'LCS-R14; LCS-A26/27')
    s.end_frame(f)
    f = s.start_frame('case | A Spain report cancellation may have reached its destination')
    s.exchange(2, 3, 'Original CANCEL* obligation with saved request identity',
        'No reliable completion result; external outcome remains unknown', '[Proposed] LCS-09/10; SPFE-S03; LIF-G04/06')
    s.note('Hold replacement reporting. A local processing ERROR does not prove external non-execution. Keep the original route, payload, operation identity and all evidence.', 'LCS-SPFE-R03; LCS-A08/09/12; LIF-G06/07')
    s.exchange(2, 3, 'Reconcile original operation under qualified read/support contract',
        'Proven result, or owned manual case if lookup is unavailable', '[To qualify] LIF-G06; no reconciliation endpoint supplied')
    s.end_frame(f)
    s.note('Resume only when the selected contract and observed result permit it. Never issue a new key, send replacement first, withdraw the invoice or switch destination to hide an uncertain cancellation.', 'LCS-SPFE-A03; LIF-API-A05/06/07')
    sequences.append(s)

    return [s.write([
        'Solid arrows: requests or deliveries. Dashed arrows: paired results. Grey bars show handling, not elapsed time.',
        'Guide/PRE transport: supplied evidence. Proposed/To qualify: design or missing contract, not deployed coverage.',
    ]) for s in sequences]


if __name__ == '__main__':
    import pymupdf
    for path in build():
        svg = ET.parse(path).getroot()
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
