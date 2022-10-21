from modules.add_note import add_note


def txt_import(filename):
    def new_string(file):
        string = file.readline
    counter = 0
    with open(filename, "r", encoding='utf-8') as file:
        flag = True
        while flag:
            current_string = file.readline()
            if current_string == "":
                flag = False
            current_string = current_string.replace("\n", "")
            if current_string == "":
                continue
            else:
                family = current_string
                name = file.readline().replace("\n", "")
                tel = file.readline().replace("\n", "")
                discription = file.readline().replace("\n", "")
                if "Surname: " in family and "Name: " in name and "Phone: " in tel and "Description: " in discription:
                    family = family.replace("Surname: ", "")
                    name = name.replace("Name: ", "")
                    tel = tel.replace("Phone: ", "")
                    discription = discription.replace("Description: ", "")
                    add_note(family, name, tel, discription)
                    counter += 1
                else:
                    print("Файл некорректен. Импорт невозможен")
                    continue
    print(f"Импортировано записей: {counter}")
