# Найти сумму чисел списка стоящих на нечетной позиции
# Нечетная позиция(первый, второй, третий ...) => четный индекс


def sum_odd_indices(num_list):
    length = len(num_list)
    if length < 2:
        return 0
    sum = 0
    for i in range(0, length, 2):
        sum += num_list[i]
    return sum


number_list = [1, -2, 3, -4, -5, 6, -7, 8, 9]
print(sum_odd_indices(number_list))

