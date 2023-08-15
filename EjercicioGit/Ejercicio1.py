"""1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir

Elija una opción:"""


def suma(vu, vd):
    s=v1+v2
    return (s)

def resta(vu, vd):
    r=v1+v2

def multiplicacion(vu, vd):
    m=v1*v2
    return(m)

def division(vu, vd):
    d=v1/v2
    return (d)


opc=int(input("Elija una opcion: "))

while(opc!=7):
    if opc==1:
        v1=float(input("Ingrese el valor 1: "))
    if opc==2: 
        v2=float(input("Ingrese el valor 2: "))
    else: 
        print("Error")
    if opc==3: 
        s=suma(v1,v2)
    else: 
        print("Error")
    if opc==4:
        r=resta(v1, v2)
    else:
        print("Error")
    if opc==5:
        m=multiplicacion(v1, v2)
    else:
        print("Error")
    if opc==6:
        d=division(v1, v2)
    



