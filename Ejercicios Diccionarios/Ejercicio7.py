# =============================================================================
# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El 
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que 
# el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y 
# el coste total, con el siguiente formato
# Lista de la compra
# Artículo 1 Precio
# Artículo 2 Precio
# Artículo 3 Precio
# … …
# Total Coste
# =============================================================================


cesta_de_compra = {}

while True:
    
    articulo = input("Ingresa el nombre del artículo (o 'terminar' para finalizar): ")
    
    if articulo.lower() == 'terminar':
        break
    
    try:
        precio = float(input("Ingresa el precio del artículo: "))
    except ValueError:
        print("El precio ingresado no es válido. Introduce un número válido.")
        continue

    cesta_de_compra[articulo] = precio


print("Lista de la compra")
total_coste = 0

for articulo, precio in cesta_de_compra.items():
    print(f"{articulo} {precio}")
    total_coste += precio

print(f"Total Coste: {total_coste}")