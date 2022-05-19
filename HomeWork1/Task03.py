# Написать программу получающую набор произведений чисел от 1 до N

def factorial(n):
    kakoiToSpisok = []
    num = 1
    for i in range(1, n + 1):
        num *= i
        kakoiToSpisok.append(num)
    
    return kakoiToSpisok

spisok = factorial(5)
print(spisok)