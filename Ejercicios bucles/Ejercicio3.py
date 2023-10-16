#EJERCICIO 3:
#Escribir un programa que pida al usuario un n√∫mero entero positivo y muestre por 
#pantalla todos los n√∫meros impares desde 1 hasta ese n√∫mero separados por comas.

numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    impares = ""
    for i in range(1, numero + 1):
        if i % 2 != 0:  
            if impares:
                impares += ", "
            impares += str(i)

    print("Números impares desde 1 hasta", numero, ":", impares)
