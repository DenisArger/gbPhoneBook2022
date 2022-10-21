from modules.show_note import view_note
from modules.add_note import add_note
from modules.exporter_main import export_interface
from modules.importer_main import import_interface


def ui():
    print('\nВас приветствует Phoneная книга')

    while True:
        print("")
        print("МЕНЮ:")
        print("1: Посмотреть все записи")
        print("2: Добавить запись")
        print("3: Экспорт")
        print("4: Импорт")
        print("0: Выход")

        number = input("Введите пункт меню: ")
        if number.isdigit():
            number = int(number)
        else:
            print("Неверный ввод, повторите попытку")
            continue
        if number not in [1, 2, 3, 4, 0]:
            print("Неверный ввод, повторите попытку")
            continue

        if number == 1:
            view_note()
        elif number == 2:
            add_note()
        elif number == 3:
            export_interface()
        elif number == 4:
            import_interface()
        elif number == 0:
            print("До новых встреч!")
            return
