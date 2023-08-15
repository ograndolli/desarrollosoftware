"""Durante los 5 días de una semana se tomaron mediciones de temperatura en la ciudad. 
Se desea conocer cuál fue la temperatura promedio de la semana. 
Escriba un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario."""

temperaturas = []

total=0

for i in range(5):
    temperatura=float(input("Ingrese la temperatura: "))
    total=temperatura+total
    temperaturas.append(temperatura)
    

prom=(total/5)

print(f"\nEl promedio de las temperaturas ingresadas es: {prom}")
