# Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  c= 3.14159265358979323846

from math import trunc

number= 3.14159265358979323846
to_round = 0.001
count = 0

while to_round < 1:
    to_round *= 10
    number *= 10
    count +=1

print(trunc(number)/(10 ** count))