# =============================================================================
# Escribir un programa que cree un diccionario vacío y 
# lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
# =============================================================================


diccionario={}

confirmacion=True


while confirmacion:
   clave= input("Que dato quiere añadir?: ")
   valor= input(clave + ":")
   diccionario[clave]= valor
   print(diccionario)
   
   confirmacion=input("Desea añadir mas datos si/no: ") == "si"
   
   
   
    