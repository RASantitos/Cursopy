# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:59:51 2021

@author: sroqu
"""
def programa4():
    a=input("Debera ingresar una contraseña\nla contraseña debe contener mínimo 5 caracteres\
             \ny máximo 15 caracteres.\
             \ndebe contener al menos un letra minúscula entre las letras:\
             \na, b, c, d, e, f, g, h, i, j\
             \ndebe contener al menos una letra mayúsucla entre las letras:\
             \nK, L ,M, N, O, P, Q, R, S, T\
            \ndebe contener al menos un número entre 0 y 9\
            \ndebe contener un símbolo entre $, %, *,@\
            \ningrese la contraseña a continuación: ")
    a=list(a)
            
    con1=("a","b","c","d","e","f","g","h","i")
    con2=("K","L","M","N","O","P","Q","R","S","T")
    con3=("0","1","2","3","4","5","6","7","8","9")
    con4=("$","%","*","@")
    
    count=0
    
    for i in a:
        for j in con1:
            #print(i,j)
            if i==j:
                count=count+1
            else:
                count=count
    i=[]
    j=[]
    count2=0
    for i in a:
        for j in con2:
            #print(i,j)
            if i==j:
                count2=count2+1
            else:
                count2=count2
    
    i=[]
    j=[]
    count3=0
    for i in a:
        for j in con3:
            #print(i,j)
            if i==j:
                count3=count3+1
            else:
                count3=count3
                
    i=[]
    j=[]
    count4=0
    for i in a:
        for j in con4:
            #print(i,j)
            if i==j:
                count4=count4+1
            else:
                count4=count4
                
    if count>0:
        if count2>0:
            if count3>0:
                if count4>0:
                    print("Contraseña Aceptada")
                else:
                    print("Contraseña no válida\
                          \nfalta al menos uno de los simbolos: $, %, *,@\
                          \nel código no se ejecutará de nuevo")
            else:
                print("Contraseña no válida\
                          \nfalta al menos uno de los simbolos:0, 1, 2, 3, 4, 5, 6, 7, 8, 9\
                          \nel código no se ejecutará de nuevo")
        else:
            print("Contraseña no válida\
                   \nfalta al menos uno de los simbolos:K, L, M, N, O, P, Q, R, S, T\
                   \nel código no se ejecutará de nuevo")
    else:
        print("Contraseña no válida\
               \nfalta al menos uno de los simbolos:a, b, c, d, e, f, g, h, i, j\
                \nel código no se ejecutará de nuevo")
    return