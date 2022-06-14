# Вычислить число c заданной точностью d
# Пример: при d = 0.001=>  c= 3.141


from decimal import Decimal


# ряд Нилаканта   π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)
# без использования Decimal вычисляет точно только до 14 знака включительно
to_round = 0.00000000000000000001 # 20 знаков
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
# -> 3,14159265358979323846 ... 
# Количество операций превышает уже 7 миллионов. С каждой дополнительной единицей точности
# количество операций увеличивается в 2 с небольшим раза
# Для 26 знака количество операций достигает порядка 1.4 млрд и занимает больше 1 часа времени
print(f"число Пи с точностью до {to_round} = {pip}, количество операций = {i - 2}")
