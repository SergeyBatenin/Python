# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


def find_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y > 0:
        return 2
    elif x == 0 and y == 0:
        return "origin"
    elif x == 0:
        return "Ox"
    else:
        return "Oy"


print(find_quarter(3, 1))   # 1
print(find_quarter(3, -1))  # 4
print(find_quarter(-3, -1)) # 3
print(find_quarter(-3, 1))  # 2
print(find_quarter(0, 0))   # origin
print(find_quarter(0, 1))   # Ox
print(find_quarter(3, 0))   # Oy