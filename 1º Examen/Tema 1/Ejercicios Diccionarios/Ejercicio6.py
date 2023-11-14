# =============================================================================
# # Ejercicio 6
# # Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
# # sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# # que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el 
# # contenido del diccionario.
# =============================================================================

# =============================================================================
# informacion_persona = {}
# 
# 
# claves = ['nombre', 'edad', 'sexo', 'teléfono', 'correo electrónico']
# 
# for clave in claves:
#    
#     valor = input(f'Por favor, ingresa el {clave} de la persona: ')
#     
#     informacion_persona[clave] = valor
#     
#     print('Información actual de la persona:')
#     for key, value in informacion_persona.items():
#         print(f'{key}: {value}')
# =============================================================================
    

persona = {}
continuar = True
while continuar:
     clave = input('¿Qué dato quieres introducir? ')
     valor = input(clave + ': ')
     persona[clave] = valor
     print(persona)
     continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
     

    
# =============================================================================
# datos_usuario={}
# 
# menu= """
# 1. Agregar datos
# 2. Salir 
# 
# """
# 
# while True:
#     print(menu)
#     opcion = int(input("¿Que quieres hacer?: "))
#     
#     if opcion == 1:
#         clave_2=input('¿Qué desea añadir: ?')
#         valor_2=input(clave_2 + ":")
#         datos_usuario[clave_2]= valor_2
#         print(datos_usuario)
#     else:
#         opcion = 2 
#         break
#         
# =============================================================================
