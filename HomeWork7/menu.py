

import UI
import DB


def view_main_menu():
    print("Выберете необходимый раздел:")
    print("\t1 - Посмотреть тел. книгу")
    print("\t2 - Добавить пользователя")
    print("\t3 - Удалить пользователя")
    print("\t4 - Посмотреть пользователя")
    print("\t5 - Очистить тел. книгу")
    print("\t6 - Экспортировать ..")
    print("\t7 - Импортировать ..")
    print("\t8 - Выход")


def choice_user():
    choice_user = int(input())
    while choice_user == "" or 1 > choice_user or choice_user > 8:
            print("Неверный ввод.")
            view_main_menu()
            choice_user = int(input())
    return choice_user


def restart_or_exit():
    print("Если хотите продолжить работу введите - 1\nДля выхода введите любое значение")
    choice_user = input()
    if choice_user == "1":
        UI.start()
    else:
        quit()


def delete_menu():
    print("Удаление пользователя по:")
    print("\t1 - Фамилии")
    print("\t2 - Номеру телефону")
    selection = int(input())
    if selection == 1:
        choice_user = input("Введите фамилию пользователя для удаления: ")
        return choice_user
    else:
        choice_user = input("Введите номер телефона для удаления: ")
        return choice_user


def export_to():
    print("В каком формате хотите экспорт")
    print("Чтобы получить в json введите - 1\nЧтобы получить в txt введите -2")
    selection = input()
    if selection == "1":
        DB.export_json()
    elif selection == "2":
        DB.export_txt()
    else:
        print("Неверный ввод")


def import_from():
    print("Из какого формата произвести импорт?")
    print("Из формата json - 1\nИз формата txt -2")
    selection = input()
    if selection == "1":
        DB.import_json()
    elif selection == "2":
        DB.import_txt()
    else:
        print("Неверный ввод")