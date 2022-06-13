# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def find_coords(quarter):
    if quarter == 1:
        return "X > 0, Y > 0"
    elif quarter == 2:
        return "X < 0, Y > 0"
    elif quarter == 3:
        return "X < 0, Y < 0"
    elif quarter == 4:
        return "X > 0, Y < 0"
    else:
        #return "The point is located on one or both coordinate axes"
        return "This quarter does not exist"


print(find_coords(1))
print(find_coords(2))
print(find_coords(3))
print(find_coords(4))
print(find_coords(0))