#Solicitar al usuario que ingrese tres numeros y mostrar cual es el mayor de los tres.

Num1 = int( input("Primer Número: "))
Num2 = int( input("Segundo Número: "))
Num3 = int( input("Tercer Número: "))

if (Num1>Num2 and Num1>Num3):
    print("El número mayor es ",Num1)

elif(Num2>Num1 and Num2>Num3):
    print ("El número mayor es ", Num2)
    
else:
    print("El número mayor es ", Num3)
