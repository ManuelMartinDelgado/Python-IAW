# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:59:06 2023

@author: farol
"""

insertar = True
lista = []

while (insertar):
    palabra = str(input("Dame una palabra: "))
    lista.append(palabra)
    insertar = input("Quiere introducir más palabras (SI/NO): ") == "SI"
    
mayor = 0
palabraMayor = ""
for i in lista:
    if (len(i) > mayor):
        mayor = len(i)
        palabraMayor = i

print ("La palabra mayor es: ", palabraMayor)