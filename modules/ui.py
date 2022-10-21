def ui():
    print('\nВас приветствует телефонная книга')

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
            print("1: Посмотреть все записи")
        elif number == 2:
            print("2: Добавить запись")
        elif number == 3:
            print("3: Экспорт")
        elif number == 4:
            print("4: Импорт")
        elif number == 4:
            print("До новых встреч!")


ui()
