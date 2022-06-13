# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
 
 
def factorial(n):
    product = []
    num = 1
    for i in range(1, n + 1):
        num *= i
        product.append(num)
    
    return product

mult_list = factorial(4)
print(mult_list)

