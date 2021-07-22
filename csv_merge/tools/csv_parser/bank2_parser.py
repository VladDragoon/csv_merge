from datetime import datetime
from csv_merge.tools.helpers import rpad, tuples_to_dicts

def transform(data):
    """Transforms data to the target common structure:
         - amount (float)
         - date (date)
         - from (int)
         - source (str)
         - to (int)
         - transaction (str)

    Args:
        data (list[dict]): source data arrived from bank2

    Returns:
        list[dict]: normalized data to the common structure
    """
    dataset = []
    record = {'source': 'BANK2'}
    for row in data:
        for (k,v) in row.items():
            if k == 'date':
                record[k] =datetime.strptime(v,'%d-%m-%Y').strftime('%Y-%m-%d')
            elif k == 'amounts':
                # converting for the input data validation
                # padding zeroes to the right to have proper cents 
                record['amount'] = rpad(str(float(v)))
            elif k == 'transaction':
                record[k] = v
            elif k in {'from', 'to'}:
                # converting for the input data validation
                record[k] = int(v)
            else:
                raise Exception(f'Unexpected column {k} obtained from BANK2')
        # sorting the dict to have the same order. 
        # Due to we have no requirement regarding the order, it will be alphabetical
        sorted_record = sorted(record.items(), key=lambda entity: entity[0])
        #due to sorted() function returns list of tuples, we need to get back list of dicts
        dataset.append(tuples_to_dicts(sorted_record))

    return dataset