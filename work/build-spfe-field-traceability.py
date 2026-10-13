"""Record every supplied BOE annex field row without inventing wire mappings.

The ledger preserves the original Spanish cells and XML row locator. English
names and logical tests support review. All wire bindings still require the
selected business schemas, country rules and implementation evidence.
"""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'assets/regulatory/spain/BOE-A-2026-20587.xml'
OUT = ROOT / 'assets/regulatory/spain/spfe/field-traceability.json'

BT = {
1:'Invoice series and number',2:'Invoice issue date',3:'Invoice type code',5:'Invoice currency',
6:'VAT accounting currency',7:'Operation date',9:'Payment due date',10:'Buyer reference',
20:'Payment terms description',21:'Invoice note code',22:'Invoice note',23:'Business process identifier',
24:'Specification identifier',25:'Previous invoice series and number',26:'Previous invoice issue date',
27:'Seller name',30:'Seller legal registration identifier',31:'Seller VAT identifier',32:'Seller tax identifier',
33:'Seller legal information',35:'Seller address',37:'Seller municipality',38:'Seller postal code',
39:'Seller province',40:'Seller country code',42:'Seller contact telephone',43:'Seller contact email',
44:'Buyer name',47:'Buyer tax identifier',48:'Buyer VAT identifier',50:'Buyer address',
52:'Buyer municipality',53:'Buyer postal code',54:'Buyer province',55:'Buyer country code',
57:'Buyer contact telephone',58:'Buyer contact email',73:'Billing period start',74:'Billing period end',
81:'Payment means code',84:'Payment account identifier',92:'Document allowance amount',
95:'Document allowance VAT category',96:'Document allowance VAT rate',97:'Document allowance reason',
99:'Document charge amount',102:'Document charge VAT category',103:'Document charge VAT rate',
104:'Document charge reason',106:'Sum of invoice line net amounts',107:'Sum of document allowances',
108:'Sum of document charges',109:'Invoice total excluding VAT',110:'Invoice VAT total',
111:'VAT total in accounting currency',112:'Invoice total including VAT',113:'Paid amount',
114:'Rounding amount',115:'Amount due',116:'Taxable amount by VAT category',117:'Tax amount by VAT category',
118:'VAT category code',119:'VAT category rate',120:'VAT exemption reason',121:'VAT exemption code',
122:'Supporting document reference identifier',123:'Supporting document description/value',
126:'Invoice line identifier',129:'Invoiced quantity',130:'Quantity unit code',131:'Invoice line net amount',
136:'Line allowance amount',139:'Line allowance reason',141:'Line charge amount',142:'Line charge base',
143:'Line charge rate',144:'Line charge reason',146:'Item net price',149:'Item price base quantity',
151:'Item VAT category',152:'Item VAT rate',153:'Item name',154:'Item description',
160:'Additional property code',161:'Additional property value',166:'Invoice issue time',
167:'VAT accounting exchange rate',179:'Context-specific collection/deduction amount',
180:'Context-specific collection/deduction description',195:'Item VAT exemption code',
}
ES = {
1:'Public-copy indicator',2:'Effective payment date',3:'Third-party name',4:'Third-party NIF',
5:'Third-party role code',6:'Document tax/fee base',7:'Document tax/fee rate',8:'Document tax/fee amount',
9:'Document non-VAT tax/fee code',10:'Third-party charge identifier',11:'Tax/fee identifier',
12:'Third-party tax/fee base',13:'Third-party tax/fee rate',14:'Third-party tax/fee total',
15:'Third-party deduction identifier',16:'Withholding identifier',17:'Total withholding',
18:'Withholding base',19:'Withholding amount',20:'Withholding rate',21:'Withholding concept code',
22:'Line non-VAT tax/fee code',23:'Property location code',24:'National tax qualifier',
25:'Fiscal QR URL reference',26:'Billing authorization reference',27:'Corrective invoice reason code',
28:'Corrective invoice method code',29:'Rectified original amount code',
}
BG = {
1:'Invoice notes',2:'Process control',3:'Previous invoice references',4:'Seller',5:'Seller address',
6:'Seller contact',7:'Buyer',8:'Buyer address',9:'Buyer contact',14:'Summary-invoice period',
16:'Payment instructions',17:'Bank transfer',20:'Document allowances',21:'Document charges',
22:'Invoice totals',23:'VAT breakdown',24:'Context-specific supporting references',25:'Invoice lines',
27:'Line allowances',28:'Line charges',29:'Item price details',30:'Line VAT information',
31:'Item information',32:'Context-specific additional line properties',33:'Payment terms',
34:'Context-specific third-party collections/deductions',
}
BG_ES = {1:'Third parties',2:'Document tax/fee details',3:'Third-party tax/fee breakdown',4:'Withholding details'}

