from datetime import datetime


def transform(data):
    """Transforms data to the target common structure:
         - amount (float)
         - date (date)
         - from (int)
         - source (str)
         - to (int)
         - transaction (str)

    Args:
        data (list[dict]): source data arrived from bank3

    Returns:
        list[dict]: normalized data to the common structure
    """
    dataset = []
    record = {'source': 'BANK3'}
    for row in data:
        for (k,v) in row.items():
            if k == 'date_readable':
                record['date'] = datetime.strptime(v,'%d %b %Y').strftime('%Y-%m-%d')
            elif k == 'type':
                record['transaction'] = v
            elif k == 'euro':
                record['amount'] = row['euro'] + '.' + row['cents']
            elif k in {'from', 'to'}:
                record[k] = v
            elif k != 'cents':
                raise Exception(f'Unexpected column {k} obtained from BANK1')
        # sorting the dict to have the same order. 
        # Due to we have no requirement regarding the order, it will be alphabetical
        sorted_record = sorted(record.items(), key=lambda entity: entity[0])
        #due to sorted() function returns list of tuples, we need to get back list of dicts
        dataset.append({k:v for k, v in sorted_record})

    return dataset