# =============================================================================
# Ejercicio 2. 
# Crea un programa que pida al usuario un número de mes (por ejemplo, el 4) y diga 
# cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas.


nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


dias_por_mes = [
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
]
numero_mes = int(input("Dame un número de mes (1-12): "))

if numero_mes >= 1 and numero_mes <= 12:
    nombre_mes = nombres_meses[numero_mes - 1]
    dias = dias_por_mes[numero_mes - 1]
    print(f"EL mes {nombre_mes} tiene {dias} días.")
else:
    print("""Intentalo de nuevo el número de mes es invalido. 
          Debe estar en el rango de 1 a 12.""")

