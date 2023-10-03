#Requerir al usuario que ingrese un día de la semana en minusculas e imprimir un 
#mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje 
#diferente si es 
#sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia= input("Ingrese un di�a de la semana en MINÚSCULAS: ")

if (dia=="lunes"):
    print("Hoy es lunes :( ")
elif (dia=="viernes"):
    print("Viva los viernes")
elif (dia=="sabado" or dia=="domingo"):
    print("Hoy se duerme")
else:
    print ("Vuelva a intentarlo")
    