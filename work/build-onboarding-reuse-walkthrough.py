"""Build five compact SPEC-SEI-021 sequences without regenerating SPEC020 assets."""
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'work' / filename)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


base = module('onboarding_contract_sources', 'build-onboarding-api-diagrams.py')
palette = module('onboarding_reuse_colours', 'recolour-onboarding-sequences.py')
SPEC = '../../specs/onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md'
VIEWS = [
    ('shared-prerequisites', 'Shared prerequisites', 'Reuse current evidence; provision a dataset only if the channel requires it', '21-shared-prerequisites'),
    ('public-readiness', 'Public readiness', 'Phase 1: assess selected functions through qualified checks', '22-public-readiness'),
    ('private-setup', 'Private setup', 'Later phase: new or retained provider; configure only missing Sage setup', '23-private-setup'),
    ('supported-change', 'Supported change', 'Requested extension or enabled transition; Private A to Private B stays disabled', '24-supported-change'),
    ('uncertainty-recovery', 'Uncertainty and recovery', 'Observe the original effect; preserve valid independent functions', '25-uncertainty-and-recovery'),
]


class Sketch:
    def __init__(self, slug, title, subtitle, anchor):
        parties = ['Product', 'E-Invoice API', 'Identity', 'Tax Service', 'Public platform']
        if slug == 'private-setup':
            parties[4] = 'Private provider'
        if slug == 'supported-change':
            parties[2] = 'Routing owner'
        if slug == 'uncertainty-recovery':
            parties[4] = 'Original provider'
        self.s = base.uml.Sequence('onboarding-reuse-' + slug + '-sequence', title,
                                  subtitle, SPEC + '#' + anchor, parties)
        self.slug, self.anchor = slug, anchor
        self.gates, self.effects, self.operations, self.refs = [], [], [], []

    def ref(self, target, label, gate=False):
        self.s.used.update((0, 1))
        f = self.s.start_frame('ref | ' + label)
        self.s.y += 8
        self.s.end_frame(f)
        self.refs.append(target)
        if gate:
            self.gates.append(self.s.y)

    def http(self, ident):
        op = base.OPERATIONS[ident]
        if ident in ('API-03', 'API-05'):
            assert self.gates and self.gates[-1] < self.s.y
            self.effects.append({'label': ident, 'y': self.s.y})
        response = {
            'API-01': '200 OK\nAccess-point IDs and names',
            'API-02': '200 OK\nStatus + connectionId (or null)',
            'API-03': '201 Created\nConnection resource; address status',
            'API-04': '200 OK\nPer-address status and errors',
            'API-05': '200 OK\nUpdated connection/address details',
        }[ident]
        self.s.exchange(0, 1, base.path_label(op['method'], op['path']), response,
                        f'[Existing] {ident} / FR-{ident[-2:]}', f'FR-{ident[-2:]} response')
        self.operations.append({'id': ident, **op})

    def finish(self):
        path = self.s.write([
            'Solid requests; dashed paired responses; grey activation bars. Timing and service placement remain proposed.',
            'Current business access is required. HTTP success is separate from readiness and activation. Unknown evidence holds dependent work.',
        ])
        palette.apply_colours(path)
        pairs = len(self.s.activations)
        assert pairs * 2 == len(self.s.messages)
        return path, {
            'view': self.slug, 'anchor': self.anchor, 'source_id': 'SPEC-SEI-021',
            'svg': str(path.relative_to(ROOT)), 'png': str(path.with_suffix('.png').relative_to(ROOT)),
            'drawio': str(path.with_suffix('.drawio').relative_to(ROOT)),
            'canvas_width': 260 + (len(self.s.used) - 1) * 385,
            'request_response_pairs': pairs, 'activation_bars': pairs,
            'operations': self.operations, 'references': self.refs,
            'pre_dispatch_gates': self.gates, 'conditional_effects': self.effects,
            'status': 'proposal; Spain implementation and logical contracts unqualified',
        }


