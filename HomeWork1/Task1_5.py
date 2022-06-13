# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве


import math


def find_distance(first_point, second_point):
    first_x = int(first_point[0])
    first_y = int(first_point[1])
    second_x = int(second_point[0])
    second_y = int(second_point[1])
    first_leg = abs(second_x - first_x)
    second_leg = abs(second_y - first_y)
    distance = math.sqrt(first_leg * first_leg + second_leg * second_leg)
    return distance


first_point = tuple(input("Enter the coordinates of the first point separated by a space\n").split())
second_point = tuple(input("Enter the coordinates of the second point separated by a space\n").split())
print(find_distance(first_point, second_point)) # (3, 6    2, 1) => 5.09
                                                # (7, -5   1, -1) => 7.21
