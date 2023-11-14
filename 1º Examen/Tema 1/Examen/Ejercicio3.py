# =============================================================================
# EJERCICIO 3. 
# Escribe un programa que pida al usuario un carácter y devuelva si es una vocal o 
# no. Se ha de comprobar mayúsculas y minúsculas
# Un ejemplo de salida sería: 
#     “El carácter X no es una vocal” o “El carácter X sí es una vocal”
# =============================================================================



listaVocales=['a','e','i','o','u']


caracter=input("Escribe un caracter: ")

if caracter == caracter in listaVocales:
    print(f'El carácter {caracter} es una vocal')
else:
    print(f'El carácter {caracter} no es una vocal')