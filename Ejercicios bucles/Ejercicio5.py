#EJERCICIO 5:
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual 
#y el numero de años, y muestre por pantalla el capital obtenido en la inversion cada 
#año que dura la inversion.

# Solicitar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
num_anos = int(input("Ingrese el número de años: "))

# Convertir la tasa de interés anual a una fracción
tasa_interes = tasa_interes_anual / 100

# Calcular el capital obtenido en la inversión cada año
for año in range(1, num_anos + 1):
    capital_obtenido = cantidad_invertir * (1 + tasa_interes)
    print(f"Año {año}: Capital obtenido = {capital_obtenido:.2f}")
    cantidad_invertir = capital_obtenido  # Actualizar la cantidad invertida para el próximo año
