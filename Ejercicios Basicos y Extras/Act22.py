# Ejercicio 2.22
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre
# por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase = input("Introduce una frase: ")
palabra = input("Introduce una palabra: ")
print(frase.replace(palabra, palabra.upper()))
