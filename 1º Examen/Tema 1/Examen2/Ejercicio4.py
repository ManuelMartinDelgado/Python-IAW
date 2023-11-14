# =============================================================================
# Ejercicio 4. 
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su 
# nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el 
# programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# =============================================================================


lista=[]

continuar=True

numeroAlumno=input("Dame el numero de alumno: ")
nombreAlumno=input("Ingresa el nombre del alumno: ")

while continuar:
    nota=int(input("nota del alumno: "))
    if nota < 0 :
        break
        print(lista)
    else:
        lista.append(nota)
        print(lista)
        continuar=input("¿Quieres añadir mas notas? si/no: ") == "si"

