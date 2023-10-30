# =============================================================================
# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo 
# guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene 
# <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
# =============================================================================


n=input("Escribe tú nombre: ")
e=int(input("Escribe tú edad: "))
d=input("Escribe tú dirección:")
t=input("Escribe tú tlfn:")

diccionario={"nombre": n,'edad': e ,'direccion': d, "tlfn": t}

print(f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en {diccionario['direccion']} y su número de teléfono es {diccionario['tlfn']}.")



