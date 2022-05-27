# Найти НОК двух чисел

from itertools import product


def find_LCM(first_num, second_num):    
    return int((first_num * second_num) / find_GCD(first_num, second_num))

def find_GCD(num_first, num_second):
    num_first, num_second = max(num_first, num_second), min(num_first, num_second)
    while num_second != 0:
        num_first, num_second = num_second, num_first % num_second
    return num_first

first = 32
second = 20
print(find_LCM(first, second))