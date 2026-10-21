"""Build SPEC-SEI-020 API views without changing the existing process diagrams.

Reuse the onboarding sequence renderer. Every HTTP operation comes from the
supplied FR contracts. GAP labels are proposed handoffs, never endpoint names.
Run with python3 work/build-onboarding-api-diagrams.py.
"""
from pathlib import Path
import importlib.util
import re
import textwrap
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
definition = importlib.util.spec_from_file_location(
    'onboarding_sequences', ROOT / 'work/build-spain-sequence-diagrams.py')
seq = importlib.util.module_from_spec(definition)
definition.loader.exec_module(seq)
seq.XS = [140, 750, 1090, 1390, 1660]


def wrap_api_label(value, width):
    """Wrap long endpoint labels at path boundaries, preserving every character."""
    if re.match(r'^\d+\s+API-\d+ (GET|POST|PUT) /', value) and len(value) > width:
        split = value.rfind('/', 0, width) + 1
        if split and len(value[split:]) <= width:
            return [value[:split], value[split:]]
    return textwrap.wrap(value, width)


seq.textwrap = SimpleNamespace(wrap=wrap_api_label)
SOURCE = '../../specs/onboarding/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md'
PARTIES = ['ERP / product', 'Global API\nFR contract candidate',
           'Domain Service -\nE-Invoice Service\nProposed coordination',
           'Domain Service -\nOther Services\nIdentity / trust / routing',
           'Public / private platforms\nQualified integration']
LIST = '/accesspoints'
DATASET = '/datasets/{datasetId}/accesspoints'
CREATE = '/connectors/{accessPointId}/datasets/{datasetId}/connect'
CONNECTION = '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/'


def diagram(slug, title, subtitle):
    return seq.Sequence(slug, title, subtitle, SOURCE, PARTIES)


def request(s, api, method, path, response, ref):
    s.msg(0, 1, f'{api} {method} {path}', ref)
    s.msg(1, 2, 'Dispatch scoped operation', 'Proposed internal handoff')
    s.msg(2, 1, response, 'Documented FR response; Spain mapping open', 'reply')
    s.msg(1, 0, response, api, 'reply')


