def numero_mayor(num1, num2):
    mayor = 0
    if num1 > num2:
        mayor = num1
    elif num2 > num1:
        mayor = num2
    return mayor


numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))
print(numero_mayor(numero1, numero2))
