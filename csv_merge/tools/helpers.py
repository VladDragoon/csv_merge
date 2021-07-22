def rpad(value):
    """Padding zeroes to cents from the right if they are got lost

    Args:
        value (str): some float number 'xx.yy'

    Returns:
        str: corrected money format
    """
    result = value
    cents = value.split('.')[1]
    if len(cents) < 2:
        euro = value.split('.')[0]
        result = euro + '.' + cents.ljust(2, '0')
    return result

def tuples_to_dicts(dataset):
    """Converts list of tuples to list of dicts

    Args:
        dataset (list[tuple]): input dataset

    Returns:
        list[dict]: output dataset after the transformation
    """
    return {k:v for k, v in dataset}