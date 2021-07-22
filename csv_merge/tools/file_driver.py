import csv

def read_csv(file_name):
    dataset = []

    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dataset.append(row)

    return dataset

def save_data(output_file, dataset):
    with open(output_file, 'w', newline="") as f:
        write = csv.writer(f)      
        write.writerows(dataset)