# Дан список чисел. Создать список в который попадают числа, описывающие 
# возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]


from itertools import combinations


def find_max_increase_sequence(lst):
    for border in range(len(lst), 2, -1):
        for item in combinations(lst, border):
            if check_increase(item):
                return item


def check_increase(cort: tuple):
    lst = list(cort)
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    
    return True


first_list = [1, 5, 2, 3, 4, 6, 1, 7]
second_list = [5, 2, 3, 4, 6, 1, 7]
third_list = [1, 9, 2, 8, 3, 7, 4, 6, 5]
forth_list = [1, 2, 3, 4, 5]
print(find_max_increase_sequence(first_list))
print(find_max_increase_sequence(second_list))
print(find_max_increase_sequence(third_list))
print(find_max_increase_sequence(forth_list))

