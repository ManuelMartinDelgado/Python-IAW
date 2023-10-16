#EJERCICIO 6:
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# Iterar a través de los números del 1 al 10
for i in range(1, 11):
    # Imprimir el encabezado de la tabla
    print(f"Tabla de multiplicar del {i}:")

    # Calcular y mostrar la tabla de multiplicar del número actual (i)
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

    # Agregar una línea en blanco entre las tablas
    print()
