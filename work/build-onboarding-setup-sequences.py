"""Build self-contained SPEC039 onboarding sequences; preserve predecessor assets."""
from pathlib import Path
import importlib.util
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'work' / filename)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


base = module('onboarding_contract_sources', 'build-onboarding-api-diagrams.py')
palette = module('onboarding_reuse_colours', 'recolour-onboarding-sequences.py')
SPEC = '../../specs/onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md'
VIEWS = [
    ('shared-prerequisites', 'Start onboarding: SXS and credential checks', 'Product integrations with SXS and Tax Connections Service are already available', '21-shared-prerequisites'),
    ('public-readiness', 'Public setup: check Sage access', 'Phase 1: confirm access for the selected business, action and environment', '22-public-readiness'),
    ('private-setup', 'Private setup: reuse or connect an account', 'Later phase: keep the chosen provider; add only missing Sage setup', '23-private-setup'),
    ('supported-change', 'Change setup: keep what already works', 'Add a supported function or make an enabled change; Private A to Private B is disabled', '24-supported-change'),
    ('uncertainty-recovery', 'Setup recovery: check what happened', 'Use after a timeout, conflicting status or an unknown setup result', '25-uncertainty-and-recovery'),
]


def existing_read_frames(path):
    svg=ET.parse(path).getroot()
    native=ET.parse(path.with_suffix('.drawio')).getroot()
    prefixes=('opt | Find a service only', 'opt | Inspect saved access-point setup', 'opt | Read saved connections only',
              'opt | Read detail only', 'opt | Read only a known connection')
    cells=list(native.iter('mxCell'))
    frames=[]
    for cell in cells:
        if cell.get('value','').startswith(prefixes):
            x,y,_,_=palette.geometry(cell)
            frames.append((x-12,y-8))
            palette.set_paint(cell,'fontColor',palette.GREY)
    for cell in cells:
        if cell.find('mxGeometry') is not None:
            x,y,_,h=palette.geometry(cell)
            if (x,y) in frames:
                palette.set_paint(cell,'strokeColor',palette.GREY)
                if h==34: palette.set_paint(cell,'fillColor','#FAFAFA')
    for node in svg:
        kind=node.tag.rsplit('}',1)[-1]
        if kind not in ('text','rect'): continue
        x,y=float(node.get('x',0)),float(node.get('y',0))
        if kind=='text' and (x-12,y-23) in frames: node.set('fill',palette.GREY)
        if kind=='rect' and (x,y) in frames:
            node.set('stroke',palette.GREY)
            if float(node.get('height',0))==34: node.set('fill','#FAFAFA')
    for node in svg:
        if node.text=='Existing FR API / flow': node.text='Existing E-Invoice API / flow'
    for cell in cells:
        if cell.get('value')=='Existing FR API / flow': cell.set('value','Existing E-Invoice API / flow')
    path.write_text(ET.tostring(svg,encoding='unicode'))
    ET.indent(native)
    path.with_suffix('.drawio').write_text(ET.tostring(native,encoding='unicode',xml_declaration=True))


