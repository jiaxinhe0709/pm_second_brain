"""Build the approval and portfolio details for SPEC-SEI-002 locally.

Reuse the existing renderer and visual system. Existing diagrams stay unchanged.
Each description creates an editable Draw.io source, SVG and checked PNG.
"""
from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[1]
definition = importlib.util.spec_from_file_location(
    'onboarding_diagrams', ROOT / 'work/build-onboarding-scenario-diagrams.py')
diagrams = importlib.util.module_from_spec(definition)
definition.loader.exec_module(diagrams)
node, edge = diagrams.node, diagrams.edge
LANES = diagrams.LANES[:5]


def build_all():
    approval_nodes = [
        node('evidence', 0, 3, 'Evidence covers decision?', 'ONB-02', kind='decision'),
        node('request', 1, 2, 'Save scoped approval request', 'ONB-12', 'Requester, purpose and version'),
        node('present', 2, 1, 'Present the client action', 'ONB-12/11', 'Eligible approver; exact scope'),
        node('respond', 3, 0, 'Approve or decline request', 'ONB-12', 'Current eligibility and version'),
        node('verify', 4, 3, 'Verify response and evidence', 'ONB-12/02', 'Approver, scope, official evidence'),
        node('effective', 5, 3, 'Authority effective?', 'ONB-02', kind='decision'),
        node('resume', 6, 2, 'Resume the covered gate', 'ONB-12', 'Recheck plan, authority and trust', 'outcome'),
        node('blocked', 5, 1, 'Keep dependent work blocked', 'ONB-12/11', 'Refusal, expiry or missing evidence', 'conditional'),
        node('result', 6, 1, 'Return result and action owner', 'ONB-11', 'Approval is separate from readiness', 'outcome'),
        node('withdraw', 3, 2, 'Approval or relationship ends', 'ONB-12/02', 'Effective withdrawal or role loss', 'conditional'),
        node('recover', 4, 2, 'Stop use; coordinate recovery', 'ONB-12/08', 'Preserve original evidence', 'recovery'),
    ]
    diagrams.classify(approval_nodes, {
        n['key']: ('Common' if n['key'] in ('evidence', 'effective', 'result')
                   else 'Conditional') for n in approval_nodes})
    approval = diagrams.build(
        'onboarding-client-approval-process',
        'Obtain missing approval; verify authority before resuming',
        'Applies across ONB-S01–08 for a direct customer or delegate. Reuse qualified evidence. A local approval response cannot establish official representation, readiness or activation.',
        approval_nodes, [
            edge('evidence', 'request', 'conditional', label='Missing approval', label_pos=(545, 590)),
            edge('evidence', 'resume', points=[(370, 702), (370, 735), (2310, 735), (2310, 510), (2270, 510)],
                 label='Valid evidence: omit a new request', label_pos=(960, 760)),
            edge('request', 'present', 'conditional'),
            edge('present', 'respond', 'conditional'),
            edge('respond', 'verify', 'conditional'),
            edge('verify', 'effective'),
            edge('effective', 'resume', label='Yes', label_pos=(1990, 632)),
            edge('effective', 'blocked', 'conditional', label='No / undetermined', label_pos=(1858, 450)),
            edge('resume', 'result'),
            edge('blocked', 'result'),
            edge('withdraw', 'recover', 'recovery'),
            edge('recover', 'blocked', 'recovery'),
        ], lanes=LANES[:4], height=890, boundaries=[
            'ONB-12 binds business, delegate, purpose, scope and request/plan version. Identity verifies effective authority separately.',
            'Pending, declined, expired or stale responses keep dependent work at ACTION_REQUIRED. Other permitted functions continue.',
            'Withdrawal stops affected new use. Reconcile uncertain effects under SPEC-SEI-004; retain historical snapshots and client continuity.',
        ])

    portfolio_nodes = [
        node('submit', 0, 0, 'Select clients and functions', 'ONB-13', 'Trusted firm and actor context'),
        node('envelope', 1, 2, 'Valid batch envelope?', 'ONB-13', kind='decision'),
        node('reject', 1, 1, 'Reject envelope safely', 'ONB-13', 'No client items or external work', 'outcome'),
        node('receipt', 2, 2, 'Persist receipt and manifest', 'ONB-13', 'Durable acceptance; not readiness'),
        node('items', 3, 2, 'Create or attach client items', 'ONB-13/01', 'Stable mapping; restart-safe'),
        node('access', 4, 3, 'Check each client permission', 'ONB-02', 'Relationship and scoped authority'),
        node('permitted', 5, 2, 'Item can proceed?', 'ONB-02', kind='decision'),
        node('run', 6, 2, 'Run the existing setup flow', 'ONB-10/03–07', 'Recheck before protected actions'),
        node('blocked', 5, 1, 'Return client action or denial', 'ONB-12/11', 'Hold only the affected item', 'conditional'),
        node('aggregate', 6, 1, 'Return permitted progress', 'ONB-13/11', 'Current access; independent results', 'outcome'),
        node('correct', 4, 0, 'Correct selected client items', 'ONB-13/12', 'Same case; new evidence version', 'conditional'),
        node('cancel', 2, 0, 'Cancel selected pending work', 'ONB-13', 'Recheck each item permission', 'conditional'),
        node('hold', 0, 2, 'Stop selected pending steps', 'ONB-13', 'Keep completed item results', 'conditional'),
        node('recover', 2, 4, 'Resolve assigned uncertainty', 'ONB-08', 'Original operation; no blind retry', 'recovery'),
    ]
    diagrams.classify(portfolio_nodes, {
        n['key']: ('Conditional' if n['key'] in ('correct', 'cancel', 'hold', 'recover', 'blocked')
                   else 'Common') for n in portfolio_nodes})
    portfolio = diagrams.build(
        'onboarding-portfolio-batch-process',
        'Receive a portfolio batch; isolate every client outcome',
        'ONB-13 coordinates independently scoped client items across ONB-S01–08. Batch receipt and coordination states cannot grant authority, readiness or activation.',
        portfolio_nodes, [
            edge('submit', 'envelope'),
            edge('envelope', 'reject', 'conditional', label='Invalid', label_pos=(683, 441)),
            edge('envelope', 'receipt', label='Valid', label_pos=(795, 450)),
            edge('receipt', 'items'),
            edge('items', 'access'),
            edge('access', 'permitted'),
            edge('permitted', 'run', label='Yes', label_pos=(1978, 540)),
            edge('permitted', 'blocked', 'conditional', label='No / action required', label_pos=(1858, 450)),
            edge('run', 'aggregate'),
            edge('blocked', 'aggregate'),
            edge('correct', 'access', 'conditional'),
            edge('cancel', 'hold', 'conditional', points=[(960, 282), (960, 300), (230, 300), (230, 510), (240, 510)]),
            edge('hold', 'aggregate', 'conditional', points=[(370, 562), (370, 730), (2310, 730), (2310, 370), (2270, 370)],
                 label='No uncertain effect', label_pos=(1250, 750)),
            edge('hold', 'recover', 'recovery', points=[(370, 562), (370, 600), (520, 600), (520, 790), (830, 790)],
                 label='Possible external effect', label_pos=(530, 700)),
            edge('recover', 'aggregate', 'recovery', points=[(1090, 790), (2320, 790), (2320, 370), (2270, 370)]),
        ], lanes=LANES, height=1030, boundaries=[
            'Persist the manifest before receipt. Suppress duplicate batch/item effects. Resume decomposition after a restart.',
            'Each client needs current access, authority and evidence. One blocked client cannot fail or disclose another.',
            'Correct or cancel only authorised items. Preserve completed work and invoice origins; hide inaccessible current progress.',
        ])
    return [approval, portfolio]


if __name__ == '__main__':
    diagrams.render_pngs(build_all())
