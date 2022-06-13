# Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет, является ли этот день выходным


def check_weekend(number_day):
    if number_day == 6 or number_day == 7:
        return "Weekend"
    elif 0 < number_day < 6:
        return "Workday"
    else:
        return "There is no such day"


print(check_weekend(6))
print(check_weekend(3))
print(check_weekend(0))
print(check_weekend(int(input())))