def cells(row):
    return [' '.join(' '.join(c.itertext()).split()) for c in row if c.tag in ('td','th')]

def expanded_cells(table):
    """Expand source rowspan cells; keep raw cells separately in the ledger."""
    spans={};result=[]
    for row in table.findall('.//tr'):
        inherited={column:value for column,(value,remaining) in spans.items()}
        spans={column:(value,remaining-1) for column,(value,remaining) in spans.items() if remaining>1}
        output=[];column=0
        for cell in row:
            if cell.tag not in ('td','th'):continue
            while column in inherited:
                output.append(inherited.pop(column));column+=1
            value=' '.join(' '.join(cell.itertext()).split())
            for _ in range(int(cell.get('colspan','1'))):
                output.append(value)
                repeat=int(cell.get('rowspan','1'))
                if repeat>1:spans[column]=(value,repeat-1)
                column+=1
        while inherited:
            output.append(inherited.pop(column,'') if column in inherited else '')
            column+=1
        result.append(output)
    return result

def name(identifier, original):
    m = re.fullmatch(r'(BT|BG)(-ES)?-(\d+)',identifier)
    assert m,identifier
    kind,es,num=m.groups();num=int(num)
    lookup = (ES if es else BT) if kind=='BT' else (BG_ES if es else BG)
    assert num in lookup,(identifier,original)
    # These identifiers repeat with distinct source meanings; retain the label.
    if identifier == 'BT-179':
        if 'retenciones' in original.lower():return 'Total withholding in collection group'
        if 'minoración' in original.lower():return 'Third-party deduction amount'
        if 'impuestos' in original.lower():return 'Tax/fee total in collection group'
        return 'Third-party charge amount'
    return lookup[num]

def field_gate(identifier, description, path):
    gates=['SPFE-Q04','SPFE-Q14']
    if identifier in ('BT-23','BT-24'):gates+=['SPFE-Q13','IC-Q01']
    if identifier in ('BT-3','BT-ES-27','BT-ES-28','BT-ES-29'):gates+=['IC-Q02']
    if identifier in ('BT-31','BT-32','BT-47','BT-48','BG-ES-1','BT-ES-3','BT-ES-4','BT-ES-5'):gates+=['IC-Q04']
    if re.search(r'BT-(?:106|107|108|109|110|111|112|113|114|115|179)\b',identifier) or identifier.startswith('BT-ES-1'):
        gates+=['IC-Q06']
    notes=[]
    if '/in:invoice' in path or '/cac:Invoice/' in path or 'TaxSubTotal' in path:
        notes.append('Literal source-path spelling/structure requires schema review; do not normalize it by assumption.')
    if identifier=='BT-48' and 'vendedor' in description:
        notes.append('Buyer field description contains seller wording; retain the discrepancy under IC-Q04.')
    if identifier=='BG-24' and 'tres grupos' in description:
        notes.append('Review source cardinality across the correction groups under IC-Q02.')
    return list(dict.fromkeys(gates)),notes

def logical_tests(record):
    card=record['cardinality'];label=record['english_name'];scope=record.get('group_context') or record['message']
    return {
        'positive': f"Use an approved applicable {scope} fixture with {label} meeting source type, cardinality {card}, description conditions and controlled values. If optional and no condition makes it required, also check permitted absence.",
        'negative': f"In the same applicable fixture, violate a source condition, cardinality, semantic type or controlled value for {label}. Missing required content within a selected group must fail; absent unselected optional groups must not be made universally required.",
        'execution_status':'not_executed',
        'fixture_status':'approved fixture and executable rule binding still required',
    }

