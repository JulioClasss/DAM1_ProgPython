# Ejercicio 2.23
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo
# electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
correo = input("Introduce tu correo electronico: ")
terminacion = "ceu.es"
nuevoCorreo = correo.split("@")[0] + "@" + terminacion
print("tu nuevo correo es:", nuevoCorreo)
