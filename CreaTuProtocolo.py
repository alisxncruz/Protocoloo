import os

a=0
b=0

print('''

***Bienvenido a la maquina creadora de protocolos***

''')
def menu():
    print('''
._._._._._._._._._._._._
    Opciones
    1)Crear protocolo
    2)Agregar linea
    3)Eliminar
    4)Mostrar
._._._._._._._._._._._._
''')
menu()
elige=input("Desea elegir una opcion? s/n ")
if (elige == "N" or elige == "s" or elige == "S" or elige == "n"):

    print("Numero de opcion")
    while (elige == "s" or elige == "S"):
        opcion=int(input("Cual elige? "))
        
        if opcion == 1:
            print("___________________")
            name=input("Cual es el nombre de su protocolo? ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("Desea escribir las lineas? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print("____________")
                linea=input("Escriba la "+str(a)+"a linea: ")
                protocolo.write(str(a) +"-"+ linea + '''\n''')
                
                sub=input("Quiere que tenga otra subinstruccion? s/n")
                
                while (sub == "s" or sub=="S"):
                    b=b+1
                    subinstruccion=input("Escribala: ")
                    protocolo.write("    "+str(a)+"."+str(b)+subinstruccion+'''\n''')
                    sub=input("Quiere que tenga otra subinstruccion? s/n")
                    
                esc=input("Desea escribir la siguiente instruccion? s/n ")
            print("Terminamos gracias")
            protocolo.close()
            
        elif  opcion == 2:
            print("____________")
            
            name=input("Escriba el nombre del protocolo que quiere agregar la linea: ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("Desea agregar una linea? s/n ")
            while (esc == "s" or esc=="S"):

                num=int(input('Escriba el numero de paso que es:'))

                print("_______________")
                linea=input("Escriba la linea: ")
                protocolo.write(str(num) +"-"+ linea + '''\n''')
                
                sub=input("Quiere que tenga subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escribala: ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("Desea escribir la otra instruccion? s/n ")
            print("terminamos el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == 3:
            print("_____________")
            name=input("Escriba el nombre del protocolo que quiere borrar: ")
            os.remove(name + ".txt")
            print("SE HA BORRADO EL PROTOCOLO")
            
        elif  opcion == 4:
            print("______________")
            name=input("Escriba el nombre del protocolo que quiere ver: ")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()
       
        elige=input("Desea elegir una opcion? s/n ")
        if (elige=="s" or elige=="S"):
            continue
        else:
            break
    print("Hasta luego :)")
    
else:
    print("Gracias por su visita <3")
