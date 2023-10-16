#EJERCICIO 8:
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
#muestre por pantalla el número de veces que aparece la letra en la frase.

# Pedir al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1

# Mostrar el resultado
print(f"La letra '{letra}' aparece {contador} veces en la frase.")
