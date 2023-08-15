"""Franco está organizando un asado con sus amigos y necesita de tu ayuda. 
Para estimar cuánta carne necesita comprar, va a suponer que cada invitado come 0.7 Kg de carne. 
Ayuda a Franco escribiendo un programa que permita al usuario ingresar la cantidad de invitados y el precio de 1Kg.
de carne, y muestre cuántos Kg de carne en total debe pedir al carnicero y cuánto dinero necesita para pagar."""


invitados=int(input("\nIngrese la cantidad de invitados: "))
precio=float(input("Ingrese el precio del kg de carne: "))

totalcarne=invitados*0.7
preciototal=totalcarne*precio

print(f"\nFranco debe comprar {totalcarne:.2f} kg de carne y gastara {preciototal:.2f} pesos ")