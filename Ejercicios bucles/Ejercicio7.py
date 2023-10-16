#EJERCICIO 7:
#Escribir un programa que almacene la cadena de caracteres contrase√±a en una 
#variable, pregunte al usuario por la contrase√±a hasta que introduzca la contrase√±a 
#correcta.

# Definir la contraseña
contrasena_correcta = "contrasena123"

# Solicitar al usuario que ingrese la contraseña
while True:
    contrasena_ingresada = input("Ingrese la contraseña: ")

    # Comprobar si la contraseña ingresada es la correcta
    if contrasena_ingresada == contrasena_correcta:
        print("¡Contraseña correcta! Acceso concedido.")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