class Sketch:
    def __init__(self, slug, title, subtitle, anchor):
        parties = ['ERP / product\nSetup screen', 'Sage\nE-Invoice API', 'Business identity\nand permission', 'Tax Service\nCertificates', 'Public platform\nSpain (SPFE)']
        if slug == 'shared-prerequisites':
            parties = ['ERP / product\nSetup screen', 'SXS\nDataset / tenant',
                       'Sage\nE-Invoice API', 'Identity\nNIF / permission',
                       'Tax / Connections\nCertificates']
        if slug == 'private-setup':
            parties[4] = 'Private provider\nSelected account'
        if slug == 'supported-change':
            parties[2] = 'Routing owner\nFuture invoice route'
        if slug == 'uncertainty-recovery':
            parties[4] = 'Original provider\nEarlier setup request'
        self.s = base.uml.Sequence('onboarding-setup-' + slug + '-sequence', title,
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
            'API-01': '200 OK\nService names + IDs\nUse service id as accessPointId',
            'API-02': '200 OK\nEntries per access point\nEach status + connectionId (or null)',
            'API-03': '201 Created\nSave data.id as connectionId\nSetup may still be IN_PROGRESS',
            'API-04': '200 OK\nEach address: status + errorCode',
            'API-05': '200 OK\nUpdated connection/address details\nRoute activation is separate',
        }[ident]
        purpose = {
            'API-01': 'Find available platform services',
            'API-02': 'Find this dataset\'s connections',
            'API-03': 'Create the missing connection',
            'API-04': 'Read each address\'s setup status',
            'API-05': 'Update supported setup details',
        }[ident]
        self.s.exchange(0, 1, purpose + '\n' + base.path_label(op['method'], op['path']), response,
                        f'[Existing] {ident} / FR-{ident[-2:]}', f'FR-{ident[-2:]} response')
        self.operations.append({'id': ident, **op})

    def finish(self):
        path = self.s.write([
            'Solid arrows: requests. Dashed arrows: responses. Lanes show responsibilities, not separate deployed services.',
            'Blue marks Spain work or an interface to confirm; it does not mean a new API. Provider setup may finish later. Route activation is separate.',
        ])
        palette.apply_colours(path)
        existing_read_frames(path)
        pairs = len(self.s.activations)
        assert pairs * 2 == len(self.s.messages)
        return path, {
            'view': self.slug, 'anchor': self.anchor, 'source_id': 'SPEC-SEI-039',
            'svg': str(path.relative_to(ROOT)), 'png': str(path.with_suffix('.png').relative_to(ROOT)),
            'drawio': str(path.with_suffix('.drawio').relative_to(ROOT)),
            'canvas_width': 260 + (len(self.s.used) - 1) * 385,
            'request_response_pairs': pairs, 'activation_bars': pairs,
            'operations': self.operations, 'references': self.refs,
            'pre_dispatch_gates': self.gates, 'conditional_effects': self.effects,
            'status': 'proposal; Spain interfaces and implementation still to confirm',
        }


