"""Build SPEC025's four-stage summary; SPEC026 owns the detailed process.

Run with --render-only to refresh previews after editing the Draw.io source.
"""
from pathlib import Path
import argparse
import importlib.util
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/diagrams/invoice-retrieval-summary-process'
SPEC = '../../specs/invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#'
LIFE = '../../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#review-and-take-action'
GREEN, PURPLE, GREY = '#E6F4F1', '#F0EBFA', '#FAFAFA'
DESCRIPTION = (
    'Four stages: receive and save invoices, view invoice list, select and open invoice, '
    'and choose the next action. Use existing platform connections and current permission. '
    'Public and private sources can both apply; save each file when it arrives. '
    'Original checks and ERP delivery continue separately from permitted saved-file access. '
    'If the original is not saved, resolve its retrieval from an available, permitted '
    'source and repeat the source checks. If retrieval cannot complete, show the next '
    'action and owner. ERP delivery stays pending while safe copy access can continue. '
    'The list includes sent and received invoices and distinguishes an empty list, '
    'incomplete collection and a failed request. Opening does not download or accept '
    'the invoice. Download, review and leaving a decision pending are separate choices. '
    'Buyer actions when only a copy is available remain an open decision in SPEC026. '
    'E markers refer to a shared problem or pending result. Colours group activities; '
    'they do not indicate implementation or readiness.')


