# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def negofibonacci(k):
    result = [0]
    first_element = 1
    second_element = 1
    for i in range(k):
        result.append(first_element)
        if i % 2 == 0:
            result.insert(0, first_element)
        else:
            result.insert(0, -first_element)
        first_element, second_element = second_element, first_element + second_element
    print(result)



k = 8
negofibonacci(k)

