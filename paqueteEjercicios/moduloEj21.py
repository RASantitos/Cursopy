# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:13:04 2021

@author: sroqu
"""
def programa3():
    datos_2021=(15,20,3,91,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,16,15,1302)
    pares=[]
    impares=[]
    
    for i in datos_2021:
        #print(i)
        if i>110:
            print(f"{i} parece ser un valor atípico")
        elif i%2==0:
            pares.append(i)
        else: 
            impares.append(i)
    
    print(pares)
    print(impares)
    return   
        