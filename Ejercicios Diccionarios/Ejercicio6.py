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



personas={}
continuar=True
while continuar:
    clave=input(Q'ue datos quieres inroducir'')
    valor=input(clave + ':')
    persona[clave]=