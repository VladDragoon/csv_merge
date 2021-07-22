import csv_merge.tools.csv_parser.bank1_parser as bank1_parser
import csv_merge.tools.csv_parser.bank2_parser as bank2_parser
import csv_merge.tools.csv_parser.bank3_parser as bank3_parser
from csv_merge.tools.sources import Sources


def normalize_data(source_name, data):
    """Calls data transformation parsers specific to a source

    Args:
        source_name (Sources): enum name of data source
        data (list[dict]): source data

    Raises:
        Exception: handles the case with the unexpected source type

    Returns:
        list[dict]: normalized data to the common structure
    """
    normalized_data = {}
    if   source_name == Sources.BANK1.name:
        normalized_data = bank1_parser.transform(data)
    elif source_name == Sources.BANK2.name:
        normalized_data = bank2_parser.transform(data)
    elif source_name == Sources.BANK3.name:
        normalized_data = bank3_parser.transform(data)
    else:
        raise Exception(f'Unexpected source name: {source_name}')
    return normalized_data

def prepare(data):
    """Transform data to be properly saved into csv

    Args:
        data (list[dict]): input data

    Returns:
        list: data with the header in the first row
    """
    dataset = [[*data[0].keys()]]
    for record in data:
        dataset.append(list(record.values()))
    return dataset