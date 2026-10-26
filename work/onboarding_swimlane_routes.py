"""Arrow placement only: retain all SPEC038 nodes, lanes and directed connections."""
import copy
import math
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/2000/svg}'

def layout(slug, nodes, edges):
    name = slug.removeprefix('onboarding-logical-').removesuffix('-process')
    columns = {
        'public-setup': {'external':1,'record':2,'recover':3,'case':3,'result':4},
        'private-setup': {'external':1,'change':2,'activate':3,'recover':3,'case':4,'result':5},
        'approval': {'recover':5,'resume':6,'result':6},
        'batch': {'recover':5,'result':6},
    }[name]
    positions = {n['key']:(240+columns.get(n['key'],n['col'])*295,178+n['lane']*140,260,104) for n in nodes}
    # Each pair has its own route. Keep labels away from both nodes and lines.
    routes = {
      'public-setup': {
        ('plan','checks'): ([(500,510),(517,510),(517,650),(535,650)],None),
        ('checks','external'): ([(625,702),(625,878)],(500,790)),
        ('external','record'): ([(795,930),(810,930),(810,510),(830,510)],(825,925)),
        ('record','result'): ([(960,458),(960,370),(1420,370)],None),
        ('checks','correct'): ([(665,598),(665,282)],(680,385)),
        ('correct','checks'): ([(625,282),(625,598)],(540,420)),
        ('correct','record'): ([(795,230),(1000,230),(1000,458)],(840,215)),
        ('checks','recover'): ([(705,598),(705,440),(1255,440),(1255,458)],(1010,425)),
        ('external','recover'): ([(795,955),(1100,955),(1100,550),(1125,550)],(860,980)),
        ('recover','plan'): ([(1125,485),(1115,485),(1115,575),(370,575),(370,562)],(800,590)),
        ('recover','record'): ([(1125,520),(1090,520)],(1125,450)),
        ('recover','case'): ([(1255,562),(1255,738)],(1270,685)),
        ('case','record'): ([(1255,842),(1255,860),(960,860),(960,562)],(980,885)),
      },
      'private-setup': {
        ('plan','setup'): ([(500,510),(517,510),(517,650),(535,650)],None),
        ('setup','external'): ([(625,702),(625,878)],(500,790)),
        ('external','setup'): ([(705,878),(705,702)],(720,825)),
        ('setup','change'): ([(795,650),(810,650),(810,510),(830,510)],(835,635)),
        ('change','activate'): ([(1090,510),(1110,510),(1110,650),(1125,650)],(850,600)),
        ('change','result'): ([(960,458),(960,300),(1805,300),(1805,318)],(1340,285)),
        ('activate','result'): ([(1385,650),(1885,650),(1885,422)],None),
        ('setup','correct'): ([(665,598),(665,282)],(680,385)),
        ('correct','setup'): ([(625,282),(625,598)],(540,420)),
        ('correct','result'): ([(795,230),(1885,230),(1885,318)],(1240,215)),
        ('setup','recover'): ([(795,675),(1100,675),(1100,535),(1125,535)],(840,700)),
        ('external','recover'): ([(795,930),(1080,930),(1080,575),(1225,575),(1225,562)],(835,955)),
        ('activate','recover'): ([(1285,598),(1285,562)],(1300,585)),
        ('recover','plan'): ([(1125,485),(1115,485),(1115,430),(370,430),(370,458)],(750,420)),
        ('recover','result'): ([(1255,458),(1255,370),(1715,370)],(1300,355)),
        ('recover','case'): ([(1385,535),(1405,535),(1405,790),(1420,790)],(1425,705)),
        ('case','result'): ([(1680,790),(2010,790),(2010,395),(1975,395)],(1750,815)),
      },
      'approval': {
        ('evidence','request'): ([(500,650),(515,650),(515,510),(535,510)],(535,590)),
        ('evidence','resume'): ([(370,702),(370,735),(2290,735),(2290,510),(2270,510)],(1030,760)),
        ('request','present'): ([(795,510),(810,510),(810,370),(830,370)],None),
        ('present','respond'): ([(1090,370),(1105,370),(1105,230),(1125,230)],None),
        ('respond','verify'): ([(1385,230),(1400,230),(1400,650),(1420,650)],None),
        ('present','result'): ([(960,318),(960,300),(2180,300),(2180,318)],(1600,285)),
        ('verify','resume'): ([(1680,650),(1990,650),(1990,510),(2010,510)],(1890,635)),
        ('verify','result'): ([(1550,702),(1550,775),(2310,775),(2310,370),(2270,370)],(1700,795)),
        ('resume','result'): ([(2140,458),(2140,422)],None),
        ('result','request'): ([(2010,345),(1995,345),(1995,165),(665,165),(665,458)],(800,190)),
        ('withdraw','recover'): ([(1385,510),(1715,510)],None),
        ('recover','result'): ([(1975,535),(1980,535),(1980,395),(2010,395)],None),
      },
      'batch': {
        ('submit','validate'): ([(370,282),(370,315),(530,315),(530,510),(535,510)],None),
        ('validate','reject'): ([(665,458),(665,422)],(680,445)),
        ('validate','receipt'): ([(795,510),(830,510)],(795,495)),
        ('receipt','access'): ([(1090,510),(1105,510),(1105,650),(1125,650)],None),
        ('access','run'): ([(1385,650),(1400,650),(1400,510),(1420,510)],(1420,610)),
        ('access','result'): ([(1255,702),(1255,710),(1415,710),(1415,370),(2010,370)],(1720,355)),
        ('run','result'): ([(1680,510),(1990,510),(1990,345),(2010,345)],None),
        ('changes','access'): ([(1255,282),(1255,598)],(1270,430)),
        ('changes','hold'): ([(1125,230),(510,230),(510,430),(370,430),(370,458)],(730,215)),
        ('hold','result'): ([(370,562),(370,880),(2160,880),(2160,422)],(1440,905)),
        ('hold','recover'): ([(500,535),(515,535),(515,720),(1695,720),(1695,650),(1715,650)],(1180,745)),
        ('recover','result'): ([(1845,598),(1845,410),(2010,410)],(1780,770)),
      },
    }[name]
    assert set(routes)=={(e['source'],e['target']) for e in edges}
    kinds={n['key']:n['kind'] for n in nodes}
    def boundary(point,key):
        # Attach to the visible curve, including the capsule-shaped outcomes.
        x,y,w,h=positions[key]
        px,py=point
        if kinds[key]=='decision':return point
        radius=42 if kinds[key]=='outcome' else 8
        if px in {x,x+w} and not y+radius<=py<=y+h-radius:
            cy=y+radius if py<y+radius else y+h-radius
            inset=radius-math.sqrt(max(0,radius**2-(py-cy)**2))
            px=x+inset if px==x else x+w-inset
        if py in {y,y+h} and not x+radius<=px<=x+w-radius:
            cx=x+radius if px<x+radius else x+w-radius
            inset=radius-math.sqrt(max(0,radius**2-(px-cx)**2))
            py=y+inset if py==y else y+h-inset
        return px,py
    for e in edges:
        points,label_pos=routes[e['source'],e['target']]
        points[0]=boundary(points[0],e['source'])
        points[-1]=boundary(points[-1],e['target'])
        assert all(a[0]==b[0] or a[1]==b[1] for a,b in zip(points,points[1:]))
        e['points']=points
        if label_pos is not None:e['label_pos']=label_pos
        if name=='public-setup' and (e['source'],e['target'])==('recover','record'):
            e['label']=''  # The adjacent target already says "Save public check results".
    return positions,{'public-setup':1740,'private-setup':2040,'approval':2340,'batch':2340}[name]

