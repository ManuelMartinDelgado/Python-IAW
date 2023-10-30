# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:54:16 2023

@author: farol
"""

insertar = True
lista = []

while (insertar):
    numero = int(input("Dame un numero: "))
    lista.append(numero)
    insertar = input("Quiere introducir más numeros (SI/NO): ") == "SI"
    
acumulaSuma = 0
acumulaMultiplicacion = 1
for i in lista:
    acumulaSuma = acumulaSuma + i
    acumulaMultiplicacion = acumulaMultiplicacion * i

print ("la suma es: ", acumulaSuma, "la multiplicacion es: ", acumulaMultiplicacion)
    
    
