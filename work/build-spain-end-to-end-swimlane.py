"""Build the proposed, spec-linked Spain responsibility overview."""
from pathlib import Path
import json
import html
import textwrap
import subprocess
from urllib.parse import quote, urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/spain-end-to-end-responsibility-overview'
LANES = ['Customer / accountant', 'ERP / product', 'Domain Service', 'Shared services / Operations', 'Public / private platforms']
NODES = []
EDGES = []
PHASES = []
ROW = 0
remote = subprocess.check_output(['git','remote','get-url','origin'],cwd=ROOT,text=True).strip()
if remote.startswith('git@'):
    host, repo = remote.split('@',1)[1].split(':',1)
else:
    remote_url = urlparse(remote)
    host, repo = remote_url.hostname, remote_url.path.lstrip('/')
assert host == 'github.com'
repo = repo.removesuffix('.git')
branch = subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
remote_paths = set(subprocess.check_output(['git','ls-tree','-r','--name-only',f'origin/{branch}','specs'],cwd=ROOT,text=True).splitlines())

def phase(title, note, rows):
    global ROW
    PHASES.append(dict(title=title, note=note, row=ROW, rows=rows))
    ROW += rows + 1
    return PHASES[-1]['row']

def node(id, lane, row, title, spec, note=''):
    p = next((ROOT / 'specs').glob(f'SPEC-SEI-{spec:03}-*.md'))
    canonical_path = str(p.relative_to(ROOT))
    published_paths = [path for path in remote_paths if Path(path).name.startswith(f'SPEC-SEI-{spec:03}-')]
    assert len(published_paths) == 1
    published_path = canonical_path if canonical_path in remote_paths else published_paths[0]
    NODES.append(dict(id=id, lane=lane, row=row, title=title, spec=f'SPEC-SEI-{spec:03}',
                      path=str(p), relative='../../' + canonical_path, note=note,
                      url=f'https://github.com/{repo}/blob/{quote(branch,safe="/")}/{published_path}'))

def edge(source, target, kind='flow', label=''):
    EDGES.append(dict(source=source, target=target, kind=kind, label=label))

r = phase('1 · Set up and connect', 'Readiness is specific to the business, action and environment.', 8)
node('SET-01',0,r+1,'Request setup for a business',2)
node('SET-02',1,r+2,'Use authorised Global API access',13)
node('SET-03',2,r+3,'Check identity and business authority',2)
node('SET-04',3,r+4,'Check required certificates and trust',1,'Only for the selected purpose; certificate possession does not confer authority.')
node('SET-05',3,r+5,'Test the enabled public operation',11,'The connector handles protocol and evidence, not business interpretation.')
node('SET-06',4,r+5,'Return public-operation evidence',11,'Exact public interfaces remain qualification gates.')
node('SET-07',2,r+6,'Record capability readiness',2,'Registration, readiness and route activation remain separate.')
node('SET-08',3,r+7,'Recover uncertain onboarding',4,'Conditional exception. Check authoritative external state before unsafe retry.')
for a,b in [('SET-01','SET-02'),('SET-02','SET-03'),('SET-03','SET-04'),('SET-04','SET-05'),('SET-05','SET-06'),('SET-06','SET-07')]:edge(a,b)
edge('SET-03','SET-08','support','If setup fails or is uncertain')

r = phase('2 · Prepare and send', 'Outbound journey. Recipient delivery and any public copy have independent outcomes.', 17)
node('OUT-01',1,r+1,'Create and submit complete draft',7)
node('OUT-02',2,r+2,'Prepare draft under Spain policy',7)
node('OUT-03',3,r+3,'Check UBL and return issues',5,'UBL-specific check. Other representations need their own qualified profiles.')
node('OUT-04',1,r+4,'Show preparation result',7)
node('OUT-05',0,r+4,'Review draft or correct issues',7)
node('OUT-06',1,r+5,'Issue only when ready; freeze revision',7,'The ERP owns issuance. A draft pass is not issuance.')
node('OUT-07',2,r+6,'Accept final data; recheck authority',7)
node('OUT-08',3,r+7,'Find current recipient destination',12,'No central AEAT directory is assumed. Failed lookup does not establish public routing.')
node('OUT-09',2,r+8,'Freeze route and required exchange actions',7)
node('OUT-10',3,r+9,'Generate with qualified Spain mapper',8,'Reuse candidate: qualify the Spain mapper migration, DTS contract, profile and operations before use.')
node('OUT-11',3,r+10,'Validate exact final UBL',5)
node('OUT-12',3,r+11,'Sign or seal only when required',1,'Only when the selected policy requires it; the exact actor and protected operation need qualification.')
node('OUT-13',2,r+12,'Execute each authorised action',7,'Public-platform actions use SPEC-SEI-011. Private delivery requires its qualified adapter or executor.')
node('OUT-14',4,r+13,'Recipient delivery action: public OR private',7)
node('OUT-15',4,r+14,'Separate public copy, if required',7,'Conditional obligation; not another recipient delivery or a universal country default.')
node('OUT-16',2,r+15,'Record each action outcome',7)
node('OUT-17',3,r+15,'Reconcile only uncertain actions',7,'Conditional recovery. Keep original route, payload and operation identity; do not replay successful actions.')
node('OUT-18',1,r+16,'Show qualified outbound status',9,'Technical acknowledgement does not establish buyer acceptance.')
for a,b in [('OUT-01','OUT-02'),('OUT-02','OUT-03'),('OUT-03','OUT-04'),('OUT-04','OUT-05'),('OUT-05','OUT-06'),('OUT-06','OUT-07'),('OUT-07','OUT-08'),('OUT-08','OUT-09'),('OUT-09','OUT-10'),('OUT-10','OUT-11'),('OUT-11','OUT-12'),('OUT-12','OUT-13'),('OUT-13','OUT-14'),('OUT-14','OUT-16'),('OUT-16','OUT-18')]:edge(a,b)
edge('OUT-13','OUT-15','conditional','Only if required')
edge('OUT-15','OUT-16')
edge('OUT-16','OUT-17','support','If result unknown')

