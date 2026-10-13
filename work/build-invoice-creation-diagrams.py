"""Build only SPEC-SEI-015 diagrams; render and check previews without network."""
from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG = '{http://www.w3.org/2000/svg}'
helper_spec = importlib.util.spec_from_file_location(
    'creation_diagram_helper', ROOT / 'work/build-shared-platform-connectivity-diagrams.py')
helper = importlib.util.module_from_spec(helper_spec)
helper_spec.loader.exec_module(helper)
helper.WIDTH = 2670
helper.SPEC = '../../specs/SPEC-SEI-015-invoice-creation-solution-specification.md'
helper.LANES = helper.LANES[:5]
N = helper.node


def edge(source, target, label='', conditional=False):
    return dict(source=source, target=target,
                kind='conditional' if conditional else 'flow', label=label)


def clean_paths(slug, pos, edges):
    """Use distinct ports and whitespace tracks for branch/recovery paths."""
    overrides = {}
    labels = {}
    if slug.endswith('preparation-process'):
        overrides = {
            ('valid','generate'): [(1550,540),(1550,591)],
            ('valid','output'): [(1550,540),(1550,558),(1845,558),(1845,591)],
            ('result','edit'): [(2010,498),(1990,498),(1990,420),(1402,420),(1402,363),(1385,363)],
            ('generate','recover'): [(1550,675),(1550,726)],
            ('recover','generate'): [(1420,768),(1404,768),(1404,633),(1420,633)],
            ('handoff','send_recover'): [(2435,540),(2435,726)],
            ('send_recover','handoff'): [(2305,768),(2287,768),(2287,520),(2305,520)],
        }
        labels = {('valid','generate'):(1550,580), ('valid','output'):(1700,551),
                  ('recover','generate'):(1404,702),
                  ('send_recover','handoff'):(2287,702)}
    else:
        overrides = {
            ('issued','scenario'): [(665,456),(665,228),(830,228)],
            ('issued','draft'): [(795,498),(812,498),(812,363),(830,363)],
            ('simplified','replace'): [(1385,228),(1402,228),(1402,363),(1420,363)],
            ('simplified','corrective'): [(1255,270),(1255,294),(1106,294),(1106,430),(960,430),(960,456)],
            ('method','substitute'): [(1255,540),(1255,633),(1420,633)],
            ('replace','references'): [(1680,363),(1698,363),(1698,475),(1715,475)],
            ('difference','references'): [(1680,498),(1715,498)],
            ('substitute','references'): [(1680,633),(1698,633),(1698,522),(1715,522)],
            ('draft','validate'): [(960,405),(960,420),(2590,420),(2590,696),(2140,696),(2140,675)],
            ('references','validate'): [(1975,498),(1992,498),(1992,633),(2010,633)],
            ('validate','result'): [(2270,633),(2435,633),(2435,540)],
            ('issue','handoff'): [(2305,363),(2287,363),(2287,498),(2270,498)],
        }
        labels = {('issued','draft'):(812,443),('issued','scenario'):(665,337),
                  ('simplified','replace'):(1402,295),
                  ('simplified','corrective'):(1175,287)}
    return [overrides.get((v['source'],v['target']),helper.route(v,pos)) for v in edges],labels


