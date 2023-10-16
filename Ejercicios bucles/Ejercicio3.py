#EJERCICIO 3:
#Escribir un programa que pida al usuario un número entero positivo y muestre por 
#pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingrese un n�mero entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un n�mero entero positivo.")
else:
    impares = ""
    for i in range(1, numero + 1):
        if i % 2 != 0:  
            if impares:
                impares += ", "
            impares += str(i)

    print("N�meros impares desde 1 hasta", numero, ":", impares)
