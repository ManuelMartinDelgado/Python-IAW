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

    
    
# Pedir al usuario un n�mero entero positivo
numero = int(input("Ingrese un n�mero entero positivo: "))

# Validar si el n�mero ingresado es positivo
if numero <= 0:
    print("Por favor, ingrese un n�mero entero positivo.")
else:
    # Inicializar una cadena vac�a para almacenar los n�meros impares
    impares = ""

    # Iterar desde 1 hasta el n�mero ingresado (inclusive)
    for i in range(1, numero + 1):
        if i % 2 != 0:  # Si el n�mero es impar
            if impares:  # Agregar una coma si ya hay n�meros impares en la cadena
                impares += ", "
            impares += str(i)  # Agregar el n�mero impar a la cadena

    # Mostrar la cadena de n�meros impares
    print("N�meros impares desde 1 hasta", numero, ":", impares)
