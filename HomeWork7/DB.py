

import csv
import os
import menu
import logger
import UI
import json


def print_db():
    check_file = os.path.isfile("db.csv")
    if check_file:
        read_db()
        menu.restart_or_exit()
    else :
        print("""Книга еще не создана. Желаете создать?
        Чтобы создать телефонную книгу введите - 1,
        чтобы вернуться в меню - любой символ""")
        choice_user = input()
        if choice_user == "1":
            create_db()
            menu.restart_or_exit()
        else :
            UI.start()


def add_user():
    lname = input("Введите фамилию: ")
    fname = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    about = input("Введите тип телефона: ")
    user = [lname, fname, phone, about]
    check_file = os.path.isfile("db.csv")
    print(check_file)
    
    if not check_file:
        create_db()

    write_in_db(user)
    # user = ["Петров", "Петр", "123", "личный"]
    # write_in_db(user)
    # user = ["Сидоров", "Коля", "1234", "домашний"]
    # write_in_db(user)
    # user = ["Зайцев", "Саша", "12345", "рабочий"]
    # write_in_db(user)

    logger.add_log(f"Был добавлен пользователь {lname}")
    menu.restart_or_exit()


def delete_user():
    delete_value = menu.delete_menu().lower()
    if delete_value.isdigit():
        index_value = "Phone"
    else:
        index_value = "Lastname"
    phone_book = []
    with open("db.csv", "r", encoding="UTF-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            phone_book.append(row)
    delete_flag = False
    
    for user in phone_book:
        current_value = user[index_value].lower()
        if current_value == delete_value:
            phone_book.remove(user)
            delete_flag = True
        
    if delete_flag:
        header = ["Lastname", "Firstname", "Phone", "About"]
        with open("db.csv", "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(phone_book)
            # for user in phone_book:
            #     writer.writerow(user)
        print("Удаление прошло успешно")
        logger.add_log(f"Был удален пользователь с {index_value} =  {delete_value}")
    else:
        print("Пользователя с такими данными не существует")
        logger.add_log(f"Неудачная попытка удаления пользователя с данными {index_value} = \"{delete_value}\"")
    menu.restart_or_exit()


def show_contact():
    lastname = input("Введите фамилию: ").lower()
    user_flag = True
    with open("db.csv", "r", encoding="UTF-8") as data:
        reader = csv.DictReader(data)
        for user in reader:
            lname_user = user["Lastname"].lower()
            if lastname == lname_user:
                user_flag = False
                print()
                for pair in user.items():
                    print(pair[0], "=", pair[1])
                break
    print()

    if user_flag:
        print("Пользователя с такой фамилией не существует\n")

    menu.restart_or_exit()


def clear_db():
    create_db()
    logger.add_log("База данных была стерта")
    print("Телефонная книга успешно очищена\n")
    menu.restart_or_exit()


def export_json():
    data_base = []
    with open("db.csv", "r", encoding="UTF-8") as data:
        reader = csv.DictReader(data)
        for line in reader:
            data_base.append(line)
    with open("exportJson.json", "w", encoding="UTF-8") as data:
        json.dump(data_base, data, sort_keys=False, indent=4, ensure_ascii=False)
    logger.add_log("Произведен экспорт справочника в формате json")
    menu.restart_or_exit()

    
def export_txt():
    data_base = []
    with open("db.csv", "r", encoding="UTF-8") as data:
        reader = csv.DictReader(data)
        for line in reader:
            data_base.append(line)
    with open("exportTxt.txt", "w", encoding="utf-8") as data:
        for users in data_base:
            user = []
            for pair in users.items():
                user.append(pair[1])            
            data.write(",".join(user))
            data.write("\n")
    logger.add_log("Произведен экспорт справочника в формате txt")
    menu.restart_or_exit()


def import_json():
    with open("importJson.json", "r", encoding="UTF-8") as data:
        data_base = json.load(data)

    header = ["Lastname", "Firstname", "Phone", "About"]
    with open("db.csv", "a", encoding="utf-8") as data:
        writer = csv.DictWriter(data, fieldnames=header)
        writer.writerows(data_base)
    logger.add_log("Произведен импорт из файла в формате json")
    menu.restart_or_exit()


def import_txt():
    data_base = []
    with open("importTxt.txt", "r", encoding="UTF-8") as data:
        reader = data.readlines()
        for users in reader:
            user = users.split(",")
            user[-1] = user[-1][:-1]
            write_in_db(user)
    logger.add_log("Произведен импорт из файла в формате txt")
    menu.restart_or_exit()


def create_db():
    header = ["Lastname", "Firstname", "Phone", "About"]
    with open("db.csv", "w", encoding="utf-8") as file:
        # writer = csv.writer(file, delimiter=",")
        # writer.writerow([i for i in header])
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
    
    logger.add_log("Телефонный справочник был создан")
        # column = 4
        # generator = ["a", "b", "c", "d"]
        # for x in range(column):
            # writer.writerow([g() for g in generator])


def write_in_db(lst):
    with open('db.csv', 'a', encoding="utf-8") as data:
            writer = csv.writer(data)
            #writer.writerow(lst)
        # lst = ["a", "b", "c", "d"]
            writer.writerow([g for g in lst])


def read_db():
    with open("db.csv", "r", encoding="UTF-8") as data:
        # reader = csv.reader(data)
        # for line in reader:
        #     print(line)
        reader = csv.DictReader(data)
        for row in reader:
            print(row)