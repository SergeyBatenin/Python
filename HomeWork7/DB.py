

import menu
import logger


def print_db():
    with open("db.txt", 'r', encoding="utf-8") as data:
        data_base = data.read()
    print(data_base)
    menu.restart_or_exit()


def add_user():
    lname = input("Введите фамилию: ")
    fname = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    about = input("Введите тип телефона: ")
    user = [lname, fname, phone, about]
    with open('db.txt', 'a+', encoding="utf-8") as data:
        for item in user:
            data.write(item + ";")
        data.write("\n")
        # ";".join(user) + "\n"
    logger.add_log(f"Был добавлен пользователь {lname}")
    menu.restart_or_exit()


def delete_user():
    delete_value = menu.delete_menu().lower()
    with open("db.txt", "r", encoding="utf-8") as data:
        data_base = []
        for line in data:
            data_base.append(line)
        print(data_base)
    delete_index = -1
    for user in data_base:
        delete_index = user.lower().find(delete_value)
        if delete_index != -1:
            data_base.remove(user)
            print("Удаление прошло успешно")
            logger.add_log(f"Был удален пользователь {user}")
            break
    if delete_index == -1:
        print("Пользователя с такими данными не существует")
        logger.add_log(f"Неудачная попытка удаления пользователя с данными = \"{delete_value}\"")
    print(data_base)
    menu.restart_or_exit()


def clear_db():
    with open("db.txt", "w", encoding="utf-8") as data:
        data.write("")
    logger.add_log("База данных была стерта")
    print("Телефонная книга успешно очищена")
    menu.restart_or_exit()

