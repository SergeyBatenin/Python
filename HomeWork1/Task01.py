# Сформировать список из N членов последовательности.
# Для N=5: 1, -3, 9, -27, 81

def numbers_list(n):
    if n < 0:
        return []
    
    result = []
    for i in range(0, n, 1):
        result.append(((-3) ** i))
    
    return result

num_list = numbers_list(5)
print(num_list)

num_list = numbers_list(-1)
print(num_list)