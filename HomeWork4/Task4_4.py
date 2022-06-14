# Задана натуральная степень n. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 


from random import randint


def create_coef_list(k): # Создаем список коэффициентов для полинома
    return [randint(1, 100) if x == 0 else randint(0, 100) for x in range (k + 1)]


def create_polynomial(power, lst): # Создаем полином из списка коэффициентов и максимальной степени
    result_list = []
    for index, elem in enumerate(lst):
        pow = power - index
        if elem == 0:
            result_list.append("")
        elif elem == 1 and pow == 1:
            result_list.append("x")
        elif elem == 1 and pow == 0:
            result_list.append("1")
        elif elem == 1:
            result_list.append(f"x^{pow}")
        elif elem != 1 and pow == 1:
            result_list.append(f"{elem}*x")
        elif elem != 1 and pow == 0:
            result_list.append(f"{elem}")
        else:
            result_list.append(f"{elem}*x^{pow}")        

    return " + ".join(x for x in result_list if x != "") + " = 0"


def import_to_file(path, item): # Запись полинома в файл, для использования в следующей задаче
    with open (path, "w") as data:
        data.write(item)


k1 = randint(3, 7)
k2 = randint(3, 7)

#coef_list1 = [1, 0, 1, 3, 150]     # для проверки граничных значений коэффициентов таких как 0,1
coef_list1 = create_coef_list(k1)
coef_list2 = create_coef_list(k2)

poly1 = create_polynomial(k1, coef_list1)
poly2 = create_polynomial(k2, coef_list2)
print(f"\nСписок коэф. первого полинома = {coef_list1}")
print(f"Первый полином = {poly1}")
print(f"\nСписок коэф. второго полинома = {coef_list2}")
print(f"Второй полином = {poly2}\n")

path1 = "polynom1.txt"
path2 = "polynom2.txt"

import_to_file(path1, poly1)
import_to_file(path2, poly2)

