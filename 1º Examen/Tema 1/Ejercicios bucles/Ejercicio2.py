#EJERCICIO 2:
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
#años que ha cumplido (desde 1 hasta su edad).

 
while True:

    try:
        edad=int(input("Edad actual: "))
    
        i=1
        while i <= edad:
            print (i)
            i+=1    
        break
    except ValueError:
        print("Vuelve a intentarlo")
        continue
        