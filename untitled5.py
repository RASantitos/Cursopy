# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#creación de funciones 
#función que no tenga argumentos ni que devuelva ningún valor, solo 
#presente un mensaje 

#def mostrar():
#    """Documentación de la función """
#    print("Mensaje de prueba de función")
#    return

#mostrar()

#La misma función pero con una entrada. 

#def mostrar_nombre(nom1):
#    """Documentación de la función 
#    Lineas adicionales de explicación"""
#    print(f"Buenos días ,{nom1.upper()}")
#    return 

#mostrar_nombre("Juan")
#mostrar_nombre("Manuel")
#mostrar_nombre("Pedro")
#mostrar_nombre("carlos")

#def datos(nombre,apellido,edad):
#    """Declarar nombre y apellido como string y edad como int"""
#    print(f"Nombre: {nombre.title()}\nApellido: {apellido.title()}\nEdad: {edad}")
#    return 

#datos("andres","javier",32)

#Escribir un programa basado en una función que permita validar que el argumento 
#ingresado a la función es un string, caso contrario que muestre en pantalla 
#un mensaje indicando que no es un string. 

#def validstr(param1):
#    """Esta función valida que lo ingresado sea un str"""
#    if isinstance(param1,str):
#        print("Es string")
#        return
#   elif isinstance(param1,int):
#        print("es un entero")
#        return
#    else:
#        print("Es otro argumento ")
#        return
    
#def validstring(string1):
#    if type(string1)==str:
#        print("es string")
#        return
#    elif type(string1)==int:
#        print("es entero")
#        return
#    else:
#        print("es otro argumento")
#        return

#def datos(nombre,apellido,edad=0):
#    print(f"nombre: {nombre}\napellido: {apellido}\nedad: {edad}")
#    return
 
#función que haga la suma de tres numeros 

#def adicion(num1,num2,num3):
#    total=num1+num2+num3 #esta variable tiene sentido solo en dentro de la función 
#    return total         #devuelve la variable total al código

#print(adicion(2,12,25))
    
def construccion(nombre,apellido):
     return f"Nombre: {nombre.title()}, Apellido {apellido.title()}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    