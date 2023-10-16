#EJERCICIO 4:
#Escribir un programa que pida al usuario un n√∫mero entero positivo y muestre por 
#pantalla la cuenta atr√°s desde ese n√∫mero hasta cero separados por comas.

# Pedir al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar si el número ingresado es positivo
if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Inicializar una cadena vacía para la cuenta regresiva
    cuenta_regresiva = ""

    # Iterar desde el número ingresado hasta 0 (inclusive) en orden descendente
    for i in range(numero, -1, -1):
        if cuenta_regresiva:  # Agregar una coma si ya hay números en la cadena
            cuenta_regresiva += ", "
        cuenta_regresiva += str(i)  # Agregar el número a la cadena

    # Mostrar la cuenta regresiva
    print("Cuenta regresiva desde", numero, "hasta 0:", cuenta_regresiva)
