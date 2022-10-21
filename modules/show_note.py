import csv


def view_note():
    counter = int(1)
    with open('database.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{counter}. ", row["Surname"],
                  row["Name"], row["Phone"], row["Description"])
            counter += 1
