# =============================================================================
# Escribir un programa que pida enteros al usuario, los meta en una lista y luego muestre la suma de esos 
# elementos y la multiplicación de los elementos. (tiempo max 10 minutos)
# =============================================================================

lista=[]
continuar = True
totalsum = 0
totalmul = 1



while continuar:

    numero=int(input("¿Que numero quieres añadir?: "))
    lista.append(numero)
    continuar=input('¿Quieres seguir añadiendo numeros?: Si/No: ') == "Si"

for x in lista:
    totalsum += x
    totalmul *= x

    print('Total Suma: ',totalsum,'Total Multiplicación: ', totalmul)