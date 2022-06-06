# Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию.

from random import randint


def create_file_with_random_numbers(count_numbers, min_value, max_value):
    with open ("numbersFile.txt", 'w') as data:
        for x in range(count_numbers):
            data.writelines(f"{randint(min_value, max_value)} ")


def create_file_with_sorted_numbers(path):
    with open (path, 'r') as data:
        lst = list(map(int, data.read().strip().split(" ")))
    print(f"base data file: {lst}")
    sorted_list = sorting_list(lst)
    print(f"sorted data file: {sorted_list}")
    with open ("numbersFile.txt", 'w') as data:
            data.writelines(" ".join(map(str, sorted_list))) # Какой вариант лучше использовать?
            #data.writelines((str(line) + " ") for line in sorted_list)


def sorting_list(lst):
    srt_lst = lst
    length = len(srt_lst)
    for i in range(length - 1):
        min_element = srt_lst[i]
        min_index = i
        for j in range(i + 1, length):
            if srt_lst[j] < min_element:
                min_element = srt_lst[j]
                min_index = j
        
        srt_lst[i], srt_lst[min_index] = srt_lst[min_index], srt_lst[i]
    return srt_lst


create_file_with_random_numbers(10, -10, 10)
path = "numbersFile.txt"
create_file_with_sorted_numbers(path)