def build_all():
    paths, views = [], []
    for slug, title, subtitle, anchor in VIEWS:
        p = Sketch(slug, title, subtitle, anchor)
        s = p.s
        if slug == 'shared-prerequisites':
            t = s.call(0, 1, 'Assess selected prerequisites', '[To qualify] Logical request; ONB-02/03')
            s.exchange(1, 2, 'Check business NIF\nand action authority',
                       'Current evidence / owned action', '[To qualify] Identity contract')
            f = s.start_frame('opt | Certificate required for this purpose; reuse valid evidence')
            s.exchange(1, 3, 'Check certificate is in date\nand suitable for this purpose',
                       'Readiness + protected reference\nor reason / unconfirmed', '[To qualify] Tax Service; CERT-05')
            s.end_frame(f)
            s.reply(t, 'Gate passed / hold + owner', '[Logical outcome] ONB-02/03/08')
            f = s.start_frame('opt | Gate passed; new dataset required; Spain provisioning and create/confirm semantics qualified')
            s.exchange(0, 1, 'POST /datasets', '202 Accepted\nNo response body',
                       '[Existing guide] INT-DS01; X-Idempotency-Key', 'INT-DS01; provisioning started')
            s.exchange(0, 1, 'POST /datasets', '200 OK\ntenantId used as datasetId',
                       '[Existing guide] Same input + same key', 'INT-DS01; successful confirmation path')
            s.end_frame(f)
        elif slug == 'public-readiness':
            p.ref('21-shared-prerequisites', 'Shared prerequisites (2.1); only missing/stale work; pass before dependent checks', gate=True)
            f = s.start_frame('opt | A supported service choice is needed')
            p.http('API-01')
            s.end_frame(f)
            f = s.start_frame('opt | Known authorised dataset; inspect existing Sage setup when needed')
            p.http('API-02')
            g = s.start_frame('opt | Known connection needs detail')
            p.http('API-04')
            s.end_frame(g)
            s.end_frame(f)
            t = s.call(0, 1, 'Assess selected public functions', '[To qualify] Logical request; ONB-03/04')
            f = s.start_frame('opt | Missing/stale check; qualified purpose-specific public contract and authority')
            s.exchange(1, 4, 'Check selected public access', 'Public evidence / limitation', '[To qualify] Selected public contract')
            s.end_frame(f)
            s.reply(t, 'Per-function findings + actions', '[Logical outcome] ONB-04/11')
        elif slug == 'private-setup':
            p.ref('21-shared-prerequisites', 'Shared prerequisites (2.1); qualified dataset; pass selected-purpose checks', gate=True)
            p.http('API-02')
            f = s.start_frame('opt | Missing Sage setup; later-phase provider, route-authority and continuity gates passed')
            p.gates.append(f[0])
            p.http('API-03')
            s.exchange(1, 4, 'Establish selected account binding', 'Provider evidence / pending / error',
                       '[To qualify] Provider contract / timing')
            s.end_frame(f)
            p.http('API-04')
            s.exchange(0, 1, 'Assess current private findings', 'Per-function findings;\nactivation assessed separately',
                       '[To qualify] Logical request; ONB-06/11', '[Logical outcome] ONB-06/11')
        elif slug == 'supported-change':
            p.ref('21-shared-prerequisites', 'Shared prerequisites (2.1); refresh only affected evidence', gate=True)
            t = s.call(0, 1, 'Assess requested change', '[To qualify] Logical request; ONB-05/07')
            g = s.start_frame('opt | Change can affect routing or earlier-invoice access')
            s.exchange(1, 2, 'Qualify plan and continuity', 'Supported scope / hold + owner',
                       '[To qualify] Route authority / earlier invoices')
            s.end_frame(g)
            s.reply(t, 'Permitted plan / owned hold', '[Logical outcome] ONB-07/09')
            f = s.start_frame('opt | Permitted extension or enabled transition; unchanged setup skips; Private A to Private B disabled')
            p.gates.append(f[0])
            p.ref('23-private-setup', 'Private setup (2.3) only if the permitted plan needs missing target setup', gate=True)
            g = s.start_frame('opt | Existing connection needs a supported requested update')
            p.http('API-05')
            s.end_frame(g)
            g = s.start_frame('opt | Routing change required and enabled; original-effect observation qualified')
            s.exchange(1, 2, 'Apply / observe approved transition', 'Boundary + prior-access evidence\nor outcome unknown',
                       '[To qualify] Routing contract / effects')
            s.end_frame(g)
            s.end_frame(f)
            s.exchange(0, 1, 'Assess changed-function findings', 'Confirmed boundary / owned hold',
                       '[To qualify] Logical request; ONB-11', '[Logical outcome] ONB-07/09/11')
        else:
            p.ref('21-shared-prerequisites', 'Shared checks (2.1) for observation access only; skip provisioning and all mutations', gate=True)
            f = s.start_frame('opt | Known connection; qualified safe detail read can add evidence')
            p.http('API-04')
            s.end_frame(f)
            t = s.call(0, 1, 'Assess original uncertain work', '[To qualify] Logical request; ONB-08')
            f = s.start_frame('opt | Original provider/operation and authoritative observation contract qualified')
            s.exchange(1, 4, 'Observe original operation', 'Confirmed / absent / conflicting\nor still unknown',
                       '[To qualify] Original-effect observation')
            s.end_frame(f)
            s.reply(t, 'Finding + safe next action owner', '[Logical outcome] ONB-08/11')
        path, item = p.finish()
        paths.append(path)
        views.append(item)
    return paths, views


if __name__ == '__main__':
    paths, views = build_all()
    base.render(paths)
    destination = ROOT / 'work/onboarding-sequence-review'
    destination.mkdir(exist_ok=True)
    (destination / 'sequences.json').write_text(json.dumps({'views': views, 'live_publication': False}, indent=2) + '\n')