def build_source():
    document = ET.Element('mxfile', host='app.diagrams.net', type='device')
    diagram = ET.SubElement(document, 'diagram', id=BASE.name,
                            name='Invoice retrieval — four-stage summary')
    model = ET.SubElement(diagram, 'mxGraphModel', page='1', pageWidth='2400',
                          pageHeight='2060', grid='1', gridSize='10', guides='1',
                          connect='1', arrows='1', tooltips='1')
    root = ET.SubElement(model, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')
    backgrounds, paths, labels = [], [], []

    def vertex(key, value, x, y, w, h, *, style, link=None, background=False):
        if link:
            item = ET.Element('object', id=key, label=value, link=link)
            cell = ET.SubElement(item, 'mxCell', vertex='1', parent='1', style=style)
        else:
            item = cell = ET.Element('mxCell', id=key, value=value, vertex='1', parent='1', style=style)
        ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(w),
                      height=str(h), attrib={'as':'geometry'})
        (backgrounds if background else labels).append(item)

    def text(key, value, x, y, w, h, *, size=19, link=None, align='left'):
        vertex(key,value,x,y,w,h,link=link,style=(
            f'text;html=0;whiteSpace=wrap;align={align};spacing=2;'
            f'fontFamily=Arial;fontSize={size};fontColor=#222222;'))

    def card(key, title, body, x, y, w, h, *, fill, link=None, dashed=False, size=19, title_size=23):
        vertex(key,'',x,y,w,h,link=link,background=True,style=(
            f'rounded=1;arcSize=8;html=0;fillColor={fill};strokeColor=#555555;strokeWidth=1.5;'
            + ('dashed=1;dashPattern=6 4;' if dashed else '')))
        text(key+'-title',title,x+22,y+12,w-44,38,size=title_size,link=link)
        text(key+'-body',body,x+22,y+55,w-44,h-70,size=size,link=link)

    def edge(key, source, target, *, start=(.5,1), end=(.5,0), points=(), dashed=False):
        c=ET.Element('mxCell', id=key, parent='1', edge='1', source=source, target=target,
            style=(f'edgeStyle=none;html=0;endArrow=block;strokeColor=#555555;strokeWidth=1.8;'
                   f'exitX={start[0]};exitY={start[1]};entryX={end[0]};entryY={end[1]};'
                   'exitPerimeter=0;entryPerimeter=0;'
                   + ('dashed=1;dashPattern=6 4;' if dashed else '')))
        g=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
        a=ET.SubElement(g,'Array',attrib={'as':'points'})
        for x,y in points: ET.SubElement(a,'mxPoint',x=str(x),y=str(y))
        paths.append(c)

    text('title','Invoice retrieval: sources, ERP receiving and customer actions',30,18,2340,48,size=30)
    text('subtitle','Four stages. Files are collected automatically; customers can view permitted saved files while ERP delivery continues.',30,76,2340,40,size=19)
    for key,x,fill,caption,w in [
        ('customer',30,GREEN,'Customer actions / ERP',280),
        ('shared',390,PURPLE,'Receiving and checks',270),
        ('notes',750,GREY,'Existing setup / notes',280),
    ]:
        vertex('colour-'+key,'',x,129,16,16,background=True,
               style=f'rounded=0;fillColor={fill};strokeColor=#999999;')
        text('colour-'+key+'-label',caption,x+26,123,w,28,size=16)
    text('colour-meaning','Colours group activities. They do not show whether a function is ready or built.',1200,123,1150,28,size=16)

    for key,title,x,y,w in [
        ('1','1. RECEIVE AND SAVE INVOICES — AUTOMATIC',40,180,2310),
        ('2','2. VIEW INVOICE LIST',210,1090,500),
        ('3','3. SELECT AND OPEN INVOICE',900,1090,470),
        ('4','4. CHOOSE THE NEXT ACTION',1470,1090,880),
    ]:
        vertex('stage-band-'+key,title,x,y,w,42,background=True,
               style='rounded=1;arcSize=5;html=0;whiteSpace=wrap;align=center;spacing=8;fontSize=20;fillColor=#eeeeee;strokeColor=none;')

    card('onboarding-setup','Use existing platform connections',
         'Use the selected business’s connected platforms.\nCheck current receiving, viewing and download permission.',
         40,260,700,130,fill=GREY,link=SPEC+'retrieval-setup-context',size=19,title_size=23)
    text('source-scope','Both sources can apply.',260,410,270,30,size=18)
    card('public-source','Public platform',
         'Get the available invoice files.',
         60,460,300,140,fill=PURPLE,link=SPEC+'choose-source-and-get-invoice',size=18,title_size=22)
    card('private-source','Private platform',
         'Use supplied files.\nFetch missing files when needed.',
         440,460,300,140,fill=PURPLE,link=SPEC+'choose-source-and-get-invoice',size=18,title_size=22)
    card('stage-1','Save each invoice file',
         'Keep the file unchanged.\nKeep its source and label.\nCheck recipient and safety.',
         240,680,420,140,fill=PURPLE,link=SPEC+'31-source-acquisition-and-stored-file-access',size=18)
    text('capture-condition','Process each file when it arrives.',750,620,500,30,size=18)
    vertex('original-available','Is the original\nalready saved?',900,675,300,150,
           link=SPEC+'34-process-review-proposal',background=True,
           style=f'shape=rhombus;html=0;whiteSpace=wrap;align=center;spacing=10;fontSize=21;fillColor={PURPLE};strokeColor=#555555;strokeWidth=1.5;')
    text('erp-work-label','ERP receiving — continues separately',1320,610,910,30,size=19)
    card('prepare-original','Check the original',
         'Check invoice format and rules.\nPrepare the invoice for delivery.',
         1320,680,360,140,fill=PURPLE,link=SPEC+'32-receiving-handoff',size=18,title_size=22)
    card('erp-delivery','Deliver to the ERP',
         'Confirm ERP receipt.\nKeep one invoice if delivery repeats.',
         1810,680,420,140,fill=PURPLE,link=SPEC+'32-receiving-handoff',size=19,title_size=22)
    card('original-pending','Resolve original-file retrieval',
         'Use an available, permitted source.\nSave returned file; repeat checks.\nIf blocked, show next action and owner.\nKeep ERP delivery pending.',
         850,910,400,160,fill=PURPLE,link=SPEC+'original-file-retrieval',size=18,title_size=22,dashed=True)
    card('separate-results','Keep results separate',
         'Saving a file is separate from ERP receipt.\nERP receipt is separate from buyer acceptance.\nSafe copy viewing and download can continue.',
         1480,900,750,140,fill=GREY,link=SPEC+'32-receiving-handoff',size=18,title_size=22)

    edge('setup-public','onboarding-setup','public-source',start=(.25,1),points=[(215,430),(210,430)])
    edge('setup-private','onboarding-setup','private-source',start=(.75,1),points=[(565,430),(590,430)])
    edge('public-capture','public-source','stage-1',points=[(210,645),(450,645)])
    edge('private-capture','private-source','stage-1',points=[(590,645),(450,645)])
    edge('classify-file','stage-1','original-available',start=(1,.5),end=(0,.5))
    edge('original-ready','original-available','prepare-original',start=(1,.5),end=(0,.5))
    text('original-yes','Yes',1230,709,70,26,size=17)
    edge('checked-for-delivery','prepare-original','erp-delivery',start=(1,.5),end=(0,.5))
    edge('original-missing','original-available','original-pending',dashed=True)
    text('original-no','No',1070,851,70,26,size=17)
    edge('original-obtained-return','original-pending','stage-1',start=(0,.5),end=(.8,1),points=[(820,990),(820,850),(576,850)],dashed=True)
    text('original-return-label','File returned\nRepeat intake checks',580,855,235,48,size=15,link=SPEC+'original-file-retrieval')

    card('stage-2','View invoice list',
         'Choose the business or client.\nShow sent and received invoices.',
         240,1170,420,140,fill=GREEN,link=SPEC+'customer-list-open-and-download')
    card('stage-3','Select and open invoice',
         'Open one invoice. Show its details,\nstatus, history and file labels.',
         920,1170,420,140,fill=GREEN,link=SPEC+'customer-list-open-and-download',title_size=22)
    vertex('stage-4','Choose the\nnext action',1640,1165,320,150,
           link=SPEC+'customer-list-open-and-download',background=True,
           style=f'shape=rhombus;html=0;whiteSpace=wrap;align=center;spacing=10;fontSize=22;fillColor={GREEN};strokeColor=#555555;strokeWidth=1.5;')
    card('download-choice','Download file',
         'Choose a labelled file.\nCheck access and safety.\nReturn the file or a clear problem.',
         1390,1450,280,160,fill=GREEN,link=SPEC+'customer-list-open-and-download',size=17,title_size=21)
    card('review-choice','Review and take action',
         'Offer allowed actions.\nSave the decision and show\nits reporting results.\nContinue in SPEC029.',
         1730,1450,300,160,fill=GREEN,link=LIFE,size=17,title_size=21)
    card('pending-choice','Leave pending',
         'Make no decision now.\nKeep required work\nand deadlines visible.',
         2090,1450,260,160,fill=GREEN,link=LIFE,size=17,title_size=21)
    edge('safe-files-to-list','stage-1','stage-2',end=(0,.5),points=[(450,1060),(180,1060),(180,1240)],dashed=True)
    text('safe-access-condition','After access and safety checks,\nsaved files are available to users.',485,1005,380,70,size=18)
    edge('list-to-open','stage-2','stage-3',start=(1,.5),end=(0,.5))
    edge('open-to-choice','stage-3','stage-4',start=(1,.5),end=(0,.5))
    edge('download-selected','stage-4','download-choice',points=[(1800,1370),(1530,1370)],dashed=True)
    edge('review-selected','stage-4','review-choice',points=[(1800,1370),(1880,1370)],dashed=True)
    edge('decision-deferred','stage-4','pending-choice',start=(1,.5),points=[(2220,1240)],dashed=True)

    text('list-outcomes','Users can open the list while collection is pending.\nEmpty list: show no results.\nCollection incomplete: show pending work.\nRequest failed: show the problem.',240,1380,460,120,size=18)
    text('open-outcomes','Opening does not download the file\nor accept the invoice.\nKeep unavailable content visible.',920,1380,420,100,size=18)
    text('choice-rule','Download is optional and is not required before review.\nBuyer actions when only a copy is available: decision open (SPEC026 §3.4).',1390,1650,960,56,size=18)

    card('shared-exception','E · Problem or pending result',
         'Show the reason, next action and who must act.\n'
         'Keep successful results. Retry only the affected step.\n'
         'If the result is unknown, check what happened before trying again.',
         40,1625,1220,160,fill=GREEN,link=SPEC+'33-failure-and-recovery-decisions',dashed=True,size=18)
    for key,x,y,start in [
        ('public-source',390,514,(1,.5)),('private-source',780,514,(1,.5)),
        ('stage-1',700,699,(1,.25)),('prepare-original',1720,699,(1,.25)),
        ('erp-delivery',2270,699,(1,.25)),
        ('stage-2',434,1330,(.5,1)),('stage-3',1114,1330,(.5,1)),
        ('download-choice',1690,1474,(1,.25)),('review-choice',2050,1474,(1,.25)),
        ('pending-choice',2360,1474,(1,.25)),
    ]:
        vertex('exception-'+key,'E',x,y,32,32,link=SPEC+'33-failure-and-recovery-decisions',
               style=f'rounded=1;arcSize=100;html=0;align=center;spacing=0;fontSize=16;fillColor={GREEN};strokeColor=#555555;')
        edge('error-'+key,key,'exception-'+key,start=start,end=(.5,0) if start==(.5,1) else (0,.5),dashed=True)
    text('exception-meaning','All E markers use the same exception result.',40,1792,1220,28,size=16)
    text('scope-note','Stage 1 is inbound only. The list also includes sent invoices. Customer access does not wait for ERP delivery.',40,1830,2310,30,size=17)
    text('line-legend','Solid: process steps and handoffs. Dashed: saved-file availability, conditional choices or exception references. Stage numbers are not delivery phases. Detailed rules: SPEC026.',40,1866,2310,28,size=15,link=SPEC+'retrieval-detailed-process')
    root.extend(backgrounds); root.extend(paths); root.extend(labels)
    ET.indent(document,space='  ')
    BASE.with_suffix('.drawio').write_text(ET.tostring(document,encoding='unicode',xml_declaration=True)+'\n')


def build(render_only=False):
    if not render_only:
        build_source()
    spec=importlib.util.spec_from_file_location('retrieval_preview',ROOT/'work/build-invoice-retrieval-overview.py')
    renderer=importlib.util.module_from_spec(spec); spec.loader.exec_module(renderer)
    return renderer.build(BASE,description=DESCRIPTION)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--render-only',action='store_true')
    print(build(parser.parse_args().render_only))
