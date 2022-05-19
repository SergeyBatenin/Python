# Подсчитать сумму цифр в вещественном числе

def sumDigits(f):
    stroka = str(f)
    spisok = stroka.split(".")
    celayaChast = int(spisok[0])
    drobnayaChast = int(spisok[1])
    sum = 0
    while celayaChast > 0:
        sum = sum + (celayaChast % 10)
        celayaChast = int(celayaChast / 10)

    while drobnayaChast > 0:
        sum = sum + (drobnayaChast % 10)
        drobnayaChast = int(drobnayaChast / 10)
    
    return sum

summa = sumDigits(14523.43532656)
print(summa)