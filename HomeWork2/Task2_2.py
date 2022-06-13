# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Немного непонятное условие, в описании задачи написан список
# в Образце представлен словарь... Хотя формула там вообще 3n + 1
# Написал через оба варианта


def sum_list(number):
    result = []
    sum = 0
    for i in range(1, number + 1):
        temp = (1 + 1 / i) ** i
        result.append(temp)
        sum += temp
    print(result)
    print(sum)


def sum_lst(number):
    result = {}
    sum = 0
    for i in range(1, number + 1):
        temp = 3 * i + 1
        result[i] = temp
        sum += temp
    print(result)
    print(sum)


sum_list(4)
sum_lst(4)

