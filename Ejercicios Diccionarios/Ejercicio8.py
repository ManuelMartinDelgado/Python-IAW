# =============================================================================
# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario 
# introducirá las palabras en español e inglés separadas por dos puntos, y cada 
# par <palabra>:<traducción> separados por comas. El programa debe crear un 
# diccionario con las palabras y sus traducciones. Después pedirá una frase en español y 
# utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el 
# diccionario debe dejarla sin traducir.
# 
# =============================================================================



diccionario = {}
entrada = input("Ingresa las palabras en español e inglés separadas por dos puntos (:) y separadas por comas (,): ")


pares = entrada.split(',')

for par in pares:
    palabra, traduccion = par.split(':')
    diccionario[palabra.strip()] = traduccion.strip()


frase_espanol = input("Ingresa una frase en español: ")


palabras = frase_espanol.split()

frase_traducida = []

for palabra in palabras:
    traduccion = diccionario.get(palabra, palabra) 
    frase_traducida.append(traduccion)


frase_traducida = ' '.join(frase_traducida)
print("Frase traducida al inglés:", frase_traducida)



diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')