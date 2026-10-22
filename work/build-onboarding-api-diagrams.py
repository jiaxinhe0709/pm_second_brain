"""Build the eight SPEC-SEI-020 sequences in conventional UML notation.

Exact documented HTTP requests and responses stay separate from unbound logical
handoffs. SVG, native editable Draw.io and PNG share one scene. No network calls.
"""
from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'work' / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


uml = module('onboarding_uml', 'onboarding-sequence-renderer.py')
render = module('onboarding_render', 'build-spain-sequence-diagrams.py').render
SPEC = '../../specs/archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md'
PARTIES = ['Product', 'E-Invoice API', 'Identity', 'Tax Service', 'Spain platform']
SCENARIOS = [
    ('01', 'new-setup', 'No established setup', 'Select the public or private path; public readiness is Phase 1'),
    ('02', 'existing-public', 'Existing public service', 'Confirm public access through Sage; reuse current evidence'),
    ('03', 'retained-private', 'Existing private provider retained', 'Keep the provider/account; establish only missing Sage setup'),
    ('04', 'combined', 'Public and private together', 'Return independent findings; respect cross-function dependencies'),
    ('05', 'existing-sage', 'Existing Sage setup', 'Confirm unchanged setup or make only the requested change'),
    ('06', 'platform-change', 'Supported platform change', 'Enabled transitions only; Private A to Private B remains disabled'),
    ('07', 'existing-b2g', 'Existing B2G use', 'Assess B2B independently and keep the B2G service intact'),
    ('08', 'unsupported-unknown', 'Unsupported or unknown setup', 'Return the limitation, available evidence and next action owner'),
]
FILES = {
    'API-01': 'get-accesspoints.md', 'API-02': 'get-dataset-accesspoints.md',
    'API-03': 'new-accesspoint-connection.md', 'API-04': 'get-accesspoint-connection.md',
    'API-05': 'put-accesspoint-connection.md',
}
OPERATIONS = {}
for ident, filename in FILES.items():
    text = (ROOT / 'context/FR API/Onboarding' / filename).read_text()
    doc = json.loads(re.search(r'```json\s*(.*?)\s*```', text, re.S)[1])
    for path, methods in doc['paths'].items():
        for method, operation in methods.items():
            if method in ('get', 'post', 'put'):
                code = next(code for code in operation['responses'] if code.startswith('2'))
                OPERATIONS[ident] = dict(method=method.upper(), path=path, code=code,
                                         operation_id=operation['operationId'])


def path_label(method, path):
    """Keep the complete contract path; wrap only after its slashes."""
    lines, current = [], method + ' '
    segments = path.split('/')
    for i, segment in enumerate(segments):
        token = segment + ('/' if i < len(segments) - 1 else '')
        if len(current + token) > 40:
            lines.append(current)
            current = ''
        current += token
    if current:
        lines.append(current)
    return '\n'.join(lines)


