# Реализуйте алгоритм перемешивания списка


from copy import copy
from random import randint


def shuffle_lst(lst):
    copy_lst = copy(lst)
    length = len(lst)
    for i in range(length):
        temp_index = randint(0, length)
        copy_lst[i], copy_lst[temp_index] = copy_lst[temp_index], copy_lst[i]
    print(lst)
    print(copy_lst)


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle_lst(lst)

