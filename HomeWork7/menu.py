import UI

def view_export_menu():
    pass  


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
    choice_user = input()
    while choice_user == "" or 1 > int(choice_user) or int(choice_user) > 8:
            print("Неверный ввод.")
            view_main_menu()
            choice_user = input()
    return choice_user


def restart_or_exit():
    print("Если хотите продолжить работу нажмите - 1\nДля выхода введите любое значение")
    choice_user = int(input())
    if choice_user == 1:
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