import csv


def view_note():
    counter = int(1)
    with open('database.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{counter}. ", row["Фамилия"],
                  row["Имя"], row["Телефон"], row["Описание"])
            counter += 1
