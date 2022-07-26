

import UI


def view_main_menu():
    print("Выберете необходимый раздел:")
    print("\t1 - Посмотреть список учеников")
    print("\t2 - Посмотреть список родителей")
    print("\t3 - Добавить ученика")
    print("\t4 - Добавить родителя")
    print("\t5 - Поиск родителя")
    print("\t6 - Выход")


def choice_user():
    choice_user = int(input())
    while choice_user == "" or 1 > choice_user or choice_user > 6:
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

