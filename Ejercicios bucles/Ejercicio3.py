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

    
    
# Pedir al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar si el número ingresado es positivo
if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Inicializar una cadena vacía para almacenar los números impares
    impares = ""

    # Iterar desde 1 hasta el número ingresado (inclusive)
    for i in range(1, numero + 1):
        if i % 2 != 0:  # Si el número es impar
            if impares:  # Agregar una coma si ya hay números impares en la cadena
                impares += ", "
            impares += str(i)  # Agregar el número impar a la cadena

    # Mostrar la cadena de números impares
    print("Números impares desde 1 hasta", numero, ":", impares)
