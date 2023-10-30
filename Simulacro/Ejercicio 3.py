# =============================================================================
# Escribir un programa que pida palabras al usuario, 
# los meta en una lista y además le pida un entero y 
# muestre todas las palabras que su longitud es mayor a ese entero. (tiempo max 10 minutos)
# =============================================================================

lista=[]

confirmar = True

while confirmar:
    palabra = input("Añade un palabra: ")
    lista.append(palabra)
    confirmar = input("Quieres seguir añadiendo palabras si/no: ") == 'si'
numero= int(input("Elige un numero: "))
    
    

for palabra in lista:
    
   if len(palabra) > numero:
       
    print(palabra)
    
Exception(print("No existen palabras"))
    