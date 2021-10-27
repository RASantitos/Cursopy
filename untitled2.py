# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:53:37 2021

@author: sroqu
"""

#Cadena_1="Palabra a resaltar: \"Prueba\""
#print("El siguiente es un número entero",
#      50,
#      "\nNúmero decimal",
#      78.92) #Esto es un ejemplo de romper la línea del 
             #código
var1="Texto1"
var2=643
var3=4.67
var4="Texto"
#trabajar para hacer un solo argumento
#para poder operar todas estas variables deben ser números 
#o todas deben ser strings 
#operación de concantenacion 

#print(var1+var2+var3+var4) #+ es un operador de concantenador 
                           #solo así se genera un error 
                           
#se va a cambiar el tipo dentro de la variable, dentro del 
#método. Declaración. Se hará uso de función constructura para
#cambiar el tipo de variable (siempre que sea posible)
#la base de la funcion constructura es el tipo de dato
#int float complex, etc 

#print(var1+str(var2)+str(var3)+var4) #aqui se han 
                                     #transformado var2 
                                     #y var3 en str
                                     
#creacion de fstring
#print(f"variable1: {var1*2}\nVariable2: {var2/var3}\nVariable3: {var3} \nVariable4: {var4}")
#solo con tipo f se puede mantener el tipo de variable en el argumento 
#\n se llama secuencia de escape 
#casos en que se construye un string y se almacena la variable para 
#procesarlo. En  analisis de datos, a veces, se requieren construir columnas en data
#frames, en donde se requiere operar las tablas. Se opera sobre la tabla 
#se crea a traves de una cadena f se crea el nombre de usuario. No necesita agregar 
#operaciones adicionales. Como en el ejemplo de la línea 23. El str no hace operaciones 
#con esas variables, las referencia con su valor y las tranforma 
#al tipo de variable directamente. 
#funcion keyword(<argument>)
#metodo.method
#print("Mi nombre es {}, mi apellido es {}, mi edad es{}".format("Roque","Santos",38))
#print("Mi nombre es {nombre}, mi apellido es {edad}, mi edad es{apellido}".format(nombre="Roque",apellido="Santos",edad=38))#los argumentos de format son}
#son los valores que se remplazan en las
                                                                  #llaves.
var_prueba="Mensaje de trabajo para pruebas" 
#print(var_prueba[-7:]) #si no se especifica el último valor con 
                       #en indices negativos, se presentarán todos los valores
                       
var_2=var_prueba.upper() #el método upper coloca todo en mayúsculas
var_3=var_prueba.lower()
var_4=var_prueba.replace("e","100")
var_5=var_prueba.split()

correo_prueba="emcorreoecu@hotmail.com"
var_6=correo_prueba.split("@")
print(var_6)

                                                                 