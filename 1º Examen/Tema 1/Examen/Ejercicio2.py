# =============================================================================
# EJERCICIO 2. 
# Escribe un programa que pida al usuario números y los ingrese en una lista hasta 
# que el usuario indique que no quiere introducir más números. Posteriormente, pregunte al 
# usuario por un número y cuente cuantas veces está el número en esta lista.
# Un ejemplo de salida sería: “El numero X aparece Y veces”
# =============================================================================



lista=[]

continuar=True

while continuar:
    n=input("Ingrese un numero: ")
    lista.append(n)
    continuar=input("Continuar?: si/no: ") == "si"
    print(lista)
    
    
    
cuenta=int(input("Que numero quiere contar?: "))

contar=0

for x in lista:
    if len(x) == cuenta:
        print=(f'El numero {x} aparece {cuenta} veces')
    else:
        contar += cuenta