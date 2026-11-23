"""Build a separate combined diagram; preserve SPEC025 and its original assets."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-retrieval-combined-workflow'
SUMMARY = '../../specs/invoice-receiving/SPEC-SEI-025-invoice-retrieval-solution-summary.md#'
LOGICAL = '../../specs/invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#'
LIFECYCLE = '../../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#review-and-take-action'
PURPLE, GREEN, GREY = '#F0EBFA', '#E6F4F1', '#FAFAFA'
DESCRIPTION = (
    'A separate combined-layout diagram for review. Shared steps check receiving setup, '
    'collect available files and save/check their recipient, safety and roles. '
    'Automatic ERP receiving and customer access then continue independently. '
    'ERP intake requires an available original that passes the required checks. '
    'A missing original starts recovery through an authorised source, account/access '
    'repair, receiving-provider investigation and sender contact if delivery remains '
    'unresolved. Matching R markers return an obtained file to shared intake checks. '
    'When requested, the customer can view the list, open an invoice and choose '
    'download, review of qualified actions or leaving a decision pending. '
    'A safe labelled copy preserves access while original recovery is pending. '
    'Copy-only buyer actions remain open; file roles, business statuses and reporting '
    'results stay separate. A copy is part of normal private exchange, not only a '
    'fallback after retrieval fails. This diagram does not replace the original '
    'diagrams or prove provider support.')


def build_source():
    document = ET.Element('mxfile', host='app.diagrams.net', type='device')
    diagram = ET.SubElement(document, 'diagram', id=BASE.name,
                            name='Invoice retrieval — combined workflow')
    model = ET.SubElement(diagram, 'mxGraphModel', page='1', pageWidth='1800',
                          pageHeight='2450', grid='1', gridSize='10', guides='1',
                          connect='1', arrows='1', tooltips='1')
    root = ET.SubElement(model, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')
    backgrounds, paths, labels = [], [], []

    def vertex(key, value, x, y, width, height, style, link=None, behind=False):
        if link:
            item = ET.Element('object', id=key, label=value, link=link)
            cell = ET.SubElement(item, 'mxCell', vertex='1', parent='1', style=style)
        else:
            item = cell = ET.Element('mxCell', id=key, value=value,
                                     vertex='1', parent='1', style=style)
        ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(width),
                      height=str(height), attrib={'as': 'geometry'})
        (backgrounds if behind else labels).append(item)

    def text(key, value, x, y, width, height, size=18, link=None, align='left'):
        vertex(key, value, x, y, width, height,
               f'text;html=0;whiteSpace=wrap;align={align};spacing=2;'
               f'fontFamily=Arial;fontSize={size};fontColor=#222222;', link)

    def card(key, title, body, x, y, width, height, fill=PURPLE,
             link=None, size=18, title_size=23, dashed=False):
        style = (f'rounded=1;arcSize=10;html=0;fillColor={fill};'
                 'strokeColor=#666666;strokeWidth=1.5;')
        if dashed:
            style += 'dashed=1;dashPattern=6 4;'
        vertex(key, '', x, y, width, height, style, link, behind=True)
        text(key+'-title', title, x+22, y+12, width-44, 36, title_size, link)
        text(key+'-body', body, x+22, y+54, width-44, height-68, size, link)

    def edge(key, source, target, start=(.5, 1), end=(.5, 0),
             points=(), dashed=False):
        style = (f'edgeStyle=none;html=0;endArrow=block;strokeColor=#555555;'
                 f'strokeWidth=1.6;exitX={start[0]};exitY={start[1]};'
                 f'entryX={end[0]};entryY={end[1]};'
                 'exitPerimeter=0;entryPerimeter=0;')
        if dashed:
            style += 'dashed=1;dashPattern=6 4;'
        cell = ET.Element('mxCell', id=key, parent='1', edge='1',
                          source=source, target=target, style=style)
        geom = ET.SubElement(cell, 'mxGeometry', relative='1', attrib={'as': 'geometry'})
        waypoints = ET.SubElement(geom, 'Array', attrib={'as': 'points'})
        for x, y in points:
            ET.SubElement(waypoints, 'mxPoint', x=str(x), y=str(y))
        paths.append(cell)

    def band(key, title, x, width, link):
        vertex(key, title, x, 850, width, 42,
               'rounded=1;arcSize=8;html=0;whiteSpace=wrap;align=center;'
               'spacing=4;fontSize=20;fillColor=#eeeeee;strokeColor=none;', link, True)

    text('title', 'Invoice retrieval: one shared start, two connected journeys',
         40, 25, 1720, 50, 30)
    text('subtitle', 'Diagram proposal · Automatic receiving and customer access share saved invoice information.',
         40, 85, 1720, 45, 19)
    for key, x, fill, title in [
        ('receiving', 40, PURPLE, 'Receiving and checks'),
        ('customer', 480, GREEN, 'Customer actions / ERP'),
        ('notes', 1000, GREY, 'Context / explanation'),
    ]:
        vertex('colour-'+key, '', x, 150, 18, 18,
               f'rounded=0;fillColor={fill};strokeColor=#999999;', behind=True)
        text('colour-'+key+'-label', title, x+28, 145, 400, 30, 17)
    text('legend', 'Solid: receiving steps. Dashed: saved information, selected choices or recovery. R: obtained file returns to step 3.',
         40, 192, 1720, 30, 16)

    card('setup', '1. Check receiving setup',
         'Reuse the business’s platforms; check current permission.\nMissing setup or access: show the next action and owner.',
         600, 250, 600, 120, link=LOGICAL+'retrieval-setup-context')
    card('collect', '2. Collect available files',
         'Original through SPFE or the recipient’s private platform.\nSPFE faithful copy where enabled and authorised.\nPublic and private sources can both apply.',
         600, 420, 600, 140, link=SUMMARY+'retrieval-use-cases')
    card('save', '3. Save and identify the invoice',
         'Keep the file unchanged; check recipient and safety.\nLabel original / faithful copy.\nVerify the relationship before linking files.',
         600, 610, 600, 140, link=LOGICAL+'31-source-acquisition-and-stored-file-access')
    card('spfe-original-context', 'Originals can come from SPFE',
         'Public issuance and private-platform interconnection\ncan supply the original. No additional faithful copy\nis required for those exchanges. Confirm the route.',
         40, 420, 470, 160, GREY, SUMMARY+'retrieval-use-cases', 16, 21)
    edge('setup-to-collect', 'setup', 'collect')
    edge('collect-to-save', 'collect', 'save')

    band('receiving-band', 'AUTOMATIC ERP RECEIVING', 100, 700,
         SUMMARY+'copy-only-access-and-actions')
    band('customer-band', 'CUSTOMER ACCESS — WHEN REQUESTED', 960, 780,
         LOGICAL+'customer-list-open-and-download')
    edge('saved-to-receiving', 'save', 'receiving-band', start=(.25, 1),
         points=[(750, 800), (450, 800)])
    edge('saved-to-customer', 'save', 'customer-band', start=(.75, 1),
         points=[(1050, 800), (1350, 800)], dashed=True)

    vertex('original-gate', 'Original\navailable?', 290, 940, 320, 140,
           f'rhombus;html=0;whiteSpace=wrap;align=center;spacing=8;fontSize=22;'
           f'fillColor={PURPLE};strokeColor=#666666;strokeWidth=1.5;',
           SUMMARY+'copy-only-access-and-actions', True)
    edge('receiving-to-original', 'receiving-band', 'original-gate')
    card('check-original', '4. Check the original',
         'Check the format and invoice rules.\nPrepare the invoice for ERP intake.',
         170, 1150, 560, 120, link=LOGICAL+'32-receiving-handoff')
    card('deliver', '5. Deliver once to the ERP',
         'Preserve the invoice identity.\nConfirm ERP receipt before claiming success.',
         170, 1320, 560, 120, link=LOGICAL+'32-receiving-handoff')
    card('result', '6. Show result and next action',
         'Show the receiving result and next owner.\nERP receipt does not mean buyer acceptance.',
         170, 1490, 560, 120, GREEN, LOGICAL+'32-receiving-handoff')
    edge('original-ready', 'original-gate', 'check-original')
    text('original-yes-label', 'Yes', 475, 1092, 90, 30, 17)
    edge('original-checked', 'check-original', 'deliver')
    edge('erp-result', 'deliver', 'result')

    text('recovery-label', 'IF THE ORIGINAL IS MISSING', 170, 1652, 560, 30, 18)
    card('recover', 'Recover the original',
         'Show the reason, attempted source, next action and owner.\n'
         'Use authorised SPFE or recipient-platform access.\n'
         'Restore setup/access; the receiving provider checks delivery.\n'
         'If unresolved, ask the sender for the destination or existing original.\n'
         'ERP intake stays pending; safe copy access continues.',
         170, 1700, 560, 230, link=SUMMARY+'retrieval-readiness-and-sender-contact',
         size=16, dashed=True)
    edge('original-missing', 'original-gate', 'recover', start=(0, .5), end=(0, .5),
         points=[(90, 1010), (90, 1815)], dashed=True)
    text('original-no-label', 'No original', 105, 1040, 160, 30, 17)
    for key, x, y in [('returned-file', 430, 1980), ('returned-intake', 520, 660)]:
        vertex(key, 'R', x, y, 40, 40,
               f'ellipse;html=0;align=center;fontSize=20;fillColor={PURPLE};'
               'strokeColor=#666666;spacing=0;',
               LOGICAL+'original-file-retrieval')
    edge('recovered-file', 'recover', 'returned-file', dashed=True)
    edge('return-to-intake', 'returned-intake', 'save', start=(1, .5), end=(0, .5))
    text('recovered-file-label', 'File obtained', 480, 1940, 220, 30, 17)
    text('return-rule', 'R → step 3: repeat checks and match any saved copy.',
         170, 2040, 640, 35, 17, LOGICAL+'original-file-retrieval')

    card('view-list', 'View invoice list',
         'Show sent and received invoices.\nRecheck user access when the list is requested.',
         1050, 940, 600, 120, GREEN, LOGICAL+'customer-list-open-and-download')
    card('open-invoice', 'Select and open invoice',
         'Show details, status, history and labelled files.\nExplain a missing original or unavailable content.',
         1050, 1110, 600, 130, GREEN, LOGICAL+'customer-list-open-and-download')
    vertex('next-action', 'Choose the\nnext action', 1190, 1310, 320, 140,
           f'rhombus;html=0;whiteSpace=wrap;align=center;spacing=8;fontSize=22;'
           f'fillColor={GREEN};strokeColor=#666666;strokeWidth=1.5;',
           LOGICAL+'customer-list-open-and-download', True)
    edge('customer-to-list', 'customer-band', 'view-list')
    edge('list-to-open', 'view-list', 'open-invoice')
    edge('open-to-choice', 'open-invoice', 'next-action')
    for key, title, body, x, link in [
        ('download', 'Download file', 'Choose a labelled file.\nRecheck access and safety.\nReturn file or problem.', 940, LOGICAL+'customer-list-open-and-download'),
        ('review', 'Review and take action', 'Check eligibility.\nCopy-only commands\nneed a policy decision.', 1200, LIFECYCLE),
        ('pending', 'Leave pending', 'Make no decision now.\nKeep pending work\nand deadlines visible.', 1460, LIFECYCLE),
    ]:
        card(key, title, body, x, 1540, 230, 180, GREEN, link, 16, 17)
    edge('download-choice', 'next-action', 'download', points=[(1350, 1490), (1055, 1490)], dashed=True)
    edge('review-choice', 'next-action', 'review', points=[(1350, 1490), (1315, 1490)], dashed=True)
    edge('pending-choice', 'next-action', 'pending', start=(1, .5), points=[(1575, 1380)], dashed=True)
    text('customer-rule', 'Download is optional. Viewing does not accept the invoice.\n'
         'Saved-file access does not wait for original recovery or ERP receipt.',
         1050, 1780, 650, 75, 18, LOGICAL+'customer-list-open-and-download')

    card('why-copy', 'Why retrieve a faithful copy?',
         'The copy is part of normal private exchange, not only a retrieval fallback.\n'
         'Allow safe, authorised view/download while original recovery is pending.\n'
         'Preserve public evidence for later matching; keep original recovery open.',
         40, 2140, 830, 190, GREY, SUMMARY+'why-retrieve-faithful-copy', 17, 23)
    card('status-note', 'One invoice; separate results',
         '“Paid” can coexist with “Original retrieval pending.”\n'
         'The copy has no second business lifecycle. Assess reports separately.\n'
         'Copy-only approval, rejection, posting and payment need decisions.\n'
         'ERP intake waits for the original under product policy.',
         920, 2140, 840, 190, GREY, LOGICAL+'copy-only-engineering-behaviour', 17, 23)
    text('footer', 'Proposed workflow · Colours group activities, not implementation readiness. Detailed controls: SPEC026 and SPEC029.',
         40, 2380, 1720, 40, 16, SUMMARY+'6-material-decisions-and-dependencies')

    root.extend(backgrounds)
    root.extend(paths)
    root.extend(labels)
    ET.indent(document, space='  ')
    BASE.with_suffix('.drawio').write_text(ET.tostring(document, encoding='unicode', xml_declaration=True)+'\n')


def build():
    build_source()
    spec = importlib.util.spec_from_file_location('combined_preview', ROOT/'work/build-invoice-retrieval-overview.py')
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    return renderer.build(BASE, description=DESCRIPTION)


if __name__ == '__main__':
    print(build())
