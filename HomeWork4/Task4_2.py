# Cоставить список простых множителей натурального числа N


from math import sqrt


def find_simple_mul(number):
    divider = 2
    lst = []
    while number > 0 and divider <= number:
        if number % divider == 0:
            lst.append(divider)
            number = number // divider
        else:
            divider +=1
    return lst


number = 65343
print(find_simple_mul(number), number) # 3, 23, 947