# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:09:10 2021

@author: sroqu
"""
def programa5():
    def maximoList(a):
        b=a.values()
        b=list(b)
        altos=[]
        bajos=[]
        for i in b:
            if i>10:
                altos.append(i)
            else:
                bajos.append(i)
        #print(altos, bajos)
        return [altos,bajos]
    
    def maximoTupleList(a):
        b=a.values()
        b=list(b)
        bprim=[]
        n=0
        for i in b :
           for j in b[n]:
               bprim.append(j)
           n=n+1
        b=bprim
        altos=[]
        bajos=[]
        i=[]
        for i in b:
            if i>10:
                altos.append(i)
            else:
                bajos.append(i)
        #print(altos,bajos)
        return [altos,bajos]
    
    dic1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
    dic2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
    dic3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
    dic4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
    
    
    a=1
    
    while a!=2:
        a=input("Se debe eligir una de las opciones para que el programa\
          ejecute\nla selección se hace a través del número de la\
          opción\n1)Calculo de valores altos o bajos\
          \n2)salir\n")
        a=int(a)
        
        if a==2:
            break
        elif a==1:
            b=input("Elija una opción de diccionario.\nLa elección se hace con el número\
                  \n1){Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}\
                  \n2){tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}\
                  \n3{val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}\
                  \n4){lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}\n")
        
            #b=int(b)
            if b=="1":
                c=input("digite el número de valores altos que desea mostrar: ")
                d=input("digite el número de valores bajos que desea mostrar: ")
                c=int(c)
                d=int(d)
                x,y=maximoList(dic1)
                e=len(x)
                if c<=e:
                    print("Valores calculados en formato lista:",x[:c])
                else:
                    print("La longitud indicada no es correcta")
                if d<=e:
                    print("Valores calculados en formato tupla:",tuple(y[:d]))
                else:
                    print("La longitud indicada no es correcta")
            
            elif b=="2":
                c=input("digite el número de valores altos que desea mostrar: ")
                d=input("digite el número de valores bajos que desea mostrar: ")
                c=int(c)
                d=int(d)
                x,y=maximoTupleList(dic2)
                e=len(x)
                if c<=e:
                    print("Valores calculados en formato lista:",x[:c])
                else:
                    print("La longitud indicada no es correcta")
                if d<=e:
                    print("valores calculados en formato tupla:",tuple(y[:d]))
                else:
                    print("La longitud indicada no es correcta")
            
            elif b=="3":
                c=input("digite el número de valores altos que desea mostrar: ")
                d=input("digite el número de valores bajos que desea mostrar: ")
                c=int(c)
                d=int(d)
                x,y=maximoList(dic3)
                e=len(x)
                if c<=e:
                    print("Valores calculados en formato lista: ",x[:c])
                else:
                    print("La longitud indicada no es correcta")
                if d<=e:
                    print("Valores calculados en formato tupla: ",tuple(y[:d]))
                else:
                    print("La longitud indicada no es correcta")
            
            elif b=="4":
                c=input("digite el número de valores altos que desea mostrar: ")
                d=input("digite el número de valores bajos que desea mostrar: ")
                c=int(c)
                d=int(d)
                x,y=maximoTupleList(dic4)
                e=len(x)
                if c<=e:
                    print("Valores calculados en formato lista: ",x[:c])
                else:
                    print("La longitud indicada no es correcta")
                if d<=e:
                    print("Valores calculados en formato tupla: ",tuple(y[:d]))
                else:
                    print("La longitud indicada no es correcta")
            else: 
               print("no es un número válido")
        else:
             print("no es una opción váldia")
        return