def build_all(selected=None):
    paths, views = [], []
    for slug, title, subtitle, anchor in VIEWS:
        if selected is not None and slug not in selected:
            continue
        p = Sketch(slug, title, subtitle, anchor)
        s = p.s
        starts = {
            'shared-prerequisites': 'Before customer setup: the product is integrated with SXS and Tax Connections Service. These are product prerequisites, not repeated customer registrations.',
            'public-readiness': 'Start: the customer wants Sage access to the public platform. Inputs: business, requested function and environment.',
            'private-setup': 'Start: the selected business/client uses a chosen supported private platform. Keep a valid account or complete its qualified onboarding; then connect to Sage. Inputs: resolved dataset, chosen service and account evidence.',
            'supported-change': 'Start: the customer requests a setup change. Inputs: business, existing connection and the requested change.',
            'uncertainty-recovery': 'Start: an earlier setup request has an uncertain result. Keep its original business, provider, environment and request identity.',
        }
        s.note(starts[slug])
        if slug == 'shared-prerequisites':
            s.note('ERP/product first checks permission to view the selected business or accountant client. Firm login does not replace client access. The product uses its qualified SXS integration; actual interface and business/client mapping remain GAP-01/06.')
            s.exchange(0, 1, 'Resolve the company dataset\nBusiness/client + environment',
                       'datasetId / tenantId\nor missing/unknown + next action',
                       '[To confirm] SXS interface; GAP-01/06')
            s.note('Continue only with a confirmed dataset mapping. Missing setup follows the channel-specific SXS process; an unavailable lookup remains pending. Reuse the dataset when adding a platform.')
            f = s.start_frame('opt | Load current saved setup only where the selected channel supports API-02')
            op = base.OPERATIONS['API-02']
            s.exchange(0, 2, 'Load permitted current setup\n'+base.path_label(op['method'], op['path']),
                       'Access-point entries + saved references\nConfiguration alone is not readiness',
                       '[Existing] API-02 / FR-02; Spain applicability open', 'FR-02 response')
            p.operations.append({'id': 'API-02', **op})
            s.end_frame(f)
            s.note('ERP/product shows permitted saved setup. The customer or authorised accountant confirms the requested action/functions before the product requests shared checks. These are ONB-01/10 product actions, not additional API contracts.')
            t = s.call(0, 2, 'Check onboarding prerequisites\nNIF + datasetId + caller + action', '[To confirm] Setup request; ONB-02/03')
            s.exchange(2, 3, 'Validate the business NIF\nand permission for this action',
                       'Identity and permission confirmed\nor missing item + action owner', '[To confirm] Identity/permission API')
            f = s.start_frame('opt | Certificate required for this action; reuse suitable saved credentials')
            s.exchange(2, 4, 'Find and check the saved credential\nDataset + business + action + environment',
                       'Protected credential connection ID\nor missing/unsuitable/unknown + action',
                       '[To confirm] Tax/Connections B2B lookup; CERT-04/05')
            s.note('Missing credential: use separate Connections Service provisioning (040 section 2), then repeat the check. An unavailable lookup does not justify another upload.')
            s.end_frame(f)
            s.reply(t, 'Checks passed: continue\nOtherwise: missing item + owner', '[Setup result] ONB-02/03/08')
        elif slug == 'public-readiness':
            p.ref('21-shared-prerequisites', 'First: SXS dataset, permission and required Tax credential checks (2.1)', gate=True)
            f = s.start_frame('opt | Find a service only if its ID is not already known')
            p.http('API-01')
            s.end_frame(f)
            f = s.start_frame('opt | Inspect saved access-point setup only if missing/stale and the public channel supports it')
            p.http('API-02')
            g = s.start_frame('opt | Read detail only for a known connection')
            p.http('API-04')
            s.end_frame(g)
            s.end_frame(f)
            t = s.call(0, 1, 'Check Sage public access\nBusiness + action + environment', '[To confirm] Setup request; ONB-03/04')
            f = s.start_frame('opt | Check only missing/stale evidence; public method and permission must be confirmed')
            s.exchange(1, 4, 'Check access for this business/action\nNo onboarding method supplied', 'Access evidence or specific limitation', '[To confirm] Public access method')
            s.end_frame(f)
            s.reply(t, 'For each requested function:\nready or missing item + owner', '[Setup result] ONB-04/11')
        elif slug == 'private-setup':
            p.ref('21-shared-prerequisites', 'First: reuse the SXS dataset; permission and required credential checks pass (2.1)', gate=True)
            f = s.start_frame('opt | Read saved connections only for missing, stale or changed setup evidence')
            p.http('API-02')
            s.end_frame(f)
            s.note('Assess the account on the chosen platform for the selected business/client. An existing provider account may need a Sage connection; a valid Sage connection is reused. An accountant account must cover that client under the qualified provider/authority model.')
            f = s.start_frame('opt | No account on the chosen platform: complete qualified provider onboarding first')
            s.note('ERP/product presents required provider onboarding or a customer/provider handoff, then resumes the same request with completion evidence. GAP-02/06/08 must qualify the method and owner. Unknown account status or unsupported onboarding remains pending; do not assume account absence or a create-account API. ONB-05.')
            s.end_frame(f)
            f = s.start_frame('opt | Connect only for missing setup; confirm provider support, permission and earlier-invoice access')
            p.gates.append(f[0])
            p.http('API-03')
            s.exchange(1, 4, 'Link the chosen provider account\nProvider method still to confirm', 'Account linked, pending or failed',
                       '[To confirm] Provider contract / timing')
            s.end_frame(f)
            p.http('API-04')
            s.exchange(0, 1, 'Check whether setup is complete\nfor the requested functions', 'Setup result + missing item/owner\nRoute activation is separate',
                       '[To confirm] Setup request; ONB-06/11', '[Setup result] ONB-06/11')
        elif slug == 'supported-change':
            p.ref('21-shared-prerequisites', 'First: keep the SXS dataset; recheck only affected permission/credential evidence (2.1)', gate=True)
            t = s.call(0, 1, 'Check the requested setup change\nBusiness + connection + change', '[To confirm] Setup request; ONB-05/07')
            g = s.start_frame('opt | If the change affects routing or access to earlier invoices')
            s.exchange(1, 2, 'Check change permission, when it\ntakes effect and earlier access', 'Change allowed or blocked\nwith reason + action owner',
                       '[To confirm] Change permission / earlier access')
            s.end_frame(g)
            s.reply(t, 'Allowed change or reason + owner', '[Setup result] ONB-07/09')
            s.note('ERP/product presents the allowed scope, start and earlier-invoice impact. Submit platform use only if requested, enabled and confirmed. Setup-only work keeps any selection unchanged; if none exists, it activates none. ONB-07/11.')
            f = s.start_frame('opt | Apply only an allowed change; skip unchanged setup; Private A to Private B disabled')
            p.gates.append(f[0])
            p.ref('23-private-setup', 'Use private setup (2.3) only for a missing target connection', gate=True)
            g = s.start_frame('opt | Update only if this provider/API supports the requested edit')
            p.http('API-05')
            s.end_frame(g)
            g = s.start_frame('opt | If an authorised routing change is needed and its result can be checked')
            s.exchange(1, 2, 'Apply the authorised route change\nand check what actually changed', 'Effective boundary + earlier access\nor result still unknown',
                       '[To confirm] Route change method')
            s.end_frame(g)
            s.end_frame(f)
            s.exchange(0, 1, 'Read the result of this change', 'Confirmed result or pending action\nwith its owner',
                       '[To confirm] Setup request; ONB-11', '[Setup result] ONB-07/09/11')
        else:
            p.ref('21-shared-prerequisites', 'First: use the original SXS dataset and permission to inspect; do not create setup (2.1)', gate=True)
            f = s.start_frame('opt | Read only a known connection whose detail can safely add evidence')
            p.http('API-04')
            s.end_frame(f)
            t = s.call(0, 1, 'Find out what happened\nOriginal request + business/provider', '[To confirm] Setup request; ONB-08')
            f = s.start_frame('opt | Check with the original provider only through a confirmed observation method')
            s.exchange(1, 4, 'Check the earlier setup request\nDo not repeat it', 'Succeeded, no effect, conflict\nor result still unknown',
                       '[To confirm] Earlier request status')
            s.end_frame(f)
            s.reply(t, 'Confirmed result or pending action\nwith a named owner', '[Setup result] ONB-08/11')
        outcomes = {
            'shared-prerequisites': 'End: reuse the resolved dataset and any required suitable credential, or return the pending action and owner. Keep each returned reference with its source API; credential/E-Invoice ID relationships remain unconfirmed under GAP-06.',
            'public-readiness': 'End: return public readiness or a specific missing item and owner. No public enrolment call or test invoice is assumed.',
            'private-setup': 'End: reuse matching setup; otherwise follow each address status. IN_PROGRESS/RETRYING means wait and observe. Route activation is separate.',
            'supported-change': 'End: retain unchanged setup or return the confirmed change and its effective boundary. Keep earlier-invoice access; hold unknown results.',
            'uncertainty-recovery': 'End: record confirmed success once. Retry only with proven absence of an effect and confirmed retry rules; otherwise hold with an owner. Never duplicate RETRYING work.',
        }
        s.note(outcomes[slug])
        path, item = p.finish()
        paths.append(path)
        views.append(item)
    return paths, views


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--view', action='append', choices=[view[0] for view in VIEWS], help='Build only the selected existing view(s).')
    parser.add_argument('--report', type=Path, help='Optional JSON report destination for selected views.')
    args = parser.parse_args()
    paths, views = build_all(selected=args.view)
    # Render PNG previews separately after the SVG/Draw.io scene checks.
    report = args.report or (ROOT / 'work/onboarding-clarity-review/diagram-sequences.json' if args.view is None else None)
    if report is not None:
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps({'views': views, 'live_publication': False}, indent=2) + '\n')
