"""Un club deportivo tiene 4 categorías de asociados según la edad:

infantiles (desde 13 a 15 años)
cadetes (a partir de los 15 y hasta 17)
juveniles (desde los 17 hasta los 19)
mayores (de 19 años en adelante)

Escriba un programa que permita al usuario ingresar el nombre y la edad de un socio y
 muestre su el nombre de la categoría en la que le corresponde estar."""

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

if edad>=13 and edad<15:
    cat="Infantil"

elif edad>=15 and edad<17:
    cat="Cadete"

elif edad>=17 and edad<19:
    cat="Juvenil"
else:
    cat="Mayor"

print(f"\n{nombre} esta asignado a la categoria: {cat}")


