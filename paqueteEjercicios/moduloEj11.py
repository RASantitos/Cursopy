# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:04:10 2021

@author: sroqu
"""

def programa1():
    print("Realizado por: Roque Santos")        #imprimir el mensaje en pantalla
    print("consultando los tipos de valores")   #imprimir el mensaje en pantalla 
    a=875                                       #inicializar una variable a
    b=4.89                                      #inicializar una variable b
    c="Now is better than never"                #inicializar una variable c
    d=1.32                                      #inicializar una variable d
    e=5+8j                                      #inicializar una variable e
    f=8.2                                       #inicializar una variable f
    g="Readabllity counts"                      #inicializar una variable g
    print(f"El tipo de dato {a} es\n", type(a)) #imprimar mensaje y tipo de dato
    print(f"El tipo de dato {b} es\n", type(b)) #imprimar mensaje y tipo de dato
    print(f"El tipo de dato {c} es\n", type(c)) #imprimar mensaje y tipo de dato
    print(f"El tipo de dato {d} es\n", type(d)) #imprimar mensaje y tipo de dato
    
    print(f"el valor {e} es un valor entero?\n")#imprimar mensaje    
    if type(e)==int:                            #comparar el tipo de dato de e
        print("si")                             #responder la pregunta 
    else:
        print("no")                             #responder la pregunta 
    print(f"el valor {f} es un valor entero?\n")#imprimir mensaje 
    if type(f)==int:                            #comparar el tipo de dato de f
        print("si")                             #responder la pregunta 
    else: 
        print("no")                             #responder la pregunta
    print(f"el texto {g} es un valor entero?\n")#imprimir mensaje 
    if type(g)==str:                            #comparar el tipo de dato de g
        print("si")                             #responder la pregunta 
    else:
        print("no")                             #responder la pregunta 
    return 