# =============================================================================
# EJERCICIO 5. 
# Adivine el número de 1 a 100. Escribe un programa que guarde un valor constante 
# en una variable llamada adivinaNumero. 
# Posteriormente pregunte al usuario que intente acertar el número. 
# Para cada intento se ha de indicar si el número guardado es mayor o menor 
# que el ingresado por el usuario. 
# Al final del programa, cuando acierte el número, se ha de indicar los intentos utilizados.
# Un ejemplo de salida sería: “Has acertado el número, te ha llevado X intentos
# =============================================================================


adivinaNumero=0


intento=input("Adivina el numero del 1 al 100: ")
if intento == adivinaNumero:
    print("Acertaste el numero")
else:
    print("intentalo de nuevo: ")
    adivinaNumero + 1
    