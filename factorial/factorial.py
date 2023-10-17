def factorial(num):
    for i in range(num - 1, 0, -1):
        num *= i
    return num

numero = int(input("Introduce un numero: "))
print(factorial(numero))