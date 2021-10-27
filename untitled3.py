# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:18:40 2021

@author: sroqu
"""

#ejercicio de aplicación 

var1Ejercicios=input("ingrese productos de compras separados por comas: ")
var2=var1Ejercicios.split(",")
#print("\nvar1 {}, \nvar2{},\nvar3{},\nvar4{},\nvar5{}".format(var2[0],var2[1],var2[2],var2[3],var2[4]))

#otra solución 
var3=var1Ejercicios.replace(",","\n")
print(var3)