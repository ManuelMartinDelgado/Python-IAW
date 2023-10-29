# =============================================================================
# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
# ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
# mensaje informando de ello.
# Fruta                   Precio
# Plátano                 1.35
# Manzana                 0.80
# Pera                    0.85
# Naranja                 0.70
# =============================================================================



diccionario={"Plátano": float(1.35),'Manzana': float(0.80) ,'Pera':  float(0.85), "Naranja": float(0.70)}

n=input("Elige una fruta: ")
k=int(input("Cuantos kilos quiere: "))

if n in diccionario:
    cuenta=k*diccionario.get(n) 
    print("Precio de la compra: ", cuenta)
    
else:
    print("Elija otra fruta: ")
    
    

frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")




