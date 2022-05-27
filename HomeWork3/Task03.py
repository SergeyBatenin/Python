# Cоставить список простых множителей натурального числа N

number = 65343
divider = 2
lst = []

while number > 0 and divider <= number:
    if number % divider == 0:
        lst.append(divider)
        number = number // divider
    else:
        divider +=1

print(lst)