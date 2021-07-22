import csv_merge.tools.file_driver as file_driver
import csv_merge.tools.parser as parser
from csv_merge.tools.sources import Sources
import functools

def process_workload(output_file, **args):
    """Root function for the ETL process

    Args:
        output_file (str): name with path to the output file
    """
    assert output_file, 'Output file was not provided'
    assert args, 'Input files were not provided'

    input_data = load_data(**args)
    intermediate_data = merge_all_data(input_data)
    output_data = parser.prepare(intermediate_data)
    file_driver.save_data(output_file, output_data)

def load_data(**kwargs):
    """Initiates reading data from file per each of the input sources

    Returns:
        list: data from source files, already normalized to the common schema
    """
    return [parser.normalize_data(source_name,
                                  file_driver.read_csv(source_file))
            for source_name, source_file in kwargs.items()]

def merge_all_data(input_data):
    """Unites data, which was taken from different sources, into one dataset

    Args:
        input_data (list[list[dict]]): array of dictionaries with the source data

    Returns:
        list[dict]: united data
    """
    return functools.reduce(lambda a, b: a + b, input_data)

if __name__ == '__main__':
    path = 'data/source'
    workload = {
        Sources.BANK1.name: f'{path}/bank1.csv',
        Sources.BANK2.name: f'{path}/bank2.csv',
        Sources.BANK3.name: f'{path}/bank3.csv'
    }
    output_file = 'data/target/output.csv'
    process_workload(output_file, **workload)