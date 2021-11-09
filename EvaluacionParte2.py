# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:23:46 2021

@author: sroqu
"""

import paqueteEjercicios.moduloEj11 as Ej11
import paqueteEjercicios.moduloEj12 as Ej12
import paqueteEjercicios.moduloEj21 as Ej21
import paqueteEjercicios.moduloEj22 as Ej22
import paqueteEjercicios.moduloEj30 as Ej30

#opciones de ejecucion 
#1 ejecuta programa 1
#2 ejecuta programa 2
#3 ejecuta programa 3
#4 Ejecuta programa 4
#5 Salir 

opcion=1
cuentas=0
cuentas_tot=0

while opcion!=6:
        a=input("Seleccione una opción de ejecución\
              \n1) Ejecute un programa que genera varios mensajes en pantalla\
              \n2) Ejecute un programa que intenta determinar el tipo de dato ingresado\
              \n   por el usuario\
              \n3) Ejecuta un programa que separa valores pares e impares de una lista\
              \n4) Ejecuta un programa que valida una contraseña 4\
              \n5) Ejecuta un programa que clasifica un conjuto de valores de un\
              \n   de un diccionario\
              \n6) Salir de la ejecución \ningrese el número ")
        
        try:
            b=int(a)
            opcion=b
            if opcion==6:
                break
            elif opcion==1:
                Ej11.programa1()
            elif opcion==2:
                Ej12.programa2()
            elif opcion==3:
                Ej21.programa3()
            elif opcion==4:
                Ej22.programa4()
            elif opcion==5:
                Ej30.programa5()
            else:
                print("Debe escoger un número de 1 a 6")    
        except: 
              print("No es un dígito. Debes ingresar un dígito de 1 a 6")
        else:
           print("Escribiste un número")
           cuentas+=1
        finally:
           cuentas_tot+=1

print("El codigo se ejecuto correctamente ",cuentas," veces")
print("El codigo se ejecuto incorrectamente ",cuentas_tot - cuentas," veces")
print("El codigo se ejecuto en total ",cuentas_tot," veces")
