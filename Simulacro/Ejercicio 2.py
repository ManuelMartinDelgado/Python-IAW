# =============================================================================
# Escribir un programa que pida palabras al usuario, los meta en una lista y 
# luego indique que palabra es la más larga. (tiempo max 10 minutos)
# =============================================================================


lista=[]

mayor= ""

continuar = True



while continuar:
    
    palabra=input("¿Que palabra quieres añadir?: ")
    lista.append(palabra)
    continuar=input('¿Quieres seguir añadiendo palabras?: Si/No: ') == "Si"
    print(lista)

palabra_mayor= max(lista, key=len)
    
    
print("La palabra más larga es: ", palabra_mayor)