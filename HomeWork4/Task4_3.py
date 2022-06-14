# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

def find_unique_elements(lst):
    result = []
    for item in lst:
        if not item in result:
            result.append(item)
    return result

original_list = [1, 2, 3, 5, 1, 5, 3, 10]
#result_list = set(original_list)
result_list = find_unique_elements(original_list)
print(result_list)