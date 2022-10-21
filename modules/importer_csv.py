import csv
from modules.add_note import add_note


def csv_import(filename):
    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        for row in reader:
            add_note(row["Surname"], row["Name"],
                     row["Phone"], row["Description"])
            counter += 1
    print(f"Импортировано записей: {counter}")