r = phase('3 · Retrieve and receive', 'Independent inbound journey. Source-file access does not wait for ERP processing.', 11)
node('RCV-01',2,r+1,'Schedule authorised public retrieval',10)
node('RCV-02',3,r+2,'Call qualified public retrieval',11)
node('RCV-03',4,r+3,'Provide recovered public file',10)
node('RCV-04',3,r+4,'Preserve exact source and file role',10,'Preserve original, public-copy and derived-file roles; safe storage is not dependent on mapping success.')
node('RCV-05',4,r+4,'Private invoice arrival',6,'Alternative ingress with independent private-route readiness; not a consequence of public retrieval.')
node('RCV-06',0,r+5,'Download authorised saved source',10,'Independent read branch. Apply current authority and safe-file controls; download is not acceptance.')
node('RCV-07',2,r+5,'Match recipient and resolve duplicates',6)
node('RCV-08',3,r+6,'Check inbound file and trust',6,'Inbound rules and acknowledgement semantics are separately qualified, not inherited from outbound UBL validation.')
node('RCV-09',3,r+7,'Transform with qualified inbound mapping',6,'Assess DTS as preferred reuse candidate. SPEC-SEI-008 does not qualify the inbound direction.')
node('RCV-10',2,r+8,'Publish one business invoice',6,'Technical acknowledgement follows its proven source milestone; it is separate from product consumption.')
node('RCV-11',1,r+9,'Receive into ERP workflow',6)
node('RCV-12',0,r+10,'Review received invoice',6)
for a,b in [('RCV-01','RCV-02'),('RCV-02','RCV-03'),('RCV-03','RCV-04'),('RCV-04','RCV-07'),('RCV-05','RCV-07'),('RCV-07','RCV-08'),('RCV-08','RCV-09'),('RCV-09','RCV-10'),('RCV-10','RCV-11'),('RCV-11','RCV-12')]:edge(a,b)
edge('RCV-04','RCV-06','access','Independent download')

r = phase('4 · Lifecycle and reporting', 'Later independent events. No acknowledgement, download or ERP receipt implies buyer acceptance.', 8)
node('LIF-01',4,r+1,'Supply delivery or lifecycle evidence',9)
node('LIF-02',2,r+2,'Correlate and preserve source events',9)
node('LIF-03',0,r+3,'Make authorised buyer decision',9)
node('LIF-04',1,r+3,'Record authorised business event',9)
node('LIF-05',2,r+4,'Plan separate reporting obligations',9)
node('LIF-06',4,r+5,'Return each reporting result',9,'Execute only the qualified country and destination obligation; reconcile uncertain results independently.')
node('LIF-07',2,r+6,'Derive evidence-based current view',9)
node('LIF-08',3,r+6,'Expose history and notify consumers',13,'Global API access does not widen customer authority; events can be recovered without replaying business operations.')
node('LIF-09',1,r+7,'Show status and next action',9)
for a,b in [('LIF-01','LIF-02'),('LIF-03','LIF-04'),('LIF-04','LIF-05'),('LIF-05','LIF-06'),('LIF-06','LIF-07'),('LIF-02','LIF-07'),('LIF-07','LIF-08'),('LIF-08','LIF-09')]:edge(a,b)

r = phase('5 · Change route or leave', 'Optional later journey. New traffic and historical obligations are handled separately.', 7)
node('EXT-01',0,r+1,'Request controlled switch or exit',3)
node('EXT-02',2,r+2,'Check new route and earlier obligations',3)
node('EXT-03',3,r+3,'Coordinate qualified cutover and recovery',3)
node('EXT-04',4,r+3,'Confirm required external changes',3)
node('EXT-05',3,r+4,'Export records and preserve evidence',3)
node('EXT-06',0,r+5,'Keep permitted historical access',3)
node('EXT-07',2,r+6,'Close only after continuity checks',3,'Retention, holds, credential release and deletion require their own approved controls.')
for a,b in [('EXT-01','EXT-02'),('EXT-02','EXT-03'),('EXT-03','EXT-04'),('EXT-04','EXT-05'),('EXT-05','EXT-06'),('EXT-06','EXT-07')]:edge(a,b)

MODEL = dict(title='Spain e-invoicing · responsibility overview', lanes=LANES, nodes=NODES, edges=EDGES, phases=PHASES,
             note='Proposed logical responsibilities, not deployment boundaries or verified implementation coverage.')
W, X, CW, RH, TOP, NH = 1420, 30, 272, 132, 176, 88

if __name__ == "__main__":
    import runpy
    runpy.run_path(str(ROOT / "work/build-spain-continuous-horizontal.py"), run_name="__main__")
