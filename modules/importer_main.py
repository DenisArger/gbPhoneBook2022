from modules.importer_csv import csv_import
from modules.importer_txt import txt_import
from modules.importer_xml import xml_import


def import_interface():
    print("Импортируемый файл должен находиться в папке import")
    filename = input("Введите наименование файла с расширением: ")
    filename = "import/" + filename
    try:
        open(filename)

    except:
        print("Указанный файл отстутствует")
        return
    file_extention = filename[filename.rindex(".") + 1:]
    if file_extention in ["txt", "csv", "xml"]:

        if file_extention == "txt":
            txt_import(filename)

        elif file_extention == "xml":
            xml_import(filename)

        elif file_extention == "csv":
            csv_import(filename)
