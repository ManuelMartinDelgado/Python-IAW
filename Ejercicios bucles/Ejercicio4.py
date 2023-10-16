#EJERCICIO 4:
#Escribir un programa que pida al usuario un número entero positivo y muestre por 
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# Pedir al usuario un n�mero entero positivo
numero = int(input("Ingrese un n�mero entero positivo: "))

# Validar si el n�mero ingresado es positivo
if numero <= 0:
    print("Por favor, ingrese un n�mero entero positivo.")
else:
    # Inicializar una cadena vac�a para la cuenta regresiva
    cuenta_regresiva = ""

    # Iterar desde el n�mero ingresado hasta 0 (inclusive) en orden descendente
    for i in range(numero, -1, -1):
        if cuenta_regresiva:  # Agregar una coma si ya hay n�meros en la cadena
            cuenta_regresiva += ", "
        cuenta_regresiva += str(i)  # Agregar el n�mero a la cadena

    # Mostrar la cuenta regresiva
    print("Cuenta regresiva desde", numero, "hasta 0:", cuenta_regresiva)
