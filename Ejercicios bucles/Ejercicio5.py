#EJERCICIO 5:
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual 
#y el numero de a�os, y muestre por pantalla el capital obtenido en la inversion cada 
#a�o que dura la inversion.

# Solicitar al usuario la cantidad a invertir, el inter�s anual y el n�mero de a�os
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
tasa_interes_anual = float(input("Ingrese la tasa de inter�s anual (en porcentaje): "))
num_anos = int(input("Ingrese el n�mero de a�os: "))

# Convertir la tasa de inter�s anual a una fracci�n
tasa_interes = tasa_interes_anual / 100

# Calcular el capital obtenido en la inversi�n cada a�o
for a�o in range(1, num_anos + 1):
    capital_obtenido = cantidad_invertir * (1 + tasa_interes)
    print(f"A�o {a�o}: Capital obtenido = {capital_obtenido:.2f}")
    cantidad_invertir = capital_obtenido  # Actualizar la cantidad invertida para el pr�ximo a�o