class Proposal:
    def __init__(self, number, slug, title, subtitle):
        self.number, self.anchor = number, f'onb-s{number}-{slug}'
        parties = list(PARTIES)
        parties[4] = {'02': 'Public platform', '03': 'Private provider', '06': 'Private provider',
                      '07': 'B2B platform', '08': 'Original provider'}.get(number, 'Spain platform')
        self.s = uml.Sequence(f'onboarding-api-s{number}-{slug}-sequence',
            f'ONB-S{number} - {title}', subtitle, SPEC + '#' + self.anchor, parties)
        self.operations, self.gates, self.effects = [], [], []

    def http(self, ident):
        op = OPERATIONS[ident]
        if ident in ('API-03', 'API-05'):
            assert self.gates and self.gates[-1] < self.s.y
            self.effects.append(dict(label=ident, y=self.s.y))
        responses = {
            'API-01': '200 OK\nAccess-point IDs and names',
            'API-02': '200 OK\nStatus + connectionId (or null)',
            'API-03': '201 Created\nConnection resource; address status',
            'API-04': '200 OK\nPer-address status and errors',
            'API-05': '200 OK\nUpdated connection/address details',
        }
        self.s.exchange(0, 1, path_label(op['method'], op['path']), responses[ident],
            f'[Existing] {ident} / FR-{ident[-2:]}', f'FR-{ident[-2:]} response')
        self.operations.append(dict(id=ident, **op))

    def inspect(self):
        f = self.s.start_frame('opt | Known authorised dataset; inspect Sage setup only')
        self.http('API-02')
        g = self.s.start_frame('opt | A known connection needs detail')
        self.http('API-04')
        self.s.end_frame(g)
        self.s.end_frame(f)

    def prerequisites(self):
        t = self.s.call(0, 1, 'Assess prerequisites', '[To qualify] Logical request; ONB-02/03')
        self.s.exchange(1, 2, 'Check business NIF\nand action authority',
            'NIF + authority evidence\nor an owned action', '[To qualify] Identity contract')
        f = self.s.start_frame('opt | Certificate required for the selected purpose; use current evidence')
        self.s.exchange(1, 3, 'Check certificate is in date\nand suitable for this purpose',
            'Readiness + protected reference\nor reason / unconfirmed',
            '[To qualify] Tax Service; CERT-05')
        self.s.end_frame(f)
        self.s.reply(t, 'Gate decision + action owner', '[Logical outcome] ONB-02/03/08')
        self.gate('Continue dependent checks only after valid NIF, current action authority and required certificate readiness pass.',
                  'ONB-02/03/08 | Unconfirmed evidence holds only dependent work')

    def gate(self, label, source):
        self.gates.append(self.s.y)
        self.s.note(label, source)

    def public(self):
        t = self.s.call(0, 1, 'Assess selected public functions', '[To qualify] Logical request; ONB-03/04')
        self.s.exchange(1, 4, 'Check purpose-specific access',
            'Public evidence / limitation', '[To qualify] Selected public contract')
        self.s.reply(t, 'Per-function public findings\n+ required actions', '[Logical outcome] ONB-04/11')

    def provider(self, label='Apply retained-provider binding', response='Provider evidence / pending / error'):
        self.s.exchange(1, 4, label, response, '[To qualify] Provider contract / timing')

    def findings(self, label):
        self.s.exchange(0, 1, 'Assess current findings', label,
                        '[To qualify] Logical request; ONB-11', '[Logical outcome] ONB-11')

    def change(self):
        f = self.s.start_frame('opt | Missing authorised setup only; qualified connect effects')
        self.http('API-03')
        self.s.end_frame(f)
        f = self.s.start_frame('opt | Existing connection needs a supported requested update')
        self.http('API-05')
        self.s.end_frame(f)

    def finish(self):
        path = self.s.write([
            'Requests: solid / filled arrow. Responses: dashed / open arrow. Grey bars: handling intervals; timing is not to scale.',
            'Precondition: authorised business/dataset access and correct environment. Spain builds and logical contracts remain to be qualified.',
            'HTTP success is not readiness or activation. Failed / uncertain evidence returns an owned hold; observe original effects under ONB-08.',
        ])
        requests = [m for m in self.s.messages if m['kind'] == 'call']
        replies = [m for m in self.s.messages if m['kind'] == 'reply']
        assert len(requests) == len(replies) == len(self.s.activations)
        return path, {
            'scenario': f'ONB-S{self.number}', 'anchor': self.anchor,
            'svg': str(path.relative_to(ROOT)), 'drawio': str(path.with_suffix('.drawio').relative_to(ROOT)),
            'png': str(path.with_suffix('.png').relative_to(ROOT)),
            'interactions': len(self.s.messages), 'request_response_pairs': len(requests),
            'activation_bars': len(self.s.activations), 'operations': self.operations,
            'pre_dispatch_gates': self.gates, 'conditional_effects': self.effects,
            'canvas_width': 260 + (len(self.s.used) - 1) * 385,
            'notation': 'UML request/response with activation bars; logical handoffs explicitly unbound',
            'status': 'proposal; Spain contracts/build coverage unqualified',
        }