def build(slug, title, description, nodes, edges, decisions, footer):
    helper.build(slug, title, description, nodes, edges)
    path = ROOT / 'assets/diagrams' / (slug+'.svg')
    svg = ET.parse(path)
    root = svg.getroot()
    # Remove the generic helper's route-specific footer and replace it.
    for t in list(root.findall(SVG+'text')):
        if float(t.get('y', '0')) >= 1000:
            root.remove(t)
    for i, line in enumerate(footer):
        ET.SubElement(root, SVG+'text', {'x': '28', 'y': str(1002+i*24),
                      'font-family': 'Arial, sans-serif', 'font-size': '15',
                      'fill': '#222222'}).text = line
    pos = {v['key']: (240+v['col']*295, 186+v['lane']*135, 260, 84) for v in nodes}
    paths, label_positions = clean_paths(slug,pos,edges)
    arrow_paths = [v for v in root.findall(SVG+'path') if v.get('stroke')]
    arrow_heads = [v for v in root.findall(SVG+'path') if not v.get('stroke')]
    for ed, points, line, head in zip(edges,paths,arrow_paths,arrow_heads):
        line.set('d','M '+' L '.join(f'{x:g},{y:g}' for x,y in points))
        a,b=points[-2:]; dx,dy=b[0]-a[0],b[1]-a[1]; length=(dx*dx+dy*dy)**.5
        ux,uy=dx/length,dy/length
        head.set('d',f'M {b[0]},{b[1]} L {b[0]-8*ux+4*uy},{b[1]-8*uy-4*ux} L {b[0]-8*ux-4*uy},{b[1]-8*uy+4*ux} Z')
    groups = root.findall(SVG+'a')
    for v, group in zip(nodes, groups):
        if v['key'] not in decisions:
            continue
        x, y, w, h = pos[v['key']]
        rect = group.find(SVG+'rect')
        group.remove(rect)
        group.insert(1, ET.Element(SVG+'path', {
            'd': f'M {x+w/2},{y} L {x+w},{y+h/2} L {x+w/2},{y+h} L {x},{y+h/2} Z',
            'fill': '#f0f0f0', 'stroke': '#333333', 'stroke-width': '1.5'}))
        texts = group.findall(SVG+'text')
        for i, t in enumerate(texts[:-1]):
            t.set('y', str(y+38+i*18))
        texts[-1].set('y', str(y+59))
    # Short branch labels sit on whitespace segments, with a white backdrop.
    for ed,points in zip(edges,paths):
        if not ed['label']:
            continue
        pairs = list(zip(points, points[1:]))
        a, b = max(pairs, key=lambda pair: abs(pair[1][0]-pair[0][0]) + abs(pair[1][1]-pair[0][1]))
        x, y = (a[0]+b[0])/2, (a[1]+b[1])/2-6
        x,y=label_positions.get((ed['source'],ed['target']),(x,y))
        w = max(36, len(ed['label'])*8+14)
        ET.SubElement(root, SVG+'rect', {'x': str(x-w/2), 'y': str(y-14),
                      'width': str(w), 'height': '20', 'fill': 'white'})
        ET.SubElement(root, SVG+'text', {'x': str(x), 'y': str(y),
                      'font-family': 'Arial, sans-serif', 'font-size': '14',
                      'fill': '#222222', 'text-anchor': 'middle'}).text = ed['label']
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    svg.write(path, encoding='unicode')
    draw = ET.parse(path.with_suffix('.drawio'))
    for obj in draw.findall('.//object'):
        if obj.get('id') in decisions:
            c = obj.find('mxCell')
            c.set('style', c.get('style').replace('rounded=1;', 'rhombus;'))
    for i,(ed,points) in enumerate(zip(edges,paths)):
        c=draw.find(f'.//mxCell[@id="edge-{i}"]')
        c.set('value',ed['label'])
        sx,sy,sw,sh=pos[ed['source']];tx,ty,tw,th=pos[ed['target']]
        c.set('style',f'edgeStyle=none;endArrow=block;strokeColor=#555555;exitX={(points[0][0]-sx)/sw};exitY={(points[0][1]-sy)/sh};entryX={(points[-1][0]-tx)/tw};entryY={(points[-1][1]-ty)/th};fontSize=14;labelBackgroundColor=#ffffff;'+('dashed=1;' if ed['kind']!='flow' else ''))
        arr=c.find('./mxGeometry/Array')
        arr.clear();arr.set('as','points')
        for x,y in points[1:-1]:ET.SubElement(arr,'mxPoint',{'x':str(x),'y':str(y)})
    draw.find('.//mxCell[@id="boundary"]').set('value', '\n'.join(footer))
    ET.indent(draw)
    draw.write(path.with_suffix('.drawio'), encoding='unicode', xml_declaration=True)
    return path


