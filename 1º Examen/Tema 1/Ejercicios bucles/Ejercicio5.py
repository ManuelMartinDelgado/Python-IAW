#EJERCICIO 5:
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual 
#y el numero de a��os, y muestre por pantalla el capital obtenido en la inversion cada 
#a�o que dura la inversion.



amount=(input("Inversion"))
intereses=(input("interes"))
years= (input("a�os"))
for i in range (years):
    amount*=1 +intereses /100 
    print ("Capital tras"+ str(i+1)+"a�os: " + str(round(amount, 2)))