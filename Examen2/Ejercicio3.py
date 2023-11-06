# =============================================================================
# Ejercicio 3. 
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un 
# alumno. 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha 
# sacado y la menor.
# =============================================================================





notas = []

for i in range(5):
   nota = float(input(f"Ingrese la nota {i + 1}: "))
   notas.append(nota)

   print("Notas del alumno:")
   
for nota in notas:
     print(nota)
 

nota_media = sum(notas) / len(notas)
print(f"Nota media: {nota_media}: ")
 

nota_mas_alta = max(notas)

nota_mas_baja = min(notas)

print(f"Nota mas alta: {nota_mas_alta}")

print(f"Nota mas baja: {nota_mas_baja}")
