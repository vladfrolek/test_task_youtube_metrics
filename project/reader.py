import csv

def read_file(file_path):
    list_of_rows = []
    try:
        with open(file_path,"r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row['ctr']=float(row['ctr'])
                row['retention_rate']=float(row['retention_rate'])
                list_of_rows.append(row)
        return list_of_rows
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл {file_path} не найден')

def read_files(file_paths):
    data = []
    for file_path in file_paths:
        rows=read_file(file_path)
        data.extend(rows)
    return data
