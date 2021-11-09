# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:18:32 2021

@author: sroqu
"""

def programa2():
    print("Programa que identifica el tipo de dato de un valor ingresado por el usuario\n")
    print("Se realizaran cinco interacciones\n")
    
    for n in range(5) :                         #automatizar las interacciones 
        a=n+1                                   #cambiar a valores enteros positivos 
        print(f"interacción {a}")               #imprimir mensaje 
        b=input("ingrese un valor cualquiera: ")#imprimir mensaje     
        print("\neste tipo de dato en Python es: ",type(b),"\n")
        if n==4:                                #imprimir mensaje de salida del código
            print("No se harán más interacciones")
    return