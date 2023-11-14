# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:03:05 2023

@author: farol
"""

insertar = True
lista = []

while (insertar):
    palabra = str(input("Dame una palabra: "))
    lista.append(palabra)
    insertar = input("Quiere introducir más palabras (SI/NO): ") == "SI"
    
    
    
enteroMayorQue = int(input("Dame un entero para comparar: "))

listaPalabrasMayores = []
for i in lista:
    if (len(i) > enteroMayorQue):
        listaPalabrasMayores.append(i)
        

print ("La palabra mayores que " , enteroMayorQue, "son: ", listaPalabrasMayores)