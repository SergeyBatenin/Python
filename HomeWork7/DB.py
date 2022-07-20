

import csv
import menu
import logger
import UI
import json


def print_db():
    with open("db.txt", 'r', encoding="UTF-8") as data:
        data_base = data.read()
    print(data_base)
    menu.restart_or_exit()


# def add_user():
#     lname = input("Введите фамилию: ")
#     fname = input("Введите имя: ")
#     phone = input("Введите номер телефона: ")
#     about = input("Введите тип телефона: ")
#     user = [lname, fname, phone, about]
#     with open('db.txt', 'a+', encoding="utf-8") as data:
#         #data.write(lname + ";" + fname + ";" + phone + ";" + about + "\n")
#         data.write(";".join(user) + "\n")
#         # for item in user:
#         #     data.write(item + ";")
#         # data.write("\n")
#         # ";".join(user) + "\n"
#     logger.add_log(f"Был добавлен пользователь {lname}")
#     menu.restart_or_exit()
def add_user():
    lname = input("Введите фамилию: ")
    fname = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    about = input("Введите тип телефона: ")
    user = [lname, fname, phone, about]
    with open('db.csv', 'a', encoding="UTF-8") as data:
        writer = csv.writer(data)
        writer.writerow(user)
        #data.write(";".join(user) + "\n")
        
        # ";".join(user) + "\n"
    logger.add_log(f"Был добавлен пользователь {lname}")
    menu.restart_or_exit()


def delete_user():
    delete_value = menu.delete_menu().lower()
    if delete_value.isdigit():
        index_value = 2
    else:
        index_value = 0
    print(index_value, delete_value)
    
    with open("db.txt", "r", encoding="UTF-8") as data:
        data_base = []
        for line in data:
            data_base.append(line)
        #print(data_base)
    delete_flag = True
    
    with open("db.txt", "w", encoding="UTF-8") as data:
        for user in data_base:
            current_value =  user.split(";")[index_value]
            current_value = current_value.lower()
            if not current_value == delete_value:
                data.write(user)
            else:
                delete_flag = False
        
    if not delete_flag:
        #data_base.remove(user)
        print("Удаление прошло успешно")
        logger.add_log(f"Был удален пользователь {delete_value}")
    else:
        print("Пользователя с такими данными не существует")
        logger.add_log(f"Неудачная попытка удаления пользователя с данными = \"{delete_value}\"")
    #print(data_base)
    menu.restart_or_exit()


# def show_contact():
#     lastname = input("Введите фамилию: ").lower()
#     data_base = []
#     with open("db.txt", "r", encoding="utf-8") as data:
#         for line in data:
#             data_base.append(line)
#     print(data_base)
#     user_flag = True
#     for user in data_base:
#         lname_user = user.split(";")[0].lower()
#         if lastname == lname_user:
#             user_flag = False
#             print(user)
#             break
#     if user_flag:
#         print("Пользователя с такой фамилией не существует")
#         print("Повторить поиск - 1\nДля возврата в главное меню - 2\nДля выхода введите любое значение")
#         choice_user = input()
#         if choice_user == "1":
#             show_contact()
#         elif choice_user == "2":
#             UI.start()
#         else:
#             quit()
def show_contact():
    lastname = input("Введите фамилию: ").lower()
    data_base = []
    with open("db.csv", "r", encoding="UTF-8") as data:
        reader = csv.reader(data)
        for line in reader:
            data_base.append(line)
    print(data_base)
    user_flag = True
    for user in data_base:
        lname_user = user.split(";")[0].lower()
        if lastname == lname_user:
            user_flag = False
            print(user)
            break
    if user_flag:
        print("Пользователя с такой фамилией не существует")
        print("Повторить поиск - 1\nДля возврата в главное меню - 2\nДля выхода введите любое значение")
        choice_user = input()
        if choice_user == "1":
            show_contact()
        elif choice_user == "2":
            UI.start()
        else:
            quit()


def clear_db():
    with open("db.txt", "w", encoding="UTF-8") as data:
        data.write("")
    logger.add_log("База данных была стерта")
    print("Телефонная книга успешно очищена")
    menu.restart_or_exit()


def export_json():
    data_base = []
    with open("db.csv", "r", encoding="UTF-8") as data:
        reader = csv.DictReader(data)
        for line in reader:
            data_base.append(line)
    # print(data_base)
    with open("export.json", "w", encoding="UTF-8") as data:
        json.dump(data_base, data)

    

def import_json():
    data_base = []
    with open("export.json", "r", encoding="UTF-8") as data:
        #file_content = data.read()
        data_base = json.load(data)
    print(data_base)