# =============================================================================
# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de 
# un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los 
# créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus 
# créditos. Al final debe mostrar también el número total de créditos del curso.
# =============================================================================



creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

total = 0

for asignatura, creditos in creditos.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total += creditos

print(f"El número total de créditos del curso es: {total}")




creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

total = 0

for asignatura in creditos:
    print(f"{asignatura} tiene {creditos[asignatura]} créditos")
    total += creditos.get(asignatura)

print(f"El número total de créditos del curso es: {total}")