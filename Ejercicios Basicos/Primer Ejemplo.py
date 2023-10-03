
def puedoComprar (dineroQueTengo, precioProducto):

   

    if (dineroQueTengo >= precioProducto):
        print("Puedes comprar el producto")
        
    else: 
        print("No puedes comprar el prodcuto")
        
    print ("FIN")
    
dineroQueTengo =int(input("¿Cuanto dinero tengo?: "))

precioProducto=int(input ("¿Cuanto vale el producto?:"))

puedoComprar(dineroQueTengo, precioProducto)


num1= int(input("Numero 1: "))
num2= int(input("Numero 2: "))
num3= int(input("Numero 3: "))

if (num1>num2 and num1>num3):
    print("El valor mayor es: ", num1)
else:
    print("No es mayor")