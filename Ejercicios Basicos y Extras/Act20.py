# Ejercicio 2.20
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del
# país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un
# número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
def aislar_numero_tlf(numero_completo):
    numero_aislado = numero_completo.split("-")[1]
    return numero_aislado


numeroTelefono = str(input("Introduce un numero con prefijo y extension: "))
print("El numero aislado es:", aislar_numero_tlf(numeroTelefono))
