#EJERCICIO 7:
#Escribir un programa que almacene la cadena de caracteres contrase√±a en una 
#variable, pregunte al usuario por la contrase√±a hasta que introduzca la contrase√±a 
#correcta.

contrasena_correcta = "123"

while True:
    contrasena_ingresada = input("Ingrese la contraseña: ")
    if contrasena_ingresada == contrasena_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Inténtelo de nuevo.")
