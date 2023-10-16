#EJERCICIO 9:
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
#una a una las letras de la palabra introducida empezando por la última+

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Recorrer la palabra en reversa e imprimir las letras
for letra in palabra[::-1]:
    print(letra)
