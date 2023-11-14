# =============================================================================
# Escribir un programa que pida enteros al usuario, los meta en una lista y luego muestre la suma de esos 
# elementos y la multiplicación de los elementos. (tiempo max 10 minutos)
# ===========================================================================


lista=[]

suma= 0
multi=1

continuar = True

while continuar:
    
    n=int(input("Escribe un entero wey: "))
    
    lista.append(n)
    
    continuar = input("Quieres añadir otro? si/no: ") == "si"
    print(lista)



for operacion in lista:
    
    suma += operacion 
    multi += operacion
    
    print(f"la suma es {suma} y la multiplicacion es {multi}")
















































# =============================================================================
# lista=[]
# continuar = True
# totalsum = 0
# totalmul = 1
# 
# 
# 
# while continuar:
# 
#     numero=float(input("¿Que numero quieres añadir?: "))
#     lista.append(numero)
#     continuar=input('¿Quieres seguir añadiendo numeros?: Si/No: ') == "Si"
# 
# for x in lista:
#     totalsum += x
#     totalmul *= x
# 
#     print('Total Suma: %.2f'%totalsum,'Total Multiplicación: ', totalmul)
# 
# 
# =============================================================================
