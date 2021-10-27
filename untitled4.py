# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:42:26 2021

@author: sroqu
"""

#edad=int(input("ingrese su edad como un número: "))
#if edad<18 :
#    print("menor de edad \n")
#elif edad>18 and edad <45 :
#    print("adulto joven")
#elif edad>45 and edad<60:
#    print("adulto") 
#else 75:
#    print("adulto mayor ")

#var1=1
#while var1<10:
#    print(var1)
#    var1+=1

#num=int(input("Escriba un número positivo: "))
#while num<0:
#    print("Número negativo, vuelva a un número positivo: ")
#    num=int(input("Escriba un número positivo: "))
#print("El número es correcto")

#usr_ing=""

#while usr_ing.lower()!="salir":
#    print(usr_ing)
#    usr_ing=input("Ingrese una o más palabras: ")
#else:
#    print("Programa terminado")

#control=True
#while control==True:
#    usr_ing=input("Ingrese una o más palabras: ")
#    if usr_ing.lower()=="salir":
#        break
#    print(usr_ing)
#print("Programa terminado")

#x=1
#while x<=10:
#    if x==5:
#       x+=1
#       continue
#    print(x)
#    x+=1

#for ch in range(1,6):
#    print("repeticion")
#    print(ch)


#lst=range(4)
#print(lst)

frase_larga=input("ingreso de la frase: ")
letra_bsq=input("Letra a contar")
cnt=0
for cntrl in frase_larga:
    if cntrl==letra_bsq: #cntrl adquiere el valor de cada posicion en frase_larga
        cnt+=1
print(cnt)



