def rounded(points,radius=7):
    commands=[f'M {points[0][0]},{points[0][1]}']
    for before,corner,after in zip(points,points[1:],points[2:]):
        incoming=math.dist(before,corner);outgoing=math.dist(corner,after)
        r=min(radius,incoming/2,outgoing/2)
        if not r:continue
        a=tuple(c+(b-c)*r/incoming for b,c in zip(before,corner))
        b=tuple(c+(v-c)*r/outgoing for c,v in zip(corner,after))
        commands.append(f'L {a[0]:g},{a[1]:g} Q {corner[0]},{corner[1]} {b[0]:g},{b[1]:g}')
    commands.append(f'L {points[-1][0]},{points[-1][1]}')
    return ' '.join(commands)

def finish(path,edges):
    """Use rounded turns and white crossing gaps, with matching editable edge styles."""
    ET.register_namespace('',NS[1:-1])
    svg=ET.parse(path).getroot()
    connectors=[e for e in svg if e.tag in {'path',NS+'path'} and e.get('fill')=='none']
    arrowheads=[e for e in svg if e.tag in {'path',NS+'path'} and e.get('fill')=='#555555']
    assert len(connectors)==len(edges)
    assert len(arrowheads)==len(edges)
    ns=NS if svg.tag.startswith(NS) else ''
    for connector,head,edge in zip(connectors,arrowheads,edges):
        connector.set('d',rounded(edge['points']))
        color='#444444' if edge['kind']=='flow' else '#777777'
        connector.set('stroke',color)
        connector.set('stroke-width','2.4' if edge['kind']=='flow' else '1.5')
        head.set('fill',color)
        connector.set('stroke-linejoin','round')
        connector.set('data-connection',edge['source']+'→'+edge['target'])
        # A narrow white outline keeps crossed arrows visually separate.
        halo=copy.deepcopy(connector)
        halo.set('stroke','white');halo.set('stroke-width','6')
        halo.attrib.pop('stroke-dasharray',None)
        halo.attrib.pop('data-connection',None)
        halo.set('data-crossing-gap','true')
        svg.insert(list(svg).index(connector),halo)
    for edge in edges:
        if not edge['label']:continue
        x,y=edge['label_pos']
        text=next(e for e in svg if e.tag==ns+'text' and e.text==edge['label'] and float(e.get('x'))==x and float(e.get('y'))==y)
        background=ET.Element(ns+'rect',x=str(x-4),y=str(y-14),width=str(len(edge['label'])*6.9+8),height='19',rx='3',fill='white',attrib={'data-arrow-label':'true'})
        svg.insert(list(svg).index(text),background)
    for e in svg:
        if e.tag==ns+'text' and (e.text or '').startswith('Proposed design ·'):
            e.text+=' · Crossed lines do not join'
    path.write_text(ET.tostring(svg,encoding='unicode'))
    native=ET.parse(path.with_suffix('.drawio')).getroot()
    for e in native.iter('mxCell'):
        if e.get('edge')=='1':
            edge=edges[int(e.get('id').removeprefix('edge-'))]
            color='#444444' if edge['kind']=='flow' else '#777777'
            width='2.4' if edge['kind']=='flow' else '1.5'
            e.set('style',e.get('style')+f'rounded=1;arcSize=7;jumpStyle=arc;jumpSize=7;strokeColor={color};strokeWidth={width};')
        if e.get('id','').startswith('edge-label-'):
            e.set('style',e.get('style')+'fillColor=#ffffff;spacingLeft=4;')
        if e.get('id')=='legend':e.set('value',e.get('value')+' · Crossed lines do not join')
    ET.indent(native)
    path.with_suffix('.drawio').write_text(ET.tostring(native,encoding='unicode',xml_declaration=True))
