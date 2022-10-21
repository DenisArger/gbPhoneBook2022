import csv


def create_txt(name="new_export"):
    with open('database.csv', encoding='utf-8') as csvfile:
        txt = ""
        reader = csv.DictReader(csvfile)
        page = open(f"export/{name}.txt", 'w')
        for row in reader:
            txt += f'Surname: {row["Surname"]}\n'
            txt += f'Name: {row["Name"]}\n'
            txt += f'Phone: {row["Phone"]}\n'
            txt += f'Description: {row["Description"]}\n\n'
        page.write(txt)
