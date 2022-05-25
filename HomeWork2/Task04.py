# Написать программу преобразования десятичного числа в двоичное
def decimal_to_int(num):
    num_str = ""
    while num > 0:
        num_str = str(num % 2) + num_str
        num = num // 2

    return int(num_str)


number = 7
print(decimal_to_int(number))