# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15] 


import math


def multiply_pairs(num_list):
    length = len(num_list)
    result_list = []
    for i in range(math.ceil(length/2)):
        result_list.append(num_list[i] * num_list[length - i -1])
    return result_list


number_list = [2, 3, 4, 5, 6]
print(multiply_pairs(number_list))
number_list = [2, 3, 5, 6]
print(multiply_pairs(number_list))