def build_all():
    paths = []
    s = diagram('onboarding-api-discovery-sequence',
                'Onboarding API view - Discover and inspect connections',
                'ONB-01/02/10/11 | Documented FR operations; proposed Spain reuse only.')
    s.band('1 - Bind the business and allowed access')
    s.note(0, 3, 'Resolve the authenticated caller, represented business and dataset mapping before protected reads. M2M authentication alone does not establish delegated authority. No dataset-to-business equivalence is assumed.', 'GAP-01/03 | ONB-02 | ONB-R01/19')
    s.band('2 - List available options and existing dataset connections')
    request(s, 'API-01', 'GET', LIST, '200 - AccessPoint resources', 'FR-01 | ONB-10')
    s.note(0, 2, 'FR-01 declares datasetId as a path parameter but /accesspoints has no matching placeholder. Confirm the canonical signature before client generation. Listing is not selection, readiness or activation.', 'GAP-07 | FR-01')
    request(s, 'API-02', 'GET', DATASET, '200 - access points and connectionId', 'FR-02 | ONB-10')
    s.band('3 - Inspect only a known authorised connection')
    f = s.start_frame('opt - A permitted connectionId is available')
    request(s, 'API-04', 'GET', CONNECTION, '200 - address status and errorCode', 'FR-04 | ONB-10/11')
    s.end_frame(f)
    s.note(0, 3, 'Compare requested functions with observed evidence. A failed read or 404 does not prove external absence. Valid unchanged setup uses no POST or PUT. Return missing checks and their owner.', 'ONB-S02/03/05/08 | ONB-R11/12/13')
    paths.append(s.write(['Existing FR shapes are reuse candidates; deployment and Spain support remain unqualified.',
                          'CONNECTED is a connection observation, not proof of per-function readiness or route activation.',
                          'Related contract and identity gaps: GAP-01/03/05/07/08. No new endpoint is implied.']))

    s = diagram('onboarding-api-private-connection-sequence',
                'Onboarding API view - Create a private connection and observe the result',
                'ONB-S01/03/04 | Later-phase proposal; qualified provider scope is required.')
    s.band('1 - Use discovery results and qualify missing work')
    s.note(0, 3, 'Use API-01/02/04 to find matching setup. Reuse valid existing configuration. Check business identity, current authority, selected service and conditional trust. Missing approval returns to ONB-12.', 'ONB-01/02/03/05/10/12 | GAP-01/02/03/06')
    s.msg(2, 3, 'Qualify authority and trust', 'GAP-03/06 - API contracts not supplied')
    s.msg(3, 2, 'Evidence or owned limitation', 'Proposed handoff; no endpoint assigned', 'reply')
    s.band('2 - Create only a separately authorised missing connection')
    f = s.start_frame('opt - Selected plan needs create and Spain contract is qualified')
    s.note(0, 3, 'Save the original intent and Idempotency-Key before dispatch. FR payload uses company/user information and France address types. Do not send Spain NIF as fr.siren or inherit the omitted-usage default.', 'OFR-01 | API-03 | GAP-02/04')
    request(s, 'API-03', 'POST', CREATE, '201 - connection resource and address status', 'FR-03 | ONB-05/06')
    s.note(0, 3, '201 records resource creation. The address result can still be IN_PROGRESS, RETRYING, CONNECTED, DISCONNECTED or ERROR. It does not establish Spain capability readiness or activation.', 'FR-03 | GAP-05')
    s.end_frame(f)
    s.band('3 - Observe and recover the original operation')
    f = s.start_frame('opt - Known connectionId; owner-approved observation schedule')
    request(s, 'API-04', 'GET', CONNECTION, '200 - current address observations', 'FR-04 | ONB-06/08')
    s.end_frame(f)
    s.note(0, 3, 'After a lost create response, connectionId may be unknown. API-02 discovery alone is not authoritative operation correlation. Keep affected work on hold until original-effect evidence or qualified same-key replay resolves it. No fresh-key POST.', 'OFR-05/06/07 | GAP-04')
    s.band('4 - Gate activation and return independent results')
    s.msg(2, 3, 'Request authorised route decision', 'GAP-06 - routing API not supplied')
    s.msg(3, 2, 'Observed boundary or hold', 'ONB-07/09 - separate activation gate', 'reply')
    s.note(0, 3, 'ONB-11 returns separate connection, readiness and evidenced activation results. Preserve earlier invoice context. Runtime owners retain current authority and credential checks.', 'ONB-11 | GAP-05/06')
    paths.append(s.write(['No supplied FR endpoint proves Spain activation, approval, certificate or representation coverage.',
                          'Source operation paths and response codes are exact; internal handoffs are proposed and labelled GAP.',
                          'Private A to Private B remains gated. A diagram cannot enable an unsupported transition.']))

    s = diagram('onboarding-api-update-recovery-sequence',
                'Onboarding API view - Update a connection and handle uncertainty',
                'ONB-S05/06 | API-05 and API-04; no approved Spain update semantics yet.')
    s.band('1 - Read current state and qualify the exact change')
    request(s, 'API-04', 'GET', CONNECTION, '200 - current connection observations', 'FR-04 | ONB-10')
    s.note(0, 3, 'Preserve the current plan and earlier obligations. FR update permits add or update; update changes address dates only. Same-SIREN grouping, country rules and expected-version protection need explicit qualification.', 'FR-05 | ONB-05/07/09 | GAP-02/04/07')
    s.band('2 - Apply a supported, authorised change')
    f = s.start_frame('opt - Selected update is qualified; otherwise return an owned limitation')
    request(s, 'API-05', 'PUT', CONNECTION, '200 - updated resource and address status', 'FR-05 | ONB-05/06')
    s.end_frame(f)
    s.band('3 - Handle a lost result without repeating a possible effect')
    s.note(0, 3, 'The supplied PUT operation declares no Idempotency-Key or expected-version header. PUT naming alone cannot prove business repeat safety. Save the original intent and keep uncertain work on hold.', 'OFR-01/05 | GAP-04')
    f = s.start_frame('opt - Known connectionId and qualified read can observe relevant state')
    request(s, 'API-04', 'GET', CONNECTION, '200 - observed values and address status', 'FR-04 | OFR-06')
    s.end_frame(f)
    s.note(0, 3, 'Compare intended and observed state with source, time and operation evidence. A matching connection record may not prove the external effect or its executor. Failed/404 observations do not permit blind repetition. Escalate unresolved work.', 'ONB-08 | OFR-06/07 | GAP-04/05')
    s.band('4 - Resume the blocked check, not an automatic route change')
    s.note(0, 3, 'A resolved change returns to ONB-06 or its exact parent check. ONB-07 separately qualifies activation/restoration. Cancellation and old-dependency release retain their own evidence gates.', 'ONB-06/07/08/09/11 | OFR-R10')
    paths.append(s.write(['FR date-only update is not a generic switch, cancellation, rollback or disconnect contract.',
                          'No DELETE, operation-status or approval endpoint is invented from the five supplied files.',
                          'Reconciliation owner and proof thresholds remain GAP-04/06 decisions.']))

    s = diagram('onboarding-api-public-readiness-sequence',
                'Onboarding API view - Public readiness and missing API coverage',
                'ONB-S02 | Phase 1; FR discovery calls are candidates, not proven public support.')
    s.band('1 - Discover public support only if the API owner qualifies it')
    f = s.start_frame('opt - API-01/02 are qualified for the selected public service')
    request(s, 'API-01', 'GET', LIST, '200 - supported access-point options', 'FR-01 | GAP-07/08')
    request(s, 'API-02', 'GET', DATASET, '200 - existing dataset connections', 'FR-02 | GAP-01/08')
    s.end_frame(f)
    s.band('2 - Qualify identity, authority, access and required trust')
    s.msg(2, 3, 'Verify represented business and action', 'GAP-03/06 - API contract not supplied')
    s.msg(3, 2, 'Independent check findings', 'ONB-02/03 - current evidence', 'reply')
    s.msg(2, 3, 'Check purpose-specific protected access', 'GAP-06 - reuse SPEC-SEI-001 contract')
    s.msg(3, 2, 'Readiness reference or limitation', 'No credential material', 'reply')
    s.band('3 - Run only the selected qualified public checks')
    s.msg(2, 4, 'Qualified non-mutating public check', 'GAP-06 - connector contract to bind')
    s.msg(4, 2, 'Observation or failed check', 'ONB-03/08 - exact operation owner', 'reply')
    s.note(0, 3, 'No supplied FR create/update operation establishes a Spain public-enrolment requirement. Do not use API-03 as external registration or send a test invoice. Missing prerequisite is not an unknown mutation.', 'ONB-SPFE-R02 | SPFE-S03/S08 | GAP-02/06')
    s.band('4 - Record and return per-function readiness')
    s.note(0, 3, 'ONB-04/11 needs a qualified per-function result contract. FR connection status cannot supply identity, authority, trust, public-readiness and activation findings by itself. Keep the missing contract visible.', 'ONB-04/11 | GAP-05/06')
    paths.append(s.write(['This view deliberately exposes missing call contracts instead of giving proposed endpoints factual names.',
                          'The full public business process remains in SPEC-SEI-019; country/source rules are unchanged.',
                          'Phase 1 performs no route activation; failure recovery returns to the affected readiness check.']))
    return paths


if __name__ == '__main__':
    seq.render(build_all())
