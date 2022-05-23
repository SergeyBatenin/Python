# Подсчитать сумму цифр в вещественном числе

def sumDigits(f):
    if f == 0:
        return 0
    if f < 0:
        f = -f
    stroka = str(f)
    spisok = stroka.split(".")
    whole_part = int(spisok[0])
    fraction = int(spisok[1])
    sum = 0
    while whole_part > 0:
        sum = sum + (whole_part % 10)
        whole_part = whole_part // 10

    while fraction > 0:
        sum = sum + (fraction % 10)
        fraction = fraction // 10
    
    return sum

summa = sumDigits(-14523.43532656)
print(summa)