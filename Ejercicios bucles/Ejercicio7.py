#EJERCICIO 7:
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
#correcta.

contrasena_correcta = "123"

while True:
    contrasena_ingresada = input("Ingrese la contrase�a: ")
    if contrasena_ingresada == contrasena_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Int�ntelo de nuevo.")