def build():
    root=ET.parse(SOURCE).getroot()
    blocks=root.findall('.//texto');block=next(x for x in blocks if len(x)>150)
    block_index=blocks.index(block)+1
    children=list(block)
    invoice=next(t for t in children if t.tag=='table' and len(t.findall('.//tr'))==177)
    invoice_index=children.index(invoice)
    tables=[c for c in children if c.tag=='table']
    ledger={'scope':'Public invoice, withdrawal and public event source-field traceability; no PRD changes.',
            'source':{'id':'SPFE-S02','xml_path':str(SOURCE.relative_to(ROOT)),
                      'xml_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                      'authority':'Final BOE Annex I/II; original Spanish cells and literal paths retained.'},
            'wire_mapping_status':'unqualified; supplied paths are source facts, not tested wire mappings',
            'rows':[],'code_lists':[]}
    groups=[]
    for i,tr in enumerate(invoice.findall('.//tr')[1:],1):
        v=cells(tr);assert len(v)==7,(i,v)
        ident=re.sub(r'\s','',v[0]);level=len(v[1]);is_group=ident.startswith('BG')
        while groups and groups[-1][0]>=level:groups.pop()
        context=' / '.join(x[1] for x in groups)
        rec={'trace_id':f'AXI-{i:03}','annex':'I','message':'Invoice','source_id':ident,
             'english_name':name(ident,v[3]),'source_name':v[3],'level':v[1],
             'cardinality':v[2],'group_context':context,'source_description':v[4],
             'semantic_type':v[5],'source_ubl_path':v[6],
             'source_locator':f'(//texto)[{block_index}]/table[{tables.index(invoice)+1}]/tbody/tr[{i}]',
             'source_cells':v,'owner_spec':'SPEC-SEI-015',
             'requirement_id':f'IC-AXI-R{i:03}',
             'positive_acceptance_id':f'IC-AXI-A{i:03}P',
             'negative_acceptance_id':f'IC-AXI-A{i:03}N',
             'logical_binding':'ERP/source fact or group with the stated meaning; actual ERP/API field binding remains open.',
             'wire_binding':'source-path-recorded' if v[6] else 'path-not-specified-in-annex',
             'implementation_coverage':'unverified'}
        rec['gates'],rec['source_review_notes']=field_gate(ident,v[4],v[6])
        rec['tests']=logical_tests(rec);ledger['rows'].append(rec)
        if is_group:groups.append((level,rec['english_name']+' ['+rec['trace_id']+']'))
    current_annex='I';message='Invoice';field_table=False;code_label='';code_number=0
    withdrawal_no=0;event_no={}
    for index,child in enumerate(children):
        plain=' '.join(' '.join(child.itertext()).split())
        if plain=='ANEXO II':current_annex='II';code_label=''
        if child.tag!='table':
            if re.match(r'^L\d',plain):code_label=plain
            continue
        trs=child.findall('.//tr')
        first=cells(trs[0]) if trs else []
        if child is invoice:continue
        if len(trs)==1:
            if 'ResponseCode:' in plain:
                message=plain.split('ResponseCode:',1)[1].strip()
            continue
        # Non-BT field tables describe withdrawal or Annex II communications.
        if first and first[0]=='Nivel':
            normalized=expanded_cells(child)
            for row_index,tr in enumerate(trs[1:],2):
                v=normalized[row_index-1];assert len(v)==6,(message,v)
                if current_annex=='I':
                    withdrawal_no+=1;num=withdrawal_no;trace=f'AXC-{num:02}';prefix='OUT-AXC';owner='SPEC-SEI-007'
                else:
                    event_no[message]=event_no.get(message,0)+1;num=event_no[message];trace=f'AXII-{message}-{num:02}';prefix=f'LCS-AXII-{message}';owner='SPEC-SEI-009'
                english=v[2]
                replacements=[('Fecha de efecto','Effective payment date'),('Fecha del cobro','Effective collection date'),
                              ('Fecha de rechazo','Rejection date'),('Fecha de vencimiento del plazo de pago','Payment due date'),
                              ('Fecha de vencimiento del pago','Payment due date'),('Fecha de recepción de las mercancías o de los servicios prestados','Goods/services receipt date'),
                              ('Fecha de recepción de la factura','Invoice receipt date'),('Factura rectificada','Corrected invoice indicator'),
                              ('Factura rectificativa','Negative corrective invoice indicator'),('Motivo de rechazo','Rejection reason code'),
                              ('Mecanismo de financiación','Financing arrangement indicator'),('FACTURA INFORMADA','Referenced invoice group'),
                              ('FACTURA ANULADA','Withdrawn invoice group'),('Fecha de la anulación.','Withdrawal date'),
                              ('Número de factura (ID)','Invoice series and number'),('Fecha de emisión factura','Invoice issue date'),
                              ('Fecha de expedición de la factura.','Invoice issue date'),('Fecha de expedición de la factura','Invoice issue date'),
                              ('NIF emisor','Seller NIF in the invoice reference'),('NIF del vendedor','Seller NIF'),
                              ('Nombre / Razón social emisor','Seller name'),('Nombre o razón social del vendedor','Seller name'),('DATOS DEL VENDEDOR','Seller group')]
                for original,target in replacements:
                    if english==original:english=target;break
                rec={'trace_id':trace,'annex':current_annex,'message':message,'source_id':None,
                     'english_name':english,'source_name':v[2],'level':v[0],'cardinality':v[1],
                     'group_context':'Selected communication and its referenced invoice',
                     'source_description':v[3],'semantic_type':v[4],'source_ubl_path':v[5],
                     'source_locator':f'(//texto)[{block_index}]/table[{tables.index(child)+1}]/tbody/tr[{row_index-1}]',
                     'source_cells':v,'source_raw_cells':cells(tr),'owner_spec':owner,'requirement_id':f'{prefix}-R{num:02}',
                     'positive_acceptance_id':f'{prefix}-A{num:02}P','negative_acceptance_id':f'{prefix}-A{num:02}N',
                     'logical_binding':'Qualified withdrawal/report fact or reference with the exact source meaning; no inferred extra wire fields.',
                     'wire_binding':'source-path-recorded' if v[5] else 'path-not-specified-in-annex',
                     'gates':['SPFE-Q04','SPFE-Q14'] if current_annex=='I' else ['SPFE-Q04','SPFE-Q16'],
                     'source_review_notes':[],'implementation_coverage':'unverified'}
                if message=='DEFAULT' and 'EffectiveDate' in v[5]:rec['source_review_notes'].append('EffectiveDate means payment due date, not observation time.')
                if message=='CANCELINVOICE':rec['gates']+=['SPFE-Q08','IC-Q02']
                rec['tests']=logical_tests(rec);ledger['rows'].append(rec)
        else:
            # Record every code-table occurrence, including separate national
            # qualifier domains. Never merge identical lexical codes across lists.
            code_number+=1
            caption=child.find('caption')
            label=' '.join(' '.join(caption.itertext()).split()) if caption is not None else code_label
            ledger['code_lists'].append({'trace_id':f'AX-CODE-{code_number:02}','annex':current_annex,
                'source_heading':label,'source_context':label,
                'source_locator':f'(//texto)[{block_index}]/table[{tables.index(child)+1}]',
                'source_rows':[cells(tr) for tr in trs],
                'owner_spec':'SPEC-SEI-015' if current_annex=='I' else 'SPEC-SEI-009',
                'requirement_id':f"{'IC' if current_annex=='I' else 'LCS'}-CODE-R{code_number:02}",
                'positive_acceptance_id':f"{'IC' if current_annex=='I' else 'LCS'}-CODE-A{code_number:02}P",
                'negative_acceptance_id':f"{'IC' if current_annex=='I' else 'LCS'}-CODE-A{code_number:02}N",
                'binding_status':'source-list-recorded; scope, namespace and executable rule binding unqualified'})
    ledger['counts']={'invoice_rows':sum(x['message']=='Invoice' for x in ledger['rows']),
                      'withdrawal_rows':withdrawal_no,'event_rows':sum(event_no.values()),
                      'event_rows_by_code':event_no,'code_tables':len(ledger['code_lists'])}
    assert ledger['counts']['invoice_rows']==176
    assert set(event_no)=={'PAYMENT','CANCELPAYMENT','REJECTION','CANCELREJECTION','SETTLEMENT','CANCELSETTLEMENT','DEFAULT','CANCELDEFAULT'}
    OUT.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(ledger['counts'],indent=2))
    return ledger

if __name__=='__main__':build()
