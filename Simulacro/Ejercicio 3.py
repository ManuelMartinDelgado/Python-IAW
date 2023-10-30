# =============================================================================
# Escribir un programa que pida palabras al usuario, 
# los meta en una lista y además le pida un entero y 
# muestre todas las palabras que su longitud es mayor a ese entero. (tiempo max 10 minutos)
# =============================================================================





lista = []

continuar = True

while continuar:
    
    palabra= input("añade palabra: ")
    lista.append(palabra)
    continuar= input("continuar? si/no: ") =="si"
    
n=int(input('numero entero: '))

for x in lista:
    if (len(x) > n): 
        
        
        print(f"la {x} es mayor a {n}")
    else:
        print("no es mayor")


















































# =============================================================================
# lista=[]
# 
# confirmar = True
# 
# while confirmar:
#     palabra = input("Añade un palabra: ")
#     lista.append(palabra)
#     confirmar = input("Quieres seguir añadiendo palabras si/no: ") == 'si'
# numero= int(input("Elige un numero: "))
#     
#     
# 
# for palabra in lista:
#     
#    if len(palabra) > numero:
#        
#     print(palabra)
#     
# Exception(print("No existen palabras"))
# =============================================================================
    