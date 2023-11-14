# =============================================================================
# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
# 'Yen':'Y'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de 
# aviso si la divisa no está en el diccionario.
# =============================================================================
diccionario={"Euro":"€",'Dollar':'$','Yen':'Y'}

n=input("Elija una divisa: ")
if n=="Euro" or n=="Dollar" or n=="Yen" in diccionario:
    print("Su divisa es: ",diccionario.get(n))
else:
    print("La divisa elegida no es encontrada")