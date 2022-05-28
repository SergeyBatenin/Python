# Вычислить число c заданной точностью d
# Пример: при d = 0.001,  c= 3.1415926535

from decimal import Decimal
from math import trunc
import math

# ряд Нилаканта   π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)
# без использования Decimal вычисляет точно только до 14 знака включительно
to_round = 0.000000000000001
pip = Decimal(3)
i = 2
curr_round = to_round + 1
sign = Decimal(4)
while curr_round > to_round:  
    pip += sign / Decimal(i * (i + 1) * (i + 2))
    sign = -sign
    pip_next = pip + sign / Decimal(str((i + 2) * (i + 3) * (i + 4)))
    curr_round = abs(pip - pip_next)
    i += 2
print(pip, (i - 2))




# Я изначально понял условие задачи так. А вообще некорректные и кривые условия задач регулярная проблема
number = math.pi
to_round = 0.00001
count = 0

while to_round < 1:
    to_round *= 10
    number *= 10
    count +=1
print(trunc(number)/(10 ** count))

pip = Decimal("0")
for i in range(10 ** (count + 1)):
    pip += Decimal(str((-1) ** i)) / Decimal(str(2 * i + 1))
pip *= 4
print(pip, i)