def build_all():
    p = build('invoice-creation-preparation-process',
      'Prepare invoice data, generate UBL and hand off the final candidate',
      'Check the business scenario and exact profile. Return issues or a checked representation. ERP issuance and sending remain separate.', [
        N('scenario',0,0,'Select the business scenario','IC-04'),
        N('source',0,1,'Submit an invoice revision','IC-01'),
        N('authority',1,2,'Check business authority and issuer roles','IC-02'),
        N('bundle',2,3,'Select qualified mapper and rules','IC-03'),
        N('checks',3,2,'Check type, links, identity and amounts','IC-04–06'),
        N('valid',4,2,'Checks pass?','IC-06'),
        N('generate',4,3,'Generate a separate UBL file','IC-07'),
        N('output',5,3,'Validate exact bytes and business meaning','IC-08'),
        N('result',6,2,'Save and return result and next action','IC-09'),
        N('issue',6,1,'Review the final candidate in ERP','IC-10'),
        N('handoff',7,2,'Hand final candidate to Sending','IC-10'),
        N('recover',4,4,'Read original task; resume only pending work','IC-11',kind='recovery'),
        N('send_recover',7,4,'Read original Sending receipt; resume owned work','IC-11',kind='recovery'),
        N('edit',3,1,'Correct the draft in a new revision','IC-12'),
      ], [
        edge('scenario','source'),edge('source','authority'),edge('authority','bundle'),
        edge('bundle','checks'),edge('checks','valid'),edge('valid','generate','Facts pass'),
        edge('valid','output','UBL passes',True),edge('valid','result','No',True),
        edge('generate','output'),edge('output','result'),
        edge('result','issue','Eligible',True),edge('issue','handoff'),
        edge('result','edit','Issues',True),edge('edit','source','',True),
        edge('generate','recover','Unknown',True),edge('recover','generate','Resume',True),
        edge('handoff','send_recover','Unknown',True),edge('send_recover','handoff','Resume',True),
      ], {'valid'}, [
        'Prebuilt UBL bypasses generation. Changed final data returns to IC-03–09. Missing authority or profile evidence blocks.',
        'ERP owns issuance. Sending qualifies the final plan before the Article 4 issue/copy boundary; bind actual issue proof.',
        'SPEC-SEI-015 · Reconcile before resume. Return existing completed results; never repeat completed generation or sending.'])
    q = build('invoice-creation-correction-process',
      'Prepare a correction or replacement and preserve the original invoice',
      'Draft edits create revisions. Issued corrections and replacements create a separate invoice. Seller and buyer keep their normal fields.', [
        N('change',0,1,'Request a change to invoice facts','IC-12'),
        N('issued',1,2,'Issued?','IC-12'),
        N('draft',2,1,'Edit a linked draft revision','IC-12'),
        N('scenario',2,0,'Choose the authorised new-invoice scenario','IC-04'),
        N('simplified',3,0,'Replace simplified?','IC-04'),
        N('replace',4,1,'Prepare type 388 with full values','IC-04/05'),
        N('corrective',2,2,'Confirm 384 or 471, reason and authority','IC-02/04'),
        N('method',3,2,'I or S?','IC-04'),
        N('difference',4,2,'Check difference values as deltas','IC-06'),
        N('substitute',4,3,'Check full values and original amounts','IC-06'),
        N('references',5,2,'Check original links and invoice identity','IC-05'),
        N('validate',6,3,'Generate and validate the new revision','IC-03–08'),
        N('result',7,2,'Return issues or checked evidence','IC-09'),
        N('issue',7,1,'Review the new candidate in ERP','IC-10'),
        N('handoff',6,2,'Hand final candidate to Sending','IC-10'),
        N('recover',5,4,'Resolve evidence; repeat IC-05 only when safe','IC-11',kind='recovery'),
      ], [
        edge('change','issued'),edge('issued','draft','No'),
        edge('draft','validate','',True),edge('issued','scenario','Yes'),
        edge('scenario','simplified'),edge('simplified','replace','Yes'),
        edge('simplified','corrective','No'),edge('corrective','method'),
        edge('method','difference','I'),edge('method','substitute','S'),
        edge('replace','references'),edge('difference','references'),
        edge('substitute','references'),edge('references','validate'),
        edge('references','recover','Unproven',True),
        edge('validate','result'),edge('result','issue','Eligible',True),
        edge('issue','handoff'),
      ], {'issued','simplified','method'}, [
        '388 replaces simplified invoices. S is a corrective substitution. These are different scenarios.',
        '384/471 use qualified BG-24 and BT-ES-27/28/29. Third-party BG-ES-1 is a separate condition.',
        'SPEC-SEI-015 · Sending coordinates required copy with ERP issuance. Original data stays unchanged; actual coordination remains gated.'])
    return [p,q]


def render(paths):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width':helper.WIDTH,'height':helper.HEIGHT},device_scale_factor=1)
        page.route('http://**/*',lambda route:route.abort())
        page.route('https://**/*',lambda route:route.abort())
        for path in paths:
            ET.parse(path)
            ET.parse(path.with_suffix('.drawio'))
            page.goto(path.as_uri())
            failures=page.evaluate('''() => {
              const s=document.querySelector('svg'),v=s.viewBox.baseVal;
              return Array.from(s.querySelectorAll('text')).flatMap(t=>{
                const b=t.getBBox();
                if(b.x<0||b.y<0||b.x+b.width>v.width||b.y+b.height>v.height)return[t.textContent];
                const a=t.closest('a'); if(!a)return[];
                const box=a.querySelector('rect,path').getBBox();
                return b.x<box.x+2||b.x+b.width>box.x+box.width-2||b.y<box.y+2||b.y+b.height>box.y+box.height-2?[t.textContent]:[];
              });}''')
            assert not failures,(path.name,failures)
            page.locator('svg').screenshot(path=str(path.with_suffix('.png')))
            page.set_viewport_size({'width':480,'height':800})
            page.goto('about:blank')
            page.set_content('<div style="overflow-x:auto">'+path.read_text()+'</div>')
            assert page.locator('div').evaluate('(e)=>e.scrollWidth>e.clientWidth')
            page.set_viewport_size({'width':helper.WIDTH,'height':helper.HEIGHT})
            print(path.stem+': XML valid, text fits, PNG rendered, narrow view scrolls')
        browser.close()


if __name__=='__main__':
    render(build_all())
