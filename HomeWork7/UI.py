

import menu
import DB


def start():
    menu.view_main_menu()

    selection = choice_user()
    if selection == 1:
        DB.print_db()
    elif selection == 2:
        lname = input("Введите фамилию:")
        fname = input("Введите имя:")
        phone = input("Введите номер телефона")
        about = input("Введите тип телефона")
        DB.add_user(lname, fname, phone, about)
    elif selection == 3:
        print(33)
    elif selection == 4:
        print(44)
    elif selection == 5:
        print(55)
    elif selection == 6:
        print(66)
    elif selection == 7:
        print(77)
    elif selection == 8:
        print("До свидания")
        quit()


def choice_user():
    choice_user = int(input())
    while 1 > choice_user or choice_user > 8:
            print("Неверный ввод.")
            menu.view_main_menu()
            choice_user = int(input())
    return choice_user