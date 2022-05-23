# Написать программу получающую набор произведений чисел от 1 до N

def factorial(n):
    product = []
    num = 1
    for i in range(1, n + 1):
        num *= i
        product.append(num)
    
    return product

spisok = factorial(5)
print(spisok)