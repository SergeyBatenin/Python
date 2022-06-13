# В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from decimal import Decimal


def fractional_difference(f_list):
    min_fraction = 1
    max_fraction = 0
    for i in f_list:
        fraction = Decimal(str(i)) % 1
        if fraction == 0:
            continue
        if fraction > max_fraction:
            max_fraction = fraction
        if fraction < min_fraction:
            min_fraction = fraction
    # print(min_fraction)
    # print(max_fraction)
    return max_fraction - min_fraction


fraction_list = [1.1, 1.2, 3.1, 5, 10.01]
print(fractional_difference(fraction_list)) # 0.19

fraction_list = [1.1, 1.2, 3.1, 5.002, 10.01] # 0.198
print(fractional_difference(fraction_list))

