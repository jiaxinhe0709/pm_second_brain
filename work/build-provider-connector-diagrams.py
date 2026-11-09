"""Build Provider Connector diagrams with the established onboarding visual renderers."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    result=importlib.util.module_from_spec(spec); spec.loader.exec_module(result)
    return result

flow=module('connector_flow','work/build-onboarding-scenario-diagrams.py')
uml=module('connector_uml','work/onboarding-sequence-renderer.py')
SUMMARY='../../specs/provider-connectors/SPEC-SEI-044-provider-connector-architecture-summary.md'
SEQUENCE='../../specs/provider-connectors/SPEC-SEI-046-provider-connector-api-sequences-and-reuse-assessment.md'
PARTIES=['ERP / product','Domain Service -\nE-Invoice Service',
         'Domain Service - Other Services\nNotifications',
         'Domain Service - Other Services\nProvider Connector',
         'Public / private\nplatforms']


def architecture():
    n,e=flow.node,flow.edge
    nodes=[
        n('product',0,0,'Product consumes shared API','SPEC013','Product-scoped requests and results'),
        n('api',1,1,'One shared e-Invoicing API','CA-ARCH01/02','Product, provider and connector roles'),
        n('feature',2,1,'E-Invoice Service owns work','CA-01–05','Saved actions, evidence and results'),
        n('controls',0,2,'Check scoped access and profile','SPEC001 / 014','Identity, authority and fixed context'),
        n('notify',2,2,'Dispatch work notification','CA-ARCH01','Assigned operation and executor'),
        n('connector',3,2,'Provider Connector consumes API','CA-ARCH01/02','Gets content; submits source results'),
        n('direct',0,4,'Authorised provider consumes API','SPEC013','Alternative integration mode','conditional'),
        n('private',4,4,'Six private-provider bindings','PRD214','B2B Router, Banqup, EDICOM,', 'flow'),
        n('public',5,4,'One SPFE binding','SPEC011','External public contract'),
        n('support',4,3,'Resolve blocked / uncertain work','CS06 / 07 / 12 / 16','Keep original action and context','recovery'),
    ]
    # Keep the full provider list in the footer, not inside an unreadable card.
    nodes[7]['note']='Provider-specific external contracts'
    flow.classify(nodes,{v['key']:('Conditional' if v['key'] in ('direct','support') else 'Scenario-specific' if v['key'] in ('private','public') else 'Common') for v in nodes})
    return flow.build('provider-connector-logical-architecture','Provider Connectors: one shared API for all consumer roles',
        'Confirmed shared-contract direction. Notifications dispatch work; external platform contracts remain separate. Source: CA-ARCH01/02.',
        nodes,[e('product','api'),e('direct','api','conditional'),e('controls','api'),e('api','feature'),
               e('feature','notify'),e('notify','connector'),e('connector','api'),
               e('connector','private'),e('connector','public'),e('connector','support','recovery')],
        spec=SUMMARY,width=2110,height=1040,
        lanes=['ERP / product','Domain Service - E-Invoice Service','Domain Service - Other Services','Operations / support','Public / private platforms'],
        legend='Solid: logical handoff / dependency · Dashed: integration-mode alternative or recovery · Darker grey: recovery',
        boundaries=[
            'Scope: six private connectors (B2B Router, Banqup, EDICOM, SERES, ZeroComa, Sovos) + SPFE = seven; one common Sage API contract.',
            'A direct provider consumer is an alternative executor role, not a second sender for an action already assigned to a connector.',
            'Shared API access has role-specific permissions. Notifications are dispatch, not a separate invoice API. Crossed lines do not join.',
        ])


def operation():
    s=uml.Sequence('provider-connector-operation-sequence','Shared API: product request, connector execution and result',
        'Same Sage API contract for product, authorised provider and connector roles; external platform calls are separate',SEQUENCE,PARTIES)
    s.note('The E-Invoice Service participant exposes the shared API. Call labels are logical until mapped to the actual version; no separate Provider Connector API is introduced.','CA-ARCH01/02; SPEC013')
    f=s.start_frame('ref | A · Accept authorised work or stop before an external effect')
    s.exchange(0,1,'Submit setup / invoice operation\nCustomer scope and stable identity','Saved receipt or denial / conflict\nTechnical acceptance is not delivery','[Proposed] CA-01/02; CS01–03 / 14')
    s.end_frame(f)
    f=s.start_frame('opt | B · Connector is the selected executor; known external response')
    s.exchange(1,2,'Publish saved work for the assigned executor','Dispatch recorded\nNot external completion','[Proposed] CA-02; CS03 / 07')
    s.exchange(2,3,'Deliver work notification\nKeep original operation identity','Notification acknowledged\nNot external completion','[Proposed] CA-02; CS03 / 07')
    s.exchange(3,1,'Read permitted work / saved content\nUse connector caller role','Scoped content and fixed context\nRecheck effective access','[Proposed] CA-01/02; CS02 / 11')
    s.exchange(3,4,'Call selected external platform\nApproved profile and credential','Source acknowledgement / rejection\nPreserve actual correlation','[Proposed] CA-03; CS04 / 05')
    s.exchange(3,1,'Submit source status / result evidence\nThrough the same shared API','Durable correlated result recorded\nIndependent item / action outcomes','[Proposed] CA-03; CS04 / 13 / 15')
    s.exchange(0,1,'Read permitted operation / invoice result','Current saved outcome and evidence\nNo inferred buyer acceptance','[Proposed] CA-03; CS04 / 13')
    s.end_frame(f)
    f=s.start_frame('opt | C · Alternative: possible external effect, lost response or failed local evidence save')
    s.exchange(3,1,'Submit uncertain execution observation\nOriginal identity and attempt','Unknown / pending recovery retained\nNo fresh send or automatic failover','[Proposed] CA-03/05; CS06 / 07 / 12')
    q=s.start_frame('opt | Reconciliation query is qualified and current authority permits access')
    s.exchange(3,4,'Query original source reference','Correlated source observation\nConfirmed or still uncertain','[Proposed] CA-03; CS06 / 11')
    s.exchange(3,1,'Submit recovered source observation\nSame shared API and original action','Evidence recorded or held for owner\nIgnore stale execution ownership','[Proposed] CA-03; CS06 / 15')
    s.end_frame(q)
    s.note('If reconciliation is unsupported, blocked or inconclusive, hold the original work for its owner. Retry lost shared-API submissions under the same identity; do not repeat the external mutation merely to recover local evidence.','CA-02/03/05; CS06 / 07 / 11 / 12 / 16')
    s.end_frame(f)
    return s.write(['Solid: requests. Dashed: paired technical responses. Grey bars: handling intervals, not elapsed time.',
        'Blue: proposed operation mapping under the confirmed common API direction. A direct provider executor uses this same API contract; only one executor may send each action.'],reuse_colours=True)


def inbound():
    parties=[PARTIES[0],PARTIES[1],PARTIES[3],PARTIES[4]]
    s=uml.Sequence('provider-connector-inbound-sequence','Shared API: source capture, product retrieval and replay',
        'Provider Connectors submit source data through the same API products use to retrieve it',SEQUENCE,parties)
    s.note('Entry paths A1/A2 are alternatives. Acquire only within authorised source scope. Source capture is separate from buyer acceptance.','CA-01/04; CS08 / 09')
    f=s.start_frame('opt | A1 · Connector polls / downloads through the selected external contract')
    s.exchange(2,3,'Query / download source invoice or event','Source bytes / page / empty / fault\nPreserve continuation and evidence','[Proposed] CA-03/04; CS08')
    s.end_frame(f)
    f=s.start_frame('opt | A2 · Alternative: qualified platform push; no supplied SPFE push interface')
    s.exchange(3,2,'Deliver source content / notification\nAuthenticate source and account scope','Contract-defined technical response\nCapture / acknowledgement order is qualified','[Proposed] CA-01/04; CS09')
    s.end_frame(f)
    f=s.start_frame('ref | B · Shared-API intake and product access')
    s.exchange(2,1,'Submit source invoice / event evidence\nStable source identity and timestamps','Durable capture receipt\nSame identity deduplicates','[Proposed] CA-04; CS08 / 10')
    s.note('Advance covered acquisition progress only after durable capture. If the external contract requires capture before its acknowledgement, complete this intake before sending that acknowledgement.','CA-04; CS08 / 09 / 10')
    s.exchange(0,1,'Retrieve permitted saved invoice / status\nUse product caller permissions','Saved content / source observation\nSame shared API contract','[Proposed] CA-01/04; CS02 / 08')
    s.end_frame(f)
    f=s.start_frame('opt | C · Intake response lost, interrupted capture or duplicate source delivery')
    s.exchange(2,1,'Repeat original intake submission\nSame source identity and input','Existing or newly committed capture\nNo duplicate business processing','[Proposed] CA-02/04; CS03 / 10 / 15')
    s.end_frame(f)
    s.note('An authorised provider can submit directly to the same API where its integration mode assigns that role. A connector and provider must not independently execute the same delivery. Expired cursors/source gaps require qualified recovery before a completeness claim.','CA-01–04; CS02 / 08 / 10')
    return s.write(['Solid: requests. Dashed: paired responses. Grey bars: handling intervals, not elapsed time.',
        'Blue: proposed operation mapping. Provider-owned and SPFE interfaces remain external contracts; permissions differ by consumer role.'],reuse_colours=True)


def fit_participant_labels(path):
    # Retain full responsibility labels while fitting the established participant boxes.
    ns={'s':'http://www.w3.org/2000/svg'}
    tree=ET.parse(path)
    labels={'Domain Service - Other Services'}
    for text in tree.findall('.//s:text',ns):
        if text.text in labels: text.set('font-size','14')
    ET.register_namespace('',ns['s']);tree.write(path,encoding='unicode')
    draw=ET.parse(path.with_suffix('.drawio'))
    for cell in draw.findall('.//mxCell'):
        value=cell.get('value','')
        if value.startswith('Domain Service - Other Services\n'):
            cell.set('style',cell.get('style').replace('fontSize=20;','fontSize=14;'))
            geom=cell.find('mxGeometry'); old_x=float(geom.get('x'));old_w=float(geom.get('width'))
            geom.set('x',str(old_x+old_w/2-108));geom.set('width','216')
    draw.write(path.with_suffix('.drawio'),encoding='unicode',xml_declaration=True)


def render(paths):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page(device_scale_factor=1)
        page.route('http://**/*',lambda route:route.abort());page.route('https://**/*',lambda route:route.abort())
        for path in paths:
            fit_participant_labels(path)
            r=ET.parse(path).getroot(); w,h=int(r.get('width')),int(r.get('height'))
            page.set_viewport_size({'width':w,'height':h});page.goto(path.as_uri())
            failures=page.evaluate('''() => {const v=document.querySelector('svg').viewBox.baseVal;return [...document.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<0||b.y<0||b.x+b.width>v.width||b.y+b.height>v.height}).map(t=>t.textContent)}''')
            assert not failures,(path.name,failures)
            card_failures=page.evaluate('''() => [...document.querySelectorAll('svg a')].flatMap(a=>{const shape=a.querySelector('rect,path');if(!shape)return [];const b=shape.getBBox();return [...a.querySelectorAll('text')].filter(t=>{const r=t.getBBox();return r.x<b.x+2||r.x+r.width>b.x+b.width-2||r.y<b.y+2||r.y+r.height>b.y+b.height-2}).map(t=>t.textContent)})''')
            assert not card_failures,(path.name,card_failures)
            page.locator('svg').screenshot(path=str(path.with_suffix('.png')))
            page.set_viewport_size({'width':480,'height':800})
            page.goto('about:blank');page.set_content('<div style="width:100%;overflow-x:auto">'+path.read_text()+'</div>')
            assert page.locator('div').evaluate('(e)=>e.scrollWidth>e.clientWidth')
            print(path.name,'rendered with onboarding visual system; text bounds valid')
        browser.close()

if __name__=='__main__':render([architecture(),operation(),inbound()])
