#EJERCICIO 3:
#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
#Considerar el caso en que ambos números son iguales.

Num1 = int( input("Primer Número: "))
Num2 = int( input("Segundo Número: "))

if (Num1<Num2):
    
    print("Mostrar " ,Num1)

elif (Num1==Num2):
    
    print("Son iguales")
    
else: 
    print("Mostrar",Num2)