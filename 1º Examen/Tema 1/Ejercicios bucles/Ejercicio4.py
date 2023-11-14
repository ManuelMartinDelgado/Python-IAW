#EJERCICIO 4:
#Escribir un programa que pida al usuario un n√∫mero entero positivo y muestre por 
#pantalla la cuenta atr√°s desde ese n√∫mero hasta cero separados por comas.
numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    cuenta_regresiva = ""
    
    for i in range(numero, -1, -1):
        if cuenta_regresiva:  
            cuenta_regresiva += ", "
        cuenta_regresiva += str(i)  
    
    print("Cuenta regresiva desde", numero, "hasta 0:", cuenta_regresiva)
    
    