def build_all():
    paths, manifest = [], []
    for number, slug, title, subtitle in SCENARIOS:
        p = Proposal(number, slug, title, subtitle)
        s = p.s
        if number == '01':
            p.http('API-01')
            p.prerequisites()
            f = s.start_frame('opt | New dataset required by this channel; Spain provisioning and create/confirm contract qualified')
            s.exchange(0, 1, 'POST /datasets', '202 Accepted\nNo response body',
                       '[Existing guide] INT-DS01', 'INT-DS01; provisioning started')
            s.exchange(0, 1, 'POST /datasets', '200 OK\ntenantId used as datasetId',
                       '[Existing guide] Same input + X-Idempotency-Key', 'INT-DS01; completion path only')
            s.end_frame(f)
            f = s.start_frame('opt | Selected public path; Phase 1')
            p.public()
            s.end_frame(f)
            p.gate('Private work requires later-phase qualification and authority, route-impact and continuity evidence before connect.',
                   'ONB-05/07 | New dataset does not establish public enrolment')
            f = s.start_frame('opt | Selected private path; only missing setup; all route gates passed')
            p.http('API-03')
            p.provider('Apply private-provider binding')
            p.http('API-04')
            s.end_frame(f)
        elif number == '02':
            p.inspect()
            p.prerequisites()
            p.public()
            s.note('An existing public account does not establish Sage access. No external enrolment or test invoice is inferred.', 'ONB-S02 | GAP-01/02/06')
        elif number == '03':
            p.inspect()
            p.prerequisites()
            p.gate('Keep the provider/account. Qualify connect effects, route authority and continuity before dispatch.', 'ONB-05/06/07 | INT-AP04: connect can take over routing')
            f = s.start_frame('opt | Missing Sage setup only; retained account and provider effects qualified')
            p.http('API-03')
            p.provider()
            s.end_frame(f)
            p.http('API-04')
            p.findings('Private findings;\nactivation assessed separately')
        elif number == '04':
            p.inspect()
            p.prerequisites()
            p.public()
            p.gate('Assess private work independently. Require later-phase, provider, authority and continuity gates before route changes.', 'ONB-S04 | Public readiness does not activate private receiving')
            p.change()
            p.provider('Observe private-provider progress')
            p.http('API-04')
            p.findings('Independent public/private findings\n+ actions; activation separate')
        elif number == '05':
            p.inspect()
            f = s.start_frame('opt | Affected evidence is stale or a requested change needs new prerequisite checks')
            p.prerequisites()
            s.end_frame(f)
            p.gate('Valid unchanged setup skips mutation. A requested update needs current authority and qualified route/version effects.', 'ONB-A15/38 | Failed lookup is not missing setup')
            f = s.start_frame('opt | Requested extension/correction only; update semantics qualified')
            p.http('API-05')
            p.http('API-04')
            s.end_frame(f)
            p.findings('Unchanged setup / affected findings\n+ action owner')
        elif number == '06':
            p.inspect()
            p.prerequisites()
            p.gate('Require a supported, enabled transition and continuity evidence. Private A to Private B stays disabled.', 'ONB-07/09 | Unsupported or unconfirmed transition returns an owned hold')
            f = s.start_frame('opt | Enabled transition; actual setup effects and effective boundary qualified')
            p.change()
            p.provider('Confirm change + prior access', 'Effective-boundary evidence\nor limitation / uncertainty')
            p.http('API-04')
            s.end_frame(f)
            p.findings('Confirmed boundary / owned hold')
        elif number == '07':
            p.http('API-01')
            p.inspect()
            p.prerequisites()
            p.public()
            s.note('Keep B2G intact. Missing B2B setup follows S01/S03 within its own phase and route gates; B2G credentials do not prove B2B fitness.', 'ONB-S07 | No B2G update or disconnection in this sequence')
        else:
            p.http('API-01')
            p.inspect()
            s.note('Classify the unsupported function, missing evidence or dependency; assign the next action owner. A failed/empty read does not prove absence.', 'ONB-S08 | ONB-08/10 | No forced switch or blind replay')
            f = s.start_frame('opt | Earlier external effect possible; original provider/operation and safe observation are qualified')
            p.provider('Observe original operation', 'Original-effect evidence\nor unresolved / conflicting')
            s.end_frame(f)
            p.findings('Limitation / uncertainty\n+ next action owner')
        path, item = p.finish()
        paths.append(path)
        manifest.append(item)
    return paths, manifest


if __name__ == '__main__':
    paths, manifest = build_all()
    render(paths)
    destination = ROOT / 'work/onboarding-api-review/scenario-sequences.json'
    destination.write_text(json.dumps({'scenarios': manifest, 'live_publication': False}, indent=2) + '\n')
