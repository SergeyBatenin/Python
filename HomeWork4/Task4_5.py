# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Нужно два полинома сложить

# Чтобы потом создать новый полином на основе суммы двух начальных в 34 строке
# импортируем метод из 4 задачи
from Task4_4 import create_polynomial


def export_from_file(path): # Чтобы достать полиномы из файла
    with open(path, "r") as data:
        polynom = data.read()
    return polynom


def add_poly_coef_list(polynom1, polynom2): # Суммируем полиномы
    index_max_power = polynom1.find("^")

    length1 = 2 if index_max_power == -1 else int(polynom1[index_max_power+1:polynom1.find(" ")])
    index_max_power = polynom2.find("^")
    length2 = 2 if index_max_power== -1 else int(polynom2[index_max_power+1: polynom2.find(" ")])
    length = max(length1, length2) + 1

    first_poly_list = poly_coef_list(length, polynom1)
    second_poly_list = poly_coef_list(length, polynom2)
    #print(first_poly_list)
    #print(second_poly_list)
    result_list = []
    for item1, item2 in zip(first_poly_list, second_poly_list):
        result_list.append(item1 + item2)
    print(f"Сумма коэффициентов полиномов = {result_list}")
    result_string = create_polynomial(length - 1, result_list)
    return result_string


def poly_coef_list(length, poly): # Создаем список коэффициентов по строке полинома
    coef_string = poly[:-4]
    list_elem = coef_string.split(" + ")
    result_list = [0 for i in range(length)]
    for item in list_elem:
        index_x = item.find("x")
        index_curr_power = item.find("^")
        if index_x == -1:
            result_list[0] = int(item)
        elif index_x == len(item) -1:
            result_list[1] = 1 if index_x == 0 else int(item[:index_x - 1])
        elif index_x == 0:
            result_list[int(item[index_curr_power+1:])] = 1
        else:
            result_list[int(item[index_curr_power+1:])] = int(item[:index_x - 1])
    result_list.reverse()
    #print(result_list)
    return result_list


path1 = "polynom1.txt"
path2 = "polynom2.txt"

poly1 = export_from_file(path1)
poly2 = export_from_file(path2)
print(poly1)
print(poly2)

sum_polynomials = add_poly_coef_list(poly1, poly2)
print(f"Итоговый полином = {sum_polynomials}")

