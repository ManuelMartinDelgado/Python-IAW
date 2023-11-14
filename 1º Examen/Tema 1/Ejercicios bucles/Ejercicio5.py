#EJERCICIO 5:
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual 
#y el numero de a–ños, y muestre por pantalla el capital obtenido en la inversion cada 
#añ–o que dura la inversion.



amount=(input("Inversion"))
intereses=(input("interes"))
years= (input("años"))
for i in range (years):
    amount*=1 +intereses /100 
    print ("Capital tras"+ str(i+1)+"años: " + str(round(amount, 2)))