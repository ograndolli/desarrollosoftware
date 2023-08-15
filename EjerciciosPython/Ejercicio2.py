"""
Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos equivalen hoy los Bitcoins (BTC) 
que encontró guardados en un disco rígido viejo. El usuario del programa debe ingresar una cantidad en Bitcoins"""

btc=float(input("Ingrese la cantidad de bitcoins: "))

peso=8260873.61

tc=btc*peso

print(f"\nUsted tiene {tc} pesos")