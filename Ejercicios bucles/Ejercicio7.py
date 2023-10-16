#EJERCICIO 7:
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
#correcta.

# Definir la contrase�a
contrasena_correcta = "contrasena123"

# Solicitar al usuario que ingrese la contrase�a
while True:
    contrasena_ingresada = input("Ingrese la contrase�a: ")

    # Comprobar si la contrase�a ingresada es la correcta
    if contrasena_ingresada == contrasena_correcta:
        print("�Contrase�a correcta! Acceso concedido.")
        break  # Salir del bucle si la contrase�a es correcta
    else:
        print("Contrase�a incorrecta. Int�ntelo de nuevo.")
