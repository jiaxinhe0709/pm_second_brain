"""Build high-level SPEC-SEI-020 API views without changing the business diagrams.

Reuse the onboarding sequence renderer. Every HTTP operation comes from the
supplied FR contracts. Each view has four or five interactions; detailed recovery stays in the spec.
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
seq.XS = [140, 750, 1490]


def wrap_api_label(value, width):
    """Wrap long endpoint labels at path boundaries, preserving every character."""
    if re.match(r'^\d+\s+API-\d+ (GET|POST|PUT) /', value) and len(value) > width:
        split = value.rfind('/', 0, width) + 1
        if split and len(value[split:]) <= width:
            return [value[:split], value[split:]]
    return textwrap.wrap(value, width)


seq.textwrap = SimpleNamespace(wrap=wrap_api_label)
SOURCE = '../../specs/onboarding/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md'
PARTIES = ['Product / ERP', 'Existing FR API\nReused for Spain',
           'Spain country pack\nRules and integrations']
LIST = '/accesspoints'
DATASET = '/datasets/{datasetId}/accesspoints'
CREATE = '/connectors/{accessPointId}/datasets/{datasetId}/connect'
CONNECTION = '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/'


def diagram(slug, title, subtitle):
    return seq.Sequence(slug, title, subtitle, SOURCE, PARTIES)


def call(s, api, method, path, ref):
    s.msg(0, 1, f'{api} {method} {path}', ref)


def result(s, title, ref):
    s.msg(1, 0, title, ref, 'reply')


def finish(s, mapping, limit):
    return s.write([
        'Agreed direction: reuse the FR API and tailor Spain through a country pack. Logical boundaries only.',
        mapping,
        limit + ' Detailed errors, recovery and contract questions stay in SPEC-SEI-020.'])


def build_all():
    paths = []
    s = diagram('onboarding-api-discovery-sequence',
                'Onboarding API overview - Discover and inspect setup',
                'Authorised product and dataset | Key calls only; intermediate responses are omitted.')
    s.band('Discover supported services and inspect existing setup')
    call(s, 'API-01', 'GET', LIST, 'FR-01 | Available services')
    s.msg(1, 2, 'Apply Spain service and access rules', 'Country pack | GAP-01/02/03')
    call(s, 'API-02', 'GET', DATASET, 'FR-02 | Existing dataset connections')
    call(s, 'API-04', 'GET', CONNECTION, 'FR-04 | Only when connection detail is needed')
    result(s, 'Return options and current setup', 'ONB-10/11 | No change for valid existing setup')
    paths.append(finish(s, 'Activity mapping: ONB-02/05/10/11. API-04 uses a known authorised connectionId.',
                        'Failed discovery cannot establish external absence.'))

    s = diagram('onboarding-api-private-connection-sequence',
                'Onboarding API overview - Connect a private provider',
                'Later-phase scope | Reuse existing setup; create only a missing authorised connection.')
    s.band('Create missing setup and return its connection result')
    call(s, 'API-03', 'POST', CREATE, 'FR-03 | Supported missing connection only')
    s.msg(1, 2, 'Apply Spain rules and provider checks', 'Country pack | Before dependent external work')
    call(s, 'API-04', 'GET', CONNECTION, 'FR-04 | Inspect returned connectionId when needed')
    result(s, 'Return connection result and next action', 'ONB-06/11 | Activation remains a separate decision')
    paths.append(finish(s, 'Activity mapping: ONB-02/03/05/06/07/08/09/11. Reuse the connection returned by API-03.',
                        'Unknown effects stay on hold; earlier invoice context is preserved.'))

    s = diagram('onboarding-api-update-recovery-sequence',
                'Onboarding API overview - Change existing setup',
                'Authorised change | Country rules and exact supported edits still require qualification.')
    s.band('Read current setup, apply a supported change and inspect the result')
    call(s, 'API-04', 'GET', CONNECTION, 'FR-04 | Current authorised setup')
    call(s, 'API-05', 'PUT', CONNECTION, 'FR-05 | Supported change only')
    s.msg(1, 2, 'Validate Spain change and permissions', 'Country pack | Before dependent external work')
    call(s, 'API-04', 'GET', CONNECTION, 'FR-04 | Observe result when needed')
    result(s, 'Return updated result or required action', 'ONB-06/08/11 | No automatic route switch')
    paths.append(finish(s, 'Activity mapping: ONB-05/06/07/08/09/10/11. Concurrent changes retain expected-version controls.',
                        'A failed observation does not permit blind PUT repetition.'))

    s = diagram('onboarding-api-public-readiness-sequence',
                'Onboarding API overview - Public readiness',
                'Public MVP means Phase 1 onboarding readiness | Required API deltas remain to confirm.')
    s.band('Select public service, assess setup and return readiness')
    call(s, 'API-01', 'GET', LIST, 'FR-01 | Spain public service option')
    call(s, 'API-02', 'GET', DATASET, 'FR-02 | Existing authorised setup')
    s.msg(1, 2, 'Apply Spain readiness checks', 'Country pack | Identity, authority and required trust')
    result(s, 'Return readiness and required actions', 'ONB-04/11 | Per requested public function')
    paths.append(finish(s, 'Activity mapping: ONB-02/03/04/08/10/11. Bind the actual shared and public connector contracts.',
                        'Internal connection setup may need API-03/05; no external enrolment is inferred.'))
    return paths


if __name__ == '__main__':
    seq.render(build_all())
