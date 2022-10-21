import csv


def create_xml(name="new_export"):
    xml = '<xml>\n'
    with open('database.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xml += f'<Surname>{row["Surname"]}</Surname>\n'
            xml += f'<Name>{row["Name"]}</Name>\n'
            xml += f'<Phone>{row["Phone"]}</Phone>\n'
            xml += f'<Description>{row["Description"]}</Description>\n'
    xml += '</xml>'
    with open(f"export/{name}.xml", 'w') as page:
        page.write(xml)
