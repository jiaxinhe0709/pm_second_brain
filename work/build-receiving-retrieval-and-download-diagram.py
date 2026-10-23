"""Build only the combined SPEC-SEI-016 intake diagram with the existing renderer.

The predecessor specs and diagrams stay unchanged. No external calls are needed.
"""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
definition = importlib.util.spec_from_file_location(
    'receiving_intake_renderer', ROOT / 'work/build-onboarding-scenario-diagrams.py')
diagram = importlib.util.module_from_spec(definition)
definition.loader.exec_module(diagram)
node, edge = diagram.node, diagram.edge
SPEC = '../../specs/archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md'


def build():
    nodes = [
        node('source', 0, 5, 'Source check or file arrival', 'RSD-01 / PRI-01', 'Selected public or private source'),
        node('authority', 0, 2, 'Check source and authority', 'RSD-01/02 / PRI-01', 'Business, caller, route and mode'),
        node('public_query', 1, 5, 'Discover public invoices', 'RSD-03', 'Qualified filters and continuation'),
        node('public_fetch', 2, 5, 'Download public source file', 'RSD-03', 'Qualified locator or ID contract'),
        node('private_file', 2, 2, 'Full file supplied?', 'PRI-02', kind='decision'),
        node('private_fetch', 3, 5, 'Fetch private source file', 'PRI-03', 'Qualified provider file contract'),
        node('private_hold', 3, 4, 'Recover pending file fetch', 'PRI-03/04', 'Same item; safe resume or reconcile', 'recovery'),
        node('capture', 4, 3, 'Verify durable source capture', 'RSD-04', 'Exact bytes, role, context and hash'),
        node('receiving', 5, 2, 'Register durable item outcome', 'RCV-01 / RSD-05', 'Saved state and recovery owner'),
        node('processing', 6, 2, 'Check, map and publish once', 'RCV-02–09', 'One business invoice and delivery'),
        node('progress', 6, 3, 'Commit covered source progress', 'RSD-06 / PRI-04', 'Every covered item accounted for', 'outcome'),
        node('product', 6, 1, 'Deliver to the product', 'RCV-07', 'Stable identity; separate receipt', 'outcome'),
        node('file_read', 5, 3, 'Read the saved source file', 'RSD-07/09', 'Current permission; labelled bytes'),
        node('customer_file', 6, 0, 'Receive the downloaded file', 'RSD-07', 'Separate from product delivery', 'outcome'),
        node('restricted', 5, 4, 'Hold or restrict the file', 'RCV-09 / RSD-07/08', 'Owned case; approved safe access', 'recovery'),
    ]
    positions = {
        'source': (240, 878, 260, 104),
        'authority': (240, 458, 260, 104),
        'public_query': (565, 878, 260, 104),
        'public_fetch': (900, 878, 260, 104),
        'private_file': (900, 458, 260, 104),
        'private_fetch': (1250, 878, 260, 104),
        'private_hold': (1250, 738, 260, 104),
        'capture': (1595, 598, 260, 104),
        'receiving': (1935, 458, 260, 104),
        'processing': (2255, 458, 260, 104),
        'progress': (2255, 598, 260, 104),
        'product': (2255, 318, 260, 104),
        'file_read': (1935, 598, 260, 104),
        'customer_file': (2255, 178, 260, 104),
        'restricted': (1935, 738, 260, 104),
    }
    edges = [
        edge('source', 'authority', points=[(370, 878), (370, 562)]),
        edge('authority', 'public_query', 'conditional',
             points=[(400, 562), (400, 855), (695, 855), (695, 878)],
             label='Public source', label_pos=(450, 843)),
        edge('public_query', 'public_fetch', points=[(825, 930), (900, 930)]),
        edge('public_fetch', 'capture', points=[(1030, 982), (1030, 1007),
             (1725, 1007), (1725, 702)]),
        edge('authority', 'private_file', 'conditional',
             points=[(500, 510), (900, 510)], label='Private source', label_pos=(590, 493)),
        edge('private_file', 'capture', points=[(1160, 510), (1555, 510),
             (1555, 650), (1595, 650)], label='File supplied', label_pos=(1250, 493)),
        edge('private_file', 'private_fetch', 'conditional',
             points=[(1030, 562), (1030, 577), (1200, 577), (1200, 930), (1250, 930)],
             label='Fetch needed', label_pos=(1220, 865)),
        edge('private_fetch', 'capture', points=[(1510, 930), (1550, 930),
             (1550, 674), (1595, 674)]),
        edge('private_fetch', 'private_hold', 'recovery', points=[(1380, 878), (1380, 842)],
             label='Failure / unknown', label_pos=(1400, 865)),
        edge('capture', 'receiving', points=[(1855, 625), (1895, 625), (1895, 510), (1935, 510)]),
        edge('receiving', 'processing', points=[(2195, 510), (2255, 510)]),
        edge('receiving', 'progress', points=[(2065, 562), (2065, 579),
             (2385, 579), (2385, 598)]),
        edge('processing', 'product', 'conditional', points=[(2385, 458), (2385, 422)],
             label='Qualified', label_pos=(2400, 444)),
        edge('capture', 'file_read', 'conditional', points=[(1855, 650), (1935, 650)]),
        edge('file_read', 'customer_file', points=[(2195, 650), (2220, 650),
             (2220, 713), (2600, 713), (2600, 230), (2515, 230)]),
        edge('capture', 'restricted', 'recovery', points=[(1855, 674), (1880, 674),
             (1880, 790), (1935, 790)]),
        edge('file_read', 'restricted', 'recovery', points=[(2065, 702), (2065, 738)],
             label='Unsafe / missing', label_pos=(2080, 729)),
    ]
    diagram.classify(nodes, {
        n['key']: ('Scenario-specific' if n['key'] in ('public_query', 'public_fetch', 'private_file', 'private_fetch')
                   else 'Conditional' if n['key'] in ('private_hold', 'restricted', 'file_read', 'customer_file', 'product')
                   else 'Common') for n in nodes})
    return diagram.build(
        'receiving-retrieval-and-download-intake-process',
        'Receive and retrieve invoices; download the saved source independently',
        'One proposed feature. Qualify the source mode, preserve the actual file, and keep notification, capture, source progress, product receipt and customer download distinct.',
        nodes, edges, spec=SPEC, positions=positions, width=2670, height=1170,
        boundaries=[
            'Missing source authority stops protected calls. A notification or query result cannot prove file capture or complete source coverage.',
            'Covered progress needs durable item outcomes; mapping and product receipt may finish later. Unsafe files retain an approved controlled-access path.',
            'The saved-file read starts with an authorised request and does not refetch externally. Buyer acceptance and payment reporting belong to SPEC-SEI-009.',
        ])


if __name__ == '__main__':
    diagram.render_pngs([build()])
