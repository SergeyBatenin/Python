

import csv
import menu


def show_pupils():
    with open("pupils.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    menu.restart_or_exit()


def show_parents():
    with open("parents.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    menu.restart_or_exit()


def add_pupils():
    fname = input("Введите имя: ")
    lname = input("Введите фамилию: ")
    class_number = input("Введите класс ")
    phone = input("Введите номер телефона: ")
    with open("pupils.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        id = int(list(reader)[-1]["Идентификатор"])
        id += 1

    pupil = [id, fname, lname, class_number, phone]
    with open("pupils.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(i for i in pupil)
    menu.restart_or_exit()


def add_parents():
    id = find_pupil()
    if id == -1:
        print("Такого ученика не найдено. Хотите добавить ученика?")
        print("\tДа - 1\n\tНет - любое значение")
        choice = input()
        if choice == "1":
            add_pupils()
        else :
            quit()
    
    fname = input("Введите имя родителя: ")
    lname = input("Введите фамилию родителя: ")
    kinship = input("Кем приходится: ")
    phone = input("Введите номер телефона: ")
    parent = [id, fname, lname, kinship, phone]

    with open("parents.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([i for i in parent])    
    
    menu.restart_or_exit()


def find_pupil():
    child_lname = input("Введите фамилию ученика: ").lower()
    child_class = input("Введите номер класса ученика: ").lower()
    id_pupil = -1
    with open("pupils.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            current_lname = row["Фамилия"].lower()
            current_class = row["Класс"].lower()
            if current_lname == child_lname and current_class == child_class:
                print(row)
                print("\nЭто ваш ребенок?\n\tДа - 1\n\tНет - любое значение")
                choice = input()
                if choice == "1":
                    id_pupil = row["Идентификатор"]
                    return id_pupil
    return id_pupil


def find_parent():
    id_pupil = find_pupil()
    flag = True
    if id_pupil != -1:
        with open("parents.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if id_pupil == row["Идентификатор"]:
                    print(row)
                    flag = False
    else :
        print("Такого ученика нет")
        flag = False
    
    if flag:
        print("Для данного ученика нет родственников в базе")
    menu.restart_or_exit()

