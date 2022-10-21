from modules.ui import ui
import csv

print("Телефонная книга версия 1.0.0")
try:
    file = open("database.csv", "r")
    file.close()
except:
    with open("database.csv", 'w', newline='') as csvfile:
        fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
ui()
