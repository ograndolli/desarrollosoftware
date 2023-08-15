"""
LISTA 

Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:

Muestre la lista
El usuario ingresa debe ingresar un valor. El programa debe informar cuántos valores de la lista son mayores 
a dicho valor, para eso debe utilizar una función. 
La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores
de la lista mayores a dicho entero.

Crear una función que calcule el promedio de la lista y utilizarla.
Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne."""

import random



def generar_lista():
    lista = []
    for i in range(10):
        numero = random.randint(1,20)
        lista.append(numero)
    return lista

def contar_mayor(lista, v0):
    cont=0
    for i in lista:
        if i>v0:
            cont+=1
    return cont
 
def mayor_numero(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def menor_numero(lista):
    menor=20
    for i in lista:
        if i<menor:
            menor=i
    return menor


def promedio(lista):
    suma=0
    for i in lista:
        suma=suma+i
    prom=suma/len(lista)
    return prom
    

#ingreso 

valor=int(input("\nIngresar un valor: "))


#funciones

lista = generar_lista()
print("\nLa lista es: ")
print(lista)


cm = contar_mayor(lista, valor)
print(f"\nLa cantidad de valores mayores a {valor} son: {cm}")


ma= mayor_numero(lista)
print(f"\nEl elemento mayor de la lista es: {ma}")


me = menor_numero(lista)
print(f"\nEl elemento menor de la lista es: {me}")


pro = promedio(lista)
print(f"\nEl promedio de la lista es: {pro} \n")



        

