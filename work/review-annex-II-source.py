"""Compare the supplied Annex II tables with the unchanged final-BOE field ledger."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'context/Anexo II/A2-Proyecto-OM-FE 21-10-26.pdf'
OUT = ROOT / 'assets/regulatory/spain/spfe'
CODES = ['PAYMENT','CANCELPAYMENT','REJECTION','CANCELREJECTION','SETTLEMENT','CANCELSETTLEMENT','DEFAULT','CANCELDEFAULT']


def normalize(value):
    return re.sub(r'\s+', '', value or '').replace('7.ª','7ª')


def extract():
    doc = pymupdf.open(PDF)
    rows = []
    code = None
    for page_index, page in enumerate(doc):
        for table in page.find_tables().tables:
            raw = table.extract()
            joined = ' '.join(cell or '' for row in raw for cell in row)
            match = re.search(r'ResponseCode:\s*('+'|'.join(CODES)+r')\b', joined)
            if match:
                code = match[1]
                continue
            for row_index, cells in enumerate(raw):
                populated = [(i,c.strip()) for i,c in enumerate(cells) if c and c.strip()]
                if not populated or not re.fullmatch(r'\+(?:\s*\+)*',populated[0][1]):
                    continue
                values = [v for _,v in populated]
                if len(values) == 4:
                    # The group heading/description wraps into a continuation row.
                    name_index, desc_index = populated[2][0], populated[3][0]
                    name, desc = values[2:]
                    for following in raw[row_index+1:]:
                        if following[0] and following[0].strip().startswith('+'):
                            break
                        name += ' ' + (following[name_index] or '')
                        desc += ' ' + (following[desc_index] or '')
                    expanded = [[values[0],values[1],name,desc,'','']]
                elif len(values) == 6 and '\n' in values[1]:
                    # Two receipt-date rows share the source description cell.
                    names = [s for s in re.split(r'(?=Fecha de recepción de)', re.sub(r'\s+',' ',values[2])) if s.strip()]
                    path = re.sub(r'\s+','',values[5])
                    cut = path.index('ShipmentDate') + len('ShipmentDate')
                    assert len(names) == 2
                    expanded = [['+','0..1',names[0],values[3],'Fecha',path[:cut]],
                                ['+','0..1',names[1],values[3],'Fecha',path[cut:]]]
                else:
                    assert len(values) == 6, (page_index+1, values)
                    expanded = [values]
                for values in expanded:
                    rows.append({'message':code,'pdf_page':page_index+1,'table_row':row_index+1,
                        'source_cells':values})
    return rows, len(doc)


def main():
    rows, pages = extract()
    ledger = json.loads((OUT / 'field-traceability.json').read_text())
    baseline = [row for row in ledger['rows'] if row['annex'] == 'II']
    assert len(rows) == len(baseline) == 52
    comparisons = []
    for current, original in zip(rows,baseline):
        assert current['message'] == original['message']
        differences = [name for name,old,new in zip(
            ['level','cardinality','name','description','semantic_type','source_ubl_path'],
            original['source_cells'],current['source_cells']) if normalize(old) != normalize(new)]
        comparisons.append({**current,'trace_id':original['trace_id'],
            'baseline_locator':original['source_locator'],'different_columns_after_whitespace_normalization':differences})
    pdf = pymupdf.open(PDF)
    code_rows = []
    for table in pdf[14].find_tables().tables:
        for row in table.extract():
            cells = [cell.strip() for cell in row if cell and cell.strip()]
            if cells and cells[0] in ('01','02'):
                code_rows.append([cells[0], ' '.join(cells[1:])])
    original_codes = next(item for item in ledger['code_lists'] if item['annex']=='II')
    assert len(code_rows) == 2
    assert [[normalize(c) for c in row] for row in code_rows] == [[normalize(c) for c in row] for row in original_codes['source_rows'][1:]]
    result = {'source_id':'SPFE-S22','source_path':str(PDF.relative_to(ROOT)),
        'source_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'pages':pages,
        'baseline_source_id':'SPFE-S02','baseline_ledger':'assets/regulatory/spain/spfe/field-traceability.json',
        'method':'Ordered table-cell comparison for all 52 field/group occurrences; shared description cells expanded. Whitespace and 7.ª/7ª typography normalized only.',
        'limits':'Original PDFs govern. This compares source fields, not wire mappings, executable rules, legal publication status or implementation readiness.',
        'counts_by_code':dict(Counter(row['message'] for row in rows)),
        'code_list':{'trace_id':original_codes['trace_id'],'pdf_page':15,'source_rows':code_rows,'matches_baseline':True},
        'rows_with_differences':[row['trace_id'] for row in comparisons if row['different_columns_after_whitespace_normalization']],
        'rows':comparisons}
    (OUT / 'event-annex-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key!='rows'},ensure_ascii=False,indent=2))
    for row in comparisons:
        if row['different_columns_after_whitespace_normalization']:
            print(row['trace_id'],row['different_columns_after_whitespace_normalization'])


if __name__ == '__main__':
    main()
