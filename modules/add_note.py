from modules.add_note_is_checker import check_tel
import csv


def add_note(family=None, name=None, tel=None, discription=None):
    if family:
        with open("database.csv", "a", encoding='utf-8') as csvfile:
            fieldnames = ["Surname", "Name", "Phone", "Description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"Surname": family, "Name": name,
                            "Phone": tel, "Description": discription})
    else:
        dict = {"Surname": None, "Name": None,
                "Phone": None, "Description": None}
        n = 0
        while n == 0:
            family = input("Введите фамилию: ")
            if family.isalpha():
                dict["Surname"] = family.capitalize()
                n = 1
            else:
                print("Неверный ввод")
                continue
        while n == 1:
            name = input("Введите Name: ")
            if name.isalpha():
                dict["Name"] = name.capitalize()
                n = 2
            else:
                print("Неверный ввод")
                continue
        while not tel:
            phone = input("Введите номер Phoneа: ")
            tel = check_tel(phone)
            if tel:
                dict["Phone"] = tel
            else:
                print("Неверный ввод")
                continue

        discription = input("Введите Description: ")
        dict["Description"] = discription.capitalize()

        with open("database.csv", "a", newline="") as csvfile:
            fieldnames = ["Surname", "Name", "Phone", "Description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict)
